#!/usr/bin/env python3
"""Audit-only join of GDELT discovery results to frozen H+1 candidate cutoffs.

No ranking changes. Missing/blocked source coverage is UNKNOWN. An empty
GDELT query is not proof that no material news exists across all sources.
"""
from pathlib import Path
from urllib.parse import urlparse
import json
import pandas as pd

CUTS = Path("outputs/prospective/target5_h1_selector_experiment_picks.csv")
NEWS = Path("data/raw/stock_news_events.csv")
COVERAGE = Path("data/raw/stock_news_coverage.csv")
OUT = Path("outputs/news_24h")
TZ = "Asia/Kolkata"
NEWS_COLUMNS = {
    "CUT_OFF", "SYMBOL", "PUBLISHED_AT", "PUBLISHER", "HEADLINE",
    "CANONICAL_URL", "SOURCE_TYPE", "VERIFICATION_STATUS",
}
COVERAGE_COLUMNS = {"CUT_OFF", "SYMBOL", "WINDOW_START", "WINDOW_END",
                    "COVERAGE_STATUS", "SOURCE_URL"}


def valid_http_url(value):
    try:
        parsed = urlparse(str(value or "").strip())
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except Exception:
        return False


def write_report(report):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "stock_news_24h_readiness.json").write_text(
        json.dumps(report, indent=2, allow_nan=False), encoding="utf-8"
    )


