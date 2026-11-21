#!/usr/bin/env python3
"""Strict, offline validator for the NSE per-file acquisition manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sessions", type=int, default=200)
    parser.add_argument("--manifest", default="data/raw/acquisition_manifest.json")
    parser.add_argument("--sessions-file", default="data/raw/sessions.txt")
    parser.add_argument("--report", default="outputs/prospective/acquisition_manifest_validation.json")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    sessions_path = Path(args.sessions_file)
    report_path = Path(args.report)
    errors: list[str] = []
    entries: list[dict] = []

    if not manifest_path.is_file():
        errors.append("MANIFEST_MISSING")
    else:
        try:
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            entries = payload.get("entries", [])
            if payload.get("schema_version") != 1:
                errors.append("UNSUPPORTED_SCHEMA_VERSION")
        except Exception as exc:
            errors.append(f"MANIFEST_INVALID_JSON:{type(exc).__name__}:{exc}")

    dates = [str(row.get("trade_date", "")) for row in entries]
    if len(entries) != args.sessions:
        errors.append(f"ENTRY_COUNT_MISMATCH:{len(entries)}!={args.sessions}")
    if len(set(dates)) != len(dates):
        errors.append("DUPLICATE_TRADE_DATE")

    if not sessions_path.is_file():
        errors.append("SESSIONS_FILE_MISSING")
        expected_dates: set[str] = set()
    else:
        expected_dates = {x.strip() for x in sessions_path.read_text().splitlines() if x.strip()}
    if set(dates) != expected_dates:
        errors.append("MANIFEST_SESSION_SET_MISMATCH")

    verified = 0
    for row in entries:
        trade_date = str(row.get("trade_date", "UNKNOWN"))
        path = Path(str(row.get("retained_file", "")))
        if not path.is_file():
            errors.append(f"{trade_date}:RETAINED_FILE_MISSING")
            continue
        actual_bytes = path.stat().st_size
        actual_hash = sha256(path)
        if actual_bytes != row.get("retained_bytes"):
            errors.append(f"{trade_date}:RETAINED_BYTE_COUNT_MISMATCH")
        if actual_hash != row.get("retained_sha256"):
            errors.append(f"{trade_date}:RETAINED_SHA256_MISMATCH")

        source_url = str(row.get("source_url") or "")
        source_hash = str(row.get("source_sha256") or "")
        source_bytes = row.get("source_bytes")
        retrieved_at = str(row.get("retrieved_at_utc") or "")
        parsed_url = urlparse(source_url)
        if row.get("provenance_status") != "VERIFIED_AT_ACQUISITION":
            errors.append(f"{trade_date}:PROVENANCE_NOT_VERIFIED")
            continue
        if parsed_url.scheme != "https" or not parsed_url.netloc:
            errors.append(f"{trade_date}:SOURCE_URL_INVALID")
        if len(source_hash) != 64 or any(c not in "0123456789abcdef" for c in source_hash.lower()):
            errors.append(f"{trade_date}:SOURCE_SHA256_INVALID")
        if not isinstance(source_bytes, int) or source_bytes <= 0:
            errors.append(f"{trade_date}:SOURCE_BYTE_COUNT_INVALID")
        try:
            stamp = datetime.fromisoformat(retrieved_at.replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                raise ValueError("timestamp has no timezone")
        except Exception:
            errors.append(f"{trade_date}:RETRIEVAL_TIMESTAMP_INVALID")
        if (actual_bytes == row.get("retained_bytes")
                and actual_hash == row.get("retained_sha256")
                and parsed_url.scheme == "https"
                and len(source_hash) == 64
                and isinstance(source_bytes, int) and source_bytes > 0
                and retrieved_at):
            verified += 1

    report = {
        "status": "PASS" if not errors and verified == args.sessions else "BLOCKED",
        "requested_sessions": args.sessions,
        "manifest_entries": len(entries),
        "verified_retained_files": sum(
            1 for row in entries
            if Path(str(row.get("retained_file", ""))).is_file()
            and Path(str(row.get("retained_file", ""))).stat().st_size == row.get("retained_bytes")
            and sha256(Path(str(row.get("retained_file", "")))) == row.get("retained_sha256")
        ),
        "fully_provenanced_entries": verified,
        "errors": errors,
        "policy": "Cached files without contemporaneous source URL, retrieval timestamp, source byte count and source SHA-256 remain UNKNOWN; no retrospective provenance is inferred.",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
