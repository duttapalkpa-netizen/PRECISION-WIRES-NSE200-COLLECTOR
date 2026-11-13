#!/usr/bin/env python3
"""Research-only global capital rotation dashboard; never alters production ranking."""
from __future__ import annotations
import argparse, csv, json, math
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

REQUIRED = {"date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status"}
ALLOWED_QUALITY = {"VERIFIED_OFFICIAL","VERIFIED_SECONDARY","PROVISIONAL","UNKNOWN"}
MAX_AGE_DAYS = {
    "em_portfolio_flow_usd_bn":45,
    "india_fpi_equity_inr_cr":7,"india_fpi_debt_inr_cr":7,"india_dii_equity_inr_cr":7,
    "india_fpi_equity_mtd_inr_cr":7,"india_fpi_equity_ytd_inr_cr":30,
    "dxy_change_pct_20d":30,"us10y_change_bp_20d":30,"fed_target_change_bp_90d":120,
    "usd_inr_change_pct_20d":7,"brent_change_pct_20d":7,
    "india_vs_world_relative_return_pct_20d":7,"vix_change_pct_20d":7,
    "us_ai_policy_event_direction":180,"us_h1b_policy_event_direction":180,"us_tariff_policy_event_direction":180,
}

def _published_key(value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError):
        raise ValueError("published_at must be an ISO date or datetime")
    # Treat timezone-naive source dates/timestamps as UTC; normalize offsets
    # before ordering vintages so lexical ordering is chronological.
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()

def load_observations(path: Path):
    grouped=defaultdict(list)
    seen_keys=set()
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or not REQUIRED.issubset(set(reader.fieldnames)):
            raise ValueError(f"missing columns: {sorted(REQUIRED-set(reader.fieldnames or []))}")
        for n,row in enumerate(reader, start=2):
            if row["quality_status"] not in ALLOWED_QUALITY:
                raise ValueError(f"row {n}: invalid quality_status")
            if not all(row[k].strip() for k in ("date","as_of_date","indicator","unit","source","source_url","published_at")):
                raise ValueError(f"row {n}: missing provenance/date")
            try:
                observed=date.fromisoformat(row["date"])
                asof=date.fromisoformat(row["as_of_date"])
                published=_published_key(row["published_at"])
                value=float(row["value"])
                if not math.isfinite(value): raise ValueError("non-finite value")
            except (TypeError,ValueError):
                raise ValueError(f"row {n}: invalid date, publication timestamp, or finite numeric value")
            duplicate_key=(row["indicator"],row["date"],row["as_of_date"],published,row["source"],row["source_url"])
            if duplicate_key in seen_keys:
                raise ValueError(f"row {n}: duplicate observation key within the same source publication vintage")
            seen_keys.add(duplicate_key)
            if observed > asof:
                raise ValueError(f"row {n}: observation date is after as_of_date")
            if not row["source_url"].startswith("https://"):
                raise ValueError(f"row {n}: source_url must use HTTPS")
            if row["quality_status"] == "UNKNOWN": continue
            grouped[row["indicator"]].append({**row,"value":value,"_published_key":published})
    return grouped

def latest(grouped,key):
    rows=grouped.get(key,[])
    if not rows: return None
    # Deterministic vintage selection: freshest observation, then latest publication.
    chosen=max(rows,key=lambda x:(x["as_of_date"],x["date"],x["_published_key"]))
    tie=[r for r in rows if (r["as_of_date"],r["date"],r["_published_key"]) ==
         (chosen["as_of_date"],chosen["date"],chosen["_published_key"])]
    if len({r["value"] for r in tie}) > 1:
        raise ValueError(f"{key}: conflicting values share the same observation and publication vintage")
    return chosen

