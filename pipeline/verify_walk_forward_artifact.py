#!/usr/bin/env python3
"""Independent verification of the exact extracted V11.4 walk-forward artifact."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="artifact_readback/outputs/backtest")
    ap.add_argument("--report", default="artifact_readback_verification.json")
    args = ap.parse_args()
    root = Path(args.input)
    blockers = []
    required = [
        "walk_forward_predictions.csv",
        "walk_forward_universe_probabilities.csv",
        "walk_forward_metrics.json",
        "walk_forward_maturity_reconciliation.json",
        "diagnostic_separation_672.csv",
    ]
    missing = [name for name in required if not (root / name).is_file()]
    if missing:
        blockers.append("MISSING_FILES:" + ",".join(missing))
        result = {"status": "BLOCKED", "blockers": blockers}
        Path(args.report).write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))
        return 1

    pred = pd.read_csv(root / required[0])
    uni = pd.read_csv(root / required[1])
    metrics = json.loads((root / required[2]).read_text())
    recon = json.loads((root / required[3]).read_text())
    diag = pd.read_csv(root / required[4])

    for frame, name in ((pred, "predictions"), (uni, "universe"), (diag, "diagnostics")):
        if not {"CUT_OFF", "SYMBOL"}.issubset(frame.columns):
            blockers.append(f"{name.upper()}_KEY_COLUMNS_MISSING")
        elif frame.duplicated(["CUT_OFF", "SYMBOL"]).any():
            blockers.append(f"{name.upper()}_DUPLICATE_KEYS")

    counts = pred.groupby("CUT_OFF").size()
    if len(counts) != 30 or not counts.eq(30).all():
        blockers.append("TOP30_CUTOFF_CARDINALITY_INVALID")
    if len(pred) != 900:
        blockers.append(f"TOP30_ROW_COUNT:{len(pred)}")
    if len(diag.columns) != 674:
        blockers.append(f"DIAGNOSTIC_COLUMN_COUNT:{len(diag.columns)}_EXPECTED_674")

    if set(pred.CUT_OFF.unique()) != set(uni.CUT_OFF.unique()):
        blockers.append("PREDICTION_UNIVERSE_CUTOFF_MISMATCH")

    keys = ["CUT_OFF", "SYMBOL"]
    if not any(x in blockers for x in ("PREDICTIONS_KEY_COLUMNS_MISSING", "UNIVERSE_KEY_COLUMNS_MISSING")):
        joined = pred[keys + ["FUT1_HIGH_PCT", "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"]].merge(
            uni[keys + ["FUT1_HIGH_PCT", "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"]],
            on=keys, how="left", suffixes=("_top", "_universe"), validate="one_to_one"
        )
        if joined.filter(like="_universe").isna().all(axis=None):
            blockers.append("SELECTED_ROWS_NOT_FOUND_IN_UNIVERSE")
        for h in (1, 3, 5):
            a = joined[f"FUT{h}_HIGH_PCT_top"]
            b = joined[f"FUT{h}_HIGH_PCT_universe"]
            both = a.notna() & b.notna()
            if not np.allclose(a[both], b[both], rtol=0, atol=1e-9):
                blockers.append(f"OUTCOME_JOIN_MISMATCH_H{h}")

    observed = {}
    for h, target in ((1, 5), (3, 10), (5, 20)):
        col = f"FUT{h}_HIGH_PCT"
        top = pred[pred[col].notna()]
        full = uni[uni[col].notna()]
        key = f"T{target}_H{h}"
        got = {
            "top30_selected": int(len(pred)),
            "top30_matured": int(len(top)),
            "top30_hits": int((top[col] >= target).sum()),
            "universe_rows": int(len(uni)),
            "universe_matured": int(len(full)),
            "universe_winners": int((full[col] >= target).sum()),
        }
        observed[key] = got
        expected = recon.get("metrics", {}).get(key, {}).get("maturity", {})
        if got != expected:
            for field, value in got.items():
                if expected.get(field) != value:
                    blockers.append(f"{key}_{field.upper()}_MISMATCH:artifact_csv={value};reconciliation_json={expected.get(field)}")
        metric_counts = metrics.get("outcome_maturity_counts", {}).get(key, {})
        if got != metric_counts:
            blockers.append(f"{key}_METRICS_JSON_MISMATCH")
        precision = (got["top30_hits"] / got["top30_matured"]) if got["top30_matured"] else None
        if precision is not None:
            stored = metrics.get("precision", {}).get(key)
            if stored is None or abs(float(stored) - precision) > 1e-12:
                blockers.append(f"{key}_PRECISION_MISMATCH")

    report = {
        "status": "PASS_ARTIFACT_READBACK" if not blockers else "BLOCKED_ARTIFACT_READBACK",
        "input": str(root),
        "files_sha256": {name: sha256(root / name) for name in required},
        "top30_rows": int(len(pred)),
        "cutoffs": int(pred["CUT_OFF"].nunique()),
        "diagnostic_columns": int(len(diag.columns)),
        "observed_maturity_counts": observed,
        "blockers": blockers,
        "note": "Independent verification of the extracted uploaded artifact; does not alter production ranking or diagnostics.",
    }
    Path(args.report).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if not blockers else 1


if __name__ == "__main__":
    sys.exit(main())