def main():
    missing_files = [str(p) for p in (CUTS, NEWS, COVERAGE) if not p.exists()]
    if missing_files:
        report = {
            "status": "BLOCKED_MISSING_INPUTS", "research_status": "BLOCKED",
            "missing_files": missing_files, "news_window_hours": 24,
            "no_news_semantics": "UNKNOWN unless source query coverage is COMPLETE; even then only no match in the observed source/query",
            "production_selector_changed": False, "ranking_score_changed": False,
            "pressure_fade_changed": False,
        }
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0

    cuts = pd.read_csv(CUTS, dtype={"SYMBOL": str})
    news = pd.read_csv(NEWS, dtype={"SYMBOL": str, "CUT_OFF": str, "CANONICAL_URL": str})
    coverage = pd.read_csv(COVERAGE, dtype={"SYMBOL": str, "CUT_OFF": str, "SOURCE_URL": str})
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
        report = {"status": "BLOCKED_BAD_NEWS_SCHEMA", "research_status": "BLOCKED",
                  "missing_news_columns": missing_news_cols,
                  "missing_coverage_columns": missing_cov_cols,
                  "production_selector_changed": False}
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0

    cuts = cuts[["CUT_OFF", "SYMBOL"]].dropna().drop_duplicates().copy()
    cuts["SYMBOL"] = cuts["SYMBOL"].astype(str).str.upper().str.strip()
    cuts["CUT_OFF"] = pd.to_datetime(cuts["CUT_OFF"], errors="coerce").dt.date.astype("string")
    cuts = cuts.dropna(subset=["CUT_OFF"])
    cuts = cuts[cuts["SYMBOL"].ne("")]
    cuts["CUTOFF_AT"] = pd.to_datetime(cuts["CUT_OFF"], errors="coerce").dt.tz_localize(TZ) + pd.Timedelta(hours=15, minutes=30)

    news["SYMBOL"] = news["SYMBOL"].astype(str).str.upper().str.strip()
    news["CUT_OFF"] = pd.to_datetime(news["CUT_OFF"], errors="coerce").dt.date.astype("string")
    news["PUBLISHED_AT"] = pd.to_datetime(news["PUBLISHED_AT"], errors="coerce", utc=True).dt.tz_convert(TZ)
    news["URL_VALID"] = news["CANONICAL_URL"].map(valid_http_url)
    news = news.dropna(subset=["PUBLISHED_AT", "SYMBOL", "CUT_OFF"])
    news = news.drop_duplicates(["SYMBOL", "CUT_OFF", "PUBLISHED_AT", "CANONICAL_URL"])

    coverage["SYMBOL"] = coverage["SYMBOL"].astype(str).str.upper().str.strip()
    coverage["CUT_OFF"] = pd.to_datetime(coverage["CUT_OFF"], errors="coerce").dt.date.astype("string")
    coverage["WINDOW_START"] = pd.to_datetime(coverage["WINDOW_START"], errors="coerce", utc=True).dt.tz_convert(TZ)
    coverage["WINDOW_END"] = pd.to_datetime(coverage["WINDOW_END"], errors="coerce", utc=True).dt.tz_convert(TZ)
    coverage["COVERAGE_STATUS"] = coverage["COVERAGE_STATUS"].astype(str).str.upper().str.strip()
    coverage["SOURCE_URL_VALID"] = coverage["SOURCE_URL"].map(valid_http_url)

    rows = []
    for row in cuts.itertuples(index=False):
        cutoff = row.CUTOFF_AT
        start = cutoff - pd.Timedelta(hours=24)
        pair_cov = coverage[(coverage["SYMBOL"] == row.SYMBOL) & (coverage["CUT_OFF"] == row.CUT_OFF)]
        cov = pair_cov[
            (pair_cov["WINDOW_START"] <= start) & (pair_cov["WINDOW_END"] >= cutoff)
            & (pair_cov["COVERAGE_STATUS"] == "COMPLETE")
            & pair_cov["SOURCE_URL_VALID"]
        ]
        hits = news[
            (news["SYMBOL"] == row.SYMBOL) & (news["CUT_OFF"] == row.CUT_OFF)
            & (news["PUBLISHED_AT"] > start) & (news["PUBLISHED_AT"] < cutoff)
        ].copy()
        invalid_url_count = int((~hits["URL_VALID"]).sum()) if len(hits) else 0
        verified_count = int(hits["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()) if len(hits) else 0
        if len(cov) == 0:
            status = "UNKNOWN_COVERAGE"
        elif invalid_url_count:
            status = "INVALID_SOURCE_URL"
        elif len(hits) and verified_count == len(hits):
            status = "VERIFIED_NEWS_PRESENT"
        elif len(hits):
            status = "UNVERIFIED_NEWS_PRESENT"
        else:
            status = "NO_MATCH_IN_GDELT_QUERY_WINDOW"
        latest = hits.sort_values("PUBLISHED_AT").iloc[-1] if len(hits) else None
        rows.append({
            "CUT_OFF": str(row.CUT_OFF), "SYMBOL": row.SYMBOL,
            "CUTOFF_AT": cutoff.isoformat(), "WINDOW_START": start.isoformat(),
            "SOURCE_QUERY_URL": str(cov.iloc[0]["SOURCE_URL"]) if len(cov) else (str(pair_cov.iloc[0]["SOURCE_URL"]) if len(pair_cov) else ""),
            "SOURCE_QUERY_URL_VALID": bool(len(cov) and cov.iloc[0]["SOURCE_URL_VALID"]),
            "COVERAGE_STATUS": str(cov.iloc[0]["COVERAGE_STATUS"]) if len(cov) else (str(pair_cov.iloc[0]["COVERAGE_STATUS"]) if len(pair_cov) else "MISSING"),
            "NEWS_ITEMS_24H": int(len(hits)), "VERIFIED_ITEMS_24H": verified_count,
            "INVALID_ARTICLE_URLS": invalid_url_count, "NEWS_STATUS": status,
            "LATEST_PUBLISHED_AT": latest["PUBLISHED_AT"].isoformat() if latest is not None else "",
            "LATEST_CANONICAL_URL": str(latest["CANONICAL_URL"]) if latest is not None else "",
            "LATEST_PUBLISHER": str(latest["PUBLISHER"]) if latest is not None else "",
            "SYMBOL_CUTOFF_MATCH": True,
            "TIMESTAMP_WINDOW_VALID": bool((hits["PUBLISHED_AT"].gt(start) & hits["PUBLISHED_AT"].lt(cutoff)).all()) if len(hits) else True,
        })
    result = pd.DataFrame(rows)
    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT / "stock_news_24h_cutoff_join.csv", index=False)
    unknown = int(result["NEWS_STATUS"].isin(["UNKNOWN_COVERAGE", "INVALID_SOURCE_URL"]).sum())
    unverified = int(result["NEWS_STATUS"].eq("UNVERIFIED_NEWS_PRESENT").sum())
    verified = int(result["NEWS_STATUS"].eq("VERIFIED_NEWS_PRESENT").sum())
    no_match = int(result["NEWS_STATUS"].eq("NO_MATCH_IN_GDELT_QUERY_WINDOW").sum())
    bad_query_url = int((~result["SOURCE_QUERY_URL_VALID"]).sum())
    bad_timestamp = int((~result["TIMESTAMP_WINDOW_VALID"]).sum())
    duplicate_pairs = int(result.duplicated(["CUT_OFF", "SYMBOL"]).sum())
    all_coverage = len(result) > 0 and unknown == 0 and bad_query_url == 0 and duplicate_pairs == 0
    ready = all_coverage and verified > 0 and unverified == 0 and bad_timestamp == 0
    report = {
        "status": "JOIN_BUILT_AUDIT_ONLY",
        "research_status": "READY_FOR_PAIRED_ABLATION" if ready else "BLOCKED_VERIFICATION_OR_COVERAGE",
        "cutoff_symbol_rows": int(len(result)), "unique_cutoff_symbol_pairs": int(len(result[["CUT_OFF", "SYMBOL"]].drop_duplicates())),
        "news_window_hours": 24, "news_rows_loaded": int(len(news)),
        "coverage_rows_loaded": int(len(coverage)), "coverage_unknown_rows": unknown,
        "unverified_news_rows": unverified, "verified_news_rows": verified,
        "no_match_in_gdelt_query_window_rows": no_match, "invalid_article_url_rows": int(news["URL_VALID"].eq(False).sum()),
        "invalid_query_source_url_rows": bad_query_url, "timestamp_window_failures": bad_timestamp,
        "duplicate_cutoff_symbol_pairs": duplicate_pairs,
        "source_url_timestamp_symbol_cutoff_checks": "RECORDED_PER_CUTOFF_SYMBOL_ROW",
        "warning": "GDELT symbol-query matches are discovery leads only. A zero-result query is not proof that no material news exists across all sources. Story verification remains separate.",
        "production_selector_changed": False, "ranking_score_changed": False, "pressure_fade_changed": False,
    }
    write_report(report)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
