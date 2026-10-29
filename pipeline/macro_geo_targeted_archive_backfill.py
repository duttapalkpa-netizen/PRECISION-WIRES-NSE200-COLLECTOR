#!/usr/bin/env python3
"""Targeted NSE archive backfill for regime anchors and H+1/H+5/H+20 windows.

Fetches only weekdays in compact windows around registered anchors (not a
continuous 2008-present daily archive sweep). Missing source history remains
explicit and blocks research; no synthetic values are created.
"""
from datetime import date, timedelta, datetime, timezone
from io import StringIO
from pathlib import Path
import json, time
import pandas as pd
import requests

ROOT=Path(".")
REGIMES=ROOT/"config/macro_geo_historical_regimes.csv"
PANEL=ROOT/"data/external/market_panel.csv"
OUT=ROOT/"outputs/macro_geo"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
ALIASES={"nifty50":"NIFTY 50","niftyit":"NIFTY IT","niftybank":"NIFTY BANK","niftyauto":"NIFTY AUTO",
 "niftymetal":"NIFTY METAL","niftypharma":"NIFTY PHARMA","niftyenergy":"NIFTY ENERGY","niftyfmcg":"NIFTY FMCG",
 "niftyrealty":"NIFTY REALTY","niftyinfrastructure":"NIFTY INFRA","indiavix":"INDIA VIX"}
REQUIRED=set(ALIASES.values())
# Keep this network collector bounded; incomplete history is recorded and blocks release.
MAX_ARCHIVE_DATES=18
CONNECT_TIMEOUT_SECONDS=2
READ_TIMEOUT_SECONDS=3

