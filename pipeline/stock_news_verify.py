#!/usr/bin/env python3
"""Conservative independent URL/headline verification for the audit-only news feed (Step 3).

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
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import requests

try:
    from googlenewsdecoder import gnewsdecoder
except Exception:  # Keep non-Google publisher URLs verifiable if decoder import fails.
    gnewsdecoder = None

NEWS = Path("data/raw/stock_news_events.csv")
REPORT = Path("outputs/news_24h/stock_news_verification_report.json")
OFFICIAL_OVERRIDES = Path("data/reference/verified_official_news_filing_overrides.csv")
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
    pending = []
    failures = []
    overrides = pd.read_csv(OFFICIAL_OVERRIDES, dtype=str).fillna("") if OFFICIAL_OVERRIDES.exists() else pd.DataFrame()
    for idx, row in df.iterrows():
        if str(row["VERIFICATION_STATUS"]).upper() == "VERIFIED":
            continue
        url = str(row["CANONICAL_URL"]).strip()
        if urlparse(url).scheme not in {"http", "https"} or not urlparse(url).netloc:
            failures.append({"row": int(idx), "reason": "INVALID_URL"})
            continue
        pending.append((int(idx), url, str(row["HEADLINE"]), str(row.get("SYMBOL", "")).upper().strip(), str(row.get("PUBLISHED_AT", "")))

    def verify_one(item):
        idx, url, headline, symbol, published_at = item
        resolved_url = url
        try:
            # Source-linked overrides require exact symbol/date/headline tokens
            # and a downloaded official NSE PDF containing all required tokens.
            if not overrides.empty and symbol and published_at:
                published_date = pd.to_datetime(published_at, utc=True, errors="coerce")
                if not pd.isna(published_date):
                    matched = overrides[
                        overrides["SYMBOL"].astype(str).str.upper().eq(symbol)
                        & overrides["PUBLISHED_DATE"].astype(str).eq(published_date.tz_convert("Asia/Kolkata").date().isoformat())
                    ]
                    headline_key = tokens(headline)
                    for _, override in matched.iterrows():
                        required_headline = {x.strip().lower() for x in str(override["HEADLINE_REQUIRED_TOKENS"]).split(";") if x.strip()}
                        if not required_headline.issubset(headline_key):
                            continue
                        official_url = str(override["OFFICIAL_SOURCE_URL"]).strip()
                        if not official_url.startswith("https://nsearchives.nseindia.com/"):
                            continue
                        pdf_response = requests.get(official_url, timeout=(5, 20), allow_redirects=True, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf"})
                        pdf_response.raise_for_status()
                        blob = bytes(pdf_response.content)
                        if not blob.startswith(b"%PDF-"):
                            continue
                        from pypdf import PdfReader
                        import io
                        document_text = " ".join((page.extract_text() or "") for page in PdfReader(io.BytesIO(blob)).pages).lower()
                        required_document = [x.strip().lower() for x in str(override["REQUIRED_DOCUMENT_TOKENS"]).split(";") if x.strip()]
                        if all(token in document_text for token in required_document):
                            return idx, True, "OFFICIAL_NSE_FILING_MATCH", official_url
            host = (urlparse(url).hostname or "").lower()
            if host == "news.google.com" or host.endswith(".news.google.com"):
                if gnewsdecoder is None:
                    raise ValueError("GOOGLE_NEWS_DECODER_UNAVAILABLE")
                decoded = gnewsdecoder(url, interval=1, timeout=15.0)
                if not isinstance(decoded, dict) or not decoded.get("success") or not decoded.get("decoded_url"):
                    message = decoded.get("message", "GOOGLE_NEWS_URL_NOT_DECODED") if isinstance(decoded, dict) else "GOOGLE_NEWS_URL_NOT_DECODED"
                    raise ValueError("GOOGLE_NEWS_URL_NOT_DECODED:" + str(message)[:120])
                resolved_url = str(decoded["decoded_url"]).strip()
                decoded_parts = urlparse(resolved_url)
                if decoded_parts.scheme not in {"http", "https"} or not decoded_parts.hostname:
                    raise ValueError("DECODER_RETURNED_INVALID_PUBLISHER_URL")
                if (decoded_parts.hostname or "").lower().endswith("google.com"):
                    raise ValueError("DECODER_RETURNED_GOOGLE_URL")
            response = requests.get(
                resolved_url, timeout=(5, 12), allow_redirects=True,
                headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"}
            )
            response.raise_for_status()
            final = urlparse(response.url)
            if not final.hostname or final.hostname.lower() == "news.google.com" or final.hostname.lower() == "google.com" or final.hostname.lower().endswith(".google.com"):
                raise ValueError("URL_DID_NOT_RESOLVE_TO_PUBLISHER")
            if "html" not in response.headers.get("Content-Type", "").lower():
                raise ValueError("PUBLISHER_RESPONSE_NOT_HTML")
            parser = PageMeta()
            parser.feed(response.text[:300000])
            page_title = parser.best_title()
            headline_tokens = tokens(headline)
            page_tokens = tokens(page_title)
            if len(headline_tokens) < 3:
                raise ValueError("HEADLINE_TOO_SHORT_FOR_VERIFICATION")
            overlap = len(headline_tokens & page_tokens) / len(headline_tokens)
            if not page_title or overlap < 0.50:
                raise ValueError("PUBLISHER_TITLE_MISMATCH")
            return idx, True, "", response.url
        except Exception as exc:
            return idx, False, f"{type(exc).__name__}:{str(exc)[:180]}", resolved_url

    checked = verified = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(verify_one, item) for item in pending]
        for future in as_completed(futures):
            idx, ok, reason, resolved_url = future.result()
            checked += 1
            if ok:
                df.at[idx, "CANONICAL_URL"] = resolved_url
                df.at[idx, "VERIFICATION_STATUS"] = "VERIFIED"
                if reason == "OFFICIAL_NSE_FILING_MATCH":
                    df.at[idx, "PUBLISHER"] = "NSE India"
                    df.at[idx, "SOURCE_TYPE"] = "OFFICIAL_EXCHANGE_FILING"
                verified += 1
            else:
                failures.append({"row": idx, "reason": reason})
    df.to_csv(NEWS, index=False)
    remaining = int(df["VERIFICATION_STATUS"].astype(str).str.upper().ne("VERIFIED").sum())
    report = {
        "status": "PASS" if remaining == 0 else "PARTIAL_VERIFICATION",
        "checked_rows": checked, "newly_verified_rows": verified,
        "verified_rows_total": int(df["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()),
        "unverified_rows_remaining": remaining,
        "verification_rule": "Decode Google News RSS article URL to publisher URL when needed; then require HTTP 200 publisher HTML after redirects, non-Google final host, page title token overlap >= 0.50; max 8 concurrent requests",
        "url_resolution": "Google News article links are decoded with googlenewsdecoder; canonical URL is replaced only after publisher-page and headline verification passes.",
        "failure_samples": failures[:20],
        "note": "Failed or ambiguous rows remain UNVERIFIED; verification never fabricates evidence."
    }
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("NEWS_SOURCE_VERIFICATION=" + json.dumps(report, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
