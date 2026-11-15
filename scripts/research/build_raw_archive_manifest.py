#!/usr/bin/env python3
"""Create a reproducible SHA-256 manifest and verify raw NSE file dates.

Research/QA only. Never repairs, rewrites, or fabricates source rows.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/qa/raw_archive_manifest.json")
DATE_ALIASES = {"DATE1", "DATE", "TRADDT", "TRADINGDATE", "TRADING_DATE", "TRADEDATE", "TRADE_DATE"}


def norm(value: object) -> str:
    return re.sub(r"[^A-Z0-9]", "", str(value or "").strip().upper())


def parse_date(value: object):
    value = str(value or "").strip()
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%d-%m-%Y", "%d/%m/%Y", "%d-%b-%Y", "%d%m%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-sessions", type=int, default=None,
                        help="Require exactly this many distinct raw sessions/files")
    args = parser.parse_args()
    if args.expected_sessions is not None and args.expected_sessions < 1:
        parser.error("--expected-sessions must be >= 1")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(RAW.glob("sec_bhavdata_full_*.csv"))
    records = []
    blockers = []
    for path in files:
        match = re.search(r"(\d{8})$", path.stem)
        try:
            expected = datetime.strptime(match.group(1), "%d%m%Y").date() if match else None
        except ValueError:
            expected = None
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        eq_rows = 0
        bad_rows = 0
        observed_dates = set()
        file_error = None
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream)
                columns = {norm(c): c for c in (reader.fieldnames or [])}
                date_col = next((columns[a] for a in DATE_ALIASES if a in columns), None)
                series_col = columns.get("SERIES") or columns.get("SCTYSRS")
                if not date_col or not series_col:
                    raise ValueError("missing date or series column")
                for row in reader:
                    if norm(row.get(series_col)) != "EQ":
                        continue
                    eq_rows += 1
                    parsed = parse_date(row.get(date_col))
                    if parsed:
                        observed_dates.add(parsed.isoformat())
                    if expected is None or parsed != expected:
                        bad_rows += 1
        except Exception as exc:
            file_error = f"{type(exc).__name__}: {exc}"
            blockers.append(f"{path.name}: {file_error}")
        if eq_rows == 0:
            blockers.append(f"{path.name}: no EQ rows")
        if bad_rows:
            blockers.append(f"{path.name}: {bad_rows} EQ rows have missing/invalid/unexpected dates")
        records.append({
            "file": path.as_posix(),
            "expected_date": expected.isoformat() if expected else None,
            "observed_dates": sorted(observed_dates),
            "eq_rows": eq_rows,
            "date_mismatch_rows": bad_rows,
            "size_bytes": path.stat().st_size,
            "sha256": digest.hexdigest(),
            "status": "PASS" if expected and eq_rows and bad_rows == 0 and file_error is None else "FAIL",
        })

    sessions_path = RAW / "sessions.txt"
    listed_sessions = [x.strip() for x in sessions_path.read_text().splitlines() if x.strip()] if sessions_path.exists() else []
    if len(listed_sessions) != len(set(listed_sessions)):
        blockers.append("sessions.txt contains duplicate dates")
    listed_sessions = sorted(listed_sessions)
    file_dates = sorted(r["expected_date"] for r in records if r["expected_date"])
    if len(file_dates) != len(set(file_dates)):
        blockers.append("multiple raw files map to the same filename session date")
    if args.expected_sessions is not None:
        if len(listed_sessions) != args.expected_sessions:
            blockers.append(f"expected {args.expected_sessions} sessions, found {len(listed_sessions)}")
        if len(records) != args.expected_sessions:
            blockers.append(f"expected {args.expected_sessions} raw files, found {len(records)}")
    missing_files = sorted(set(listed_sessions) - set(file_dates))
    unlisted_files = sorted(set(file_dates) - set(listed_sessions))
    if not sessions_path.exists():
        blockers.append("data/raw/sessions.txt missing")
    if missing_files:
        blockers.append("sessions.txt dates without raw files: " + ",".join(missing_files))
    if unlisted_files:
        blockers.append("raw files absent from sessions.txt: " + ",".join(unlisted_files))
    result = {
        "schema_version": 1,
        "status": "PASS" if records and not blockers and all(r["status"] == "PASS" for r in records) else "FAIL",
        "raw_file_count": len(records),
        "sessions_listed": len(listed_sessions),
        "first_session": file_dates[0] if file_dates else None,
        "last_session": file_dates[-1] if file_dates else None,
        "files": records,
        "blockers": blockers,
        "note": "Hashes identify the exact archived bytes; this report does not certify upstream completeness beyond the listed files.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "files"}, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
