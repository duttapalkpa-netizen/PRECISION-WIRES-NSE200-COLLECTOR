#!/usr/bin/env python3
"""Backfill point-in-time, source-linked historical macro/geo news via Google News RSS.

Google News is used only as a discovery/index layer. An event is accepted only
when its item has a publication timestamp, the redirect resolves to a trusted
publisher URL, and the headline passes the existing strict market-relevance
classifier. This is a media-mention event study, not proof of event occurrence
or causal impact. No dates or timestamps are inferred.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import json
import time
import xml.etree.ElementTree as ET

import pandas as pd
import requests

from macro_geo_collect_p0 import classify, is_trusted_news_url

ROOT = Path(".")
EVENTS = ROOT / "data/external/events.csv"
OUT = ROOT / "outputs/macro_geo"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
BASE = "https://news.google.com/rss/search"
LOOKBACK_DAYS = 90
TIMEOUT = (5, 15)
QUERIES = [
    ('(oil OR crude OR tanker OR "Strait of Hormuz" OR "Red Sea" OR shipping)', "ENERGY_SHIPPING_NEWS"),
    ('(sanctions OR tariff OR embargo OR "export ban" OR "trade restriction")', "SANCTIONS_TARIFF_NEWS"),
    ('(missile OR airstrike OR invasion OR ceasefire OR blockade OR "military attack")', "GEOPOLITICAL_CONFLICT_NEWS"),
]
REQUIRED = ["EVENT_DATE", "EVENT_ID", "EVENT_TYPE", "PUBLISHED_AT", "SOURCE",
            "SOURCE_URL", "TITLE", "CONFIDENCE", "EVIDENCE_TYPE", "EVENT_DATE_BASIS",
            "QUERY_GROUP", "SOURCE_COUNTRY", "GDELT_API_URL"]


def parse_pubdate(value):
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            return None
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        return None


class CanonicalURLParser(HTMLParser):
    """Read canonical article URLs without treating publisher homepages as evidence."""
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() != "link":
            return
        a = {str(k).lower(): str(v or "") for k, v in attrs}
        rel = {x.lower() for x in a.get("rel", "").split()}
        if "canonical" in rel and a.get("href"):
            self.urls.append(a["href"])


def normalize_item(title, google_url, pubdate, source_name, source_host, session=None, diagnostics=None):
    """Return (auditable row, rejection reason); never accept a Google URL as publisher evidence."""
    title = str(title or "").strip()
    published = parse_pubdate(pubdate)
    if not title:
        return None, "empty_title"
    if published is None:
        return None, "invalid_or_timezone_missing_pubdate"
    group = str(source_name or "GOOGLE_NEWS_HISTORICAL_RSS")
    event_type = classify(title, group)
    if event_type is None:
        # The query's category is not proof of relevance; preserve strict classifier.
        event_type = next((classify(title, label) for _, label in QUERIES if classify(title, label)), None)
    if event_type is None:
        return None, "irrelevant_headline"
    client = session or requests.Session()
    try:
        response = client.get(google_url, headers={"User-Agent": UA}, timeout=TIMEOUT,
                              allow_redirects=True)
        final_url = str(response.url or "")
        canonical = []
        if is_trusted_news_url(final_url):
            canonical = [final_url]
        else:
            parser = CanonicalURLParser()
            # Bounded response parsing: only inspect a small prefix; never trust Google wrapper URLs.
            parser.feed((response.text or "")[:500000])
            canonical = parser.urls
        trusted = next((u for u in canonical if is_trusted_news_url(u)), "")
        response.close()
    except Exception as exc:
        return None, "publisher_redirect_or_fetch_error:" + type(exc).__name__
    if not trusted:
        return None, "no_trusted_publisher_article_url"
    host = (urlparse(trusted).hostname or "").lower()
    event_id = hashlib.sha256((published.isoformat() + "|" + trusted).encode()).hexdigest()[:20]
    return ({
        "EVENT_DATE": published.date().isoformat(),
        "EVENT_ID": event_id,
        "EVENT_TYPE": event_type,
        "PUBLISHED_AT": published.isoformat(),
        "SOURCE": str(source_name or host or "trusted publisher via Google News RSS"),
        "SOURCE_URL": trusted,
        "TITLE": title,
        "CONFIDENCE": 0.80,
        "EVIDENCE_TYPE": "TRUSTED_PUBLISHER_ARTICLE_DISCOVERED_VIA_GOOGLE_NEWS_RSS",
        "EVENT_DATE_BASIS": "PUBLISHER_RSS_PUBLICATION_TIMESTAMP",
        "QUERY_GROUP": group,
        "SOURCE_COUNTRY": "",
        "GDELT_API_URL": "",
    }, None)


def collect(start, end, session=None):
    client = session or requests.Session()
    client.headers.update({"User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml"})
    events, failures = [], []
    diagnostics = {"rss_requests": 0, "rss_items_seen": 0, "accepted_before_date_filter": 0,
                   "accepted": 0, "outside_requested_slice": 0, "rejections": {},
                   "slice_item_counts": []}
    def reject(reason):
        diagnostics["rejections"][reason] = diagnostics["rejections"].get(reason, 0) + 1
    # Narrow date slices prevent search ranking from returning only the newest
    # articles and make it more likely that older events have matured close windows.
    for query, _ in QUERIES:
        cursor = start
        while cursor <= end:
            slice_end = min(end, cursor + timedelta(days=13))
            q = f'{query} after:{cursor.isoformat()} before:{(slice_end + timedelta(days=1)).isoformat()}'
            try:
                resp = client.get(BASE, params={"q": q, "hl": "en-US", "gl": "US", "ceid": "US:en"},
                                  timeout=TIMEOUT)
                diagnostics["rss_requests"] += 1
                resp.raise_for_status()
                root = ET.fromstring(resp.content)
                items = root.findall(".//item")
                diagnostics["rss_items_seen"] += len(items)
                diagnostics["slice_item_counts"].append({"start": cursor.isoformat(), "end": slice_end.isoformat(), "items": len(items)})
                for item in items:
                    title = (item.findtext("title") or "").strip()
                    link = (item.findtext("link") or "").strip()
                    pub = item.findtext("pubDate") or ""
                    source_el = item.find("source")
                    source_name = (source_el.text or "").strip() if source_el is not None else ""
                    source_host = source_el.attrib.get("url", "") if source_el is not None else ""
                    row, reason = normalize_item(title, link, pub, source_name, source_host, client)
                    if reason:
                        reject(reason)
                        continue
                    diagnostics["accepted_before_date_filter"] += 1
                    if cursor.isoformat() <= row["EVENT_DATE"] <= slice_end.isoformat():
                        events.append(row)
                        diagnostics["accepted"] += 1
                    else:
                        diagnostics["outside_requested_slice"] += 1
            except Exception as exc:
                failures.append({"query": query, "slice_start": cursor.isoformat(),
                                 "slice_end": slice_end.isoformat(),
                                 "error": f"{type(exc).__name__}: {exc}"})
                reject("rss_request_or_xml_error:" + type(exc).__name__)
            cursor = slice_end + timedelta(days=1)
            time.sleep(0.2)
    df = pd.DataFrame(events, columns=REQUIRED)
    if not df.empty:
        df = df.drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT", "EVENT_ID"])
    return df, failures, diagnostics


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    end = datetime.now(timezone.utc).date() - timedelta(days=1)
    start = end - timedelta(days=LOOKBACK_DAYS - 1)
    fresh, failures, diagnostics = collect(start, end)
    existing = pd.read_csv(EVENTS) if EVENTS.exists() else pd.DataFrame(columns=REQUIRED)
    existing.columns = [str(c).strip().upper() for c in existing.columns]
    for col in REQUIRED:
        if col not in existing.columns:
            existing[col] = ""
    combined = pd.concat([existing[REQUIRED], fresh], ignore_index=True)
    if not combined.empty:
        combined["PUBLISHED_AT"] = pd.to_datetime(combined["PUBLISHED_AT"], utc=True, errors="coerce")
        combined = combined.dropna(subset=["PUBLISHED_AT"])
        combined = combined.drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT", "EVENT_ID"])
        combined["PUBLISHED_AT"] = combined["PUBLISHED_AT"].map(lambda x: x.isoformat())
    combined.to_csv(EVENTS, index=False)
    report = {
        "status": "BACKFILL_COMPLETE" if not fresh.empty else "BACKFILL_NO_VERIFIED_EVENTS",
        "lookback_start": start.isoformat(), "lookback_end": end.isoformat(),
        "new_verified_event_rows": int(len(fresh)),
        "total_deduplicated_event_rows": int(len(combined)),
        "new_events_with_source_urls": int(fresh["SOURCE_URL"].astype(str).str.startswith("https://").sum()) if not fresh.empty else 0,
        "failures": failures,
        "collection_diagnostics": diagnostics,
        "diagnostic_note": "A clean zero-row result is not a pass; inspect RSS item counts, rejection reasons, and slice counts. RSS pubDate is publication metadata from the discovery feed, not independently verified event-occurrence time.",
        "event_semantics": "Trusted publisher media mentions with explicit publisher publication timestamps; not verified event-occurrence times or causal evidence.",
        "no_synthetic_timestamps": True,
        "output": str(EVENTS),
    }
    (OUT / "historical_news_backfill_report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    # Empty backfill is a research blocker recorded in the report, not a collector crash.
    # The downstream hard gate remains the authority on release readiness.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
