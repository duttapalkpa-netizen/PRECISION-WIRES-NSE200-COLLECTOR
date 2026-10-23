#!/usr/bin/env python3
"""Collect point-in-time GDELT news queries for frozen H+1 audit candidates.

GDELT is a secondary discovery source, not proof of a verified stock catalyst.
Every hit is UNVERIFIED until manually/independently confirmed. A successful
empty query means no match in this source/query, never proof that no news exists.
"""
from pathlib import Path
from datetime import timedelta
import json
import re
import time
import requests
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from requests.exceptions import HTTPError
import pandas as pd

PICKS = Path("outputs/prospective/target5_h1_selector_experiment_picks.csv")
RAW = Path("data/raw")
NEWS_OUT = RAW / "stock_news_events.csv"
COVERAGE_OUT = RAW / "stock_news_coverage.csv"
REPORT_OUT = Path("outputs/news_24h/stock_news_collection_report.json")
API = "https://api.gdeltproject.org/api/v2/doc/doc"
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search"
TZ = "Asia/Kolkata"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; PRECISION-WIRES-Research/1.0; audit-only)", "Accept": "application/json"}
MAX_RETRIES = 3
BACKOFF_SECONDS = (2, 4, 6)

# English-word symbols can match ordinary prose (e.g. "comes into focus").
# For these symbols, require explicit exchange/ticker notation before retaining
# a headline as a stock-specific event. This is a relevance filter, not a
# verification rule; surviving discovery rows remain UNVERIFIED.
AMBIGUOUS_ENGLISH_SYMBOLS = {"FOCUS", "STANLEY"}


