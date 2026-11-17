#!/usr/bin/env python3
"""Fetch full-history public FRED CSV exports for four Board H.10 daily series.

Raw bytes are archived before parsing. Missing values remain blank; no fill,
calendar fabrication, series substitution, or claim of capital flows is made.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(".")
BASE = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="
OUT = ROOT / "data/global_capital_rotation/fed_h10"
RAW = OUT / "raw"
UA = "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (research-only; public FRED CSV download)"
SERIES = {
    # Three H.10 nominal dollar indices.
    "DTWEXBGS": {"name":"Nominal Broad U.S. Dollar Index","unit":"Index Jan 2006=100","frequency":"Daily","h10_code":"H10/H10/JRXWTFB_N.B","expected_start":"2006-01-02","source_type":"PRICE_INDEX"},
    "DTWEXAFEGS": {"name":"Nominal Advanced Foreign Economies U.S. Dollar Index","unit":"Index Jan 2006=100","frequency":"Daily","h10_code":"H10/H10/JRXWTFN_N.B","expected_start":"2006-01-02","source_type":"PRICE_INDEX"},
    "DTWEXEMEGS": {"name":"Nominal Emerging Market Economies U.S. Dollar Index","unit":"Index Jan 2006=100","frequency":"Daily","h10_code":"H10/H10/JRXWTFO_N.B","expected_start":"2006-01-02","source_type":"PRICE_INDEX"},
    # All 23 bilateral daily FX series present in the user's H.10 snapshot.
    # Unit direction is preserved: four series are USD per foreign currency;
    # the remaining 19 are foreign-currency units per USD.
    "DEXUSAL": {"name":"U.S. Dollars to Australian Dollar Spot Exchange Rate","unit":"U.S. dollars per Australian dollar","frequency":"Daily","h10_code":"H10/H10/RXI$US_N.B.AL","source_type":"FX_RATE"},
    "DEXUSEU": {"name":"U.S. Dollars to Euro Spot Exchange Rate","unit":"U.S. dollars per euro","frequency":"Daily","h10_code":"H10/H10/RXI$US_N.B.EU","source_type":"FX_RATE"},
    "DEXUSNZ": {"name":"U.S. Dollars to New Zealand Dollar Spot Exchange Rate","unit":"U.S. dollars per New Zealand dollar","frequency":"Daily","h10_code":"H10/H10/RXI$US_N.B.NZ","source_type":"FX_RATE"},
    "DEXUSUK": {"name":"U.S. Dollars to U.K. Pound Sterling Spot Exchange Rate","unit":"U.S. dollars per pound sterling","frequency":"Daily","h10_code":"H10/H10/RXI$US_N.B.UK","source_type":"FX_RATE"},
    "DEXBZUS": {"name":"Brazilian Reals to U.S. Dollar Spot Exchange Rate","unit":"Brazilian reals per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.BZ","source_type":"FX_RATE"},
    "DEXCAUS": {"name":"Canadian Dollars to U.S. Dollar Spot Exchange Rate","unit":"Canadian dollars per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.CA","source_type":"FX_RATE"},
    "DEXCHUS": {"name":"Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate","unit":"Chinese yuan per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.CH","source_type":"FX_RATE"},
    "DEXDNUS": {"name":"Danish Kroner to U.S. Dollar Spot Exchange Rate","unit":"Danish kroner per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.DN","source_type":"FX_RATE"},
    "DEXHKUS": {"name":"Hong Kong Dollars to U.S. Dollar Spot Exchange Rate","unit":"Hong Kong dollars per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.HK","source_type":"FX_RATE"},
    "DEXINUS": {"name":"Indian Rupees to U.S. Dollar Spot Exchange Rate","unit":"Indian rupees per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.IN","expected_start":"1973-01-02","source_type":"FX_RATE","note":"Noon buying rate in New York City; not RBI reference rate or DBIE interbank close."},
    "DEXJPUS": {"name":"Japanese Yen to U.S. Dollar Spot Exchange Rate","unit":"Japanese yen per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.JA","source_type":"FX_RATE"},
    "DEXMAUS": {"name":"Malaysian Ringgit to U.S. Dollar Spot Exchange Rate","unit":"Malaysian ringgit per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.MA","source_type":"FX_RATE"},
    "DEXMXUS": {"name":"Mexican Pesos to U.S. Dollar Spot Exchange Rate","unit":"Mexican pesos per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.MX","source_type":"FX_RATE"},
    "DEXNOUS": {"name":"Norwegian Kroner to U.S. Dollar Spot Exchange Rate","unit":"Norwegian kroner per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.NO","source_type":"FX_RATE"},
    "DEXSFUS": {"name":"South African Rand to U.S. Dollar Spot Exchange Rate","unit":"South African rand per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.SF","source_type":"FX_RATE"},
    "DEXSIUS": {"name":"Singapore Dollars to U.S. Dollar Spot Exchange Rate","unit":"Singapore dollars per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.SI","source_type":"FX_RATE"},
    "DEXKOUS": {"name":"South Korean Won to U.S. Dollar Spot Exchange Rate","unit":"South Korean won per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.KO","source_type":"FX_RATE"},
    "DEXSLUS": {"name":"Sri Lankan Rupees to U.S. Dollar Spot Exchange Rate","unit":"Sri Lankan rupees per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.SL","source_type":"FX_RATE"},
    "DEXSDUS": {"name":"Swedish Kronor to U.S. Dollar Spot Exchange Rate","unit":"Swedish kronor per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.SD","source_type":"FX_RATE"},
    "DEXSZUS": {"name":"Swiss Francs to U.S. Dollar Spot Exchange Rate","unit":"Swiss francs per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.SZ","source_type":"FX_RATE"},
    "DEXTAUS": {"name":"Taiwan Dollars to U.S. Dollar Spot Exchange Rate","unit":"Taiwan dollars per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.TA","source_type":"FX_RATE"},
    "DEXTHUS": {"name":"Thai Baht to U.S. Dollar Spot Exchange Rate","unit":"Thai baht per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.TH","source_type":"FX_RATE"},
    "DEXVZUS": {"name":"Venezuelan Bolivares to U.S. Dollar Spot Exchange Rate","unit":"Venezuelan bolivares per U.S. dollar","frequency":"Daily","h10_code":"H10/H10/RXI_N.B.VES","source_type":"FX_RATE"},
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def get_bytes(url: str, attempts: int = 2) -> tuple[bytes, dict]:
    last = None
    for n in range(attempts):
        try:
            req = Request(url, headers={"User-Agent": UA, "Accept": "text/csv,*/*"})
            with urlopen(req, timeout=20) as response:
                body = response.read()
                meta = {
                    "http_status": response.status,
                    "content_type": response.headers.get("Content-Type"),
                    "last_modified": response.headers.get("Last-Modified"),
                    "final_url": response.geturl(),
                }
            if not body or b"\x00" in body[:256]:
                raise ValueError("empty or non-text CSV response")
            return body, meta
        except Exception as exc:
            last = exc
            if n + 1 < attempts:
                time.sleep(1.0)
    raise RuntimeError(f"FRED download failed after {attempts} bounded attempts: {last}")

def parse_csv(series_id: str, raw: bytes) -> tuple[list[dict], dict]:
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    fields = [str(x or "").strip() for x in (reader.fieldnames or [])]
    date_col = next((x for x in fields if x.lower() in {"date", "observation_date"}), None)
    value_col = next((x for x in fields if x.upper() == series_id), None)
    if not date_col or not value_col:
        raise ValueError(f"{series_id}: unexpected FRED CSV schema {fields}")
    rows = []
    seen = set()
    previous = None
    missing = 0
    for line_no, row in enumerate(reader, start=2):
        day = (row.get(date_col) or "").strip()
        val = (row.get(value_col) or "").strip()
        if not day:
            raise ValueError(f"{series_id}: blank date at line {line_no}")
        datetime.strptime(day, "%Y-%m-%d")
        if day in seen:
            raise ValueError(f"{series_id}: duplicate date {day}")
        if previous is not None and day <= previous:
            raise ValueError(f"{series_id}: non-monotonic date {day}")
        seen.add(day)
        previous = day
        if val in {"", ".", "NA", "N/A"}:
            value = ""
            missing += 1
        else:
            number = float(val)
            if number != number or number in (float("inf"), float("-inf")):
                raise ValueError(f"{series_id}: non-finite numeric value at {day}")
            value = format(number, ".10g")
        rows.append({"DATE": day, "VALUE": value})
    if not rows:
        raise ValueError(f"{series_id}: no observations")
    return rows, {
        "row_count": len(rows),
        "unique_dates": len(seen),
        "nonmissing_values": len(rows) - missing,
        "missing_values": missing,
        "first_observation": rows[0]["DATE"],
        "last_observation": rows[-1]["DATE"],
        "expected_start_match": (rows[0]["DATE"] == SERIES[series_id]["expected_start"]) if SERIES[series_id].get("expected_start") else None,
    }

def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    if len(SERIES) != 26 or sum(1 for x in SERIES.values() if x["source_type"] == "FX_RATE") != 23:
        raise RuntimeError("H.10 mapping contract must contain 3 dollar indices + 23 bilateral FX series")
    h10_codes = [x["h10_code"] for x in SERIES.values()]
    if len(set(h10_codes)) != len(h10_codes):
        raise RuntimeError("Duplicate H.10 source-series mapping")
    retrieved = datetime.now(timezone.utc).isoformat()
    manifest = {
        "schema_version": "1.0",
        "status": "BLOCKED",
        "dataset": "Board of Governors H.10 daily dollar indices and INR spot FX via FRED",
        "retrieved_at_utc": retrieved,
        "distribution_interface": "Federal Reserve Bank of St. Louis FRED public CSV",
        "source_owner": "Board of Governors of the Federal Reserve System (US)",
        "release": "H.10 Foreign Exchange Rates",
        "revision_policy": "FRED observations can be revised; this is a retrieval-vintage snapshot.",
        "synthetic_rows": False,
        "forward_fill": False,
        "series": {},
        "outputs": {},
    }
    combined = {}
    try:
        for sid, spec in SERIES.items():
            url = BASE + sid
            raw, response_meta = get_bytes(url)
            raw_path = RAW / f"{sid}.csv"
            raw_path.write_bytes(raw)
            rows, qa = parse_csv(sid, raw)
            if qa["expected_start_match"] is False:
                raise ValueError(f"{sid}: unexpected first observation {qa['first_observation']}")
            manifest["series"][sid] = {
                **spec,
                "source_url": url,
                "final_url": response_meta["final_url"],
                "http_status": response_meta["http_status"],
                "content_type": response_meta["content_type"],
                "last_modified_header": response_meta["last_modified"],
                "retrieved_at_utc": retrieved,
                "raw_path": str(raw_path),
                "raw_bytes": len(raw),
                "raw_sha256": sha256(raw),
                **qa,
            }
            for row in rows:
                combined.setdefault(row["DATE"], {})[sid] = row["VALUE"]

        long_path = OUT / "daily_historical_panel_long.csv"
        with long_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["DATE", "SERIES_ID", "VALUE"])
            for sid in SERIES:
                for day in sorted(combined):
                    if sid in combined[day]:
                        w.writerow([day, sid, combined[day][sid]])

        wide_path = OUT / "daily_historical_panel_wide.csv"
        with wide_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["DATE", *SERIES.keys()])
            for day in sorted(combined):
                w.writerow([day, *[combined[day].get(sid, "") for sid in SERIES]])

        for path in (long_path, wide_path):
            data = path.read_bytes()
            manifest["outputs"][str(path)] = {"bytes": len(data), "sha256": sha256(data)}
        manifest["date_union"] = {
            "unique_dates": len(combined),
            "first_date": min(combined),
            "last_date": max(combined),
        }
        manifest["status"] = "PASS_RAW_FULL_HISTORY_DOWNLOADED_AND_SCHEMA_QA"
        manifest["acceptance_boundary"] = (
            "Source downloads and per-series schema/date QA only. Does not prove point-in-time "
            "vintage availability, NSE-session coverage, RBI equivalence, event-study maturity, "
            "capital flows, or production readiness."
        )
    except Exception as exc:
        manifest["status"] = "BLOCKED"
        manifest["failure"] = f"{type(exc).__name__}: {str(exc)[:500]}"
        (OUT / "daily_historical_panel_manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        print(json.dumps(manifest, indent=2))
        raise

    (OUT / "daily_historical_panel_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
