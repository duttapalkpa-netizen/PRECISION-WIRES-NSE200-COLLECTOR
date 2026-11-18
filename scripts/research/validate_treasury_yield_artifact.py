#!/usr/bin/env python3
"""Independently validate a Treasury macro-history GitHub Actions ZIP artifact.

Usage:
  python scripts/research/validate_treasury_yield_artifact.py treasury-macro-history-<run-id>.zip

Checks ZIP integrity, manifest page byte counts/SHA-256/HTTP status, Atom XML
entry counts, empty-page pagination terminators, raw observation dates/values,
normalized CSV hashes/row counts, duplicate dates, and exact raw-to-CSV equality.
Only Python standard-library modules are required.
"""
from __future__ import annotations
import csv
import hashlib
import io
import json
import sys
import zipfile
import xml.etree.ElementTree as ET

ATOM = "{http://www.w3.org/2005/Atom}"
META = "{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}"
DATA = "{http://schemas.microsoft.com/ado/2007/08/dataservices}"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


def main(path: str) -> None:
    with open(path, "rb") as handle:
        archive_bytes = handle.read()
    print("artifact_zip_sha256=" + sha256(archive_bytes))
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as zf:
        bad_member = zf.testzip()
        if bad_member:
            fail("ZIP CRC failure: " + bad_member)
        manifest = json.loads(zf.read("manifest.json"))
        summary = json.loads(zf.read("summary.json"))

        for feed, summary_index in (("nominal", 0), ("real", 1)):
            page_records = manifest["feeds"][feed]["pages"]
            raw_observations = {}
            empty_pages = []
            populated_page_numbers = []
            for record in page_records:
                page = int(record["page"])
                member = f"raw/{feed}_page_{page:03d}.xml"
                raw = zf.read(member)
                digest = sha256(raw)
                if len(raw) != int(record["byte_count"]):
                    fail(f"{feed} page {page}: byte_count mismatch")
                if digest != record["sha256"] or digest != record["raw_sha256_recomputed"]:
                    fail(f"{feed} page {page}: SHA-256 mismatch")
                if int(record["http_status"]) != 200:
                    fail(f"{feed} page {page}: HTTP status not 200")
                root = ET.fromstring(raw)
                entries = root.findall(ATOM + "entry")
                if len(entries) != int(record["entry_count"]):
                    fail(f"{feed} page {page}: manifest/XML entry count mismatch")
                if not entries:
                    empty_pages.append(page)
                    continue
                populated_page_numbers.append(page)
                for entry in entries:
                    props = entry.find(ATOM + "content/" + META + "properties")
                    if props is None:
                        fail(f"{feed} page {page}: missing m:properties")
                    observation = {node.tag[len(DATA):]: (node.text or "") for node in list(props)}
                    date = observation.get("NEW_DATE", "")[:10]
                    if not date:
                        fail(f"{feed} page {page}: missing NEW_DATE")
                    if date in raw_observations:
                        fail(f"{feed}: duplicate raw observation date {date}")
                    raw_observations[date] = observation

            if len(empty_pages) != 1 or empty_pages[0] != max(int(x["page"]) for x in page_records):
                fail(f"{feed}: expected exactly one final empty pagination terminator")
            if populated_page_numbers != list(range(len(populated_page_numbers))):
                fail(f"{feed}: non-contiguous page sequence")

            csv_name = f"treasury_{feed}_yield_curve.csv"
            csv_bytes = zf.read(csv_name)
            csv_digest = sha256(csv_bytes)
            expected = summary["feeds"][summary_index]
            if csv_digest != expected["csv_sha256"]:
                fail(f"{feed}: CSV SHA-256 differs from summary")
            rows = list(csv.DictReader(io.StringIO(csv_bytes.decode("utf-8-sig"))))
            by_date = {row["date"]: row for row in rows}
            if len(by_date) != len(rows):
                fail(f"{feed}: duplicate CSV dates")
            if len(rows) != int(expected["row_count"]):
                fail(f"{feed}: CSV row count differs from summary")
            if set(by_date) != set(raw_observations):
                fail(f"{feed}: raw XML and CSV date sets differ")

            mismatches = []
            for date, observation in raw_observations.items():
                row = by_date[date]
                for key, value in observation.items():
                    if key == "NEW_DATE":
                        continue
                    if key not in row or row[key] != value:
                        mismatches.append((date, key, value, row.get(key)))
                        if len(mismatches) >= 5:
                            break
                if mismatches:
                    break
            if mismatches:
                fail(f"{feed}: raw-to-CSV value mismatch: {mismatches}")

            dates = sorted(by_date)
            if dates[0] != expected["first_date"] or dates[-1] != expected["last_date"]:
                fail(f"{feed}: date range differs from summary")
            print(
                f"{feed}: PASS pages={len(page_records)} populated_pages={len(populated_page_numbers)} "
                f"terminator_page={empty_pages[0]} observations={len(rows)} "
                f"first={dates[0]} last={dates[-1]} duplicate_dates=0 "
                f"raw_csv_value_mismatches=0 csv_sha256={csv_digest}"
            )
    print("OVERALL: PASS (Treasury artifact integrity and raw-to-CSV reconciliation only)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python validate_treasury_yield_artifact.py <artifact.zip>")
    main(sys.argv[1])
