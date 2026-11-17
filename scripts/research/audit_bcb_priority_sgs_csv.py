#!/usr/bin/env python3
"""Deterministic QA for captured BCB priority SGS CSV files; no sign transformation."""
from __future__ import annotations
import csv, hashlib, json
from decimal import Decimal
from datetime import date, datetime
from pathlib import Path

ROOT = Path("bcb_priority_capture")
CODES = ("22905", "22906", "22907", "22908", "22924", "22925", "22926")
START, END = (1995, 1), (2026, 9)

def parse_value(raw: str) -> Decimal:
    s = raw.strip().strip('"').strip()
    if not s:
        raise ValueError("empty value")
    return Decimal(s.replace(".", "").replace(",", "."))

def expected_months():
    y, m = START
    result = []
    while (y, m) <= END:
        result.append(date(y, m, 1))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return result

def audit(root: Path):
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    report = {
        "schema_version": 1,
        "purpose": "research_only_bcb_raw_csv_structural_and_identity_audit",
        "series": {}, "identity_diagnostics": {}, "errors": [],
        "accounting_sign_reconciliation": "PARTIAL_EMPIRICAL_ALIGNMENT",
        "country_period_qa": "NOT_DONE", "brazil_pilot_acceptance": "NOT_ACCEPTED",
        "em_wide_panel": "NOT_DONE", "production_integration": "NOT_AUTHORIZED",
    }
    parsed, expected = {}, expected_months()
    for code in CODES:
        path = root / f"sgs_{code}.csv"
        meta = manifest.get("series", {}).get(code, {})
        if not path.exists():
            report["errors"].append(f"missing raw file: {path.name}")
            continue
        raw = path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        rows = []
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as fh:
                reader = csv.DictReader(fh, delimiter=";")
                if reader.fieldnames != ["data", "valor"]:
                    raise ValueError(f"unexpected columns: {reader.fieldnames}")
                for row in reader:
                    dt = datetime.strptime(row["data"].strip().strip('"'), "%d/%m/%Y").date()
                    if dt.day != 1:
                        raise ValueError(f"non-month-start date: {dt}")
                    rows.append((dt, parse_value(row["valor"])))
            dates = [d for d, _ in rows]
            unique = len(set(dates)) == len(dates)
            ordered = all(dates[i] < dates[i+1] for i in range(len(dates)-1))
            coverage = dates == expected
            if not (unique and ordered and coverage):
                report["errors"].append(f"{code}: duplicate/order/coverage check failed")
            if sha != meta.get("sha256") or len(raw) != meta.get("byte_length"):
                report["errors"].append(f"{code}: raw file hash/length differs from capture manifest")
            parsed[code] = dict(rows)
            report["series"][code] = {
                "http_status": meta.get("http_status"), "content_type": meta.get("content_type"),
                "byte_length": len(raw), "sha256": sha,
                "manifest_sha256_match": sha == meta.get("sha256"),
                "manifest_byte_length_match": len(raw) == meta.get("byte_length"),
                "columns": ["data", "valor"], "delimiter": ";",
                "date_format": "DD/MM/YYYY", "value_decimal_separator": ",",
                "row_count": len(rows),
                "first_date": dates[0].isoformat() if dates else None,
                "last_date": dates[-1].isoformat() if dates else None,
                "unique_dates": unique, "strictly_increasing_dates": ordered,
                "complete_monthly_coverage_1995_01_to_2026_09": coverage,
                "missing_numeric_values": 0,
            }
        except Exception as exc:
            report["errors"].append(f"{code}: parse/QA error: {exc}")
    relations = [
        ("22906 = 22908 - 22907", "22906", lambda d: parsed["22908"][d] - parsed["22907"][d]),
        ("22924 = 22925 - 22926", "22924", lambda d: parsed["22925"][d] - parsed["22926"][d]),
        ("22905 = 22906 - 22924", "22905", lambda d: parsed["22906"][d] - parsed["22924"][d]),
    ]
    if len(parsed) == 7:
        common = set.intersection(*(set(x) for x in parsed.values()))
        for label, target, formula in relations:
            deltas = [parsed[target][d] - formula(d) for d in sorted(common)]
            report["identity_diagnostics"][label] = {
                "observations_tested": len(deltas),
                "exact_matches": sum(x == 0 for x in deltas),
                "differences_plus_or_minus_0_1": sum(abs(x) <= Decimal("0.1") for x in deltas),
                "differences_greater_than_0_1": sum(abs(x) > Decimal("0.1") for x in deltas),
                "max_absolute_difference": str(max(abs(x) for x in deltas)),
                "difference_counts": {str(x): deltas.count(x) for x in sorted(set(deltas))},
                "interpretation": "Empirical rounding-consistency only; not final accounting acceptance.",
            }
    else:
        report["errors"].append("identity checks skipped because all seven series did not parse")
    report["acceptance"] = {
        "seven_raw_files_present_and_manifest_hash_verified": len(parsed) == 7 and not report["errors"],
        "all_seven_have_381_contiguous_monthly_rows": len(parsed) == 7 and all(x.get("row_count") == 381 and x.get("complete_monthly_coverage_1995_01_to_2026_09") for x in report["series"].values()),
        "all_three_net_component_identities_within_0_1": all(v.get("differences_greater_than_0_1") == 0 for v in report["identity_diagnostics"].values()) if len(report["identity_diagnostics"]) == 3 else False,
        "rounding_tolerance_formally_approved": False,
        "official_series_specific_sign_methodology_fully_reconciled": False,
        "trusted_observation_admission": "NOT_AUTHORIZED",
    }
    report["status"] = "STRUCTURAL_QA_PASS_IDENTITY_ROUNDING_REVIEW_PENDING" if not report["errors"] and report["acceptance"]["all_seven_have_381_contiguous_monthly_rows"] else "BLOCKED"
    return report

if __name__ == "__main__":
    root = Path("bcb_priority_capture")
    result = audit(root)
    (root / "qa_report.json").write_text(json.dumps(result, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["errors"]:
        raise SystemExit(1)
