#!/usr/bin/env python3
"""Broad country-level BOP query to distinguish key mismatch from empty series."""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,csv,io
BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
OUT=Path("imf_bop_broad_probe");OUT.mkdir(exist_ok=True)
QUERIES=[
 ("BRA_quarterly_all","BRA.*.*.*.Q","2020-Q1","2026-Q3"),
 ("IND_quarterly_all","IND.*.*.*.Q","2020-Q1","2026-Q3"),
 ("BRA_annual_all","BRA.*.*.*.A","2015","2025"),
 ("BRA_portfolio_quarterly_all_entries","BRA.*.P_MV.USD.Q","2015-Q1","2026-Q3"),
 ("BRA_current_account_quarterly","BRA.NETCD_T.CAB.USD.Q","2015-Q1","2026-Q3"),
]
def sha(b):return hashlib.sha256(b).hexdigest()
out=[]
for name,key,start,end in QUERIES:
 url=f"{BASE}/{key}?startPeriod={start}&endPeriod={end}&format=csvdata"
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-BOP-broad-diagnostic/1.0","Accept":"text/csv, */*"})
 try:
  with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 fn=name+".csv";(OUT/fn).write_bytes(body)
 row={"name":name,"key":key,"start_period":start,"end_period":end,"url":url,"final_url":final,
  "retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn,
  "body_preview":body[:1200].decode("utf-8","replace")}
 if status==200:
  try:
   txt=body.decode("utf-8-sig")
   rows=list(csv.DictReader(io.StringIO(txt)))
   obs=[x for x in rows if (x.get("OBS_VALUE") or "").strip()]
   row["csv_parse"]="PASS";row["row_count"]=len(rows);row["nonempty_obs_value_count"]=len(obs)
   row["sample_rows"]=obs[:3]
  except Exception as e:row["csv_parse"]="FAIL";row["parse_error"]=str(e)
 out.append(row)
summary={"scope":"diagnostic only; broad keys are wildcard queries and not production series definitions","queries":out,
 "http_200_count":sum(x["http_status"]==200 for x in out),
 "csv_parse_pass_count":sum(x.get("csv_parse")=="PASS" for x in out),
 "total_nonempty_observations":sum(x.get("nonempty_obs_value_count",0) for x in out)}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if summary["http_200_count"]!=len(out) or summary["csv_parse_pass_count"]!=len(out):raise SystemExit("HTTP or CSV parse failure")
