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
INTEGRATED_RESULTS_URL = NSE_HOME + "/api/corporate-integrated-filings"
MEETINGS_URL = NSE_HOME + "/api/corporate-boardMeetings"
ANNOUNCEMENTS_URL = NSE_HOME + "/api/corporate-announcements"
FINANCIALS_INPUT = RAW / "quarterly_financial_metrics.csv"
EVENT_COLUMNS = ["SYMBOL", "ISIN", "COMPANY", "SUBJECT", "EVENT_KIND", "RESULT_DECLARED", "BROADCAST_AT", "MEETING_DATE", "PERIOD_END", "ATTACHMENT_URL", "SOURCE_URL", "SOURCE_RECORD_SHA256", "OBSERVED_AT_UTC", "RAW_RECORD_JSON"]
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

def parse_reporting_period(row):
    """Parse an explicitly stated period end from NSE filing metadata only.

    Do not infer a period from the filing date, attachment filename or quarter
    number. A financial-results announcement without a period stays UNKNOWN.
    """
    explicit = first(row, ["periodended", "period_end", "periodenddate",
                           "quarterenddate", "financialperiod", "quarterended",
                           "toDate", "period"])
    if explicit:
        parsed = pd.to_datetime(explicit, errors="coerce", dayfirst=True)
        if pd.notna(parsed):
            return parsed.date().isoformat()

    metadata = " ".join(str(first(row, [key])) for key in
                        ("attchmntText", "subject", "purpose", "description",
                         "desc", "relatingTo", "details"))
    date_pattern = (
        r"(?:\d{1,2}(?:st|nd|rd|th)?\s+"
        r"[A-Za-z]+,?\s+\d{4}"
        r"|[A-Za-z]+\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}"
        r"|\d{1,2}[-/][A-Za-z]{3,9}[-/]\d{4}"
        r"|\d{4}-\d{2}-\d{2})"
    )
    pattern = (r"\b(?:quarter|qtr|half[\s-]*year|six months|"
               r"financial year|year|financial period|period)\s+"
               r"ended\s+(?:on\s+|as\s+on\s+)?"
               + "(" + date_pattern + ")")
    matches = re.findall(pattern, metadata, flags=re.IGNORECASE)
    periods = set()
    for raw in matches:
        cleaned = re.sub(r"(?i)(?<=\d)(st|nd|rd|th)\b", "", raw)
        parsed = pd.to_datetime(cleaned, errors="coerce", dayfirst=True)
        if pd.notna(parsed):
            periods.add(parsed.date().isoformat())
    return next(iter(periods)) if len(periods) == 1 else ""


def normalize_event(row, kind, source_url):
    symbol = str(first(row, ["symbol", "sm_symbol", "ticker", "securitysymbol"])).upper().strip()
    company = str(first(row, ["company", "companyname", "sm_name", "securityname"])).strip()
    subject = str(first(row, ["subject", "purpose", "description", "desc", "attchmntText", "meetingpurpose", "details", "relatingTo"])).strip()
    broadcast = parse_date(first(row, ["broadcastdate", "broadcast_date", "disseminationdate", "filingdate", "an_dt", "sort_date", "sortdate", "dt", "dateandtime", "date"]))
    meeting = parse_date(first(row, ["meetingdate", "meeting_date", "bm_date", "dateofmeeting"]))
    period = parse_reporting_period(row)
    attachment = str(first(row, ["attchmntfile", "attachment", "attachmenturl", "detailsurl", "xbrlurl", "pdfurl", "xbrl", "fileurl"])).strip()
    # NSE announcement metadata often labels the row "Outcome of Board Meeting"
    # while attchmntText explicitly states that financial results were submitted.
    # Classify using all filing metadata, not only the first display subject.
    event_text = " ".join(
        str(first(row, names))
        for names in (
            ["attchmntText"], ["subject"], ["purpose"], ["description"], ["desc"],
            ["relatingTo"], ["details"], ["company", "companyname", "sm_name"]
        )
    ).lower()
    has_results_phrase = bool(re.search(
        r"financial results|quarterly results|half year results|unaudited financial|audited financial results|results for the quarter|integrated filing.*financial",
        event_text
    ))
    excluded = bool(re.search(
        r"reply to clarification|clarification|delayed|non-submission|non submission|resubmission|revised filing",
        event_text
    ))
    is_results = kind == "RESULT_DISCLOSURE" and has_results_phrase and not excluded and bool(period)
    return {
        "SYMBOL": symbol, "ISIN": str(first(row, ["sm_isin", "isin", "securityisin"])).upper().strip(),
        "COMPANY": company, "SUBJECT": subject, "EVENT_KIND": kind,
        "RESULT_DECLARED": bool(kind == "RESULT_DISCLOSURE" and is_results),
        "BROADCAST_AT": broadcast, "MEETING_DATE": meeting, "PERIOD_END": period,
        "ATTACHMENT_URL": attachment, "SOURCE_URL": attachment if (attachment.startswith("https://www.nseindia.com/") or attachment.startswith("https://nsearchives.nseindia.com/")) else source_url,
        "SOURCE_RECORD_SHA256": digest(row), "OBSERVED_AT_UTC": now_utc(),
        "RAW_RECORD_JSON": json.dumps(row, sort_keys=True, default=str),
    }

