#!/usr/bin/env python3
"""Offline QA for the April-2026 NIC-2025 first-release cross-check ledger.

This validator never downloads, infers, or backfills source values. A missing raw
PDF SHA-256 is permitted only while the ledger explicitly remains provisional.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path

EXPECTED_CODES = [f"{n:02d}" for n in range(10, 33)]
EXPECTED_IDS = ["IIPMFY26006MAY", "IIPMFY26010JUN", "IIPMFY26018AUG"]
EXPECTED_DATES = ["29 Jun 2026", "28 Jul 2026", "28 Sep 2026"]
EXPECTED_URL = (
    "https://www.mospi.gov.in/uploads/latestReleases/"
    "latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_"
    "Press_Release_IIP_2022-23f.pdf"
)
REQUIRED = {
    "reference_period", "base_year", "classification", "nic_code",
    "first_release_index", "first_release_date", "source_type",
    "source_table", "source_page", "source_url", "raw_pdf_sha256",
    "later_vintage_ids", "later_vintage_release_dates",
    "later_vintage_index_values", "latest_later_index",
    "revision_delta_latest_minus_first", "revision_detected",
    "later_vintage_assessment", "evidence_status",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - fields)
        if missing:
            return [f"missing required columns: {', '.join(missing)}"]
        rows = list(reader)

    if len(rows) != 23:
        errors.append(f"expected 23 rows; found {len(rows)}")
    codes = [row["nic_code"].strip() for row in rows]
    if codes != EXPECTED_CODES:
        errors.append("NIC codes must be exactly 10 through 32, in ascending order, once each")

    for line, row in enumerate(rows, start=2):
        prefix = f"line {line} NIC {row.get('nic_code', '?')}: "
        for key, expected in (
            ("reference_period", "2026-04"),
            ("base_year", "2022-23"),
            ("classification", "NIC-2025"),
            ("first_release_date", "2026-06-01"),
            ("source_type", "OFFICIAL_MOSPI_PRESS_RELEASE_PDF"),
            ("source_table", "STATEMENT II A"),
            ("source_page", "5"),
            ("source_url", EXPECTED_URL),
        ):
            if row.get(key, "").strip() != expected:
                errors.append(prefix + f"{key} must equal {expected!r}")

        ids = row.get("later_vintage_ids", "").split(";")
        dates = row.get("later_vintage_release_dates", "").split(";")
        values_text = row.get("later_vintage_index_values", "").split(";")
        if ids != EXPECTED_IDS:
            errors.append(prefix + "later vintage IDs/order mismatch")
        if dates != EXPECTED_DATES:
            errors.append(prefix + "later vintage release dates/order mismatch")
        try:
            parsed_dates = [datetime.strptime(value, "%d %b %Y") for value in dates]
            if parsed_dates != sorted(parsed_dates):
                errors.append(prefix + "later vintage dates are not chronological")
        except ValueError:
            errors.append(prefix + "invalid later vintage date")

        try:
            first = float(row["first_release_index"])
            values = [float(value) for value in values_text]
            latest = float(row["latest_later_index"])
            delta = float(row["revision_delta_latest_minus_first"])
            if len(values) != 3:
                errors.append(prefix + "exactly three later index values required")
            elif len(set(values)) != 1:
                errors.append(prefix + "three later vintage values must agree for this ledger status")
            if values and abs(latest - values[-1]) > 1e-9:
                errors.append(prefix + "latest_later_index does not match final chronological value")
            if abs(delta - (latest - first)) > 1e-9:
                errors.append(prefix + "revision delta arithmetic mismatch")
            expected_revision = abs(latest - first) > 1e-9
            if row["revision_detected"].strip().upper() != str(expected_revision).upper():
                errors.append(prefix + "revision_detected flag mismatch")
            if not expected_revision:
                errors.append(prefix + "expected first-release revision for this evidence ledger")
        except (TypeError, ValueError):
            errors.append(prefix + "non-numeric index or revision field")

        raw_hash = row.get("raw_pdf_sha256", "").strip().lower()
        status = row.get("evidence_status", "")
        if raw_hash:
            if not re.fullmatch(r"[0-9a-f]{64}", raw_hash):
                errors.append(prefix + "raw_pdf_sha256 must be 64 lowercase hex characters")
        elif "RAW_PDF_SHA256_PENDING" not in status:
            errors.append(prefix + "blank raw PDF hash must remain explicitly pending")
        if row.get("later_vintage_assessment") != "3_LATER_VINTAGES_AGREE_CHRONOLOGICAL_ORDER":
            errors.append(prefix + "later vintage assessment label mismatch")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    errors = validate(args.csv_path)
    if errors:
        for error in errors:
            print("FAIL:", error)
        print(f"QA_FAIL errors={len(errors)}")
        return 1
    digest = hashlib.sha256(args.csv_path.read_bytes()).hexdigest()
    print("QA_PASS rows=23 nic_codes=10-32 chronological_vintages=3")
    print(f"raw_pdf_sha256_status={'PRESENT' if all(r.get('raw_pdf_sha256','').strip() for r in csv.DictReader(args.csv_path.open(encoding='utf-8-sig'))) else 'PENDING_PROVISIONAL'}")
    print(f"ledger_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
