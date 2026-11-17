#!/usr/bin/env python3
"""Capture official H.10 XML, segmented FRED graph CSV, and Fed DDP/FRED crosswalk.
No API key, paid service, synthetic values, or production integration. Raw bytes are
preserved per source/window with independent SHA-256 hashes.
"""
from __future__ import annotations
import csv, hashlib, io, json, os, sys, urllib.parse, urllib.request, zipfile
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(os.environ.get("OUT_DIR", "artifacts/h10_fred_capture"))
OUT.mkdir(parents=True, exist_ok=True)
BASE = {
    "fed_h10_xml.zip": "https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip",
    "ddp_fred_crosswalk.csv": "https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv",
}
TARGET_BOARD, TARGET_FRED = "JRXWTFB_N.B", "DTWEXBGS"
WINDOWS = [
    ("2006_2010", "2006-01-02", "2010-12-31"),
    ("2011_2015", "2011-01-01", "2015-12-31"),
    ("2016_2020", "2016-01-01", "2020-12-31"),
    ("2021_2025", "2021-01-01", "2025-12-31"),
    ("2026_ytd", "2026-01-01", "2026-11-13"),
]

def fetch_bytes(url: str, timeout: int = 45) -> tuple[bytes, dict]:
    req = urllib.request.Request(url, headers={"User-Agent": "PRECISION-WIRES-research/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        data = response.read()
        meta = {"url": url, "final_url": response.geturl(), "http_status": response.status,
                "content_type": response.headers.get("Content-Type"),
                "content_length_header": response.headers.get("Content-Length"),
                "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                "byte_length": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    if not data:
        raise RuntimeError("empty response")
    return data, meta

def save_source(name: str, url: str, timeout: int = 45) -> dict:
    data, meta = fetch_bytes(url, timeout)
    (OUT / name).write_bytes(data)
    return meta

manifest = {"schema_version": 2, "sources": {}, "checks": {}, "fred_windows": {}, "errors": [], "status": "INCOMPLETE"}
errors = manifest["errors"]
for name, url in BASE.items():
    try:
        manifest["sources"][name] = save_source(name, url, 45)
    except Exception as exc:
        errors.append(f"{name}: {type(exc).__name__}: {exc}")

# Bounded windows prevent one long full-history response from blocking all FRED evidence.
all_dates = set()
fred_window_failures = 0
for label, start, end in WINDOWS:
    params = urllib.parse.urlencode({"id": TARGET_FRED, "cosd": start, "coed": end})
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?" + params
    filename = f"fred_dtwexbgs_{label}.csv"
    try:
        meta = save_source(filename, url, 45)
        raw = (OUT / filename).read_text(encoding="utf-8-sig")
        rows = list(csv.DictReader(io.StringIO(raw)))
        valid_schema = bool(rows and "observation_date" in rows[0] and TARGET_FRED in rows[0])
        dates = [r.get("observation_date", "") for r in rows]
        if not valid_schema:
            raise RuntimeError("FRED CSV schema/rows invalid")
        if len(dates) != len(set(dates)):
            raise RuntimeError("duplicate observation dates in FRED window")
        if any(d < start or d > end for d in dates):
            raise RuntimeError("FRED returned date outside requested window")
        all_dates.update(dates)
        manifest["fred_windows"][label] = {**meta, "filename": filename, "requested_start": start,
            "requested_end": end, "row_count": len(rows), "first_date": min(dates) if dates else None,
            "last_date": max(dates) if dates else None,
            "missing_value_count": sum(r.get(TARGET_FRED, "") in ("", ".") for r in rows),
            "schema_valid": True}
    except Exception as exc:
        fred_window_failures += 1
        errors.append(f"{filename}: {type(exc).__name__}: {exc}")
manifest["checks"]["fred_segmented"] = {
    "requested_window_count": len(WINDOWS), "captured_window_count": len(manifest["fred_windows"]),
    "failed_window_count": fred_window_failures, "unique_date_count": len(all_dates),
    "first_date": min(all_dates) if all_dates else None, "last_date": max(all_dates) if all_dates else None,
    "no_synthetic_merge": True
}

if "ddp_fred_crosswalk.csv" in manifest["sources"]:
    try:
        rows = list(csv.DictReader(io.StringIO((OUT / "ddp_fred_crosswalk.csv").read_text(encoding="utf-8-sig"))))
        cols = list(rows[0].keys()) if rows else []
        def norm(s): return (s or "").strip().lower().replace(" ", "_")
        board = next((c for c in cols if norm(c) in ("board_series_id", "ddp_series_id", "series_id")), None)
        fred = next((c for c in cols if norm(c) == "fred_series_id"), None)
        release = next((c for c in cols if norm(c) in ("ddp_release", "release_id", "release")), None)
        matches = [r for r in rows if board and fred and r.get(board, "").strip() == TARGET_BOARD and
                   r.get(fred, "").strip() == TARGET_FRED and
                   (not release or r.get(release, "").strip().upper() == "H10")]
        manifest["checks"]["crosswalk"] = {"columns": cols, "rows": len(rows), "board_column": board,
            "fred_column": fred, "release_column": release, "target_exact_match_count": len(matches),
            "target_rows": matches}
        if len(matches) != 1:
            errors.append(f"Expected exactly one crosswalk match, found {len(matches)}")
    except Exception as exc:
        errors.append(f"Crosswalk parse: {type(exc).__name__}: {exc}")

if "fed_h10_xml.zip" in manifest["sources"]:
    try:
        with zipfile.ZipFile(OUT / "fed_h10_xml.zip") as z:
            bad = z.testzip()
            manifest["checks"]["h10_zip"] = {"member_count": len(z.namelist()),
                "members": z.namelist()[:50], "zip_integrity": "PASS" if bad is None else "FAIL",
                "first_bad_member": bad}
            if bad is not None:
                errors.append("H.10 ZIP integrity failed")
            root = ET.fromstring(z.read("H10_data.xml"))
        target = []
        for element in root.iter():
            if element.tag.endswith("Series") and element.attrib.get("SERIES_NAME") == TARGET_BOARD:
                target.append((element.attrib, [x for x in element if x.tag.endswith("Obs")]))
        if len(target) != 1:
            errors.append(f"Expected one H.10 target series, found {len(target)}")
        else:
            attrs, obs = target[0]
            statuses, dates = {}, []
            for item in obs:
                status = item.attrib.get("OBS_STATUS", "")
                statuses[status] = statuses.get(status, 0) + 1
                dates.append(item.attrib.get("TIME_PERIOD", ""))
            manifest["checks"]["h10_target_series"] = {"series_name": TARGET_BOARD,
                "series_attributes": attrs, "observation_count": len(obs), "status_counts": statuses,
                "first_date": min(dates) if dates else None, "last_date": max(dates) if dates else None,
                "duplicate_date_count": len(dates)-len(set(dates)),
                "active_observation_count": statuses.get("A", 0), "nd_observation_count": statuses.get("ND", 0)}
            if len(dates) != len(set(dates)):
                errors.append("Duplicate dates in H.10 target series")
    except Exception as exc:
        errors.append(f"H.10 ZIP/XML parse: {type(exc).__name__}: {exc}")

required_ok = ("fed_h10_xml.zip" in manifest["sources"] and
               "ddp_fred_crosswalk.csv" in manifest["sources"] and
               len(manifest["fred_windows"]) == len(WINDOWS) and not errors)
manifest["status"] = "PASS_CAPTURE" if required_ok else "PARTIAL_BLOCKED"
(OUT / "capture_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, sort_keys=True))
sys.exit(0 if required_ok else 2)
