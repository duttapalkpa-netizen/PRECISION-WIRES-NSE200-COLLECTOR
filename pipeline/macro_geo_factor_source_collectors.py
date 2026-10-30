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

# Independently reviewed official decision/communication pages. Exact URL matching
# prevents RSS publication dates from being silently promoted to event dates.
# Unknown/new pages remain publication-date proxies until separately reviewed.
OFFICIAL_POLICY_EVENT_DATES = {
    "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm":
        {"event_date": "2026-09-16", "event_type": "FED_FOMC_POLICY_STATEMENT"},
    "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm":
        {"event_date": "2026-10-28", "event_type": "FED_FOMC_POLICY_STATEMENT"},
    "https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html":
        {"event_date": "2026-10-29", "event_type": "ECB_MONETARY_POLICY_DECISION"},
    "https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is261029~5c5ffe99e5.en.html":
        {"event_date": "2026-10-29", "event_type": "ECB_POLICY_PRESS_CONFERENCE"},
}


def validate_official_policy_event_date(article_url):
    """Return reviewed evidence for an exact official page after safe URL normalization."""
    from urllib.parse import urlsplit, urlunsplit
    raw = str(article_url).strip()
    parts = urlsplit(raw)
    # Normalize repeated path separators only; scheme, host, path and query
    # remain constrained by the exact reviewed allowlist below.
    normalized_path = "/" + "/".join(part for part in parts.path.split("/") if part)
    canonical = urlunsplit((parts.scheme.lower(), parts.netloc.lower(), normalized_path, parts.query, ""))
    item = OFFICIAL_POLICY_EVENT_DATES.get(canonical)
    if not item:
        return None
    return {
        "event_date": item["event_date"],
        "event_type": item["event_type"],
        "validation_method": "EXACT_MATCH_TO_INDEPENDENTLY_REVIEWED_OFFICIAL_EVENT_PAGE",
        "validation_source_url": canonical,
    }



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
    """Fetch a FRED series in bounded monthly chunks with resilient retries.

    Transport failures receive three bounded attempts with backoff. Schema and
    data-contract failures fail closed immediately. Failed chunks are never
    silently omitted and only observed non-missing values are returned.
    """
    from calendar import monthrange
    chunks = []
    cursor = start.replace(day=1)
    while cursor <= end:
        last_day = monthrange(cursor.year, cursor.month)[1]
        chunk_end = min(end, cursor.replace(day=last_day))
        # Three-month windows, bounded independently for resilient retries.
        chunks.append((max(start, cursor), chunk_end))
        if cursor.month >= 10:
            cursor = cursor.replace(year=cursor.year + 1, month=1)
        else:
            cursor = cursor.replace(month=cursor.month + 1)
        # group monthly windows below into quarters
    # Keep each request to one calendar month. Quarterly aggregation caused
    # repeated commodity-series read timeouts; monthly bounds reduce payload size
    # without changing series identity or treating missing observations as zero.
    rows, failures = [], []
    for chunk_start, chunk_end in chunks:
        last_error = None
        for attempt in range(3):
            try:
                response = session.get(
                    FRED_URL,
                    params={"id": series_id, "cosd": chunk_start.isoformat(), "coed": chunk_end.isoformat()},
                    timeout=(5, 12),
                )
                response.raise_for_status()
                frame = pd.read_csv(StringIO(response.content.decode("utf-8-sig", errors="replace")))
                frame.columns = [str(c).strip().upper() for c in frame.columns]
                date_col = next((c for c in ("DATE", "OBSERVATION_DATE") if c in frame.columns), None)
                if date_col is None or series_id.upper() not in frame.columns:
                    raise ValueError(f"FRED schema mismatch for {series_id}: {list(frame.columns)}")
                dates = pd.to_datetime(frame[date_col], errors="coerce")
                values = pd.to_numeric(frame[series_id.upper()], errors="coerce")
                got = []
                for i in range(len(frame)):
                    if pd.isna(dates.iloc[i]) or pd.isna(values.iloc[i]):
                        continue
                    day = dates.iloc[i].date()
                    if chunk_start <= day <= chunk_end:
                        got.append((day.isoformat(), float(values.iloc[i]), response.url))
                if not got:
                    raise ValueError(f"no valid observations for {series_id} in {chunk_start}..{chunk_end}")
                rows.extend(got)
                last_error = None
                break
            except ValueError:
                # Schema/data-contract failures are deterministic and must fail
                # closed immediately; retry only transport/server exceptions.
                raise
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {str(exc)[:180]}"
                if attempt < 2:
                    import time
                    # Small bounded backoff: enough to clear transient upstream
                    # throttling without allowing a retry storm or unbounded run.
                    time.sleep(0.5 * (attempt + 1))
        if last_error:
            failures.append(f"{chunk_start}..{chunk_end}: {last_error}")
    if failures:
        raise RuntimeError(f"FRED {series_id} failed {len(failures)}/{len(chunks)} monthly chunks: " + " | ".join(failures[:3]))
    if not rows:
        raise ValueError(f"FRED returned no valid observations for {series_id} in {start}..{end}")
    return sorted({row[0]: row for row in rows}.values(), key=lambda row: row[0])


