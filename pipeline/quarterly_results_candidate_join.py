#!/usr/bin/env python3
"""Attach point-in-time quarterly-result evidence to frozen H+1 research picks.

Audit-only: this creates evidence columns for paired analysis and never changes
RANKING_SCORE, production selection, or the frozen +1 PRESSURE_FADE.
Unavailable feeds remain UNKNOWN; no headline-derived financial values are used.
"""
from pathlib import Path
import json
import pandas as pd

PICKS = Path("outputs/prospective/target5_h1_selector_experiment_picks.csv")
EVENTS = Path("data/raw/quarterly_results_disclosures.csv")
FEATURES = Path("outputs/quarterly_results/quarterly_financial_features.csv")
REPORT = Path("outputs/quarterly_results/quarterly_results_research_report.json")
SESSIONS = Path("data/processed/nse_eq_200_sessions.csv")
OUT = Path("outputs/quarterly_results/target5_h1_quarterly_catalyst_join.csv")
OUT_REPORT = Path("outputs/quarterly_results/target5_h1_quarterly_catalyst_join_report.json")
IST = "Asia/Kolkata"
FEATURE_FIELDS = [
    "PERIOD_END", "BASIS", "REVENUE_YOY_PCT", "PAT_YOY_PCT", "EPS_YOY_PCT",
    "REVENUE_QOQ_PCT", "PAT_QOQ_PCT", "EBITDA_MARGIN_PCT", "PAT_MARGIN_PCT",
    "REVENUE_SURPRISE_PCT", "PAT_SURPRISE_PCT", "EPS_SURPRISE_PCT",
    "FINANCIALS_STATUS", "SOURCE_URL", "DISCLOSED_AT"
]

