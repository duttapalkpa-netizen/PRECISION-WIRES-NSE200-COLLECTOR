#!/usr/bin/env python3
"""Independent, fail-closed validation and classification of IIP vintage deltas.

Reads only the exact outputs from audit_iip_41_vintages.py. A delta is labelled
VERIFIED_SNAPSHOT_DIFFERENCE only when both values and source hashes reconcile
to the raw-vintage observation ledger and release chronology is valid. This
does not infer why MoSPI changed a value and does not treat every difference
as an error.
"""
from __future__ import annotations
import csv, json, hashlib
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path("artifacts/iip_41_vintage_audit")
OBS = ROOT / "all_vintage_observations.csv"
DIFF = ROOT / "revision_differences.csv"
OUT = ROOT / "revision_difference_classification.json"
VALID_SERIES = {("2011-12", "NIC-2008"), ("2022-23", "NIC-2025")}

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def number(v):
    x = float(v)
    if not (x == x and abs(x) != float("inf")):
        raise ValueError("non-finite numeric value")
    return x

def date_key(v):
    return datetime.strptime(v, "%d %b %Y").date()

def main():
    observations = read_csv(OBS)
    differences = read_csv(DIFF)
    if not observations or not differences:
        raise SystemExit("BLOCKED: observation or difference ledger is empty")

    obs_index = {}
    for row in observations:
        key = (row["table_id"], row["base_year"], row["classification"], row["period"], row["nic_code"])
        if key in obs_index:
            raise SystemExit(f"BLOCKED: duplicate observation key {key}")
        obs_index[key] = row

    errors = []
    pair_counts = Counter()
    series_counts = Counter()
    magnitude = Counter()
    signs = Counter()
    seen = set()
    rows_out = []

    for line, row in enumerate(differences, start=2):
        base = row["base_year"]
        cls = row["classification"]
        series = (base, cls)
        if series not in VALID_SERIES:
            errors.append(f"row {line}: unsupported series lineage {series}")
            continue
        key = (base, cls, row["period"], row["nic_code"])
        comparison_key = (row["previous_table_id"], row["current_table_id"], *key)
        if comparison_key in seen:
            errors.append(f"row {line}: duplicate comparison-pair key {comparison_key}")
            continue
        seen.add(comparison_key)

        prev_key = (row["previous_table_id"], *key)
        curr_key = (row["current_table_id"], *key)
        prev = obs_index.get(prev_key)
        curr = obs_index.get(curr_key)
        if prev is None or curr is None:
            errors.append(f"row {line}: source observation missing for {key}")
            continue

        pv, cv = number(row["previous_value"]), number(row["current_value"])
        delta = number(row["revision_delta"])
        if abs(number(prev["value"]) - pv) > 1e-9:
            errors.append(f"row {line}: previous value does not reconcile")
        if abs(number(curr["value"]) - cv) > 1e-9:
            errors.append(f"row {line}: current value does not reconcile")
        if prev["source_sha256"] != row["previous_sha256"]:
            errors.append(f"row {line}: previous source SHA-256 mismatch")
        if curr["source_sha256"] != row["current_sha256"]:
            errors.append(f"row {line}: current source SHA-256 mismatch")
        if abs((cv - pv) - delta) > 1e-9:
            errors.append(f"row {line}: revision_delta arithmetic mismatch")
        if date_key(row["current_release_date"]) <= date_key(row["previous_release_date"]):
            errors.append(f"row {line}: release chronology is not increasing")
        if abs(delta) <= 1e-12:
            errors.append(f"row {line}: zero delta should not be in difference ledger")

        abs_delta = abs(delta)
        band = "<0.1" if abs_delta < 0.1 else "<1" if abs_delta < 1 else "<5" if abs_delta < 5 else ">=5"
        magnitude[band] += 1
        signs["positive" if delta > 0 else "negative"] += 1
        pair = (row["previous_table_id"], row["current_table_id"])
        pair_counts[(base, cls, *pair)] += 1
        series_counts[series] += 1
        rows_out.append({
            "status": "VERIFIED_SNAPSHOT_DIFFERENCE",
            "base_year": base, "classification": cls,
            "period": row["period"], "nic_code": row["nic_code"],
            "previous_table_id": pair[0], "current_table_id": pair[1],
            "previous_release_date": row["previous_release_date"],
            "current_release_date": row["current_release_date"],
            "previous_value": pv, "current_value": cv, "delta": delta,
            "absolute_delta_band": band,
            "cause": "NOT_DETERMINED_FROM_SNAPSHOT_COMPARISON"
        })

    if errors:
        OUT.write_text(json.dumps({"status":"BLOCKED","errors":errors[:100],"error_count":len(errors)},indent=2)+"\n")
        raise SystemExit(f"BLOCKED: {len(errors)} integrity errors; see {OUT}")

    pairs = [
        {"base_year": k[0], "classification": k[1],
         "previous_table_id": k[2], "current_table_id": k[3], "difference_rows": v}
        for k, v in sorted(pair_counts.items())
    ]
    series = []
    for (base, cls), n in sorted(series_counts.items()):
        subset = [r["delta"] for r in rows_out if r["base_year"] == base and r["classification"] == cls]
        absvals = sorted(abs(x) for x in subset)
        mid = len(absvals)//2
        median_abs = absvals[mid] if len(absvals)%2 else (absvals[mid-1]+absvals[mid])/2
        series.append({
            "base_year": base, "classification": cls, "verified_difference_rows": n,
            "positive_deltas": sum(x > 0 for x in subset),
            "negative_deltas": sum(x < 0 for x in subset),
            "mean_absolute_delta": round(sum(abs(x) for x in subset)/len(subset), 6),
            "median_absolute_delta": round(median_abs, 6),
            "max_absolute_delta": round(max(abs(x) for x in subset), 6)
        })

    result = {
        "status": "PASS",
        "classification": "SNAPSHOT_DIFFERENCES_VERIFIED_CAUSE_NOT_DETERMINED",
        "observation_rows_checked": len(observations),
        "difference_rows_checked": len(differences),
        "integrity_errors": 0,
        "unique_series_period_nic_comparisons": len(seen),
        "series_summary": series,
        "delta_sign_counts": dict(signs),
        "absolute_delta_bands": dict(magnitude),
        "release_pair_summary": pairs,
        "interpretation": [
            "Each reported delta reconciles to both source-vintage observation rows and their recorded SHA-256 values.",
            "The 1,058 rows are verified differences between successive available snapshots for the same base year, classification, NIC code and observation period; they are not 1,058 independent monthly observations.",
            "Successive available snapshots are not guaranteed to be adjacent calendar releases where catalogue vintages are missing or failed.",
            "The comparison establishes that the published snapshots differ; it does not establish the reason, correction policy, or which vintage is economically preferable.",
            "Magnitude bands are descriptive only and are not pass/fail thresholds."
        ]
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
