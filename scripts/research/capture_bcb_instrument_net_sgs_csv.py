#!/usr/bin/env python3
"""Capture eight BCB portfolio instrument-net SGS CSVs; raw-byte research-only stage."""
from __future__ import annotations
import csv, hashlib, json, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OUT=Path("bcb_instrument_net_capture")
OUT.mkdir(parents=True,exist_ok=True)
SERIES={
 "22909":{"title":"Portfolio investment - equities - assets - monthly - net","branch":"assets/equities"},
 "22912":{"title":"Portfolio investment - investment funds - assets - monthly - net","branch":"assets/investment_funds"},
 "22915":{"title":"Portfolio investment - debt securities - assets - monthly - net","branch":"assets/debt"},
 "22927":{"title":"Portfolio investment - equities - liabilities - monthly - net","branch":"liabilities/equities"},
 "22936":{"title":"Portfolio investment - investment funds - liabilities - monthly - net","branch":"liabilities/investment_funds"},
 "22939":{"title":"Portfolio investment - debt securities - liabilities - monthly - net","branch":"liabilities/debt"},
 "22942":{"title":"Portfolio investment - debt securities - liabilities - domestic market - monthly - net","branch":"liabilities/debt_domestic"},
 "22945":{"title":"Portfolio investment - debt securities - liabilities - external market - monthly - net","branch":"liabilities/debt_external"},
}
manifest={"schema_version":1,"purpose":"research_only_bcb_instrument_level_net_raw_capture","provider":"Banco Central do Brasil / BCData SGS","retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"series":{},"errors":[],"instrument_accounting_reconciliation":"NOT_DONE","trusted_feature_admission":"NOT_AUTHORIZED"}
for code,meta in SERIES.items():
 url=f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=csv"
 started=datetime.now(timezone.utc).isoformat()
 last=None
 for attempt in range(3):
  try:
   req=Request(url,headers={"User-Agent":"PRECISION-WIRES-BCB-instrument-audit/1.0","Accept":"text/csv, text/plain, */*"})
   with urlopen(req,timeout=60) as response:
    raw=response.read(); status=response.status
    headers={k.lower():v for k,v in response.headers.items()}
    final=response.geturl()
   if status!=200 or not raw: raise RuntimeError(f"HTTP {status} / empty body")
   if raw.lstrip().lower().startswith((b"<!doctype html",b"<html")): raise RuntimeError("HTML body, not CSV")
   raw.decode("utf-8-sig")
   path=OUT/f"sgs_{code}.csv"; path.write_bytes(raw)
   manifest["series"][code]={
    **meta,"requested_url":url,"final_url":final,"retrieval_started_at_utc":started,
    "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"http_status":status,
    "response_headers":headers,"content_type":headers.get("content-type"),
    "byte_length":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
    "raw_capture_status":"PASS","local_file":str(path)
   }
   break
  except (HTTPError,URLError,TimeoutError,OSError,RuntimeError,UnicodeDecodeError) as exc:
   last=repr(exc)
   if attempt<2: time.sleep(attempt+1)
 else:
  manifest["series"][code]={**meta,"requested_url":url,"retrieval_started_at_utc":started,"raw_capture_status":"BLOCKED","error":last}
  manifest["errors"].append(f"{code}: {last}")
passed=sum(x.get("raw_capture_status")=="PASS" for x in manifest["series"].values())
manifest["acceptance"]={"expected_series":8,"raw_capture_pass":passed,"all_eight_pass":passed==8,"date_value_qa":"NOT_RUN","instrument_sum_reconciliation":"NOT_DONE","domestic_external_debt_reconciliation":"NOT_DONE","country_period_qa":"NOT_DONE","production_integration":"NOT_AUTHORIZED"}
manifest["status"]="RAW_CAPTURE_8_OF_8_PASS" if passed==8 and not manifest["errors"] else "BLOCKED"
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
print(json.dumps(manifest,indent=2,sort_keys=True))
if manifest["status"]!="RAW_CAPTURE_8_OF_8_PASS": sys.exit(1)
