#!/usr/bin/env python3
"""Collect point-in-time GDELT news queries for frozen H+1 audit candidates.

GDELT is a secondary discovery source, not proof of a verified stock catalyst.
Every hit is UNVERIFIED until manually/independently confirmed. A successful
empty query means no match in this source/query, never proof that no news exists.
"""
from pathlib import Path
from datetime import timedelta
import json
import time
import requests
import pandas as pd

PICKS = Path("outputs/prospective/target5_h1_selector_experiment_picks.csv")
RAW = Path("data/raw")
NEWS_OUT = RAW / "stock_news_events.csv"
COVERAGE_OUT = RAW / "stock_news_coverage.csv"
REPORT_OUT = Path("outputs/news_24h/stock_news_collection_report.json")
API = "https://api.gdeltproject.org/api/v2/doc/doc"
TZ = "Asia/Kolkata"
HEADERS = {"User-Agent": "PRECISION-WIRES-Research/1.0 (audit-only; contact via repository)"}


def utc_stamp(ts):
    return ts.tz_convert("UTC").strftime("%Y%m%d%H%M%S")


def main():
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)
    if not PICKS.exists():
        report = {"status": "BLOCKED_MISSING_CANDIDATE_PICKS", "input": str(PICKS),
                  "news_rows": 0, "coverage_rows": 0, "source": "GDELT DOC API",
                  "verification": "All matches require independent verification."}
        REPORT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        return 0

    picks = pd.read_csv(PICKS, dtype={"SYMBOL": str})
    required = {"CUT_OFF", "SYMBOL"}
    missing = sorted(required - set(picks.columns))
    if missing:
        report = {"status": "BLOCKED_BAD_CANDIDATE_SCHEMA", "missing_columns": missing,
                  "news_rows": 0, "coverage_rows": 0}
        REPORT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        return 0

    pairs = picks[["CUT_OFF", "SYMBOL"]].dropna().drop_duplicates().copy()
    pairs["CUT_OFF"] = pd.to_datetime(pairs["CUT_OFF"], errors="coerce")
    pairs["SYMBOL"] = pairs["SYMBOL"].astype(str).str.upper().str.strip()
    pairs = pairs.dropna(subset=["CUT_OFF"])
    pairs = pairs[pairs["SYMBOL"].ne("")]
    if pairs.empty:
        report = {"status": "BLOCKED_NO_CANDIDATE_PAIRS", "news_rows": 0, "coverage_rows": 0}
        REPORT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report))
        return 0

    news_rows, coverage_rows = [], []
    ok, failed = 0, 0
    with requests.Session() as session:
        session.headers.update(HEADERS)
        for n, pair in enumerate(pairs.itertuples(index=False), start=1):
            cutoff = pd.Timestamp(pair.CUT_OFF).normalize().tz_localize(TZ) + pd.Timedelta(hours=15, minutes=30)
            start = cutoff - pd.Timedelta(hours=24)
            query = f'"{pair.SYMBOL}"'
            coverage = {
                "CUT_OFF": cutoff.date().isoformat(), "SYMBOL": pair.SYMBOL,
                "WINDOW_START": start.isoformat(), "WINDOW_END": cutoff.isoformat(),
                "COVERAGE_STATUS": "UNKNOWN", "SOURCE_SCOPE": "GDELT_DOC_API_SYMBOL_QUERY",
                "QUERY": query, "ERROR": "",
            }
            try:
                response = session.get(API, params={
                    "query": query, "mode": "ArtList", "format": "json",
                    "startdatetime": utc_stamp(start), "enddatetime": utc_stamp(cutoff),
                    "maxrecords": 75, "sort": "DateDesc",
                }, timeout=(8, 25))
                response.raise_for_status()
                payload = response.json()
                if not isinstance(payload, dict) or not isinstance(payload.get("articles", []), list):
                    raise ValueError("GDELT response missing articles list")
                articles = payload.get("articles", [])
                for article in articles:
                    raw_date = str(article.get("seendate", "")).strip()
                    published = pd.to_datetime(raw_date, format="%Y%m%d%H%M%S", errors="coerce", utc=True)
                    url = str(article.get("url", "")).strip()
                    title = str(article.get("title", "")).strip()
                    domain = str(article.get("domain", "")).strip()
                    if pd.isna(published) or not url.startswith(("http://", "https://")) or not title:
                        continue
                    published_ist = published.tz_convert(TZ)
                    if not (start < published_ist < cutoff):
                        continue
                    event_id = f"{pair.SYMBOL}|{published.isoformat()}|{url}"
                    news_rows.append({
                        "EVENT_ID": event_id, "CUT_OFF": cutoff.date().isoformat(),
                        "SYMBOL": pair.SYMBOL, "PUBLISHED_AT": published.isoformat(),
                        "PUBLISHER": domain or "UNKNOWN_DOMAIN", "HEADLINE": title,
                        "CANONICAL_URL": url, "SOURCE_TYPE": "GDELT_DISCOVERY",
                        "VERIFICATION_STATUS": "UNVERIFIED_GDELT_MATCH",
                    })
                coverage["COVERAGE_STATUS"] = "COMPLETE"
                coverage["RESULTS_RETURNED"] = len(articles)
                ok += 1
            except Exception as exc:
                coverage["ERROR"] = f"{type(exc).__name__}: {exc}"
                coverage["RESULTS_RETURNED"] = ""
                failed += 1
            coverage_rows.append(coverage)
            if n % 25 == 0:
                print(f"PROGRESS={n}/{len(pairs)} queries_ok={ok} queries_failed={failed}", flush=True)
            time.sleep(0.15)

    news_cols = ["EVENT_ID", "CUT_OFF", "SYMBOL", "PUBLISHED_AT", "PUBLISHER",
                 "HEADLINE", "CANONICAL_URL", "SOURCE_TYPE", "VERIFICATION_STATUS"]
    cov_cols = ["CUT_OFF", "SYMBOL", "WINDOW_START", "WINDOW_END", "COVERAGE_STATUS",
                "SOURCE_SCOPE", "QUERY", "RESULTS_RETURNED", "ERROR"]
    news_df = pd.DataFrame(news_rows, columns=news_cols).drop_duplicates(["SYMBOL", "PUBLISHED_AT", "CANONICAL_URL"])
    cov_df = pd.DataFrame(coverage_rows, columns=cov_cols)
    news_df.to_csv(NEWS_OUT, index=False)
    cov_df.to_csv(COVERAGE_OUT, index=False)
    report = {
        "status": "COLLECTED_WITH_GAPS" if failed else "COLLECTED_GDELT_DISCOVERY_ONLY",
        "candidate_cutoff_pairs": int(len(pairs)), "queries_succeeded": int(ok),
        "queries_failed": int(failed), "news_rows": int(len(news_df)),
        "coverage_rows": int(len(cov_df)), "coverage_complete_rows": int((cov_df["COVERAGE_STATUS"] == "COMPLETE").sum()),
        "coverage_unknown_rows": int((cov_df["COVERAGE_STATUS"] != "COMPLETE").sum()),
        "source": "GDELT DOC API", "source_limit": "A successful query only establishes coverage of this source/query; it does not establish absence of all news.",
        "verification": "All matches are UNVERIFIED_GDELT_MATCH; independent source/headline verification is required before paired news ablation.",
        "news_output": str(NEWS_OUT), "coverage_output": str(COVERAGE_OUT),
    }
    REPORT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
