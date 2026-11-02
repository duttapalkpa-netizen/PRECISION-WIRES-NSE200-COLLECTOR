#!/usr/bin/env python3
"""Fail-closed raw evidence collector. Research-only; no source promotion."""
from __future__ import annotations
import argparse,csv,hashlib,io,json,re,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError

GROUPS=("benchmark_index","sector_indices","volatility","geopolitical_events")
ALLOWED=(".nseindia.com",".niftyindices.com",".pib.gov.in",".mea.gov.in")
UA="PRECISION-WIRES-research-only/1.1"

def digest(b): return hashlib.sha256(b).hexdigest()
def allowed(url):
 p=urlparse(url); return p.scheme=="https" and p.hostname and any(p.hostname==d[1:] or p.hostname.endswith(d) for d in ALLOWED)
def fetch(url):
 if not allowed(url): raise ValueError("URL_NOT_ALLOWLISTED")
 req=Request(url,headers={"User-Agent":UA,"Accept":"text/csv,text/html,application/pdf,*/*"})
 try:
  with urlopen(req,timeout=35) as r: return r.status,dict(r.headers.items()),r.read()
 except HTTPError as e: return e.code,dict(e.headers.items()),e.read()
 except (URLError,TimeoutError) as e: raise RuntimeError(f"FETCH_ERROR:{url}:{e}") from e

