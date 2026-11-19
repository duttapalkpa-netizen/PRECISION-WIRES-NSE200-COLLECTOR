#!/usr/bin/env python3
"""Exact-key IMF BOP observation smoke test built only from retrieved DSD/codelists.

Country codes BRA/IND, BOP accounting entries A_NFA_T/L_NIL_T,
indicator P_MV, unit USD and frequency Q were confirmed in the official
DSD_BOP(24.0.0), CS_BOP(17.0.0), and referenced codelists before query.
No API key/cookie is sent. This is a two-country access smoke test, not an EM
aggregate or a trading signal.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,csv,io
BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
OUT=Path("imf_bop_observation_smoketest");OUT.mkdir(exist_ok=True)
COUNTRIES=["BRA","IND"]
ENTRIES=["A_NFA_T","L_NIL_T"]
INDICATOR="P_MV";UNIT="USD";FREQ="Q"
START="2015-Q1";END="2026-Q3"
def sha(b):return hashlib.sha256(b).hexdigest()
records=[]
for country in COUNTRIES:
 for entry in ENTRIES:
  key=".".join([country,entry,INDICATOR,UNIT,FREQ])
  url=f"{BASE}/{key}?startPeriod={START}&endPeriod={END}&format=csvdata"
  ts=datetime.now(timezone.utc).isoformat()
  req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-BOP-observation-audit/1.0","Accept":"text/csv, application/vnd.sdmx.data+csv;version=2.0.0, application/vnd.sdmx.data+json;version=2.0.0, application/xml, */*"})
  try:
   with urlopen(req,timeout=60) as r: status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
  except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
  except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
  safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
  fn=f"{country}_{entry}_{INDICATOR}_{UNIT}_{FREQ}.csv"
  (OUT/fn).write_bytes(body)
  row={"country":country,"accounting_entry":entry,"indicator":INDICATOR,"unit":UNIT,"frequency":FREQ,
       "start_period":START,"end_period":END,"key":key,"url":url,"final_url":final,
       "retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),
       "sha256":sha(body),"file":fn}
  if status==200:
   try:
    text=body.decode("utf-8-sig")
    if text.strip().startswith("<"): raise ValueError("HTTP 200 returned XML/HTML, not CSV")
    rows=list(csv.DictReader(io.StringIO(text)))
    row["csv_parse"]="PASS";row["row_count"]=len(rows)
    row["columns"]=list(rows[0].keys()) if rows else []
    obs=[x for x in rows if (x.get("OBS_VALUE") or "").strip() not in ("","NA","NaN","null")]
    row["nonempty_obs_value_count"]=len(obs)
    row["empty_obs_value_count"]=len(rows)-len(obs)
    row["time_period_min"]=min((x.get("TIME_PERIOD","") for x in obs),default=None)
    row["time_period_max"]=max((x.get("TIME_PERIOD","") for x in obs),default=None)
    row["sample_rows"]=rows[:3]
   except Exception as e:row["csv_parse"]="FAIL";row["parse_error"]=str(e)
  records.append(row)
summary={"scope":"official IMF BOP exact-key two-country access smoke test; no EM aggregation",
 "dataflow":"IMF.STA:BOP(21.0.0)","dsd":"IMF.STA:DSD_BOP(24.0.0)",
 "dimensions":["COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY"],
 "dimension_code_basis":{"COUNTRY":"CL_BOP_COUNTRY(1.0.0)","BOP_ACCOUNTING_ENTRY":"CL_BOP_ACCOUNTING_ENTRY(3.3.0)",
 "INDICATOR":"CL_BOP_INDICATOR(10.0.0)","UNIT":"CL_UNIT(2.13.0)","FREQUENCY":"CL_FREQ(1.2.0)"},
 "country_codes":COUNTRIES,"accounting_entries":ENTRIES,"indicator":INDICATOR,"unit":UNIT,"frequency":FREQ,
 "period_window":[START,END],"requests":records,
 "http_200_count":sum(x["http_status"]==200 for x in records),
 "csv_parse_pass_count":sum(x.get("csv_parse")=="PASS" for x in records),
 "nonempty_observation_total":sum(x.get("nonempty_obs_value_count",0) for x in records)}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if summary["http_200_count"]!=len(records) or summary["csv_parse_pass_count"]!=len(records):
 raise SystemExit("BOP observation access smoke test did not pass")
