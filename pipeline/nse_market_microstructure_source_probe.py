#!/usr/bin/env python3
"""Probe official NSE daily reports, price bands and surveillance APIs (bounded, read-only)."""
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO
import hashlib, json, time
import requests
import pandas as pd

ROOT=Path("artifacts/nse_market_microstructure_probe")
HEADERS={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
 "Accept":"text/csv,application/json,application/octet-stream,*/*",
 "Accept-Language":"en-US,en;q=0.9"}
ARCHIVE="https://nsearchives.nseindia.com/content/equities/"
NSE="https://www.nseindia.com"

def norm(x): return "".join(c for c in str(x).upper() if c.isalnum())

def sha(raw): return hashlib.sha256(raw).hexdigest()

def inspect_csv(raw, category):
    frame=pd.read_csv(BytesIO(raw),dtype=str,nrows=5000).fillna("")
    cols={norm(c):str(c) for c in frame.columns}
    symbol=next((cols[k] for k in ("SYMBOL","TCKRSYMB","SECURITY","SCRIP") if k in cols),None)
    isin=next((cols[k] for k in ("ISIN","ISINNUMBER") if k in cols),None)
    stage=next((cols[k] for k in ("SURVEILLANCEINDICATOR","INDICATOR","STAGE","ASMSTAGE","GSMSTAGE","ESMSTAGE","GSM","ESM","LONGTERMADDITIONALSURVEILLANCEMEASURE","SHORTTERMADDITIONALSURVEILLANCEMEASURE","ACTION","REMARKS","MEASURE","STATUS","DEFAULT","PLEDGE") if k in cols),None)
    band=next((cols[k] for k in ("BAND","PRICEBAND","PRICEBANDPERCENT","BANDPERCENT") if k in cols),None)
    if not symbol: raise ValueError(f"symbol column missing: {list(frame.columns)}")
    if category=="price_band" and not band: raise ValueError(f"price band column missing: {list(frame.columns)}")
    if category.startswith("surveillance") or category in ("asm","gsm","esm"):
        if not stage: raise ValueError(f"surveillance stage/indicator column missing: {list(frame.columns)}")
    return {"columns":list(frame.columns),"sample_rows":len(frame),"symbol_column":symbol,
            "isin_column":isin,"stage_or_remarks_column":stage,"band_column":band,"schema_status":"PASS"}

