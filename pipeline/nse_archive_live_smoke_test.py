#!/usr/bin/env python3
"""Bounded live smoke test for official NSE daily index archive CSVs."""
from datetime import date
from io import StringIO
import json, time
import requests
import pandas as pd

UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36"
ALIASES={
 "nifty50":"NIFTY 50","niftyit":"NIFTY IT","niftybank":"NIFTY BANK",
 "niftyauto":"NIFTY AUTO","niftymetal":"NIFTY METAL","niftypharma":"NIFTY PHARMA",
 "niftyenergy":"NIFTY ENERGY","niftyfmcg":"NIFTY FMCG","niftyrealty":"NIFTY REALTY",
 "niftyinfrastructure":"NIFTY INFRA","indiavix":"INDIA VIX"
}
def main():
    # Two widely separated known sessions; bounded to two dates and two hosts.
    test_dates=[date(2008,9,15),date(2013,5,22),date(2015,8,11),date(2016,11,8),date(2018,9,4),date(2020,2,24),date(2022,2,24),date(2023,3,10),date(2024,6,4),date(2025,1,2),date(2026,10,23)]
    rows=[]; diagnostics=[]
    session=requests.Session()
    headers={"User-Agent":UA,"Accept":"text/csv,*/*","Referer":"https://www.nseindia.com/all-reports"}
    for day in test_dates:
        stamp=day.strftime("%d%m%Y")
        urls=[f"https://nsearchives.nseindia.com/content/indices/ind_close_all_{stamp}.csv",
              f"https://archives.nseindia.com/content/indices/ind_close_all_{stamp}.csv"]
        found=False
        for url in urls:
            try:
                resp=session.get(url,headers=headers,timeout=(5,15))
                diag={"date_requested":day.isoformat(),"url":url,"http_status":resp.status_code,
                      "content_type":resp.headers.get("Content-Type",""),"bytes":len(resp.content)}
                if resp.status_code==404:
                    diagnostics.append({**diag,"result":"NOT_FOUND"}); continue
                resp.raise_for_status()
                df=pd.read_csv(StringIO(resp.content.decode("utf-8-sig",errors="replace")))
                df.columns=[str(c).strip().upper() for c in df.columns]
                namecol=next((c for c in ("INDEX NAME","INDEX_NAME") if c in df.columns),None)
                datecol=next((c for c in ("INDEX DATE","INDEX_DATE","DATE") if c in df.columns),None)
                closecol=next((c for c in ("CLOSING INDEX VALUE","CLOSING","CLOSE","CLOSE VALUE") if c in df.columns),None)
                diag["columns"]=list(df.columns)
                if not (namecol and datecol and closecol):
                    diagnostics.append({**diag,"result":"SCHEMA_FAIL","preview":resp.text[:200]})
                    continue
                df["_KEY"]=df[namecol].astype(str).str.lower().str.replace(r"[^a-z0-9]","",regex=True)
                selected=df[df["_KEY"].isin(ALIASES)]
                for _,r in selected.iterrows():
                    parsed=pd.to_datetime(r[datecol],errors="coerce",dayfirst=True)
                    close=pd.to_numeric(pd.Series([r[closecol]]),errors="coerce").iloc[0]
                    if pd.isna(parsed) or pd.isna(close) or close<=0: continue
                    if parsed.date()!=day:
                        diagnostics.append({**diag,"result":"DATE_MISMATCH","row_date":str(parsed.date())})
                        continue
                    rows.append({"requested_date":day.isoformat(),"observed_date":parsed.date().isoformat(),
                      "index_name_raw":str(r[namecol]),"series":ALIASES[r["_KEY"]],"close":float(close),
                      "source_url":url,"http_status":resp.status_code,"content_type":resp.headers.get("Content-Type","")})
                diag["matching_index_rows"]=len(selected)
                diag["result"]="PASS" if len(selected)>0 else "NO_REGISTERED_INDEX_NAMES"
                diagnostics.append(diag); found=True; break
            except Exception as exc:
                diagnostics.append({"date_requested":day.isoformat(),"url":url,"result":"ERROR",
                                    "error":f"{type(exc).__name__}: {exc}"})
        time.sleep(0.2)
    valid=bool(rows) and all(r["close"]>0 and r["observed_date"]==r["requested_date"] for r in rows)
    # Require both dates and the core benchmark for smoke-test PASS.
    dates={r["observed_date"] for r in rows}
    core=all(any(r["observed_date"]==d.isoformat() and r["series"]=="NIFTY 50" for r in rows) for d in test_dates)
    report={"status":"PASS" if valid and core else "FAIL","test_dates":[d.isoformat() for d in test_dates],
      "validated_rows":len(rows),"validated_series":sorted({r["series"] for r in rows}),
      "date_coverage":sorted(dates),"core_benchmark_both_dates":core,
      "schema_contract":{"index_name_column":"present","date_column":"present","close_column":"present",
                         "positive_close":True,"requested_date_matches_observed_date":True},
      "rows":rows,"diagnostics":diagnostics,
      "note":"Live smoke test only; checks selected regime anchors and recent date, not every trading session or complete history."}
    from pathlib import Path
    Path("outputs/macro_geo").mkdir(parents=True,exist_ok=True)
    Path("outputs/macro_geo/nse_archive_live_smoke_test.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["status"]=="PASS" else 1)
if __name__=="__main__": main()
