#!/usr/bin/env python3
"""Research-only official H.10 / FRED raw-byte capture and crosswalk gate."""
from __future__ import annotations
import csv, hashlib, json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from zipfile import ZipFile

OUT = Path("h10_fred_capture")
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
    "ddp_fred_crosswalk.csv": "https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv",
    "fred_dtwexbgs.csv": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS",
    "frb_h10_xml.zip": "https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip",
}
manifest = {"schema_version": 1, "purpose": "research_only_raw_capture", "retrieved_at_utc": datetime.now(timezone.utc).isoformat(), "sources": {}, "acceptance": {}}
errors = []

def capture(name: str, url: str) -> Path:
    path = OUT / name
    req = Request(url, headers={"User-Agent": "PRECISION-WIRES-research-audit/1.0", "Accept": "*/*"})
    last = None
    for attempt in range(3):
        try:
            with urlopen(req, timeout=90) as response:
                data = response.read()
                if response.status != 200 or not data:
                    raise RuntimeError(f"unexpected HTTP status/empty body: {response.status}/{len(data)}")
                path.write_bytes(data)
                headers = {k.lower(): v for k, v in response.headers.items()}
                manifest["sources"][name] = {
                    "requested_url": url, "final_url": response.geturl(),
                    "http_status": response.status, "response_headers": headers,
                    "byte_length": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                }
                return path
        except (HTTPError, URLError, TimeoutError, OSError, RuntimeError) as exc:
            last = repr(exc)
            time.sleep(attempt + 1)
    raise RuntimeError(f"{name}: {last}")

for name, url in SOURCES.items():
    try:
        capture(name, url)
    except Exception as exc:
        errors.append(str(exc))

# Parse the exact Board-published mapping by named columns, never by position.
crosswalk = OUT / "ddp_fred_crosswalk.csv"
if crosswalk.exists():
    try:
        with crosswalk.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            headers = [h.strip() for h in (reader.fieldnames or [])]
            required = {"ddp_release", "board_series_id", "fred_series_id"}
            if not required.issubset(set(headers)):
                raise ValueError(f"required columns missing; observed={headers}")
            matches = []
            for row in reader:
                norm = {str(k).strip().lower(): (v or "").strip() for k, v in row.items() if k}
                board = norm.get("board_series_id", "")
                release = norm.get("ddp_release", "").upper()
                fred = norm.get("fred_series_id", "")
                board_leaf = board.split("/")[-1]
                if release == "H10" and board_leaf == "JRXWTFB_N.B":
                    matches.append({"ddp_release": norm.get("ddp_release"), "board_series_id": board, "fred_series_id": fred})
            manifest["acceptance"]["crosswalk_target_rows"] = matches
            manifest["acceptance"]["crosswalk_exactly_one_target_row"] = len(matches) == 1
            if len(matches) != 1 or matches[0].get("fred_series_id") != "DTWEXBGS":
                errors.append(f"crosswalk target row gate failed: rows={len(matches)}, matches={matches}")
    except Exception as exc:
        errors.append(f"crosswalk parse failed: {exc}")

# Basic payload checks only; this is not the full date/value reconciliation.
fred = OUT / "fred_dtwexbgs.csv"
if fred.exists():
    try:
        with fred.open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        if not rows or "observation_date" not in rows[0] or "DTWEXBGS" not in rows[0]:
            raise ValueError("FRED CSV missing expected observation_date / DTWEXBGS columns")
        manifest["acceptance"]["fred_row_count"] = len(rows)
        manifest["acceptance"]["fred_first_date"] = rows[0]["observation_date"]
        manifest["acceptance"]["fred_last_date"] = rows[-1]["observation_date"]
    except Exception as exc:
        errors.append(f"FRED CSV parse failed: {exc}")

h10 = OUT / "frb_h10_xml.zip"
if h10.exists():
    try:
        with ZipFile(h10) as zf:
            bad = zf.testzip()
            if bad:
                raise ValueError(f"ZIP CRC failure at {bad}")
            manifest["acceptance"]["h10_zip_member_count"] = len(zf.namelist())
            manifest["acceptance"]["h10_zip_crc_test"] = "PASS"
    except Exception as exc:
        errors.append(f"H.10 ZIP validation failed: {exc}")

manifest["errors"] = errors
manifest["status"] = "CAPTURE_AND_BASIC_VALIDATION_PASS" if not errors and len(manifest["sources"]) == 3 else "BLOCKED"
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, sort_keys=True))
if errors or len(manifest["sources"]) != 3:
    sys.exit(1)
