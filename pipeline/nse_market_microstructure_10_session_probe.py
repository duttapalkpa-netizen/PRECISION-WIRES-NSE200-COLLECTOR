#!/usr/bin/env python3
"""Ten-session smoke test for historical NSE price-band and surveillance joins."""
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib, json, time
import requests
import pandas as pd

ROOT=Path("artifacts/nse_market_microstructure_10_session")
SNAPSHOT_ROOT=Path("inputs/nse_snapshot")
BASE="https://nsearchives.nseindia.com/content/"
HEADERS={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
         "Accept":"text/csv,application/octet-stream,*/*","Referer":"https://www.nseindia.com/all-reports"}
def norm(c): return "".join(x for x in str(c).upper() if x.isalnum())
def sha(raw): return hashlib.sha256(raw).hexdigest()
def date_parts(iso):
    d=pd.Timestamp(iso)
    return d.strftime("%d%m%Y"),d.strftime("%d%m%y")

def clean_frame(raw,kind):
    df=pd.read_csv(BytesIO(raw),dtype=str).fillna("")
    df.columns=[str(c).strip() for c in df.columns]
    cmap={norm(c):c for c in df.columns}
    symbol=next((cmap[k] for k in ("SYMBOL","TCKRSYMB") if k in cmap),None)
    series=next((cmap[k] for k in ("SERIES","SCTYSRS") if k in cmap),None)
    if not symbol or not series: raise ValueError(f"{kind}: symbol/series missing; columns={df.columns.tolist()}")
    df=df.rename(columns={symbol:"SYMBOL",series:"SERIES"})
    df["SYMBOL"]=df["SYMBOL"].astype(str).str.strip().str.upper()
    df["SERIES"]=df["SERIES"].astype(str).str.strip().str.upper()
    if df.duplicated(["SYMBOL","SERIES"]).any(): raise ValueError(f"{kind}: duplicate symbol/series rows")
    if kind=="price_band":
        b=next((cmap[k] for k in ("BAND","PRICEBAND","PRICEBANDPERCENT") if k in cmap),None)
        r=next((cmap[k] for k in ("REMARKS","REMARK") if k in cmap),None)
        if not b: raise ValueError("price_band: Band column missing")
        df=df.rename(columns={b:"PRICE_BAND_PERCENT"})
        if r: df=df.rename(columns={r:"PRICE_BAND_REMARKS"})
    return df