def fetch_nse(endpoint, start, end):
    """Fetch structured filings first; announcements are a strict metadata-only fallback."""
    session = requests.Session()
    session.headers.update(HEADERS)
    session.get(NSE_HOME, timeout=(5, 20))
    params = {"index": "equities", "from_date": start.strftime("%d-%m-%Y"),
              "to_date": end.strftime("%d-%m-%Y")}
    if endpoint == RESULTS_URL:
        candidates = [
            (INTEGRATED_RESULTS_URL, {"integratedType": "integratedfilingfinancials"}),
            (RESULTS_URL, {}),
            (ANNOUNCEMENTS_URL, {}),
        ]
    elif endpoint == MEETINGS_URL:
        candidates = [(MEETINGS_URL, {}), (ANNOUNCEMENTS_URL, {})]
    else:
        candidates = [(endpoint, {})]
    failures = []
    for candidate, extra_params in candidates:
        try:
            request_params = {**params, **extra_params}
            response = session.get(candidate, params=request_params, timeout=(5, 30))
            response.raise_for_status()
            payload = response.json()
            rows = records_from(payload)
            if candidate == ANNOUNCEMENTS_URL:
                def announcement_text(row):
                    return " ".join(str(first(row, names)) for names in (
                        ["subject", "purpose", "description", "desc", "attchmntText", "details", "relatingTo"],
                        ["company", "companyname", "sm_name"]
                    )).lower()
                def row_date(row):
                    return pd.to_datetime(first(row, [
                        "broadcastDateTime", "broadcastDate", "broadcast_date",
                        "exchdisstime", "an_dt", "sort_date", "sortdate", "dt", "date"
                    ]), errors="coerce", dayfirst=True, utc=True)
                start_ts = pd.Timestamp(start, tz="UTC")
                end_ts = pd.Timestamp(end + timedelta(days=1), tz="UTC")
                in_window = []
                for row in rows:
                    stamp = row_date(row)
                    if pd.notna(stamp) and start_ts <= stamp < end_ts:
                        in_window.append(row)
                rows = in_window
                if endpoint == RESULTS_URL:
                    rows = [r for r in rows
                            if re.search(r"financial results|quarterly results|half year results|unaudited financial|audited financial results|results for the quarter|integrated filing.*financial", announcement_text(r))
                            and not re.search(r"reply to clarification|clarification|delayed|non-submission|non submission|resubmission|revised filing|board meeting", announcement_text(r))
                            ]
                elif endpoint == MEETINGS_URL:
                    rows = [r for r in rows if re.search(r"board meeting|meeting of the board", announcement_text(r))]
            if rows:
                return rows, response.url, payload
            failures.append(f"{candidate}: no recognizable rows for requested event class/window")
        except Exception as exc:
            failures.append(f"{candidate}: {type(exc).__name__}: {exc}")
    raise RuntimeError("All NSE endpoints failed or returned no matching structured rows: " + " | ".join(failures))

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
    panel.columns = [str(c).strip().upper() for c in panel.columns]
    # The normalized NSE daily dataset uses CLOSE_PRICE; explicitly normalize this
    # known schema variant rather than falsely blocking the event study.
    if "CLOSE" not in panel.columns and "CLOSE_PRICE" in panel.columns:
        panel = panel.rename(columns={"CLOSE_PRICE": "CLOSE"})
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
    validation_rows = []
    raw_dir = RAW / "quarterly_results_raw_responses"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for kind, endpoint, target in (
        ("RESULT_DISCLOSURE", RESULTS_URL, result_events),
        ("BOARD_MEETING", MEETINGS_URL, calendar_events),
    ):
        try:
            raw, source_url, payload = fetch_nse(endpoint, start, end + (timedelta(days=30) if kind == "BOARD_MEETING" else timedelta(0)))
            raw_path = raw_dir / ("".join(ch.lower() if ch.isalnum() else "_" for ch in kind) + ".json")
            raw_path.write_text(json.dumps({"request_url": source_url, "observed_at_utc": now_utc(), "payload": payload}, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
            normalized = [normalize_event(row, kind, source_url) for row in raw]
            target.extend(normalized)
            for item in normalized:
                fields = {
                    "source_url": (str(item.get("SOURCE_URL", "")).startswith("https://www.nseindia.com/") or str(item.get("SOURCE_URL", "")).startswith("https://nsearchives.nseindia.com/")),
                    "publication_timestamp": bool(parse_date(item.get("BROADCAST_AT"))),
                    "reporting_period": bool(str(item.get("PERIOD_END", "")).strip()) if kind == "RESULT_DISCLOSURE" else True,
                    "symbol": bool(re.fullmatch(r"[A-Z0-9&._-]{1,30}", str(item.get("SYMBOL", "")))),
                    "isin": bool(re.fullmatch(r"[A-Z]{2}[A-Z0-9]{9}[0-9]", str(item.get("ISIN", "")))),
                }
                validation_rows.append({"EVENT_KIND": kind, "SYMBOL": item.get("SYMBOL", ""), "ISIN": item.get("ISIN", ""), "SOURCE_URL": item.get("SOURCE_URL", ""), "PUBLICATION_TIMESTAMP": item.get("BROADCAST_AT", ""), "REPORTING_PERIOD": item.get("PERIOD_END", ""), **{f"{name.upper()}_VALID": value for name, value in fields.items()}, "RECORD_VALID": all(fields.values()), "MISSING_FIELDS": ";".join(name for name, value in fields.items() if not value), "SOURCE_RECORD_SHA256": item.get("SOURCE_RECORD_SHA256", "")})
            manifest["sources"][kind] = {"status": "AVAILABLE", "rows": len(raw), "response_sha256": digest(payload), "request_url": source_url, "raw_response_file": str(raw_path)}
        except Exception as exc:
            manifest["sources"][kind] = {"status": "UNKNOWN", "error": f"{type(exc).__name__}: {exc}"}
        time.sleep(0.2)
    validation_path = OUT / "source_validation_report.csv"
    pd.DataFrame(validation_rows, columns=["EVENT_KIND", "SYMBOL", "ISIN", "SOURCE_URL", "PUBLICATION_TIMESTAMP", "REPORTING_PERIOD", "SOURCE_URL_VALID", "PUBLICATION_TIMESTAMP_VALID", "REPORTING_PERIOD_VALID", "SYMBOL_VALID", "ISIN_VALID", "RECORD_VALID", "MISSING_FIELDS", "SOURCE_RECORD_SHA256"]).to_csv(validation_path, index=False)
    manifest["source_validation"] = {"status": "PASS" if validation_rows and all(x["RECORD_VALID"] for x in validation_rows) else "BLOCKED", "records_checked": len(validation_rows), "valid_records": sum(bool(x["RECORD_VALID"]) for x in validation_rows), "report_file": str(validation_path), "required_fields": ["source_url", "publication_timestamp", "reporting_period", "symbol", "isin"]}
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
