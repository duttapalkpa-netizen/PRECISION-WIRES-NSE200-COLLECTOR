#!/usr/bin/env python3
"""Extract selected daily Federal Reserve H.10 series with status-preserving QA."""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import math
from collections import Counter
from datetime import date
from pathlib import Path
from zipfile import ZipFile, BadZipFile
import xml.etree.ElementTree as ET

MESSAGE_NS = "http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message"
STRUCTURE_NS = "http://www.SDMX.org/resources/SDMXML/schemas/v1_0/structure"
FRB_NS = "http://www.federalreserve.gov/structure/compact/common"
H10_NS = "http://www.federalreserve.gov/structure/compact/H10_H10"
REQUIRED = {
    "JRXWTFB_N.B": {"column": "broad_usd_index", "fx": "BRD", "unit": "Index:_1997_Jan_100", "currency": "NA"},
    "JRXWTFN_N.B": {"column": "advanced_usd_index", "fx": "AFE", "unit": "Index:_1997_Jan_100", "currency": "NA"},
    "JRXWTFO_N.B": {"column": "emerging_usd_index", "fx": "EME", "unit": "Index:_1997_Jan_100", "currency": "NA"},
    "RXI_N.B.IN": {"column": "usd_inr", "fx": "INR", "unit": "Currency", "currency": "INR"},
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_archive(archive_path: Path, raw_manifest_path: Path, output_dir: Path) -> dict:
    raw = archive_path.read_bytes()
    raw_manifest = json.loads(raw_manifest_path.read_text(encoding="utf-8"))
    digest = sha256(raw)
    if digest != raw_manifest.get("sha256"):
        raise ValueError("raw archive SHA-256 does not match retrieval manifest")
    if raw_manifest.get("source_class") != "OFFICIAL_GOVERNMENT":
        raise ValueError("raw source manifest is not classified as official government")

    with ZipFile(io.BytesIO(raw)) as zf:
        names = set(zf.namelist())
        required_files = {"H10_data.xml", "H10_struct.xml", "H10_H10.xsd", "frb_common.xsd"}
        if not required_files.issubset(names):
            raise ValueError(f"H.10 archive is missing required files: {sorted(required_files - names)}")
        bad = zf.testzip()
        if bad:
            raise BadZipFile(f"inner archive CRC failure: {bad}")
        data_bytes = zf.read("H10_data.xml")
        struct_bytes = zf.read("H10_struct.xml")
        xsd_bytes = {n: zf.read(n) for n in ("H10_H10.xsd", "frb_common.xsd")}

    data_root = ET.fromstring(data_bytes)
    struct_root = ET.fromstring(struct_bytes)
    for name, payload in xsd_bytes.items():
        ET.fromstring(payload)  # well-formedness only; not full XSD validation
    header_prepared = data_root.findtext(f".//{{{MESSAGE_NS}}}Prepared")
    if not header_prepared:
        raise ValueError("H.10 data XML is missing the Prepared timestamp")

    freq_description = None
    for codelist in struct_root.findall(f".//{{{STRUCTURE_NS}}}CodeList"):
        if codelist.get("id") == "CL_FREQ":
            for code in codelist.findall(f"{{{STRUCTURE_NS}}}Code"):
                if code.get("value") == "9":
                    freq_description = code.findtext(f"{{{STRUCTURE_NS}}}Description")
                    break
    if freq_description != "Business day":
        raise ValueError(f"frequency code 9 did not resolve to Business day: {freq_description!r}")

    all_series = data_root.findall(f".//{{{H10_NS}}}Series")
    names_seen = [s.get("SERIES_NAME") for s in all_series]
    if len(names_seen) != len(set(names_seen)):
        raise ValueError("duplicate SERIES_NAME values found in H.10 XML")
    series_map = {s.get("SERIES_NAME"): s for s in all_series}

    parsed = {}
    for code, expected in REQUIRED.items():
        series = series_map.get(code)
        if series is None:
            raise ValueError(f"required H.10 series missing: {code}")
        attrs = {k: series.get(k) for k in ("FREQ", "UNIT", "UNIT_MULT", "FX", "CURRENCY")}
        if attrs["FREQ"] != "9" or attrs["UNIT"] != expected["unit"] or attrs["FX"] != expected["fx"] or attrs["CURRENCY"] != expected["currency"] or attrs["UNIT_MULT"] != "1":
            raise ValueError(f"series metadata mismatch for {code}: {attrs}")
        observations = {}
        obs_counts = Counter()
        for obs in series.findall(f"{{{FRB_NS}}}Obs"):
            period = obs.get("TIME_PERIOD")
            value = obs.get("OBS_VALUE")
            status = obs.get("OBS_STATUS")
            try:
                date.fromisoformat(period or "")
            except ValueError as exc:
                raise ValueError(f"invalid date in {code}: {period!r}") from exc
            if period in observations:
                raise ValueError(f"duplicate date in {code}: {period}")
            if status not in {"A", "ND"}:
                raise ValueError(f"unexpected OBS_STATUS in {code}: {status!r}")
            try:
                numeric = float(value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"non-numeric OBS_VALUE in {code} at {period}") from exc
            if not math.isfinite(numeric):
                raise ValueError(f"non-finite OBS_VALUE in {code} at {period}")
            if status == "ND" and numeric != -9999:
                raise ValueError(f"ND sentinel mismatch in {code} at {period}: {value}")
            if status == "A" and numeric == -9999:
                raise ValueError(f"active observation uses ND sentinel in {code} at {period}")
            observations[period] = {"raw_value": value, "status": status, "value": numeric if status == "A" else None}
            obs_counts[status] += 1
        periods = list(observations)
        if not periods or periods != sorted(periods):
            raise ValueError(f"observations are empty or not in ascending order for {code}")
        parsed[code] = {"attributes": attrs, "observations": observations, "counts": dict(obs_counts), "first": periods[0], "last": periods[-1], "count": len(periods)}

    index_codes = ("JRXWTFB_N.B", "JRXWTFN_N.B", "JRXWTFO_N.B")
    index_calendars = [set(parsed[c]["observations"]) for c in index_codes]
    index_dates = index_calendars[0]
    if any(cal != index_dates for cal in index_calendars[1:]):
        raise ValueError("three dollar-index series do not share an identical observation calendar")
    inr_dates = set(parsed["RXI_N.B.IN"]["observations"])
    if not index_dates.issubset(inr_dates):
        raise ValueError("USD/INR series does not cover every dollar-index business date")
    dates = sorted(index_dates)

    output_dir.mkdir(parents=True, exist_ok=True)
    panel_path = output_dir / "fed_h10_daily_fx_panel.csv"
    fields = ["date"]
    for meta in REQUIRED.values():
        fields += [meta["column"], meta["column"] + "_status"]
    with panel_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for period in dates:
            row = {"date": period}
            for code, meta in REQUIRED.items():
                item = parsed[code]["observations"][period]
                row[meta["column"]] = "" if item["value"] is None else format(item["value"], ".10g")
                row[meta["column"] + "_status"] = item["status"]
            writer.writerow(row)

    panel_bytes = panel_path.read_bytes()
    manifest = {
        "status": "PANEL_EXTRACTED_WITH_STATUS_PRESERVATION_SCHEMA_VALIDATION_PENDING",
        "source": raw_manifest.get("source"),
        "source_url": raw_manifest.get("source_url"),
        "raw_archive_sha256": digest,
        "raw_archive_bytes": len(raw),
        "retrieved_at_utc": raw_manifest.get("retrieved_at_utc"),
        "data_release_prepared_at": header_prepared,
        "inner_files_sha256": {"H10_data.xml": sha256(data_bytes), "H10_struct.xml": sha256(struct_bytes), **{n: sha256(b) for n,b in xsd_bytes.items()}},
        "inner_xsd_files_well_formed": True,
        "xml_message_namespace": MESSAGE_NS,
        "frequency_code": "9",
        "frequency_description": freq_description,
        "total_series_in_release": len(all_series),
        "selected_series": {
            code: {"fx": parsed[code]["attributes"]["FX"], "unit": parsed[code]["attributes"]["UNIT"], "unit_multiplier": parsed[code]["attributes"]["UNIT_MULT"], "first_observation": parsed[code]["first"], "last_observation": parsed[code]["last"], "observations": parsed[code]["count"], "status_counts": parsed[code]["counts"]}
            for code in REQUIRED
        },
        "calendar": {"rows": len(dates), "start": dates[0], "end": dates[-1], "dollar_index_series_identical_calendar": True, "usd_inr_covers_every_dollar_index_date": True, "usd_inr_full_history_rows": parsed["RXI_N.B.IN"]["count"]},
        "panel_file": panel_path.name,
        "panel_sha256": sha256(panel_bytes),
        "panel_bytes": len(panel_bytes),
        "missing_policy": "OBS_STATUS=ND values are emitted as blank with the original status retained; no imputation or forward fill.",
        "xsd_validation": {"status": "UNKNOWN_NOT_RUN", "reason": "The official raw ZIP contains H10_H10.xsd and frb_common.xsd but omits the imported SDMX-ML v1.0 files SDMXMessage.xsd, SDMXCompactData.xsd and SDMXCommon.xsd. SDMX-ML v2.1 schemas are not substituted."},
        "production_integration": "NOT_AUTHORIZED",
    }
    manifest_path = output_dir / "fed_h10_daily_fx_panel_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archive", required=True)
    p.add_argument("--raw-manifest", required=True)
    p.add_argument("--output-dir", default="artifacts/processed/fed_h10")
    args = p.parse_args()
    result = parse_archive(Path(args.archive), Path(args.raw_manifest), Path(args.output_dir))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
