#!/usr/bin/env python3
"""Audit-only quarterly-results event ledger and feature study.

NSE corporate-filings API is the primary discovery source. A board-meeting
intimation is a scheduled event, NOT a declared result. Numeric financials are
accepted only from the separately normalized, source-linked financials ledger;
this script never invents consensus or parses headline text into numbers.
"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
from pathlib import Path
import hashlib, json, re, time
import requests
import pandas as pd

ROOT = Path(".")
RAW = ROOT / "data/raw"
OUT = ROOT / "outputs/quarterly_results"
PANEL = ROOT / "data/processed/nse_eq_200_sessions.csv"
NSE_HOME = "https://www.nseindia.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
HEADERS = {"User-Agent": UA, "Accept": "application/json,text/plain,*/*",
           "Referer": "https://www.nseindia.com/companies-listing/corporate-filings-application"}
RESULTS_URL = NSE_HOME + "/api/corporates-financial-results"
MEETINGS_URL = NSE_HOME + "/api/corporates-board-meetings"
FINANCIALS_INPUT = RAW / "quarterly_financial_metrics.csv"
EVENT_COLUMNS = ["SYMBOL", "COMPANY", "SUBJECT", "EVENT_KIND", "RESULT_DECLARED", "BROADCAST_AT", "MEETING_DATE", "PERIOD_END", "ATTACHMENT_URL", "SOURCE_URL", "SOURCE_RECORD_SHA256", "OBSERVED_AT_UTC", "RAW_RECORD_JSON"]
REQUIRED_METRICS = {"SYMBOL", "PERIOD_END", "BASIS", "SOURCE_URL", "DISCLOSED_AT",
                    "REVENUE", "PAT", "EPS"}
OPTIONAL_METRICS = {"EBITDA", "INTEREST_EXPENSE", "DEBT", "OPERATING_CASH_FLOW",
                    "CONSENSUS_REVENUE", "CONSENSUS_PAT", "CONSENSUS_EPS"}
FINANCIAL_OUTPUT_COLUMNS = [
    "SYMBOL", "PERIOD_END", "BASIS", "SOURCE_URL", "DISCLOSED_AT",
    "REVENUE", "PAT", "EPS", "EBITDA", "INTEREST_EXPENSE", "DEBT",
    "OPERATING_CASH_FLOW", "CONSENSUS_REVENUE", "CONSENSUS_PAT", "CONSENSUS_EPS",
    "REVENUE_YOY_PCT", "PAT_YOY_PCT", "EPS_YOY_PCT", "REVENUE_QOQ_PCT",
    "PAT_QOQ_PCT", "EBITDA_MARGIN_PCT", "PAT_MARGIN_PCT", "REVENUE_SURPRISE_PCT",
    "PAT_SURPRISE_PCT", "EPS_SURPRISE_PCT", "FINANCIALS_STATUS"
]

def now_utc():
    return datetime.now(timezone.utc).isoformat()

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()

def records_from(payload):
    """Find the first list of row-like dictionaries in common NSE response envelopes."""
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    if isinstance(payload, dict):
        for key in ("data", "rows", "results", "financialResults", "boardMeetings"):
            if isinstance(payload.get(key), list):
                return [x for x in payload[key] if isinstance(x, dict)]
        for value in payload.values():
            if isinstance(value, (dict, list)):
                found = records_from(value)
                if found:
                    return found
    return []

def first(row, names):
    lowered = {str(k).lower().replace("_", "").replace(" ", ""): v for k, v in row.items()}
    for name in names:
        key = name.lower().replace("_", "").replace(" ", "")
        if key in lowered and lowered[key] not in (None, ""):
            return lowered[key]
    return ""

def parse_date(value):
    if value in (None, ""):
        return ""
    dt = pd.to_datetime(value, errors="coerce", dayfirst=True, utc=True)
    return "" if pd.isna(dt) else dt.isoformat()

def normalize_event(row, kind, source_url):
    symbol = str(first(row, ["symbol", "sm_symbol", "ticker", "securitysymbol"])).upper().strip()
    company = str(first(row, ["company", "companyname", "sm_name", "securityname"])).strip()
    subject = str(first(row, ["subject", "purpose", "description", "meetingpurpose", "details"])).strip()
    broadcast = parse_date(first(row, ["broadcastdate", "broadcast_date", "disseminationdate", "filingdate", "date"]))
    meeting = parse_date(first(row, ["meetingdate", "meeting_date", "bm_date", "dateofmeeting"]))
    period = str(first(row, ["periodended", "period_end", "financialperiod", "quarterended"])).strip()
    attachment = str(first(row, ["attchmntfile", "attachment", "attachmenturl", "pdfurl", "xbrl", "fileurl"])).strip()
    text = (subject + " " + company).lower()
    is_results = bool(re.search(r"financial results|quarterly results|half year results|unaudited financial|audited financial results|results for the quarter", text))
    return {
        "SYMBOL": symbol, "COMPANY": company, "SUBJECT": subject, "EVENT_KIND": kind,
        "RESULT_DECLARED": bool(kind == "RESULT_DISCLOSURE" and is_results),
        "BROADCAST_AT": broadcast, "MEETING_DATE": meeting, "PERIOD_END": period,
        "ATTACHMENT_URL": attachment, "SOURCE_URL": source_url,
        "SOURCE_RECORD_SHA256": digest(row), "OBSERVED_AT_UTC": now_utc(),
        "RAW_RECORD_JSON": json.dumps(row, sort_keys=True, default=str),
    }

def fetch_nse(endpoint, start, end):
    session = requests.Session()
    session.headers.update(HEADERS)
    # NSE may change access controls; failures must be visible, not silently replaced.
    session.get(NSE_HOME, timeout=(5, 20))
    params = {"index": "equities", "from_date": start.strftime("%d-%m-%Y"),
              "to_date": end.strftime("%d-%m-%Y")}
    response = session.get(endpoint, params=params, timeout=(5, 30))
    response.raise_for_status()
    payload = response.json()
    rows = records_from(payload)
    if not rows:
        raise RuntimeError("NSE endpoint returned no recognizable rows")
    return rows, response.url, payload

def pct_change(current, previous):
    try:
        current, previous = float(current), float(previous)
        if previous == 0:
            return None
        return (current / previous - 1.0) * 100.0
    except (TypeError, ValueError):
        return None

def build_financial_features(path):
    if not path.exists():
        return pd.DataFrame(columns=FINANCIAL_OUTPUT_COLUMNS), {
            "status": "BLOCKED_MISSING_NORMALIZED_FINANCIALS",
            "missing_file": str(path),
            "note": "Quarterly financial values and consensus are not inferred from headlines."
        }
    df = pd.read_csv(path)
    missing = sorted(REQUIRED_METRICS - set(df.columns))
    if missing:
        return pd.DataFrame(columns=FINANCIAL_OUTPUT_COLUMNS), {
            "status": "BLOCKED_BAD_FINANCIALS_SCHEMA", "missing_columns": missing
        }
    for col in OPTIONAL_METRICS:
        if col not in df:
            df[col] = pd.NA
    df["SYMBOL"] = df["SYMBOL"].astype(str).str.upper().str.strip()
    df["BASIS"] = df["BASIS"].astype(str).str.upper().str.strip()
    df["PERIOD_END"] = pd.to_datetime(df["PERIOD_END"], errors="coerce")
    df["DISCLOSED_AT"] = pd.to_datetime(df["DISCLOSED_AT"], errors="coerce", utc=True)
    for col in REQUIRED_METRICS & set(df.columns) | OPTIONAL_METRICS:
        if col not in {"SYMBOL", "PERIOD_END", "BASIS", "SOURCE_URL", "DISCLOSED_AT"}:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["SYMBOL", "PERIOD_END", "DISCLOSED_AT", "REVENUE", "PAT", "EPS"])
    # A duplicate key is ambiguous (e.g. standalone and consolidated); BASIS is part of key.
    key = ["SYMBOL", "PERIOD_END", "BASIS"]
    if df.duplicated(key).any():
        dupes = df.loc[df.duplicated(key, keep=False), key].to_dict("records")
        return pd.DataFrame(columns=FINANCIAL_OUTPUT_COLUMNS), {
            "status": "BLOCKED_DUPLICATE_PERIOD_BASIS", "duplicate_keys": dupes[:50]
        }
    df = df.sort_values(["SYMBOL", "BASIS", "PERIOD_END"])
    rows = []
    for (symbol, basis), group in df.groupby(["SYMBOL", "BASIS"], sort=False):
        group = group.sort_values("PERIOD_END")
        prior_year = {pd.Timestamp(r.PERIOD_END) + pd.DateOffset(years=1): r for r in group.itertuples(index=False)}
        prior_quarter = {}
        previous = None
        for r in group.itertuples(index=False):
            period = pd.Timestamp(r.PERIOD_END)
            yoy = prior_year.get(period)
            revenue_yoy = pct_change(r.REVENUE, yoy.REVENUE) if yoy else None
            pat_yoy = pct_change(r.PAT, yoy.PAT) if yoy else None
            eps_yoy = pct_change(r.EPS, yoy.EPS) if yoy else None
            revenue_qoq = pct_change(r.REVENUE, previous.REVENUE) if previous else None
            pat_qoq = pct_change(r.PAT, previous.PAT) if previous else None
            ebitda_margin = (float(r.EBITDA) / float(r.REVENUE) * 100) if pd.notna(r.EBITDA) and pd.notna(r.REVENUE) and float(r.REVENUE) else None
            pat_margin = (float(r.PAT) / float(r.REVENUE) * 100) if pd.notna(r.PAT) and pd.notna(r.REVENUE) and float(r.REVENUE) else None
            rows.append({
                "SYMBOL": symbol, "PERIOD_END": period.date().isoformat(), "BASIS": basis,
                "SOURCE_URL": r.SOURCE_URL, "DISCLOSED_AT": pd.Timestamp(r.DISCLOSED_AT).isoformat(),
                "REVENUE": r.REVENUE, "PAT": r.PAT, "EPS": r.EPS, "EBITDA": r.EBITDA,
                "INTEREST_EXPENSE": r.INTEREST_EXPENSE, "DEBT": r.DEBT,
                "OPERATING_CASH_FLOW": r.OPERATING_CASH_FLOW,
                "CONSENSUS_REVENUE": r.CONSENSUS_REVENUE, "CONSENSUS_PAT": r.CONSENSUS_PAT,
                "CONSENSUS_EPS": r.CONSENSUS_EPS,
                "REVENUE_YOY_PCT": revenue_yoy, "PAT_YOY_PCT": pat_yoy, "EPS_YOY_PCT": eps_yoy,
                "REVENUE_QOQ_PCT": revenue_qoq, "PAT_QOQ_PCT": pat_qoq,
                "EBITDA_MARGIN_PCT": ebitda_margin, "PAT_MARGIN_PCT": pat_margin,
                "REVENUE_SURPRISE_PCT": pct_change(r.REVENUE, r.CONSENSUS_REVENUE) if pd.notna(r.CONSENSUS_REVENUE) else None,
                "PAT_SURPRISE_PCT": pct_change(r.PAT, r.CONSENSUS_PAT) if pd.notna(r.CONSENSUS_PAT) else None,
                "EPS_SURPRISE_PCT": pct_change(r.EPS, r.CONSENSUS_EPS) if pd.notna(r.CONSENSUS_EPS) else None,
                "FINANCIALS_STATUS": "SOURCE_LINKED_ACTUALS" if r.SOURCE_URL else "BLOCKED_MISSING_SOURCE_URL"
            })
            previous = r
    out = pd.DataFrame(rows, columns=FINANCIAL_OUTPUT_COLUMNS)
    return out, {"status": "COMPUTED" if len(out) else "BLOCKED_NO_VALID_ROWS",
                 "valid_financial_rows": int(len(out)), "symbols": int(out.SYMBOL.nunique()) if len(out) else 0,
                 "consensus_rows": int(out[["CONSENSUS_REVENUE", "CONSENSUS_PAT", "CONSENSUS_EPS"]].notna().any(axis=1).sum()) if len(out) else 0}

def build_event_study(events_path, panel_path):
    if not events_path.exists() or not panel_path.exists():
        return pd.DataFrame(), {"status": "BLOCKED_MISSING_EVENT_OR_PRICE_PANEL",
                                "missing_files": [str(p) for p in (events_path, panel_path) if not p.exists()]}
    events = pd.read_csv(events_path)
    panel = pd.read_csv(panel_path)
    required_e = {"SYMBOL", "RESULT_DECLARED", "BROADCAST_AT", "SOURCE_URL"}
    required_p = {"SYMBOL", "DATE", "CLOSE"}
    if required_e - set(events.columns) or required_p - set(panel.columns):
        return pd.DataFrame(), {"status": "BLOCKED_BAD_EVENT_OR_PRICE_SCHEMA",
            "missing_event_columns": sorted(required_e-set(events.columns)),
            "missing_price_columns": sorted(required_p-set(panel.columns))}
    events = events[events["RESULT_DECLARED"].astype(str).str.lower().isin(["true", "1"])].copy()
    panel["SYMBOL"] = panel["SYMBOL"].astype(str).str.upper().str.strip()
    panel["DATE"] = pd.to_datetime(panel["DATE"], errors="coerce").dt.normalize()
    panel["CLOSE"] = pd.to_numeric(panel["CLOSE"], errors="coerce")
    panel = panel.dropna(subset=["SYMBOL", "DATE", "CLOSE"])
    results = []
    for e in events.itertuples(index=False):
        symbol = str(e.SYMBOL).upper().strip()
        disclosed = pd.to_datetime(e.BROADCAST_AT, errors="coerce", utc=True)
        if not symbol or pd.isna(disclosed) or not str(e.SOURCE_URL).strip():
            continue
        # Conservative timing: if only date-level disclosure timestamp is available,
        # use the first trading session strictly after the disclosure date.
        event_date = disclosed.tz_convert("Asia/Kolkata").tz_localize(None).normalize()
        series = panel[panel["SYMBOL"] == symbol].sort_values("DATE")
        dates = series["DATE"].drop_duplicates().tolist()
        reaction_dates = [d for d in dates if d > event_date]
        if not reaction_dates:
            continue
        base_date = reaction_dates[0]
        price_map = dict(zip(series["DATE"], series["CLOSE"]))
        base = price_map.get(base_date)
        if pd.isna(base) or not base or base <= 0:
            continue
        row = {"SYMBOL": symbol, "BROADCAST_AT": disclosed.isoformat(), "EVENT_DATE": event_date.date().isoformat(),
               "REACTION_BASE_DATE": base_date.date().isoformat(), "SOURCE_URL": e.SOURCE_URL,
               "EVENT_TYPE": "RESULT_DECLARED", "BASE_CLOSE": float(base)}
        for horizon in (1, 3, 5):
            idx = dates.index(base_date) + horizon
            target = price_map.get(dates[idx]) if idx < len(dates) else None
            row[f"FWD_CLOSE_RETURN_D{horizon}_PCT"] = (float(target)/float(base)-1)*100 if target and base else None
        results.append(row)
    out = pd.DataFrame(results)
    return out, {"status": "COMPUTED_EXPLORATORY" if len(out) else "BLOCKED_NO_MATCHED_EVENTS",
                 "matched_result_events": int(len(out)), "warning": "Descriptive event study only; no causal claim. Returns start at the first trading session after disclosure date to avoid look-ahead on date-only timestamps."}

def main():
    RAW.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)
    end = datetime.now(timezone.utc).date()
    start = end - timedelta(days=45)
    manifest = {"observed_at_utc": now_utc(), "window_start": start.isoformat(), "window_end": end.isoformat(),
                "primary_source": "NSE India corporate filings API", "sources": {}, "production_selector_changed": False}
    result_events, calendar_events = [], []
    for kind, endpoint, target in (
        ("RESULT_DISCLOSURE", RESULTS_URL, result_events),
        ("BOARD_MEETING", MEETINGS_URL, calendar_events),
    ):
        try:
            raw, source_url, payload = fetch_nse(endpoint, start, end + (timedelta(days=30) if kind == "BOARD_MEETING" else timedelta(0)))
            target.extend(normalize_event(row, kind, source_url) for row in raw)
            manifest["sources"][kind] = {"status": "AVAILABLE", "rows": len(raw), "response_sha256": digest(payload), "request_url": source_url}
        except Exception as exc:
            manifest["sources"][kind] = {"status": "UNKNOWN", "error": f"{type(exc).__name__}: {exc}"}
        time.sleep(0.2)
    disclosures_path = RAW / "quarterly_results_disclosures.csv"
    calendar_path = RAW / "quarterly_results_calendar.csv"
    pd.DataFrame(result_events, columns=EVENT_COLUMNS).to_csv(disclosures_path, index=False)
    pd.DataFrame(calendar_events, columns=EVENT_COLUMNS).to_csv(calendar_path, index=False)
    financials, financial_report = build_financial_features(FINANCIALS_INPUT)
    financials.to_csv(OUT / "quarterly_financial_features.csv", index=False)
    event_study, event_report = build_event_study(disclosures_path, PANEL)
    event_study.to_csv(OUT / "quarterly_results_event_study.csv", index=False)
    manifest["disclosure_rows"] = len(result_events)
    manifest["result_disclosure_rows"] = sum(bool(x["RESULT_DECLARED"]) for x in result_events)
    manifest["calendar_rows"] = len(calendar_events)
    manifest["financial_metrics"] = financial_report
    manifest["event_study"] = event_report
    manifest["status"] = "COLLECTED_WITH_BLOCKERS" if any(x["status"] != "AVAILABLE" for x in manifest["sources"].values()) or financial_report["status"].startswith("BLOCKED") else "COLLECTED"
    manifest["data_policy"] = {
        "board_meeting_is_not_result": True,
        "no_headline_number_extraction": True,
        "consensus_required_for_surprise": True,
        "standalone_consolidated_separate": True,
        "missing_data_semantics": "UNKNOWN/BLOCKED, never zero or negative",
        "retrospective_returns_are_not_live_signal_validation": True
    }
    (OUT / "quarterly_results_research_report.json").write_text(json.dumps(manifest, indent=2, allow_nan=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    # A failed/blocked source is represented in the report; workflow remains auditable.
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
