#!/usr/bin/env python3
"""Rebuild the verified historical NSE 317-session source from prior Actions artifacts."""
import hashlib, json
from pathlib import Path
import pandas as pd

def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest()

def find_one(root, pattern):
    items=list(Path(root).rglob(pattern))
    if len(items)!=1: raise SystemExit("BLOCKED: expected exactly one "+pattern)
    return items[0]

def main():
    base_path=find_one("artifacts/baseline","nse_eq_200_sessions.csv")
    if sha(base_path)!="8165073d0bdd7b2da8accd4780e4154aee336e54d6f43803248f77d95b8a0959":
        raise SystemExit("BLOCKED: baseline SHA-256 mismatch")
    base=pd.read_csv(base_path,dtype={"SYMBOL":str,"SERIES":str})
    base["DATE"]=pd.to_datetime(base["DATE"],errors="coerce")
    if base.DATE.nunique()!=200: raise SystemExit("BLOCKED: baseline is not 200 sessions")
    parts=[("artifacts/backfill_57",57,"2025-11-04","2026-01-27"),
           ("artifacts/backfill_60",60,"2025-08-06","2025-11-03")]
    frames=[base]
    dates_all=[]
    for folder,count,first,last in parts:
        manifest=json.loads(find_one(folder,"*MANIFEST*.json").read_text())
        records=manifest.get("files",[])
        if len(records)!=count: raise SystemExit("BLOCKED: backfill manifest count mismatch")
        dates=[]
        for rec in records:
            raw=find_one(folder,rec["file"])
            if sha(raw)!=rec["sha256"]: raise SystemExit("BLOCKED: raw SHA mismatch "+raw.name)
            day=rec["trading_date"]; dates.append(day)
            df=pd.read_csv(raw,dtype=str)
            df.columns=[str(c).strip().upper() for c in df.columns]
            cols=["SYMBOL","SERIES","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","LAST_PRICE","PREV_CLOSE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER"]
            if not set(cols).issubset(df.columns): raise SystemExit("BLOCKED: raw schema mismatch "+raw.name)
            df=df[df.SERIES.astype(str).str.strip().str.upper().eq("EQ")].copy()
            df["DATE"]=pd.Timestamp(day)
            for c in cols:
                if c not in ("SYMBOL","SERIES"): df[c]=pd.to_numeric(df[c].astype(str).str.replace(",","",regex=False),errors="coerce")
            frames.append(df[cols+["DATE"]])
        if len(set(dates))!=count or min(dates)!=first or max(dates)!=last:
            raise SystemExit("BLOCKED: backfill calendar mismatch")
        dates_all.extend(dates)
    if len(set(dates_all))!=117: raise SystemExit("BLOCKED: duplicate backfill dates")
    merged=pd.concat(frames,ignore_index=True,sort=False)
    merged["SYMBOL"]=merged.SYMBOL.astype(str).str.strip().str.upper()
    merged["SERIES"]=merged.SERIES.astype(str).str.strip().str.upper()
    merged["DATE"]=pd.to_datetime(merged.DATE,errors="coerce")
    merged=merged[merged.SERIES.eq("EQ")].copy()
    if merged.duplicated(["SYMBOL","SERIES","DATE"]).any(): raise SystemExit("BLOCKED: duplicate symbol/date rows")
    cal=sorted(merged.DATE.dropna().dt.strftime("%Y-%m-%d").unique())
    if len(cal)!=317 or cal[0]!="2025-08-06" or cal[-1]!="2026-11-03": raise SystemExit("BLOCKED: merged date range mismatch")
    if len(merged)!=765887 or merged.SYMBOL.nunique()!=3040: raise SystemExit("BLOCKED: row/symbol totals mismatch")
    out=Path("data/processed/nse_eq_317_sessions.csv")
    out.parent.mkdir(parents=True,exist_ok=True)
    merged.to_csv(out,index=False)
    report={"status":"PASS_SOURCE_RECONCILIATION","sessions":len(cal),"first_session":cal[0],"last_session":cal[-1],"rows":len(merged),"symbols":int(merged.SYMBOL.nunique()),"sha256":sha(out),"baseline_run":41633211838,"backfill_runs":[41846486071,41887855100],"guardrails":["research-only","no synthetic rows","production selector unchanged","RANKING_SCORE unchanged","+1 PRESSURE_FADE unchanged","CORE-672 unchanged","UNKNOWN is neither PASS nor FAIL"]}
    Path("data/processed/nse_eq_317_sessions_manifest.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
