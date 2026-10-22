#!/usr/bin/env python3
"""Conservative independent URL/headline verification for the audit-only news feed.

A row is marked VERIFIED only when its article URL resolves to a non-Google
publisher page, the page returns HTTP 200, and the extracted page title has
strong token overlap with the collected headline. Failed checks stay
UNVERIFIED; no headlines, URLs, or timestamps are synthesized.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import time

import pandas as pd
import requests

NEWS = Path("data/raw/stock_news_events.csv")
REPORT = Path("outputs/news_24h/stock_news_verification_report.json")
USER_AGENT = "Mozilla/5.0 (compatible; PRECISION-WIRES-audit/1.0)"
STOP = {"the", "and", "for", "with", "from", "after", "before", "into", "over",
        "says", "said", "its", "this", "that", "will", "has", "have", "are",
        "was", "were", "about", "india", "indian", "stock", "stocks", "share",
        "shares", "nse", "bse", "limited", "ltd", "company", "market"}

class PageMeta(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_parts = []
        self.in_title = False
        self.meta_titles = []
    def handle_starttag(self, tag, attrs):
        attrs = {str(k).lower(): str(v or "") for k, v in attrs}
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "meta":
            key = (attrs.get("property") or attrs.get("name") or "").lower()
            if key in {"og:title", "twitter:title"} and attrs.get("content"):
                self.meta_titles.append(attrs["content"])
    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title and data.strip():
            self.title_parts.append(data.strip())
    def best_title(self):
        return (self.meta_titles[0] if self.meta_titles else " ".join(self.title_parts)).strip()

def tokens(value):
    return {x for x in re.findall(r"[a-z0-9]+", str(value or "").lower())
            if len(x) > 2 and x not in STOP}

def main():
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    if not NEWS.exists():
        report = {"status": "BLOCKED_MISSING_NEWS_FILE", "checked_rows": 0,
                  "verified_rows": 0, "unverified_rows": 0}
        REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, sort_keys=True))
        return 0
    df = pd.read_csv(NEWS, dtype=str).fillna("")
    required = {"HEADLINE", "CANONICAL_URL", "VERIFICATION_STATUS"}
    if not required.issubset(df.columns):
        report = {"status": "BLOCKED_BAD_NEWS_SCHEMA",
                  "missing_columns": sorted(required - set(df.columns)),
                  "checked_rows": 0, "verified_rows": 0}
        REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, sort_keys=True))
        return 0
    checked = verified = 0
    failures = []
    with requests.Session() as session:
        session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
        for idx, row in df.iterrows():
            if str(row["VERIFICATION_STATUS"]).upper() == "VERIFIED":
                continue
            url = str(row["CANONICAL_URL"]).strip()
            if urlparse(url).scheme not in {"http", "https"} or not urlparse(url).netloc:
                failures.append({"row": int(idx), "reason": "INVALID_URL"})
                continue
            checked += 1
            try:
                response = session.get(url, timeout=(10, 18), allow_redirects=True,
                                       headers={"Range": "bytes=0-400000"})
                response.raise_for_status()
                final = urlparse(response.url)
                if not final.hostname or final.hostname.lower() in {"news.google.com", "google.com", "www.google.com"}:
                    raise ValueError("URL_DID_NOT_RESOLVE_TO_PUBLISHER")
                ctype = response.headers.get("Content-Type", "").lower()
                if "html" not in ctype:
                    raise ValueError("PUBLISHER_RESPONSE_NOT_HTML")
                parser = PageMeta()
                parser.feed(response.text[:400000])
                page_title = parser.best_title()
                headline_tokens = tokens(row["HEADLINE"])
                page_tokens = tokens(page_title)
                if len(headline_tokens) < 3:
                    raise ValueError("HEADLINE_TOO_SHORT_FOR_VERIFICATION")
                overlap = len(headline_tokens & page_tokens) / len(headline_tokens)
                if not page_title or overlap < 0.50:
                    raise ValueError("PUBLISHER_TITLE_MISMATCH")
                df.at[idx, "VERIFICATION_STATUS"] = "VERIFIED"
                verified += 1
            except Exception as exc:
                failures.append({"row": int(idx), "reason": f"{type(exc).__name__}:{str(exc)[:180]}"})
            time.sleep(0.25)
    df.to_csv(NEWS, index=False)
    remaining = int(df["VERIFICATION_STATUS"].astype(str).str.upper().ne("VERIFIED").sum())
    report = {
        "status": "PASS" if remaining == 0 else "PARTIAL_VERIFICATION",
        "checked_rows": checked, "newly_verified_rows": verified,
        "verified_rows_total": int(df["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()),
        "unverified_rows_remaining": remaining,
        "verification_rule": "HTTP 200 publisher HTML after redirects, non-Google final host, page title token overlap >= 0.50",
        "failure_samples": failures[:20],
        "note": "Failed or ambiguous rows remain UNVERIFIED; verification never fabricates evidence."
    }
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("NEWS_SOURCE_VERIFICATION=" + json.dumps(report, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
