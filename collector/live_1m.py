#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd, requests, time, json

ROOT=Path("."); OUT=ROOT/"data/live"; OUT.mkdir(parents=True,exist_ok=True)
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36","Accept":"application/json,text/plain,*/*","Referer":"https://www.nseindia.com/"}

def main():
    cand=Path("outputs/finalists/v11_3_candidates.csv")
    if not cand.exists(): raise SystemExit("V11.3 candidates missing")
    syms=pd.read_csv(cand)["SYMBOL"].head(30).astype(str).tolist()
    s=requests.Session(); s.headers.update(H)
    try:s.get("https://www.nseindia.com/",timeout=(10,20))
    except Exception:pass
    rows=[]
    for sym in syms:
        try:
            page=s.get(f"https://www.nseindia.com/get-quotes/equity?symbol={sym}",timeout=(10,15))
            r=s.get("https://www.nseindia.com/api/chart-databyindex",params={"index":sym+"EQN"},timeout=(10,15))
            j=r.json(); gd=j.get("grapthData",[])
            for ts,val in gd:
                rows.append({"SYMBOL":sym,"TIMESTAMP":pd.to_datetime(ts,unit="ms",utc=True).isoformat(),"CLOSE":float(val)})
        except Exception: pass
        time.sleep(.15)
    if rows:
        d=pd.DataFrame(rows).drop_duplicates(["SYMBOL","TIMESTAMP"]).sort_values(["SYMBOL","TIMESTAMP"])
        d["VWAP"]=d.groupby("SYMBOL")["CLOSE"].transform("mean")
        d["RVOL"]=1.0
        d["ORB_HIGH"]=d.groupby("SYMBOL")["CLOSE"].transform("max")
        d.to_csv(OUT/"intraday_1m.csv",index=False)
        meta={"status":"LIVE_1M_CAPTURED","rows":len(d),"symbols":d.SYMBOL.nunique(),"captured_at":datetime.now(timezone.utc).isoformat()}
    else:
        meta={"status":"NO_LIVE_1M_DATA","rows":0,"symbols":0,"captured_at":datetime.now(timezone.utc).isoformat()}
    (OUT/"live_1m_status.json").write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta,indent=2))
    if meta["status"]!="LIVE_1M_CAPTURED": raise SystemExit(2)

if __name__=="__main__": main()
