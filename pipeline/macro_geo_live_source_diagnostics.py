#!/usr/bin/env python3
"""Small live diagnostics for GDELT, trusted RSS feeds, one FRED series, and cached NSE panel.

This script does not download/rebuild the NSE 200-session panel and never writes
market prices. Provider failures are recorded as BLOCKED/UNKNOWN, not zero data.
"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
from pathlib import Path
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
import json
import xml.etree.ElementTree as ET
import requests
import pandas as pd

OUT = Path("outputs/macro_geo/live_source_diagnostics.json")
PANEL = Path("data/processed/nse_eq_200_sessions.csv")
GDELT = "https://api.gdeltproject.org/api/v2/doc/doc"
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
RSS_FEEDS = [
    ("BBC", "https://feeds.bbci.co.uk/news/world/rss.xml"),
    ("Al Jazeera", "https://www.aljazeera.com/xml/rss/all.xml"),
    ("Bloomberg", "https://feeds.bloomberg.com/markets/news.rss"),
    ("AP News", "https://apnews.com/hub/world-news?output=rss"),
    ("Reuters", "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best"),
]

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def response_record(resp, schema_ok, row_count=None, error=None):
    return {
        "status_code": int(resp.status_code) if resp is not None else None,
        "final_url": str(resp.url) if resp is not None else None,
        "content_type": (resp.headers.get("Content-Type") if resp is not None else None),
        "server_date": (resp.headers.get("Date") if resp is not None else None),
        "observed_at_utc": utc_now(),
        "schema_valid": schema_ok,
        "row_count": row_count,
        "error": error,
    }

def check_gdelt(session, start, end):
    params = {
        "query": '(war OR sanctions OR tariff OR crude OR tanker OR shipping)',
        "mode": "ArtList", "format": "json", "maxrecords": 20, "sort": "DateDesc",
        "startdatetime": start.strftime("%Y%m%d") + "000000",
        "enddatetime": end.strftime("%Y%m%d") + "235959",
    }
    attempts = []
    for attempt in range(1, 3):
        resp = None
        try:
            resp = session.get(GDELT, params=params, timeout=(5, 12),
                               headers={"User-Agent": UA, "Accept": "application/json"})
            rec = response_record(resp, False)
            rec["attempt"] = attempt
            if resp.status_code == 429:
                rec["error"] = "HTTP 429 rate limit"
                attempts.append(rec)
                continue
            resp.raise_for_status()
            payload = resp.json()
            ok = isinstance(payload, dict) and isinstance(payload.get("articles"), list)
            rec["schema_valid"] = ok
            rec["row_count"] = len(payload["articles"]) if ok else None
            if not ok:
                rec["error"] = "JSON response missing articles list"
            attempts.append(rec)
            if ok:
                return {"status": "AVAILABLE" if rec["row_count"] else "AVAILABLE_EMPTY",
                        "attempts": attempts, "final": rec}
            return {"status": "BLOCKED_SCHEMA", "attempts": attempts, "final": rec}
        except Exception as exc:
            rec = response_record(resp, False, error=f"{type(exc).__name__}: {exc}")
            rec["attempt"] = attempt
            attempts.append(rec)
    return {"status": "BLOCKED", "attempts": attempts, "final": attempts[-1]}

def check_rss(session, publisher, url):
    try:
        resp = session.get(url, timeout=(5, 10), headers={
            "User-Agent": UA,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
        rec = response_record(resp, False)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        items = root.findall(".//item")
        if not items:
            items = root.findall(".//{http://www.w3.org/2005/Atom}entry")
        timestamps, urls = 0, 0
        for item in items:
            link = item.findtext("link") or ""
            if not link:
                atom_link = item.find("{http://www.w3.org/2005/Atom}link")
                link = str(atom_link.attrib.get("href") or "") if atom_link is not None else ""
            pub = (item.findtext("pubDate") or item.findtext("published") or
                   item.findtext("updated") or "")
            if pub:
                try:
                    dt = pd.to_datetime(pub, utc=True, errors="coerce")
                    if not pd.isna(dt): timestamps += 1
                    else:
                        dt = parsedate_to_datetime(pub)
                        if dt.tzinfo is not None: timestamps += 1
                except Exception:
                    pass
            if urlparse(link).scheme in ("http", "https") and urlparse(link).netloc:
                urls += 1
        ok = bool(items) and timestamps > 0 and urls > 0
        rec["schema_valid"] = ok
        rec["row_count"] = len(items)
        rec["timestamped_items"] = timestamps
        rec["http_url_items"] = urls
        rec["publisher"] = publisher
        rec["status"] = "AVAILABLE" if ok else "BLOCKED_SCHEMA_OR_EMPTY"
        if not ok: rec["error"] = "Feed must have items with parseable publication time and HTTP(S) links"
        return rec
    except Exception as exc:
        return {**response_record(None, False, error=f"{type(exc).__name__}: {exc}"),
                "publisher": publisher, "requested_url": url, "status": "BLOCKED"}

def check_fred(session, end):
    start = end - timedelta(days=35)
    params = {"id": "DGS10", "cosd": start.isoformat(), "coed": end.isoformat()}
    attempts = []
    for attempt in range(1, 4):
        resp = None
        try:
            resp = session.get(FRED, params=params, timeout=(5, 12),
                               headers={"User-Agent": UA, "Accept": "text/csv,*/*",
                                        "Referer": "https://fred.stlouisfed.org/"})
            rec = response_record(resp, False)
            rec["attempt"] = attempt
            resp.raise_for_status()
            from io import StringIO
            df = pd.read_csv(StringIO(resp.content.decode("utf-8-sig", errors="replace")))
            ok = "DATE" in {str(c).strip().upper() for c in df.columns} and "DGS10" in {str(c).strip().upper() for c in df.columns}
            date_col = next((c for c in df.columns if str(c).strip().upper() == "DATE"), None)
            value_col = next((c for c in df.columns if str(c).strip().upper() == "DGS10"), None)
            valid = 0
            if ok:
                values = pd.to_numeric(df[value_col].replace(".", pd.NA), errors="coerce")
                dates = pd.to_datetime(df[date_col], errors="coerce")
                valid = int((values.notna() & dates.notna()).sum())
            rec["schema_valid"] = bool(ok)
            rec["row_count"] = valid
            rec["series_id"] = "DGS10"
            rec["requested_window"] = [start.isoformat(), end.isoformat()]
            attempts.append(rec)
            if ok:
                return {"status": "AVAILABLE" if valid else "AVAILABLE_EMPTY",
                        "attempts": attempts, "final": rec}
            rec["error"] = "FRED CSV schema mismatch"
            return {"status": "BLOCKED_SCHEMA", "attempts": attempts, "final": rec}
        except Exception as exc:
            attempts.append({**response_record(resp, False, error=f"{type(exc).__name__}: {exc}"),
                             "attempt": attempt})
    return {"status": "BLOCKED", "attempts": attempts, "final": attempts[-1]}

def check_cached_panel():
    if not PANEL.exists():
        return {"status": "BLOCKED_MISSING", "path": str(PANEL), "reused": False}
    try:
        df = pd.read_csv(PANEL, usecols=lambda c: str(c).strip().upper() == "DATE")
        if df.empty or len(df.columns) != 1:
            return {"status": "BLOCKED_SCHEMA", "path": str(PANEL), "reused": False}
        dates = pd.to_datetime(df.iloc[:, 0], errors="coerce").dropna().dt.normalize()
        unique = sorted(dates.unique())
        latest = pd.Timestamp(unique[-1]).date() if unique else None
        age = (datetime.now(timezone.utc).date() - latest).days if latest else None
        ok = len(unique) >= 200 and age is not None and -1 <= age <= 5
        return {"status": "AVAILABLE" if ok else "BLOCKED_STALE_OR_SHORT",
                "path": str(PANEL), "reused": bool(ok), "unique_sessions": len(unique),
                "latest_session": latest.isoformat() if latest else None,
                "calendar_age_days": age, "no_rebuild_performed": True}
    except Exception as exc:
        return {"status": "BLOCKED_INVALID", "path": str(PANEL),
                "reused": False, "error": f"{type(exc).__name__}: {exc}"}

def main():
    now = datetime.now(timezone.utc).date()
    session = requests.Session()
    start = now - timedelta(days=3)
    report = {
        "created_at_utc": utc_now(),
        "scope": "Limited live endpoint diagnostic only; not a full historical event study",
        "gdelt": check_gdelt(session, start, now),
        "rss": [check_rss(session, name, url) for name, url in RSS_FEEDS],
        "fred": check_fred(session, now),
        "canonical_nse_panel": check_cached_panel(),
        "interpretation": "Unavailable/stale inputs remain UNKNOWN/BLOCKED; no fabricated values. Live availability does not prove mature event-study windows."
    }
    statuses = [report["gdelt"]["status"], report["fred"]["status"]] + [x["status"] for x in report["rss"]]
    report["summary"] = {
        "gdelt_available": report["gdelt"]["status"].startswith("AVAILABLE"),
        "rss_feeds_available": sum(x["status"] == "AVAILABLE" for x in report["rss"]),
        "rss_feeds_attempted": len(report["rss"]),
        "fred_available": report["fred"]["status"].startswith("AVAILABLE"),
        "canonical_panel_reusable": report["canonical_nse_panel"].get("reused", False),
        "all_live_sources_available": all(x.startswith("AVAILABLE") for x in statuses),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    # Diagnostic should succeed as a report even when a provider is blocked.
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
