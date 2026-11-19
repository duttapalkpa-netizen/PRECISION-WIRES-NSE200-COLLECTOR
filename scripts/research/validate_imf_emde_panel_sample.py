#!/usr/bin/env python3
"""Independent exact-key cross-check of 12-country sample against 154-country panel."""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import csv,io,json,hashlib,collections
BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
COUNTRIES=["ARG","BGD","BRA","CHN","IDN","IND","MEX","NGA","POL","SAU","TUR","ZAF"]
ENTRIES=["A_NFA_T","L_NIL_T"];START="2015-Q1";END="2026-Q3"
OUT=Path("imf_emde_sample_validation");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
PANEL=Path("/tmp/emde/emde_portfolio_flows.csv")
def get(url):
 ts=datetime.now(timezone.utc).isoformat();req=Request(url,headers={"User-Agent":"PRECISION-WIRES-EMDE-exact-crosscheck/1.0","Accept":"text/csv, */*"})
 try:
  with urlopen(req,timeout=45) as r:status=r.status;headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"body":body}
def parse(body):
 text=body.decode("utf-8-sig")
 if text.lstrip().startswith("<"):raise ValueError("non-CSV")
 return list(csv.DictReader(io.StringIO(text)))
broad=list(csv.DictReader(PANEL.open(encoding="utf-8-sig",newline="")))
broad_index={}
for r in broad:
 if r["COUNTRY"] in COUNTRIES:
  key=(r["COUNTRY"],r["BOP_ACCOUNTING_ENTRY"],r["TIME_PERIOD"])
  broad_index[key]={k:v for k,v in r.items() if k not in ("SOURCE_FILE","SOURCE_SHA256")}
results=[];total_match=0;total_rows=0
for country in COUNTRIES:
 for entry in ENTRIES:
  key=f"{country}.{entry}.P_F.USD.Q"
  url=f"{BASE}/{quote(key,safe='.') }?c%5BTIME_PERIOD%5D=ge%3A{START}&c%5BTIME_PERIOD%5D=le%3A{END}&format=csvdata"
  r=get(url);fn=f"{country}_{entry}.csv";(RAW/fn).write_bytes(r["body"])
  row={"country":country,"entry":entry,"key":key,"url":url,**{k:v for k,v in r.items() if k!="body"}}
  if r["http_status"]!=200:row["status"]="HTTP_FAIL";results.append(row);continue
  try:
   exact=parse(r["body"]);nonempty=[x for x in exact if (x.get("OBS_VALUE") or "").strip()]
   matched=0;missing=[];mismatch=[]
   for x in nonempty:
    k=(country,entry,x["TIME_PERIOD"]);b=broad_index.get(k)
    if b is None:missing.append(x["TIME_PERIOD"]);continue
    for col,val in x.items():
     if b.get(col,"")!=val:mismatch.append({"period":x["TIME_PERIOD"],"column":col,"exact":val,"broad":b.get(col,"")})
    if not any(z["period"]==x["TIME_PERIOD"] for z in mismatch):matched+=1
   exact_periods={x["TIME_PERIOD"] for x in nonempty}
   broad_periods={k[2] for k in broad_index if k[0]==country and k[1]==entry}
   row.update({"status":"PASS" if not missing and not mismatch and exact_periods==broad_periods else "MISMATCH",
    "raw_rows":len(exact),"nonempty_observations":len(nonempty),"broad_observations":len(broad_periods),
    "exact_to_broad_match_count":matched,"missing_from_broad":missing,"attribute_or_value_mismatches":mismatch,
    "exact_period_min":min(exact_periods,default=None),"exact_period_max":max(exact_periods,default=None)})
   total_match+=matched;total_rows+=len(nonempty)
  except Exception as e:row["status"]="PARSE_FAIL";row["error"]=str(e)
  results.append(row)
summary={"scope":"independent exact-key cross-check of 12 WEO EMDE members × 2 accounting entries against multi-country raw panel",
 "countries":COUNTRIES,"entry_codes":ENTRIES,"request_count":len(results),
 "http_200_count":sum(x["http_status"]==200 for x in results),
 "series_pass_count":sum(x.get("status")=="PASS" for x in results),
 "series_total":len(results),"exact_observation_rows":total_rows,"exact_to_broad_match_count":total_match,
 "failed_series":[x for x in results if x.get("status")!="PASS"],"responses":results}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if summary["http_200_count"]!=24 or summary["series_pass_count"]!=24 or total_match!=total_rows:
 raise SystemExit("EMDE sample cross-check failed")
