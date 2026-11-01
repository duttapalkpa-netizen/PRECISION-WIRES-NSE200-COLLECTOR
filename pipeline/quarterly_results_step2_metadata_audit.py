#!/usr/bin/env python3
"""Independent Step 2 five-field metadata acceptance audit.

Consumes the complete raw NSE disclosure response and normalized row-level
validation output. Does not download or parse XBRL/PDF attachments.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED = {
    "SYMBOL": "SYMBOL_VALID",
    "ISIN": "ISIN_VALID",
    "SOURCE_URL": "SOURCE_URL_VALID",
    "PUBLICATION_TIMESTAMP": "PUBLICATION_TIMESTAMP_VALID",
    "REPORTING_PERIOD": "REPORTING_PERIOD_VALID",
}

def find_payload(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("payload"), (dict, list)):
            return obj["payload"]
        return obj
    return obj

def find_rows(obj):
    if isinstance(obj, list) and (not obj or isinstance(obj[0], dict)):
        return obj
    if isinstance(obj, dict):
        for key in ("data", "rows", "results", "financialResults"):
            value = obj.get(key)
            if isinstance(value, list) and (not value or isinstance(value[0], dict)):
                return value
        for value in obj.values():
            if isinstance(value, (dict, list)):
                found = find_rows(value)
                if found:
                    return found
    return []

def find_pagination(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("_audit_pagination"), dict):
            return obj["_audit_pagination"]
        for value in obj.values():
            if isinstance(value, (dict, list)):
                found = find_pagination(value)
                if found:
                    return found
    return {}

def truth(value):
    return str(value).strip().lower() in {"true", "1", "yes"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="data/raw/quarterly_results_raw_responses/result_disclosure.json")
    ap.add_argument("--validation", default="outputs/quarterly_results/source_validation_report.csv")
    ap.add_argument("--out", default="outputs/quarterly_results")
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    raw_envelope = json.loads(Path(args.raw).read_text(encoding="utf-8"))
    payload = find_payload(raw_envelope)
    raw_rows = find_rows(payload)
    pagination = find_pagination(payload)
    with Path(args.validation).open(newline="", encoding="utf-8") as fh:
        all_rows = list(csv.DictReader(fh))
    rows = [r for r in all_rows if r.get("EVENT_KIND") == "RESULT_DISCLOSURE"]
    # Preserve one-to-one raw/normalized accounting. A mismatch is a hard blocker.
    reported_total = pagination.get("reported_total_count", pagination.get("total_count"))
    try: reported_total = int(reported_total)
    except (TypeError, ValueError): reported_total = None
    expected = reported_total if reported_total is not None else len(raw_rows)
    hashes = [r.get("SOURCE_RECORD_SHA256", "").strip() for r in rows]
    hash_counts = Counter(h for h in hashes if h)
    duplicate_hashes = {h for h, n in hash_counts.items() if n > 1}
    # Conflicting identity mappings are ambiguous; never select one arbitrarily.
    identity_isins = defaultdict(set)
    for r in rows:
        symbol, period, isin = (r.get("SYMBOL","").strip(), r.get("REPORTING_PERIOD","").strip(),
                               r.get("ISIN","").strip())
        if symbol and period and isin:
            identity_isins[(symbol, period)].add(isin)
    conflicting_identities = {k for k,v in identity_isins.items() if len(v) > 1}
    missing, ambiguous, normalized = [], [], []
    field_counts = {k: {"valid": 0, "missing_or_invalid": 0} for k in REQUIRED}
    for index, r in enumerate(rows, 1):
        invalid = [field for field, flag in REQUIRED.items() if not truth(r.get(flag, ""))]
        for field, flag in REQUIRED.items():
            if truth(r.get(flag, "")): field_counts[field]["valid"] += 1
            else: field_counts[field]["missing_or_invalid"] += 1
        reasons = []
        digest = r.get("SOURCE_RECORD_SHA256", "").strip()
        if digest and digest in duplicate_hashes: reasons.append("DUPLICATE_SOURCE_RECORD_HASH")
        key = (r.get("SYMBOL","").strip(), r.get("REPORTING_PERIOD","").strip())
        if key in conflicting_identities: reasons.append("CONFLICTING_ISIN_FOR_SYMBOL_PERIOD")
        record = {**r, "AUDIT_ROW_NUMBER": index, "INVALID_FIELDS": ";".join(invalid),
                  "AMBIGUITY_REASONS": ";".join(reasons)}
        normalized.append(record)
        if invalid: missing.append(record)
        if reasons: ambiguous.append(record)
    pagination_complete = pagination.get("complete") is True
    count_match = len(raw_rows) == expected == len(rows)
    no_duplicate_hashes = not duplicate_hashes
    no_ambiguous = not ambiguous
    no_missing = not missing
    acceptance = {
        "raw_rows_equal_reported_total": count_match,
        "normalized_rows_equal_raw_rows": len(rows) == len(raw_rows),
        "pagination_complete": pagination_complete,
        "all_five_fields_valid_for_every_row": no_missing,
        "no_ambiguous_records": no_ambiguous,
        "no_duplicate_source_record_hashes": no_duplicate_hashes,
    }
    passed = all(acceptance.values()) and len(rows) == 1767
    report = {
        "status": "PASS" if passed else "BLOCKED",
        "acceptance_status": "PASS" if passed else "BLOCKED",
        "scope": "all RESULT_DISCLOSURE rows; independent of XBRL/PDF attachment extraction",
        "required_fields": list(REQUIRED),
        "raw_rows": len(raw_rows), "reported_total_count": reported_total,
        "normalized_disclosure_rows": len(rows), "unique_source_record_hashes": len(set(hashes)),
        "field_coverage": field_counts,
        "missing_record_count": len(missing), "ambiguous_record_count": len(ambiguous),
        "pagination": pagination, "acceptance_tests": acceptance,
        "no_timestamp_inference": True,
        "revision_timestamp_policy": "Only explicit source-labelled revision records may use revised_Date as that revision event publication timestamp; creation_Date is never substituted.",
        "note": "PASS requires exactly 1,767 source rows and every acceptance test true. Unknown or unverified values remain blockers."
    }
    (out/"step2_metadata_coverage.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    for name, data in (("step2_all_record_field_audit.csv", normalized),
                       ("step2_missing_records.csv", missing),
                       ("step2_ambiguous_records.csv", ambiguous)):
        cols = sorted({k for item in data for k in item})
        with (out/name).open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=cols or ["STATUS"])
            writer.writeheader(); writer.writerows(data)
    print("STEP2_METADATA_ACCEPTANCE=" + json.dumps(report, sort_keys=True))
    return 0 if passed else 2

if __name__ == "__main__":
    raise SystemExit(main())
