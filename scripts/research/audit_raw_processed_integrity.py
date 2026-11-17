#!/usr/bin/env python3
"""Read-only raw-to-processed NSE session/key integrity audit.

Does not alter source files. Duplicate raw keys, duplicate processed keys, invalid
raw filenames/dates, and date/key-set differences are reported explicitly.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import pandas as pd


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def audit(raw_dir: Path, processed_path: Path) -> dict:
    raw_files = sorted(raw_dir.glob("sec_bhavdata_full_*.csv"))
    issues: list[str] = []
    raw_parts = []
    file_manifest = []
    invalid_files = []
    for path in raw_files:
        token = path.stem.removeprefix("sec_bhavdata_full_")
        date = pd.to_datetime(token, format="%d%m%Y", errors="coerce")
        if pd.isna(date):
            invalid_files.append(path.name)
            continue
        try:
            frame = pd.read_csv(path, dtype=str)
        except Exception as exc:
            issues.append(f"RAW_READ_ERROR:{path.name}:{type(exc).__name__}")
            continue
        frame.columns = [str(c).strip().upper() for c in frame.columns]
        if not {"SYMBOL", "SERIES"}.issubset(frame.columns):
            issues.append(f"RAW_REQUIRED_COLUMNS_MISSING:{path.name}")
            continue
        eq = frame[frame["SERIES"].astype(str).str.strip().str.upper().eq("EQ")].copy()
        eq["SYMBOL"] = eq["SYMBOL"].astype(str).str.strip().str.upper()
        eq["DATE"] = date.normalize()
        raw_parts.append(eq[["SYMBOL", "DATE"]])
        file_manifest.append({"file": path.name, "sha256": sha256(path), "eq_rows": int(len(eq))})

    if invalid_files:
        issues.append("INVALID_RAW_FILENAME_DATE:" + ",".join(invalid_files))
    if not raw_files:
        issues.append("NO_RAW_BHAVCOPY_FILES")
    if not raw_parts:
        issues.append("NO_VALID_RAW_EQ_ROWS")
        raw = pd.DataFrame(columns=["SYMBOL", "DATE"])
    else:
        raw = pd.concat(raw_parts, ignore_index=True)

    raw_dup = raw[raw.duplicated(["SYMBOL", "DATE"], keep=False)]
    raw_dup_count = int(len(raw_dup))
    if raw_dup_count:
        issues.append("DUPLICATE_RAW_SYMBOL_DATE_KEYS")

    if not processed_path.is_file():
        issues.append("PROCESSED_DATASET_MISSING")
        processed = pd.DataFrame(columns=["SYMBOL", "DATE"])
        processed_hash = None
    else:
        processed_hash = sha256(processed_path)
        try:
            processed = pd.read_csv(processed_path, usecols=["SYMBOL", "DATE"], dtype={"SYMBOL": str})
        except Exception as exc:
            issues.append(f"PROCESSED_READ_OR_SCHEMA_ERROR:{type(exc).__name__}")
            processed = pd.DataFrame(columns=["SYMBOL", "DATE"])
        if not processed.empty:
            processed["SYMBOL"] = processed["SYMBOL"].astype(str).str.strip().str.upper()
            parsed = pd.to_datetime(processed["DATE"], errors="coerce")
            if parsed.isna().any():
                issues.append("INVALID_PROCESSED_DATE")
            processed["DATE"] = parsed.dt.normalize()
        proc_dup = processed[processed.duplicated(["SYMBOL", "DATE"], keep=False)]
        proc_dup_count = int(len(proc_dup))
        if proc_dup_count:
            issues.append("DUPLICATE_PROCESSED_SYMBOL_DATE_KEYS")

    raw_dates = set(raw["DATE"].dropna().tolist())
    proc_dates = set(processed["DATE"].dropna().tolist())
    missing_dates = sorted(raw_dates - proc_dates)
    extra_dates = sorted(proc_dates - raw_dates)
    if missing_dates:
        issues.append("PROCESSED_MISSING_RAW_SESSION_DATES")
    if extra_dates:
        issues.append("PROCESSED_HAS_NON_RAW_SESSION_DATES")

    raw_keys = set(map(tuple, raw[["SYMBOL", "DATE"]].drop_duplicates().to_numpy()))
    proc_keys = set(map(tuple, processed[["SYMBOL", "DATE"]].drop_duplicates().to_numpy()))
    missing_keys = raw_keys - proc_keys
    extra_keys = proc_keys - raw_keys
    if missing_keys:
        issues.append("PROCESSED_MISSING_RAW_SYMBOL_DATE_KEYS")
    if extra_keys:
        issues.append("PROCESSED_HAS_NON_RAW_SYMBOL_DATE_KEYS")

    calendar = sorted(raw_dates)
    symbol_missing = {}
    if calendar:
        for symbol, group in raw.groupby("SYMBOL"):
            observed = set(group["DATE"].dropna().tolist())
            absent = [d for d in calendar if d not in observed]
            if absent:
                symbol_missing[str(symbol)] = {
                    "missing_sessions": len(absent),
                    "available_sessions": len(observed),
                    "calendar_sessions": len(calendar),
                }

    return {
        "status": "PASS" if not issues else "FAIL",
        "audit_type": "READ_ONLY_RAW_TO_PROCESSED_NSE_INTEGRITY",
        "raw_file_count": len(raw_files),
        "valid_raw_file_count": len(file_manifest),
        "raw_eq_rows": int(len(raw)),
        "raw_unique_symbols": int(raw["SYMBOL"].nunique()),
        "raw_session_count": len(raw_dates),
        "processed_rows": int(len(processed)),
        "processed_unique_symbols": int(processed["SYMBOL"].nunique()),
        "processed_session_count": len(proc_dates),
        "raw_duplicate_key_rows": raw_dup_count,
        "processed_duplicate_key_rows": int(processed.duplicated(["SYMBOL", "DATE"], keep=False).sum()),
        "missing_processed_session_dates": [d.strftime("%Y-%m-%d") for d in missing_dates],
        "extra_processed_session_dates": [d.strftime("%Y-%m-%d") for d in extra_dates],
        "missing_raw_symbol_date_key_count": len(missing_keys),
        "extra_processed_symbol_date_key_count": len(extra_keys),
        "symbols_with_incomplete_raw_session_coverage": len(symbol_missing),
        "symbol_session_gaps": symbol_missing,
        "raw_files": file_manifest,
        "processed_sha256": processed_hash,
        "issues": sorted(set(issues)),
        "limitations": [
            "A missing symbol row is reported, not automatically treated as a trading failure; listing dates, suspensions and source omissions require separate provenance.",
            "This audit compares the raw Bhavcopy EQ keys to the processed dataset and does not certify price-band/circuit executability.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="data/raw")
    parser.add_argument("--processed", default="data/processed/nse_eq_200_sessions.csv")
    parser.add_argument("--out", default="data/qa/raw_processed_integrity_report.json")
    args = parser.parse_args()
    report = audit(Path(args.raw_dir), Path(args.processed))
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, default=str) + "\\n", encoding="utf-8")
    print(json.dumps(report, indent=2, default=str))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
