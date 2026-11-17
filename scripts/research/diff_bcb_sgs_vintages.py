#!/usr/bin/env python3
"""Verify and compare immutable BCB SGS point-in-time snapshots.

The tool never downloads data, synthesizes observations, or attributes causes.
With one valid snapshot it records WAITING_FOR_SECOND_VINTAGE. With two or more,
it compares the two latest retrieval vintages after independently verifying
raw CSV byte length, SHA-256, CSV structure, chronology and manifest values.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_ROOT = ROOT / "data" / "raw" / "bcb" / "sgs_vintage_snapshots"
OUTPUT_ROOT = ROOT / "data" / "qa"
EXPECTED_CODES = {"22924", "22930", "22936", "22942"}


class AuditError(ValueError):
    pass


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def parse_utc(value: str, label: str) -> datetime:
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise AuditError(f"{label}: invalid ISO timestamp") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise AuditError(f"{label}: timezone is required")
    return result


def load_snapshot(directory: Path) -> dict:
    manifest_path = directory / "manifest.json"
    if not manifest_path.is_file():
        raise AuditError(f"{directory}: manifest.json missing")
    manifest_raw = manifest_path.read_bytes()
    manifest = json.loads(manifest_raw.decode("utf-8"))
    snapshot_id = manifest.get("snapshot_id_utc")
    if not isinstance(snapshot_id, str) or snapshot_id != directory.name:
        raise AuditError(f"{directory}: snapshot ID does not match directory")
    captured_at = parse_utc(manifest.get("captured_at_utc"), f"{snapshot_id}.captured_at_utc")
    series = manifest.get("series")
    if not isinstance(series, dict) or set(series) != EXPECTED_CODES:
        raise AuditError(f"{snapshot_id}: expected exact series set {sorted(EXPECTED_CODES)}")
    loaded = {}
    for code in sorted(EXPECTED_CODES):
        meta = series[code]
        filename = f"sgs_{code}.csv"
        path = directory / filename
        if not path.is_file():
            raise AuditError(f"{snapshot_id}/{filename}: raw file missing")
        raw = path.read_bytes()
        if len(raw) != meta.get("byte_length"):
            raise AuditError(f"{snapshot_id}/{filename}: byte length mismatch")
        digest = sha256_bytes(raw)
        if digest != meta.get("sha256"):
            raise AuditError(f"{snapshot_id}/{filename}: SHA-256 mismatch")
        if meta.get("http_status") != 200 or meta.get("csv_validation") != "PASS":
            raise AuditError(f"{snapshot_id}/{filename}: source/CSV gate not PASS")
        parse_utc(meta.get("retrieved_at_utc"), f"{snapshot_id}.{code}.retrieved_at_utc")
        if meta.get("final_url") != meta.get("requested_url"):
            raise AuditError(f"{snapshot_id}/{filename}: final URL differs from requested URL")

        text = raw.decode("utf-8-sig")
        rows = list(csv.reader(text.splitlines(), delimiter=";", quotechar='"'))
        if not rows or [x.strip().lower() for x in rows[0]] != ["data", "valor"]:
            raise AuditError(f"{snapshot_id}/{filename}: unexpected CSV header")
        observations = {}
        previous_date = None
        for line_no, row in enumerate(rows[1:], start=2):
            if len(row) != 2:
                raise AuditError(f"{snapshot_id}/{filename}: malformed row {line_no}")
            try:
                day = datetime.strptime(row[0].strip(), "%d/%m/%Y").date()
                value = Decimal(row[1].strip().replace(".", "").replace(",", "."))
            except (ValueError, InvalidOperation) as exc:
                raise AuditError(f"{snapshot_id}/{filename}: invalid row {line_no}") from exc
            if not value.is_finite():
                raise AuditError(f"{snapshot_id}/{filename}: non-finite value at row {line_no}")
            key = day.strftime("%Y-%m")
            if key in observations:
                raise AuditError(f"{snapshot_id}/{filename}: duplicate month {key}")
            if previous_date is not None and day <= previous_date:
                raise AuditError(f"{snapshot_id}/{filename}: non-ascending date at row {line_no}")
            previous_date = day
            observations[key] = {"date": day.isoformat(), "value": value}
        if len(observations) != meta.get("observation_summary", {}).get("row_count"):
            raise AuditError(f"{snapshot_id}/{filename}: row-count/manifest mismatch")
        if set(observations) != set(meta.get("observations", {})):
            raise AuditError(f"{snapshot_id}/{filename}: month set/manifest mismatch")
        for month, parsed in observations.items():
            recorded = meta["observations"][month]
            try:
                recorded_value = Decimal(str(recorded["value"]))
            except (KeyError, InvalidOperation) as exc:
                raise AuditError(f"{snapshot_id}/{filename}: invalid manifest value for {month}") from exc
            if recorded_value != parsed["value"] or recorded.get("date") != parsed["date"]:
                raise AuditError(f"{snapshot_id}/{filename}: raw/manifest value mismatch at {month}")
        loaded[code] = {
            "source_url": meta["final_url"],
            "retrieved_at_utc": meta["retrieved_at_utc"],
            "sha256": digest,
            "byte_length": len(raw),
            "row_count": len(observations),
            "first_period": min(observations),
            "last_period": max(observations),
            "observations": observations,
        }
    return {
        "snapshot_id": snapshot_id,
        "captured_at": captured_at,
        "manifest_sha256": sha256_bytes(manifest_raw),
        "series": loaded,
    }


def compare_snapshots(old: dict, new: dict) -> dict:
    if new["captured_at"] <= old["captured_at"]:
        raise AuditError("new snapshot capture time must be later than old snapshot")
    results = {}
    totals = {"unchanged": 0, "changed": 0, "added": 0, "removed": 0}
    for code in sorted(EXPECTED_CODES):
        before, after = old["series"][code], new["series"][code]
        if before["source_url"] != after["source_url"]:
            raise AuditError(f"SGS {code}: source URL changed; comparison not admissible")
        old_obs, new_obs = before["observations"], after["observations"]
        counts = {"unchanged": 0, "changed": 0, "added": 0, "removed": 0}
        changes = []
        for month in sorted(set(old_obs) | set(new_obs)):
            a, b = old_obs.get(month), new_obs.get(month)
            if a is None:
                kind = "added"
            elif b is None:
                kind = "removed"
            elif a["value"] == b["value"]:
                kind = "unchanged"
            else:
                kind = "changed"
                changes.append({
                    "month": month,
                    "date": b["date"],
                    "old_value": str(a["value"]),
                    "new_value": str(b["value"]),
                    "delta": str(b["value"] - a["value"]),
                })
            counts[kind] += 1
            totals[kind] += 1
        results[code] = {
            "old_sha256": before["sha256"],
            "new_sha256": after["sha256"],
            "old_row_count": before["row_count"],
            "new_row_count": after["row_count"],
            "counts": counts,
            "changes": changes,
        }
    return {"series": results, "totals": totals}


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    directories = sorted(p for p in SNAPSHOT_ROOT.iterdir() if p.is_dir() and (p / "manifest.json").is_file())
    if not directories:
        raise AuditError("no BCB SGS snapshots found")
    snapshots = [load_snapshot(p) for p in directories]
    snapshots.sort(key=lambda x: x["captured_at"])
    if len(snapshots) == 1:
        only = snapshots[0]
        result = {
            "schema_version": 1,
            "status": "WAITING_FOR_SECOND_VINTAGE",
            "comparison_performed": False,
            "snapshot_count": 1,
            "baseline": {
                "snapshot_id": only["snapshot_id"],
                "captured_at_utc": only["captured_at"].isoformat(),
                "manifest_sha256": only["manifest_sha256"],
                "series": {
                    code: {k: v for k, v in series.items() if k != "observations"}
                    for code, series in only["series"].items()
                },
            },
            "revision_attribution": "UNKNOWN_NOT_ASSESSED",
            "message": "One fully verified snapshot exists. A revision comparison requires a second independently captured vintage; no values or causes have been inferred.",
        }
        output_name = f"BCB_SGS_VINTAGE_REVISION_DIFF_{only['snapshot_id']}.json"
    else:
        old, new = snapshots[-2], snapshots[-1]
        diff = compare_snapshots(old, new)
        result = {
            "schema_version": 1,
            "status": "PASS_TWO_VINTAGES_COMPARED",
            "comparison_performed": True,
            "snapshot_count": len(snapshots),
            "old_snapshot": {"snapshot_id": old["snapshot_id"], "captured_at_utc": old["captured_at"].isoformat(), "manifest_sha256": old["manifest_sha256"]},
            "new_snapshot": {"snapshot_id": new["snapshot_id"], "captured_at_utc": new["captured_at"].isoformat(), "manifest_sha256": new["manifest_sha256"]},
            "diff": diff,
            "revision_attribution": "UNKNOWN_NOT_PROVEN",
            "message": "The comparison identifies value changes between two captured current-response vintages. It does not prove why or when BCB changed a value.",
        }
        output_name = f"BCB_SGS_VINTAGE_REVISION_DIFF_{new['snapshot_id']}.json"
    output_path = OUTPUT_ROOT / output_name
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "snapshot_count": result["snapshot_count"],
        "output": str(output_path.relative_to(ROOT)),
        "series_verified": sorted(EXPECTED_CODES),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AuditError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
