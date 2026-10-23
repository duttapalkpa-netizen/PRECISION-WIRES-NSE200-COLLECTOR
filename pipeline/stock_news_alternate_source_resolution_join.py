#!/usr/bin/env python3
"""Audited join of independently verified publisher resolutions to discovery evidence.

A timestamp is aligned only when the original and publisher-native timestamps
parse and differ by <=24 hours. RSS/discovery copies are not independent proof.
This audit never rewrites the source news ledger or declares research READY.
"""
from pathlib import Path
import json
import pandas as pd

CANDIDATES = Path("artifact/outputs/news_24h/stock_news_alternate_source_candidates.csv")
VERIFIED = Path("outputs/news_24h/alternate_source_verification_results.csv")
OUT = Path("outputs/news_24h/alternate_source_resolution_join.json")
CSV = Path("outputs/news_24h/alternate_source_resolution_join.csv")
KEYS = ["SOURCE_ROW_INDEX", "CUT_OFF", "SYMBOL", "ORIGINAL_PUBLISHED_AT", "ORIGINAL_HEADLINE", "ORIGINAL_URL", "ALTERNATE_ARTICLE_URL"]

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for p in (CANDIDATES, VERIFIED):
        if not p.is_file():
            report = {"status": "BLOCKED_MISSING_INPUT", "missing": str(p), "joined_rows": 0, "research_status": "BLOCKED"}
            OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
            print(json.dumps(report))
            raise SystemExit(2)
    c = pd.read_csv(CANDIDATES, dtype=str).fillna("")
    v = pd.read_csv(VERIFIED, dtype=str).fillna("")
    missing = [k for k in KEYS if k not in c.columns or k not in v.columns]
    if missing:
        report = {"status": "BLOCKED_BAD_SCHEMA", "missing_columns": missing, "joined_rows": 0, "research_status": "BLOCKED"}
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        raise SystemExit(2)
    if "PUBLISHER_PUBLISHED_AT" not in v.columns:
        report = {"status": "BLOCKED_MISSING_PUBLISHER_TIMESTAMP_FIELD", "missing_columns": ["PUBLISHER_PUBLISHED_AT"], "joined_rows": 0, "research_status": "BLOCKED"}
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        raise SystemExit(2)
    j = c.merge(v, on=KEYS, how="left", suffixes=("_DISCOVERY", "_VERIFY"), validate="one_to_one", indicator=True)
    j["RESOLUTION_JOIN_STATUS"] = "UNRESOLVED"
    is_verified = j["_merge"].eq("both") & j["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED")
    orig = pd.to_datetime(j["ORIGINAL_PUBLISHED_AT"], utc=True, errors="coerce", format="mixed")
    publisher = pd.to_datetime(j["PUBLISHER_PUBLISHED_AT"], utc=True, errors="coerce", format="mixed")
    rss = pd.to_datetime(j.get("ALTERNATE_PUBLISHED_AT_DISCOVERY", pd.Series("", index=j.index)), utc=True, errors="coerce", format="mixed")
    diff = (orig - publisher).abs().dt.total_seconds() / 3600
    rss_diff = (rss - publisher).abs().dt.total_seconds() / 3600
    time_ok = orig.notna() & publisher.notna() & (diff <= 24)
    j.loc[is_verified & time_ok, "RESOLUTION_JOIN_STATUS"] = "SOURCE_URL_RESOLVED_TIME_ALIGNED"
    j.loc[is_verified & ~time_ok, "RESOLUTION_JOIN_STATUS"] = "VERIFIED_PAGE_BUT_TIMESTAMP_UNCONFIRMED"
    j["TIMESTAMP_DIFFERENCE_HOURS"] = diff
    j["RSS_VS_PUBLISHER_TIMESTAMP_DIFFERENCE_HOURS"] = rss_diff
    cols = [x for x in ["SOURCE_ROW_INDEX", "CUT_OFF", "SYMBOL", "ORIGINAL_PUBLISHED_AT", "ALTERNATE_PUBLISHED_AT_DISCOVERY", "PUBLISHER_PUBLISHED_AT", "TIMESTAMP_DIFFERENCE_HOURS", "RSS_VS_PUBLISHER_TIMESTAMP_DIFFERENCE_HOURS", "ORIGINAL_PUBLISHER", "ORIGINAL_HEADLINE", "ORIGINAL_URL", "ALTERNATE_PUBLISHER_DISCOVERY", "ALTERNATE_ARTICLE_URL", "VERIFICATION_STATUS", "RESOLVED_URL", "PUBLISHER_PAGE_TITLE", "HEADLINE_TOKEN_OVERLAP", "RESOLUTION_JOIN_STATUS"] if x in j.columns]
    out = j[cols].copy()
    out.to_csv(CSV, index=False)
    resolved = int(out["RESOLUTION_JOIN_STATUS"].eq("SOURCE_URL_RESOLVED_TIME_ALIGNED").sum())
    time_uncertain = int(out["RESOLUTION_JOIN_STATUS"].eq("VERIFIED_PAGE_BUT_TIMESTAMP_UNCONFIRMED").sum())
    report = {"status": "PASS_RESOLUTION_JOIN_AUDIT_ONLY" if resolved > 0 else "BLOCKED_NO_TIME_ALIGNED_RESOLUTIONS", "candidate_rows": len(c), "verified_candidate_rows": int(j["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()), "source_url_resolved_time_aligned_rows": resolved, "verified_page_timestamp_unconfirmed_rows": time_uncertain, "timestamp_rule": "Original publication timestamp and independently extracted publisher-native publication timestamp must both parse and differ by <=24h; RSS timestamps are diagnostic only and cannot establish alignment.", "join_keys": KEYS, "output_csv": str(CSV), "source_ledger_modified": False, "research_status": "BLOCKED", "reason": "This audit joins verified leads to discovery evidence only. It does not update original news rows; source-ledger reconciliation and full readiness checks remain required.", "rows": out.to_dict("records")}
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print("ALTERNATE_SOURCE_RESOLUTION_JOIN=" + json.dumps(report, sort_keys=True, ensure_ascii=False))
    if resolved == 0:
        raise SystemExit(1)
if __name__ == "__main__":
    main()
