#!/usr/bin/env python3
"""Cross-check all April-2026 official IIP API records against the latest 28-Oct-2026 PIB revision."""
from __future__ import annotations
import hashlib, json, ssl
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPSHandler

BASE = "https://api.mospi.gov.in/api/iip/getIIPData"
PARAMS = {"frequency":"Monthly","base_year":"2022-23","year":"2026","month_code":"4","type":"All","viz_req":"true"}
PIB_URL = "https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475"
OUT = Path("artifacts/iip_api_pib_crosscheck_2026_04")
RAW = OUT / "raw"
RAW.mkdir(parents=True, exist_ok=True)
TLS_CONTEXT = ssl.create_default_context()
TLS_CONTEXT.set_ciphers("DEFAULT:@SECLEVEL=1")
TLS_CONTEXT.options |= 0x4  # Legacy renegotiation compatibility; certificate verification remains enabled.
OPENER = build_opener(HTTPSHandler(context=TLS_CONTEXT))
URL = BASE + "?" + urlencode(PARAMS)

# April-2026 revised index values transcribed from official PIB PRID 2329475,
# Statement I, Statement III and Statement IV (Base 2022-23=100).
EXPECTED = {
    ("General","General",""):118.2,
    ("Sectoral","Mining & Quarrying","Fuel Minerals"):95.9,
    ("Sectoral","Mining & Quarrying","Metallic Minerals incl. Rare Earth Minerals"):130.8,
    ("Sectoral","Mining & Quarrying","Non-Metallic Minerals incl. Minor Minerals"):108.5,
    ("Sectoral","Mining & Quarrying",""):106.1,
    ("Sectoral","Manufacturing","Manufacture of food products"):100.5,
    ("Sectoral","Manufacturing","Manufacture of beverages"):155.2,
    ("Sectoral","Manufacturing","Manufacture of tobacco products"):113.8,
    ("Sectoral","Manufacturing","Manufacture of textiles"):135.7,
    ("Sectoral","Manufacturing","Manufacture of wearing apparel"):91.0,
    ("Sectoral","Manufacturing","Manufacture of leather and related products"):99.8,
    ("Sectoral","Manufacturing","Manufacture of wood and products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials"):84.3,
    ("Sectoral","Manufacturing","Manufacture of paper and paper products"):115.0,
    ("Sectoral","Manufacturing","Printing and reproduction of recorded media"):103.8,
    ("Sectoral","Manufacturing","Manufacture of coke and refined petroleum products"):104.6,
    ("Sectoral","Manufacturing","Manufacture of chemicals and chemical products"):104.9,
    ("Sectoral","Manufacturing","Manufacture of basic pharmaceutical products and pharmaceutical preparations"):110.7,
    ("Sectoral","Manufacturing","Manufacture of rubber and plastics products"):125.8,
    ("Sectoral","Manufacturing","Manufacture of other non-metallic mineral products"):115.8,
    ("Sectoral","Manufacturing","Manufacture of basic metals"):128.9,
    ("Sectoral","Manufacturing","Manufacture of fabricated metal products, except machinery and equipment"):125.9,
    ("Sectoral","Manufacturing","Manufacture of computer, electronic and optical products"):137.9,
    ("Sectoral","Manufacturing","Manufacture of electrical equipment"):151.5,
    ("Sectoral","Manufacturing","Manufacture of machinery and equipment n.e.c."):109.9,
    ("Sectoral","Manufacturing","Manufacture of motor vehicles, trailers and semi-trailers"):130.4,
    ("Sectoral","Manufacturing","Manufacture of other transport equipment"):153.4,
    ("Sectoral","Manufacturing","Manufacture of furniture"):109.8,
    ("Sectoral","Manufacturing","Other manufacturing"):112.1,
    ("Sectoral","Manufacturing",""):118.7,
    ("Sectoral","Electricity & Gas Supply","Non-Renewable Electricity"):120.9,
    ("Sectoral","Electricity & Gas Supply","Renewable Electricity"):129.7,
    ("Sectoral","Electricity & Gas Supply","Electricity"):122.9,
    ("Sectoral","Electricity & Gas Supply","Gas Supply"):104.3,
    ("Sectoral","Electricity & Gas Supply",""):121.7,
    ("Sectoral","Water Supply, Sewerage & Waste Management","Water Supply"):156.2,
    ("Sectoral","Water Supply, Sewerage & Waste Management","Sewerage & Waste Management"):134.9,
    ("Sectoral","Water Supply, Sewerage & Waste Management",""):146.1,
    ("Use-based category","Primary Goods",""):113.7,
    ("Use-based category","Capital Goods",""):124.8,
    ("Use-based category","Intermediate Goods",""):123.7,
    ("Use-based category","Infrastructure/ Construction Goods",""):128.0,
    ("Use-based category","Consumer Durables",""):118.0,
    ("Use-based category","Consumer Non-durables",""):109.4,
}
def norm(v): return " ".join(str(v or "").strip().lower().split())
def key(row): return tuple(norm(row.get(k)) for k in ("type","category","sub_category"))
def sha(b): return hashlib.sha256(b).hexdigest()
report = {
    "source_url":URL,
    "official_comparison_source":PIB_URL,
    "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
    "request_parameters":PARAMS,
    "official_pib_reference":"PRID 2329475, 2026-10-28, latest IIP release; April-2026 revised values from Statement I, Statement III and Statement IV",
    "official_pib_locator":"Statement I line 109; Statement III line 197; Statement IV lines 220-260 (April-26 column)",
    "expected_official_records":len(EXPECTED),
}
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-IIP-PIB-crosscheck/1.0","Accept":"application/json"})
try:
    with OPENER.open(req,timeout=35) as response:
        body=response.read()
        report.update({"http_status":response.status,"content_type":response.headers.get("Content-Type",""),"response_bytes":len(body),"response_sha256":sha(body),"final_url":response.geturl()})
