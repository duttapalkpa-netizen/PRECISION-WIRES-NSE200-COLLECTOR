#!/usr/bin/env python3
"""Capture official BCB SGS priority-series CSV bytes; research-only, no accounting transforms."""
from __future__ import annotations
import csv
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OUT = Path("bcb_priority_capture")
OUT.mkdir(parents=True, exist_ok=True)

SERIES = {
    "22905": {
        "title": "Portfolio investment - monthly - net",
        "dataset": "https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net",
    },
    "22906": {
        "title": "Portfolio investment - Net acquisition of financial assets - monthly - net",
        "dataset": "https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net",
    },
    "22907": {
        "title": "Portfolio investment - Net acquisition of financial assets - monthly - inflows",
        "dataset": "https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows",
    },
    "22908": {
        "title": "Portfolio investment - Net acquisition of financial assets - monthly - outflows",
        "dataset": "https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows",
    },
    "22924": {
        "title": "Portfolio investment - Net incurrence of liabilities - monthly - net",
        "dataset": "https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net",
    },
    "22925": {
        "title": "Portfolio investment - Net incurrence of liabilities - monthly - inflows",
        "dataset": "https://opendata.bcb.gov.br/dataset/22925-portfolio-investment---net-incurrence-of-liabilities---monthly---inflows",
    },
    "22926": {
        "title": "Portfolio investment - Net incurrence of liabilities - monthly - outflows",
        "dataset": "https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows",
    },
}

def csv_url(code: str) -> str:
    if code not in SERIES:
        raise ValueError(f"Unapproved SGS code: {code}")
    return f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=csv"

def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()

manifest = {
    "schema_version": 1,
    "purpose": "research_only_raw_observation_capture",
    "provider": "Banco Central do Brasil / BCData SGS",
    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    "series": {},
    "acceptance": {},
    "errors": [],
    "accounting_sign_reconciliation": "NOT_DONE",
    "combined_flow_calculation": "NOT_AUTHORIZED",
}
for code, meta in SERIES.items():
    name = f"sgs_{code}.csv"
    url = csv_url(code)
    started = datetime.now(timezone.utc).isoformat()
    try:
        request = Request(
            url,
            headers={
                "User-Agent": "PRECISION-WIRES-BCB-research-capture/1.0",
                "Accept": "text/csv, text/plain, */*",
            },
        )
        last_error = None
        for attempt in range(3):
            try:
                with urlopen(request, timeout=60) as response:
                    payload = response.read()
                    status = response.status
                    headers = {k.lower(): v for k, v in response.headers.items()}
                    final_url = response.geturl()
                if status != 200:
                    raise RuntimeError(f"HTTP status {status}")
                if not payload:
                    raise RuntimeError("empty response body")
                if payload.lstrip().lower().startswith((b"<!doctype html", b"<html")):
                    raise RuntimeError("HTML error page received instead of CSV")
                # UTF-8 decode is a transport sanity check only; raw bytes remain authoritative.
                decoded = payload.decode("utf-8-sig")
                sample = decoded[:8192]
                delimiter = None
                try:
                    delimiter = csv.Sniffer().sniff(sample, delimiters=",;\\t|").delimiter
                except csv.Error:
                    pass
                path = OUT / name
                path.write_bytes(payload)
                manifest["series"][code] = {
                    "title": meta["title"],
                    "dataset_page_url": meta["dataset"],
                    "requested_url": url,
                    "final_url": final_url,
                    "retrieval_started_at_utc": started,
                    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                    "http_status": status,
                    "response_headers": headers,
                    "content_type": headers.get("content-type"),
                    "byte_length": len(payload),
                    "sha256": sha256_bytes(payload),
                    "local_file": str(path),
                    "utf8_decode": "PASS",
                    "sniffed_delimiter": delimiter,
                    "raw_capture_status": "PASS",
                }
                break
            except (HTTPError, URLError, TimeoutError, OSError, RuntimeError, UnicodeDecodeError) as exc:
                last_error = repr(exc)
                if attempt < 2:
                    time.sleep(attempt + 1)
        else:
            raise RuntimeError(last_error or "capture failed")
    except Exception as exc:
        manifest["series"][code] = {
            "title": meta["title"],
            "dataset_page_url": meta["dataset"],
            "requested_url": url,
            "retrieval_started_at_utc": started,
            "raw_capture_status": "BLOCKED",
            "error": str(exc),
        }
        manifest["errors"].append(f"SGS {code}: {exc}")

passed = sum(1 for item in manifest["series"].values() if item.get("raw_capture_status") == "PASS")
manifest["acceptance"] = {
    "priority_series_expected": len(SERIES),
    "priority_series_raw_capture_pass": passed,
    "all_seven_raw_capture_pass": passed == len(SERIES),
    "http_response_metadata_recorded_for_passes": passed,
    "sha256_recorded_for_passes": passed,
    "date_level_observation_qa": "NOT_RUN",
    "accounting_sign_reconciliation": "NOT_DONE",
    "country_period_qa": "NOT_DONE",
    "brazil_pilot_acceptance": "NOT_ACCEPTED",
    "em_wide_panel": "NOT_DONE",
    "production_integration": "NOT_AUTHORIZED",
}
manifest["status"] = "RAW_CAPTURE_7_OF_7_PASS" if passed == len(SERIES) and not manifest["errors"] else "BLOCKED"
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, sort_keys=True))
if manifest["status"] != "RAW_CAPTURE_7_OF_7_PASS":
    sys.exit(1)
