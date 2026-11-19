#!/usr/bin/env python3
"""Capture exact BOP portfolio-investment series for Brazil and India.

Key dimensions and code meanings were read from IMF DSD_BOP(24.0.0),
CS_BOP(17.0.0), CL_BOP_ACCOUNTING_ENTRY(3.3.0), CL_BOP_INDICATOR(10.0.0),
CL_BOP_COUNTRY(1.0.0), CL_UNIT(2.13.0), CL_FREQ(1.2.0).
P_F is the observed portfolio-investment total financial assets/liabilities
indicator found in the broad IMF response; P_MV was not observed in these
country panels and is explicitly rejected for this extraction.
"""
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from pathlib import Path
import hashlib,json,csv,io
BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
OUT=Path("imf_bop_portfolio_exact_panel");OUT.mkdir(exist_ok=True)
COUNTRIES=["BRA","IND"]; ENTRIES=["A_NFA_T","L_NIL_T"]
INDICATOR="P_F";UNIT="USD";FREQ="Q";START="2015-Q1";END="2026-Q3"
def sha(b):return hashlib.sha256(b).hexdigest()
records=[];panel=[]
for country in COUNTRIES:
 for entry in ENTRIES:
  key=".".join([country,entry,INDICATOR,UNIT,FREQ])
  # SDMX 3.0 observation-period constraints, not startPeriod/endPeriod.
  url=f"{BASE}/{key}?c%5BTIME_PERIOD%5D=ge%3A{START}&c%5BTIME_PERIOD%5D=le%3A{END}&format=csvdata"
  ts=datetime.now(timezone.utc).isoformat()
  req=Request(url,headers={"User-Agent":"PRECISION-WIRES-IMF-BOP-panel-audit/1.0","Accept":"text/csv, */*"})
  try:
   with urlopen(req,timeout=60) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
  except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
  except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
  safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
  fn=f"{country}_{entry}_{INDICATOR}_{UNIT}_{FREQ}.csv";(OUT/fn).write_bytes(body)
  row={"country":country,"accounting_entry":entry,"indicator":INDICATOR,"unit":UNIT,"frequency":FREQ,
   "period_start":START,"period_end":END,"key":key,"url":url,"final_url":final,"retrieved_at_utc":ts,
   "http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"file":fn}
  if status==200:
   try:
    txt=body.decode("utf-8-sig")
    if txt.lstrip().startswith("<"):raise ValueError("non-CSV payload")
    rows=list(csv.DictReader(io.StringIO(txt)))
    obs=[]
    for x in rows:
     if (x.get("OBS_VALUE") or "").strip():
      period=x.get("TIME_PERIOD","")
      if not (START<=period<=END):raise ValueError(f"out-of-window period {period}")
      obs.append(x)
      panel.append({**x,"source_file":fn,"source_sha256":sha(body)})
    row["csv_parse"]="PASS";row["row_count"]=len(rows);row["nonempty_obs_value_count"]=len(obs)
    row["empty_obs_value_count"]=len(rows)-len(obs)
    row["period_min"]=min((x["TIME_PERIOD"] for x in obs),default=None)
    row["period_max"]=max((x["TIME_PERIOD"] for x in obs),default=None)
    row["sample_first"]=obs[:2];row["sample_last"]=obs[-2:]
   except Exception as e:row["csv_parse"]="FAIL";row["parse_error"]=str(e)
  records.append(row)
# Preserve a normalized panel, without unit conversion or scale manipulation.
fields=["STRUCTURE[;]","STRUCTURE_ID","ACTION","COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY","TIME_PERIOD","OBS_VALUE","SCALE","PRECISION","DECIMALS_DISPLAYED","INSTR_ASSET","FUNCTIONAL_CAT","INT_ACC_ITEM","SECTOR","ACCOUNTING_ENTRY","ACCOUNTS","FLOW_STOCK_ENTRY","FI_MATURITY","VALUATION","AL_TYPE","DERIVATION_TYPE","BOP_TYPE","OVERLAP","FR_ADJ","IFS_FLAG","BPM6_BASIS_START_DATE","STATUS","source_file","source_sha256"]
with (OUT/"portfolio_flows_panel.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(panel)
# Exact uniqueness and coverage checks.
keys=[(x["COUNTRY"],x["BOP_ACCOUNTING_ENTRY"],x["INDICATOR"],x["UNIT"],x["FREQUENCY"],x["TIME_PERIOD"]) for x in panel]
summary={"scope":"Brazil and India portfolio-investment BOP quarterly flow panel smoke test; not an EM aggregate",
 "dataflow":"IMF.STA:BOP(21.0.0)","dsd":"IMF.STA:DSD_BOP(24.0.0)",
 "dimension_order":["COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY"],
 "codelists":{"COUNTRY":"IMF.STA:CL_BOP_COUNTRY(1.0.0)","BOP_ACCOUNTING_ENTRY":"IMF.STA:CL_BOP_ACCOUNTING_ENTRY(3.3.0)",
 "INDICATOR":"IMF.STA:CL_BOP_INDICATOR(10.0.0)","UNIT":"IMF:CL_UNIT(2.13.0)","FREQUENCY":"IMF:CL_FREQ(1.2.0)"},
 "indicator_definition":"P_F — Portfolio investment, Total financial assets/liabilities",
 "accounting_entry_definitions":{"A_NFA_T":"Assets, Net acquisition of financial assets","L_NIL_T":"Liabilities, Net incurrence of liabilities"},
 "unit":"USD (preserved exactly as source code; no rescaling/conversion applied)",
 "frequency":"Quarterly","period_window":[START,END],"requests":records,
 "request_count":len(records),"http_200_count":sum(x["http_status"]==200 for x in records),
 "csv_parse_pass_count":sum(x.get("csv_parse")=="PASS" for x in records),
 "panel_row_count":len(panel),"nonempty_observation_count":len(panel),
 "duplicate_key_count":len(keys)-len(set(keys)),
 "country_entry_coverage":{c:{e:sum(1 for x in panel if x["COUNTRY"]==c and x["BOP_ACCOUNTING_ENTRY"]==e) for e in ENTRIES} for c in COUNTRIES},
 "period_min":min((x["TIME_PERIOD"] for x in panel),default=None),
 "period_max":max((x["TIME_PERIOD"] for x in panel),default=None),
 "no_scale_conversion":True,"no_forward_fill":True,"no_synthetic_rows":True}
(OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if summary["http_200_count"]!=len(records) or summary["csv_parse_pass_count"]!=len(records) or not panel or summary["duplicate_key_count"] or any(x["nonempty_obs_value_count"]==0 for x in records):
 raise SystemExit("Targeted BOP panel did not pass integrity gates")