def download(session,url):
    last=None
    for attempt in range(3):
        try:
            r=session.get(url,timeout=(5,20))
            r.raise_for_status()
            if len(r.content)<20 or r.content.lstrip().startswith(b"<"): raise ValueError("non-CSV response")
            return r.content,datetime.now(timezone.utc).isoformat()
        except Exception as e:
            last=e;time.sleep(0.5*(attempt+1))
    raise RuntimeError(f"{url}: {type(last).__name__}: {last}")

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    if not SNAPSHOT.is_file(): raise SystemExit("BLOCKED_MISSING_NSE_SNAPSHOT_ARTIFACT")
    with zipfile.ZipFile(SNAPSHOT) as z:
        mname=next(n for n in z.namelist() if n.endswith(".json") and "nse_snapshot_manifest" in n)
        manifest=json.loads(z.read(mname))
        records=manifest["records"]
        if len(records)!=200 or manifest["actual_sessions"]!=200:
            raise SystemExit("BLOCKED_SNAPSHOT_NOT_200_SESSIONS")
        records=sorted(records,key=lambda x:x["trade_date"])
        chosen=records[-10:]
        by_date={r["trade_date"]:r for r in records}
        session_dates=[r["trade_date"] for r in records]
        outputs=[];failures=[];counts={"price_band":0,"surveillance_old":0,"surveillance_new":0}
        session=requests.Session();session.headers.update(HEADERS)
    for idx,rec in enumerate(chosen,start=len(records)-10):
            trade_date=rec["trade_date"]
            prev_date=session_dates[idx-1] if idx>0 else None
            if not prev_date:
                failures.append({"trade_date":trade_date,"error":"missing prior exchange session for surveillance effective-date join"});continue
            ddmmyyyy,ddmmyy=date_parts(trade_date)
            _,prev_ddmmyy=date_parts(prev_date)
            raw_name="raw/"+rec["file"]
            raw=(SNAPSHOT_ROOT/raw_name).read_bytes()
            if sha(raw)!=rec["sha256"]:
                raise SystemExit(f"BLOCKED_BHAVCOPY_SHA256_MISMATCH:{trade_date}")
            bhav=pd.read_csv(BytesIO(raw),dtype=str).fillna("")
            bhav.columns=[str(c).strip() for c in bhav.columns]
            bhav["SYMBOL"]=bhav["SYMBOL"].astype(str).str.strip().str.upper()
            bhav["SERIES"]=bhav["SERIES"].astype(str).str.strip().str.upper()
            pb_url=BASE+"equities/"+f"sec_list_{ddmmyyyy}.csv"
            old_url=BASE+"cm/"+f"REG_IND{prev_ddmmyy}.csv"
            new_url=BASE+"cm/"+f"REG1_IND{prev_ddmmyy}.csv"
            try:
                pb_raw,pb_time=download(session,pb_url);pb=clean_frame(pb_raw,"price_band")
                old_raw,old_time=download(session,old_url);old=clean_frame(old_raw,"surveillance_old")
                new_raw,new_time=download(session,new_url);new=clean_frame(new_raw,"surveillance_new")
                counts["price_band"]+=1;counts["surveillance_old"]+=1;counts["surveillance_new"]+=1
                # Prefix the raw official indicator columns to preserve every indicator without interpretation.
                base_keys=["SYMBOL","SERIES"]
                old=old.rename(columns={c:"REG_IND__"+c for c in old.columns if c not in base_keys})
                new=new.rename(columns={c:"REG1_IND__"+c for c in new.columns if c not in base_keys})
                pb=pb.rename(columns={c:"PRICE_BAND__"+c for c in pb.columns if c not in base_keys})
                merged=bhav.merge(pb,on=base_keys,how="left",validate="one_to_one")
                merged=merged.merge(old,on=base_keys,how="left",validate="one_to_one")
                merged=merged.merge(new,on=base_keys,how="left",validate="one_to_one")
                merged["TRADE_DATE"]=trade_date
                merged["SURVEILLANCE_SOURCE_DATE"]=prev_date
                merged["SURVEILLANCE_EFFECTIVE_DATE"]=trade_date
                merged["SURVEILLANCE_EFFECTIVE_RULE"]="REG_IND file dated prior session applies to next trading day"
                merged["CIRCUIT_STATUS"]="UNKNOWN"
                merged["FREE_FLOAT"]="UNKNOWN"
                merged["BHAVCOPY_SOURCE_URL"]=rec.get("source_url") or ""
                merged["BHAVCOPY_SOURCE_SHA256"]=rec["sha256"]
                merged["BHAVCOPY_PROVENANCE_STATUS"]=rec.get("source_provenance","")
                merged["PRICE_BAND_SOURCE_URL"]=pb_url
                merged["PRICE_BAND_SOURCE_SHA256"]=sha(pb_raw)
                merged["PRICE_BAND_RETRIEVED_AT_UTC"]=pb_time
                merged["REG_IND_SOURCE_URL"]=old_url
                merged["REG_IND_SOURCE_SHA256"]=sha(old_raw)
                merged["REG_IND_RETRIEVED_AT_UTC"]=old_time
                merged["REG1_IND_SOURCE_URL"]=new_url
                merged["REG1_IND_SOURCE_SHA256"]=sha(new_raw)
                merged["REG1_IND_RETRIEVED_AT_UTC"]=new_time
                outputs.append(merged)
                (ROOT/f"raw_{trade_date}_{ddmmyyyy}.json").write_text(json.dumps({
                    "trade_date":trade_date,"surveillance_source_date":prev_date,
                    "bhavcopy_sha256":rec["sha256"],"price_band_url":pb_url,"price_band_sha256":sha(pb_raw),
                    "reg_ind_url":old_url,"reg_ind_sha256":sha(old_raw),
                    "reg1_ind_url":new_url,"reg1_ind_sha256":sha(new_raw),
                    "retrieved_at_utc":{"price_band":pb_time,"reg_ind":old_time,"reg1_ind":new_time}},indent=2))
            except Exception as e:
                failures.append({"trade_date":trade_date,"surveillance_source_date":prev_date,"error":f"{type(e).__name__}: {e}"})
            time.sleep(0.15)
    if not outputs: raise SystemExit("BLOCKED_NO_MARKET_MICROSTRUCTURE_ROWS")
    panel=pd.concat(outputs,ignore_index=True,sort=False)
    out=ROOT/"market_microstructure_10_session.csv"
    panel.to_csv(out,index=False)
    report={
      "status":"PASS_10_SESSION_SMOKE" if len(outputs)==10 and not failures else "PARTIAL",
      "snapshot_id":manifest["snapshot_id"],"snapshot_sessions":manifest["actual_sessions"],
      "probe_sessions":len(outputs),"requested_probe_sessions":10,
      "price_band_files":counts["price_band"],"surveillance_old_files":counts["surveillance_old"],
      "surveillance_new_files":counts["surveillance_new"],"failed_sessions":failures,
      "panel_rows":int(len(panel)),"unique_trade_dates":int(panel["TRADE_DATE"].nunique()),
      "price_band_join_coverage":float(panel["PRICE_BAND__PRICE_BAND_PERCENT"].notna().mean()),
      "reg_ind_join_coverage":float(panel.filter(regex="^REG_IND__").notna().any(axis=1).mean()),
      "reg1_ind_join_coverage":float(panel.filter(regex="^REG1_IND__").notna().any(axis=1).mean()),
      "unknown_circuit_status_rows":int(panel["CIRCUIT_STATUS"].eq("UNKNOWN").sum()),
      "unknown_free_float_rows":int(panel["FREE_FLOAT"].eq("UNKNOWN").sum()),
      "bhavcopy_legacy_source_url_missing_rows":int(panel["BHAVCOPY_SOURCE_URL"].eq("").sum()),
      "promotion_allowed":False,
      "blockers":["Only 10 of 200 sessions tested in this smoke run.",
        "CIRCUIT_STATUS remains UNKNOWN; price-band percentage is not itself proof of a circuit hit.",
        "FREE_FLOAT remains UNKNOWN.",
        "Legacy bhavcopy source URLs/retrieval timestamps are unrecoverable for cached sessions."],
      "output_sha256":sha(out),"observed_at_utc":datetime.now(timezone.utc).isoformat()
    }
    (ROOT/"market_microstructure_10_session_qa.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))
    if report["status"]!="PASS_10_SESSION_SMOKE": raise SystemExit("10-session market microstructure source probe incomplete")
if __name__=="__main__": main()
