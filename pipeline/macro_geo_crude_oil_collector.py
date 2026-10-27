#!/usr/bin/env python3
"""Bounded Brent crude collector for the Macro-Geo P0 hard gate.

Uses FRED's DCOILBRENTEU observation series. The source is explicitly named;
WTI is never substituted for Brent. Empty/malformed responses remain BLOCKED.
"""
from __future__ import annotations
from datetime import datetime, timezone, timedelta
from io import StringIO
from pathlib import Path
import json
import os
import time
import pandas as pd
import requests

ROOT = Path(".")
OUT = ROOT / "data/external"
REPORT = ROOT / "outputs/macro_geo/crude_oil_collection_report.json"
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
SERIES = "DCOILBRENTEU"
UA = "PRECISION-WIRES-NSE200-COLLECTOR/1.0 (research audit; public data)"

def validate_brent_proxy(frame, reference_date):
    """Domain QA for the explicitly labelled Yahoo Brent futures proxy.

    This validates usable proxy data, not equivalence to FRED spot Brent.
    """
    required = {"DATE", "CLOSE", "SOURCE", "SOURCE_SERIES", "SOURCE_URL", "OBSERVED_AT_UTC", "UNIT"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Brent proxy domain QA missing columns: {missing}")
    if frame.empty:
        raise ValueError("Brent proxy domain QA has no rows")
    dates = pd.to_datetime(frame["DATE"], errors="coerce")
    closes = pd.to_numeric(frame["CLOSE"], errors="coerce")
    if dates.isna().any() or closes.isna().any():
        raise ValueError("Brent proxy domain QA found invalid date/close values")
    if dates.dt.strftime("%Y-%m-%d").duplicated().any():
        raise ValueError("Brent proxy domain QA found duplicate dates")
    if (closes <= 0).any() or ((closes < 20) | (closes > 200)).any():
        raise ValueError("Brent proxy close outside conservative plausibility bounds (20..200 USD/barrel)")
    if not (frame["SOURCE_SERIES"].astype(str) == "BZ=F").all():
        raise ValueError("Brent proxy provenance must remain BZ=F")
    if not frame["SOURCE_URL"].astype(str).str.contains("query1.finance.yahoo.com/v8/finance/chart/BZ=F", regex=False).all():
        raise ValueError("Brent proxy source URL does not match Yahoo BZ=F endpoint")
    if not (frame["UNIT"].astype(str) == "USD_PER_BARREL").all():
        raise ValueError("Brent proxy unit must be USD_PER_BARREL")
    reference = pd.Timestamp(reference_date).normalize()
    latest = dates.max().normalize()
    age = int((reference - latest).days)
    if age < 0 or age > 3:
        raise ValueError(f"Brent proxy freshness failed: age={age} calendar days")
    return {"status": "COLLECTED_AND_DOMAIN_QA_PASSED", "freshness_age_calendar_days": age,
            "freshness_status": "FRESH", "proxy_only": True,
            "domain_qa_checks": ["required provenance/unit columns", "valid dates and closes",
                "unique dates", "plausible USD/barrel closes", "BZ=F endpoint provenance",
                "0..3 calendar-day freshness"],
            "domain_qa_boundary": "Yahoo Brent futures proxy; not equivalent to FRED Brent spot."}


def validate_fred_brent(frame, reference_date):
    """Domain QA for FRED Brent spot observations; does not imply 20-year completeness."""
    required = {"DATE", "CLOSE", "SOURCE", "SOURCE_SERIES", "SOURCE_URL", "OBSERVED_AT_UTC", "UNIT"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"FRED Brent domain QA missing columns: {missing}")
    if frame.empty:
        raise ValueError("FRED Brent domain QA has no rows")
    dates = pd.to_datetime(frame["DATE"], errors="coerce")
    closes = pd.to_numeric(frame["CLOSE"], errors="coerce")
    if dates.isna().any() or closes.isna().any():
        raise ValueError("FRED Brent domain QA found invalid date/close values")
    if dates.dt.strftime("%Y-%m-%d").duplicated().any():
        raise ValueError("FRED Brent domain QA found duplicate dates")
    if ((closes < 20) | (closes > 200)).any():
        raise ValueError("FRED Brent close outside conservative plausibility bounds (20..200 USD/barrel)")
    if not (frame["SOURCE_SERIES"].astype(str) == SERIES).all():
        raise ValueError("FRED Brent provenance must remain DCOILBRENTEU")
    if not frame["SOURCE"].astype(str).str.contains("FRED", case=False, regex=False).all():
        raise ValueError("FRED Brent source label missing")
    if not frame["SOURCE_URL"].astype(str).str.contains("fred.stlouisfed.org/graph/fredgraph.csv", regex=False).all():
        raise ValueError("FRED Brent source URL does not match FRED endpoint")
    if not (frame["UNIT"].astype(str) == "USD_PER_BARREL").all():
        raise ValueError("FRED Brent unit must be USD_PER_BARREL")
    reference = pd.Timestamp(reference_date).normalize()
    age = int((reference - dates.max().normalize()).days)
    if age < 0 or age > 3:
        raise ValueError(f"FRED Brent freshness failed: age={age} calendar days")
    return {"status":"COLLECTED_AND_DOMAIN_QA_PASSED","freshness_age_calendar_days":age,
            "freshness_status":"FRESH","proxy_only":False,
            "domain_qa_checks":["required provenance/unit columns","valid dates and closes","unique dates",
                "plausible USD/barrel closes","DCOILBRENTEU FRED endpoint provenance","0..3 calendar-day freshness"],
            "domain_qa_boundary":"FRED DCOILBRENTEU spot observations passed bounded domain QA; this does not establish full historical coverage."}


def observed_reference_date():
    candidates = [Path("data/processed/nse_eq_200_sessions.csv"), Path("data/external/benchmark_indices.csv")]
    panel = next((p for p in candidates if p.exists()), None)
    if panel is None:
        raise ValueError("Brent domain QA blocked: no observed market-session reference panel")
    pf = pd.read_csv(panel)
    col = next((c for c in pf.columns if str(c).strip().upper()=="DATE"), None)
    if col is None:
        raise ValueError("Brent domain QA blocked: reference panel has no DATE column")
    dates = pd.to_datetime(pf[col], errors="coerce").dropna()
    if dates.empty:
        raise ValueError("Brent domain QA blocked: reference panel has no valid dates")
    return dates.max()


def collect(session=None, start=None, end=None):
    session = session or requests.Session()
    session.headers.update({"User-Agent": UA})
    # Bound requests to the canonical panel window; never download all FRED history in CI.
    if start is None or end is None:
        candidates = [Path("data/processed/nse_eq_200_sessions.csv"), Path("data/external/benchmark_indices.csv")]
        panel = next((p for p in candidates if p.exists()), None)
        if panel is None:
            raise RuntimeError("No canonical market panel available to bound Brent collection window")
        pf = pd.read_csv(panel)
        date_col = next((c for c in pf.columns if str(c).strip().upper() == "DATE"), None)
        if date_col is None:
            raise ValueError("Panel missing DATE column; cannot bound Brent collection")
        pdts = pd.to_datetime(pf[date_col], errors="coerce").dropna()
        if pdts.empty:
            raise ValueError("Panel contains no valid dates; cannot bound Brent collection")
        unique = sorted(pdts.dt.date.unique())
        start = start or (unique[-min(200, len(unique))] - timedelta(days=30))
        # Decision-time safety: exclude commodity bars beyond the latest observed market session.
        # Future-dated bars can fail freshness checks and risk point-in-time leakage.
        end = end or unique[-1]
    params = {"id": SERIES, "cosd": str(start), "coed": str(end)}
    observed = datetime.now(timezone.utc).isoformat()
    response = None
    errors = []
    for attempt in range(3):
        try:
            response = session.get(URL, params=params, timeout=(8, 12))
            response.raise_for_status()
            break
        except requests.RequestException as exc:
            errors.append(f"{type(exc).__name__}: {str(exc)[:180]}")
            response = None
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
    if response is None:
        # Explicit third-party Brent futures fallback; never label it as the FRED spot series.
        start_ts = int(pd.Timestamp(str(start), tz="UTC").timestamp())
        end_ts = int((pd.Timestamp(str(end), tz="UTC") + pd.Timedelta(days=1)).timestamp())
        fallback_url = "https://query1.finance.yahoo.com/v8/finance/chart/BZ=F"
        try:
            fb = session.get(fallback_url, params={"period1":start_ts,"period2":end_ts,"interval":"1d"}, timeout=(8, 15))
            fb.raise_for_status()
            payload = fb.json()
            result_list = payload.get("chart",{}).get("result") or []
            if not result_list:
                raise ValueError("Yahoo Brent futures chart has no result")
            item = result_list[0]
            timestamps = item.get("timestamp") or []
            quote = (item.get("indicators",{}).get("quote") or [{}])[0]
            closes = quote.get("close") or []
            from zoneinfo import ZoneInfo
            tz = ZoneInfo((item.get("meta") or {}).get("exchangeTimezoneName") or "UTC")
            rows = []
            for stamp, val in zip(timestamps, closes):
                if val is None:
                    continue
                day = pd.Timestamp(int(stamp), unit="s", tz="UTC").tz_convert(tz).date().isoformat()
                if str(start) <= day <= str(end):
                    rows.append({"DATE":day,"CLOSE":float(val),"SOURCE":"Yahoo Finance chart API; Brent crude futures proxy",
                        "SOURCE_SERIES":"BZ=F","SOURCE_URL":fb.url,"OBSERVED_AT_UTC":observed,"UNIT":"USD_PER_BARREL"})
            out = pd.DataFrame(rows).drop_duplicates(["DATE"]).sort_values("DATE")
            if out.empty:
                raise ValueError("Yahoo Brent futures proxy returned no valid observations")
            OUT.mkdir(parents=True, exist_ok=True)
            target = OUT / "brent_crude.csv"
            tmp = target.with_suffix(".csv.tmp")
            out.to_csv(tmp, index=False)
            os.replace(tmp, target)
            # Validate against the latest observed market session, not wall-clock today.
            reference_candidates = [Path("data/processed/nse_eq_200_sessions.csv"), Path("data/external/benchmark_indices.csv")]
            reference_panel = next((p for p in reference_candidates if p.exists()), None)
            if reference_panel is None:
                raise ValueError("Brent proxy QA blocked: no observed market-session reference panel")
            reference_frame = pd.read_csv(reference_panel)
            reference_col = next((c for c in reference_frame.columns if str(c).strip().upper() == "DATE"), None)
            if reference_col is None:
                raise ValueError("Brent proxy QA blocked: reference panel has no DATE column")
            reference_dates = pd.to_datetime(reference_frame[reference_col], errors="coerce").dropna()
            if reference_dates.empty:
                raise ValueError("Brent proxy QA blocked: reference panel has no valid dates")
            qa = validate_brent_proxy(out, reference_dates.max())
            result = {"status":qa["status"],"series":"BZ=F","rows":int(len(out)),
                "date_min":str(out["DATE"].min()),"date_max":str(out["DATE"].max()),"source_url":fb.url,
                "path":str(target),"fallback_from":"FRED DCOILBRENTEU","fred_errors":errors,
                "freshness_age_calendar_days":qa["freshness_age_calendar_days"],
                "freshness_status":qa["freshness_status"],"domain_qa_checks":qa["domain_qa_checks"],
                "proxy_only":True,"domain_qa_boundary":qa["domain_qa_boundary"],
                "notes":"Yahoo Brent futures proxy passed bounded data-quality QA; it is not equivalent to FRED Brent spot."}
            REPORT.parent.mkdir(parents=True, exist_ok=True)
            REPORT.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
            print(json.dumps(result))
            return result
        except Exception as fallback_exc:
            raise RuntimeError(f"FRED Brent failed {errors}; Yahoo futures fallback failed: {type(fallback_exc).__name__}: {fallback_exc}") from fallback_exc
    frame = pd.read_csv(StringIO(response.content.decode("utf-8-sig", errors="replace")))
    frame.columns = [str(c).strip().upper() for c in frame.columns]
    date_col = next((c for c in ("DATE", "OBSERVATION_DATE") if c in frame.columns), None)
    if date_col is None or SERIES not in frame.columns:
        raise ValueError(f"FRED Brent schema mismatch: {list(frame.columns)}")
    dates = pd.to_datetime(frame[date_col], errors="coerce")
    values = pd.to_numeric(frame[SERIES], errors="coerce")
    out = pd.DataFrame({
        "DATE": dates.dt.strftime("%Y-%m-%d"),
        "CLOSE": values,
        "SOURCE": "Federal Reserve Bank of St. Louis FRED",
        "SOURCE_SERIES": SERIES,
        "SOURCE_URL": response.url,
        "OBSERVED_AT_UTC": observed,
        "UNIT": "USD_PER_BARREL",
    }).dropna(subset=["DATE", "CLOSE"])
    if start:
        out = out[out["DATE"] >= str(start)]
    if end:
        out = out[out["DATE"] <= str(end)]
    out = out.drop_duplicates(["DATE"]).sort_values("DATE")
    if out.empty:
        raise ValueError("FRED Brent series returned zero valid observations; crude_oil remains UNKNOWN/BLOCKED")
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "brent_crude.csv"
    tmp = target.with_suffix(".csv.tmp")
    out.to_csv(tmp, index=False)
    os.replace(tmp, target)
    qa = validate_fred_brent(out, observed_reference_date())
    result = {"status":qa["status"], "series":SERIES, "rows":int(len(out)),
              "date_min":str(out["DATE"].min()), "date_max":str(out["DATE"].max()),
              "source_url":response.url, "path":str(target),
              "freshness_age_calendar_days":qa["freshness_age_calendar_days"],
              "freshness_status":qa["freshness_status"],"domain_qa_checks":qa["domain_qa_checks"],
              "proxy_only":False,"domain_qa_boundary":qa["domain_qa_boundary"],
              "notes":"FRED Brent spot passed bounded domain QA; full historical coverage and point-in-time suitability remain separate checks."}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result))
    return result

if __name__ == "__main__":
    collect()
