"""Bounded live RSS smoke test; one symbol/cutoff, no dataset rebuild."""
import json
import os
import sys
from datetime import timedelta
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import pandas as pd
import requests

symbol = os.getenv("NEWS_SYMBOL", "TESTCO").strip().upper()
cutoff_day = pd.Timestamp(os.getenv("NEWS_CUTOFF", "2026-10-14")).normalize().tz_localize("Asia/Kolkata") + pd.Timedelta(hours=15, minutes=30)
start = cutoff_day - pd.Timedelta(hours=24)
url = "https://news.google.com/rss/search"
params = {"q": f'"{symbol}" NSE stock after:{start.date().isoformat()} before:{cutoff_day.date().isoformat()}', "hl": "en-IN", "gl": "IN", "ceid": "IN:en"}
prepared_url = requests.Request("GET", url, params=params).prepare().url
report = {"symbol": symbol, "cutoff": cutoff_day.isoformat(), "window_start": start.isoformat(), "window_end": cutoff_day.isoformat(), "source_url": prepared_url, "status": "UNKNOWN", "items_in_window": 0, "error": ""}
try:
    response = requests.get(url, params=params, timeout=(10, 20), headers={"User-Agent": "Mozilla/5.0 (compatible; PRECISION-WIRES-audit/1.0)"})
    response.raise_for_status()
    root = ET.fromstring(response.content)
    channel = root.find("channel")
    if channel is None:
        raise ValueError("RSS missing channel")
    items = channel.findall("item")
    valid = []
    for item in items:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        raw_date = (item.findtext("pubDate") or "").strip()
        try:
            published = pd.Timestamp(parsedate_to_datetime(raw_date)).tz_convert("UTC").tz_convert("Asia/Kolkata")
        except Exception:
            continue
        parsed = urlparse(link)
        if title and parsed.scheme in ("http", "https") and parsed.netloc and start < published < cutoff_day:
            valid.append({"title": title, "published_at": published.isoformat(), "url": link, "verification_status": "UNVERIFIED_GOOGLE_NEWS_RSS_MATCH"})
    report.update({"status": "PASS" if response.ok else "UNKNOWN", "http_status": response.status_code, "rss_items_returned": len(items), "items_in_window": len(valid), "sample_items": valid[:3], "all_items_unverified": True})
except Exception as exc:
    report["error"] = f"{type(exc).__name__}: {exc}"
print(json.dumps(report, indent=2))
if report["status"] != "PASS":
    sys.exit("LIVE_RSS_SMOKE_BLOCKED")
