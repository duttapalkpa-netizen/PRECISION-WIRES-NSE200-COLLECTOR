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
from urllib.parse import urlparse, unquote
import base64
import hashlib
import json
import re
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


class ArticleMetadataParser(HTMLParser):
    """Extract canonical article URLs and explicit publisher publication metadata."""
    def __init__(self):
        super().__init__()
        self.urls, self.timestamps = [], []
    def handle_starttag(self, tag, attrs):
        a = {str(k).lower(): str(v or "") for k, v in attrs}
        if tag.lower() == "link":
            rel = {x.lower() for x in a.get("rel", "").split()}
            if "canonical" in rel and a.get("href"):
                self.urls.append(a["href"])
        if tag.lower() == "meta":
            key = (a.get("property") or a.get("name") or a.get("itemprop") or "").lower()
            if key in {"article:published_time", "datepublished", "datepublished", "date", "pubdate", "parsely-pub-date", "og:published_time"}:
                if a.get("content"):
                    self.timestamps.append(a["content"])
        if tag.lower() == "time" and a.get("datetime"):
            self.timestamps.append(a["datetime"])


def parse_publisher_timestamp(html):
    parser = ArticleMetadataParser()
    parser.feed(html[:1000000])
    # JSON-LD datePublished is commonly not exposed as a meta tag.
    for match in re.findall(r'"datePublished"\s*:\s*"([^"]+)"', html[:1000000], flags=re.I):
        parser.timestamps.append(match)
    for value in parser.timestamps:
        try:
            stamp = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
            if stamp.tzinfo is not None:
                return stamp.astimezone(timezone.utc)
        except (TypeError, ValueError, OverflowError):
            try:
                stamp = parse_pubdate(value)
                if stamp is not None:
                    return stamp
            except Exception:
                pass
    return None


def extract_article_urls(google_url, body=""):
    """Resolve modern Google News RSS links that do not redirect directly to publisher URLs."""
    candidates = []
    parsed = urlparse(google_url)
    # Older Google News links sometimes carry the destination as a query parameter.
    for part in parsed.query.split("&"):
        if "=" in part:
            k, v = part.split("=", 1)
            if k.lower() in {"url", "u"}:
                candidates.append(unquote(v))
    # Modern /rss/articles/CBMi... IDs encode a protobuf-like payload. Search its
    # decoded bytes for URL strings, but only accept a trusted publisher article URL.
    token = parsed.path.rsplit("/", 1)[-1]
    if token.startswith("CB") or token.startswith("CA"):
        for padding in ("", "=", "==", "==="):
            try:
                raw = base64.urlsafe_b64decode(token + padding)
                decoded = raw.decode("latin-1", errors="ignore")
                candidates.extend(re.findall(r'https?://[^\s\x00\\"<>]+', decoded))
            except Exception:
                pass
    # Google embeds destination URLs in escaped/HTML-encoded page metadata as well
    # as href attributes. Normalize those encodings before trusted-domain filtering.
    from html import unescape
    normalized_body = unescape((body or "").replace(r"\\/", "/").replace(r"\\u0026", "&"))
    candidates.extend(re.findall(r"""href=["'](https?://[^"']+)["']""", normalized_body, flags=re.I))
    candidates.extend(re.findall(r"""https?://[^\s\\\"<>']+""", normalized_body, flags=re.I))
    clean = []
    for u in candidates:
        u = unquote(unescape(u)).rstrip(".,;)")
        if is_trusted_news_url(u) and len(urlparse(u).path.strip("/")) > 5 and u not in clean:
            clean.append(u)
    return clean


def normalize_item(title, google_url, pubdate, source_name, source_host, session=None, diagnostics=None):
    """Return (auditable row, rejection reason); accept only article URL + publisher page timestamp."""
    title = str(title or "").strip()
    if not title:
        return None, "empty_title"
    group = str(source_name or "GOOGLE_NEWS_HISTORICAL_RSS")
    event_type = classify(title, group)
    if event_type is None:
        event_type = next((classify(title, label) for _, label in QUERIES if classify(title, label)), None)
    if event_type is None:
        return None, "irrelevant_headline"
    client = session or requests.Session()
    try:
        response = client.get(google_url, headers={"User-Agent": UA}, timeout=TIMEOUT, allow_redirects=True)
        final_url = str(response.url or "")
        body = (response.text or "")[:1000000]
        parser = ArticleMetadataParser()
        parser.feed(body)
        candidates = ([final_url] if is_trusted_news_url(final_url) else []) + parser.urls
        candidates.extend(extract_article_urls(google_url, body))
        trusted = next((u for u in candidates if is_trusted_news_url(u) and len(urlparse(u).path.strip("/")) > 5), "")
        response.close()
        if not trusted:
            return None, "no_trusted_publisher_article_url"
        # Fetch the actual publisher page and require explicit publication metadata.
        article = client.get(trusted, headers={"User-Agent": UA}, timeout=TIMEOUT, allow_redirects=True)
        article_url = str(article.url or trusted)
        article_body = (article.text or "")[:1000000]
        actual_published = parse_publisher_timestamp(article_body)
        article.close()
    except Exception as exc:
        return None, "publisher_redirect_or_fetch_error:" + type(exc).__name__
    if not is_trusted_news_url(article_url):
        return None, "publisher_article_redirect_untrusted"
    if actual_published is None:
        return None, "publisher_publication_timestamp_missing"
    host = (urlparse(article_url).hostname or "").lower()
    event_id = hashlib.sha256((actual_published.isoformat() + "|" + article_url).encode()).hexdigest()[:20]
    return ({
        "EVENT_DATE": actual_published.date().isoformat(),
        "EVENT_ID": event_id,
        "EVENT_TYPE": event_type,
        "PUBLISHED_AT": actual_published.isoformat(),
        "SOURCE": str(source_name or host or "trusted publisher"),
        "SOURCE_URL": article_url,
        "TITLE": title,
        "CONFIDENCE": 0.90,
        "EVIDENCE_TYPE": "TRUSTED_PUBLISHER_ARTICLE_WITH_PAGE_PUBLICATION_METADATA",
        "EVENT_DATE_BASIS": "PUBLISHER_ARTICLE_PUBLICATION_TIMESTAMP",
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
        "diagnostic_note": "Only publisher-page publication metadata is accepted for new rows; Google RSS pubDate is discovery metadata only. Inspect rejection reasons if no verified rows are found.",
        "event_semantics": "Trusted publisher media mentions with explicit publication metadata extracted from publisher article pages; not verified event-occurrence times or causal evidence.",
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
