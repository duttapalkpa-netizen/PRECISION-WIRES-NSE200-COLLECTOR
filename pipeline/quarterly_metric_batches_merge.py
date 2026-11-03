#!/usr/bin/env python3
"""Merge bounded NSE quarterly-metric batches and reapply revision policy globally.

Evidence-only. Never changes the production selector, RANKING_SCORE,
+1 PRESSURE_FADE, or the 672 diagnostic definitions.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
import pandas as pd

ROOT = Path(".")
B1 = ROOT / "inputs/batch1/data/raw/quarterly_financial_metrics.csv"
B2 = ROOT / "inputs/batch2/data/raw/quarterly_financial_metrics.csv"
DISC = ROOT / "inputs/batch1/data/raw/quarterly_results_disclosures.csv"
EVIDENCE = ROOT / "data/raw/quarterly_filing_evidence"
OUT = ROOT / "outputs/quarterly_results"
CANONICAL = ROOT / "data/raw/quarterly_financial_metrics.csv"
FEATURES = OUT / "quarterly_financial_features.csv"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
VALID = {"SOURCE_LINKED_XBRL_FACTS", "SOURCE_LINKED_PDF_TABLE_FACTS"}

def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def restore_prior_superseded(rows):
    d = rows.copy()
    mask = d["EXTRACTION_STATUS"].eq("SUPERSEDED_BY_LATER_DISCLOSURE")
    for idx in d.index[mask]:
        row = d.loc[idx]
        metrics = all(str(row.get(k, "")).strip() for k in ("REVENUE", "PAT", "EPS"))
        provenance = bool(str(row.get("SOURCE_URL", "")).strip()) and bool(SHA_RE.fullmatch(str(row.get("SOURCE_SHA256", ""))))
        timestamp = pd.notna(pd.to_datetime(row.get("DISCLOSED_AT", ""), errors="coerce", utc=True))
        if metrics and provenance and timestamp:
            ctype = str(row.get("SOURCE_CONTENT_TYPE", "")).lower()
            d.at[idx, "EXTRACTION_STATUS"] = "SOURCE_LINKED_PDF_TABLE_FACTS" if "pdf" in ctype else "SOURCE_LINKED_XBRL_FACTS"
        else:
            d.at[idx, "EXTRACTION_STATUS"] = "BLOCKED_SUPERSEDED_ROW_WITH_INCOMPLETE_EVIDENCE"
            d.loc[idx, ["REVENUE", "PAT", "EPS"]] = ""
    return d

def apply_global_revision_policy(rows):
    d = restore_prior_superseded(rows)
    d["_DISCLOSED_SORT"] = pd.to_datetime(d["DISCLOSED_AT"], errors="coerce", utc=True)
    valid = d["EXTRACTION_STATUS"].isin(VALID)
    for _, group in d.loc[valid].groupby(["SYMBOL", "PERIOD_END", "BASIS"], dropna=False):
        if len(group) < 2:
            continue
        latest = group["_DISCLOSED_SORT"].max()
        latest_rows = group[group["_DISCLOSED_SORT"].eq(latest)]
        if len(latest_rows) == 1 and pd.notna(latest):
            older = group.index.difference(latest_rows.index)
            d.loc[older, "EXTRACTION_STATUS"] = "SUPERSEDED_BY_LATER_DISCLOSURE"
        else:
            d.loc[group.index, "EXTRACTION_STATUS"] = "BLOCKED_AMBIGUOUS_LATEST_PERIOD_BASIS"
            d.loc[group.index, ["REVENUE", "PAT", "EPS"]] = ""
    return d.drop(columns=["_DISCLOSED_SORT"])

def validate_evidence(rows):
    checked = 0
    missing = []
    mismatched = []
    for idx, row in rows.iterrows():
        digest = str(row.get("SOURCE_SHA256", "")).strip().lower()
        if not digest:
            continue
        checked += 1
        path = ROOT / str(row.get("EVIDENCE_PATH", ""))
        if not path.is_file():
            missing.append({"row": int(idx), "path": str(path), "symbol": row.get("SYMBOL", "")})
            continue
        actual = sha256_file(path)
        if actual != digest:
            mismatched.append({"row": int(idx), "path": str(path), "expected": digest, "actual": actual})
    if missing or mismatched:
        raise ValueError(json.dumps({"missing_evidence": missing[:20], "hash_mismatches": mismatched[:20]}))
    return checked

def main():
    for p in (B1, B2, DISC):
        if not p.is_file():
            raise SystemExit(f"BLOCKED_MISSING_INPUT: {p}")
    b1 = pd.read_csv(B1, dtype=str).fillna("")
    b2 = pd.read_csv(B2, dtype=str).fillna("")
    disclosures = pd.read_csv(DISC, dtype=str).fillna("")
    if len(b1) != 1000 or len(b2) != 988:
        raise SystemExit(f"BLOCKED_BATCH_ROW_COUNTS: batch1={len(b1)} batch2={len(b2)}")
    if int(disclosures.get("EVENT_KIND", pd.Series(dtype=str)).eq("RESULT_DISCLOSURE").sum()) != 1988:
        raise SystemExit("BLOCKED_SOURCE_DISCLOSURE_COUNT_NOT_1988")
    if list(b1.columns) != list(b2.columns):
        raise SystemExit("BLOCKED_BATCH_SCHEMA_MISMATCH")
    rows = pd.concat([b1, b2], ignore_index=True)
    if len(rows) != 1988:
        raise SystemExit("BLOCKED_MERGED_LEDGER_ROW_COUNT")
    if rows["SOURCE_URL"].duplicated().any():
        dup = rows.loc[rows["SOURCE_URL"].duplicated(keep=False), ["SYMBOL", "SOURCE_URL"]].to_dict("records")
        raise SystemExit("BLOCKED_DUPLICATE_SOURCE_URLS: " + json.dumps(dup[:20]))
    evidence_checked = validate_evidence(rows)
    rows = apply_global_revision_policy(rows)
    CANONICAL.parent.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    rows.to_csv(CANONICAL, index=False)
    sys.path.insert(0, str(ROOT.resolve()))
    from pipeline.quarterly_results_research import build_financial_features
    features, feature_report = build_financial_features(CANONICAL)
    features.to_csv(FEATURES, index=False)
    counts = rows["EXTRACTION_STATUS"].value_counts().to_dict()
    if counts.get("BLOCKED_AMBIGUOUS_LATEST_PERIOD_BASIS", 0):
        raise SystemExit("BLOCKED_AMBIGUOUS_LATEST_PERIOD_BASIS")
    report = {
        "status": "MERGED_WITH_EXPLICIT_BLOCKERS",
        "batch1_rows": len(b1),
        "batch2_rows": len(b2),
        "source_result_disclosures": int(len(disclosures[disclosures["EVENT_KIND"].eq("RESULT_DISCLOSURE")])),
        "merged_ledger_rows": len(rows),
        "status_counts_after_global_revision_reconciliation": counts,
        "source_evidence_files_sha256_verified": evidence_checked,
        "unique_source_urls": int(rows["SOURCE_URL"].nunique()),
        "feature_report": feature_report,
        "feature_rows": int(len(features)),
        "policy": "Prior superseded statuses were restored only when source URL, SHA-256, disclosure timestamp and all three metric facts were present; global latest-revision policy then re-applied across both batches. Blocked rows remain blocked.",
        "production_invariants": {
            "production_selector_changed": False,
            "ranking_score_changed": False,
            "pressure_fade_changed": False,
            "diagnostics_672_changed": False
        },
        "input_files": {
            "batch1_sha256": sha256_file(B1),
            "batch2_sha256": sha256_file(B2),
            "source_disclosures_sha256": sha256_file(DISC)
        }
    }
    (OUT / "quarterly_metric_batches_reconciliation.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