def target_dates(regimes):
    dates=set()
    for _,r in regimes.iterrows():
        anchor=pd.to_datetime(r["start_date"],errors="coerce")
        if pd.isna(anchor): continue
        # The NSE daily archive is only used where the bounded live test established availability.
        # For 2008/2013 anchors the archive currently has no confirmed rows: keep them explicitly missing.
        if anchor.date()<date(2015,1,1): continue
        start=(anchor-timedelta(days=7)).date()
        end=(anchor+timedelta(days=38)).date() # enough calendar room for 20 sessions plus holidays
        d=start
        while d<=end:
            if d.weekday()<5: dates.add(d)
            d+=timedelta(days=1)
    return sorted(dates)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not REGIMES.exists() or not PANEL.exists(): raise SystemExit("Required regime registry or market panel missing.")
    regimes=pd.read_csv(REGIMES)
    existing=pd.read_csv(PANEL)
    existing.columns=[str(c).strip().upper() for c in existing.columns]
    if not {"DATE","SERIES","CLOSE"}.issubset(existing.columns): raise SystemExit("Market panel schema invalid.")
    sess=requests.Session(); headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://www.nseindia.com/all-reports"}
    new=[]; diagnostics=[]; all_target_dates=target_dates(regimes)
    # Bounded deterministic sample: prioritize dates closest to registered anchors,
    # then spread remaining budget across the requested windows. Never imply full coverage.
    if len(all_target_dates)>MAX_ARCHIVE_DATES:
        anchor_dates=sorted({pd.to_datetime(v,errors="coerce").date() for v in regimes["start_date"] if pd.notna(pd.to_datetime(v,errors="coerce"))})
        prioritized=[]
        for anchor in anchor_dates:
            candidates=sorted(all_target_dates,key=lambda d:abs((d-anchor).days))
            for day in candidates:
                if day not in prioritized: prioritized.append(day)
                if len(prioritized)>=MAX_ARCHIVE_DATES: break
            if len(prioritized)>=MAX_ARCHIVE_DATES: break
        attempted=sorted(prioritized[:MAX_ARCHIVE_DATES])
    else:
        attempted=all_target_dates
    for n,day in enumerate(attempted,1):
        stamp=day.strftime("%d%m%Y")
        urls=[f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{stamp}.csv",
              f"https://archives.nseindia.com/content/indices/ind_close_all_{stamp}.csv"]
        accepted=False
        for url in urls:
            try:
                resp=sess.get(url,headers=headers,timeout=(CONNECT_TIMEOUT_SECONDS,READ_TIMEOUT_SECONDS))
                if resp.status_code==404:
                    diagnostics.append({"date":day.isoformat(),"url":url,"http_status":404,"result":"NOT_FOUND"}); continue
                resp.raise_for_status()
                df=pd.read_csv(StringIO(resp.content.decode("utf-8-sig",errors="replace")))
                df.columns=[str(c).strip().upper() for c in df.columns]
                nc=next((c for c in ("INDEX NAME","INDEX_NAME") if c in df.columns),None)
                dc=next((c for c in ("INDEX DATE","INDEX_DATE","DATE") if c in df.columns),None)
                cc=next((c for c in ("CLOSING INDEX VALUE","CLOSING","CLOSE","CLOSE VALUE") if c in df.columns),None)
                if not (nc and dc and cc):
                    diagnostics.append({"date":day.isoformat(),"url":url,"http_status":resp.status_code,"result":"SCHEMA_FAIL","columns":list(df.columns),"preview":resp.text[:160]}); continue
                df["_KEY"]=df[nc].astype(str).str.lower().str.replace(r"[^a-z0-9]","",regex=True)
                selected=df[df["_KEY"].isin(ALIASES)]
                for _,r in selected.iterrows():
                    dt=pd.to_datetime(r[dc],errors="coerce",dayfirst=True); close=pd.to_numeric(pd.Series([r[cc]]),errors="coerce").iloc[0]
                    if pd.isna(dt) or dt.date()!=day or pd.isna(close) or close<=0: continue
                    label=ALIASES[r["_KEY"]]
                    new.append({"DATE":day.isoformat(),"SERIES":label,"CLOSE":float(close),"SOURCE":"NSE daily index close archive",
                      "SOURCE_URL":url,"SOURCE_SYMBOL":str(r[nc]),"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
                diagnostics.append({"date":day.isoformat(),"url":url,"http_status":resp.status_code,
                    "content_type":resp.headers.get("Content-Type",""),"schema":"PASS","matching_index_rows":len(selected),
                    "validated_rows":sum(1 for x in new if x["DATE"]==day.isoformat()),"result":"PASS" if selected.empty is False else "NO_REGISTERED_INDEX_NAMES"})
                accepted=True; break
            except Exception as exc:
                diagnostics.append({"date":day.isoformat(),"url":url,"result":"ERROR","error":f"{type(exc).__name__}: {exc}"})
        if n%25==0: print(json.dumps({"attempted":n,"total_dates":len(attempted),"valid_rows":len(new)}),flush=True)
        time.sleep(0.06)
    fetched=pd.DataFrame(new)
    if not fetched.empty:
        fetched=fetched.drop_duplicates(["DATE","SERIES"],keep="last")
        existing["DATE"]=pd.to_datetime(existing["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
        keys=set(zip(fetched["DATE"],fetched["SERIES"]))
        existing=existing[~existing.apply(lambda r:(r["DATE"],r["SERIES"]) in keys,axis=1)]
        merged=pd.concat([existing,fetched],ignore_index=True,sort=False).drop_duplicates(["DATE","SERIES"],keep="last").sort_values(["DATE","SERIES"])
        merged.to_csv(PANEL,index=False)
    else: merged=existing
    windows=[]
    for _,r in regimes.iterrows():
        anchor=pd.to_datetime(r["start_date"],errors="coerce")
        item={"regime_id":str(r["regime_id"]),"regime_label":str(r["regime_label"]),
              "anchor_date":None if pd.isna(anchor) else anchor.date().isoformat(),"horizons":{}}
        for series in sorted(REQUIRED):
            g=merged[merged["SERIES"].astype(str).str.upper().eq(series)].copy()
            g["_D"]=pd.to_datetime(g["DATE"],errors="coerce")
            g=g[g["_D"].notna()].sort_values("_D")
            if pd.isna(anchor):
                item["horizons"][series]={"status":"UNKNOWN_INVALID_ANCHOR"}; continue
            before=g[g["_D"]<anchor]
            after=g[g["_D"]>=anchor]
            h={}
            h["baseline"]=None if before.empty else {"date":before.iloc[-1]["_D"].date().isoformat(),"close":float(before.iloc[-1]["CLOSE"])}
            for horizon in (1,5,20):
                if len(after)>=horizon:
                    z=after.iloc[horizon-1]
                    h[f"H+{horizon}"]={"date":z["_D"].date().isoformat(),"close":float(z["CLOSE"])}
                else: h[f"H+{horizon}"]=None
            h["status"]="COMPLETE" if h["baseline"] and all(h[f"H+{x}"] for x in (1,5,20)) else "INCOMPLETE"
            item["horizons"][series]=h
        item["complete_series_count"]=sum(v.get("status")=="COMPLETE" for v in item["horizons"].values())
        item["status"]="COMPLETE" if item["complete_series_count"]==len(REQUIRED) else "INCOMPLETE"
        windows.append(item)
    missing_anchors=[x["regime_id"] for x in windows if x["status"]!="COMPLETE"]
    report={"status":"TARGETED_BACKFILL_COMPLETE" if not missing_anchors else "TARGETED_BACKFILL_WITH_GAPS",
      "method":"NSE official daily archive CSV; compact weekday windows around registered regime anchors; no interpolation",
      "requested_dates":len(attempted),"all_candidate_dates":len(all_target_dates),"request_budget_limited":len(attempted)<len(all_target_dates),"max_archive_dates":MAX_ARCHIVE_DATES,"fetched_rows":int(len(fetched)) if not fetched.empty else 0,
      "fetched_series":int(fetched["SERIES"].nunique()) if not fetched.empty else 0,
      "panel_date_min":str(pd.to_datetime(merged["DATE"],errors="coerce").min().date()),
      "panel_date_max":str(pd.to_datetime(merged["DATE"],errors="coerce").max().date()),
      "regimes":windows,"incomplete_regimes":missing_anchors,
      "old_archive_anchors_skipped":[str(x) for x in regimes.loc[pd.to_datetime(regimes["start_date"],errors="coerce").dt.date < date(2015,1,1),"regime_id"].tolist()],
      "diagnostics_summary":{"requests":len(diagnostics),"http_404":sum(x.get("http_status")==404 for x in diagnostics),
       "schema_fail":sum(x.get("result")=="SCHEMA_FAIL" for x in diagnostics),"valid_rows":len(new)},
      "diagnostics":diagnostics,
      "limitations":["A successful live smoke test does not guarantee every historical weekday archive exists.",
       "H+ horizons use actual returned close observations on/after anchor; missing series/windows remain incomplete.",
       "Historical anchor source verification and full Factor Registry validation remain separate hard-gate requirements."]}
    (OUT/"historical_index_backfill_report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps({k:report[k] for k in ("status","requested_dates","fetched_rows","fetched_series","incomplete_regimes","diagnostics_summary")},indent=2))
    # Do not fail collection on partial historical coverage; strict hard gate must block it.
    return 0
if __name__=="__main__": raise SystemExit(main())
