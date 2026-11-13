"""Fail-closed, byte-preserving intake audit for exchange security-master files.

This module audits uploaded/local bytes only. It does not authenticate the publisher,
infer a file vintage, or assign issuer/industry membership.
"""
from __future__ import annotations
import argparse
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path

ISIN_HEADERS = {"isin", "isin code", "isin_code", "isin no", "isin number"}

def inspect_security_master(path: str | Path) -> dict:
    p = Path(path)
    raw = p.read_bytes()
    if not raw:
        raise ValueError("empty input: no evidence to inspect")
    digest = hashlib.sha256(raw).hexdigest()
    is_gzip = raw[:2] == b"\x1f\x8b"
    if p.suffix.lower() == ".gz" and not is_gzip:
        raise ValueError(".gz extension without gzip magic bytes")
    try:
        payload = gzip.decompress(raw) if is_gzip else raw
    except (OSError, EOFError) as exc:
        raise ValueError("gzip integrity/decompression failure") from exc
    if not payload:
        raise ValueError("decompressed payload is empty")
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("not valid UTF-8/UTF-8-BOM; encoding must be established separately") from exc
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",|;\t")
    except csv.Error as exc:
        raise ValueError("CSV delimiter is ambiguous; no parser assumption permitted") from exc
    reader = csv.reader(io.StringIO(text, newline=""), dialect)
    try:
        header = next(reader)
    except StopIteration:
        raise ValueError("missing header record")
    if len(header) < 2 or any(not h.strip() for h in header):
        raise ValueError("header is blank or structurally implausible")
    normalized = [h.strip().lower() for h in header]
    if len(set(normalized)) != len(normalized):
        raise ValueError("duplicate header names after normalization")
    isin_indices = [i for i, h in enumerate(normalized) if h in ISIN_HEADERS]
    isin_values, row_width_errors, blank_rows = [], 0, 0
    data_rows = 0
    for row in reader:
        if not row or all(not cell.strip() for cell in row):
            blank_rows += 1
            continue
        data_rows += 1
        if len(row) != len(header):
            row_width_errors += 1
        for idx in isin_indices:
            if idx < len(row) and row[idx].strip():
                isin_values.append(row[idx].strip().upper())
    duplicates = len(isin_values) - len(set(isin_values))
    return {
        "file_name": p.name,
        "raw_byte_size": len(raw),
        "raw_sha256": digest,
        "gzip_by_magic_bytes": is_gzip,
        "decompressed_byte_size": len(payload),
        "encoding": "utf-8-sig",
        "delimiter": dialect.delimiter,
        "header": header,
        "data_row_count": data_rows,
        "blank_row_count": blank_rows,
        "row_width_error_count": row_width_errors,
        "isin_column_indices": isin_indices,
        "isin_nonblank_count": len(isin_values),
        "isin_unique_count": len(set(isin_values)),
        "duplicate_isin_occurrence_count": duplicates,
        "acceptance": "PASS_STRUCTURAL_ONLY" if row_width_errors == 0 else "FAIL_ROW_WIDTH",
        "limitations": [
            "file publisher and official provenance are not authenticated",
            "file vintage/publication time are not inferred from filename or upload time",
            "header semantics and exchange-specific schema are not certified by this generic audit",
            "ISIN is a security-level identifier; issuer aggregation and industry membership are not inferred",
        ],
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = inspect_security_master(args.file)
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["acceptance"] == "PASS_STRUCTURAL_ONLY" else 2

if __name__ == "__main__":
    raise SystemExit(main())
