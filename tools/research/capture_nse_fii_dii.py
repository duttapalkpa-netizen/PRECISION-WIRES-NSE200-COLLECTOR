#!/usr/bin/env python3
"""One-off research capture for NSE FII/DII. Never imports production pipeline code.

Usage:
  python tools/research/capture_nse_fii_dii.py --out-dir /tmp/nse-fii-dii-capture

Only public NSE endpoints are requested. Cookies/session headers are never written.
Raw response bytes and both official CSV files are kept locally; do not commit them
unless repository data-retention policy explicitly permits it.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

BASE = "https://www.nseindia.com"
REPORT = "https://www.nseindia.in/reports/fii-dii"
API = BASE + "/api/fiidiiTradeReact"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
TIMEOUT = (10, 25)

class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items, self.href, self.text = [], None, []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self.href = dict(attrs).get("href")
            self.text = []
    def handle_data(self, data):
        if self.href is not None:
            self.text.append(data)
    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.href is not None:
            self.items.append((self.href, " ".join(" ".join(self.text).split())))
            self.href, self.text = None, []

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_nse_url(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host == "nseindia.com" or host.endswith(".nseindia.com") or host == "nseindia.in" or host.endswith(".nseindia.in")

def write_bytes(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"path": str(path), "bytes": len(data), "sha256": sha(data)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True, help="Local output directory; do not commit raw captures")
    args = ap.parse_args()
    out = Path(args.out_dir).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": UA, "Accept": "text/html,application/json,text/csv,*/*",
                            "Referer": REPORT})
    started = datetime.now(timezone.utc).isoformat()
    result = {"status": "ACCESS_BLOCKED", "started_at": started, "report_url": REPORT,
              "api_url": API, "captures": {}, "errors": []}

    try:
        page = session.get(REPORT, timeout=TIMEOUT)
        page.raise_for_status()
        page_bytes = page.content
        result["captures"]["report_html"] = write_bytes(out / "nse_fii_dii_report.html", page_bytes)
        parser = AnchorParser()
        parser.feed(page.text)
        choices = []
        for href, label in parser.items:
            low = label.lower()
            if "capital market" not in low:
                continue
            if not ("fii" in low or "dii" in low):
                continue
            url = urljoin(REPORT, href)
            if safe_nse_url(url):
                scope = "combined_nse_bse_msei" if all(x in low for x in ("nse", "bse", "msei")) else "nse_only" if "nse" in low else "unclassified"
                choices.append({"label": label, "url": url, "scope": scope})
        # Keep one link per explicit scope; never guess if page extraction is ambiguous.
        by_scope = {}
        for item in choices:
            if item["scope"] in ("nse_only", "combined_nse_bse_msei"):
                by_scope.setdefault(item["scope"], item)
        if set(by_scope) != {"nse_only", "combined_nse_bse_msei"}:
            raise RuntimeError("Could not resolve two distinct official CSV links from report HTML; manual review required")
        if by_scope["nse_only"]["url"] == by_scope["combined_nse_bse_msei"]["url"]:
            raise RuntimeError("Official report controls resolved to the same URL; refusing ambiguous capture")
        result["official_csv_links"] = by_scope

        # Session bootstrap through the public NSE homepage, then exact API request.
        session.get(BASE + "/", timeout=TIMEOUT).raise_for_status()
        api = session.get(API, timeout=TIMEOUT, headers={"Accept": "application/json"})
        api.raise_for_status()
        raw = api.content
        result["captures"]["api_raw"] = write_bytes(out / "fiidiiTradeReact.raw.json", raw)
        parsed = api.json()
        parsed_bytes = json.dumps(parsed, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8")
        result["captures"]["api_parsed"] = write_bytes(out / "fiidiiTradeReact.parsed.json", parsed_bytes)
        result["api_http_status"] = api.status_code
        result["api_content_type"] = api.headers.get("Content-Type", "")
        result["api_top_level_type"] = type(parsed).__name__

        for scope, item in by_scope.items():
            resp = session.get(item["url"], timeout=TIMEOUT)
            resp.raise_for_status()
            suffix = ".csv" if "csv" in resp.headers.get("Content-Type", "").lower() or resp.content[:4096].count(b",") else ".bin"
            result["captures"][scope] = write_bytes(out / (scope + suffix), resp.content)
            result.setdefault("csv_http", {})[scope] = {
                "status": resp.status_code, "content_type": resp.headers.get("Content-Type", ""),
                "label": item["label"], "url": item["url"]
            }

        result["status"] = "CAPTURED"
    except Exception as exc:
        # Do not serialize request headers/cookies or exception objects that may contain secrets.
        result["errors"].append(type(exc).__name__ + ": " + str(exc)[:300])
    finally:
        result["completed_at"] = datetime.now(timezone.utc).isoformat()
        manifest = out / "capture_manifest.json"
        manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"status": result["status"], "out_dir": str(out),
                          "capture_names": sorted(result["captures"]),
                          "errors": result["errors"],
                          "manifest": str(manifest)}, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "CAPTURED" else 2

if __name__ == "__main__":
    raise SystemExit(main())
