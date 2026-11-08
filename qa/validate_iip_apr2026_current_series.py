#!/usr/bin/env python3
"""Offline QA for extracted April-2026 current-series NIC-2025 IIP observations."""
from __future__ import annotations
import argparse, csv, hashlib, re
from pathlib import Path

EXPECTED_CODES = [str(n) for n in range(10, 33)]
EXPECTED_INDEXES = {
    "10": 100.5, "11": 155.2, "12": 113.8, "13": 135.7,
    "14": 91.0, "15": 99.8, "16": 84.3, "17": 115.0,
    "18": 103.8, "19": 104.6, "20": 104.9, "21": 110.7,
    "22": 125.8, "23": 115.8, "24": 128.9, "25": 125.9,
    "26": 137.9, "27": 151.5, "28": 109.9, "29": 130.4,
    "30": 153.4, "31": 109.8, "32": 112.1,
}
EXPECTED_WORKBOOK_SHA256 = "ce4c0bba17d2135474c6abd10aabe03758248e1423d434817c90a2d497ee16ce"
EXPECTED = {
    "period": "2026-04",
    "base_year": "2022-23",
    "classification": "NIC-2025",
    "deflator": "Output PPI",
    "source_sheet": "NIC 2d, sectoral monthly",
    "source_month_column": "Apr-26",
    "source_table_id": "NOT_VERIFIED",
    "official_crosscheck_release_id": "2315957",
    "official_crosscheck_date": "2026-09-28",
    "official_crosscheck_statement": "Statement IV",
    "official_crosscheck_locator": "NIC 10-32; Apr-26 column",
    "verification_status": "VERIFIED_AGAINST_OFFICIAL_AUG_2026_STATEMENT_IV",
    "second_official_release_id": "2329475",
    "second_official_release_date": "2026-10-28",
    "second_official_statement": "Statement IV",
    "second_official_source_url": "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2329475&lang=2&reg=48",
    "second_official_crosscheck_status": "VERIFIED_23_OF_23_SECOND_OFFICIAL_RELEASE",
}
REQUIRED = set(EXPECTED) | {
    "nic_code", "description", "weight", "monthly_index",
    "source_workbook", "source_workbook_sha256",
}

def validate(path: Path) -> list[str]:
    errors = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        duplicate_source_fields = sorted(name for name in fields if name.startswith("third_official_"))
        if duplicate_source_fields:
            return [f"duplicate source fields must not be counted as independent evidence: {', '.join(duplicate_source_fields)}"]
        missing = sorted(REQUIRED - fields)
        if missing:
            return [f"missing required columns: {', '.join(missing)}"]
        rows = list(reader)
    if len(rows) != 23:
        errors.append(f"expected 23 rows; found {len(rows)}")
    codes = [r["nic_code"].strip() for r in rows]
    if codes != EXPECTED_CODES:
        errors.append("NIC codes must be exactly 10 through 32, in ascending order, once each")
    workbook_hashes = set()
    for line, row in enumerate(rows, 2):
        p = f"line {line} NIC {row.get('nic_code', '?')}: "
        for key, expected in EXPECTED.items():
            if row.get(key, "").strip() != expected:
                errors.append(p + f"{key} must equal {expected!r}")
        if not row.get("description", "").strip():
            errors.append(p + "description is blank")
        try:
            weight = float(row["weight"])
            if not (0 < weight < 100):
                errors.append(p + "weight must be >0 and <100")
        except (ValueError, TypeError):
            errors.append(p + "weight must be numeric")
        value = None
        try:
            value = float(row["monthly_index"])
            if not (0 < value < 1000):
                errors.append(p + "monthly_index must be >0 and <1000")
            expected_value = EXPECTED_INDEXES.get(row.get("nic_code", "").strip())
            if expected_value is not None and value != expected_value:
                errors.append(p + f"monthly_index must match official Statement IV value {expected_value}")
        except (ValueError, TypeError):
            errors.append(p + "monthly_index must be numeric")
        h = row.get("source_workbook_sha256", "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", h):
            errors.append(p + "source_workbook_sha256 must be 64 lowercase hex characters")
        workbook_hashes.add(h)
        if h != EXPECTED_WORKBOOK_SHA256:
            errors.append(p + "source_workbook_sha256 does not match the inspected original workbook")
        if not row.get("source_workbook", "").strip():
            errors.append(p + "source_workbook is blank")
    if len(workbook_hashes) != 1 or "" in workbook_hashes:
        errors.append("all rows must reference one identical, non-empty source workbook SHA-256")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    errors = validate(args.csv_path)
    if errors:
        for error in errors:
            print("FAIL:", error)
        print(f"CURRENT_SERIES_QA_FAIL errors={len(errors)}")
        return 1
    print("CURRENT_SERIES_QA_PASS rows=23 nic_codes=10-32")
    print("base_year=2022-23 classification=NIC-2025 deflator=Output_PPI")
    print("independent_official_crosschecks=2; PIB_2315957_AND_2329475; 23_OF_23_EACH")
    print(f"csv_sha256={hashlib.sha256(args.csv_path.read_bytes()).hexdigest()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
