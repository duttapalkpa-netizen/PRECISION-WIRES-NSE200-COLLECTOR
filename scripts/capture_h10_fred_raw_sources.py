#!/usr/bin/env python3
"""Capture official H.10 XML ZIP, FRED graph CSV, and Fed DDP/FRED crosswalk.

No API key, paid service, synthetic values, or production integration.
Raw response bytes are preserved before parsing; missing values remain missing.
"""
from __future__ import annotations
import csv, hashlib, io, json, os, sys, urllib.request, zipfile
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(os.environ.get("OUT_DIR", "artifacts/h10_fred_capture"))
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
    "fed_h10_xml.zip": "https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip",
    "fred_dtwexbgs.csv": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS",
    "ddp_fred_crosswalk.csv": "https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv",
}
TARGET_BOARD = "JRXWTFB_N.B"
TARGET_FRED = "DTWEXBGS"

def fetch(name: str, url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "PRECISION-WIRES-research/1.0"})
    with urllib.request.urlopen(req, timeout=180) as response:
        data = response.read()
        meta = {
            "url": url,
            "final_url": response.geturl(),
            "http_status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "content_length_header": response.headers.get("Content-Length"),
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "byte_length": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    if not data:
        raise RuntimeError(f"{name}: empty response")
    (OUT / name).write_bytes(data)
    return meta

manifest = {"schema_version": 1, "sources": {}, "checks": {}, "status": "INCOMPLETE"}
errors = []
for name, url in SOURCES.items():
    try:
        manifest["sources"][name] = fetch(name, url)
    except Exception as exc:
        errors.append(f"{name}: {type(exc).__name__}: {exc}")

if "fred_dtwexbgs.csv" in manifest["sources"]:
    raw = (OUT / "fred_dtwexbgs.csv").read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(raw)))
    manifest["checks"]["fred_csv"] = {
        "rows": len(rows),
        "has_observation_date": bool(rows and "observation_date" in rows[0]),
        "first_date": rows[0].get("observation_date") if rows else None,
        "last_date": rows[-1].get("observation_date") if rows else None,
        "missing_values_preserved": any((r.get(TARGET_FRED, "") in ("", ".")) for r in rows),
    }
    if not rows or "observation_date" not in rows[0] or TARGET_FRED not in rows[0]:
        errors.append("FRED CSV schema/rows invalid")

if "ddp_fred_crosswalk.csv" in manifest["sources"]:
    raw = (OUT / "ddp_fred_crosswalk.csv").read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(raw)))
    cols = list(rows[0].keys()) if rows else []
    def norm(s): return (s or "").strip().lower().replace(" ", "_")
    board_col = next((c for c in cols if norm(c) in ("board_series_id", "ddp_series_id", "series_id")), None)
    fred_col = next((c for c in cols if norm(c) == "fred_series_id"), None)
    release_col = next((c for c in cols if norm(c) in ("ddp_release", "release_id", "release")), None)
    matches = [r for r in rows if board_col and fred_col and r.get(board_col, "").strip() == TARGET_BOARD and r.get(fred_col, "").strip() == TARGET_FRED and (not release_col or r.get(release_col, "").strip().upper() == "H10")]
    manifest["checks"]["crosswalk"] = {
        "columns": cols, "rows": len(rows), "board_column": board_col,
        "fred_column": fred_col, "release_column": release_col,
        "target_exact_match_count": len(matches),
        "target_rows": matches,
    }
    if len(matches) != 1:
        errors.append(f"Expected exactly one crosswalk match, found {len(matches)}")

if "fed_h10_xml.zip" in manifest["sources"]:
    try:
        with zipfile.ZipFile(OUT / "fed_h10_xml.zip") as z:
            members = z.namelist()
            bad = z.testzip()
            manifest["checks"]["h10_zip"] = {
                "member_count": len(members), "members": members[:50],
                "zip_integrity": "PASS" if bad is None else "FAIL",
                "first_bad_member": bad,
            }
            if bad is not None or not members:
                errors.append("H.10 ZIP integrity or member check failed")
    except Exception as exc:
        errors.append(f"H.10 ZIP parse failed: {type(exc).__name__}: {exc}")


if "fed_h10_xml.zip" in manifest["sources"]:
    try:
        with zipfile.ZipFile(OUT / "fed_h10_xml.zip") as z:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(z.read("H10_data.xml"))
            target = []
            for element in root.iter():
                if element.tag.endswith("Series") and element.attrib.get("SERIES_NAME") == TARGET_BOARD:
                    observations = [x for x in element if x.tag.endswith("Obs")]
                    target.append((element.attrib, observations))
            if len(target) != 1:
                errors.append(f"Expected one H.10 target series, found {len(target)}")
            else:
                attrs, observations = target[0]
                statuses = {}
                dates = []
                for obs in observations:
                    status = obs.attrib.get("OBS_STATUS", "")
                    statuses[status] = statuses.get(status, 0) + 1
                    dates.append(obs.attrib.get("TIME_PERIOD", ""))
                manifest["checks"]["h10_target_series"] = {
                    "series_name": TARGET_BOARD,
                    "series_attributes": attrs,
                    "observation_count": len(observations),
                    "status_counts": statuses,
                    "first_date": min(dates) if dates else None,
                    "last_date": max(dates) if dates else None,
                    "duplicate_date_count": len(dates) - len(set(dates)),
                    "active_observation_count": statuses.get("A", 0),
                    "nd_observation_count": statuses.get("ND", 0),
                }
                if len(dates) != len(set(dates)):
                    errors.append("Duplicate dates in H.10 target series")
    except Exception as exc:
        errors.append(f"H.10 target-series parse failed: {type(exc).__name__}: {exc}")
manifest["errors"] = errors
manifest["status"] = "PASS_CAPTURE" if not errors and len(manifest["sources"]) == 3 else "PARTIAL_BLOCKED"
(OUT / "capture_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, sort_keys=True))
sys.exit(0 if manifest["status"] == "PASS_CAPTURE" else 2)
