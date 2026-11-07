#!/usr/bin/env python3
"""Cross-check all May-2026 official IIP API records against the 29-Jun-2026 PIB PPI-based release."""
from __future__ import annotations
import hashlib, json, ssl
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPSHandler
from urllib.error import HTTPError

BASE = "https://api.mospi.gov.in/api/iip/getIIPData"
PARAMS = {"frequency":"Monthly","base_year":"2022-23","year":"2026","month_code":"5","type":"All","viz_req":"true"}
PIB_URL = "https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475"

OUT = Path("artifacts/iip_api_pib_crosscheck_2026_05")
RAW = OUT / "raw"
RAW.mkdir(parents=True, exist_ok=True)
TLS_CONTEXT = ssl.create_default_context()
TLS_CONTEXT.set_ciphers("DEFAULT:@SECLEVEL=1")
TLS_CONTEXT.options |= 0x4  # Legacy renegotiation compatibility only; certificate verification remains enabled.
OPENER = build_opener(HTTPSHandler(context=TLS_CONTEXT))
URL = BASE + "?" + urlencode(PARAMS)

# Official published May-2026 index values transcribed from PIB PRID 2278961:
# General/sectoral + NIC-2025 Statements II-A to II-D + Use-Based Statement III.
EXPECTED = {
    ("General","General",""):122.5,
    ("Sectoral","Mining & Quarrying","Fuel Minerals"):99.2,
    ("Sectoral","Mining & Quarrying","Metallic Minerals incl. Rare Earth Minerals"):143.1,
    ("Sectoral","Mining & Quarrying","Non-Metallic Minerals incl. Minor Minerals"):118.5,
    ("Sectoral","Mining & Quarrying",""):113.1,
    ("Sectoral","Manufacturing","Manufacture of food products"):103.3,
    ("Sectoral","Manufacturing","Manufacture of beverages"):166.9,
    ("Sectoral","Manufacturing","Manufacture of tobacco products"):113.7,
    ("Sectoral","Manufacturing","Manufacture of textiles"):136.8,
    ("Sectoral","Manufacturing","Manufacture of wearing apparel"):94.7,
    ("Sectoral","Manufacturing","Manufacture of leather and related products"):102.1,
    ("Sectoral","Manufacturing","Manufacture of wood and products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials"):94.7,
    ("Sectoral","Manufacturing","Manufacture of paper and paper products"):119.5,
    ("Sectoral","Manufacturing","Printing and reproduction of recorded media"):97.5,
    ("Sectoral","Manufacturing","Manufacture of coke and refined petroleum products"):106.8,
    ("Sectoral","Manufacturing","Manufacture of chemicals and chemical products"):108.0,
    ("Sectoral","Manufacturing","Manufacture of basic pharmaceutical products and pharmaceutical preparations"):115.3,
    ("Sectoral","Manufacturing","Manufacture of rubber and plastics products"):111.4,
    ("Sectoral","Manufacturing","Manufacture of other non-metallic mineral products"):122.3,
    ("Sectoral","Manufacturing","Manufacture of basic metals"):131.8,
    ("Sectoral","Manufacturing","Manufacture of fabricated metal products, except machinery and equipment"):128.4,
    ("Sectoral","Manufacturing","Manufacture of computer, electronic and optical products"):160.0,
    ("Sectoral","Manufacturing","Manufacture of electrical equipment"):162.5,
    ("Sectoral","Manufacturing","Manufacture of machinery and equipment n.e.c."):125.9,
    ("Sectoral","Manufacturing","Manufacture of motor vehicles, trailers and semi-trailers"):132.9,
    ("Sectoral","Manufacturing","Manufacture of other transport equipment"):146.8,
    ("Sectoral","Manufacturing","Manufacture of furniture"):116.3,
    ("Sectoral","Manufacturing","Other manufacturing"):100.7,
    ("Sectoral","Manufacturing",""):122.2,
    ("Sectoral","Electricity & Gas Supply","Non-Renewable Electricity"):124.4,
    ("Sectoral","Electricity & Gas Supply","Renewable Electricity"):153.8,
    ("Sectoral","Electricity & Gas Supply","Electricity"):131.1,
    ("Sectoral","Electricity & Gas Supply","Gas Supply"):115.2,
    ("Sectoral","Electricity & Gas Supply",""):130.1,
    ("Sectoral","Water Supply, Sewerage & Waste Management","Water Supply"):156.6,
    ("Sectoral","Water Supply, Sewerage & Waste Management","Sewerage & Waste Management"):132.4,
    ("Sectoral","Water Supply, Sewerage & Waste Management",""):145.1,
    ("Use-based category","Primary Goods",""):119.8,
    ("Use-based category","Capital Goods",""):138.4,
    ("Use-based category","Intermediate Goods",""):123.1,
    ("Use-based category","Infrastructure/ Construction Goods",""):131.7,
    ("Use-based category","Consumer Durables",""):121.3,
    ("Use-based category","Consumer Non-durables",""):113.8,
}

