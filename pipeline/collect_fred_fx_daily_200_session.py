#!/usr/bin/env python3
"""Collect free Federal Reserve H.10 daily USD/INR and USD/JPY observations.

These are FX spot proxies only. No carry return or cross-currency basis is
computed without verified interest-rate/basis source series.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import pandas as pd
import requests

SNAPSHOT_ID="1f6d79d9bcdf3a6aa11dd9a80033276061447401dac6c708ab6622b6258b7534"
MANIFEST=Path("inputs/nse_snapshot/raw/nse_snapshot_manifest_1f6d79d9bcdf3a6a.json")
ROOT=Path("artifacts/fx_carry_cross_currency")
SERIES={
 "DEXINUS":{"name":"Indian Rupees to U.S. Dollar Spot Exchange Rate","unit":"INR per USD","url":"https://fred.stlouisfed.org/series/DEXINUS"},
 "DEXJPUS":{"name":"Japanese Yen to U.S. Dollar Spot Exchange Rate","unit":"JPY per USD","url":"https://fred.stlouisfed.org/series/DEXJPUS"}
}
BASE="https://fred.stlouisfed.org/graph/fredgraph.csv"

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    if not MANIFEST.is_file(): raise SystemExit("BLOCKED_MISSING_NSE_SNAPSHOT")
    m=json.loads(MANIFEST.read_text())
    if m.get("snapshot_id")!=SNAPSHOT_ID or m.get("actual_sessions")!=200 or len(m.get("records",[]))!=200:
        raise SystemExit("BLOCKED_NSE_SNAPSHOT_MISMATCH")
    sessions=sorted({str(x["trade_date"]) for x in m["records"]})
    if len(sessions)!=200: raise SystemExit("BLOCKED_DUPLICATE_NSE_DATES")
    start,end=sessions[0],sessions[-1]
    ROOT.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update({"User-Agent":"PRECISION-WIRES-research/1.0","Accept":"text/csv,*/*"})
    data={};reports=[]
    for sid,spec in SERIES.items():
        url=BASE
        params={"id":sid,"cosd":start,"coed":end}
        r=s.get(url,params=params,timeout=(10,45));r.raise_for_status()
        raw=r.content
        if len(raw)<20: raise SystemExit(f"BLOCKED_EMPTY_FRED_SERIES:{sid}")
        raw_path=ROOT/f"{sid}.csv";raw_path.write_bytes(raw)
        frame=pd.read_csv(raw_path,dtype=str)
        if frame.shape[1]<2: raise SystemExit(f"BLOCKED_FRED_SCHEMA:{sid}")
        date_col=frame.columns[0]
        value_col=sid if sid in frame.columns else frame.columns[1]
        frame=frame.rename(columns={date_col:"DATE",value_col:sid})
        frame["DATE"]=pd.to_datetime(frame["DATE"],errors="coerce").dt.strftime("%Y-%m-%d")
        frame[sid]=pd.to_numeric(frame[sid],errors="coerce")
        frame=frame[frame["DATE"].notna()]
        if frame["DATE"].duplicated().any(): raise SystemExit(f"BLOCKED_FRED_DUPLICATES:{sid}")
        if len(frame)==0 or frame[sid].notna().sum()==0: raise SystemExit(f"BLOCKED_FRED_NO_VALUES:{sid}")
        data[sid]=frame.set_index("DATE")[sid]
        reports.append({"series_id":sid,"title":spec["name"],"unit":spec["unit"],
          "source":"Board of Governors of the Federal Reserve System (US), H.10 Foreign Exchange Rates via FRED",
          "series_url":spec["url"],"download_url":r.url,"http_status":r.status_code,
          "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"raw_sha256":sha(raw),
          "raw_file":str(raw_path),"source_frequency":"Daily","seasonal_adjustment":"Not Seasonally Adjusted",
          "source_last_observation":frame["DATE"].max(),"observations":int(frame[sid].notna().sum())})
    panel=pd.DataFrame({"DATE":sessions})
    for sid in SERIES:
        panel[sid]=panel["DATE"].map(data[sid])
    panel["NSE_SNAPSHOT_ID"]=SNAPSHOT_ID
    panel["OBSERVED_AT_UTC"]=datetime.now(timezone.utc).isoformat()
    panel["SOURCE"]="Federal Reserve Board H.10 via FRED"
    panel["SOURCE_URL"]="https://fred.stlouisfed.org/graph/fredgraph.csv"
    out=ROOT/"fred_fx_spot_200_session.csv";panel.to_csv(out,index=False)
    coverage={sid:int(panel[sid].notna().sum()) for sid in SERIES}
    report={
      "status":"PASS_FX_SPOT_COLLECTION_WITH_EXPLICIT_CARRY_BLOCKERS",
      "snapshot_id":SNAPSHOT_ID,"nse_sessions":200,"date_min":start,"date_max":end,
      "series":reports,"panel_rows":len(panel),"series_session_coverage":coverage,
      "complete_fx_spot_rows":int(panel[list(SERIES)].notna().all(axis=1).sum()),
      "missing_value_cells":int(panel[list(SERIES)].isna().sum().sum()),
      "output_sha256":sha(out.read_bytes()),"output_file":str(out),
      "promotion_allowed":False,
      "unresolved_requirements":[
        "Official short-term interest-rate series with release timestamps required to calculate FX carry differential.",
        "Cross-currency basis observations are not supplied by these spot exchange-rate series.",
        "Do not label spot FX returns as carry or cross-currency basis."
      ],
      "observed_at_utc":datetime.now(timezone.utc).isoformat()
    }
    (ROOT/"fx_spot_qa.json").write_text(json.dumps(report,indent=2))
    print(json.dumps({k:report[k] for k in ("status","nse_sessions","series_session_coverage","complete_fx_spot_rows","missing_value_cells","promotion_allowed")},indent=2))
if __name__=="__main__": main()
