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
# Fetch every registered post-2015 event window date. The former 18-date
# diagnostic sample could never establish H+1/H+5/H+20 coverage across 9 regimes.
# Requests remain bounded by compact anchor windows, short timeouts and pacing.
MAX_ARCHIVE_DATES=320
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

def fetch_historical_nifty50_secondary(start_date, end_date):
    """Fetch a real daily NIFTY 50 history series as an explicitly labelled secondary source.

    This is used only to cover historical anchors older than the NSE CSV archive
    collector's supported window. Missing observations remain missing; no values
    are interpolated and the source is never represented as an official NSE feed.
    """
    import math
    import urllib.parse
    import requests
    start = pd.Timestamp(start_date).date()
    end = pd.Timestamp(end_date).date()
    period1 = int(datetime.combine(start, datetime.min.time(), tzinfo=timezone.utc).timestamp())
    period2 = int(datetime.combine(end + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp())
    base = "https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"
    params = {"period1": period1, "period2": period2, "interval": "1d", "events": "history"}
    response = requests.get(base, params=params, headers={"User-Agent": UA, "Accept": "application/json"}, timeout=(3, 8))
    response.raise_for_status()
    payload = response.json()
    result = (payload.get("chart", {}).get("result") or [None])[0]
    if not isinstance(result, dict):
        raise RuntimeError("Yahoo chart returned no NIFTY 50 result object")
    meta = result.get("meta", {})
    if meta.get("symbol") != "^NSEI":
        raise RuntimeError(f"Unexpected historical index identity: {meta.get('symbol')!r}")
    timestamps = result.get("timestamp") or []
    quote = ((result.get("indicators") or {}).get("quote") or [{}])[0]
    closes = quote.get("close") or []
    if len(timestamps) != len(closes) or not timestamps:
        raise RuntimeError("Historical NIFTY 50 response has mismatched/empty timestamp and close arrays")
    url = response.url
    rows = []
    for ts, value in zip(timestamps, closes):
        if value is None:
            continue
        day = datetime.fromtimestamp(int(ts), tz=timezone.utc).date()
        close = float(value)
        if start <= day <= end and math.isfinite(close) and close > 0:
            rows.append({"DATE": day.isoformat(), "SERIES": "NIFTY 50", "CLOSE": close,
                "SOURCE": "Yahoo Finance historical chart (secondary NIFTY 50 index history)",
                "SOURCE_URL": url, "SOURCE_SYMBOL": "^NSEI",
                "OBSERVED_AT_UTC": datetime.now(timezone.utc).isoformat()})
    frame = pd.DataFrame(rows)
    if frame.empty:
        raise RuntimeError("No valid historical NIFTY 50 observations returned")
    if frame.duplicated(["DATE", "SERIES"]).any():
        raise RuntimeError("Historical NIFTY 50 secondary source has duplicate date/series keys")
    if not frame["SOURCE_URL"].astype(str).str.startswith("https://query1.finance.yahoo.com/").all():
        raise RuntimeError("Historical NIFTY 50 source URL provenance failed")
    return frame


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not REGIMES.exists() or not PANEL.exists(): raise SystemExit("Required regime registry or market panel missing.")
    regimes=pd.read_csv(REGIMES)
    existing=pd.read_csv(PANEL)
    existing.columns=[str(c).strip().upper() for c in existing.columns]
    if not {"DATE","SERIES","CLOSE"}.issubset(existing.columns): raise SystemExit("Market panel schema invalid.")
    sess=requests.Session(); headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://www.nseindia.com/all-reports"}
    new=[]; diagnostics=[]; all_target_dates=target_dates(regimes)
    # Deterministic complete request set for every registered post-2015 event window.
    # Older anchors are explicitly listed as unsupported by this NSE daily archive;
    # they are not silently sampled or represented as complete.
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
    # The NSE daily archive path has no confirmed coverage before 2015. Fill
    # historical NIFTY 50 anchor gaps from a separately labelled real secondary
    # history series so old regimes are tested against observations, not today's
    # panel. Do not overwrite existing NSE observations for the same date.
    secondary_status={"status":"NOT_ATTEMPTED"}
    try:
        min_anchor=pd.to_datetime(regimes["start_date"],errors="coerce").min()
        max_anchor=pd.to_datetime(regimes["end_date"],errors="coerce").max()
        if pd.notna(min_anchor) and pd.notna(max_anchor):
            secondary=fetch_historical_nifty50_secondary(min_anchor.date()-timedelta(days=10),
                                                         max_anchor.date()+timedelta(days=45))
            existing["DATE"]=pd.to_datetime(existing["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
            existing_keys=set(zip(existing["DATE"].astype(str),existing["SERIES"].astype(str).str.upper()))
            secondary=secondary[~secondary.apply(lambda r:(r["DATE"],r["SERIES"].upper()) in existing_keys,axis=1)]
            fetched=pd.concat([fetched,secondary],ignore_index=True,sort=False) if not fetched.empty else secondary
            secondary_status={"status":"COLLECTED_SECONDARY","rows":len(secondary),
                "source":"Yahoo Finance historical chart (secondary NIFTY 50 index history)",
                "source_url":"https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI",
                "note":"Only missing NIFTY 50 date keys filled; existing observations preserved; no interpolation."}
    except Exception as exc:
        secondary_status={"status":"BLOCKED","error":f"{type(exc).__name__}: {str(exc)[:220]}",
            "source_url":"https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"}
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
            # Never let a modern panel observation stand in for an old regime horizon.
            # H+1/H+5/H+20 must fall inside the anchor's bounded forward window;
            # otherwise the series remains explicitly incomplete.
            # Baseline must also be local to the event. An old panel row (for
            # example, 2015-08-27 used as the baseline for a 2024 regime) is not
            # a valid pre-event close. Keep the same bounded 40-calendar-day
            # contract on both sides of the anchor; missing local history stays
            # UNKNOWN/INCOMPLETE rather than borrowing a distant observation.
            before=g[(g["_D"]<anchor) & (g["_D"]>=anchor-pd.Timedelta(days=40))]
            after=g[(g["_D"]>=anchor) & (g["_D"]<=anchor+pd.Timedelta(days=40))]
            h={}
            h["baseline"]=None if before.empty else {"date":before.iloc[-1]["_D"].date().isoformat(),"close":float(before.iloc[-1]["CLOSE"])}
            for horizon in (1,5,20):
                if len(after)>=horizon:
                    z=after.iloc[horizon-1]
                    h["H+%s"%horizon]={"date":z["_D"].date().isoformat(),"close":float(z["CLOSE"])}
                else: h["H+%s"%horizon]=None
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
      "diagnostics":diagnostics,"historical_nifty50_secondary":secondary_status,
      "limitations":["A successful live smoke test does not guarantee every historical weekday archive exists.",
       "H+ horizons use actual returned close observations on/after anchor; missing series/windows remain incomplete.",
       "Historical anchor source verification and full Factor Registry validation remain separate hard-gate requirements."]}
    (OUT/"historical_index_backfill_report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps({k:report[k] for k in ("status","requested_dates","fetched_rows","fetched_series","incomplete_regimes","diagnostics_summary")},indent=2))
    # Do not fail collection on partial historical coverage; strict hard gate must block it.
    return 0
if __name__=="__main__": raise SystemExit(main())
