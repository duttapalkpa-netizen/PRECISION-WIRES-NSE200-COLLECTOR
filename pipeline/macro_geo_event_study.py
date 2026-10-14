#!/usr/bin/env python3
"""Publication-time event study; descriptive only, not causal or a ranking engine."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

PANEL=Path("data/external/market_panel.csv")
EVENTS=Path("data/external/events.csv")
OUT=Path("outputs/macro_geo")
WINDOWS=(1,5,20)
IST="Asia/Kolkata"

def load_inputs(panel_path=PANEL, events_path=EVENTS):
    if not panel_path.exists() or not events_path.exists():
        return None,None,"Missing input: provide market_panel.csv and events.csv."
    panel=pd.read_csv(panel_path); events=pd.read_csv(events_path)
    panel.columns=[str(c).strip().upper() for c in panel.columns]
    events.columns=[str(c).strip().upper() for c in events.columns]
    needp={"DATE","SERIES","CLOSE"}
    neede={"EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","CONFIDENCE"}
    if needp-set(panel.columns): return None,None,"Panel missing columns: "+",".join(sorted(needp-set(panel.columns)))
    if neede-set(events.columns): return None,None,"Events missing columns: "+",".join(sorted(neede-set(events.columns)))
    panel["DATE"]=pd.to_datetime(panel["DATE"],errors="coerce").dt.normalize()
    panel["CLOSE"]=pd.to_numeric(panel["CLOSE"],errors="coerce")
    events["EVENT_DATE"]=pd.to_datetime(events["EVENT_DATE"],errors="coerce").dt.normalize()
    events["PUBLISHED_AT"]=pd.to_datetime(events["PUBLISHED_AT"],errors="coerce",utc=True)
    events["CONFIDENCE"]=pd.to_numeric(events["CONFIDENCE"],errors="coerce")
    panel=panel.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    events=events.dropna(subset=["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT"])
    if panel.empty: return None,None,"Market panel contains no valid rows."
    if (panel["CLOSE"]<=0).any(): return None,None,"Non-positive close detected."
    if panel.duplicated(["DATE","SERIES"]).any(): return None,None,"Duplicate DATE+SERIES rows detected."
    if events["EVENT_ID"].duplicated().any(): return None,None,"Duplicate EVENT_ID rows detected; deduplicate before study."
    return panel,events,None

def compute_event_windows(panel, events):
    rows=[]
    for series,g0 in panel.groupby("SERIES"):
        g=g0.reset_index(drop=True)
        dates=[pd.Timestamp(d).date() for d in g["DATE"]]
        closes=[pd.Timestamp(d).tz_localize(IST)+pd.Timedelta(hours=15,minutes=30) for d in g["DATE"]]
        for _,ev in events.iterrows():
            pub=ev["PUBLISHED_AT"].tz_convert(IST)
            base_candidates=[i for i,ts in enumerate(closes) if ts<=pub]
            post_candidates=[i for i,ts in enumerate(closes) if ts>pub]
            if not base_candidates or not post_candidates: continue
            base_i=base_candidates[-1]
            rec={"EVENT_ID":ev["EVENT_ID"],"EVENT_TYPE":ev["EVENT_TYPE"],"EVENT_DATE":ev["EVENT_DATE"].date().isoformat(),
                 "SERIES":series,"SOURCE":ev.get("SOURCE",""),"SOURCE_URL":ev.get("SOURCE_URL",""),
                 "TITLE":ev.get("TITLE",""),"CONFIDENCE":ev.get("CONFIDENCE",np.nan),
                 "PUBLISHED_AT":ev["PUBLISHED_AT"].isoformat(),"EVENT_DATE_BASIS":ev.get("EVENT_DATE_BASIS","UNSPECIFIED"),
                 "BASE_DATE":dates[base_i].isoformat(),"PUBLICATION_IST":pub.isoformat(),"BASE_CLOSE":float(g.iloc[base_i]["CLOSE"])}
            for h in WINDOWS:
                if h<=len(post_candidates):
                    j=post_candidates[h-1]
                    rec[f"TARGET_DATE_H{h}"]=dates[j].isoformat()
                    rec[f"RETURN_H{h}_PCT"]=float((g.iloc[j]["CLOSE"]/g.iloc[base_i]["CLOSE"]-1)*100)
                else:
                    rec[f"TARGET_DATE_H{h}"]=""
                    rec[f"RETURN_H{h}_PCT"]=np.nan
            rows.append(rec)
    result=pd.DataFrame(rows)
    if result.empty: return result
    # Simple same-event NIFTY 50 subtraction; descriptive proxy, not a causal model.
    if "NIFTY 50" in set(result["SERIES"]):
        b=result[result.SERIES.eq("NIFTY 50")][["EVENT_ID"]+[f"RETURN_H{h}_PCT" for h in WINDOWS]].copy()
        b=b.rename(columns={f"RETURN_H{h}_PCT":f"BENCHMARK_RETURN_H{h}_PCT" for h in WINDOWS})
        result=result.merge(b,on="EVENT_ID",how="left",validate="many_to_one")
        for h in WINDOWS: result[f"ABNORMAL_RETURN_H{h}_PCT"]=result[f"RETURN_H{h}_PCT"]-result[f"BENCHMARK_RETURN_H{h}_PCT"]
    return result

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    panel,events,error=load_inputs()
    if error:
        report={"status":"BLOCKED_MISSING_OR_INVALID_INPUTS","reason":error,"required_panel":str(PANEL),"required_events":str(EVENTS),"note":"No synthetic market result was substituted."}
        (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
    results=compute_event_windows(panel,events)
    results.to_csv(OUT/"event_study_windows.csv",index=False)
    summary=[]
    if not results.empty:
        metrics=[f"RETURN_H{h}_PCT" for h in WINDOWS]+[f"ABNORMAL_RETURN_H{h}_PCT" for h in WINDOWS if f"ABNORMAL_RETURN_H{h}_PCT" in results.columns]
        for (typ,series),g in results.groupby(["EVENT_TYPE","SERIES"]):
            for col in metrics:
                vals=pd.to_numeric(g[col],errors="coerce").dropna()
                summary.append({"EVENT_TYPE":typ,"SERIES":series,"METRIC":col,"N_EVENTS":len(vals),
                    "MEAN_PCT":float(vals.mean()) if len(vals) else None,"MEDIAN_PCT":float(vals.median()) if len(vals) else None,
                    "STD_PCT":float(vals.std(ddof=1)) if len(vals)>1 else None})
    pd.DataFrame(summary).to_csv(OUT/"event_study_summary.csv",index=False)
    report={"status":"COMPUTED_EXPLORATORY" if not results.empty else "NO_MATCHING_EVENT_WINDOWS",
        "panel_rows":len(panel),"panel_series":int(panel.SERIES.nunique()),"event_rows":len(events),"window_rows":len(results),
        "series":sorted(panel.SERIES.unique().tolist()),
        "publication_time_rule":"Baseline is last 15:30 Asia/Kolkata close at/before PUBLISHED_AT; H+1/H+5/H+20 are the 1st/5th/20th closes strictly after publication.",
        "benchmark_adjustment":"Same-event NIFTY 50 return subtraction when available; descriptive only.",
        "limitations":["GDELT publication timestamp is a news-mention proxy, not verified event occurrence.","News-selection bias and overlapping windows remain.","No matched controls, confidence intervals or multiple-testing correction yet.","Yahoo Finance is a secondary market-data source; validate against official/licensed sources before production."],
        "warning":"Exploratory only; no ranking integration."}
    (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
if __name__=="__main__": raise SystemExit(main())
