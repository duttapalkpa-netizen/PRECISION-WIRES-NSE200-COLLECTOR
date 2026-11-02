#!/usr/bin/env python3
"""Fail-closed, research-only raw evidence collector for Macro-Geo P0.

Input JSON schema:
{"sources":[{"group":"benchmark_index|sector_indices|volatility|geopolitical_events",
"name":"...","url":"https://official-host/path","expected_content_types":["text/csv"]}],
 "archived_pairs":[{"group":"...","name":"...","vintage_a_url":"...","vintage_b_url":"..."}]}
Only official domains are accepted. Every source is fetched twice; bytes, headers,
status and SHA-256 are retained. No source is promoted and no vintage is inferred.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, re, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ALLOWED = (".nseindia.com", ".niftyindices.com", ".pib.gov.in", ".mea.gov.in")
GROUPS = ("benchmark_index", "sector_indices", "volatility", "geopolitical_events")
UA = "PRECISION-WIRES-research-evidence-collector/1.0 (research-only; contact: none)"

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def host_ok(url: str) -> bool:
    p=urlparse(url)
    return p.scheme=="https" and any(p.hostname==d[1:] or p.hostname.endswith(d) for d in ALLOWED)
def fetch(url: str, timeout: int=45):
    if not host_ok(url): raise ValueError(f"URL_NOT_ALLOWLISTED: {url}")
    req=Request(url, headers={"User-Agent":UA,"Accept":"text/csv,application/json,text/html,application/pdf,*/*"})
    try:
        with urlopen(req, timeout=timeout) as r:
            body=r.read()
            return r.status, dict(r.headers.items()), body
    except HTTPError as e:
        return e.code, dict(e.headers.items()), e.read()
    except (URLError, TimeoutError) as e:
        raise RuntimeError(f"FETCH_ERROR {url}: {e}") from e

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config", required=True); ap.add_argument("--start-date", required=True)
    ap.add_argument("--end-date", required=True); ap.add_argument("--out", default="macro_geo_p0_raw_evidence")
    args=ap.parse_args()
    datetime.strptime(args.start_date,"%Y-%m-%d"); datetime.strptime(args.end_date,"%Y-%m-%d")
    if args.start_date>args.end_date: raise SystemExit("INVALID_DATE_RANGE")
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    sources=cfg.get("sources",[])
    if not sources: raise SystemExit("NO_SOURCES_CONFIGURED")
    seen={g:0 for g in GROUPS}
    for s in sources:
        if s.get("group") not in GROUPS or not s.get("name") or not host_ok(s.get("url","")):
            raise SystemExit(f"INVALID_SOURCE_CONFIG: {s}")
        seen[s["group"]]+=1
    missing=[g for g,n in seen.items() if n==0]
    if missing: raise SystemExit("P0_GROUPS_MISSING_SOURCES: "+",".join(missing))
    root=Path(args.out); raw=root/"raw"; raw.mkdir(parents=True,exist_ok=True)
    records=[]; drift=[]
    for i,s in enumerate(sources):
        for attempt in (1,2):
            if attempt==2: time.sleep(1.2)
            status,headers,body=fetch(s["url"])
            ct=headers.get("Content-Type",headers.get("content-type","")).split(";")[0].strip().lower()
            expected=[x.lower() for x in s.get("expected_content_types",[])]
            digest=sha(body)
            suffix={"text/csv":".csv","application/json":".json","text/html":".html",
                    "application/pdf":".pdf","application/zip":".zip"}.get(ct,".bin")
            name=re.sub(r"[^A-Za-z0-9_.-]+","_",s["name"])[:80]
            path=raw/f'{i:03d}_{name}_attempt{attempt}{suffix}'
            path.write_bytes(body)
            records.append({"group":s["group"],"name":s["name"],"url":s["url"],
                "attempt":attempt,"http_status":status,"content_type":ct,"bytes":len(body),
                "sha256":digest,"raw_path":str(path),"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
                "expected_content_types":expected,"content_type_match":(not expected or ct in expected),
                "http_ok":status==200,"nonempty":len(body)>0})
        a,b=records[-2],records[-1]
        drift.append({"group":s["group"],"name":s["name"],"url":s["url"],
            "attempt1_sha256":a["sha256"],"attempt2_sha256":b["sha256"],
            "same_bytes":a["sha256"]==b["sha256"],"drift_status":"NO_DRIFT_OBSERVED" if a["sha256"]==b["sha256"] else "DRIFT_OBSERVED"})
    # A revision row is permitted only for explicit, separately supplied archive URLs.
    revisions=[]
    for p in cfg.get("archived_pairs",[]):
        if p.get("group") not in GROUPS: raise SystemExit(f"INVALID_ARCHIVE_PAIR: {p}")
        pair=[]
        for label,key in (("a","vintage_a_url"),("b","vintage_b_url")):
            status,headers,body=fetch(p[key]); ct=headers.get("Content-Type","").split(";")[0].lower()
            path=raw/f'archive_{len(revisions):03d}_{label}.bin'; path.write_bytes(body)
            pair.append({"label":label,"url":p[key],"http_status":status,"content_type":ct,
                         "bytes":len(body),"sha256":sha(body),"raw_path":str(path)})
        revisions.append({"group":p["group"],"name":p.get("name","unnamed"),"vintage_a":pair[0],
                          "vintage_b":pair[1],"same_bytes":pair[0]["sha256"]==pair[1]["sha256"],
                          "revision_status":"NO_CONTENT_CHANGE" if pair[0]["sha256"]==pair[1]["sha256"] else "CONTENT_CHANGED_REVIEW_REQUIRED",
                          "publication_vintage_verified":bool(p.get("publication_vintage_verified",False))})
    manifest={"schema_version":"1.0","research_only":True,"start_date":args.start_date,
        "end_date":args.end_date,"created_at_utc":datetime.now(timezone.utc).isoformat(),
        "source_count":len(sources),"group_source_counts":seen,"sources":records,
        "repeat_download_drift":drift,"archived_vintage_pairs":revisions,
        "hard_gate_effect":"UNCHANGED_BLOCKED","source_promotion":"PROHIBITED",
        "limitations":["HTTP retrieval time is not source publication time.",
        "Identical repeated downloads do not prove historical vintage immutability.",
        "A content change is not automatically a revision; human lineage review is required."]}
    (root/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    with (root/"repeat_download_drift.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(drift[0])); w.writeheader(); w.writerows(drift)
    with (root/"archived_vintage_revision_ledger.csv").open("w",newline="",encoding="utf-8") as f:
        fields=["group","name","vintage_a_url","vintage_a_sha256","vintage_b_url","vintage_b_sha256","revision_status","publication_vintage_verified"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in revisions: w.writerow({"group":r["group"],"name":r["name"],"vintage_a_url":r["vintage_a"]["url"],
            "vintage_a_sha256":r["vintage_a"]["sha256"],"vintage_b_url":r["vintage_b"]["url"],
            "vintage_b_sha256":r["vintage_b"]["sha256"],"revision_status":r["revision_status"],
            "publication_vintage_verified":r["publication_vintage_verified"]})
    bad=[r for r in records if not r["http_ok"] or not r["nonempty"] or not r["content_type_match"]]
    if bad: raise SystemExit(f"FAIL_CLOSED_SOURCE_QA: {len(bad)} invalid retrieval(s); inspect manifest")
    print(json.dumps({"status":"PASS_RETRIEVAL_AND_INTEGRITY_ONLY","sources":len(sources),
        "drift_observations":len(drift),"drift_detected":sum(not x["same_bytes"] for x in drift),
        "archived_pairs":len(revisions),"revision_changes":sum(x["revision_status"]=="CONTENT_CHANGED_REVIEW_REQUIRED" for x in revisions),
        "group_source_counts":seen,"hard_gate":"BLOCKED"},indent=2))
if __name__=="__main__": main()
