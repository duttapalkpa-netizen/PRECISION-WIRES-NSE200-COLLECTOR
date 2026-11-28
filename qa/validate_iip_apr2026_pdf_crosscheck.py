#!/usr/bin/env python3
"""Offline QA for the April-2026 NIC-2025 first-release ledger.

Later-vintage values are retained as raw observations but quarantined because
the matching official monthwise table explicitly declares base 2011-12=100.
No cross-base-year revision arithmetic is permitted.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path

EXPECTED_CODES = [f"{n:02d}" for n in range(10, 33)]
EXPECTED_IDS = ["IIPMFY26006MAY", "IIPMFY26010JUN", "IIPMFY26018AUG"]
EXPECTED_FIRST_RELEASE_VALUES = {
    "10": 101.0, "11": 152.8, "12": 116.6, "13": 132.6, "14": 91.6,
    "15": 98.3, "16": 83.6, "17": 116.0, "18": 106.8, "19": 104.1,
    "20": 104.4, "21": 117.5, "22": 107.6, "23": 116.0, "24": 130.0,
    "25": 124.3, "26": 138.7, "27": 150.6, "28": 122.5, "29": 130.8,
    "30": 148.4, "31": 111.1, "32": 124.6,
}
EXPECTED_DATES = ["29 Jun 2026", "28 Jul 2026", "28 Sep 2026"]
EXPECTED_URL = (
    "https://www.mospi.gov.in/uploads/latestReleases/"
    "latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_"
    "Press_Release_IIP_2022-23f.pdf"
)
LATER_SOURCE_URL = "https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616"
REQUIRED = {
    "reference_period", "base_year", "classification", "nic_code",
    "first_release_index", "first_release_date", "source_type",
    "source_table", "source_page", "source_url", "raw_pdf_sha256",
    "later_vintage_ids", "later_vintage_release_dates",
    "later_vintage_index_values", "latest_later_index",
    "revision_delta_latest_minus_first", "revision_detected",
    "later_vintage_assessment", "evidence_status",
    "later_vintage_source_base_year", "later_vintage_source_table",
    "later_vintage_source_url",
    "first_release_deflator", "first_release_series_status",
    "superseded_by_release_id", "superseding_release_date",
    "superseding_deflator", "current_series_apr2026_index_status",
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
            ("later_vintage_source_base_year", "2011-12"),
            ("later_vintage_source_table", "INDEX OF INDUSTRIAL PRODUCTION - MONTHWISE"),
            ("later_vintage_source_url", LATER_SOURCE_URL),
            ("later_vintage_assessment", "SOURCE_BASE_YEAR_MISMATCH_NOT_COMPARABLE"),
            ("revision_detected", "UNKNOWN"),
            ("first_release_deflator", "WPI"),
            ("first_release_series_status", "SUPERSEDED_BY_OUTPUT_PPI_SERIES"),
            ("superseded_by_release_id", "IIPMFY26006MAY"),
            ("superseding_release_date", "2026-06-29"),
            ("superseding_deflator", "Output PPI"),
            ("current_series_apr2026_index_status", "NOT_YET_EXTRACTED_FROM_COMPARABLE_CURRENT_SERIES_SOURCE"),
        ):
            if row.get(key, "").strip() != expected:
                errors.append(prefix + f"{key} must equal {expected!r}")

        try:
            first_value = float(row.get("first_release_index", "").strip())
            expected_first_value = EXPECTED_FIRST_RELEASE_VALUES.get(row.get("nic_code", "").strip())
            if expected_first_value is None or first_value != expected_first_value:
                errors.append(prefix + f"first_release_index must match official first-release Statement II-A value {expected_first_value}")
        except (ValueError, TypeError):
            errors.append(prefix + "first_release_index must be numeric")

        if row.get("latest_later_index", "").strip():
            errors.append(prefix + "latest_later_index must be blank for cross-base-year evidence")
        if row.get("revision_delta_latest_minus_first", "").strip():
            errors.append(prefix + "revision delta must be blank for cross-base-year evidence")

        ids = row.get("later_vintage_ids", "").split(";")
        dates = row.get("later_vintage_release_dates", "").split(";")
        values_text = row.get("later_vintage_index_values", "").split(";")
        if ids != EXPECTED_IDS:
            errors.append(prefix + "later vintage IDs/order mismatch")
        if dates != EXPECTED_DATES:
            errors.append(prefix + "later vintage release dates/order mismatch")
        try:
            values = [float(value) for value in values_text]
            if len(values) != 3:
                errors.append(prefix + "expected three preserved raw monthwise observations")
        except ValueError:
            errors.append(prefix + "non-numeric preserved source observation")

        status = row.get("evidence_status", "")
        required_statuses = (
            "RUN245_XLSX_NOT_COMPARABLE_BASEYEAR_CLASSIFICATION_MISMATCH",
            "LATER_VALUES_MATCH_2011_12_MONTHWISE_TABLE",
            "REVISION_STATUS_UNKNOWN_NOT_COMPARABLE",
        )
        for marker in required_statuses:
            if marker not in status:
                errors.append(prefix + f"evidence status must retain {marker}")

        raw_hash = row.get("raw_pdf_sha256", "").strip().lower()
        pending_marker = "RAW_PDF_SHA256_PENDING" in status
        if pending_marker and raw_hash:
            errors.append(prefix + "raw_pdf_sha256 must remain blank while evidence status is pending")
        if not pending_marker and not raw_hash:
            errors.append(prefix + "a missing raw_pdf_sha256 must retain RAW_PDF_SHA256_PENDING")
        if raw_hash and not re.fullmatch(r"[0-9a-f]{64}", raw_hash):
            errors.append(prefix + "raw_pdf_sha256 must be 64 lowercase hex characters")

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
    print("QA_PASS rows=23 nic_codes=10-32 later_values_quarantined=2011-12")
    print("revision_status=UNKNOWN_CROSS_BASE_YEAR_NOT_COMPARABLE")
    print(f"raw_pdf_sha256_status={'PRESENT' if all(r.get('raw_pdf_sha256','').strip() for r in csv.DictReader(args.csv_path.open(encoding='utf-8-sig'))) else 'PENDING_PROVISIONAL'}")
    print(f"ledger_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