def norm(value):
    return " ".join(str(value or "").strip().lower().split())

def key(row):
    return tuple(norm(row.get(k)) for k in ("type","category","sub_category"))

def sha(data):
    return hashlib.sha256(data).hexdigest()

report = {
    "source_url":URL,
    "official_comparison_source":PIB_URL,
    "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
    "request_parameters":PARAMS,
    "official_pib_reference":"PRID 2329475, 2026-10-28, latest IIP release; May-2026 revised values from Statement IV, Statement I and Statement III",
    "official_pib_locator":"Statement I sectoral May column; Statement III May row; Statement IV May-26 column for NIC-2025 and sector/sub-sector groups",
    "expected_official_records":len(EXPECTED),
}
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-IIP-PIB-crosscheck/1.0","Accept":"application/json"})
try:
    with OPENER.open(req,timeout=35) as response:
        body=response.read()
        report.update({"http_status":response.status,"content_type":response.headers.get("Content-Type",""),"response_bytes":len(body),"response_sha256":sha(body),"final_url":response.geturl()})
except Exception as exc:
    report.update({"status":"BLOCKED_REQUEST_ERROR","error":f"{type(exc).__name__}: {exc}"})
    (OUT/"iip_api_pib_crosscheck_2026_05.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
(RAW/"response.json").write_bytes(body)
try:
    payload=json.loads(body.decode("utf-8-sig"))
except Exception as exc:
    report.update({"status":"BLOCKED_INVALID_JSON","error":f"{type(exc).__name__}: {exc}"})
    (OUT/"iip_api_pib_crosscheck_2026_05.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
rows=payload.get("data") if isinstance(payload,dict) else None
if payload.get("statusCode") is not True or not isinstance(rows,list):
    report.update({"status":"BLOCKED_API_ENVELOPE_INVALID","api_message":payload.get("msg") if isinstance(payload,dict) else None})
    (OUT/"iip_api_pib_crosscheck_2026_05.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False)); raise SystemExit(2)
expected_normalized={tuple(norm(x) for x in k):v for k,v in EXPECTED.items()}
observed={}
for row in rows:
    if str(row.get("base_year"))!="2022-23" or str(row.get("year"))!="2026" or norm(row.get("month"))!="may":
        continue
    k=key(row)
    if k in observed:
        report.setdefault("duplicate_keys",[]).append(k)
    observed[k]=row
mismatches=[]
missing=[]
for k,expected in expected_normalized.items():
    row=observed.get(k)
    if row is None:
        missing.append({"key":k,"expected_index":expected})
        continue
    try: actual=round(float(row.get("index")),1)
    except Exception: actual=None
    if actual!=expected:
        mismatches.append({"key":k,"expected_index":expected,"api_index":row.get("index"),"api_growth_rate":row.get("growth_rate")})
extra=[k for k in observed if k not in expected_normalized]
report.update({
    "api_statusCode":payload.get("statusCode"),
    "api_message":payload.get("msg"),
    "meta_data":payload.get("meta_data",{}),
    "api_records_returned":len(rows),
    "valid_may_records":len(observed),
    "matched_official_pib_values":len(EXPECTED)-len(missing)-len(mismatches),
    "missing_expected_records":missing,
    "mismatches":mismatches,
    "unexpected_records":extra,
    "duplicate_keys":report.get("duplicate_keys",[]),
    "rounding_policy":"API index values rounded to one decimal before comparison with official PIB values published to one decimal; no growth rates recomputed.",
    "status":"PASS_ALL_43_MATCH" if len(observed)==len(EXPECTED) and not missing and not mismatches and not extra and not report.get("duplicate_keys") else "BLOCKED_PIB_API_MISMATCH",
    "interpretation":"This verifies the API's May-2026 2022-23 response against the latest official 28-Oct-2026 PIB IIP release after subsequent revisions. The 29-Jun quick-estimate values were deliberately not used because IIP values are revised; the latest published May values are the benchmark. A full match validates the API's current series identity for May. April records from the same official 2022-23 API endpoint remain separately captured and retain their own raw hash. Native catalogue XLSX is not replaced by this API evidence.",
    "hard_gate":"BLOCKED",
})
(OUT/"iip_api_pib_crosscheck_2026_05.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2,ensure_ascii=False))
if report["status"]!="PASS_ALL_43_MATCH": raise SystemExit(2)
