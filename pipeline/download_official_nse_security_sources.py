#!/usr/bin/env python3
"""Bounded downloader for official NSE security-master CSV snapshots."""
from __future__ import annotations
import hashlib, json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv, re

SOURCES = {
 "equity": "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
 "etf": "https://nsearchives.nseindia.com/content/equities/eq_etfseclist.csv",
 "symbol_changes": "https://nsearchives.nseindia.com/content/equities/symbolchange.csv",
}
ALLOWED_HOSTS={"nsearchives.nseindia.com"}
MAX_BYTES=10*1024*1024

def sha256(b): return hashlib.sha256(b).hexdigest()
def csv_check(raw, name):
    text=raw.decode("utf-8-sig")
    rows=list(csv.reader(text.splitlines()))
    if len(rows)<2 or not rows[0]: raise ValueError(f"{name}: empty/header-only CSV")
    norm=[re.sub(r"[^A-Z0-9]","",x.strip().upper()) for x in rows[0]]
    if any(not x for x in norm) or len(norm)!=len(set(norm)):
        raise ValueError(f"{name}: blank or duplicate normalized headers")
    return {"columns":norm,"record_count":len(rows)-1}
def main():
    out=Path(os.environ.get("NSE_OUT","nse_official_sources")); out.mkdir(parents=True,exist_ok=True)
    entries=[]; failures=[]
    for name,url in SOURCES.items():
        u=urlparse(url)
        if u.scheme!="https" or u.hostname not in ALLOWED_HOSTS:
            raise RuntimeError(f"blocked non-official host: {url}")
        last=None
        for attempt in range(1,4):
            try:
                req=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; PrecisionWiresResearch/1.0)","Accept":"text/csv,*/*;q=0.8","Referer":"https://www.nseindia.com/"})
                with urlopen(req,timeout=25) as response:
                    final=urlparse(response.geturl())
                    if final.scheme!="https" or final.hostname not in ALLOWED_HOSTS:
                        raise ValueError(f"redirected outside official NSE host: {response.geturl()}")
                    ctype=response.headers.get("Content-Type","").split(";")[0].strip().lower()
                    raw=response.read(MAX_BYTES+1)
                    if len(raw)>MAX_BYTES: raise ValueError(f"{name}: exceeds {MAX_BYTES} byte cap")
                    if ctype not in {"text/csv","application/csv","application/octet-stream","application/vnd.ms-excel"}:
                        raise ValueError(f"{name}: unexpected content-type {ctype!r}")
                    stats=csv_check(raw,name)
                    # Save only after all checks pass.
                    path=out/(name+".csv"); path.write_bytes(raw)
                    entries.append({"name":name,"source_url":url,"final_url":response.geturl(),
                        "report_date":datetime.now(timezone.utc).date().isoformat(),
                        "published_at":None,"retrieved_at":datetime.now(timezone.utc).isoformat(),
                        "content_type":ctype,"bytes":len(raw),"sha256":sha256(raw),
                        "path":str(path),**stats})
                    print(f"PASS {name}: bytes={len(raw)} rows={stats['record_count']} sha256={sha256(raw)}")
                    last=None; break
            except Exception as exc:
                last=f"{type(exc).__name__}: {exc}"
                print(f"ATTEMPT {attempt}/3 {name} FAILED: {last}",file=sys.stderr)
                if attempt<3: time.sleep(attempt*2)
        if last: failures.append({"name":name,"url":url,"error":last})
    manifest={"status":"PASS_ALL_OFFICIAL_SNAPSHOTS_DOWNLOADED" if not failures else "PARTIAL_OFFICIAL_SOURCE_DOWNLOAD",
      "source_count":len(entries),"failure_count":len(failures),
      "timestamp_policy":"retrieved_at is UTC collector time; report_date is UTC retrieval snapshot date, not publisher release date; published_at remains null unless explicitly supplied",
      "sources":entries,"failures":failures}
    p=out/"source_manifest.json"; p.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":manifest["status"],"source_count":len(entries),"failure_count":len(failures),"manifest_sha256":sha256(p.read_bytes())},indent=2))
    return 0 if entries else 2
if __name__=="__main__": raise SystemExit(main())
