#!/usr/bin/env python3
"""Date-anchor historical regime study. Exploratory only; not a causal estimator or selector."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT=Path(".")
PANEL=ROOT/"data/external/market_panel.csv"
REGIMES=ROOT/"config/macro_geo_historical_regimes.csv"
OUT=ROOT/"outputs/macro_geo"
HORIZONS=(1,5,20)
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not PANEL.exists() or not REGIMES.exists():
        report={"status":"BLOCKED_MISSING_INPUTS","reason":"Need historical market_panel.csv and macro_geo_historical_regimes.csv; no synthetic prices created."}
        (OUT/"historical_regime_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    panel=pd.read_csv(PANEL); panel.columns=[str(c).strip().upper() for c in panel.columns]
    regimes=pd.read_csv(REGIMES); regimes.columns=[str(c).strip().upper() for c in regimes.columns]
    need={"DATE","SERIES","CLOSE"}
    if need-set(panel.columns):
        report={"status":"BLOCKED_SCHEMA","missing_panel_columns":sorted(need-set(panel.columns))}
        (OUT/"historical_regime_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    panel["DATE"]=pd.to_datetime(panel["DATE"],errors="coerce").dt.normalize()
    panel["CLOSE"]=pd.to_numeric(panel["CLOSE"],errors="coerce")
    panel=panel.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    panel=panel[panel.CLOSE>0]
    if panel.duplicated(["DATE","SERIES"]).any():
        report={"status":"BLOCKED_DUPLICATE_PANEL_KEYS","duplicate_rows":int(panel.duplicated(["DATE","SERIES"]).sum())}
        (OUT/"historical_regime_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    rows=[]; coverage=[]
    for _,r in regimes.iterrows():
        start=pd.to_datetime(r["START_DATE"],errors="coerce")
        end=pd.to_datetime(r["END_DATE"],errors="coerce")
        if pd.isna(start) or pd.isna(end) or start>end: continue
        for series,g0 in panel.groupby("SERIES"):
            g=g0.reset_index(drop=True)
            ix=np.flatnonzero(g.DATE.to_numpy()>=np.datetime64(start.normalize()))
            if not len(ix):
                coverage.append({"REGIME_ID":r["REGIME_ID"],"REGIME_LABEL":r["REGIME_LABEL"],"SERIES":series,"STATUS":"NO_PANEL_AFTER_ANCHOR","PANEL_START":str(g.DATE.min().date()),"PANEL_END":str(g.DATE.max().date())})
                continue
            event_i=int(ix[0]); base_i=event_i-1
            if base_i<0:
                coverage.append({"REGIME_ID":r["REGIME_ID"],"REGIME_LABEL":r["REGIME_LABEL"],"SERIES":series,"STATUS":"NO_PRE_EVENT_BASE","PANEL_START":str(g.DATE.min().date()),"PANEL_END":str(g.DATE.max().date())})
                continue
            rec={"REGIME_ID":r["REGIME_ID"],"REGIME_LABEL":r["REGIME_LABEL"],"SERIES":series,
              "REGIME_START":start.date().isoformat(),"REGIME_END":end.date().isoformat(),
              "ANCHOR_QUALITY":r.get("ANCHOR_QUALITY","DATE_ONLY_REGIME_ANCHOR"),
              "SOURCE_STATUS":r.get("SOURCE_STATUS","NEEDS_PRIMARY_SOURCE_LINKS"),
              "BASE_DATE":g.iloc[base_i].DATE.date().isoformat(),"BASE_CLOSE":float(g.iloc[base_i].CLOSE),
              "FIRST_SESSION_ON_OR_AFTER_ANCHOR":g.iloc[event_i].DATE.date().isoformat()}
            for h in HORIZONS:
                j=event_i+h-1
                if j<len(g):
                    rec[f"TARGET_DATE_H{h}"]=g.iloc[j].DATE.date().isoformat()
                    rec[f"RETURN_H{h}_PCT"]=float((g.iloc[j].CLOSE/g.iloc[base_i].CLOSE-1)*100)
                else:
                    rec[f"TARGET_DATE_H{h}"]=""; rec[f"RETURN_H{h}_PCT"]=np.nan
            rows.append(rec)
            coverage.append({"REGIME_ID":r["REGIME_ID"],"REGIME_LABEL":r["REGIME_LABEL"],"SERIES":series,"STATUS":"WINDOWS_COMPUTED" if len(g)>event_i+19 else "PARTIAL_HORIZONS","PANEL_START":str(g.DATE.min().date()),"PANEL_END":str(g.DATE.max().date())})
    result=pd.DataFrame(rows)
    if not result.empty and "NIFTY 50" in set(result.SERIES):
        b=result[result.SERIES.eq("NIFTY 50")][["REGIME_ID"]+[f"RETURN_H{h}_PCT" for h in HORIZONS]].drop_duplicates("REGIME_ID")
        b=b.rename(columns={f"RETURN_H{h}_PCT":f"NIFTY_RETURN_H{h}_PCT" for h in HORIZONS})
        result=result.merge(b,on="REGIME_ID",how="left",validate="many_to_one")
        for h in HORIZONS:
            result[f"ABNORMAL_RETURN_H{h}_PCT"]=result[f"RETURN_H{h}_PCT"]-result[f"NIFTY_RETURN_H{h}_PCT"]
    result.to_csv(OUT/"historical_regime_study_windows.csv",index=False)
    pd.DataFrame(coverage).to_csv(OUT/"historical_regime_coverage.csv",index=False)
    summary=[]
    if not result.empty:
        for (regime,series),g in result.groupby(["REGIME_LABEL","SERIES"]):
            for col in [f"RETURN_H{h}_PCT" for h in HORIZONS]+[f"ABNORMAL_RETURN_H{h}_PCT" for h in HORIZONS if f"ABNORMAL_RETURN_H{h}_PCT" in result.columns]:
                v=pd.to_numeric(g[col],errors="coerce").dropna().to_numpy(float)
                summary.append({"REGIME_LABEL":regime,"SERIES":series,"METRIC":col,"N_REGIME_ANCHORS":len(v),
                  "MEAN_PCT":float(v.mean()) if len(v) else None,"MEDIAN_PCT":float(np.median(v)) if len(v) else None,
                  "NOTE":"One anchor per regime is not a repeated-sample estimate; no causal inference."})
    pd.DataFrame(summary).to_csv(OUT/"historical_regime_study_summary.csv",index=False)
    start=panel.DATE.min().date().isoformat() if not panel.empty else None
    end=panel.DATE.max().date().isoformat() if not panel.empty else None
    regimes_covered=int(result.REGIME_ID.nunique()) if not result.empty else 0
    report={"status":"COMPUTED_EXPLORATORY" if not result.empty else "BLOCKED_NO_MATCHING_REGIMES",
      "research_status":"COMPUTED_EXPLORATORY" if not result.empty else "BLOCKED",
      "operational_status":"PASS" if not result.empty else "PASS_WITH_RESEARCH_BLOCKED",
      "panel_rows":len(panel),"panel_series":int(panel.SERIES.nunique()) if not panel.empty else 0,
      "panel_start":start,"panel_end":end,"regime_anchors":len(regimes),"regimes_with_windows":regimes_covered,
      "window_rows":len(result),"coverage_rows":len(coverage),
      "method":"Date-only regime anchor; baseline is previous available close; H+1/H+5/H+20 are first/5th/20th closes on or after anchor session.",
      "limitations":["Regime date anchors are provisional and require primary-source verification.","Single historical episodes do not provide repeated-sample inference.","No matched controls, overlap correction, multiple-testing adjustment or causal identification.","A 20-year study is incomplete unless the panel itself covers the full requested window and relevant series start dates.","No factor scoring or production ranking integration."]}
    (OUT/"historical_regime_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