except Exception as exc:
    report.update({"status":"BLOCKED_REQUEST_ERROR","error":f"{type(exc).__name__}: {exc}"})
    (OUT/"iip_api_pib_crosscheck_2026_04.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
(RAW/"response.json").write_bytes(body)
try: payload=json.loads(body.decode("utf-8-sig"))
except Exception as exc:
    report.update({"status":"BLOCKED_INVALID_JSON","error":f"{type(exc).__name__}: {exc}"})
    (OUT/"iip_api_pib_crosscheck_2026_04.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
rows=payload.get("data") if isinstance(payload,dict) else None
if payload.get("statusCode") is not True or not isinstance(rows,list):
    report.update({"status":"BLOCKED_API_ENVELOPE_INVALID","api_message":payload.get("msg") if isinstance(payload,dict) else None})
    (OUT/"iip_api_pib_crosscheck_2026_04.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
expected={tuple(norm(x) for x in k):v for k,v in EXPECTED.items()}
observed={}
for row in rows:
    if str(row.get("base_year"))!="2022-23" or str(row.get("year"))!="2026" or norm(row.get("month"))!="april": continue
    k=key(row)
    if k in observed: report.setdefault("duplicate_keys",[]).append(k)
    observed[k]=row
missing=[]; mismatches=[]
for k,expected_value in expected.items():
    row=observed.get(k)
    if row is None:
        missing.append({"key":k,"expected_index":expected_value}); continue
    try: actual=round(float(row.get("index")),1)
    except Exception: actual=None
    if actual!=expected_value:
        mismatches.append({"key":k,"expected_index":expected_value,"api_index":row.get("index"),"api_growth_rate":row.get("growth_rate")})
extra=[k for k in observed if k not in expected]
report.update({
    "api_statusCode":payload.get("statusCode"),
    "api_message":payload.get("msg"),
    "meta_data":payload.get("meta_data",{}),
    "api_records_returned":len(rows),
    "valid_april_records":len(observed),
    "matched_official_pib_values":len(EXPECTED)-len(missing)-len(mismatches),
    "missing_expected_records":missing,
    "mismatches":mismatches,
    "unexpected_records":extra,
    "duplicate_keys":report.get("duplicate_keys",[]),
    "rounding_policy":"API index values rounded to one decimal before comparison with official PIB values published to one decimal; no growth rates recomputed.",
    "status":"PASS_ALL_43_MATCH" if len(observed)==len(EXPECTED) and not missing and not mismatches and not extra and not report.get("duplicate_keys") else "BLOCKED_PIB_API_MISMATCH",
    "interpretation":"This verifies April-2026 API values against the latest official 28-Oct-2026 PIB revised values. It is a separate API provenance check and does not claim recovery of the catalogue-native XLSX. Keep the old 1-Jun quick-estimate PIB crosswalk separately labelled QUICK_ESTIMATE.",
    "hard_gate":"BLOCKED",
})
(OUT/"iip_api_pib_crosscheck_2026_04.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2,ensure_ascii=False))
if report["status"]!="PASS_ALL_43_MATCH": raise SystemExit(2)
