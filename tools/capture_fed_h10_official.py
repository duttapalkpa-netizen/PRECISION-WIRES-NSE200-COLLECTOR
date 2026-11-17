#!/usr/bin/env python3
"""Capture the official Federal Reserve H.10 ZIP response with transport evidence."""
from __future__ import annotations
import csv, hashlib, json, os, sys, urllib.request, urllib.error, zipfile, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

URL = "https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10"
OUT = Path(os.environ.get("OUTPUT_DIR", "fed_h10_capture"))
OUT.mkdir(parents=True, exist_ok=True)
started = datetime.now(timezone.utc)
request = urllib.request.Request(URL, headers={"User-Agent": "PRECISION-WIRES-research-evidence-capture/1.0", "Accept": "application/zip, application/octet-stream;q=0.9, */*;q=0.8"})
try:
    with urllib.request.urlopen(request, timeout=90) as response:
        retrieved = datetime.now(timezone.utc)
        status = response.status
        final_url = response.geturl()
        headers = {k.lower(): v for k, v in response.headers.items()}
        payload = response.read()
except Exception as exc:
    print(f"official H.10 download failed: {type(exc).__name__}: {exc}", file=sys.stderr)
    raise

if status != 200:
    raise SystemExit(f"unexpected HTTP status: {status}")
if not payload:
    raise SystemExit("empty H.10 response")
content_type = headers.get("content-type", "").split(";", 1)[0].strip().lower()
if "zip" not in content_type and not payload.startswith(b"PK\\x03\\x04"):
    raise SystemExit(f"response is not a ZIP payload: content-type={content_type!r}")
zip_path = OUT / "FRB_H10_official_response.zip"
zip_path.write_bytes(payload)
with zipfile.ZipFile(zip_path) as archive:
    bad_member = archive.testzip()
    if bad_member:
        raise SystemExit(f"ZIP integrity failure in member {bad_member}")
    members = [{"name": x.filename, "size_bytes": x.file_size, "compressed_size_bytes": x.compress_size} for x in archive.infolist()]
    xml_root = ET.fromstring(archive.read("H10_data.xml"))
ns = {"message": "http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message",
      "frb": "http://www.federalreserve.gov/structure/compact/common",
      "kf": "http://www.federalreserve.gov/structure/compact/H10_H10"}
prepared = xml_root.findtext("message:Header/message:Prepared", namespaces=ns)
series_map = {
    "JRXWTFB_N.B": ("fed_h10_nominal_broad_dollar_index", "Index:_1997_Jan_100"),
    "JRXWTFN_N.B": ("fed_h10_nominal_advanced_dollar_index", "Index:_1997_Jan_100"),
    "JRXWTFO_N.B": ("fed_h10_nominal_em_dollar_index", "Index:_1997_Jan_100"),
    "RXI_N.B.IN": ("fed_h10_inr_per_usd", "Currency")
}
series_summary = []
for series in xml_root.findall(".//kf:Series", ns):
    code = series.attrib.get("SERIES_NAME")
    if code in series_map:
        observations = series.findall("frb:Obs", ns)
        series_summary.append({
            "series_id": code, "indicator": series_map[code][0],
            "unit": series.attrib.get("UNIT"), "unit_multiplier": series.attrib.get("UNIT_MULT"),
            "observation_count": len(observations),
            "first_observation": observations[0].attrib if observations else None,
            "latest_observation": observations[-1].attrib if observations else None
        })
if len(series_summary) != len(series_map):
    raise SystemExit("one or more required H.10 series are absent from the downloaded XML")
manifest_dir = OUT / "evidence_manifests"
manifest_dir.mkdir(exist_ok=True)
for item in series_summary:
    code = item["series_id"]
    indicator, unit = series_map[code]
    evidence_id = "fed-h10-" + code.lower().replace(".", "-")
    series_manifest = {
        "schema_version": 1, "evidence_manifest_id": evidence_id,
        "source": "Federal Reserve Board H.10 Data Download Program",
        "source_url": URL, "final_url": final_url, "indicator": indicator, "unit": unit,
        "quality_status": "VERIFIED_OFFICIAL", "published_at": prepared,
        "retrieved_at": retrieved.isoformat(), "http_status": status,
        "content_type": content_type, "byte_length": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(), "raw_payload_path": zip_path.name,
        "series_id": code, "series_unit_multiplier": item["unit_multiplier"],
        "observation_count": item["observation_count"]
    }
    (manifest_dir / (evidence_id + ".json")).write_text(json.dumps(series_manifest, indent=2) + "\n", encoding="utf-8")
