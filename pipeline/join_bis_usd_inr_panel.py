#!/usr/bin/env python3
"""Join BIS daily USD/INR to the H.10 panel without filling missing observations."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from datetime import date
from pathlib import Path
from statistics import mean, median


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def join_panel(panel_path: Path, bis_csv_path: Path, bis_manifest_path: Path, output_dir: Path) -> dict:
    bis_bytes = bis_csv_path.read_bytes()
    bis_manifest = json.loads(bis_manifest_path.read_text(encoding="utf-8"))
    if sha256(bis_bytes) != bis_manifest.get("sha256"):
        raise ValueError("BIS raw CSV SHA-256 does not match retrieval manifest")
    if bis_manifest.get("source_class") != "OFFICIAL_INTERNATIONAL_ORGANIZATION":
        raise ValueError("BIS source manifest is not classified as an official international organization")
    if bis_manifest.get("series") != "D.IN.INR.A" or bis_manifest.get("dataflow") != "BIS,WS_XRU,1.0":
        raise ValueError("BIS source manifest does not identify the expected USD/INR series")

    with panel_path.open(newline="", encoding="utf-8") as f:
        panel = list(csv.DictReader(f))
    if not panel:
        raise ValueError("H.10 panel is empty")
    panel_dates = [r.get("date", "") for r in panel]
    if panel_dates != sorted(panel_dates) or len(panel_dates) != len(set(panel_dates)):
        raise ValueError("H.10 panel dates are not unique and ascending")

    with bis_csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"FREQ", "REF_AREA", "CURRENCY", "COLLECTION", "TIME_PERIOD", "OBS_VALUE", "OBS_STATUS", "UNIT_MULT", "OBS_CONF"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"BIS CSV missing required columns: {sorted(required - set(reader.fieldnames or []))}")
        bis_rows = list(reader)
    bis_map = {}
    for row in bis_rows:
        if (row["FREQ"], row["REF_AREA"], row["CURRENCY"], row["COLLECTION"]) != ("D", "IN", "INR", "A"):
            raise ValueError("BIS CSV contains an unexpected frequency, area, currency or collection dimension")
        if row["UNIT_MULT"] != "0" or row["OBS_CONF"] != "F":
            raise ValueError("BIS CSV has unexpected unit multiplier or confidentiality metadata")
        period = row["TIME_PERIOD"]
        try:
            date.fromisoformat(period)
        except ValueError as exc:
            raise ValueError(f"invalid BIS TIME_PERIOD: {period!r}") from exc
        if period in bis_map:
            raise ValueError(f"duplicate BIS observation date: {period}")
        status = row["OBS_STATUS"]
        if status not in {"A", "M"}:
            raise ValueError(f"unexpected BIS OBS_STATUS: {status!r}")
        if status == "A":
            try:
                value = float(row["OBS_VALUE"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"invalid active BIS value on {period}") from exc
            if not math.isfinite(value):
                raise ValueError(f"non-finite active BIS value on {period}")
        else:
            if row["OBS_VALUE"] not in {"NaN", "", "nan"}:
                raise ValueError(f"BIS missing status has unexpected value on {period}")
        bis_map[period] = row
    bis_dates = list(bis_map)
    if bis_dates != sorted(bis_dates):
        raise ValueError("BIS observations are not in ascending date order")

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "fed_h10_bis_usd_inr_daily_panel.csv"
    fields = list(panel[0].keys()) + ["bis_usd_inr", "bis_usd_inr_status"]
    counts = Counter()
    diffs = []
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in panel:
            period = row["date"]
            bis = bis_map.get(period)
            out = dict(row)
            if bis is None:
                out["bis_usd_inr"] = ""
                out["bis_usd_inr_status"] = "NO_OBSERVATION"
                counts["NO_OBSERVATION"] += 1
            else:
                status = bis["OBS_STATUS"]
                out["bis_usd_inr_status"] = status
                out["bis_usd_inr"] = bis["OBS_VALUE"] if status == "A" else ""
                counts[status] += 1
                if status == "A" and row.get("usd_inr_status") == "A":
                    diffs.append(abs(float(row["usd_inr"]) - float(bis["OBS_VALUE"])))
            writer.writerow(out)

    out_bytes = out_path.read_bytes()
    active_pairs = len(diffs)
    manifest = {
        "status": "DUAL_SOURCE_DAILY_PANEL_JOINED_WITH_EXPLICIT_GAPS",
        "h10_panel_sha256": sha256(panel_path.read_bytes()),
        "bis_raw_csv_sha256": sha256(bis_bytes),
        "bis_retrieved_at_utc": bis_manifest.get("retrieved_at_utc"),
        "bis_dataflow": bis_manifest["dataflow"],
        "bis_series": bis_manifest["series"],
        "bis_observations": len(bis_rows),
        "bis_first_observation": bis_dates[0],
        "bis_last_observation": bis_dates[-1],
        "h10_panel_rows": len(panel),
        "h10_panel_start": panel_dates[0],
        "h10_panel_end": panel_dates[-1],
        "bis_status_counts_on_h10_calendar": dict(counts),
        "both_sources_active_comparison_pairs": active_pairs,
        "h10_minus_bis_absolute_difference": {
            "mean": mean(diffs) if diffs else None,
            "median": median(diffs) if diffs else None,
            "max": max(diffs) if diffs else None,
        },
        "comparison_policy": "Keep H.10 and BIS USD/INR observations as separate source columns. Differences are descriptive only; no source is promoted and no values are overwritten.",
        "missing_policy": "BIS OBS_STATUS=M remains blank with status M; absent dates are blank with status NO_OBSERVATION. No imputation or forward fill.",
        "output_file": out_path.name,
        "output_sha256": sha256(out_bytes),
        "output_bytes": len(out_bytes),
        "production_integration": "NOT_AUTHORIZED",
    }
    manifest_path = output_dir / "fed_h10_bis_usd_inr_daily_panel_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--h10-panel", required=True)
    p.add_argument("--bis-csv", required=True)
    p.add_argument("--bis-manifest", required=True)
    p.add_argument("--output-dir", default="artifacts/processed/fed_h10_bis")
    args = p.parse_args()
    print(json.dumps(join_panel(Path(args.h10_panel), Path(args.bis_csv), Path(args.bis_manifest), Path(args.output_dir)), indent=2))


if __name__ == "__main__":
    main()
