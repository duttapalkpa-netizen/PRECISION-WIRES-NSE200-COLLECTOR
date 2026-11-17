#!/usr/bin/env python3
"""Deterministic, provenance-gated H.10 vintage comparison.

Inputs are normalized observation CSVs with columns:
date,series_id,value,status
and JSON manifests containing:
source_url,source_publication_timestamp,retrieved_at,raw_byte_length,
raw_sha256,normalized_csv_sha256,series_id,vintage_label.

This tool compares only supplied snapshots. It never downloads data or infers vintages.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

TARGET_SERIES = "JRXWTFB_N.B"
REQUIRED_COLUMNS = {"date", "series_id", "value", "status"}
REQUIRED_MANIFEST = {
    "source_url", "source_publication_timestamp", "retrieved_at",
    "raw_byte_length", "raw_sha256", "normalized_csv_sha256",
    "series_id", "vintage_label",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class VintageError(ValueError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_timestamp(value: str, field: str) -> None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise VintageError(f"{field} must be ISO-8601 with timezone") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise VintageError(f"{field} must include timezone")


def load_snapshot(csv_path: Path, manifest_path: Path):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_MANIFEST - set(manifest))
    if missing:
        raise VintageError(f"manifest missing fields: {','.join(missing)}")
    if not isinstance(manifest["source_url"], str) or not manifest["source_url"].startswith("https://"):
        raise VintageError("source_url must be an https URL")
    parse_timestamp(manifest["source_publication_timestamp"], "source_publication_timestamp")
    parse_timestamp(manifest["retrieved_at"], "retrieved_at")
    if manifest["series_id"] != TARGET_SERIES:
        raise VintageError(f"unexpected manifest series_id: {manifest['series_id']}")
    if manifest["vintage_label"] not in {"pre_correction", "post_correction", "unspecified"}:
        raise VintageError("invalid vintage_label")
    if not isinstance(manifest["raw_byte_length"], int) or manifest["raw_byte_length"] <= 0:
        raise VintageError("raw_byte_length must be a positive integer")
    for key in ("raw_sha256", "normalized_csv_sha256"):
        if not isinstance(manifest[key], str) or not SHA256_RE.fullmatch(manifest[key]):
            raise VintageError(f"{key} must be lowercase SHA-256")
    actual_hash = sha256_file(csv_path)
    if actual_hash != manifest["normalized_csv_sha256"]:
        raise VintageError("normalized CSV SHA-256 mismatch")

    rows = {}
    previous = None
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            raise VintageError("CSV must contain date,series_id,value,status")
        for line_no, row in enumerate(reader, 2):
            try:
                day = date.fromisoformat(row["date"])
            except (TypeError, ValueError) as exc:
                raise VintageError(f"invalid date at line {line_no}") from exc
            if row["series_id"] != TARGET_SERIES:
                raise VintageError(f"unexpected series_id at line {line_no}")
            if previous is not None and day <= previous:
                raise VintageError("dates must be strictly chronological and unique")
            previous = day
            status = (row["status"] or "").strip()
            value_text = (row["value"] or "").strip()
            if status == "A":
                try:
                    value = Decimal(value_text)
                except InvalidOperation as exc:
                    raise VintageError(f"active value is not numeric at line {line_no}") from exc
                if not value.is_finite():
                    raise VintageError(f"active value is not finite at line {line_no}")
            elif status == "ND":
                if value_text not in {"", "-9999"}:
                    raise VintageError(f"ND value must be blank or -9999 at line {line_no}")
                value = None
            else:
                raise VintageError(f"unsupported status {status!r} at line {line_no}")
            rows[day.isoformat()] = {"value": value, "status": status}
    if not rows:
        raise VintageError("snapshot contains no observations")
    return rows, manifest


def compare(old_rows, new_rows):
    output = []
    counts = {k: 0 for k in ("unchanged", "changed", "added", "removed", "missing_or_status_changed")}
    for day in sorted(set(old_rows) | set(new_rows)):
        old, new = old_rows.get(day), new_rows.get(day)
        record = {"date": day, "old_status": old["status"] if old else "",
                  "new_status": new["status"] if new else "",
                  "old_value": str(old["value"]) if old and old["value"] is not None else "",
                  "new_value": str(new["value"]) if new and new["value"] is not None else "",
                  "absolute_delta": "", "relative_delta_pct": "", "classification": ""}
        if old is None:
            kind = "added"
        elif new is None:
            kind = "removed"
        elif old["status"] != new["status"] or (old["value"] is None) != (new["value"] is None):
            kind = "missing_or_status_changed"
        elif old["value"] is None:
            kind = "unchanged"
        elif old["value"] == new["value"]:
            kind = "unchanged"
        else:
            kind = "changed"
            delta = new["value"] - old["value"]
            record["absolute_delta"] = str(delta)
            if old["value"] != 0:
                record["relative_delta_pct"] = format(((delta / old["value"]) * Decimal(100)).normalize(), "f")
        record["classification"] = kind
        counts[kind] += 1
        output.append(record)
    return output, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-csv", required=True, type=Path)
    parser.add_argument("--old-manifest", required=True, type=Path)
    parser.add_argument("--new-csv", required=True, type=Path)
    parser.add_argument("--new-manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()
    old_rows, old_manifest = load_snapshot(args.old_csv, args.old_manifest)
    new_rows, new_manifest = load_snapshot(args.new_csv, args.new_manifest)
    if old_manifest["source_publication_timestamp"] == new_manifest["source_publication_timestamp"]:
        raise VintageError("vintages must have distinct source publication timestamps")
    records, counts = compare(old_rows, new_rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    summary = {
        "status": "PASS_INPUTS_VALID_DIFF_COMPUTED_NOT_SOURCE_CORRECTION_VERIFIED",
        "series_id": TARGET_SERIES,
        "old_source_publication_timestamp": old_manifest["source_publication_timestamp"],
        "new_source_publication_timestamp": new_manifest["source_publication_timestamp"],
        "old_observation_count": len(old_rows), "new_observation_count": len(new_rows),
        "difference_counts": counts,
        "old_csv_sha256": sha256_file(args.old_csv), "new_csv_sha256": sha256_file(args.new_csv),
        "diff_csv_sha256": sha256_file(args.output),
        "warning": "A computed difference is not proof of an official correction unless both vintage provenances and labels are independently established.",
    }
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    try:
        main()
    except (VintageError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: {exc}")
