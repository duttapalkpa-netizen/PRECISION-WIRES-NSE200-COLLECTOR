#!/usr/bin/env python3
"""Capture immutable point-in-time snapshots of selected BCB SGS monthly series.

Research-only. Each execution writes to a unique UTC timestamp directory; raw
responses are never overwritten. The snapshot is a current-vintage observation,
not an original publication vintage.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CODES = {
    "22924": "portfolio investment liabilities - net (aggregate comparator)",
    "22930": "domestic-market equity liabilities - net",
    "22936": "investment-fund liabilities - net (market perimeter documented in Table 10 footnote)",
    "22942": "domestic-market debt securities liabilities - net (target discrepancy series)",
}
BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=csv"
USER_AGENT = "PRECISION-WIRES-NSE200-COLLECTOR research-only vintage capture/1.0"


def parse_csv(raw: bytes, code: str) -> dict:
    text = raw.decode("utf-8-sig")
    reader = csv.reader(io.StringIO(text), delimiter=";", quotechar='"')
    rows = list(reader)
    if not rows or [x.strip().lower() for x in rows[0]] != ["data", "valor"]:
        raise ValueError(f"SGS {code}: unexpected CSV header: {rows[0] if rows else 'EMPTY'}")
    values = {}
    previous = None
    for line_no, row in enumerate(rows[1:], start=2):
        if len(row) != 2:
            raise ValueError(f"SGS {code}: malformed row {line_no}: {row!r}")
        date_raw, value_raw = row[0].strip(), row[1].strip()
        date = datetime.strptime(date_raw, "%d/%m/%Y").date()
        key = date.strftime("%Y-%m")
        if key in values:
            raise ValueError(f"SGS {code}: duplicate month {key}")
        if previous and date < previous:
            raise ValueError(f"SGS {code}: dates not ascending at {date_raw}")
        previous = date
        try:
            value = Decimal(value_raw.replace(".", "").replace(",", "."))
        except InvalidOperation as exc:
            raise ValueError(f"SGS {code}: invalid numeric value {value_raw!r}") from exc
        values[key] = {"date": date.isoformat(), "value": str(value)}
    if not values:
        raise ValueError(f"SGS {code}: no observations")
    return {
        "row_count": len(values),
        "first_period": min(values),
        "last_period": max(values),
        "target_2026_02": values.get("2026-02"),
        "latest_observation": values[max(values)],
        "latest_period": max(values),
        "values": values,
    }


def capture(code: str) -> tuple[bytes, dict]:
    url = BASE_URL.format(code=code)
    started = datetime.now(timezone.utc)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/csv"})
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            raw = response.read()
            status = response.status
            headers = {k.lower(): v for k, v in response.headers.items()}
            final_url = response.geturl()
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"SGS {code}: HTTP {exc.code}") from exc
    ended = datetime.now(timezone.utc)
    if status != 200 or not raw:
        raise RuntimeError(f"SGS {code}: HTTP {status} or empty body")
    if "csv" not in headers.get("content-type", "").lower():
        raise RuntimeError(f"SGS {code}: unexpected Content-Type {headers.get('content-type')}")
    parsed = parse_csv(raw, code)
    meta = {
        "sgs_code": code,
        "series_description": CODES[code],
        "requested_url": url,
        "final_url": final_url,
        "http_status": status,
        "response_headers": headers,
        "retrieval_started_at_utc": started.isoformat(),
        "retrieved_at_utc": ended.isoformat(),
        "byte_length": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "content_type": headers.get("content-type"),
        "csv_validation": "PASS",
        "observation_summary": {k: v for k, v in parsed.items() if k != "values"},
        "observations": parsed["values"],
    }
    return raw, meta


def main() -> None:
    started = datetime.now(timezone.utc)
    snapshot_id = started.strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "data" / "raw" / "bcb" / "sgs_vintage_snapshots" / snapshot_id
    out_dir.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema_version": 1,
        "purpose": "prospective_point_in_time_bcb_sgs_vintage_archive",
        "snapshot_id_utc": snapshot_id,
        "captured_at_utc": started.isoformat(),
        "provider": "Banco Central do Brasil / BCData SGS",
        "scope": "Research-only; four series retained as separate raw files",
        "vintage_semantics": "This records the current SGS response as observed at retrieval time. It is not a reconstructed original publication vintage.",
        "series": {},
        "acceptance": "IN_PROGRESS",
        "errors": [],
    }
    for code in CODES:
        raw, meta = capture(code)
        (out_dir / f"sgs_{code}.csv").write_bytes(raw)
        manifest["series"][code] = meta
        print(f"PASS SGS {code}: {meta['byte_length']} bytes; sha256={meta['sha256']}; periods={meta['observation_summary']['row_count']}")
    manifest["acceptance"] = "PASS_4_OF_4"
    manifest["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"SNAPSHOT_DIR={out_dir.relative_to(ROOT)}")
    print(f"SNAPSHOT_MANIFEST_SHA256={hashlib.sha256(manifest_path.read_bytes()).hexdigest()}")
    print(f"SNAPSHOT_STATUS={manifest['acceptance']}")


if __name__ == "__main__":
    main()
