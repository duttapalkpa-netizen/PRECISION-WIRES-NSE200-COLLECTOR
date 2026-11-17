#!/usr/bin/env python3
"""Targeted official NSE archive backfill around pre-registered regime anchors only."""
from datetime import date, timedelta, datetime, timezone
from io import StringIO
from pathlib import Path
import json, time
import pandas as pd
import requests

ROOT=Path("."); REGIMES=ROOT/"config/macro_geo_historical_regimes.csv"
PANEL=ROOT/"data/external/market_panel.csv"; OUT=ROOT/"outputs/macro_geo"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
ALIASES={"nifty50":"NIFTY 50","niftyit":"NIFTY IT","niftybank":"NIFTY BANK","niftyauto":"NIFTY AUTO",
 "niftymetal":"NIFTY METAL","niftypharma":"NIFTY PHARMA","niftyenergy":"NIFTY ENERGY","niftyfmcg":"NIFTY FMCG",
 "niftyrealty":"NIFTY REALTY","niftyinfrastructure":"NIFTY INFRA","indiavix":"INDIA VIX"}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 if not REGIMES.exists(): raise SystemExit("Regime registry missing")
 regimes=pd.read_csv(REGIMES)
 # R11 is a broad multi-year span, not a single event anchor; do not flood archive with it.
 regimes=regimes[regimes["regime_id"].astype(str)!="R11"].copy()
 anchors=pd.to_datetime(regimes["start_date"],errors="coerce").dropna().dt.date.tolist()
 if not anchors: raise SystemExit("No valid targeted anchors")
 # H+20 is at most about 28 calendar days; include previous baseline and safety margin.
 requested=set()
 for anchor in anchors:
  d=anchor-timedelta(days=14); end=anchor+timedelta(days=40)
  while d<=end:
   if d.weekday()<5: requested.add(d)
   d+=timedelta(days=1)
 sess=requests.Session(); headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://www.nseindia.com/all-reports"}
 rows=[]; failures=[]; successful_dates=[]
 for day in sorted(requested):
  stamp=day.strftime("%d%m%Y"); urls=[
   f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{stamp}.csv",
   f"https://archives.nseindia.com/content/indices/ind_close_all_{stamp}.csv"]
  ok=False
  for url in urls:
   try:
    r=sess.get(url,headers=headers,timeout=(4,10))
    if r.status_code==404: continue
    r.raise_for_status()
    df=pd.read_csv(StringIO(r.content.decode("utf-8-sig",errors="replace")))
    df.columns=[str(c).strip().upper() for c in df.columns]
    nc=next((c for c in ("INDEX NAME","INDEX_NAME") if c in df.columns),None)
    dc=next((c for c in ("INDEX DATE","INDEX_DATE","DATE") if c in df.columns),None)
    cc=next((c for c in ("CLOSING INDEX VALUE","CLOSING","CLOSE","CLOSE VALUE") if c in df.columns),None)
    if not (nc and dc and cc):
     failures.append({"date":day.isoformat(),"url":url,"error":"schema mismatch","columns":list(df.columns)})
     continue
    df["_KEY"]=df[nc].astype(str).str.lower().str.replace(r"[^a-z0-9]","",regex=True)
    found=0
    for _,x in df[df["_KEY"].isin(ALIASES)].iterrows():
     dt=pd.to_datetime(x[dc],errors="coerce",dayfirst=True); close=pd.to_numeric(pd.Series([x[cc]]),errors="coerce").iloc[0]
     if pd.isna(dt) or pd.isna(close) or close<=0 or dt.date()!=day: continue
     rows.append({"DATE":day.isoformat(),"SERIES":ALIASES[x["_KEY"]],"CLOSE":float(close),
      "SOURCE":"NSE daily index close archive","SOURCE_URL":url,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
     found+=1
    if found: successful_dates.append(day.isoformat()); ok=True; break
    failures.append({"date":day.isoformat(),"url":url,"error":"schema valid but no registered index rows"})
   except Exception as e: failures.append({"date":day.isoformat(),"url":url,"error":f"{type(e).__name__}: {e}"})
  if not ok and day in anchors: failures.append({"date":day.isoformat(),"error":"anchor date unavailable from both archive hosts"})
  time.sleep(.06)
 fetched=pd.DataFrame(rows).drop_duplicates(["DATE","SERIES"],keep="last") if rows else pd.DataFrame()
 existing=pd.read_csv(PANEL) if PANEL.exists() else pd.DataFrame(columns=["DATE","SERIES","CLOSE"])
 existing.columns=[str(c).strip().upper() for c in existing.columns]
 if not fetched.empty:
  existing["DATE"]=pd.to_datetime(existing["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
  fetched["DATE"]=pd.to_datetime(fetched["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
  keys=set(zip(fetched["DATE"],fetched["SERIES"]))
  old=existing[~existing.apply(lambda r:(r.get("DATE"),r.get("SERIES")) in keys,axis=1)]
  merged=pd.concat([old,fetched],ignore_index=True,sort=False).drop_duplicates(["DATE","SERIES"],keep="last").sort_values(["DATE","SERIES"])
  merged.to_csv(PANEL,index=False)
 else: merged=existing
 coverage=[]
 for _,reg in regimes.iterrows():
  anchor=pd.Timestamp(reg["start_date"]).date()
  for series in ["NIFTY 50","NIFTY IT","NIFTY BANK","NIFTY AUTO","NIFTY METAL","NIFTY PHARMA","NIFTY ENERGY","NIFTY FMCG","NIFTY REALTY","NIFTY INFRA","INDIA VIX"]:
   g=merged[merged["SERIES"].astype(str).eq(series)].copy()
   g["_D"]=pd.to_datetime(g["DATE"],errors="coerce")
   g=g.dropna(subset=["_D","CLOSE"]).sort_values("_D")
   after=g[g["_D"].dt.date>=anchor]
   before=g[g["_D"].dt.date<anchor]
   coverage.append({"regime_id":reg["regime_id"],"anchor":anchor.isoformat(),"series":series,
    "pre_anchor_baseline":bool(len(before)>0),"anchor_or_after_rows":int(len(after)),
    "H1_available":len(after)>=1,"H5_available":len(after)>=5,"H20_available":len(after)>=20,
    "source_rows_in_target_window":int(g[g["_D"].dt.date.between(anchor-timedelta(days=14),anchor+timedelta(days=40))].shape[0])})
 cov=pd.DataFrame(coverage)
 report={"status":"TARGETED_BACKFILL_COLLECTED" if not fetched.empty else "TARGETED_BACKFILL_FAILED",
  "source":"NSE daily index close archive","requested_weekdays":len(requested),"successful_archive_dates":len(set(successful_dates)),
  "fetched_rows":int(len(fetched)),"fetched_series":int(fetched["SERIES"].nunique()) if not fetched.empty else 0,
  "targeted_regimes":regimes["regime_id"].tolist(),"broad_R11_skipped":"R11 is a multi-year interval; needs verified sub-event anchors before targeted requests.",
  "coverage_summary":{"regimes":int(regimes.shape[0]),"series":11,"H1_complete":int(cov.H1_available.sum()),"H5_complete":int(cov.H5_available.sum()),"H20_complete":int(cov.H20_available.sum()),"coverage_rows":int(len(cov))},
  "coverage":coverage,"failures":failures[:200],"failure_count":len(failures),
  "limitations":["Official archive availability varies by date; no synthetic/interpolated values.","Coverage rows are per regime and series; event windows remain blocked if any required series/window is incomplete.","Regime anchors still need independent primary-source validation."]}
 (OUT/"targeted_historical_backfill_report.json").write_text(json.dumps(report,indent=2))
 cov.to_csv(OUT/"targeted_historical_backfill_coverage.csv",index=False)
 print(json.dumps({k:report[k] for k in ["status","requested_weekdays","successful_archive_dates","fetched_rows","fetched_series","coverage_summary","failure_count"]},indent=2))
 raise SystemExit(0 if not fetched.empty else 1)
if __name__=="__main__": main()
