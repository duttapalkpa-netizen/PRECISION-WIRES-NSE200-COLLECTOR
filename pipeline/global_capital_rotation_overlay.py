#!/usr/bin/env python3
"""Research-only global capital rotation dashboard; never alters production ranking."""
from __future__ import annotations
import argparse, csv, json
from collections import defaultdict
from pathlib import Path

REQUIRED = {"date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status"}
ALLOWED_QUALITY = {"VERIFIED_OFFICIAL","VERIFIED_SECONDARY","PROVISIONAL","UNKNOWN"}

def load_observations(path: Path):
    grouped=defaultdict(list)
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or not REQUIRED.issubset(set(reader.fieldnames)):
            raise ValueError(f"missing columns: {sorted(REQUIRED-set(reader.fieldnames or []))}")
        for n,row in enumerate(reader, start=2):
            if row["quality_status"] not in ALLOWED_QUALITY:
                raise ValueError(f"row {n}: invalid quality_status")
            if not row["date"] or not row["indicator"] or not row["source"] or not row["source_url"]:
                raise ValueError(f"row {n}: missing provenance/date/indicator")
            if row["quality_status"] == "UNKNOWN":
                continue
            try: value=float(row["value"])
            except (TypeError,ValueError):
                raise ValueError(f"row {n}: non-numeric value")
            grouped[row["indicator"]].append({**row,"value":value})
    return grouped

def latest(grouped, key):
    rows=grouped.get(key, [])
    if not rows: return None
    # Use observation date for ordering; publication/as-of timestamps remain separately visible.
    return sorted(rows,key=lambda x:(x["date"],x["published_at"]))[-1]

def classify(grouped):
    keys=[
      "em_portfolio_flow_usd_bn","india_fpi_equity_inr_cr","india_fpi_debt_inr_cr",
      "india_dii_equity_inr_cr","dxy_change_pct_20d","us10y_change_bp_20d",
      "fed_target_change_bp_90d","usd_inr_change_pct_20d","brent_change_pct_20d",
      "india_vs_world_relative_return_pct_20d","vix_change_pct_20d",
      "us_ai_policy_event_direction","us_h1b_policy_event_direction","us_tariff_policy_event_direction"
    ]
    x={k:latest(grouped,k) for k in keys}
    def v(k): return None if x[k] is None else x[k]["value"]
    # Conservative, interpretable flags. Missing inputs always yield UNKNOWN, never neutral/PASS.
    if v("em_portfolio_flow_usd_bn") is None: global_flow="UNKNOWN"
    elif v("em_portfolio_flow_usd_bn")>0: global_flow="EM_NET_INFLOW"
    elif v("em_portfolio_flow_usd_bn")<0: global_flow="EM_NET_OUTFLOW"
    else: global_flow="FLAT"
    if v("india_fpi_equity_inr_cr") is None: india_fpi="UNKNOWN"
    elif v("india_fpi_equity_inr_cr")>0: india_fpi="FPI_EQUITY_NET_BUY"
    elif v("india_fpi_equity_inr_cr")<0: india_fpi="FPI_EQUITY_NET_SELL"
    else: india_fpi="FLAT"
    if v("dxy_change_pct_20d") is None or v("usd_inr_change_pct_20d") is None: fx="UNKNOWN"
    elif v("dxy_change_pct_20d")<0 and v("usd_inr_change_pct_20d")<0: fx="USD_AND_INR_TAILWIND"
    elif v("dxy_change_pct_20d")>0 and v("usd_inr_change_pct_20d")>0: fx="USD_AND_INR_HEADWIND"
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
    # No composite score and no political-event auto-sign. Policy-event direction is a sourced manual input.
    return {
      "status":"RESEARCH_ONLY_NO_PRODUCTION_SCORE",
      "global_em_flow":global_flow,"india_fpi_equity":india_fpi,"fx_transmission":fx,
      "us_rates_transmission":rates,"relative_attraction":relative,"oil_transmission":oil,
      "global_risk_appetite":risk,
      "india_dii_equity":"UNKNOWN" if v("india_dii_equity_inr_cr") is None else ("DII_NET_BUY" if v("india_dii_equity_inr_cr")>0 else "DII_NET_SELL" if v("india_dii_equity_inr_cr")<0 else "FLAT"),
      "policy_events":{k:("UNKNOWN" if v(k) is None else {"direction":v(k),"source":x[k]["source"],"source_url":x[k]["source_url"],"published_at":x[k]["published_at"]}) for k in keys[-3:]},
      "latest_observations":{k:(None if x[k] is None else {q:x[k][q] for q in ("date","value","unit","source","source_url","published_at","as_of_date","quality_status")}) for k in keys},
      "interpretation":"Global EM flows and India-specific FPI flows are separate populations and periods. A positive India daily print does not prove broad EM rotation. Missing or stale inputs remain UNKNOWN."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,help="long-format provenance CSV")
    p.add_argument("--output",default="global_capital_rotation_dashboard.json")
    a=p.parse_args()
    result=classify(load_observations(Path(a.input)))
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"output":a.output,"global_em_flow":result["global_em_flow"],"india_fpi_equity":result["india_fpi_equity"]},indent=2))
if __name__=="__main__": main()