def headline_relevant_to_symbol(symbol, headline):
    symbol = str(symbol or "").strip().upper()
    headline = str(headline or "")
    if not symbol or not headline.strip():
        return False
    if symbol in AMBIGUOUS_ENGLISH_SYMBOLS:
        if symbol == "STANLEY":
            # The ticker query can return unrelated stories because Stanley is
            # also a common name. Require issuer name or explicit ticker notation.
            patterns = (
                r"\bNSE\s*[:\-]\s*STANLEY\b",
                r"\bSTANLEY\.NS\b",
                r"\bSTANLEY\s+LIFESTYLES\b",
            )
        else:
            patterns = (
                rf"\bNSE\s*[:\-]\s*{re.escape(symbol)}\b",
                rf"\b{re.escape(symbol)}\.NS\b",
                rf"\b{re.escape(symbol)}\s+(?:LTD|LIMITED|SHARES|STOCK)\b",
            )
        return any(re.search(pattern, headline, flags=re.IGNORECASE) for pattern in patterns)
    # For ordinary tickers, the query is already ticker-specific and headlines
    # may use company names instead of symbols. Keep those discovery leads
    # unverified; apply strict headline relevance only to ambiguous English words.
    return True


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
                "QUERY": query, "SOURCE_URL": "", "ERROR": "",
            }
            try:
                payload = None
                last_error = None
                params = {
                    "query": query, "mode": "ArtList", "format": "json",
                    "startdatetime": utc_stamp(start), "enddatetime": utc_stamp(cutoff),
                    "maxrecords": 75, "sort": "DateDesc",
                }
                coverage["SOURCE_URL"] = requests.Request("GET", API, params=params).prepare().url
                for attempt in range(MAX_RETRIES):
                    try:
                        response = session.get(API, params=params, timeout=(15, 60))
                        response.raise_for_status()
                        candidate_payload = response.json()
                        if not isinstance(candidate_payload, dict) or "articles" not in candidate_payload or not isinstance(candidate_payload.get("articles"), list):
                            raise ValueError("GDELT response missing articles list")
                        payload = candidate_payload
                        break
                    except Exception as exc:
                        last_error = exc
                        retryable = isinstance(exc, (requests.Timeout, requests.ConnectionError)) or (
                            isinstance(exc, HTTPError) and getattr(exc.response, "status_code", None) in (429, 500, 502, 503, 504)
                        )
                        if not retryable or attempt + 1 >= MAX_RETRIES:
                            raise
                        delay = BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS) - 1)]
                        retry_after = getattr(getattr(exc, "response", None), "headers", {}).get("Retry-After")
                        try:
                            delay = max(delay, min(45, int(retry_after))) if retry_after else delay
                        except (TypeError, ValueError):
                            pass
                        print(f"RETRY symbol={pair.SYMBOL} attempt={attempt+1}/{MAX_RETRIES} delay_s={delay} reason={type(exc).__name__}", flush=True)
                        time.sleep(delay)
                if payload is None:
                    raise last_error or RuntimeError("GDELT request failed without response")
                articles = payload.get("articles", [])
                for article in articles:
                    raw_date = str(article.get("seendate", "")).strip()
                    published = pd.to_datetime(raw_date, format="%Y%m%d%H%M%S", errors="coerce", utc=True)
                    url = str(article.get("url", "")).strip()
                    title = str(article.get("title", "")).strip()
                    domain = str(article.get("domain", "")).strip()
                    if pd.isna(published) or not url.startswith(("http://", "https://")) or not title:
                        continue
                    if not headline_relevant_to_symbol(pair.SYMBOL, title):
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
                coverage["SOURCE_SCOPE"] = "GDELT_DOC_API_SYMBOL_QUERY"
                ok += 1
            except Exception as exc:
                gdelt_error = "{}: {}".format(type(exc).__name__, exc)
                try:
                    rss_params = {"q": '"{}" NSE stock after:{} before:{}'.format(pair.SYMBOL, start.date().isoformat(), cutoff.date().isoformat()), "hl": "en-IN", "gl": "IN", "ceid": "IN:en"}
                    rss_url = requests.Request("GET", GOOGLE_NEWS_RSS, params=rss_params).prepare().url
                    rss_response = session.get(GOOGLE_NEWS_RSS, params=rss_params, timeout=(15, 30))
                    rss_response.raise_for_status()
                    root = ET.fromstring(rss_response.content)
                    channel = root.find("channel")
                    if channel is None:
                        raise ValueError("Google News RSS missing channel")
                    rss_articles = channel.findall("item")
                    for article in rss_articles:
                        title = (article.findtext("title") or "").strip()
                        url = (article.findtext("link") or "").strip()
                        raw_date = (article.findtext("pubDate") or "").strip()
                        domain = (article.findtext("source") or "Google News RSS").strip()
                        try:
                            published = pd.Timestamp(parsedate_to_datetime(raw_date)).tz_convert("UTC")
                        except Exception:
                            continue
                        published_ist = published.tz_convert(TZ)
                        if not title or not url.startswith(("http://", "https://")) or not (start < published_ist < cutoff):
                            continue
                        if not headline_relevant_to_symbol(pair.SYMBOL, title):
                            continue
                        event_id = "{}|{}|{}".format(pair.SYMBOL, published.isoformat(), url)
                        news_rows.append({"EVENT_ID": event_id, "CUT_OFF": cutoff.date().isoformat(), "SYMBOL": pair.SYMBOL, "PUBLISHED_AT": published.isoformat(), "PUBLISHER": domain, "HEADLINE": title, "CANONICAL_URL": url, "SOURCE_TYPE": "GOOGLE_NEWS_RSS_DISCOVERY", "VERIFICATION_STATUS": "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH"})
                    coverage["COVERAGE_STATUS"] = "COMPLETE"
                    coverage["SOURCE_SCOPE"] = "GOOGLE_NEWS_RSS_SYMBOL_QUERY"
                    coverage["SOURCE_URL"] = rss_url
                    coverage["RESULTS_RETURNED"] = len(rss_articles)
                    coverage["ERROR"] = "GDELT fallback used: " + gdelt_error
                    ok += 1
                except Exception as rss_exc:
                    coverage["ERROR"] = gdelt_error + " | GoogleNewsRSS {}: {}".format(type(rss_exc).__name__, rss_exc)
                    coverage["RESULTS_RETURNED"] = ""
                    failed += 1
            coverage_rows.append(coverage)
            if n % 25 == 0:
                print(f"PROGRESS={n}/{len(pairs)} queries_ok={ok} queries_failed={failed}", flush=True)
            time.sleep(3.0)

    # Publisher-native RSS fast path: collect once per run, then map headlines
    # to frozen cutoff/symbol pairs. Feed-origin status means source/time provenance
    # was supplied by the publisher feed; it is not a claim that the story predicts price.
    publisher_feeds = {
        "BBC News": "https://feeds.bbci.co.uk/news/rss.xml",
        "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
        "BBC Business": "https://feeds.bbci.co.uk/news/business/rss.xml",
        "Sky News World": "https://feeds.skynews.com/feeds/rss/world.xml",
        "Sky News Business": "https://feeds.skynews.com/feeds/rss/business.xml",
        "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
        "DW News": "https://rss.dw.com/rdf/rss-en-all",
        "France 24": "https://www.france24.com/en/rss",
        "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    }
    publisher_feed_status = {}
    pair_symbols = sorted(set(str(x).upper().strip() for x in pairs["SYMBOL"] if str(x).strip()))
    pair_windows = {str(r.SYMBOL).upper().strip(): [] for r in pairs.itertuples(index=False)}
    for pair in pairs.itertuples(index=False):
        cutoff = pd.Timestamp(pair.CUT_OFF).normalize().tz_localize(TZ) + pd.Timedelta(hours=15, minutes=30)
        window_start = cutoff - pd.Timedelta(hours=24)
        pair_windows.setdefault(str(pair.SYMBOL).upper().strip(), []).append(
            (window_start, cutoff, str(cutoff.date()))
        )
    for publisher, feed_url in publisher_feeds.items():
        try:
            response = requests.get(feed_url, headers={"User-Agent": HEADERS["User-Agent"], "Accept": "application/rss+xml,application/xml,text/xml"}, timeout=(5, 12))
            response.raise_for_status()
            root = ET.fromstring(response.content)
            items = root.findall(".//item")
            if not items:
                items = root.findall(".//{*}entry")
            for item in items:
                title = (item.findtext("title") or item.findtext("{*}title") or "").strip()
                url = (item.findtext("link") or item.findtext("{*}link") or "").strip()
                if not url:
                    link_node = item.find("{*}link")
                    if link_node is not None:
                        url = (link_node.attrib.get("href") or "").strip()
                raw_date = (item.findtext("pubDate") or item.findtext("{*}published") or item.findtext("{*}updated") or item.findtext("{*}date") or "").strip()
                try:
                    published = pd.Timestamp(parsedate_to_datetime(raw_date)).tz_convert("UTC")
                except Exception:
                    try:
                        published = pd.to_datetime(raw_date, utc=True, errors="raise")
                    except Exception:
                        continue
                if not title or not url.startswith(("https://", "http://")):
                    continue
                title_key = title.lower()
                for symbol, windows in pair_windows.items():
                    # Symbol token must be explicit in the title to avoid broad false matches.
                    if not re.search(r"(?<![A-Z0-9])" + re.escape(symbol) + r"(?![A-Z0-9])", title, flags=re.I):
                        continue
                    for win_start, cutoff, cutoff_date in windows:
                        pub_ist = published.tz_convert(TZ)
                        if not (win_start < pub_ist < cutoff):
                            continue
                        news_rows.append({
                            "EVENT_ID": f"{symbol}|{published.isoformat()}|{url}",
                            "CUT_OFF": cutoff_date, "SYMBOL": symbol,
                            "PUBLISHED_AT": published.isoformat(), "PUBLISHER": publisher,
                            "HEADLINE": title, "CANONICAL_URL": url,
                            "SOURCE_TYPE": "PUBLISHER_NATIVE_RSS",
                            "VERIFICATION_STATUS": "VERIFIED",
                        })
            publisher_feed_status[publisher] = {"status": "AVAILABLE", "feed_url": feed_url, "items_seen": len(items)}
        except Exception as exc:
            publisher_feed_status[publisher] = {"status": "UNKNOWN", "feed_url": feed_url, "error": f"{type(exc).__name__}: {str(exc)[:160]}"}

    news_cols = ["EVENT_ID", "CUT_OFF", "SYMBOL", "PUBLISHED_AT", "PUBLISHER",
                 "HEADLINE", "CANONICAL_URL", "SOURCE_TYPE", "VERIFICATION_STATUS"]
    cov_cols = ["CUT_OFF", "SYMBOL", "WINDOW_START", "WINDOW_END", "COVERAGE_STATUS",
                "SOURCE_SCOPE", "QUERY", "SOURCE_URL", "RESULTS_RETURNED", "ERROR"]
    news_df = pd.DataFrame(news_rows, columns=news_cols).drop_duplicates(["SYMBOL", "PUBLISHED_AT", "CANONICAL_URL"])
    news_before_syndication_dedupe = len(news_df)
    if not news_df.empty:
        news_df["_TITLE_KEY"] = news_df["HEADLINE"].astype(str).str.lower().str.replace(r"[^a-z0-9]+", " ", regex=True).str.strip()
        news_df = news_df.drop_duplicates(["SYMBOL", "CUT_OFF", "_TITLE_KEY"]).drop(columns=["_TITLE_KEY"])
    syndicated_duplicates_removed = news_before_syndication_dedupe - len(news_df)
    cov_df = pd.DataFrame(coverage_rows, columns=cov_cols)
    news_df.to_csv(NEWS_OUT, index=False)
    cov_df.to_csv(COVERAGE_OUT, index=False)
    report = {
        "status": "COLLECTED_WITH_GAPS" if failed else "COLLECTED_GDELT_DISCOVERY_ONLY",
        "candidate_cutoff_pairs": int(len(pairs)), "queries_succeeded": int(ok),
        "queries_failed": int(failed), "news_rows": int(len(news_df)),
        "error_samples": [x["ERROR"] for x in coverage_rows if x.get("ERROR")][:5],
        "coverage_rows": int(len(cov_df)), "coverage_complete_rows": int((cov_df["COVERAGE_STATUS"] == "COMPLETE").sum()),
        "coverage_unknown_rows": int((cov_df["COVERAGE_STATUS"] != "COMPLETE").sum()),
        "syndicated_duplicate_rows_removed": int(syndicated_duplicates_removed),
        "source": "Publisher-native RSS first-class fast path plus GDELT DOC API and Google News RSS discovery fallback",
        "publisher_native_feeds": publisher_feed_status, "request_timeout_seconds": {"connect": 15, "read": 60}, "retry_policy": {"max_attempts": MAX_RETRIES, "backoff_seconds": list(BACKOFF_SECONDS), "retry_after_cap_seconds": 45, "inter_query_delay_seconds": 3}, "source_limit": "A successful query only establishes coverage of this source/query; it does not establish absence of all news.",
        "verification": "Publisher-native RSS items carry VERIFIED source/time provenance from the official feed; GDELT rows remain UNVERIFIED_GDELT_MATCH and Google News RSS rows remain UNVERIFIED_GOOGLE_NEWS_RSS_MATCH until independently resolved. VERIFIED is not a prediction or guarantee of market impact.",
        "news_output": str(NEWS_OUT), "coverage_output": str(COVERAGE_OUT),
    }
    REPORT_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
