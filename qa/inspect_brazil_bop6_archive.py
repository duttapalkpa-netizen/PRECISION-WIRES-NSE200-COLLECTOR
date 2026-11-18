#!/usr/bin/env python3
"""Inventory and integrity-check the official BCB BPM6 monthly ZIP.

This first-stage archive audit deliberately does not interpret workbook cells.
It records the exact downloaded bytes and safe ZIP member inventory so a later
parser can be written against the observed source schema, not guessed columns.
"""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path, PurePosixPath


def inspect_archive(path):
    p = Path(path)
    raw = p.read_bytes()
    if not raw:
        raise ValueError("Monthly BPM6 archive is empty")
    digest = hashlib.sha256(raw).hexdigest()
    if not zipfile.is_zipfile(p):
        raise ValueError("Official monthly BPM6 payload is not a ZIP archive")
    with zipfile.ZipFile(p) as zf:
        bad = zf.testzip()
        if bad is not None:
            raise ValueError(f"ZIP CRC failure in member: {bad}")
        members = []
        for info in zf.infolist():
            name = info.filename
            pp = PurePosixPath(name)
            if pp.is_absolute() or ".." in pp.parts or "\\" in name:
                raise ValueError(f"Unsafe ZIP member path: {name}")
            if info.is_dir():
                continue
            suffix = pp.suffix.lower()
            members.append({
                "name": name,
                "uncompressed_bytes": info.file_size,
                "compressed_bytes": info.compress_size,
                "crc32": f"{info.CRC:08x}",
                "suffix": suffix,
                "candidate_data_file": suffix in {".xls", ".xlsx", ".csv", ".ods", ".txt"}
            })
        if not members:
            raise ValueError("ZIP archive contains no files")
    return {
        "schema_version": 1,
        "status": "PASS_ZIP_INTEGRITY_AND_INVENTORY_ONLY",
        "scope": "Archive integrity and member inventory only; no workbook cell interpretation or series reconciliation.",
        "source_url": "https://www.bcb.gov.br/ftp/notaecon/balpaym.zip",
        "archive": {
            "filename": p.name,
            "raw_bytes": len(raw),
            "sha256": digest,
            "member_count": len(members),
            "data_candidate_count": sum(x["candidate_data_file"] for x in members)
        },
        "members": members,
        "next_gate": "Inspect actual workbook sheets, headers, labels, units, periods and portfolio investment rows before comparing any values."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    try:
        report = inspect_archive(args.zip)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        report = {"schema_version": 1, "status": "FAIL", "error": str(exc),
                  "admission": "NOT_AUTHORIZED"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS_ZIP_INTEGRITY_AND_INVENTORY_ONLY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
