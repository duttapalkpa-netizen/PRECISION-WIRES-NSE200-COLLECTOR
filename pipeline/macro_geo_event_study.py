#!/usr/bin/env python3
"""Reproducible event-window study for market/sector index panels; exploratory only.

Expected data/external/market_panel.csv: DATE,SERIES,CLOSE
Expected data/external/events.csv: EVENT_DATE,EVENT_ID,EVENT_TYPE,PUBLISHED_AT,SOURCE,CONFIDENCE
Optional benchmark series name: NIFTY 50. No post-event headline timestamp is allowed to masquerade as known pre-close information.
"""
from pathlib import Path
from datetime import time as clock_time
import json
import numpy as np
import pandas as pd

PANEL=Path("data/external/market_panel.csv")
EVENTS=Path("data/external/events.csv")
OUT=Path("outputs/macro_geo")
WINDOWS=(1,5,20)

def load_inputs(panel_path=PANEL, events_path=EVENTS):
    if not panel_path.exists() or not events_path.exists():
        return None, None, "Missing input: provide market_panel.csv and events.csv."
    panel=pd.read_csv(panel_path)
    events=pd.read_csv(events_path)
    panel.columns=[str(c).strip().upper() for c in panel.columns]
    events.columns=[str(c).strip().upper() for c in events.columns]
    needp={"DATE","SERIES","CLOSE"}; neede={"EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","CONFIDENCE"}
    if needp-set(panel.columns): return None,None,"Panel missing columns: "+",".join(sorted(needp-set(panel.columns)))
    if neede-set(events.columns): return None,None,"Events missing columns: "+",".join(sorted(neede-set(events.columns)))
    panel["DATE"]=pd.to_datetime(panel["DATE"],errors="coerce")
    panel["CLOSE"]=pd.to_numeric(panel["CLOSE"],errors="coerce")
    events["EVENT_DATE"]=pd.to_datetime(events["EVENT_DATE"],errors="coerce")
    events["PUBLISHED_AT"]=pd.to_datetime(events["PUBLISHED_AT"],errors="coerce",utc=True)
    events["CONFIDENCE"]=pd.to_numeric(events["CONFIDENCE"],errors="coerce")
    panel=panel.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    events=events.dropna(subset=["EVENT_DATE","EVENT_ID","EVENT_TYPE"])
    if (panel["CLOSE"]<=0).any(): return None,None,"Non-positive close detected."
    if panel.duplicated(["DATE","SERIES"]).any(): return None,None,"Duplicate DATE+SERIES rows detected."
    return panel,events,None

def compute_event_windows(panel, events):
    rows=[]
    series_map={s:g.reset_index(drop=True) for s,g in panel.groupby("SERIES")}
    for _,ev in events.iterrows():
        for series,g in series_map.items():
            dates=g["DATE"].tolist()
            # Event windows are anchored to first trading session on/after event date.
            pos=int(np.searchsorted(np.array(dates,dtype="datetime64[ns]"),np.datetime64(ev["EVENT_DATE"])))
            if pos>=len(g) or pos==0: continue
            # Event-date reaction is only interpretable if event timestamp precedes that market's close.
            event_ts=ev.get("PUBLISHED_AT",pd.NaT)
            known_before_close=bool(pd.notna(event_ts) and event_ts.tz_convert("Asia/Kolkata").date() <= dates[pos].date() and
                                    (event_ts.tz_convert("Asia/Kolkata").date() < dates[pos].date() or event_ts.tz_convert("Asia/Kolkata").time().replace(tzinfo=None) <= clock_time(15, 30)))
            base=float(g.iloc[pos-1]["CLOSE"])
            rec={"EVENT_ID":ev["EVENT_ID"],"EVENT_TYPE":ev["EVENT_TYPE"],"EVENT_DATE":ev["EVENT_DATE"].date().isoformat(),
                 "SERIES":series,"SOURCE":ev.get("SOURCE",""),"CONFIDENCE":ev.get("CONFIDENCE",np.nan),
                 "PUBLISHED_AT":event_ts.isoformat() if pd.notna(event_ts) else "",
                 "KNOWN_BEFORE_SESSION":known_before_close,"BASE_DATE":dates[pos-1].date().isoformat()}
            for h in WINDOWS:
                j=pos+h-1
                rec[f"RETURN_H{h}_PCT"]=float((g.iloc[j]["CLOSE"]/base-1)*100) if j<len(g) else np.nan
            rows.append(rec)
    return pd.DataFrame(rows)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    panel,events,error=load_inputs()
    if error:
        report={"status":"BLOCKED_MISSING_OR_INVALID_INPUTS","reason":error,
                "required_panel":str(PANEL),"required_events":str(EVENTS),
                "note":"No synthetic market result was substituted. Add timestamped, sourced input files to run the study."}
        (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2))
        print(json.dumps(report))
        return 0
    results=compute_event_windows(panel,events)
    results.to_csv(OUT/"event_study_windows.csv",index=False)
    summary=[]
    if not results.empty:
        for (typ,series),g in results.groupby(["EVENT_TYPE","SERIES"]):
            for col in [f"RETURN_H{h}_PCT" for h in WINDOWS]:
                vals=pd.to_numeric(g[col],errors="coerce").dropna()
                summary.append({"EVENT_TYPE":typ,"SERIES":series,"HORIZON":col,
                                "N_EVENTS":int(len(vals)),"MEAN_RETURN_PCT":float(vals.mean()) if len(vals) else None,
                                "MEDIAN_RETURN_PCT":float(vals.median()) if len(vals) else None,
                                "STD_RETURN_PCT":float(vals.std(ddof=1)) if len(vals)>1 else None,
                                "KNOWN_BEFORE_SESSION_N":int(g["KNOWN_BEFORE_SESSION"].sum())})
    pd.DataFrame(summary).to_csv(OUT/"event_study_summary.csv",index=False)
    report={"status":"COMPUTED_EXPLORATORY" if not results.empty else "NO_MATCHING_EVENT_WINDOWS",
            "panel_rows":int(len(panel)),"event_rows":int(len(events)),"window_rows":int(len(results)),
            "series":sorted(panel["SERIES"].unique().tolist()),"warning":"Unadjusted event-window returns are descriptive, not causal. Add benchmark-adjusted returns, matched controls, overlap handling and walk-forward validation before any ranking integration."}
    (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report))
    return 0
if __name__=="__main__": raise SystemExit(main())
