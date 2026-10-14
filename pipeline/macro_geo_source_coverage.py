#!/usr/bin/env python3
"""Inventory macro/geo/sector source coverage and run generic quality checks."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path("."); OUT=Path("outputs/macro_geo"); REPORT=OUT/"source_coverage.json"
SOURCES={
"nse_daily_equity":{"paths":["data/processed/nse_eq_200_sessions.csv"],"required":["DATE","SYMBOL","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]},
"sector_indices":{"paths":["data/external/sector_indices.csv","data/context/sector_indices.csv"],"required":["DATE","SERIES","CLOSE"]},
"benchmark_index":{"paths":["data/external/benchmark_indices.csv","data/context/benchmark_indices.csv"],"required":["DATE","SERIES","CLOSE"]},
"crude_oil":{"paths":["data/external/brent_crude.csv","data/context/brent_crude.csv"],"required":["DATE","CLOSE"]},
"usd_inr":{"paths":["data/external/usd_inr.csv","data/context/usd_inr.csv"],"required":["DATE","CLOSE"]},
"us_yields":{"paths":["data/external/us_yields.csv","data/context/us_yields.csv"],"required":["DATE","SERIES","CLOSE"]},
"us_real_yields":{"paths":["data/external/us_real_yields.csv"],"required":["DATE","SERIES","CLOSE"]},
"dxy":{"paths":["data/external/dxy.csv","data/context/dxy.csv"],"required":["DATE","CLOSE"]},
"volatility":{"paths":["data/external/volatility.csv","data/context/volatility.csv"],"required":["DATE","SERIES","CLOSE"]},
"fpi_dii_flows":{"paths":["data/external/fpi_dii_flows.csv","data/context/fii_dii.csv"],"required":["DATE","GROUP","NET_VALUE"]},
"india_bond_yields":{"paths":["data/external/india_bond_yields.csv","data/context/india_bond_yields.csv"],"required":["DATE","YIELD_10Y"]},
"rbi_policy_liquidity":{"paths":["data/external/rbi_policy_liquidity.csv"],"required":["DATE","REPO_RATE","POLICY_SURPRISE"]},
"macro_indicators":{"paths":["data/external/macro_indicators.csv"],"required":["DATE","INDICATOR","VALUE"]},
"fed_policy_surprises":{"paths":["data/external/fed_policy_surprises.csv"],"required":["DATE","ANNOUNCEMENT_AT","EXPECTED_RATE","ACTUAL_RATE","SURPRISE_BPS","SOURCE_URL"]},
"india_current_account":{"paths":["data/external/india_current_account.csv"],"required":["DATE","RELEASED_AT","CURRENT_ACCOUNT_USD","GDP_PCT","SOURCE_URL"]},
"valuation_snapshot":{"paths":["data/external/valuation_snapshot.csv"],"required":["DATE","SYMBOL","PE_TTM","PB","EV_EBITDA","MARKET_CAP","EPS_TTM"]},
"china_indicators":{"paths":["data/external/china_indicators.csv"],"required":["DATE","INDICATOR","VALUE","RELEASED_AT","SOURCE_URL"]},
"government_capex":{"paths":["data/external/government_capex.csv"],"required":["DATE","DEPARTMENT","ACTUAL_SPEND","BUDGET_SPEND","RELEASED_AT","SOURCE_URL"]},
"inflation_components":{"paths":["data/external/inflation_components.csv"],"required":["DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE_URL"]},
"sector_catalysts":{"paths":["data/external/sector_catalysts.csv"],"required":["DATE","SECTOR","SYMBOL","CATALYST_TYPE","PUBLISHED_AT","SOURCE_URL"]},
"domestic_policy_events":{"paths":["data/external/domestic_policy_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","AFFECTED_SECTOR","SOURCE_URL"]},
"shipping_route_risk":{"paths":["data/external/shipping_route_risk.csv"],"required":["DATE","ROUTE","STATUS","SOURCE_URL"]},
"earnings_revisions":{"paths":["data/external/earnings_revisions.csv"],"required":["DATE","SYMBOL","REVISION","PUBLISHED_AT"]},
"corporate_events":{"paths":["data/external/corporate_events.csv"],"required":["DATE","SYMBOL","EVENT_TYPE","PUBLISHED_AT","SOURCE_URL"]},
"geopolitical_events":{"paths":["data/external/geopolitical_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]},
"sector_fundamentals":{"paths":["data/external/sector_fundamentals.csv"],"required":["DATE","SECTOR","METRIC","VALUE"]},
"global_commodity_prices":{"paths":["data/external/commodity_prices.csv"],"required":["DATE","COMMODITY","CLOSE"]},
"market_microstructure":{"paths":["data/external/market_microstructure.csv"],"required":["DATE","SYMBOL","CIRCUIT_STATUS","SURVEILLANCE_STATUS"]},
"fx_carry_and_cross_currency":{"paths":["data/external/fx_carry.csv"],"required":["DATE","PAIR","VALUE"]},
"weather_agriculture":{"paths":["data/external/weather_agriculture.csv"],"required":["DATE","REGION","INDICATOR","VALUE"]},
"global_freight_shipping":{"paths":["data/external/freight_shipping.csv"],"required":["DATE","INDICATOR","VALUE"]},
"global_policy_events":{"paths":["data/external/global_policy_events.csv"],"required":["EVENT_DATE","PUBLISHED_AT","COUNTRY","EVENT_TYPE","SOURCE_URL"]},
"ipo_float_unlocks":{"paths":["data/external/ipo_float_unlocks.csv"],"required":["DATE","SYMBOL","EFFECTIVE_FLOAT","EVENT_TYPE"]},
"research_house_actions":{"paths":["data/external/research_house_actions.csv"],"required":["PUBLISHED_AT","SYMBOL","HOUSE","ACTION","SOURCE_URL"]},
}
def main():
    OUT.mkdir(parents=True,exist_ok=True); rows=[]
    now=pd.Timestamp.now(tz="UTC")
    for name,spec in SOURCES.items():
        path=next((ROOT/p for p in spec["paths"] if (ROOT/p).exists()),None)
        row={"source":name,"candidate_paths":";".join(spec["paths"]),"status":"NOT_CONNECTED","selected_path":"",
             "rows":0,"missing_columns":spec["required"],"date_min":None,"date_max":None,"age_days":None,
             "missing_cell_pct":None,"duplicate_key_rows":None,"invalid_date_rows":None,"invalid_timestamp_rows":None,
             "notes":"No source file found; absence is UNKNOWN, not NEGATIVE."}
        if path:
            row["selected_path"]=str(path)
            try:
                df=pd.read_csv(path); df.columns=[str(c).strip().upper() for c in df.columns]
                missing=sorted(set(spec["required"])-set(df.columns))
                row.update(rows=int(len(df)),missing_columns=missing,
                           missing_cell_pct=round(float(df.isna().sum().sum()/max(1,df.shape[0]*df.shape[1])*100),4),
                           invalid_date_rows=0,invalid_timestamp_rows=0,duplicate_key_rows=0)
                dcol=next((c for c in ["DATE","EVENT_DATE"] if c in df.columns),None)
                if dcol and len(df):
                    parsed=pd.to_datetime(df[dcol],errors="coerce")
                    row["invalid_date_rows"]=int(parsed.isna().sum())
                    valid=parsed.dropna()
                    if len(valid):
                        latest=valid.max()
                        row.update(date_min=str(valid.min().date()),date_max=str(latest.date()),age_days=max(0,int((now.tz_localize(None)-latest).days)))
                key=next((k for k in [["DATE","SYMBOL"],["DATE","SERIES"],["DATE","COMMODITY"],["DATE","INDICATOR"],["EVENT_ID"],["EVENT_DATE","EVENT_TYPE","SOURCE_URL"]] if set(k).issubset(df.columns)),None)
                if key: row["duplicate_key_rows"]=int(df.duplicated(key).sum())
                if "PUBLISHED_AT" in df.columns:
                    ts=pd.to_datetime(df["PUBLISHED_AT"],errors="coerce",utc=True)
                    row["invalid_timestamp_rows"]=int(ts.isna().sum())
                quality_issues=[]
                if df.empty: quality_issues.append("source file exists but contains zero data rows")
                if missing: quality_issues.append("missing required columns")
                if row["duplicate_key_rows"] not in (None,0): quality_issues.append("duplicate keys")
                if row["invalid_date_rows"] not in (None,0): quality_issues.append("invalid dates")
                if row["invalid_timestamp_rows"] not in (None,0): quality_issues.append("invalid publication timestamps")
                if row["missing_cell_pct"] is not None and row["missing_cell_pct"]>5: quality_issues.append("more than 5% missing cells")
                status="SCHEMA_FAIL" if missing else ("DATA_QUALITY_WARN" if quality_issues else "AVAILABLE")
                row.update(status=status,notes="; ".join(quality_issues) if quality_issues else "Generic QA passed; units, source authenticity, revisions, market-calendar alignment and point-in-time leakage still need domain-specific checks.")
            except Exception as e: row.update(status="READ_ERROR",notes=f"Could not read file: {type(e).__name__}: {e}")
        rows.append(row)
    frame=pd.DataFrame(rows)
    # Explicitly distinguish the P0 decision-support backbone from the wider
    # optional context inventory. A file's presence is not proof of officialness.
    by_name={r["source"]:r for r in rows}
    p0_required=["benchmark_index","sector_indices","volatility","crude_oil","usd_inr","fpi_dii_flows","corporate_events","geopolitical_events"]
    p0_rows={name:{"status":by_name.get(name,{}).get("status","NOT_CONNECTED"),
                   "rows":by_name.get(name,{}).get("rows",0),
                   "selected_path":by_name.get(name,{}).get("selected_path","")} for name in p0_required}
    p0_available=[name for name,info in p0_rows.items() if info["status"]=="AVAILABLE" and info["rows"]>0]
    report={"status":"INVENTORY_COMPLETE_WITH_GAPS" if (frame.status!="AVAILABLE").any() else "SCHEMA_AND_GENERIC_QA_AVAILABLE",
            "as_of_utc":now.isoformat(),"sources_total":len(rows),"available":int((frame.status=="AVAILABLE").sum()),
            "not_connected":int((frame.status=="NOT_CONNECTED").sum()),"schema_fail":int((frame.status=="SCHEMA_FAIL").sum()),
            "quality_warn":int((frame.status=="DATA_QUALITY_WARN").sum()),"read_error":int((frame.status=="READ_ERROR").sum()),
            "p0_coverage":{"required_groups":p0_required,"available_groups":p0_available,
                "available_count":len(p0_available),"required_count":len(p0_required),
                "status":"P0_COMPLETE" if len(p0_available)==len(p0_required) else "P0_INCOMPLETE",
                "groups":p0_rows,
                "boundary":"AVAILABLE means file/schema/generic QA only; secondary-source provenance and point-in-time validity remain separately qualified."},
            "important_boundary":"This is a source inventory and generic QA only. It does not imply live-feed connectivity, verified units, causal validity or complete 20-year history. Missing data remains UNKNOWN.",
            "sources":rows}
    REPORT.write_text(json.dumps(report,indent=2)); frame.to_csv(OUT/"source_coverage.csv",index=False)
    print(json.dumps({k:report[k] for k in ["status","sources_total","available","not_connected","schema_fail","quality_warn","read_error"]}))
if __name__=="__main__": main()