def read_report():
    if not REPORT.exists():
        return {}
    try:
        return json.loads(REPORT.read_text(encoding="utf-8"))
    except Exception:
        return {}

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    source_report = read_report()
    source_status = source_report.get("sources", {}).get("RESULT_DISCLOSURE", {}).get("status", "UNKNOWN")
    if not PICKS.exists():
        report = {"status":"BLOCKED_MISSING_CANDIDATE_PICKS","source_status":source_status,
                  "production_selector_changed":False,"rows":0}
        OUT_REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2)); return 0

    picks = pd.read_csv(PICKS, dtype={"SYMBOL":str})
    required = {"CUT_OFF","SYMBOL"}
    missing = sorted(required - set(picks.columns))
    if missing:
        report = {"status":"BLOCKED_BAD_CANDIDATE_SCHEMA","missing_columns":missing,
                  "source_status":source_status,"production_selector_changed":False,"rows":0}
        OUT_REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2)); return 0

    picks["SYMBOL"] = picks["SYMBOL"].astype(str).str.upper().str.strip()
    picks["CUT_OFF"] = pd.to_datetime(picks["CUT_OFF"], errors="coerce")
    sessions = set()
    if SESSIONS.exists():
        s = pd.read_csv(SESSIONS, usecols=lambda c: str(c).strip().upper() == "DATE")
        if not s.empty:
            sessions = set(pd.to_datetime(s.iloc[:,0], errors="coerce").dropna().dt.normalize())
    events = pd.DataFrame()
    if EVENTS.exists():
        events = pd.read_csv(EVENTS)
        events.columns = [str(c).strip().upper() for c in events.columns]
    features = pd.DataFrame()
    if FEATURES.exists():
        features = pd.read_csv(FEATURES)
        features.columns = [str(c).strip().upper() for c in features.columns]
        if "SYMBOL" in features:
            features["SYMBOL"] = features["SYMBOL"].astype(str).str.upper().str.strip()
        if "DISCLOSED_AT" in features:
            features["DISCLOSED_AT"] = pd.to_datetime(features["DISCLOSED_AT"], errors="coerce", utc=True)

    out_rows = []
    for pick in picks.to_dict("records"):
        symbol = str(pick.get("SYMBOL","")).upper().strip()
        cut = pd.Timestamp(pick["CUT_OFF"])
        cut_date = cut.normalize()
        cutoff_ist = cut_date.tz_localize(IST) + pd.Timedelta(hours=15, minutes=30)
        if sessions:
            prior_sessions = sorted(d for d in sessions if d <= cut_date)
            window_start = prior_sessions[-5] if len(prior_sessions) >= 5 else (prior_sessions[0] if prior_sessions else cut_date - pd.Timedelta(days=7))
        else:
            window_start = cut_date - pd.Timedelta(days=7)

        fresh = []
        if source_status == "AVAILABLE" and not events.empty and {"SYMBOL","RESULT_DECLARED","BROADCAST_AT","SOURCE_URL"}.issubset(events.columns):
            e = events.copy()
            e["SYMBOL"] = e["SYMBOL"].astype(str).str.upper().str.strip()
            e["BROADCAST_AT_PARSED"] = pd.to_datetime(e["BROADCAST_AT"], errors="coerce", utc=True)
            e["EVENT_DATE"] = e["BROADCAST_AT_PARSED"].dt.tz_convert(IST).dt.tz_localize(None).dt.normalize()
            declared = e["RESULT_DECLARED"].astype(str).str.lower().isin(["true","1"])
            e = e[(e["SYMBOL"] == symbol) & declared & e["BROADCAST_AT_PARSED"].notna()]
            for ev in e.to_dict("records"):
                published = ev["BROADCAST_AT_PARSED"]
                # Date-only NSE timestamps normalize to UTC midnight; treat same-day
                # timing as ambiguous and do not leak it into a 15:30 cutoff.
                date_only_proxy = published.hour == 0 and published.minute == 0 and published.second == 0
                pub_ist = published.tz_convert(IST)
                if date_only_proxy and pub_ist.date() == cutoff_ist.date():
                    continue
                if window_start.date() <= pub_ist.date() and pub_ist < cutoff_ist and str(ev.get("SOURCE_URL","")).startswith("http"):
                    fresh.append(ev)

        row = dict(pick)
        row["QUARTERLY_SOURCE_STATUS"] = source_status
        row["QUARTERLY_WINDOW_START"] = pd.Timestamp(window_start).date().isoformat()
        row["QUARTERLY_WINDOW_END_CUTOFF_IST"] = cutoff_ist.isoformat()
        row["QUARTERLY_RESULT_EVENT_COUNT_5_SESSIONS"] = len(fresh)
        row["QUARTERLY_CATALYST_STATUS"] = (
            "UNKNOWN_SOURCE_COVERAGE" if source_status != "AVAILABLE"
            else "FRESH_RESULT_DISCLOSURE" if fresh
            else "NO_RESULT_DISCLOSURE_MATCH_IN_AVAILABLE_FEED"
        )
        row["QUARTERLY_LATEST_DISCLOSED_AT"] = ""
        row["QUARTERLY_SOURCE_URL"] = ""
        if fresh:
            latest = sorted(fresh, key=lambda x: x["BROADCAST_AT_PARSED"])[-1]
            row["QUARTERLY_LATEST_DISCLOSED_AT"] = latest["BROADCAST_AT_PARSED"].isoformat()
            row["QUARTERLY_SOURCE_URL"] = latest.get("SOURCE_URL","")

        for field in FEATURE_FIELDS:
            row["LATEST_QUARTERLY_" + field] = ""
        if not features.empty and {"SYMBOL","DISCLOSED_AT"}.issubset(features.columns):
            eligible = features[(features["SYMBOL"] == symbol) & features["DISCLOSED_AT"].notna() & (features["DISCLOSED_AT"] <= cutoff_ist.tz_convert("UTC"))]
            if not eligible.empty:
                f = eligible.sort_values("DISCLOSED_AT").iloc[-1]
                for field in FEATURE_FIELDS:
                    if field in features.columns and pd.notna(f.get(field)):
                        row["LATEST_QUARTERLY_" + field] = f.get(field)
        out_rows.append(row)

    out = pd.DataFrame(out_rows)
    out.to_csv(OUT, index=False)
    status = "COMPUTED_AUDIT_JOIN" if source_status == "AVAILABLE" else "COMPUTED_WITH_UNKNOWN_SOURCE_COVERAGE"
    report = {
        "status":status,"rows":int(len(out)),"unique_symbols":int(out["SYMBOL"].nunique()) if len(out) else 0,
        "quarterly_source_status":source_status,
        "fresh_result_disclosure_rows":int(out["QUARTERLY_CATALYST_STATUS"].eq("FRESH_RESULT_DISCLOSURE").sum()) if len(out) else 0,
        "unknown_coverage_rows":int(out["QUARTERLY_CATALYST_STATUS"].eq("UNKNOWN_SOURCE_COVERAGE").sum()) if len(out) else 0,
        "no_match_rows":int(out["QUARTERLY_CATALYST_STATUS"].eq("NO_RESULT_DISCLOSURE_MATCH_IN_AVAILABLE_FEED").sum()) if len(out) else 0,
        "financial_feature_rows":int(out["LATEST_QUARTERLY_FINANCIALS_STATUS"].eq("SOURCE_LINKED_ACTUALS").sum()) if len(out) and "LATEST_QUARTERLY_FINANCIALS_STATUS" in out else 0,
        "window_rule":"Latest five available trading sessions up to cutoff; cutoff is 15:30 Asia/Kolkata; same-day date-only disclosures are excluded as timing-ambiguous.",
        "data_policy":"UNKNOWN coverage is not no-result evidence; numeric features only from normalized source-linked financial metrics.",
        "production_selector_changed":False,"ranking_score_changed":False,"pressure_fade_changed":False
    }
    OUT_REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
