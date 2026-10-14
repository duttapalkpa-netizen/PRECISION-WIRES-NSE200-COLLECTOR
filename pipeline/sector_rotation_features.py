#!/usr/bin/env python3
"""Calculate historical sector-relative returns/ranks from the market panel; descriptive, no prediction."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path("."); PANEL=ROOT/"data/external/market_panel.csv"; OUT=ROOT/"outputs/macro_geo"
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not PANEL.exists():
        report={"status":"BLOCKED_MISSING_PANEL","reason":"market_panel.csv missing; no synthetic data created."}
        (OUT/"sector_rotation_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    df=pd.read_csv(PANEL); df.columns=[str(c).strip().upper() for c in df.columns]
    required={"DATE","SERIES","CLOSE"}
    if required-set(df.columns):
        report={"status":"BLOCKED_SCHEMA","missing_columns":sorted(required-set(df.columns))}
        (OUT/"sector_rotation_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    df["DATE"]=pd.to_datetime(df["DATE"],errors="coerce")
    df["CLOSE"]=pd.to_numeric(df["CLOSE"],errors="coerce")
    df=df.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    df=df[df.CLOSE>0]
    if df.duplicated(["DATE","SERIES"]).any():
        report={"status":"BLOCKED_DUPLICATES","duplicate_rows":int(df.duplicated(["DATE","SERIES"]).sum())}
        (OUT/"sector_rotation_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    frames=[]
    for series,g in df.groupby("SERIES"):
        g=g.copy()
        for h in (1,5,20,60):
            g[f"RETURN_{h}D_PCT"]=(g.CLOSE/g.CLOSE.shift(h)-1)*100
        g["SERIES"]=series
        frames.append(g)
    out=pd.concat(frames,ignore_index=True)
    if "NIFTY 50" not in set(out.SERIES):
        report={"status":"BLOCKED_NO_BENCHMARK","series":sorted(out.SERIES.unique().tolist())}
        (OUT/"sector_rotation_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    bench=out[out.SERIES.eq("NIFTY 50")][["DATE"]+[f"RETURN_{h}D_PCT" for h in (1,5,20,60)]].copy()
    bench=bench.rename(columns={f"RETURN_{h}D_PCT":f"NIFTY_RETURN_{h}D_PCT" for h in (1,5,20,60)})
    out=out.merge(bench,on="DATE",how="left",validate="many_to_one")
    for h in (1,5,20,60):
        out[f"RELATIVE_RETURN_{h}D_PCT"]=out[f"RETURN_{h}D_PCT"]-out[f"NIFTY_RETURN_{h}D_PCT"]
        out[f"SECTOR_RS_RANK_{h}D"]=out.groupby("DATE")[f"RELATIVE_RETURN_{h}D_PCT"].rank(ascending=False,method="min")
    out["IS_SECTOR_INDEX"]=out.SERIES.str.startswith("NIFTY ") & ~out.SERIES.eq("NIFTY 50")
    out.to_csv(OUT/"sector_rotation_daily.csv",index=False)
    latest=out[out.IS_SECTOR_INDEX].sort_values("DATE").groupby("SERIES",as_index=False).tail(1)
    report={"status":"COMPUTED_DESCRIPTIVE","panel_start":out.DATE.min().date().isoformat(),"panel_end":out.DATE.max().date().isoformat(),
      "panel_rows":len(out),"series":int(out.SERIES.nunique()),"sector_series":int(out[out.IS_SECTOR_INDEX].SERIES.nunique()),
      "latest_sector_snapshot":latest[["DATE","SERIES","RETURN_5D_PCT","RETURN_20D_PCT","RETURN_60D_PCT","RELATIVE_RETURN_20D_PCT","SECTOR_RS_RANK_20D"]].to_dict("records"),
      "limitations":["Ranks are descriptive historical relative returns, not forward predictions.","Sector index start dates differ; rankings only compare available rows on each date.","No stock-level valuation, earnings revisions or point-in-time fundamentals included.","No production ranking integration."]}
    (OUT/"sector_rotation_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