def save_report(session, category, name, url, metadata=None):
    item={"category":category,"filename":name,"url":url,
          "retrieved_at_utc":datetime.now(timezone.utc).isoformat()}
    if metadata: item["official_report_metadata"]=metadata
    try:
        r=session.get(url,timeout=(5,20))
        item.update({"http_status":r.status_code,"content_type":r.headers.get("Content-Type",""),"bytes":len(r.content)})
        if r.status_code!=200 or len(r.content)<20 or r.content.lstrip().startswith(b"<"):
            item["result"]="HTTP_OR_CONTENT_FAIL"
        else:
            item["sha256"]=sha(r.content)
            item.update(inspect_csv(r.content,category))
            (ROOT/name).write_bytes(r.content)
            item["saved_path"]=str(ROOT/name)
            item["result"]="PASS"
    except Exception as e:
        item["result"]="REQUEST_OR_SCHEMA_ERROR"
        item["error"]=f"{type(e).__name__}: {e}"
    return item

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update(HEADERS)
    results=[]
    # Warm the public site and obtain the official daily report metadata.
    for page in ("/all-reports","/reports/asm","/reports/gsm"):
        try: s.get(NSE+page,headers={"Referer":NSE+"/"},timeout=(5,15))
        except Exception: pass
    # Exact price-band files published for the requested 02-Nov-2026 trading day.
    results.append(save_report(s,"price_band","sec_list_02112026.csv",ARCHIVE+"sec_list_02112026.csv",
                               {"report_date":"2026-11-02"}))
    results.append(save_report(s,"price_band_changes","eq_band_changes_02112026.csv",ARCHIVE+"eq_band_changes_02112026.csv",
                               {"report_date":"2026-11-02","effective_from_next_trade_date":True}))
    # Use NSE's own daily-reports index to discover surveillance file names and exact paths.
    daily={"result":"NOT_ATTEMPTED"}
    try:
        r=s.get(NSE+"/api/daily-reports?key=CM",headers={"Referer":NSE+"/all-reports"},timeout=(5,20))
        daily={"http_status":r.status_code,"content_type":r.headers.get("Content-Type",""),
               "bytes":len(r.content),"retrieved_at_utc":datetime.now(timezone.utc).isoformat()}
        if r.status_code==200:
            payload=r.json()
            daily["sha256"]=sha(r.content)
            daily["day_types"]={}
            for day_type in ("CurrentDay","PreviousDay"):
                files=payload.get(day_type,[]) or []
                daily["day_types"][day_type]=[]
                for f in files:
                    name=str(f.get("fileActlName") or "")
                    key=str(f.get("fileKey") or "")
                    if name.upper().startswith(("REG_IND","REG1_IND")):
                        category="surveillance_old" if name.upper().startswith("REG_IND") else "surveillance_new"
                        url=str(f.get("filePath") or "")+name
                        meta={k:f.get(k) for k in ("fileKey","displayName","tradingDate","fileSize","filePath","fileActlName")}
                        item=save_report(s,category,name,url,meta)
                        results.append(item);daily["day_types"][day_type].append(meta)
            daily["result"]="PASS"
        else:
            daily["result"]="HTTP_FAIL"
    except Exception as e:
        daily.update({"result":"REQUEST_ERROR","error":f"{type(e).__name__}: {e}"})
    (ROOT/"daily_reports_api_metadata.json").write_text(json.dumps(daily,indent=2),encoding="utf-8")
    # Public current surveillance list APIs. These are current lists, not historical effective-date archives.
    for category, page, endpoint in (
        ("asm","/reports/asm","/api/reportASM?csv=true"),
        ("gsm","/reports/gsm","/api/reportGSM?csv=true"),
        ("esm","/static/regulations/enhanced-surveillance-measure-esm","/api/reportESM?csv=true")
    ):
        try:
            r=s.get(NSE+endpoint,headers={"Referer":NSE+page,"Accept":"text/csv,*/*"},timeout=(5,20))
            item={"category":category,"url":NSE+endpoint,"http_status":r.status_code,
                  "content_type":r.headers.get("Content-Type",""),"bytes":len(r.content),
                  "retrieved_at_utc":datetime.now(timezone.utc).isoformat()}
            if r.status_code==200 and len(r.content)>20 and not r.content.lstrip().startswith(b"<"):
                item["sha256"]=sha(r.content)
                item.update(inspect_csv(r.content,category))
                name=f"{category}_current_surveillance.csv"
                (ROOT/name).write_bytes(r.content);item.update({"filename":name,"saved_path":str(ROOT/name),"result":"PASS"})
            else:item["result"]="HTTP_OR_CONTENT_FAIL"
            results.append(item)
        except Exception as e:
            results.append({"category":category,"url":NSE+endpoint,"result":"REQUEST_ERROR","error":f"{type(e).__name__}: {e}"})
        time.sleep(0.2)
    passed=sorted({x["category"] for x in results if x.get("result")=="PASS"})
    required=["price_band","surveillance_old","surveillance_new","asm","gsm"]
    missing=[x for x in required if x not in passed]
    report={"status":"PASS" if not missing else ("PARTIAL" if passed else "BLOCKED"),
      "requested_trade_date":"2026-11-02","price_band_report_date":"2026-11-02",
      "daily_surveillance_report_effective_date_rule":"NSE circular states REG_INDDDMMYY.csv is applicable for the next trading day; use official tradingDate metadata and calendar before joining.",
      "required_categories":required,"passed_categories":passed,"missing_categories":missing,
      "daily_reports_api":daily,"results":results,"observed_at_utc":datetime.now(timezone.utc).isoformat(),
      "policy":"Probe only. No source-group promotion until 200-session date coverage, symbol/date join, surveillance effective-date QA, free-float coverage and source provenance pass."}
    (ROOT/"probe_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({"status":report["status"],"passed_categories":passed,"missing_categories":missing,
                      "daily_reports_api_status":daily.get("result"),"results":results},indent=2))
    if report["status"]=="BLOCKED": raise SystemExit("No official NSE market microstructure data source validated")
if __name__=="__main__": main()
