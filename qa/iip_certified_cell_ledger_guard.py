#!/usr/bin/env python3
"""Fail-closed IIP certified-cell ledger guard; no new source certification.

Checks existing certified batch ledgers for duplicate transition keys, accounting
consistency and required source-cell evidence. Does not infer unreviewed PASS.
"""
import argparse
import csv
import json
from pathlib import Path

KEY = ("base_year", "classification", "observation_period", "nic_code",
       "previous_vintage_table_id", "current_vintage_table_id")
REQUIRED = KEY + ("previous_workbook_sha256", "current_workbook_sha256",
                  "previous_workbook_sheet", "previous_workbook_cell",
                  "current_workbook_sheet", "current_workbook_cell",
                  "previous_pib_prid", "current_pib_prid",
                  "source_value_match", "certification_status")

def audit(ledgers, summary_path):
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    seen = {}
    errors = []
    total = 0
    for path in ledgers:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = set(REQUIRED) - set(reader.fieldnames or [])
            if missing:
                errors.append(f"{path}: missing columns {sorted(missing)}")
                continue
            for line, row in enumerate(reader, 2):
                total += 1
                key = tuple(row[k].strip() for k in KEY)
                if not all(key):
                    errors.append(f"{path}:{line}: blank transition key")
                if key in seen:
                    errors.append(f"{path}:{line}: duplicate of {seen[key]}")
                seen[key] = f"{path}:{line}"
                if any(not row[k].strip() for k in REQUIRED):
                    errors.append(f"{path}:{line}: incomplete source-cell provenance")
                if row["source_value_match"] != "PASS_BOTH_OFFICIAL_PIB_AND_SOURCE_WORKBOOK" or row["certification_status"] != "CERTIFIED_CELL_LEVEL_SOURCE_MATCH":
                    errors.append(f"{path}:{line}: unsupported certification label")
    certified = summary.get("certified_cell_level_source_matches")
    remaining = summary.get("remaining_policy_aligned_candidates_not_certified")
    unresolved = summary.get("historical_panel_or_out_of_window_transitions_unresolved")
    observed = summary.get("total_observed_differences")
    if not all(isinstance(v, int) and v >= 0 for v in (certified, remaining, unresolved, observed)):
        errors.append("summary: invalid accounting fields")
    else:
        if total != certified:
            errors.append(f"certified count mismatch: ledger={total}, summary={certified}")
        if certified + remaining + unresolved != observed:
            errors.append("summary: partition does not reconcile to observed differences")
    if summary.get("hard_gate") != "BLOCKED":
        errors.append("summary: hard_gate must remain BLOCKED in this bounded audit")
    return {"status": "PASS_LEDGER_GUARD" if not errors else "BLOCKED_LEDGER_GUARD",
            "certified_rows_checked": total, "unique_transition_keys": len(seen),
            "errors": errors, "hard_gate": "BLOCKED",
            "scope": "Ledger consistency only; does not recertify XLSX/PIB or certify any new row."}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", type=Path, action="append", required=True)
    p.add_argument("--summary", type=Path, required=True)
    a = p.parse_args()
    result = audit(a.ledger, a.summary)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS_LEDGER_GUARD" else 1)

if __name__ == "__main__":
    main()
