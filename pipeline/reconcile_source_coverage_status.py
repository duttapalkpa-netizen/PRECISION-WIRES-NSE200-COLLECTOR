#!/usr/bin/env python3
"""Reconcile source_coverage.csv statuses to the canonical same-snapshot JSON."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def reconcile(coverage_json: Path, coverage_csv: Path, output_dir: Path) -> dict:
    cov_bytes = coverage_json.read_bytes()
    cov = json.loads(cov_bytes)
    sources = cov.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("canonical source_coverage.json has no source rows")
    json_rows = {}
    for item in sources:
        if not isinstance(item, dict):
            raise ValueError("canonical JSON contains a non-object source row")
        name = str(item.get("source", "")).strip()
        if not name or name in json_rows:
            raise ValueError(f"blank or duplicate canonical source key: {name!r}")
        json_rows[name] = item

    frame = pd.read_csv(coverage_csv, dtype=str, keep_default_na=False)
    required = {"source", "status", "rows", "selected_path", "notes"}
    if not required.issubset(frame.columns):
        raise ValueError(f"source_coverage.csv missing columns: {sorted(required - set(frame.columns))}")
    names = frame["source"].astype(str).str.strip()
    if names.eq("").any() or names.duplicated().any():
        raise ValueError("CSV contains blank or duplicate source keys")
    csv_keys = set(names)
    json_keys = set(json_rows)
    if csv_keys != json_keys:
        raise ValueError(f"CSV/JSON source key sets differ: csv_only={sorted(csv_keys-json_keys)}, json_only={sorted(json_keys-csv_keys)}")

    changes = []
    for idx, name in enumerate(names):
        item = json_rows[name]
        canonical_status = str(item.get("status", "UNKNOWN"))
        if not canonical_status:
            raise ValueError(f"canonical JSON status is blank for {name}")
        old = frame.at[idx, "status"]
        if old != canonical_status:
            changes.append({"source": name, "csv_status_before": old, "canonical_json_status": canonical_status})
        frame.at[idx, "status"] = canonical_status
        frame.at[idx, "selected_path"] = str(item.get("selected_path") or "")
        frame.at[idx, "rows"] = str(item.get("rows") if item.get("rows") is not None else 0)
        frame.at[idx, "notes"] = str(item.get("reason") or item.get("notes") or "")

    output_dir.mkdir(parents=True, exist_ok=True)
    original_csv_sha = sha256(coverage_csv)
    frame.to_csv(coverage_csv, index=False)
    new_csv_sha = sha256(coverage_csv)
    # Re-read the emitted CSV and assert exact key and status parity, not a subset match.
    emitted = pd.read_csv(coverage_csv, dtype=str, keep_default_na=False)
    emitted_status = dict(zip(emitted["source"], emitted["status"]))
    if set(emitted_status) != json_keys or len(emitted_status) != len(emitted):
        raise RuntimeError("emitted CSV source keys are not a one-to-one match with canonical JSON")
    mismatches = [
        {"source": name, "json_status": str(item.get("status")), "csv_status": emitted_status.get(name)}
        for name, item in json_rows.items()
        if emitted_status.get(name) != str(item.get("status"))
    ]
    if mismatches:
        raise RuntimeError(f"CSV/JSON status parity still fails: {mismatches[:5]}")

    report = {
        "schema_version": 1,
        "status": "PASS_EXACT_SOURCE_KEY_AND_STATUS_PARITY",
        "audit_created_at_utc": datetime.now(timezone.utc).isoformat(),
        "workflow_run_id": cov.get("p0_workflow_run_id") or cov.get("workflow_run_id"),
        "source_snapshot_as_of_utc": cov.get("as_of_utc"),
        "canonical_json_sha256": sha256(coverage_json),
        "csv_sha256_before": original_csv_sha,
        "csv_sha256_after": new_csv_sha,
        "json_source_rows": len(json_rows),
        "csv_source_rows": len(emitted),
        "exact_source_key_set_match": True,
        "duplicate_source_keys": 0,
        "status_mismatches_after_reconciliation": 0,
        "rows_changed": changes,
        "policy": "JSON status is canonical. CSV is reconciled to the exact JSON source keys and statuses; no source evidence, row count, timestamp, or availability is promoted.",
    }
    out = output_dir / "source_coverage_status_reconciliation.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_dir / "source_coverage_status_reconciliation.sha256").write_text(
        f"{sha256(out)}  {out.name}\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--coverage-json", default="outputs/macro_geo/source_coverage.json")
    p.add_argument("--coverage-csv", default="outputs/macro_geo/source_coverage.csv")
    p.add_argument("--output-dir", default="outputs/macro_geo")
    args = p.parse_args()
    reconcile(Path(args.coverage_json), Path(args.coverage_csv), Path(args.output_dir))


if __name__ == "__main__":
    main()
