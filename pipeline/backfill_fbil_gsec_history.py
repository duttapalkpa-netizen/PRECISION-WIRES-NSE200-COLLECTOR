#!/usr/bin/env python3
"""Historical FBIL G-Sec archive backfill via official first-party endpoints."""
import hashlib, json, re, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
import requests

BASE="https://www.fbil.org.in/wasdm"
START=date(2025,11,1)
END=date(2026,11,1)  # exclusive
OUT=Path("artifacts/fbil_10y_provenance")

def month_ranges(start, end):
    y,m=start.year,start.month
    while date(y,m,1)<end:
        a=date(y,m,1)
        y2,m2=(y+1,1) if m==12 else (y,m+1)
        b=min(date(y2,m2,1),end)
        yield a,b
        y,m=y2,m2

def get_session():
    s=requests.Session()
    s.headers.update({"User-Agent":"Mozilla/5.0 (compatible; PRECISION-WIRES provenance audit)",
                      "Accept":"application/json, text/plain, */*","Referer":"https://www.fbil.org.in/"})
    return s

def fetch_month(pair):
    a,b=pair
    s=get_session()
    r=s.get(BASE+"/gsec/fetchfiltered",params={"fromDate":a.isoformat(),"toDate":b.isoformat(),"authenticated":"false"},timeout=(10,45))
    r.raise_for_status()
    data=r.json()
    if not isinstance(data,list): raise RuntimeError(f"Unexpected index JSON for {a}: {type(data).__name__}")
    return {"from":a.isoformat(),"to":b.isoformat(),"http_status":r.status_code,
            "response_sha256":hashlib.sha256(r.content).hexdigest(),"records":data}

def download_one(day):
    # Retry transient publisher/server failures without bypassing access controls.
    # Keep every attempt visible in the audit report; never accept non-XLSX bodies.
    attempts=[]
    for attempt in range(1,5):
        try:
            s=get_session()
            r=s.get(BASE+"/gsec/downloadPublished",params={"date":day},timeout=(10,60))
            body=r.content
            cd=r.headers.get("Content-Disposition","")
            if r.status_code==200 and body.startswith(bytes([80,75,3,4])):
                path=OUT/f"fbil_gsec_published_{day.replace('-','')}.bin"
                path.write_bytes(body)
                return {"date":day,"status":r.status_code,"attempts":attempt,"attempt_log":attempts,
                        "content_type":r.headers.get("Content-Type"),"content_disposition":cd,
                        "bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":path.name}
            attempts.append({"attempt":attempt,"status":r.status_code,
                             "error":"non-200" if r.status_code!=200 else "response is not XLSX/ZIP",
                             "bytes":len(body),"preview":body[:120].decode("utf-8","replace")})
        except Exception as exc:
            attempts.append({"attempt":attempt,"error":str(exc)})
        if attempt<4:
            time.sleep(min(2**attempt,8))
    last=attempts[-1] if attempts else {}
    return {"date":day,"status":last.get("status"),"attempts":len(attempts),
            "attempt_log":attempts,"error":"download failed after bounded retries"}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    observed=datetime.now(timezone.utc).isoformat()
    month_results=[]
    for pair in month_ranges(START,END):
        try: month_results.append(fetch_month(pair))
        except Exception as e: month_results.append({"from":pair[0].isoformat(),"to":pair[1].isoformat(),"error":str(e),"records":[]})
        time.sleep(0.15)
    all_records=[x for m in month_results for x in m.get("records",[]) if isinstance(x,dict)]
    dates=sorted({str(x.get("processRunDate","")) for x in all_records
                  if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",str(x.get("processRunDate","")))})
    results=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(download_one,d):d for d in dates}
        for f in as_completed(futures):
            try: results.append(f.result())
            except Exception as e: results.append({"date":futures[f],"error":str(e)})
    results.sort(key=lambda x:x.get("date",""))
    # Also capture the live first-party GSEC endpoint separately. Only exact
    # publisher fields are eligible for timestamp provenance; archive XLSX
    # date fields are never converted into an invented time.
    live={}
    try:
        s=get_session()
        r=s.get(BASE+"/gsec/fetch",params={"authenticated":"false"},timeout=(10,45))
        r.raise_for_status()
        raw=r.content
        (OUT/"fbil_gsec_live_fetch.json").write_bytes(raw)
        payload=r.json()
        live={"url":r.url,"http_status":r.status_code,"content_type":r.headers.get("Content-Type"),
              "sha256":hashlib.sha256(raw).hexdigest(),"records":len(payload) if isinstance(payload,list) else None,
              "sample":payload[:5] if isinstance(payload,list) else str(payload)[:500]}
    except Exception as e: live={"error":str(e)}
    successful=[x for x in results if x.get("file")]
    report={"status":"FBIL_HISTORICAL_ARCHIVE_BACKFILL_COMPLETE" if len(successful)>=200 else "FBIL_HISTORICAL_ARCHIVE_BACKFILL_INCOMPLETE",
            "source":"Official FBIL /wasdm/gsec/fetchfiltered and /gsec/downloadPublished",
            "range_start":START.isoformat(),"range_end_exclusive":END.isoformat(),
            "month_index_queries":len(month_results),"month_index_errors":[x for x in month_results if x.get("error")],
            "archive_index_records":len(all_records),"unique_archive_dates":len(dates),
            "downloaded_xlsx_files":len(successful),"download_errors":[x for x in results if not x.get("file")],
            "downloaded_date_min":min((x["date"] for x in successful),default=None),
            "downloaded_date_max":max((x["date"] for x in successful),default=None),
            "live_gsec_fetch":live,"observed_at_utc":observed,
            "timestamp_policy":"Archive workbooks expose observation date but not a publisher clock time. No time is inferred. Live endpoint fields are retained for exact-schema review only.",
            "commercial_permission":"NOT_OBTAINED; written permission required before production use",
            "minimum_200_sessions_met":len(successful)>=200}
    (OUT/"fbil_historical_backfill_report.json").write_text(json.dumps(report,indent=2)+chr(10),encoding="utf-8")
    print(json.dumps(report,indent=2))
    if len(successful)<200:
        raise RuntimeError(f"Historical archive backfill has only {len(successful)} files; minimum 200 not met")
if __name__=="__main__": main()
