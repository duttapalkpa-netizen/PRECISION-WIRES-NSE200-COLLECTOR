#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd, requests, time, json, math

ROOT=Path(".")
OUT=ROOT/"data/live"
OUT.mkdir(parents=True,exist_ok=True)
H={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36",
    "Accept":"application/json,text/plain,*/*",
    "Referer":"https://www.nseindia.com/",
}

def num(v):
    try:return float(str(v).replace(",","").strip())
    except:return float("nan")

def capital_market_open(s):
    try:
        j=s.get("https://www.nseindia.com/api/marketStatus",timeout=(10,15)).json()
        for x in j.get("marketState",[]):
            if x.get("market")=="Capital Market":
                return str(x.get("marketStatus","")).upper() in {"OPEN","OPENING","PRE-OPEN"}
    except Exception:
        pass
    return False

def quote(s,sym):
    r=s.get("https://www.nseindia.com/api/quote-equity",params={"symbol":sym},timeout=(10,15))
    r.raise_for_status()
    j=r.json()
    pi=j.get("priceInfo",{})
    info=j.get("info",{})
    return {
        "prev_close":num(pi.get("previousClose")),
        "open":num(pi.get("open")),
        "ltp":num(pi.get("lastPrice")),
        "vwap":num(pi.get("vwap") if pi.get("vwap") is not None else pi.get("averagePrice")),
        "volume":num(pi.get("totalTradedVolume") if pi.get("totalTradedVolume") is not None else j.get("securityWiseDP",{}).get("quantityTraded")),
        "company":info.get("companyName","")
    }

def chart(s,sym):
    r=s.get("https://www.nseindia.com/api/chart-databyindex",params={"index":sym+"EQN"},timeout=(10,15))
    r.raise_for_status()
    j=r.json()
    gd=j.get("grapthData",[])
    return [(pd.to_datetime(ts,unit="ms",utc=True),float(val)) for ts,val in gd]

def main():
    cand=Path("outputs/finalists/v11_3_candidates.csv")
    hist=Path("data/processed/nse_eq_200_sessions.csv")
    if not cand.exists(): raise SystemExit("V11.3 candidates missing")
    syms=pd.read_csv(cand)["SYMBOL"].head(30).astype(str).tolist()
    hdf=pd.read_csv(hist) if hist.exists() else pd.DataFrame()
    if not hdf.empty and "SYMBOL" in hdf and "VOLUME" in hdf:
        hdf["VOLUME"]=pd.to_numeric(hdf["VOLUME"],errors="coerce")
        avg20=hdf.groupby("SYMBOL")["VOLUME"].apply(lambda x:x.tail(20).mean()).to_dict()
    else: avg20={}

    s=requests.Session(); s.headers.update(H)
    try:s.get("https://www.nseindia.com/",timeout=(10,20))
    except Exception:pass

    # On scheduled market-hours runs, wait/retry so a delayed GitHub runner
    # still gets the current-day NSE stream. Never manufacture rows.
    attempts=12
    all_rows=[]
    quote_rows=[]
    for attempt in range(attempts):
        all_rows=[]; quote_rows=[]
        for sym in syms:
            try:
                gd=chart(s,sym)
                q=quote(s,sym)
                if gd:
                    for ts,val in gd:
                        all_rows.append({"SYMBOL":sym,"TIMESTAMP":ts.isoformat(),"CLOSE":val})
                    quote_rows.append({"SYMBOL":sym,**q,"CHART_POINTS":len(gd)})
            except Exception:
                pass
            time.sleep(.10)
        if all_rows:
            break
        time.sleep(60)

    if not all_rows:
        meta={"status":"NO_LIVE_1M_DATA","rows":0,"symbols":0,"attempts":attempts,
              "market_open_observed":capital_market_open(s),
              "captured_at":datetime.now(timezone.utc).isoformat(),
              "source":"NSE current-day chart-databyindex + quote-equity"}
    else:
        d=pd.DataFrame(all_rows).drop_duplicates(["SYMBOL","TIMESTAMP"]).sort_values(["SYMBOL","TIMESTAMP"])
        qdf=pd.DataFrame(quote_rows).drop_duplicates("SYMBOL")
        d["SESSION_DATE"]=pd.to_datetime(d["TIMESTAMP"],utc=True).dt.date.astype(str)
        d["PREV_CLOSE"]=d["SYMBOL"].map(qdf.set_index("SYMBOL")["prev_close"])
        d["DAY_VWAP"]=d["SYMBOL"].map(qdf.set_index("SYMBOL")["vwap"])
        d["DAY_VOLUME"]=d["SYMBOL"].map(qdf.set_index("SYMBOL")["volume"])
        d["AVG20_VOLUME"]=d["SYMBOL"].map(avg20)
        d["DAY_RVOL"]=d["DAY_VOLUME"]/d["AVG20_VOLUME"]
        summaries=[]
        for sym,g in d.groupby("SYMBOL"):
            g=g.sort_values("TIMESTAMP")
            prev=num(g["PREV_CLOSE"].iloc[-1])
            vwap=num(g["DAY_VWAP"].iloc[-1])
            last=num(g["CLOSE"].iloc[-1])
            first15=g.head(min(15,len(g)))
            orb_high=num(first15["CLOSE"].max()) if len(first15) else float("nan")
            gain=((last/prev)-1)*100 if prev and not math.isnan(prev) else float("nan")
            rvol=num(g["DAY_RVOL"].iloc[-1])
            vwap_ok=bool(not math.isnan(vwap) and last>=vwap)
            orb_ok=bool(not math.isnan(orb_high) and last>orb_high)
            if gain>=1 and vwap_ok and (math.isnan(rvol) or rvol>=1.0):
                status="IGNITION CONFIRMED"
            elif gain>=1 or vwap_ok:
                status="TOUCH-WAIT"
            else:
                status="FALSE IGNITION"
            summaries.append({
                "SYMBOL":sym,"LAST":last,"PREV_CLOSE":prev,"GAIN_PCT":gain,
                "DAY_VWAP":vwap,"ORB_HIGH_15":orb_high,"DAY_RVOL":rvol,
                "VWAP_HOLD":vwap_ok,"ORB_BREAK":orb_ok,
                "LIVE_1PCT_STATUS":status
            })
        sd=pd.DataFrame(summaries)
        d.to_csv(OUT/"intraday_1m.csv",index=False)
        sd.to_csv(OUT/"live_1m_candidates.csv",index=False)
        meta={"status":"LIVE_1M_CAPTURED","rows":len(d),"symbols":d.SYMBOL.nunique(),
              "attempts":attempt+1,"market_open_observed":capital_market_open(s),
              "captured_at":datetime.now(timezone.utc).isoformat(),
              "source":"NSE current-day chart-databyindex + quote-equity",
              "feed_note":"1-minute price chart plus NSE quote day VWAP/volume; licensed 1-minute volume feed is not claimed"}

    (OUT/"live_1m_status.json").write_text(json.dumps(meta,indent=2,default=str),encoding="utf-8")
    print(json.dumps(meta,indent=2))
    if meta["status"]!="LIVE_1M_CAPTURED": raise SystemExit(2)

if __name__=="__main__":
    main()
