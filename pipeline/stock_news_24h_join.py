#!/usr/bin/env python3
"""Audit-only join of GDELT discovery results to frozen H+1 candidate cutoffs.

No ranking changes. Missing/blocked source coverage is UNKNOWN. An empty
GDELT query is not proof that no material news exists across all sources.
"""
from pathlib import Path
import json
import pandas as pd

CUTS = Path("outputs/prospective/target5_h1_selector_experiment_picks.csv")
NEWS = Path("data/raw/stock_news_events.csv")
COVERAGE = Path("data/raw/stock_news_coverage.csv")
OUT = Path("outputs/news_24h")
TZ = "Asia/Kolkata"
NEWS_COLUMNS = {
    "SYMBOL", "PUBLISHED_AT", "PUBLISHER", "HEADLINE", "CANONICAL_URL",
    "SOURCE_TYPE", "VERIFICATION_STATUS",
}
COVERAGE_COLUMNS = {"SYMBOL", "WINDOW_START", "WINDOW_END", "COVERAGE_STATUS"}


def write_report(report):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "stock_news_24h_readiness.json").write_text(
        json.dumps(report, indent=2, allow_nan=False), encoding="utf-8"
    )


def main():
    missing_files = [str(p) for p in (CUTS, NEWS, COVERAGE) if not p.exists()]
    if missing_files:
        report = {
            "status": "BLOCKED_MISSING_INPUTS",
            "research_status": "BLOCKED",
            "missing_files": missing_files,
            "news_window_hours": 24,
            "no_news_semantics": "UNKNOWN unless source query coverage is COMPLETE; even then only no match in the observed source/query",
            "production_selector_changed": False,
            "ranking_score_changed": False,
            "pressure_fade_changed": False,
        }
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0

    cuts = pd.read_csv(CUTS)
    news = pd.read_csv(NEWS)
    coverage = pd.read_csv(COVERAGE)
    missing_news_cols = sorted(NEWS_COLUMNS - set(news.columns))
    missing_cov_cols = sorted(COVERAGE_COLUMNS - set(coverage.columns))
    if not {"CUT_OFF", "SYMBOL"}.issubset(cuts.columns):
        report = {"status": "BLOCKED_BAD_CANDIDATE_SCHEMA", "research_status": "BLOCKED",
                  "required_cutoff_columns": ["CUT_OFF", "SYMBOL"],
                  "production_selector_changed": False}
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0
    if missing_news_cols or missing_cov_cols:
        report = {
            "status": "BLOCKED_BAD_NEWS_SCHEMA",
            "research_status": "BLOCKED",
            "missing_news_columns": missing_news_cols,
            "missing_coverage_columns": missing_cov_cols,
            "production_selector_changed": False,
        }
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0

    cuts = cuts[["CUT_OFF", "SYMBOL"]].dropna().drop_duplicates().copy()
    cuts["SYMBOL"] = cuts["SYMBOL"].astype(str).str.upper().str.strip()
    cuts["CUT_OFF"] = pd.to_datetime(cuts["CUT_OFF"], errors="coerce")
    cuts = cuts.dropna(subset=["CUT_OFF"])
    cuts["CUTOFF_AT"] = cuts["CUT_OFF"].dt.normalize().dt.tz_localize(TZ) + pd.Timedelta(hours=15, minutes=30)

    news["SYMBOL"] = news["SYMBOL"].astype(str).str.upper().str.strip()
    news["PUBLISHED_AT"] = pd.to_datetime(news["PUBLISHED_AT"], errors="coerce", utc=True)
    news["PUBLISHED_AT"] = news["PUBLISHED_AT"].dt.tz_convert(TZ)
    news = news.dropna(subset=["PUBLISHED_AT", "SYMBOL"])
    news = news.drop_duplicates(["SYMBOL", "PUBLISHED_AT", "CANONICAL_URL"])

    coverage["SYMBOL"] = coverage["SYMBOL"].astype(str).str.upper().str.strip()
    coverage["WINDOW_START"] = pd.to_datetime(coverage["WINDOW_START"], errors="coerce", utc=True).dt.tz_convert(TZ)
    coverage["WINDOW_END"] = pd.to_datetime(coverage["WINDOW_END"], errors="coerce", utc=True).dt.tz_convert(TZ)
    coverage["COVERAGE_STATUS"] = coverage["COVERAGE_STATUS"].astype(str).str.upper().str.strip()

    rows = []
    for row in cuts.itertuples(index=False):
        cutoff = row.CUTOFF_AT
        start = cutoff - pd.Timedelta(hours=24)
        cov = coverage[
            (coverage["SYMBOL"] == row.SYMBOL)
            & (coverage["WINDOW_START"] <= start)
            & (coverage["WINDOW_END"] >= cutoff)
            & (coverage["COVERAGE_STATUS"] == "COMPLETE")
        ]
        hits = news[
            (news["SYMBOL"] == row.SYMBOL)
            & (news["PUBLISHED_AT"] > start)
            & (news["PUBLISHED_AT"] < cutoff)
        ].copy()
        verified_count = int(hits["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()) if len(hits) else 0
        if len(cov) == 0:
            status = "UNKNOWN_COVERAGE"
        elif len(hits) and verified_count == len(hits):
            status = "VERIFIED_NEWS_PRESENT"
        elif len(hits):
            status = "UNVERIFIED_NEWS_PRESENT"
        else:
            status = "NO_MATCH_IN_GDELT_QUERY_WINDOW"
        rows.append({
            "CUT_OFF": row.CUT_OFF.date().isoformat(),
            "SYMBOL": row.SYMBOL,
            "CUTOFF_AT": cutoff.isoformat(),
            "WINDOW_START": start.isoformat(),
            "NEWS_ITEMS_24H": int(len(hits)),
            "VERIFIED_ITEMS_24H": verified_count,
            "NEWS_STATUS": status,
            "LATEST_PUBLISHED_AT": hits["PUBLISHED_AT"].max().isoformat() if len(hits) else "",
        })
    result = pd.DataFrame(rows)
    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT / "stock_news_24h_cutoff_join.csv", index=False)
    unknown = int(result["NEWS_STATUS"].eq("UNKNOWN_COVERAGE").sum())
    unverified = int(result["NEWS_STATUS"].eq("UNVERIFIED_NEWS_PRESENT").sum())
    verified = int(result["NEWS_STATUS"].eq("VERIFIED_NEWS_PRESENT").sum())
    no_match = int(result["NEWS_STATUS"].eq("NO_MATCH_IN_GDELT_QUERY_WINDOW").sum())
    all_coverage = len(result) > 0 and unknown == 0
    ready = all_coverage and verified > 0 and unverified == 0
    report = {
        "status": "JOIN_BUILT_AUDIT_ONLY",
        "research_status": "READY_FOR_PAIRED_ABLATION" if ready else "BLOCKED_VERIFICATION_OR_COVERAGE",
        "cutoff_symbol_rows": int(len(result)),
        "news_window_hours": 24,
        "news_rows_loaded": int(len(news)),
        "coverage_rows_loaded": int(len(coverage)),
        "coverage_unknown_rows": unknown,
        "unverified_news_rows": unverified,
        "verified_news_rows": verified,
        "no_match_in_gdelt_query_window_rows": no_match,
        "warning": "GDELT symbol-query matches are discovery leads only. Do not treat a zero-result query as no material news across all sources. Paired ablation remains blocked until relevant stories are independently verified and coverage gaps resolved.",
        "production_selector_changed": False,
        "ranking_score_changed": False,
        "pressure_fade_changed": False,
    }
    write_report(report)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
