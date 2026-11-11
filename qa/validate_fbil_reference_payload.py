#!/usr/bin/env python3
"""Fail-closed validator for an acquired FBIL fetchfiltered raw JSON response.

This tool does not fetch data, fabricate rows, fill dates, or infer OHLC.
It preserves the input bytes and reports their SHA-256 before parsing.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from datetime import date
from pathlib import Path

PAIR_UNITS = {
    "INR / 1 USD": ("USD", 1),
    "INR / 1 GBP": ("GBP", 1),
    "INR / 1 EUR": ("EUR", 1),
    "INR / 100 JPY": ("JPY", 100),
    "INR / 1 AED": ("AED", 1),
    "INR / 10000 IDR": ("IDR", 10000),
}


class ValidationError(ValueError):
    pass


def parse_payload(raw: bytes, start: date, end: date):
    raw_sha256 = hashlib.sha256(raw).hexdigest()
    try:
        decoded = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError("response is not UTF-8") from exc
    try:
        payload = json.loads(decoded)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"response is not valid JSON: {exc}") from exc
    if not isinstance(payload, list):
        raise ValidationError("JSON root must be an array")
    if not payload:
        raise ValidationError("empty response: no observations to validate")

    rows = []
    seen = set()
    unknown_labels = set()
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValidationError(f"record {index}: expected JSON object")
        missing = {"processRunDate", "subProdName", "rate"} - item.keys()
        if missing:
            raise ValidationError(f"record {index}: missing fields {sorted(missing)}")

        label = item["subProdName"]
        if label not in PAIR_UNITS:
            unknown_labels.add(str(label))
            continue

        raw_date = item["processRunDate"]
        if not isinstance(raw_date, str) or len(raw_date) < 10:
            raise ValidationError(f"record {index}: invalid processRunDate")
        try:
            obs_date = date.fromisoformat(raw_date[:10])
        except ValueError as exc:
            raise ValidationError(f"record {index}: invalid date {raw_date!r}") from exc
        if not start <= obs_date <= end:
            raise ValidationError(
                f"record {index}: observation date {obs_date} outside requested range"
            )

        try:
            rate = float(item["rate"])
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"record {index}: rate is not numeric") from exc
        if not math.isfinite(rate) or rate <= 0:
            raise ValidationError(f"record {index}: rate must be finite and positive")

        currency, unit = PAIR_UNITS[label]
        key = (obs_date.isoformat(), currency)
        if key in seen:
            raise ValidationError(f"duplicate date-currency key: {key}")
        seen.add(key)
        rows.append((key[0], currency, format(rate, ".10g"), unit, label))

    if unknown_labels:
        raise ValidationError(f"unrecognized product labels: {sorted(unknown_labels)}")
    if not rows:
        raise ValidationError("no recognized reference-rate observations")
    rows.sort(key=lambda row: (row[0], row[1]))
    return raw_sha256, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", required=True, type=Path, help="unchanged raw JSON response")
    parser.add_argument("--from-date", required=True, type=date.fromisoformat)
    parser.add_argument("--to-date", required=True, type=date.fromisoformat)
    parser.add_argument("--csv-out", required=True, type=Path, help="new CSV path; must not exist")
    args = parser.parse_args()

    if args.from_date > args.to_date:
        parser.error("--from-date must be <= --to-date")
    if not args.raw.is_file():
        parser.error("raw response file does not exist")
    if args.csv_out.exists():
        parser.error("refusing to overwrite existing CSV output")

    raw = args.raw.read_bytes()
    try:
        raw_sha256, rows = parse_payload(raw, args.from_date, args.to_date)
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    args.csv_out.parent.mkdir(parents=True, exist_ok=True)
    with args.csv_out.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "currency", "rate", "unit", "source_product_label"])
        writer.writerows(rows)

    print(json.dumps({
        "status": "PASS",
        "raw_file": str(args.raw),
        "raw_bytes": len(raw),
        "raw_sha256": raw_sha256,
        "requested_from": args.from_date.isoformat(),
        "requested_to": args.to_date.isoformat(),
        "validated_rows": len(rows),
        "unique_date_currency_keys": len({(r[0], r[1]) for r in rows}),
        "csv_file": str(args.csv_out),
        "note": "No gap filling; no OHLC derivation; input bytes unchanged.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
