#!/usr/bin/env python3
"""One-shot, read-only probe of the official e-Sankhyiki IIP API for April 2026."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPSHandler
from urllib.error import HTTPError, URLError
import ssl

BASE = "https://api.mospi.gov.in/api/iip/getIIPData"
PARAMS = {
    "frequency": "Monthly",
    "base_year": "2022-23",
    "year": "2026",
    "month_code": "4",
    "type": "All",
    "viz_req": "true",
}
OUT = Path("artifacts/iip_api_apr2026")
RAW = OUT / "raw"
RAW.mkdir(parents=True, exist_ok=True)
URL = BASE + "?" + urlencode(PARAMS)
TLS_CONTEXT = ssl.create_default_context()
TLS_CONTEXT.set_ciphers("DEFAULT:@SECLEVEL=1")
TLS_CONTEXT.options |= 0x4  # Permit legacy server renegotiation; certificate verification stays enabled.
OPENER = build_opener(HTTPSHandler(context=TLS_CONTEXT))
retrieved = datetime.now(timezone.utc).isoformat()

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

request = Request(
    URL,
    headers={
        "User-Agent": "PRECISION-WIRES-IIP-API-source-probe/1.0",
        "Accept": "application/json",
    },
)
report = {
    "source_url": URL,
    "retrieved_at_utc": retrieved,
    "request_parameters": PARAMS,
    "data_api_called": True,
    "source_format": "official_json_api",
    "native_xlsx_recovered": False,
    "methodology_vintage": "NOT_EXPLICITLY_IDENTIFIED_IN_API_RESPONSE",
    "hard_gate": "BLOCKED",
}
try:
    with OPENER.open(request, timeout=35) as response:
        body = response.read()
        report.update({
            "http_status": response.status,
            "content_type": response.headers.get("Content-Type", ""),
            "final_url": response.geturl(),
            "response_bytes": len(body),
            "response_sha256": sha256(body),
        })
except HTTPError as exc:
    body = exc.read()
    (RAW / "http_error_body.bin").write_bytes(body)
    report.update({
        "status": "BLOCKED_HTTP_ERROR",
        "http_status": exc.code,
        "content_type": exc.headers.get("Content-Type", ""),
        "response_bytes": len(body),
        "response_sha256": sha256(body),
        "error": f"HTTPError: {exc.code}",
    })
    (OUT / "iip_api_apr2026_probe_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(2)
except Exception as exc:
    report.update({
        "status": "BLOCKED_REQUEST_ERROR",
        "error": f"{type(exc).__name__}: {exc}",
    })
    (OUT / "iip_api_apr2026_probe_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(2)

(RAW / "response.json").write_bytes(body)
try:
    payload = json.loads(body.decode("utf-8-sig"))
except Exception as exc:
    report.update({
        "status": "BLOCKED_INVALID_JSON",
        "error": f"{type(exc).__name__}: {exc}",
    })
    (OUT / "iip_api_apr2026_probe_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(2)

rows = payload.get("data") if isinstance(payload, dict) else None
meta = payload.get("meta_data", {}) if isinstance(payload, dict) else {}
if not isinstance(rows, list) or payload.get("statusCode") is not True:
    report.update({
        "status": "BLOCKED_API_ENVELOPE_INVALID_OR_UNSUCCESSFUL",
        "api_message": payload.get("msg") if isinstance(payload, dict) else None,
        "api_statusCode": payload.get("statusCode") if isinstance(payload, dict) else None,
    })
    (OUT / "iip_api_apr2026_probe_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(2)

def normalized_month(value):
    return str(value or "").strip().lower()

def valid_row(row):
    base = str(row.get("base_year", "")).strip()
    year = str(row.get("year", "")).strip()
    month = normalized_month(row.get("month"))
    month_code = str(row.get("month_code", "")).strip()
    return base == "2022-23" and year == "2026" and (month == "april" or month_code == "4")

invalid = [i for i, row in enumerate(rows) if not isinstance(row, dict) or not valid_row(row)]
required = ("base_year", "year", "month", "type", "category", "sub_category", "index", "growth_rate")
missing_fields = sorted({field for row in rows if isinstance(row, dict) for field in required if field not in row})
report.update({
    "api_message": payload.get("msg"),
    "api_statusCode": payload.get("statusCode"),
    "meta_data": meta,
    "record_count": len(rows),
    "invalid_filter_rows": invalid,
    "missing_expected_fields": missing_fields,
    "record_types": sorted({str(r.get("type")) for r in rows if isinstance(r, dict)}),
    "record_categories_count": len({str(r.get("category")) for r in rows if isinstance(r, dict)}),
    "sample_records": rows[:5],
    "methodology_caveat": "The API schema confirms base_year 2022-23 and monthly filters, but the returned record schema does not identify the deflator or release vintage. Do not label these rows Output-PPI-vintage until reconciled with the official 29-Jun-2026 superseding release.",
    "native_xlsx_recovered": False,
    "hard_gate": "BLOCKED",
})
if not rows:
    report["status"] = "BLOCKED_NO_MATCHING_RECORDS"
elif invalid or missing_fields:
    report["status"] = "BLOCKED_RESPONSE_CONTRACT_MISMATCH"
else:
    report["status"] = "PASS_FILTERED_OFFICIAL_API_ROWS_RETURNED_SOURCE_VINTAGE_RECONCILIATION_PENDING"

(OUT / "iip_api_apr2026_probe_audit.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2, ensure_ascii=False))
if report["status"] != "PASS_FILTERED_OFFICIAL_API_ROWS_RETURNED_SOURCE_VINTAGE_RECONCILIATION_PENDING":
    raise SystemExit(2)