def fetch_commodity_fallback(session, series_id, label, start, end):
    """Use exact-identity public source fallbacks for WTI spot and LBMA gold AM.

    WTI: US EIA official daily XLS (RWTCd.xls). Gold: LBMA published AM-price
    JSON (USD/troy ounce). Neither series is substituted with a futures proxy.
    """
    observed = datetime.now(timezone.utc).isoformat()
    rows = []
    if series_id == "DCOILWTICO":
        url = "https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls"
        response = session.get(url, timeout=(8, 35))
        response.raise_for_status()
        from io import BytesIO
        book = pd.ExcelFile(BytesIO(response.content), engine="xlrd")
        found = None
        for sheet in book.sheet_names:
            raw = pd.read_excel(book, sheet_name=sheet, header=None)
            for i in range(min(15, len(raw))):
                vals = [str(v).strip().lower() for v in raw.iloc[i].tolist()]
                if any(v == "date" for v in vals) and any("cushing" in v and "spot price" in v for v in vals):
                    found = (raw, i)
                    break
            if found:
                break
        if not found:
            raise ValueError("EIA RWTC workbook schema not recognized for WTI Cushing spot")
        raw, header_row = found
        headers = [str(v).strip() for v in raw.iloc[header_row].tolist()]
        frame = raw.iloc[header_row + 1:].copy()
        frame.columns = headers
        date_col = next((x for x in frame.columns if str(x).strip().lower() == "date"), None)
        value_col = next((x for x in frame.columns if "cushing" in str(x).lower() and "spot price" in str(x).lower()), None)
        if date_col is None or value_col is None:
            raise ValueError("EIA RWTC workbook missing Date or WTI Cushing spot-price column")
        for _, row in frame.iterrows():
            day = pd.to_datetime(row[date_col], errors="coerce")
            value = pd.to_numeric(pd.Series([row[value_col]]), errors="coerce").iloc[0]
            if pd.notna(day) and pd.notna(value) and start <= day.date() <= end:
                rows.append({"DATE": day.date().isoformat(), "CLOSE": float(value),
                    "SOURCE": "US Energy Information Administration (official daily XLS)",
                    "SOURCE_SERIES": "RWTC", "SOURCE_URL": url,
                    "OBSERVED_AT_UTC": observed, "COMMODITY": label})
    elif series_id == "GOLDAMGBD228NLBM":
        url = "https://prices.lbma.org.uk/json/gold_am.json"
        response = session.get(url, timeout=(8, 25))
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, list):
            raise ValueError("LBMA gold AM response must be a JSON list")
        for item in payload:
            if not isinstance(item, dict) or "d" not in item or "v" not in item:
                raise ValueError("LBMA gold AM schema mismatch: expected d/v records")
            day = pd.to_datetime(item["d"], errors="coerce")
            values = item["v"]
            if pd.isna(day) or not isinstance(values, list) or len(values) < 1:
                continue
            value = pd.to_numeric(pd.Series([values[0]]), errors="coerce").iloc[0]
            if pd.notna(value) and start <= day.date() <= end:
                rows.append({"DATE": day.date().isoformat(), "CLOSE": float(value),
                    "SOURCE": "London Bullion Market Association (LBMA) gold AM price",
                    "SOURCE_SERIES": "LBMA_GOLD_AM_USD", "SOURCE_URL": url,
                    "OBSERVED_AT_UTC": observed, "COMMODITY": label})
    else:
        raise ValueError(f"No approved exact-identity fallback for {series_id}")
    if not rows:
        raise ValueError(f"Approved fallback returned no valid observations for {series_id} in {start}..{end}")
    frame = pd.DataFrame(rows).drop_duplicates(["DATE", "COMMODITY"]).sort_values(["DATE", "COMMODITY"])
    dates = pd.to_datetime(frame["DATE"], errors="coerce")
    values = pd.to_numeric(frame["CLOSE"], errors="coerce")
    if dates.isna().any() or values.isna().any() or (values <= 0).any():
        raise ValueError(f"Fallback domain QA failed for {series_id}: invalid date/value")
    if frame["SOURCE_URL"].astype(str).str.strip().eq("").any() or frame["OBSERVED_AT_UTC"].astype(str).str.strip().eq("").any():
        raise ValueError(f"Fallback domain QA failed for {series_id}: missing provenance")
    if frame.duplicated(["DATE", "COMMODITY"]).any() or dates.min().date() < start or dates.max().date() > end:
        raise ValueError(f"Fallback domain QA failed for {series_id}: duplicate keys or out-of-window dates")
    age = (end - dates.max().date()).days
    if age < 0 or age > 5:
        raise ValueError(f"Fallback domain QA failed for {series_id}: latest observation age {age} exceeds 5 days")
    expected_source = "US Energy Information Administration" if series_id == "DCOILWTICO" else "London Bullion Market Association"
    if not frame["SOURCE"].astype(str).str.contains(expected_source, regex=False).all():
        raise ValueError(f"Fallback domain QA failed for {series_id}: source identity mismatch")
    return frame.to_dict("records"), {"source": expected_source, "source_series": str(frame["SOURCE_SERIES"].iloc[0]),
        "url": url, "rows": int(len(frame)), "date_min": str(frame["DATE"].min()),
        "date_max": str(frame["DATE"].max()), "freshness_age_calendar_days": age,
        "domain_qa_checks": ["exact source identity", "schema validation", "positive numeric values",
            "unique date/commodity keys", "requested-window bounds", "source URL and observed timestamp",
            "freshness <= 5 calendar days"]}