# Build a parser-ingestion fixture for the one registry-qualified broad-dollar series.
broad = next(x for x in series_summary if x["series_id"] == "JRXWTFB_N.B")
broad_id = "fed-h10-jrxwtfb_n-b"
broad_observations = next(
    series.findall("frb:Obs", ns) for series in xml_root.findall(".//kf:Series", ns)
    if series.attrib.get("SERIES_NAME") == "JRXWTFB_N.B"
)
csv_path = OUT / "fed_h10_broad_dollar_observations.csv"
columns = ["date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status",
           "evidence_manifest_id","raw_sha256","retrieved_at","http_status","content_type","byte_length","raw_payload_path"]
with csv_path.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=columns)
    writer.writeheader()
    for obs in broad_observations:
        value = obs.attrib.get("OBS_VALUE")
        if value in (None, "", "ND"):
            continue
        writer.writerow({
            "date": obs.attrib["TIME_PERIOD"], "indicator": "fed_h10_nominal_broad_dollar_index",
            "value": value, "unit": "Index:_1997_Jan_100",
            "source": "Federal Reserve Board H.10 Data Download Program", "source_url": URL,
            "published_at": prepared, "as_of_date": prepared[:10], "quality_status": "VERIFIED_OFFICIAL",
            "evidence_manifest_id": broad_id, "raw_sha256": hashlib.sha256(payload).hexdigest(),
            "retrieved_at": retrieved.isoformat(), "http_status": status, "content_type": content_type,
            "byte_length": len(payload), "raw_payload_path": zip_path.name
        })
from pipeline.global_capital_rotation_overlay import load_observations
loaded = load_observations(csv_path)
admitted = loaded.get("fed_h10_nominal_broad_dollar_index", [])
if len(admitted) != broad["observation_count"]:
    raise SystemExit(f"parser admission mismatch: expected {broad['observation_count']}, got {len(admitted)}")
if not admitted or admitted[-1]["date"] != broad["latest_observation"]["TIME_PERIOD"]:
    raise SystemExit("parser-admitted latest observation does not match official XML")
parser_admission = {
    "status": "PASS", "indicator": "fed_h10_nominal_broad_dollar_index",
    "admitted_observation_count": len(admitted),
    "first_observation_date": admitted[0]["date"], "latest_observation_date": admitted[-1]["date"],
    "latest_observation_value": admitted[-1]["value"], "manifest_id": broad_id
}
(OUT / "fed_h10_parser_admission.json").write_text(json.dumps(parser_admission, indent=2) + "\\n", encoding="utf-8")
manifest = {
    "schema_version": 1,
    "evidence_type": "official_http_transport_capture",
    "publisher": "Board of Governors of the Federal Reserve System",
    "dataset": "G.5/H.10 - Foreign Exchange Rates",
    "requested_url": URL,
    "final_url": final_url,
    "request_started_at_utc": started.isoformat(),
    "retrieved_at_utc": retrieved.isoformat(),
    "http_status": status,
    "response_headers": headers,
    "content_type": content_type,
    "byte_length": len(payload),
    "sha256": hashlib.sha256(payload).hexdigest(),
    "raw_payload_path": zip_path.name,
    "zip_integrity_test": "PASS",
    "members": members,
    "source_prepared_timestamp": prepared,
    "selected_series": series_summary,
    "github": {
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "commit_sha": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT")
    }
}
(OUT / "FRB_H10_official_response_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
(OUT / "FRB_H10_official_response.sha256").write_text(f"{manifest['sha256']}  {zip_path.name}\n", encoding="ascii")
print(json.dumps({k: manifest[k] for k in ("final_url","retrieved_at_utc","http_status","content_type","byte_length","sha256","zip_integrity_test")}, indent=2))