def classify(grouped,as_of_date=None):
    asof=date.fromisoformat(as_of_date) if as_of_date else date.today()
    keys=list(MAX_AGE_DAYS)
    x={k:latest(grouped,k) for k in keys}
    stale={}
    for k,row in x.items():
        if row:
            observed=date.fromisoformat(row["as_of_date"])
            age=(asof-observed).days
            if age<0: raise ValueError(f"{k}: as_of_date is in the future")
            if age>MAX_AGE_DAYS[k]:
                stale[k]={"age_days":age,"max_age_days":MAX_AGE_DAYS[k]}
                x[k]=None
    def v(k): return None if x.get(k) is None else x[k]["value"]
    if v("em_portfolio_flow_usd_bn") is None: global_flow="UNKNOWN"
    elif v("em_portfolio_flow_usd_bn")>0: global_flow="EM_NET_INFLOW"
    elif v("em_portfolio_flow_usd_bn")<0: global_flow="EM_NET_OUTFLOW"
    else: global_flow="FLAT"
    if v("india_fpi_equity_inr_cr") is None: india_fpi="UNKNOWN"
    elif v("india_fpi_equity_inr_cr")>0: india_fpi="FPI_EQUITY_NET_BUY"
    elif v("india_fpi_equity_inr_cr")<0: india_fpi="FPI_EQUITY_NET_SELL"
    else: india_fpi="FLAT"
    if v("dxy_change_pct_20d") is None or v("usd_inr_change_pct_20d") is None: fx="UNKNOWN"
    elif v("dxy_change_pct_20d")<0 and v("usd_inr_change_pct_20d")<0: fx="USD_WEAKENING_INR_STRENGTHENING"
    elif v("dxy_change_pct_20d")>0 and v("usd_inr_change_pct_20d")>0: fx="USD_STRENGTHENING_INR_WEAKENING"
    else: fx="DIVERGENT_OR_MIXED"
    if v("us10y_change_bp_20d") is None or v("fed_target_change_bp_90d") is None: rates="UNKNOWN"
    elif v("us10y_change_bp_20d")<0 and v("fed_target_change_bp_90d")<=0: rates="US_RATE_RELIEF"
    elif v("us10y_change_bp_20d")>0 and v("fed_target_change_bp_90d")>0: rates="US_RATE_PRESSURE"
    else: rates="MIXED"
    if v("india_vs_world_relative_return_pct_20d") is None: relative="UNKNOWN"
    elif v("india_vs_world_relative_return_pct_20d")>0: relative="INDIA_OUTPERFORMING"
    elif v("india_vs_world_relative_return_pct_20d")<0: relative="INDIA_UNDERPERFORMING"
    else: relative="INLINE"
    if v("brent_change_pct_20d") is None: oil="UNKNOWN"
    elif v("brent_change_pct_20d")<0: oil="OIL_PRICE_RELIEF"
    elif v("brent_change_pct_20d")>0: oil="OIL_PRICE_PRESSURE"
    else: oil="FLAT"
    if v("vix_change_pct_20d") is None: risk="UNKNOWN"
    elif v("vix_change_pct_20d")<0: risk="VOLATILITY_EASING"
    elif v("vix_change_pct_20d")>0: risk="VOLATILITY_RISING"
    else: risk="FLAT"
    mtd=v("india_fpi_equity_mtd_inr_cr"); ytd=v("india_fpi_equity_ytd_inr_cr")
    if mtd is None or ytd is None: horizon="UNKNOWN"
    elif mtd>0 and ytd<0: horizon="SHORT_TERM_INFLOW_LONG_TERM_OUTFLOW"
    elif mtd<0 and ytd<0: horizon="OUTFLOW_BOTH_HORIZONS"
    elif mtd>0 and ytd>0: horizon="INFLOW_BOTH_HORIZONS"
    elif mtd<0 and ytd>0: horizon="SHORT_TERM_OUTFLOW_LONG_TERM_INFLOW"
    else: horizon="MIXED_OR_FLAT"
    return {
      "status":"RESEARCH_ONLY_NO_PRODUCTION_SCORE","as_of_date":asof.isoformat(),
      "global_em_flow":global_flow,"india_fpi_equity":india_fpi,"india_fpi_horizon_divergence":horizon,"fx_transmission":fx,
      "us_rates_transmission":rates,"relative_attraction":relative,"oil_transmission":oil,
      "global_risk_appetite":risk,
      "india_fpi_debt":"UNKNOWN" if v("india_fpi_debt_inr_cr") is None else ("FPI_DEBT_NET_BUY" if v("india_fpi_debt_inr_cr")>0 else "FPI_DEBT_NET_SELL" if v("india_fpi_debt_inr_cr")<0 else "FLAT"),
      "india_dii_equity":"UNKNOWN" if v("india_dii_equity_inr_cr") is None else ("DII_NET_BUY" if v("india_dii_equity_inr_cr")>0 else "DII_NET_SELL" if v("india_dii_equity_inr_cr")<0 else "FLAT"),
      "policy_events":{k:("UNKNOWN" if v(k) is None else {"direction":v(k),"source":x[k]["source"],"source_url":x[k]["source_url"],"published_at":x[k]["published_at"]}) for k in keys[-3:]},
      "stale_observations_excluded":stale,
      "latest_observations":{k:(None if x[k] is None else {q:x[k][q] for q in ("date","value","unit","source","source_url","published_at","as_of_date","quality_status")}) for k in keys},
      "interpretation":"Global EM flows and India-specific FPI flows are separate populations and periods. A positive India daily print does not prove broad EM rotation. Missing or stale inputs remain UNKNOWN."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,help="long-format provenance CSV")
    p.add_argument("--output",default="global_capital_rotation_dashboard.json")
    p.add_argument("--as-of-date",help="ISO date for reproducible freshness checks; defaults to system date")
    a=p.parse_args()
    result=classify(load_observations(Path(a.input)),a.as_of_date)
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"output":a.output,"global_em_flow":result["global_em_flow"],"india_fpi_equity":result["india_fpi_equity"],"excluded_stale":len(result["stale_observations_excluded"])},indent=2))
if __name__=="__main__": main()