def validate_csv(body,source):
 try: text=body.decode("utf-8-sig"); rows=list(csv.DictReader(io.StringIO(text)))
 except Exception as e: return False,{"reason":"CSV_PARSE_ERROR","detail":str(e)}
 if not rows: return False,{"reason":"CSV_NO_DATA_ROWS"}
 headers=list(rows[0])
 date_col=source.get("date_column","Date")
 if date_col not in headers: return False,{"reason":"DATE_COLUMN_MISSING","headers":headers}
 wanted=source.get("expected_date")
 dates={str(r.get(date_col,"")).strip() for r in rows}
 if wanted and wanted not in dates:
  # Accept common display form only when it parses to the exact expected date.
  from datetime import datetime as dt
  found=False
  for value in dates:
   for fmt in ("%d-%b-%Y","%d-%m-%Y","%d/%m/%Y","%Y-%m-%d"):
    try:
     if dt.strptime(value,fmt).date().isoformat()==wanted: found=True
    except ValueError: pass
  if not found: return False,{"reason":"EXPECTED_DATE_NOT_FOUND","expected_date":wanted,"observed_dates":sorted(dates)[:8]}
 index_col=source.get("index_name_column")
 expected=source.get("expected_index_names",[])
 if index_col:
  if index_col not in headers: return False,{"reason":"INDEX_NAME_COLUMN_MISSING","headers":headers}
  observed={str(r.get(index_col,"")).strip().upper() for r in rows}
  missing=[n for n in expected if n.upper() not in observed]
  if missing: return False,{"reason":"EXPECTED_INDEX_NAMES_MISSING","missing":missing,"observed":sorted(observed)[:20]}
 required=source.get("required_columns",[])
 missing=[c for c in required if c not in headers]
 if missing: return False,{"reason":"REQUIRED_COLUMNS_MISSING","missing":missing}
 return True,{"row_count":len(rows),"headers":headers,"date_values":sorted(dates)[:12],"index_names":sorted({str(r.get(index_col,"")).strip() for r in rows})[:30] if index_col else []}

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--config",required=True);p.add_argument("--start-date",required=True);p.add_argument("--end-date",required=True);p.add_argument("--out",default="macro_geo_p0_raw_evidence")
 a=p.parse_args(); start=datetime.strptime(a.start_date,"%Y-%m-%d").date();end=datetime.strptime(a.end_date,"%Y-%m-%d").date()
 if start>end: raise SystemExit("INVALID_DATE_RANGE")
 cfg=json.loads(Path(a.config).read_text());sources=cfg.get("sources",[])
 if not sources: raise SystemExit("NO_SOURCES")
 counts={g:0 for g in GROUPS}
 for s in sources:
  if s.get("group") not in GROUPS or not allowed(s.get("url","")): raise SystemExit("INVALID_SOURCE_CONFIG")
  if s["group"] in ("benchmark_index","sector_indices","volatility") and not s.get("expected_date"): raise SystemExit("MARKET_SOURCE_REQUIRES_EXPECTED_DATE")
  counts[s["group"]]+=1
 if any(not n for n in counts.values()): raise SystemExit("P0_GROUP_MISSING")
 # A single URL cannot masquerade as three independent data groups.
 url_groups={}
 for s in sources: url_groups.setdefault(s["url"],set()).add(s["group"])
 if any(len(gs)>1 for gs in url_groups.values()): raise SystemExit("CROSS_GROUP_URL_REUSE_REJECTED")
 root=Path(a.out);raw=root/"raw";raw.mkdir(parents=True,exist_ok=True)
 records=[];drift=[];bad=[]
 for i,s in enumerate(sources):
  pair=[]
  for attempt in (1,2):
   if attempt==2: time.sleep(1.1)
   status,h,b=fetch(s["url"]);ct=h.get("Content-Type",h.get("content-type","")).split(";")[0].strip().lower()
   suffix={"text/csv":".csv","text/html":".html","application/pdf":".pdf"}.get(ct,".bin")
   fn=f"{i:03d}_{re.sub(r'[^A-Za-z0-9_.-]+','_',s['name'])[:70]}_{attempt}{suffix}";(raw/fn).write_bytes(b)
   item={"group":s["group"],"name":s["name"],"url":s["url"],"attempt":attempt,"http_status":status,"content_type":ct,"bytes":len(b),"sha256":digest(b),"raw_path":str(raw/fn),"retrieved_at_utc":datetime.now(timezone.utc).isoformat()}
   expected=[x.lower() for x in s.get("expected_content_types",[])]
   item["content_type_ok"]=not expected or ct in expected
   item["http_ok"]=status==200 and bool(b)
   if s["group"] in ("benchmark_index","sector_indices","volatility") and item["http_ok"] and item["content_type_ok"] and ct=="text/csv":
    ok,detail=validate_csv(b,s);item["csv_validation"]={"ok":ok,**detail}
   elif s["group"]=="geopolitical_events":
    ok=ct in ("text/html","application/pdf") and bool(b);item["document_validation"]={"ok":ok,"format":ct}
   else: ok=False;item["csv_validation"]={"ok":False,"reason":"UNEXPECTED_CONTENT_TYPE"}
   item["valid"]=item["http_ok"] and item["content_type_ok"] and ok
   if not item["valid"]: bad.append(item)
   records.append(item);pair.append(item)
  drift.append({"group":s["group"],"name":s["name"],"sha256_attempt1":pair[0]["sha256"],"sha256_attempt2":pair[1]["sha256"],"same_bytes":pair[0]["sha256"]==pair[1]["sha256"],"status":"NO_DRIFT_OBSERVED" if pair[0]["sha256"]==pair[1]["sha256"] else "DRIFT_OBSERVED"})
 # Historical revision ledger is only created for explicitly proven, immutable archived vintages.
 revisions=[]
 for p0 in cfg.get("archived_pairs",[]):
  if not p0.get("publication_vintage_verified"): continue
  pair=[]
  for key in ("vintage_a_url","vintage_b_url"):
   st,h,b=fetch(p0[key]);pair.append({"url":p0[key],"status":st,"sha256":digest(b),"bytes":len(b),"raw_path":""})
  revisions.append({"group":p0["group"],"name":p0["name"],"vintage_a":pair[0],"vintage_b":pair[1],"revision":"NO_CONTENT_CHANGE" if pair[0]["sha256"]==pair[1]["sha256"] else "CONTENT_CHANGED_REVIEW_REQUIRED"})
 manifest={"schema_version":"1.1","research_only":True,"window":{"start":a.start_date,"end":a.end_date},"created_at_utc":datetime.now(timezone.utc).isoformat(),"group_source_counts":counts,"records":records,"repeat_download_drift":drift,"verified_archived_vintage_pairs":revisions,"failed_records":len(bad),"hard_gate":"BLOCKED","source_promotion":"PROHIBITED"}
 (root/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
 with (root/"repeat_download_drift.csv").open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(drift[0]));w.writeheader();w.writerows(drift)
 if revisions:
  with (root/"vintage_revision_ledger.json").open("w") as f:json.dump(revisions,f,indent=2)
 if bad: raise SystemExit(f"FAIL_CLOSED:{len(bad)} invalid records; see manifest")
 print(json.dumps({"status":"PASS_RAW_RETRIEVAL_AND_SCHEMA_ONLY","records":len(records),"failed":len(bad),"drift":len(drift),"verified_vintage_pairs":len(revisions),"hard_gate":"BLOCKED"},indent=2))
if __name__=="__main__":main()
