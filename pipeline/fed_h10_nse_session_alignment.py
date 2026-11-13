#!/usr/bin/env python3
"""Align full-history H.10/FRED daily series to the exact verified NSE 200 sessions.

Both input artifacts must already be downloaded and extracted. Raw bytes and
missing-value semantics are verified; no forward-fill or synthetic dates.
"""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path

H10 = Path("inputs/h10")
NSE = Path("inputs/nse")
OUT = Path("outputs/fed_h10_nse_alignment")
EXPECTED_SNAPSHOT = "ee037b46aa2e8e7bce7df51919aada51418fd03787a1ed740a103f4b47804305"
EXPECTED_NSE_MANIFEST_SHA = "ab37d0e14458aceaa13b7684e5739d9486c27e4b3f04d2667e1911abd568a17a"
EXPECTED_H10_SERIES = 26

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def read_csv_series(path: Path, sid: str):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = {str(c).strip().upper(): c for c in (reader.fieldnames or [])}
        dc = cols.get("DATE") or cols.get("OBSERVATION_DATE")
        vc = cols.get(sid.upper())
        if not dc or not vc:
            raise ValueError(f"{sid}: schema mismatch {reader.fieldnames}")
        values = {}
        previous = None
        for line, row in enumerate(reader, start=2):
            day = (row.get(dc) or "").strip()
            val = (row.get(vc) or "").strip()
            if not day:
                raise ValueError(f"{sid}: blank date at line {line}")
            if day in values:
                raise ValueError(f"{sid}: duplicate date {day}")
            if previous is not None and day <= previous:
                raise ValueError(f"{sid}: non-monotonic date {day}")
            previous = day
            values[day] = "" if val in {"", ".", "NA", "N/A"} else val
    return values

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    nse_manifest_path = NSE / "raw/nse_snapshot_manifest_ee037b46aa2e8e7b.json"
    h10_manifest_path = H10 / "daily_historical_panel_manifest.json"
    if not nse_manifest_path.is_file() or not h10_manifest_path.is_file():
        raise FileNotFoundError("Expected H10 and NSE artifact manifests are missing")
    nse_bytes = nse_manifest_path.read_bytes()
    if sha(nse_bytes) != EXPECTED_NSE_MANIFEST_SHA:
        raise ValueError("Pinned NSE 200-session manifest SHA-256 mismatch")
    nm = json.loads(nse_bytes)
    hm = json.loads(h10_manifest_path.read_text(encoding="utf-8"))
    if nm.get("snapshot_id") != EXPECTED_SNAPSHOT or nm.get("expected_sessions") != 200 or nm.get("actual_sessions") != 200:
        raise ValueError("Pinned NSE snapshot identity/session count mismatch")
    if hm.get("status") != "PASS_RAW_FULL_HISTORY_DOWNLOADED_AND_SCHEMA_QA" or len(hm.get("series", {})) != EXPECTED_H10_SERIES:
        raise ValueError("H10 historical panel manifest is not accepted or not 26 series")

    session_dates = [x["trade_date"] for x in nm["records"]]
    if len(session_dates) != 200 or len(set(session_dates)) != 200 or session_dates != sorted(session_dates):
        raise ValueError("NSE session dates are not exactly 200 unique sorted dates")

    # Verify all original NSE raw files against the pinned manifest before using its dates.
    nse_raw_verified = 0
    for rec in nm["records"]:
        p = NSE / "raw" / rec["file"]
        data = p.read_bytes()
        if len(data) != rec["bytes"] or sha(data) != rec["sha256"]:
            raise ValueError(f"NSE raw evidence mismatch: {rec['file']}")
        nse_raw_verified += 1
    if nse_raw_verified != 200:
        raise ValueError("NSE raw evidence verification count mismatch")

    series = hm["series"]
    values_by_series = {}
    for sid, meta in series.items():
        raw_path = H10 / "raw" / f"{sid}.csv"
        raw = raw_path.read_bytes()
        if len(raw) != meta["raw_bytes"] or sha(raw) != meta["raw_sha256"]:
            raise ValueError(f"H10 raw evidence mismatch: {sid}")
        values_by_series[sid] = read_csv_series(raw_path, sid)

    all_source_dates = set().union(*(set(v.keys()) for v in values_by_series.values()))
    present_in_source_union = [d for d in session_dates if d in all_source_dates]
    absent_from_all_sources = [d for d in session_dates if d not in all_source_dates]

    report = {
        "schema_version": "1.0",
        "status": "BLOCKED",
        "nse_snapshot_id": EXPECTED_SNAPSHOT,
        "nse_manifest_sha256": EXPECTED_NSE_MANIFEST_SHA,
        "nse_sessions": 200,
        "nse_first_session": session_dates[0],
        "nse_last_session": session_dates[-1],
        "nse_raw_files_sha256_verified": nse_raw_verified,
        "h10_series_count": len(series),
        "h10_raw_files_sha256_verified": len(values_by_series),
        "source_union_session_intersection": len(present_in_source_union),
        "source_union_session_absent_dates": absent_from_all_sources,
        "series_coverage": {},
        "no_forward_fill": True,
        "synthetic_observations": False,
        "point_in_time_vintage_status": "UNKNOWN_NOT_ESTABLISHED_BY_CURRENT_RETRIEVAL_SNAPSHOT",
    }

    wide_path = OUT / "h10_nse_200_session_wide.csv"
    long_path = OUT / "h10_nse_200_session_long.csv"
    ids = list(series.keys())
    with wide_path.open("w", encoding="utf-8", newline="") as fw, long_path.open("w", encoding="utf-8", newline="") as fl:
        ww = csv.writer(fw); wl = csv.writer(fl)
        ww.writerow(["DATE", *ids])
        wl.writerow(["DATE", "SERIES_ID", "VALUE", "OBSERVATION_STATUS"])
        for day in session_dates:
            wide = []
            for sid in ids:
                obs = values_by_series[sid]
                if day not in obs:
                    value, status = "", "NO_SOURCE_ROW"
                elif obs[day] == "":
                    value, status = "", "SOURCE_MISSING_MARKER"
                else:
                    value, status = obs[day], "OBSERVED"
                wide.append(value)
                wl.writerow([day, sid, value, status])
            ww.writerow([day, *wide])

    for sid in ids:
        obs = values_by_series[sid]
        observed = [d for d in session_dates if d in obs and obs[d] != ""]
        source_missing = [d for d in session_dates if d in obs and obs[d] == ""]
        no_row = [d for d in session_dates if d not in obs]
        report["series_coverage"][sid] = {
            "source_type": series[sid]["source_type"],
            "source_series_id": sid,
            "observed_sessions": len(observed),
            "source_missing_marker_sessions": len(source_missing),
            "no_source_row_sessions": len(no_row),
            "coverage_pct": round(100 * len(observed) / len(session_dates), 2),
            "first_observed_session": observed[0] if observed else None,
            "last_observed_session": observed[-1] if observed else None,
            "source_missing_marker_dates": source_missing,
            "no_source_row_dates": no_row,
        }

    # Current FRED retrieval has a common latest observation date of 2026-11-06.
    # A full 200-session calendar is emitted, but missing values remain blank.
    all_counts = {x["observed_sessions"] for x in report["series_coverage"].values()}
    if len(all_counts) != 1:
        report["status"] = "PASS_ALIGNED_WITH_SERIES_SPECIFIC_COVERAGE"
    else:
        report["status"] = "PASS_ALIGNED_WITH_MISSING_VALUES_PRESERVED"
    report["outputs"] = {}
    for p in (wide_path, long_path):
        b = p.read_bytes()
        report["outputs"][p.name] = {"bytes": len(b), "sha256": sha(b)}
    report["acceptance_boundary"] = (
        "Exact 200-session join and raw-source integrity passed. Missing source rows and explicit "
        "missing-value markers are preserved as blanks. No forward-fill. Publication-time/vintage "
        "availability at each historical signal timestamp remains UNKNOWN; this is not a predictive "
        "backtest, capital-flow inference, or production signal."
    )
    (OUT / "h10_nse_200_session_alignment_report.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
