#!/usr/bin/env python3
"""Inventory macro/geo/sector source coverage without fabricating missing data."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(".")
OUT = Path("outputs/macro_geo")
REPORT = OUT / "source_coverage.json"
# These are logical datasets, not claims that providers are connected.
SOURCES = {
    "nse_daily_equity": {"paths": ["data/processed/nse_eq_200_sessions.csv"], "required": ["DATE","SYMBOL","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]},
    "sector_indices": {"paths": ["data/external/sector_indices.csv", "data/context/sector_indices.csv"], "required": ["DATE","SERIES","CLOSE"]},
    "benchmark_index": {"paths": ["data/external/benchmark_indices.csv", "data/context/benchmark_indices.csv"], "required": ["DATE","SERIES","CLOSE"]},
    "crude_oil": {"paths": ["data/external/brent_crude.csv", "data/context/brent_crude.csv"], "required": ["DATE","CLOSE"]},
    "usd_inr": {"paths": ["data/external/usd_inr.csv", "data/context/usd_inr.csv"], "required": ["DATE","CLOSE"]},
    "us_yields": {"paths": ["data/external/us_yields.csv", "data/context/us_yields.csv"], "required": ["DATE","US2Y","US10Y"]},
    "dxy": {"paths": ["data/external/dxy.csv", "data/context/dxy.csv"], "required": ["DATE","CLOSE"]},
    "volatility": {"paths": ["data/external/volatility.csv", "data/context/volatility.csv"], "required": ["DATE","SERIES","CLOSE"]},
    "fpi_dii_flows": {"paths": ["data/external/fpi_dii_flows.csv", "data/context/fii_dii.csv"], "required": ["DATE","GROUP","NET_VALUE"]},
    "india_bond_yields": {"paths": ["data/external/india_bond_yields.csv", "data/context/india_bond_yields.csv"], "required": ["DATE","YIELD_10Y"]},
    "rbi_policy_liquidity": {"paths": ["data/external/rbi_policy_liquidity.csv"], "required": ["DATE","REPO_RATE","POLICY_SURPRISE"]},
    "macro_indicators": {"paths": ["data/external/macro_indicators.csv"], "required": ["DATE","INDICATOR","VALUE"]},
    "earnings_revisions": {"paths": ["data/external/earnings_revisions.csv"], "required": ["DATE","SYMBOL","REVISION","PUBLISHED_AT"]},
    "corporate_events": {"paths": ["data/external/corporate_events.csv"], "required": ["DATE","SYMBOL","EVENT_TYPE","PUBLISHED_AT","SOURCE_URL"]},
    "geopolitical_events": {"paths": ["data/external/geopolitical_events.csv"], "required": ["EVENT_DATE","PUBLISHED_AT","EVENT_TYPE","SOURCE","SOURCE_URL","CONFIDENCE"]},
    "sector_fundamentals": {"paths": ["data/external/sector_fundamentals.csv"], "required": ["DATE","SECTOR","METRIC","VALUE"]},
    "global_commodity_prices": {"paths": ["data/external/commodity_prices.csv"], "required": ["DATE","COMMODITY","CLOSE"]},
    "market_microstructure": {"paths": ["data/external/market_microstructure.csv"], "required": ["DATE","SYMBOL","CIRCUIT_STATUS","SURVEILLANCE_STATUS"]},
}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows=[]
    for name, spec in SOURCES.items():
        candidates=[ROOT / p for p in spec["paths"]]
        path=next((p for p in candidates if p.exists()), None)
        row={"source":name,"candidate_paths":";".join(spec["paths"]),"status":"NOT_CONNECTED","selected_path":"","rows":0,"missing_columns":spec["required"],"date_min":None,"date_max":None,"notes":"No source file found; absence is UNKNOWN, not NEGATIVE."}
        if path:
            row["selected_path"]=str(path)
            try:
                df=pd.read_csv(path)
                cols={str(c).strip().upper() for c in df.columns}
                missing=sorted(set(spec["required"])-cols)
                row.update(status="SCHEMA_FAIL" if missing else "AVAILABLE",rows=int(len(df)),missing_columns=missing,
                           notes="Required schema missing." if missing else "Schema present; freshness, provenance, units and point-in-time integrity still require validation.")
                date_col=next((c for c in df.columns if str(c).strip().upper() in {"DATE","EVENT_DATE"}),None)
                if date_col and len(df):
                    dates=pd.to_datetime(df[date_col],errors="coerce").dropna()
                    if len(dates): row.update(date_min=str(dates.min().date()),date_max=str(dates.max().date()))
            except Exception as e:
                row.update(status="READ_ERROR",notes=f"Could not read file: {type(e).__name__}: {e}")
        rows.append(row)
    frame=pd.DataFrame(rows)
    report={"status":"INVENTORY_COMPLETE_WITH_GAPS" if (frame.status!="AVAILABLE").any() else "SCHEMA_COVERAGE_AVAILABLE",
            "as_of_utc":pd.Timestamp.now(tz="UTC").isoformat(),"sources_total":len(rows),
            "available":int((frame.status=="AVAILABLE").sum()),"not_connected":int((frame.status=="NOT_CONNECTED").sum()),
            "schema_fail":int((frame.status=="SCHEMA_FAIL").sum()),"read_error":int((frame.status=="READ_ERROR").sum()),
            "important_boundary":"Schema availability is not proof of data quality or live connectivity. Missing data remains UNKNOWN.",
            "sources":rows}
    REPORT.write_text(json.dumps(report,indent=2))
    frame.to_csv(OUT/"source_coverage.csv",index=False)
    print(json.dumps({k:report[k] for k in ["status","sources_total","available","not_connected","schema_fail","read_error"]}))
if __name__=="__main__": main()
