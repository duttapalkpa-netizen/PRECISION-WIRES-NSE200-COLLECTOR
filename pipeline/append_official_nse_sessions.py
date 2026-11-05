#!/usr/bin/env python3
"""Append only newly published official NSE sessions to the immutable 317+ rolling research cache."""
import argparse, hashlib, json
from pathlib import Path
import pandas as pd

ROOT=Path("data/processed")
RAW=Path("data/raw/rolling_incremental")
BASE=ROOT/"nse_eq_rolling_sessions.csv"
MANIFEST=ROOT/"nse_eq_rolling_manifest.json"
REQUIRED=["SYMBOL","SERIES","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","LAST_PRICE","PREV_CLOSE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER","DATE"]

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",action="store_true")
    args=ap.parse_args()
    ROOT.mkdir(parents=True,exist_ok=True)
    if args.seed:
        seed=ROOT/"nse_eq_317_sessions.csv"
        seed_manifest=ROOT/"nse_eq_317_sessions_manifest.json"
        if not seed.exists() or not seed_manifest.exists():
            raise SystemExit("BLOCKED: verified 317-session seed/manifest missing")
        meta=json.loads(seed_manifest.read_text())
        if meta.get("status")!="PASS_SOURCE_RECONCILIATION" or meta.get("sessions")!=317:
            raise SystemExit("BLOCKED: 317 seed manifest not PASS")
        d=pd.read_csv(seed,dtype={"SYMBOL":str,"SERIES":str})
        d["DATE"]=pd.to_datetime(d["DATE"],errors="coerce")
        if d["DATE"].nunique()!=317 or d.duplicated(["SYMBOL","SERIES","DATE"]).any():
            raise SystemExit("BLOCKED: seed calendar/key validation failed")
        d.to_csv(BASE,index=False)
        manifest={"status":"PASS_ROLLING_SEED","seed_sha256":sha(seed),"sessions":317,
                  "first_session":d.DATE.min().date().isoformat(),"last_session":d.DATE.max().date().isoformat(),
                  "append_ledger":[],"guardrails":["research-only","append-only","no synthetic rows",
                  "production selector unchanged","RANKING_SCORE unchanged","+1 PRESSURE_FADE unchanged",
                  "CORE-672 unchanged","UNKNOWN is neither PASS nor FAIL"]}
        MANIFEST.write_text(json.dumps(manifest,indent=2)+"\n")
    if not BASE.exists() or not MANIFEST.exists():
        raise SystemExit("BLOCKED: rolling cache missing; seed step required")
    d=pd.read_csv(BASE,dtype={"SYMBOL":str,"SERIES":str})
    d["DATE"]=pd.to_datetime(d["DATE"],errors="coerce")
    if d["DATE"].isna().any() or d.duplicated(["SYMBOL","SERIES","DATE"]).any():
        raise SystemExit("BLOCKED: rolling cache contains invalid dates or duplicate keys")
    last=d.DATE.max()
    files=sorted(RAW.glob("sec_bhavdata_full_*.csv"))
    additions=[]
    ledger=[]
    for path in files:
        raw=pd.read_csv(path,dtype=str)
        raw.columns=[str(c).strip().upper() for c in raw.columns]
        aliases={"DATE":["DATE","DATE1","TRAD_DT","TRADDT"],"LOW_PRICE":["LOW_PRICE","LOWPRICE","LOW"],
                 "CLOSE_PRICE":["CLOSE_PRICE","CLOSEPRICE","CLOSE"],"OPEN_PRICE":["OPEN_PRICE","OPENPRICE","OPEN"],
                 "HIGH_PRICE":["HIGH_PRICE","HIGHPRICE","HIGH"],"LAST_PRICE":["LAST_PRICE","LASTPRICE","LTP"],
                 "PREV_CLOSE":["PREV_CLOSE","PREVCLOSE","PREV_CL_PR"],"TTL_TRD_QNTY":["TTL_TRD_QNTY","TTLTRDQNTY","TOTTRDQTY"],
                 "TURNOVER_LACS":["TURNOVER_LACS","TURNOVERLACS"],"NO_OF_TRADES":["NO_OF_TRADES","NOOFTRADES"],
                 "DELIV_QTY":["DELIV_QTY","DELIVERY_QTY","DELIVQTY"],"DELIV_PER":["DELIV_PER","DELIVERY_PER","DELIVPER"]}
        out=pd.DataFrame()
        for col in REQUIRED:
            candidates=[col]+aliases.get(col,[])
            found=next((x for x in candidates if x in raw.columns),None)
            if found is None:
                raise SystemExit("BLOCKED: daily official file missing "+col+" in "+path.name)
            out[col]=raw[found]
        out["SYMBOL"]=out.SYMBOL.astype(str).str.strip().str.upper()
        out["SERIES"]=out.SERIES.astype(str).str.strip().str.upper()
        out=out[out.SERIES.eq("EQ")].copy()
        out["DATE"]=pd.to_datetime(out.DATE,errors="coerce",dayfirst=True)
        if out.DATE.isna().any() or out.DATE.nunique()!=1:
            raise SystemExit("BLOCKED: daily file has invalid/multiple dates "+path.name)
        day=out.DATE.iloc[0]
        if day<=last:
            continue
        if day.date()>pd.Timestamp.now(tz="UTC").date():
            raise SystemExit("BLOCKED: source date is in the future")
        for c in REQUIRED:
            if c not in ("SYMBOL","SERIES","DATE"):
                out[c]=pd.to_numeric(out[c].astype(str).str.replace(",","",regex=False),errors="coerce")
        for c in ["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]:
            if out[c].isna().any() or (out[c]<=0).any():
                raise SystemExit("BLOCKED: invalid "+c+" in "+path.name)
        if out.DELIV_PER.dropna().between(0,100).all() is False:
            raise SystemExit("BLOCKED: delivery percentage outside 0..100")
        if out.duplicated(["SYMBOL","SERIES","DATE"]).any():
            raise SystemExit("BLOCKED: duplicate keys in "+path.name)
        additions.append(out)
        ledger.append({"date":day.date().isoformat(),"file":path.name,"sha256":sha(path),"rows":len(out)})
    if additions:
        merged=pd.concat([d]+additions,ignore_index=True)
        merged=merged.sort_values(["DATE","SYMBOL","SERIES"])
        if merged.duplicated(["SYMBOL","SERIES","DATE"]).any():
            raise SystemExit("BLOCKED: append introduces duplicate keys")
        cal=sorted(merged.DATE.dt.strftime("%Y-%m-%d").unique())
        merged.to_csv(BASE,index=False)
        manifest=json.loads(MANIFEST.read_text())
        manifest["status"]="PASS_ROLLING_APPEND"
        manifest["sessions"]=len(cal)
        manifest["first_session"]=cal[0]
        manifest["last_session"]=cal[-1]
        manifest.setdefault("append_ledger",[]).extend(ledger)
        manifest["dataset_sha256"]=sha(BASE)
        MANIFEST.write_text(json.dumps(manifest,indent=2)+"\n")
        print(json.dumps({"status":"PASS_ROLLING_APPEND","appended_sessions":[x["date"] for x in ledger],
                          "sessions":len(cal),"rows":len(merged),"last_session":cal[-1],
                          "dataset_sha256":sha(BASE)},indent=2))
    else:
        print(json.dumps({"status":"PASS_NO_NEW_OFFICIAL_SESSION","sessions":int(d.DATE.nunique()),
                          "last_session":last.date().isoformat(),"dataset_sha256":sha(BASE)},indent=2))

if __name__=="__main__": main()
