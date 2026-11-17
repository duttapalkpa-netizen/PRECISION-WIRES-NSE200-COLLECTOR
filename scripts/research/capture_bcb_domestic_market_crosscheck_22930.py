#!/usr/bin/env python3
"""Capture SGS 22930 and reconcile Sep-2026 domestic portfolio flows to BCB's release."""
from __future__ import annotations
import csv, hashlib, json, sys, time
from datetime import datetime, timezone, date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OUT=Path("bcb_domestic_market_crosscheck_202609")
OUT.mkdir(parents=True,exist_ok=True)
URL="https://api.bcb.gov.br/dados/serie/bcdata.sgs.22930/dados?formato=csv"
PARENT=Path("data/raw/bcb/instrument_net_capture_20261117")
TARGET=date(2026,9,1)
last=None
started=datetime.now(timezone.utc).isoformat()
for attempt in range(3):
 try:
  req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-BCB-country-period-audit/1.0","Accept":"text/csv, text/plain, */*"})
  with urlopen(req,timeout=60) as response:
   raw=response.read(); status=response.status; headers={k.lower():v for k,v in response.headers.items()}; final=response.geturl()
  if status!=200 or not raw: raise RuntimeError(f"HTTP {status}/empty")
  if raw.lstrip().lower().startswith((b"<!doctype html",b"<html")): raise RuntimeError("HTML body, not CSV")
  raw.decode("utf-8-sig")
  (OUT/"sgs_22930.csv").write_bytes(raw)
  meta={"requested_url":URL,"final_url":final,"retrieval_started_at_utc":started,"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"http_status":status,"response_headers":headers,"content_type":headers.get("content-type"),"byte_length":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
  break
 except (HTTPError,URLError,TimeoutError,OSError,RuntimeError,UnicodeDecodeError) as exc:
  last=repr(exc)
  if attempt<2: time.sleep(attempt+1)
else:
 (OUT/"manifest.json").write_text(json.dumps({"status":"BLOCKED","error":last},indent=2)+chr(10),encoding="utf-8")
 print(last); sys.exit(1)

def load(code,root):
 path=root/f"sgs_{code}.csv"
 out={}
 with path.open(encoding="utf-8-sig",newline="") as f:
  reader=csv.DictReader(f,delimiter=";")
  if reader.fieldnames!=["data","valor"]: raise ValueError(f"{code}: unexpected CSV header")
  for row in reader:
   d=datetime.strptime(row["data"].strip().strip('"'),"%d/%m/%Y").date()
   val=Decimal(row["valor"].strip().strip('"').replace(".","").replace(",","."))
   if d in out: raise ValueError(f"{code}: duplicate date {d}")
   out[d]=val
 return out

v30=load("22930",OUT)[TARGET]
v36=load("22936",PARENT)[TARGET]
v42=load("22942",PARENT)[TARGET]
def one_decimal_bn(x):
 return x.quantize(Decimal("0.1"),rounding=ROUND_HALF_UP)
equity_funds_outflow=-(v30+v36)/Decimal(1000)
debt_outflow=-v42/Decimal(1000)
total_outflow=equity_funds_outflow+debt_outflow
release={"publication_date":"2026-10-26","reference_period":"2026-09","source_url":"https://www.bcb.gov.br/estatisticas/estatisticassetorexterno?mode=light","reported_total_domestic_portfolio_outflow_usd_bn":Decimal("2.1"),"reported_equity_and_funds_domestic_outflow_usd_bn":Decimal("1.7"),"reported_domestic_debt_outflow_usd_bn":Decimal("0.4")}
report={
 "schema_version":1,"purpose":"research_only_official_bcb_country_period_crosscheck",
 "raw_capture":meta,"reference_date":TARGET.isoformat(),
 "input_values_usd_million":{"22930_domestic_equity_liabilities_net":str(v30),"22936_fund_liabilities_net":str(v36),"22942_domestic_debt_liabilities_net":str(v42)},
 "derived_outflows_usd_billion":{"equity_and_funds":str(equity_funds_outflow),"domestic_debt":str(debt_outflow),"total":str(total_outflow)},
 "derived_rounded_to_0_1_usd_billion":{"equity_and_funds":str(one_decimal_bn(equity_funds_outflow)),"domestic_debt":str(one_decimal_bn(debt_outflow)),"total":str(one_decimal_bn(total_outflow))},
 "official_release":{k:(str(v) if isinstance(v,Decimal) else v) for k,v in release.items()},
 "checks":{
  "equity_funds_matches_release_rounded":one_decimal_bn(equity_funds_outflow)==release["reported_equity_and_funds_domestic_outflow_usd_bn"],
  "domestic_debt_matches_release_rounded":one_decimal_bn(debt_outflow)==release["reported_domestic_debt_outflow_usd_bn"],
  "total_matches_release_rounded":one_decimal_bn(total_outflow)==release["reported_total_domestic_portfolio_outflow_usd_bn"],
 },
 "country_period_qa":"PASS" if all([
  one_decimal_bn(equity_funds_outflow)==release["reported_equity_and_funds_domestic_outflow_usd_bn"],
  one_decimal_bn(debt_outflow)==release["reported_domestic_debt_outflow_usd_bn"],
  one_decimal_bn(total_outflow)==release["reported_total_domestic_portfolio_outflow_usd_bn"]]) else "BLOCKED",
 "accounting_rounding_tolerance":"RELEASE_COMPARISON_ONLY; reported to USD 0.1bn; not a universal series reconciliation tolerance",
 "brazil_pilot_acceptance":"NOT_ACCEPTED",
 "em_wide_panel":"NOT_DONE",
 "production_integration":"NOT_AUTHORIZED"
}
manifest={"schema_version":1,"purpose":"research_only_single_series_country_period_capture","provider":"BCB/SGS","series_code":"22930","series_title":"Portfolio investment - equities - domestic market - liabilities - monthly - net","raw_capture_status":"PASS","raw_file":"sgs_22930.csv",**meta}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
(OUT/"crosscheck_report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
print(json.dumps(report,indent=2,sort_keys=True))
if report["country_period_qa"]!="PASS": sys.exit(1)
