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
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote_plus
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


def normalize_item(title, google_url, pubdate, source_name, source_host, session=None):
    """Return an auditable row or None; never accept Google URL as the publisher source."""
    title = str(title or "").strip()
    published = parse_pubdate(pubdate)
    if not title or published is None:
        return None
    group = "GOOGLE_NEWS_HISTORICAL_RSS"
    event_type = classify(title, group)
    if event_type is None:
        return None
    client = session or requests.Session()
    try:
        response = client.get(google_url, headers={"User-Agent": UA}, timeout=TIMEOUT,
                              allow_redirects=True, stream=True)
        final_url = str(response.url or "")
        response.close()
    except Exception:
        return None
    if not is_trusted_news_url(final_url):
        return None
    event_id = hashlib.sha256((published.isoformat() + "|" + final_url).encode()).hexdigest()[:20]
    return {
        "EVENT_DATE": published.date().isoformat(),
        "EVENT_ID": event_id,
        "EVENT_TYPE": event_type,
        "PUBLISHED_AT": published.isoformat(),
        "SOURCE": str(source_name or source_host or "trusted publisher via Google News RSS"),
        "SOURCE_URL": final_url,
        "TITLE": title,
        "CONFIDENCE": 0.80,
        "EVIDENCE_TYPE": "TRUSTED_PUBLISHER_ARTICLE_DISCOVERED_VIA_GOOGLE_NEWS_RSS",
        "EVENT_DATE_BASIS": "PUBLISHER_RSS_PUBLICATION_TIMESTAMP",
        "QUERY_GROUP": group,
        "SOURCE_COUNTRY": "",
        "GDELT_API_URL": "",
    }


def collect(start, end, session=None):
    client = session or requests.Session()
    client.headers.update({"User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml"})
    events, failures = [], []
    for query, _ in QUERIES:
        q = f'{query} after:{start.isoformat()} before:{(end + timedelta(days=1)).isoformat()}'
        try:
            resp = client.get(BASE, params={"q": q, "hl": "en-US", "gl": "US", "ceid": "US:en"},
                              timeout=TIMEOUT)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            items = root.findall(".//item")
            for item in items:
                title = (item.findtext("title") or "").strip()
                link = (item.findtext("link") or "").strip()
                pub = item.findtext("pubDate") or ""
                source_el = item.find("source")
                source_name = (source_el.text or "").strip() if source_el is not None else ""
                source_host = source_el.attrib.get("url", "") if source_el is not None else ""
                row = normalize_item(title, link, pub, source_name, source_host, client)
                if row and start.isoformat() <= row["EVENT_DATE"] <= end.isoformat():
                    events.append(row)
        except Exception as exc:
            failures.append({"query": query, "error": f"{type(exc).__name__}: {exc}"})
        time.sleep(0.2)
    df = pd.DataFrame(events, columns=REQUIRED)
    if not df.empty:
        df = df.drop_duplicates(["EVENT_ID"]).sort_values(["PUBLISHED_AT", "EVENT_ID"])
    return df, failures


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    end = datetime.now(timezone.utc).date() - timedelta(days=1)
    start = end - timedelta(days=LOOKBACK_DAYS - 1)
    fresh, failures = collect(start, end)
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
