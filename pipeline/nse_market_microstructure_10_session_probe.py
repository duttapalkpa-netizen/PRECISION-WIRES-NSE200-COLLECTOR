#!/usr/bin/env python3
"""Ten-session smoke test for historical NSE price-band and surveillance joins."""
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib, json, time, os
import requests
import pandas as pd

ROOT=Path("artifacts/nse_market_microstructure_10_session")
SNAPSHOT_ROOT=Path("inputs/nse_snapshot")
BASE="https://nsearchives.nseindia.com/content/"
BHAVCOPY_BASE="https://archives.nseindia.com/products/content/"
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
    if not SNAPSHOT_ROOT.is_dir(): raise SystemExit("BLOCKED_MISSING_NSE_SNAPSHOT_ARTIFACT")
    manifest_files=list(SNAPSHOT_ROOT.rglob("nse_snapshot_manifest_*.json"))
    if len(manifest_files)!=1: raise SystemExit(f"BLOCKED_EXPECTED_ONE_SNAPSHOT_MANIFEST_FOUND_{len(manifest_files)}")
    manifest=json.loads(manifest_files[0].read_text(encoding="utf-8"))
    records=manifest["records"]
    if len(records)!=200 or manifest["actual_sessions"]!=200:
        raise SystemExit("BLOCKED_SNAPSHOT_NOT_200_SESSIONS")
    records=sorted(records,key=lambda x:x["trade_date"])
    batch_size=int(os.environ.get("MARKET_MICROSTRUCTURE_BATCH_SIZE","10"))
    offset=int(os.environ.get("MARKET_MICROSTRUCTURE_BATCH_OFFSET",str(max(0,len(records)-batch_size))))
    if batch_size<1 or offset<0 or offset+batch_size>len(records):
        raise SystemExit("BLOCKED_INVALID_BATCH_WINDOW")
    chosen=records[offset:offset+batch_size]
    session_dates=[r["trade_date"] for r in records]
    outputs=[];failures=[];counts={"bhavcopy":0,"price_band":0,"surveillance_old":0,"surveillance_new":0}
    session=requests.Session();session.headers.update(HEADERS)
    # The 200-session window begins on 09-Jan-2026; verify 08-Jan directly before using its surveillance file for the first session.
    first_prior_verified=False
    if offset==0:
        prior_url=BHAVCOPY_BASE+"sec_bhavdata_full_08012026.csv"
        try:
            prior_raw,_=download(session,prior_url)
            prior_df=pd.read_csv(BytesIO(prior_raw),dtype=str).fillna("")
            prior_df.columns=[str(x).strip() for x in prior_df.columns]
            assert len(prior_df)>0 and prior_df["DATE1"].astype(str).str.contains("08-Jan-2026",case=False).all()
            first_prior_verified=True
        except Exception as e:
            failures.append({"trade_date":"2026-01-09","error":f"prior-session verification failed: {type(e).__name__}: {e}"})
    for idx,rec in enumerate(chosen,start=offset):
            trade_date=rec["trade_date"]
            prev_date=session_dates[idx-1] if idx>0 else ("2026-01-08" if first_prior_verified else None)
            if not prev_date:
                failures.append({"trade_date":trade_date,"error":"missing prior exchange session for surveillance effective-date join"});continue
            ddmmyyyy,ddmmyy=date_parts(trade_date)
            _,prev_ddmmyy=date_parts(prev_date)
            raw_name="raw/"+rec["file"]
            cached_raw=(SNAPSHOT_ROOT/raw_name).read_bytes()
            if sha(cached_raw)!=rec["sha256"]:
                raise SystemExit(f"BLOCKED_BHAVCOPY_SHA256_MISMATCH:{trade_date}")
            bhavcopy_url=BHAVCOPY_BASE+rec["file"]
            raw,bhavcopy_time=download(session,bhavcopy_url)
            if sha(raw)!=rec["sha256"]:
                failures.append({"trade_date":trade_date,"error":"official bhavcopy re-download SHA-256 differs from frozen snapshot"})
                continue
            counts["bhavcopy"]+=1
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
                merged["BHAVCOPY_SOURCE_URL"]=bhavcopy_url
                merged["BHAVCOPY_SOURCE_SHA256"]=sha(raw)
                merged["BHAVCOPY_REVALIDATED_AT_UTC"]=bhavcopy_time
                merged["BHAVCOPY_PROVENANCE_STATUS"]="OFFICIAL_SOURCE_URL_REVALIDATED_SHA_MATCH"
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
    out=ROOT/f"market_microstructure_batch_{offset}_{batch_size}.csv"
    panel.to_csv(out,index=False)
    report={
      "status":"PASS_BATCH" if len(outputs)==batch_size and not failures and counts["bhavcopy"]==batch_size else "PARTIAL",
      "snapshot_id":manifest["snapshot_id"],"snapshot_sessions":manifest["actual_sessions"],
      "batch_offset":offset,"batch_size":batch_size,"probe_sessions":len(outputs),"requested_probe_sessions":batch_size,
      "bhavcopy_files_sha256_revalidated":counts["bhavcopy"],
      "price_band_files":counts["price_band"],"surveillance_old_files":counts["surveillance_old"],
      "surveillance_new_files":counts["surveillance_new"],"failed_sessions":failures,
      "panel_rows":int(len(panel)),"unique_trade_dates":int(panel["TRADE_DATE"].nunique()),
      "price_band_join_coverage":float(panel["PRICE_BAND__PRICE_BAND_PERCENT"].astype(str).str.strip().ne("").mean()),
      "reg_ind_join_coverage":float(panel.filter(regex="^REG_IND__").astype(str).apply(lambda x:x.str.strip().ne("")).any(axis=1).mean()),
      "reg1_ind_join_coverage":float(panel.filter(regex="^REG1_IND__").astype(str).apply(lambda x:x.str.strip().ne("")).any(axis=1).mean()),
      "unknown_circuit_status_rows":int(panel["CIRCUIT_STATUS"].eq("UNKNOWN").sum()),
      "unknown_free_float_rows":int(panel["FREE_FLOAT"].eq("UNKNOWN").sum()),
      "bhavcopy_source_url_missing_rows":int(panel["BHAVCOPY_SOURCE_URL"].eq("").sum()),
      "promotion_allowed":False,
      "blockers":[f"Only {batch_size} of 200 sessions in this batch.",
        "CIRCUIT_STATUS remains UNKNOWN; price-band percentage is not proof of a circuit hit.",
        "FREE_FLOAT remains UNKNOWN."],
      "output_sha256":sha(out.read_bytes()),"observed_at_utc":datetime.now(timezone.utc).isoformat()
    }
    (ROOT/f"market_microstructure_batch_{offset}_{batch_size}_qa.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))
    if report["status"]!="PASS_BATCH": raise SystemExit("market microstructure source batch incomplete")
if __name__=="__main__": main()
