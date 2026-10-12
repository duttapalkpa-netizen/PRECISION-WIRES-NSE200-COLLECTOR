#!/usr/bin/env python3
"""Run the same multi-window audit twice and verify byte-for-byte reproducibility.

This is a deterministic-code check, not prospective validation and not a selector promotion.
The audit's input CSV must remain unchanged during both executions.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "pipeline" / "multiwindow_retrospective_audit.py"
INPUT = ROOT / "outputs" / "backtest" / "walk_forward_universe_probabilities.csv"
FILES = [
    ROOT / "outputs" / "prospective" / "multiwindow_retrospective_audit.json",
    ROOT / "outputs" / "prospective" / "multiwindow_retrospective_daily.csv",
]
REPORT = ROOT / "outputs" / "prospective" / "reproducibility_check.json"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def run_once():
    subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
    absent = [str(p.relative_to(ROOT)) for p in FILES if not p.exists()]
    if absent:
        raise RuntimeError(f"Expected audit output missing: {absent}")
    return {str(p.relative_to(ROOT)): sha256(p) for p in FILES}

def main():
    if not INPUT.exists():
        raise SystemExit(f"Required input missing: {INPUT}")
    input_hash_before = sha256(INPUT)
    first = run_once()
    input_hash_mid = sha256(INPUT)
    second = run_once()
    input_hash_after = sha256(INPUT)
    same = first == second and input_hash_before == input_hash_mid == input_hash_after
    report = {
        "status": "PASS_BYTE_FOR_BYTE_REPRODUCIBLE" if same else "FAIL_NONDETERMINISTIC_OR_INPUT_CHANGED",
        "audit_type": "retrospective exploratory; not prospective validation",
        "repetitions": 2,
        "input": str(INPUT.relative_to(ROOT)),
        "input_sha256_before": input_hash_before,
        "input_sha256_between_runs": input_hash_mid,
        "input_sha256_after": input_hash_after,
        "first_run_output_sha256": first,
        "second_run_output_sha256": second,
        "outputs_match_byte_for_byte": first == second,
        "input_unchanged": input_hash_before == input_hash_mid == input_hash_after,
        "production_selector_changed": False,
        "promotion_authorized": False,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    if not same:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
