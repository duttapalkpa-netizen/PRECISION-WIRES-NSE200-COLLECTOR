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
    neede={"EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","CONFIDENCE","EVENT_DATE_BASIS"}
    if needp-set(panel.columns): return None,None,"Panel missing columns: "+",".join(sorted(needp-set(panel.columns)))
    if neede-set(events.columns): return None,None,"Events missing columns: "+",".join(sorted(neede-set(events.columns)))
    panel["DATE"]=pd.to_datetime(panel["DATE"],errors="coerce").dt.normalize()
    panel["CLOSE"]=pd.to_numeric(panel["CLOSE"],errors="coerce")
    if events.empty: return None,None,"Events file contains no rows."
    raw_published=events["PUBLISHED_AT"].astype(str).str.strip()
    has_timezone=raw_published.str.contains(r"(?:Z|[+-][0-9]{2}:?[0-9]{2})$",case=False,regex=True,na=False)
    if not bool(has_timezone.all()): return None,None,"Every PUBLISHED_AT must include an explicit UTC offset or Z timezone."
    events["EVENT_DATE"]=pd.to_datetime(events["EVENT_DATE"],errors="coerce").dt.normalize()
    events["PUBLISHED_AT"]=pd.to_datetime(events["PUBLISHED_AT"],errors="coerce",utc=True)
    events["CONFIDENCE"]=pd.to_numeric(events["CONFIDENCE"],errors="coerce")
    panel=panel.dropna(subset=["DATE","SERIES","CLOSE"]).sort_values(["SERIES","DATE"])
    if panel.empty: return None,None,"Market panel contains no valid rows."
    if events[["EVENT_DATE","EVENT_ID","EVENT_TYPE","PUBLISHED_AT","SOURCE","SOURCE_URL","EVENT_DATE_BASIS","CONFIDENCE"]].isna().any().any():
        return None,None,"Events contain missing required date, ID, type, source, URL, basis, or confidence values."
    if events["EVENT_ID"].astype(str).str.strip().eq("").any() or events["SOURCE"].astype(str).str.strip().eq("").any():
        return None,None,"Events contain blank IDs or source names."
    if not events["SOURCE_URL"].astype(str).str.match(r"^https?://",case=False).all():
        return None,None,"Every event must include an HTTP(S) source URL."
    if not events["CONFIDENCE"].between(0,1).all():
        return None,None,"CONFIDENCE must be numeric and between 0 and 1."
    proxy=events["EVENT_DATE_BASIS"].astype(str).eq("GDELT_SEENDATE_PUBLICATION_PROXY")
    published_dates=events["PUBLISHED_AT"].dt.date.astype(str)
    event_dates=events["EVENT_DATE"].dt.date.astype(str)
    if (proxy & (published_dates!=event_dates)).any():
        return None,None,"GDELT publication-proxy EVENT_DATE must match the UTC publication date."
    panel_min=panel["DATE"].min().date(); panel_max=panel["DATE"].max().date()
    if ((events["EVENT_DATE"].dt.date<panel_min)|(events["EVENT_DATE"].dt.date>panel_max)).any():
        return None,None,"One or more event dates fall outside the market-panel date range."
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
        report={"status":"BLOCKED_MISSING_OR_INVALID_INPUTS","research_status":"BLOCKED","operational_status":"FAIL_QA",
                "reason":error,"required_panel":str(PANEL),"required_events":str(EVENTS),
                "note":"No synthetic market result was substituted; this is not a successful study."}
        (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 2
    results=compute_event_windows(panel,events)
    results.to_csv(OUT/"event_study_windows.csv",index=False)
    summary=[]
    if not results.empty:
        metrics=[f"RETURN_H{h}_PCT" for h in WINDOWS]+[f"ABNORMAL_RETURN_H{h}_PCT" for h in WINDOWS if f"ABNORMAL_RETURN_H{h}_PCT" in results.columns]
        # Deterministic non-parametric bootstrap interval for the mean. This is
        # descriptive uncertainty, not causal inference; overlapping events can
        # still make the nominal interval too narrow.
        rng=np.random.default_rng(20261014)
        for (typ,series),g in results.groupby(["EVENT_TYPE","SERIES"]):
            for col in metrics:
                vals=pd.to_numeric(g[col],errors="coerce").dropna().to_numpy(dtype=float)
                if len(vals):
                    boot=np.array([rng.choice(vals,size=len(vals),replace=True).mean() for _ in range(2000)])
                    ci_low,ci_high=np.quantile(boot,[0.025,0.975])
                    mean=float(vals.mean()); median=float(np.median(vals))
                else:
                    ci_low=ci_high=mean=median=None
                summary.append({"EVENT_TYPE":typ,"SERIES":series,"METRIC":col,"N_EVENTS":int(len(vals)),
                    "MEAN_PCT":mean,"MEDIAN_PCT":median,
                    "STD_PCT":float(np.std(vals,ddof=1)) if len(vals)>1 else None,
                    "BOOTSTRAP_95CI_LOW_PCT":float(ci_low) if ci_low is not None else None,
                    "BOOTSTRAP_95CI_HIGH_PCT":float(ci_high) if ci_high is not None else None,
                    "CI_METHOD":"percentile bootstrap, 2000 resamples, seed=20261014" if len(vals) else "not estimable"})
    pd.DataFrame(summary).to_csv(OUT/"event_study_summary.csv",index=False)
    if results.empty:
        report={"status":"BLOCKED_NO_MATCHING_EVENT_WINDOWS","research_status":"BLOCKED","operational_status":"PASS",
                "panel_rows":len(panel),"panel_series":int(panel.SERIES.nunique()),"event_rows":len(events),"window_rows":0,
                "reason":"No event had both a valid pre/post publication close window; research is blocked, not successful."}
        (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
    report={"status":"COMPUTED_EXPLORATORY",
        "panel_rows":len(panel),"panel_series":int(panel.SERIES.nunique()),"event_rows":len(events),"window_rows":len(results),
        "series":sorted(panel.SERIES.unique().tolist()),
        "publication_time_rule":"Baseline is last 15:30 Asia/Kolkata close at/before PUBLISHED_AT; H+1/H+5/H+20 are the 1st/5th/20th closes strictly after publication.",
        "benchmark_adjustment":"Same-event NIFTY 50 return subtraction when available; descriptive only.",
        "uncertainty":"Summary includes deterministic 95% percentile-bootstrap intervals for mean returns; overlapping events, selection bias and multiple comparisons mean these are not causal confidence intervals.",
        "event_source_quality":"Collector filters to explicit market-relevant titles from trusted publisher domains; publication timestamps remain proxies and headlines are not independently coded as verified event occurrence.",
        "limitations":["News-selection bias and overlapping windows remain.","No matched-control design or multiple-testing correction.","Bootstrap intervals are descriptive and may understate uncertainty under dependent/overlapping events.","NSE official index closes are used for Indian indices; any Yahoo fallback series are secondary and identified in the panel source column.","P0 FPI/DII and official corporate-event sources may remain unavailable; missing data stays UNKNOWN."],
        "warning":"Exploratory historical publication-time study only; no ranking integration or causal claims."}
    (OUT/"event_study_report.json").write_text(json.dumps(report,indent=2)); print(json.dumps(report)); return 0
if __name__=="__main__": raise SystemExit(main())