def fetch_world_bank_monthly_gold(session, start, end):
    """Collect monthly World Bank Pink Sheet gold; never present it as daily LBMA spot."""
    import re
    from urllib.parse import urljoin
    landing = "https://www.worldbank.org/en/research/commodity-markets"
    page = session.get(landing, timeout=(8, 25))
    page.raise_for_status()
    html = page.text
    matches = re.findall(r"""href=["']([^"']*CMO-Historical-Data-Monthly\.xlsx[^"']*)["']""", html, flags=re.I)
    urls = [urljoin(landing, item.replace("&amp;", "&")) for item in matches]
    url = next((u for u in urls if u.startswith("https://thedocs.worldbank.org/") and
                "/related/CMO-Historical-Data-Monthly.xlsx" in u), None)
    if not url:
        raise ValueError("World Bank landing page did not expose an approved monthly Pink Sheet workbook URL")
    response = session.get(url, timeout=(8, 45))
    response.raise_for_status()
    frame = pd.read_excel(BytesIO(response.content), sheet_name="Monthly Prices", skiprows=4)
    frame.columns = [str(col).strip().upper() for col in frame.columns]
    if frame.empty or "GOLD" not in frame.columns:
        raise ValueError(f"World Bank monthly workbook schema mismatch: {list(frame.columns)[:20]}")
    period_col = frame.columns[0]
    rows = []
    observed = datetime.now(timezone.utc).isoformat()
    for _, row in frame.iterrows():
        raw_period = str(row.get(period_col, "")).strip()
        match = re.fullmatch(r"(\d{4})M(\d{1,2})", raw_period, flags=re.I)
        if not match:
            continue
        year, month = int(match.group(1)), int(match.group(2))
        if not 1 <= month <= 12:
            continue
        period = datetime(year, month, 1).date()
        value = pd.to_numeric(pd.Series([row.get("GOLD")]), errors="coerce").iloc[0]
        if pd.notna(value) and start <= period <= end:
            rows.append({"DATE": period.isoformat(), "CLOSE": float(value),
                         "UNIT": "USD_PER_TROY_OUNCE", "FREQUENCY": "MONTHLY",
                         "SOURCE": "World Bank Prospects Group Pink Sheet",
                         "SOURCE_SERIES": "GOLD", "SOURCE_URL": url,
                         "OBSERVED_AT_UTC": observed,
                         "REVISION_POLICY": "MONTHLY_SOURCE_REVISIONS_POSSIBLE"})
    if not rows:
        raise ValueError("World Bank monthly Pink Sheet returned no valid GOLD observations in requested window")
    out = pd.DataFrame(rows).drop_duplicates(["DATE"]).sort_values("DATE")
    dates = pd.to_datetime(out["DATE"], errors="coerce")
    values = pd.to_numeric(out["CLOSE"], errors="coerce")
    if dates.isna().any() or values.isna().any() or (values <= 0).any() or out["SOURCE_URL"].eq("").any():
        raise ValueError("World Bank monthly gold domain QA failed: invalid date/value/provenance")
    last_period_end = dates.max() + pd.offsets.MonthEnd(0)
    freshness_days = int((pd.Timestamp(end) - last_period_end.date()).days)
    if freshness_days < 0 or freshness_days > 45:
        raise ValueError(f"World Bank monthly gold freshness failed: {freshness_days} days since month-end")
    target = OUT / "gold_prices_monthly.csv"
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    out.to_csv(tmp, index=False)
    os.replace(tmp, target)
    return {"status": "COLLECTED_MONTHLY_DOMAIN_QA_PASSED", "rows": int(len(out)),
            "date_min": str(out["DATE"].min()), "date_max": str(out["DATE"].max()),
            "freshness_age_calendar_days": freshness_days, "path": str(target),
            "source": "World Bank Prospects Group Pink Sheet", "observed_source_series": ["GOLD"],
            "frequency": "MONTHLY", "unit": "USD_PER_TROY_OUNCE", "url": url,
            "revision_policy": "MONTHLY_SOURCE_REVISIONS_POSSIBLE",
            "domain_qa_checks": ["official World Bank landing-page link", "exact GOLD column",
                "monthly period parsing", "positive numeric values", "unique monthly keys",
                "source URL and observation timestamp", "month-end freshness <= 45 days"]}



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
    if not isinstance(payload, dict):
        raise ValueError(f"Yahoo chart response must be a JSON object, got {type(payload).__name__}")
    chart = payload.get("chart")
    if not isinstance(chart, dict):
        raise ValueError(f"Yahoo chart response missing chart object; keys={list(payload)[:20]}")
    raw_results = chart.get("result")
    if not isinstance(raw_results, list) or not raw_results:
        raise ValueError(f"Yahoo chart returned no result: {chart.get('error')}")
    result = raw_results[0]
    if not isinstance(result, dict):
        raise ValueError(f"Yahoo chart result must be an object, got {type(result).__name__}")
    timestamps = result.get("timestamp") or []
    indicators = result.get("indicators")
    if not isinstance(indicators, dict):
        raise ValueError("Yahoo chart result has no indicators object")
    quote_list = indicators.get("quote")
    if not isinstance(quote_list, list) or not quote_list or not isinstance(quote_list[0], dict):
        raise ValueError("Yahoo chart result has no valid quote array")
    closes = quote_list[0].get("close") or []
    meta = result.get("meta") or {}
    tz_name = meta.get("exchangeTimezoneName") if isinstance(meta, dict) else None
    tz_name = tz_name or "UTC"
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
    # Bounded data-domain QA: this clears observed-series integrity only, not
    # licensing review or suitability as a point-in-time trading signal.
    parsed_dates = pd.to_datetime(frame["DATE"], errors="coerce")
    numeric = pd.to_numeric(frame["CLOSE"], errors="coerce")
    if parsed_dates.isna().any() or numeric.isna().any() or ((numeric < 50) | (numeric > 180)).any():
        raise ValueError("DXY domain QA failed: invalid date/value or close outside conservative 50..180 index bounds")
    if frame["SOURCE_SERIES"].astype(str).ne("DX-Y.NYB").any():
        raise ValueError("DXY domain QA failed: source-series identity changed")
    if frame["SOURCE_URL"].astype(str).str.strip().eq("").any() or frame["OBSERVED_AT_UTC"].astype(str).str.strip().eq("").any():
        raise ValueError("DXY domain QA failed: missing provenance")
    if frame.duplicated(["DATE"]).any():
        raise ValueError("DXY domain QA failed: duplicate dates")
    age = (end - parsed_dates.max().date()).days
    if age < 0 or age > 5 or parsed_dates.min().date() < start or parsed_dates.max().date() > end:
        raise ValueError(f"DXY domain QA failed: date bounds/freshness age={age}")
    return {"status": "COLLECTED_AND_DOMAIN_QA_PASSED", "rows": int(len(frame)),
            "date_min": str(frame["DATE"].min()), "date_max": str(frame["DATE"].max()),
            "freshness_age_calendar_days": age,
            "domain_qa_checks": ["DX-Y.NYB identity", "valid dates and 50..180 index bounds",
                "non-empty source URL and observed timestamp", "unique date keys",
                "requested-window bounds", "latest observation age <= 5 calendar days"],
            "path": str(target), "source": "Yahoo Finance chart API; ICE US Dollar Index ticker",
            "observed_source_series": ["DX-Y.NYB"], "source_urls": sorted(set(frame["SOURCE_URL"])),
            "notes": "Observed-series integrity passed. Third-party market-data mirror; licensing review, exact index definition and point-in-time suitability remain separate."}


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
                reviewed = validate_official_policy_event_date(article_url)
                rows.append({
                    "EVENT_DATE": reviewed["event_date"] if reviewed else published.date().isoformat(),
                    "PUBLISHED_AT": published.isoformat(),
                    "COUNTRY": country,
                    "EVENT_TYPE": reviewed["event_type"] if reviewed else source_name + "_POLICY_RELEASE_PUBLICATION_DATE_PROXY",
                    "SOURCE_URL": article_url,
                    "SOURCE": source_name,
                    "TITLE": title,
                    "FEED_URL": response.url,
                    "EVENT_DATE_BASIS": "INDEPENDENTLY_VALIDATED_EVENT_DATE" if reviewed else "PUBLICATION_DATE_PROXY_NOT_CONFIRMED_EVENT_DATE",
                    "EVENT_DATE_VALIDATION_METHOD": reviewed["validation_method"] if reviewed else "UNVALIDATED_PUBLICATION_DATE_PROXY",
                    "EVENT_DATE_VALIDATION_SOURCE_URL": reviewed["validation_source_url"] if reviewed else "",
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


def validate_observed_series_group(name, frame, start, end, series_map):
    """Domain QA for exact, observed source series; never fills missing dates or values."""
    if frame.empty:
        raise ValueError(f"{name} domain QA failed: no observed rows")
    required = {"DATE", "CLOSE", "SOURCE", "SOURCE_SERIES", "SOURCE_URL", "OBSERVED_AT_UTC"}
    if name == "us_yields":
        required.add("SERIES")
    else:
        required.add("COMMODITY")
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"{name} domain QA failed: missing columns {missing}")
    dates = pd.to_datetime(frame["DATE"], errors="coerce")
    values = pd.to_numeric(frame["CLOSE"], errors="coerce")
    if dates.isna().any() or values.isna().any() or (values <= 0).any():
        raise ValueError(f"{name} domain QA failed: invalid dates or non-positive/non-numeric values")
    if frame["SOURCE_URL"].astype(str).str.strip().eq("").any():
        raise ValueError(f"{name} domain QA failed: missing source URL")
    if frame["SOURCE_SERIES"].astype(str).str.strip().eq("").any():
        raise ValueError(f"{name} domain QA failed: missing source series identity")
    if frame["OBSERVED_AT_UTC"].astype(str).str.strip().eq("").any():
        raise ValueError(f"{name} domain QA failed: missing observation timestamp")
    key = ["DATE", "SERIES"] if name == "us_yields" else ["DATE", "COMMODITY"]
    if frame.duplicated(key).any():
        raise ValueError(f"{name} domain QA failed: duplicate date/series keys")
    if name == "us_yields":
        expected = set(series_map.values())
        actual = set(frame["SERIES"].astype(str))
        if actual != expected:
            raise ValueError(f"us_yields domain QA failed: expected {sorted(expected)}, got {sorted(actual)}")
        if not frame["SOURCE"].astype(str).str.contains("FRED|Treasury", case=False, regex=True).all():
            raise ValueError("us_yields domain QA failed: source is neither FRED nor US Treasury")
    else:
        expected = set(series_map.values())
        actual = set(frame["COMMODITY"].astype(str))
        if actual != expected:
            raise ValueError(f"global_commodity_prices domain QA failed: expected {sorted(expected)}, got {sorted(actual)}")
        allowed_sources = (
            frame["SOURCE"].astype(str).str.contains("FRED", case=False)
            | frame["SOURCE"].astype(str).str.contains("US Energy Information Administration", case=False, regex=False)
            | frame["SOURCE"].astype(str).str.contains("London Bullion Market Association", case=False, regex=False)
        )
        if not allowed_sources.all():
            raise ValueError("global_commodity_prices domain QA failed: unapproved source identity")
    observed_days = sorted(dates.dt.date.unique())
    if observed_days[0] < start or observed_days[-1] > end:
        raise ValueError(f"{name} domain QA failed: dates outside requested window")
    age = (end - observed_days[-1]).days
    if age < 0 or age > 5:
        raise ValueError(f"{name} domain QA failed: latest observed value age {age} days exceeds 5-day bound")
    return {"status": "COLLECTED_AND_DOMAIN_QA_PASSED", "rows": int(len(frame)),
            "date_min": str(observed_days[0]), "date_max": str(observed_days[-1]),
            "freshness_age_calendar_days": age,
            "domain_qa_checks": ["exact source-series identity", "required schema", "non-empty provenance",
                                 "valid positive numeric values", "unique date/series keys",
                                 "requested-window bounds", "latest observation age <= 5 calendar days"]}


def collect_group(name, series_map, start, end, session):
    rows, failures, fallback_evidence = [], {}, {}
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
            if name == "global_commodity_prices":
                try:
                    fallback_rows, fallback_report = fetch_commodity_fallback(session, series_id, label, start, end)
                    rows.extend(fallback_rows)
                    failures.pop(series_id, None)
                    fallback_evidence[series_id] = fallback_report
                except Exception as fallback_exc:
                    failures[series_id] += f"; exact-source fallback failed: {type(fallback_exc).__name__}: {str(fallback_exc)[:200]}"
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
    qa = None
    if not failures:
        try:
            qa = validate_observed_series_group(name, frame, start, end, series_map)
        except Exception as exc:
            failures["DOMAIN_QA"] = f"{type(exc).__name__}: {str(exc)[:240]}"
    return {"status": ("AVAILABLE_WITH_SOURCE_FAILURES" if failures else qa["status"]),
            "rows": int(len(frame)), "date_min": str(frame["DATE"].min()),
            "date_max": str(frame["DATE"].max()), "path": str(target),
            "source": sorted(set(frame["SOURCE"].astype(str))),
            "observed_source_series": sorted(set(frame["SOURCE_SERIES"].astype(str))),
            "requested_fred_series_ids": list(series_map),
            "failures": failures, "fallback_evidence": fallback_evidence, "domain_qa_checks": qa["domain_qa_checks"] if qa else [],
            "freshness_age_calendar_days": qa["freshness_age_calendar_days"] if qa else None,
            "provenance_columns": ["SOURCE", "SOURCE_SERIES", "SOURCE_URL", "OBSERVED_AT_UTC"],
            "notes": ("Exact source identity, schema, provenance, value, duplicate and freshness checks passed; "
                      "factor-specific economic interpretation and point-in-time release timing remain separate.") if qa else
                     "Collection did not pass domain QA; missing or invalid data remains UNKNOWN."}


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
        try:
            report["groups"]["gold_prices_monthly"] = fetch_world_bank_monthly_gold(session, start, end)
        except Exception as exc:
            report["groups"]["gold_prices_monthly"] = {"status": "BLOCKED", "rows": 0,
                "error": f"{type(exc).__name__}: {str(exc)[:240]}",
                "notes": "Monthly gold is separate from daily LBMA; missing data remains UNKNOWN."}
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
