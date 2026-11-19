#!/usr/bin/env python3
"""Reconcile IMF Brazil quarterly P_F asset/liability values to official BCB monthly net series.

BCB 22906 = portfolio investment net acquisition of financial assets (USD million).
BCB 22924 = portfolio investment net incurrence of liabilities (USD million).
For each selected quarter, sum the three monthly BCB values and compare with the
IMF quarterly raw OBS_VALUE / 1e6. The BCB source reports one decimal place;
three monthly rounding errors imply a maximum absolute quarterly rounding
bound of 0.15 million USD. No values are written back to the production panel.
"""
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import csv,json,hashlib,re

OUT=Path("bcb_scale_reconciliation"); RAW=OUT/"raw"; RAW.mkdir(parents=True,exist_ok=True)
BASE="https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json"
SOURCES={
 "A_NFA_T":{"sgs":22906,"url":BASE.format(22906),"imf_csv":"imf_bop_portfolio_exact_panel/BRA_A_NFA_T_P_F_USD_Q.csv"},
 "L_NIL_T":{"sgs":22924,"url":BASE.format(22924),"imf_csv":"imf_bop_portfolio_exact_panel/BRA_L_NIL_T_P_F_USD_Q.csv"}
}
QUARTERS=[f"{y}-Q{q}" for y in range(2015,2026) for q in range(1,5)] + [f"2026-Q{q}" for q in range(1,4)]
TOL=Decimal("0.15")

def fetch(url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-BOP-scale-crosscheck/1.0","Accept":"application/json"})
 try:
  with urlopen(req,timeout=45) as r: status=r.status; headers=dict(r.headers.items()); body=r.read(); final=r.geturl()
 except HTTPError as e: status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read(); final=e.geturl()
 except (URLError,TimeoutError) as e: status=0; headers={}; body=str(e).encode(); final=url
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"body":body}

def sha(b): return hashlib.sha256(b).hexdigest()

def qmonths(q):
 y,qn=q.split("-Q"); m0=(int(qn)-1)*3+1
 return [f"{y}-{m:02d}" for m in range(m0,m0+3)]

def main():
 outrows=[]; receipts=[]
 for entry,src in SOURCES.items():
  r=fetch(src["url"]); body=r.pop("body")
  fn=f"BCB_SGS_{src['sgs']}.json"; (RAW/fn).write_bytes(body)
  receipt={**r,"file":"raw/"+fn,"byte_count":len(body),"sha256":sha(body),"sgs_code":src["sgs"]}
  receipts.append(receipt)
  if r["http_status"]!=200: raise SystemExit(f"BCB {src['sgs']} HTTP {r['http_status']}")
  data=json.loads(body)
  monthly={}
  for x in data:
   d=datetime.strptime(x["data"],"%d/%m/%Y").strftime("%Y-%m")
   monthly[d]=Decimal(x["valor"])
  imf=[]
  with open(src["imf_csv"],newline="",encoding="utf-8") as f:
   for x in csv.DictReader(f):
    if x.get("COUNTRY")=="BRA" and x.get("BOP_ACCOUNTING_ENTRY")==entry and x.get("INDICATOR")=="P_F" and x.get("UNIT")=="USD" and x.get("FREQUENCY")=="Q":
     imf.append(x)
  imf_by_period={x["TIME_PERIOD"]:x for x in imf}
  for q in QUARTERS:
   months=qmonths(q); missing=[m for m in months if m not in monthly]
   raw=imf_by_period.get(q)
   if missing or raw is None:
    outrows.append({"entry":entry,"quarter":q,"status":"BLOCKED_MISSING_SOURCE","missing_bcb_months":missing,"imf_row_present":raw is not None})
    continue
   vals=[monthly[m] for m in months]
   bcb_sum=sum(vals,Decimal("0"))
   raw_value=Decimal(raw["OBS_VALUE"])
   scale=raw.get("SCALE","")
   imf_million=raw_value/Decimal("1000000")
   residual=imf_million-bcb_sum
   one_decimal=all(re.fullmatch(r"-?\d+\.\d",str(monthly[m])) for m in months)
   passed=one_decimal and abs(residual)<=TOL and scale=="6"
   outrows.append({
    "entry":entry,"bcb_sgs_code":src["sgs"],"quarter":q,"bcb_months":months,
    "bcb_monthly_values_usd_million":[str(v) for v in vals],
    "bcb_quarter_sum_usd_million":str(bcb_sum),
    "imf_obs_value_raw_usd":str(raw_value),"imf_scale":scale,
    "imf_obs_value_div_1e6_usd_million":str(imf_million),
    "residual_imf_minus_bcb_usd_million":str(residual),
    "tolerance_usd_million":str(TOL),"bcb_month_values_one_decimal":one_decimal,
    "status":"PASS" if passed else "REVIEW"
   })
 (OUT/"quarter_reconciliation.json").write_text(json.dumps(outrows,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 with (OUT/"quarter_reconciliation.csv").open("w",newline="",encoding="utf-8") as f:
  fields=list(outrows[0]); w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for x in outrows: w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in x.items()})
 summary={"scope":"Brazil BOP scale/sign reconciliation against official BCB monthly portfolio investment net flows",
  "sources":receipts,"series":{"A_NFA_T":"BCB SGS 22906, net acquisition of financial assets, monthly, million US dollars",
   "L_NIL_T":"BCB SGS 22924, net incurrence of liabilities, monthly, million US dollars"},
  "quarters":QUARTERS,"expected_comparisons":len(SOURCES)*len(QUARTERS),
  "pass_count":sum(x.get("status")=="PASS" for x in outrows),
  "review_count":sum(x.get("status")=="REVIEW" for x in outrows),
  "blocked_count":sum(x.get("status")=="BLOCKED_MISSING_SOURCE" for x in outrows),
  "tolerance_rule":"0.15 USD million = 3 monthly source values each rounded to 0.1 USD million (maximum aggregate rounding bound)",
  "conversion_test":"IMF OBS_VALUE / 1,000,000 compared with sum of three BCB monthly values",
  "all_pass":len(outrows)==94 and all(x.get("status")=="PASS" for x in outrows),
  "max_abs_residual_usd_million":str(max((abs(Decimal(x["residual_imf_minus_bcb_usd_million"])) for x in outrows if x.get("residual_imf_minus_bcb_usd_million") is not None),default=Decimal("0"))),
  "warning":"This validates Brazil across 47 quarters and two flow entries; do not generalize to all EMDE countries or India without additional country-source checks."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if not summary["all_pass"]: raise SystemExit("Brazil scale/sign reconciliation did not fully PASS")
if __name__=="__main__": main()
