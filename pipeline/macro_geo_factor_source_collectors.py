#!/usr/bin/env python3
"""Bounded, provenance-preserving collectors for factor-registry source gaps.

This first repair batch covers US Treasury yields and global commodity prices
using public FRED observation CSVs. It deliberately does not infer release
timestamps from observation dates. Missing/invalid series remain UNKNOWN and
are reported as BLOCKED; no synthetic rows are written.
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from io import StringIO
from pathlib import Path
import json
import os
import xml.etree.ElementTree as ET

import pandas as pd
import requests

ROOT = Path(".")
PANEL_CANDIDATES = (
    ROOT / "data/processed/nse_eq_200_sessions.csv",
    ROOT / "data/external/benchmark_indices.csv",
)
OUT = ROOT / "data/external"
REPORT = ROOT / "outputs/macro_geo/factor_source_collection_report.json"
UA = "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (research audit; public data)"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"

# FRED series IDs are explicit and auditable. The WTI series is not relabelled
# as Brent; the commodity name is preserved in the output.
YIELD_SERIES = {"DGS2": "US_TREASURY_2Y", "DGS10": "US_TREASURY_10Y", "DGS30": "US_TREASURY_30Y"}
COMMODITY_SERIES = {"DCOILWTICO": "WTI_CRUDE_USD_PER_BBL", "GOLDAMGBD228NLBM": "GOLD_USD_PER_TROY_OUNCE"}
POLICY_FEEDS = [
    ("https://www.federalreserve.gov/feeds/press_all.xml", "United States", "FEDERAL_RESERVE"),
    ("https://www.ecb.europa.eu/rss/press.html", "Euro Area", "EUROPEAN_CENTRAL_BANK"),
]
POLICY_TERMS = ("monetary policy", "policy rate", "interest rate", "rate decision",
                "fomc", "policy statement", "key interest rates", "monetary-policy")


def observed_window():
    panel = next((p for p in PANEL_CANDIDATES if p.exists()), None)
    if panel is None:
        raise RuntimeError("No observed NSE equity or benchmark panel; refusing wall-clock-only collection window")
    frame = pd.read_csv(panel)
    date_col = next((c for c in frame.columns if str(c).strip().upper() == "DATE"), None)
    if date_col is None:
        raise RuntimeError(f"Panel has no DATE column: {panel}")
    dates = pd.to_datetime(frame[date_col], errors="coerce").dropna()
    if dates.empty:
        raise RuntimeError(f"Panel has no valid observed dates: {panel}")
    sessions = sorted(dates.dt.date.unique())
    return max(datetime(1990, 1, 1).date(), sessions[-min(200, len(sessions))] - timedelta(days=30)), min(
        datetime.now(timezone.utc).date(), sessions[-1] + timedelta(days=3)
    ), str(panel)


def fetch_fred(session, series_id, start, end):
    params = {"id": series_id, "cosd": start.isoformat(), "coed": end.isoformat()}
    response = session.get(FRED_URL, params=params, timeout=(8, 25))
    response.raise_for_status()
    frame = pd.read_csv(StringIO(response.content.decode("utf-8-sig", errors="replace")))
    frame.columns = [str(c).strip().upper() for c in frame.columns]
    date_col = next((c for c in ("DATE", "OBSERVATION_DATE") if c in frame.columns), None)
    if date_col is None or series_id.upper() not in frame.columns:
        raise ValueError(f"FRED schema mismatch for {series_id}: {list(frame.columns)}")
    dates = pd.to_datetime(frame[date_col], errors="coerce")
    values = pd.to_numeric(frame[series_id.upper()], errors="coerce")
    rows = []
    for i in range(len(frame)):
        if pd.isna(dates.iloc[i]) or pd.isna(values.iloc[i]):
            continue
        day = dates.iloc[i].date()
        if start <= day <= end:
            rows.append((day.isoformat(), float(values.iloc[i]), response.url))
    if not rows:
        raise ValueError(f"FRED returned no valid observations for {series_id} in {start}..{end}")
    return rows


def fetch_treasury_yields(session, start, end):
    """Use the official US Treasury CSV export as an exact-source fallback for yields."""
    rows = []
    url_template = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
                    "daily-treasury-rates.csv/{year}/all")
    tenor_map = {"2 YR": "US_TREASURY_2Y", "10 YR": "US_TREASURY_10Y", "30 YR": "US_TREASURY_30Y"}
    for year in range(start.year, end.year + 1):
        url = url_template.format(year=year)
        response = session.get(url, params={"type": "daily_treasury_yield_curve",
                              "field_tdr_date_value": str(year), "page": "", "_format": "csv"},
                              timeout=(8, 25))
        response.raise_for_status()
        frame = pd.read_csv(StringIO(response.content.decode("utf-8-sig", errors="replace")))
        frame.columns = [str(col).strip().upper() for col in frame.columns]
        date_col = next((col for col in ("DATE", "RECORD DATE") if col in frame.columns), None)
        if date_col is None or not set(tenor_map).issubset(frame.columns):
            raise ValueError(f"US Treasury CSV schema mismatch for {year}: {list(frame.columns)}")
        dates = pd.to_datetime(frame[date_col], errors="coerce")
        for tenor, label in tenor_map.items():
            values = pd.to_numeric(frame[tenor], errors="coerce")
            for i in range(len(frame)):
                if pd.isna(dates.iloc[i]) or pd.isna(values.iloc[i]):
                    continue
                day = dates.iloc[i].date()
                if start <= day <= end:
                    rows.append({"DATE": day.isoformat(), "SERIES": label, "CLOSE": float(values.iloc[i]),
                                 "SOURCE": "US Department of the Treasury",
                                 "SOURCE_SERIES": tenor, "SOURCE_URL": response.url,
                                 "OBSERVED_AT_UTC": datetime.now(timezone.utc).isoformat()})
    if not rows:
        raise ValueError(f"US Treasury returned no valid yield observations in {start}..{end}")
    return rows


def fetch_dxy_yahoo(session, start, end):
    """Fetch the ICE US Dollar Index ticker from Yahoo Finance; keep provider explicit."""
    period1 = int(datetime.combine(start, datetime.min.time(), tzinfo=timezone.utc).timestamp())
    period2 = int(datetime.combine(end + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp())
    base = "https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB"
    response = session.get(base, params={"period1": period1, "period2": period2, "interval": "1d",
                                         "events": "history"}, timeout=(8, 20))
    response.raise_for_status()
    payload = response.json()
    result = (((payload.get("chart") or {}).get("result") or [None])[0])
    if not result:
        error = (payload.get("chart") or {}).get("error")
        raise ValueError(f"Yahoo chart returned no result: {error}")
    timestamps = result.get("timestamp") or []
    quotes = (((result.get("indicators") or {}).get("quote") or [{}])[0])
    closes = quotes.get("close") or []
    tz_name = (result.get("meta") or {}).get("exchangeTimezoneName") or "UTC"
    tz = ZoneInfo(tz_name)
    rows = []
    for ts, value in zip(timestamps, closes):
        if value is None:
            continue
        day = datetime.fromtimestamp(int(ts), tz=tz).date()
        if start <= day <= end:
            rows.append({"DATE": day.isoformat(), "CLOSE": float(value),
                         "SOURCE": "Yahoo Finance chart API; ICE US Dollar Index ticker",
                         "SOURCE_SERIES": "DX-Y.NYB", "SOURCE_URL": response.url,
                         "OBSERVED_AT_UTC": datetime.now(timezone.utc).isoformat()})
    if not rows:
        raise ValueError(f"Yahoo returned no valid DXY observations in {start}..{end}")
    frame = pd.DataFrame(rows).drop_duplicates(["DATE"]).sort_values("DATE")
    target = OUT / "dxy.csv"
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    frame.to_csv(tmp, index=False)
    os.replace(tmp, target)
    return {"status": "COLLECTED_NEEDS_DOMAIN_QA", "rows": int(len(frame)),
            "date_min": str(frame["DATE"].min()), "date_max": str(frame["DATE"].max()),
            "path": str(target), "source": "Yahoo Finance chart API; ICE US Dollar Index ticker",
            "observed_source_series": ["DX-Y.NYB"], "source_urls": sorted(set(frame["SOURCE_URL"])),
            "notes": "Third-party market-data mirror; verify licensing, exact index definition, units and point-in-time suitability before use."}


def fetch_global_policy_events(session, start, end):
    """Collect official central-bank feed items; publication date is explicitly only a proxy."""
    rows, failures = [], {}
    for feed_url, country, source_name in POLICY_FEEDS:
        try:
            response = session.get(feed_url, timeout=(8, 20))
            response.raise_for_status()
            root = ET.fromstring(response.content)
            for entry in root.iter():
                fields = {}
                for child in list(entry):
                    key = child.tag.rsplit("}", 1)[-1].lower()
                    text = "".join(child.itertext()).strip()
                    if key == "link":
                        link_value = child.attrib.get("href") or text
                        if link_value:
                            fields["link"] = link_value.strip()
                    elif key in ("title", "pubdate", "published", "updated", "date", "issued"):
                        fields[key] = text
                title = fields.get("title", "")
                if not title or not any(term in title.lower() for term in POLICY_TERMS):
                    continue
                published_raw = next((fields[k] for k in ("pubdate", "published", "updated", "date", "issued") if fields.get(k)), "")
                published = pd.to_datetime(published_raw, errors="coerce", utc=True)
                article_url = fields.get("link", "")
                if pd.isna(published) or not (start <= published.date() <= end):
                    continue
                if not article_url.startswith("https://"):
                    continue
                rows.append({
                    "EVENT_DATE": published.date().isoformat(),
                    "PUBLISHED_AT": published.isoformat(),
                    "COUNTRY": country,
                    "EVENT_TYPE": source_name + "_POLICY_RELEASE_PUBLICATION_DATE_PROXY",
                    "SOURCE_URL": article_url,
                    "SOURCE": source_name,
                    "TITLE": title,
                    "FEED_URL": response.url,
                    "EVENT_DATE_BASIS": "PUBLICATION_DATE_PROXY_NOT_CONFIRMED_EVENT_DATE",
                    "OBSERVED_AT_UTC": datetime.now(timezone.utc).isoformat(),
                })
        except Exception as exc:
            failures[feed_url] = f"{type(exc).__name__}: {str(exc)[:220]}"
    frame = pd.DataFrame(rows)
    if not frame.empty:
        frame = frame.drop_duplicates(["PUBLISHED_AT", "SOURCE_URL"]).sort_values("PUBLISHED_AT")
        OUT.mkdir(parents=True, exist_ok=True)
        target = OUT / "global_policy_events.csv"
        tmp = target.with_suffix(target.suffix + ".tmp")
        frame.to_csv(tmp, index=False)
        os.replace(tmp, target)
        return {"status": "COLLECTED_NEEDS_DOMAIN_QA", "rows": int(len(frame)),
                "date_min": str(frame["EVENT_DATE"].min()), "date_max": str(frame["EVENT_DATE"].max()),
                "path": str(target), "source": "Official Federal Reserve and ECB RSS feeds",
                "failures": failures,
                "notes": "Publication date is not assumed to be the actual policy decision date; event-study eligibility requires independent date validation."}
    return {"status": "BLOCKED", "rows": 0, "failures": failures,
            "notes": "No valid policy feed events found; missing event data remains UNKNOWN."}


def collect_group(name, series_map, start, end, session):
    rows, failures = [], {}
    for series_id, label in series_map.items():
        try:
            for day, value, url in fetch_fred(session, series_id, start, end):
                common = {"DATE": day, "SOURCE": "Federal Reserve Bank of St. Louis FRED",
                          "SOURCE_SERIES": series_id, "SOURCE_URL": url,
                          "OBSERVED_AT_UTC": datetime.now(timezone.utc).isoformat()}
                if name == "us_yields":
                    rows.append({**common, "SERIES": label, "CLOSE": value})
                else:
                    rows.append({**common, "COMMODITY": label, "CLOSE": value})
        except Exception as exc:
            failures[series_id] = f"{type(exc).__name__}: {str(exc)[:240]}"
    if name == "us_yields" and failures:
        # Do not mix partially fetched FRED rows with Treasury observations.
        # If any FRED maturity failed, replace the whole group from one official source.
        try:
            rows = fetch_treasury_yields(session, start, end)
            failures = {}
        except Exception as exc:
            failures["TREASURY_OFFICIAL_FALLBACK"] = f"{type(exc).__name__}: {str(exc)[:240]}"
    if not rows:
        return {"status": "BLOCKED", "rows": 0, "failures": failures,
                "notes": "No valid source observations; missing data remains UNKNOWN."}
    key = ["DATE", "SERIES"] if name == "us_yields" else ["DATE", "COMMODITY"]
    frame = pd.DataFrame(rows).drop_duplicates(key).sort_values(key)
    target = OUT / ("us_yields.csv" if name == "us_yields" else "commodity_prices.csv")
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    frame.to_csv(tmp, index=False)
    os.replace(tmp, target)
    return {"status": "AVAILABLE_WITH_SOURCE_FAILURES" if failures else "COLLECTED_NEEDS_DOMAIN_QA",
            "rows": int(len(frame)), "date_min": str(frame["DATE"].min()),
            "date_max": str(frame["DATE"].max()), "path": str(target),
            "source": sorted(set(frame["SOURCE"].astype(str))),
            "observed_source_series": sorted(set(frame["SOURCE_SERIES"].astype(str))),
            "requested_fred_series_ids": list(series_map),
            "failures": failures,
            "provenance_columns": ["SOURCE", "SOURCE_SERIES", "SOURCE_URL", "OBSERVED_AT_UTC"],
            "notes": "Collection is not proof of official-source authenticity, point-in-time release timing, or factor validity."}


def main():
    report = {"observed_at_utc": datetime.now(timezone.utc).isoformat(), "groups": {},
              "policy": "Only observed public source values are written; failed series remain UNKNOWN."}
    try:
        start, end, panel = observed_window()
        report["window"] = {"start": start.isoformat(), "end": end.isoformat(), "basis_panel": panel}
        session = requests.Session()
        session.headers.update({"User-Agent": UA, "Accept": "text/csv,*/*"})
        report["groups"]["us_yields"] = collect_group("us_yields", YIELD_SERIES, start, end, session)
        report["groups"]["global_commodity_prices"] = collect_group("global_commodity_prices", COMMODITY_SERIES, start, end, session)
        try:
            report["groups"]["dxy"] = fetch_dxy_yahoo(session, start, end)
        except Exception as exc:
            report["groups"]["dxy"] = {"status": "BLOCKED", "rows": 0,
                                       "error": f"{type(exc).__name__}: {str(exc)[:240]}",
                                       "notes": "No validated DXY rows; missing data remains UNKNOWN."}
        report["groups"]["global_policy_events"] = fetch_global_policy_events(session, start, end)
    except Exception as exc:
        report["window"] = {"status": "BLOCKED", "error": f"{type(exc).__name__}: {str(exc)[:240]}"}
        for name in ("us_yields", "global_commodity_prices", "global_policy_events", "dxy"):
            report["groups"][name] = {"status": "BLOCKED", "rows": 0,
                                      "notes": "No rows written; missing data remains UNKNOWN."}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    if not any(g.get("rows", 0) > 0 for g in report["groups"].values()):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
