#!/usr/bin/env python3
"""Fetch genuine long-range NSE Indices history for registered historical regimes.

No synthetic fills are allowed. Existing market data for series not returned by
the official historical endpoint is preserved; fetched observations replace
same (DATE, SERIES) keys and retain source URL and observation timestamp.
"""
from pathlib import Path
import importlib.util, json
import pandas as pd

ROOT=Path(".")
PANEL=ROOT/"data/external/market_panel.csv"
REGIMES=ROOT/"config/macro_geo_historical_regimes.csv"
OUT=ROOT/"outputs/macro_geo"
COLLECTOR=ROOT/"pipeline/macro_geo_collect_p0.py"
REQUIRED_SERIES={"NIFTY 50","NIFTY IT","NIFTY BANK","NIFTY AUTO","NIFTY METAL","NIFTY PHARMA","NIFTY ENERGY","NIFTY FMCG","NIFTY REALTY","NIFTY INFRA","INDIA VIX"}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not REGIMES.exists():
        raise SystemExit("Historical regime registry missing; refusing to infer anchors.")
    regimes=pd.read_csv(REGIMES)
    dates=pd.to_datetime(regimes["start_date"],errors="coerce").dropna()
    if dates.empty:
        raise SystemExit("No valid historical regime start dates.")
    start=dates.min().date()
    if not PANEL.exists():
        raise SystemExit("Current market_panel.csv missing; no synthetic panel will be created.")
    existing=pd.read_csv(PANEL)
    existing.columns=[str(c).strip().upper() for c in existing.columns]
    if not {"DATE","SERIES","CLOSE"}.issubset(existing.columns):
        raise SystemExit("Existing market panel schema invalid.")
    existing["DATE"]=pd.to_datetime(existing["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
    end=pd.to_datetime(existing["DATE"],errors="coerce").max()
    if pd.isna(end): raise SystemExit("Existing market panel has no valid dates.")
    spec=importlib.util.spec_from_file_location("macro_geo_collect_p0",COLLECTOR)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    records,detail=mod.niftyindices_history(start,end.date())
    fetched=pd.DataFrame(records)
    if not fetched.empty:
        fetched.columns=[str(c).strip().upper() for c in fetched.columns]
        fetched["DATE"]=pd.to_datetime(fetched["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
        fetched["CLOSE"]=pd.to_numeric(fetched["CLOSE"],errors="coerce")
        fetched=fetched.dropna(subset=["DATE","SERIES","CLOSE"])
        fetched=fetched[fetched["CLOSE"]>0]
        fetched=fetched.drop_duplicates(["DATE","SERIES"],keep="last")
    if not fetched.empty:
        # Preserve other sources/series, while official fetched rows supersede duplicate keys.
        keys=set(zip(fetched["DATE"],fetched["SERIES"]))
        old=existing[~existing.apply(lambda r:(r["DATE"],r["SERIES"]) in keys,axis=1)]
        merged=pd.concat([old,fetched],ignore_index=True,sort=False)
        merged=merged.drop_duplicates(["DATE","SERIES"],keep="last").sort_values(["DATE","SERIES"])
        merged.to_csv(PANEL,index=False)
    else:
        merged=existing
    summary=[]
    for name in sorted(REQUIRED_SERIES):
        g=merged[merged["SERIES"].astype(str).str.upper().eq(name)]
        ds=pd.to_datetime(g["DATE"],errors="coerce").dropna()
        summary.append({"series":name,"rows":int(len(g)),"date_min":str(ds.min().date()) if len(ds) else None,
          "date_max":str(ds.max().date()) if len(ds) else None,"covers_first_anchor":bool(len(ds) and ds.min().date()<=start)})
    missing=[x["series"] for x in summary if not x["covers_first_anchor"]]
    report={"status":"HISTORICAL_SERIES_COLLECTED" if not missing else "HISTORICAL_COVERAGE_INCOMPLETE",
      "source":"NSE Indices historical data API / NSE Indices India VIX historical API",
      "requested_start":start.isoformat(),"requested_end":end.date().isoformat(),
      "fetched_rows":int(len(fetched)),"fetched_series":int(fetched["SERIES"].nunique()) if not fetched.empty else 0,
      "series_coverage":summary,"missing_anchor_coverage":missing,"endpoint_diagnostics":detail,
      "limitations":["Historical dates and closes are only accepted from returned source records; no interpolation or synthetic values.",
        "Regime anchors remain provisional until independently verified against primary-source event records.",
        "Coverage of the first anchor date does not by itself validate the event window or causal interpretation."]}
    (OUT/"historical_index_backfill_report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    # This step records partial coverage; the hard gate remains responsible for blocking incomplete research.
    return 0

if __name__=="__main__": raise SystemExit(main())
