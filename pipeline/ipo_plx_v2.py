#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd

SRC=Path("data/processed/nse_eq_200_sessions.csv")
OUT=Path("outputs/ipo_plx")

def pct(a,b):
    return (a/b-1)*100 if pd.notna(a) and pd.notna(b) and b else np.nan

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(SRC,parse_dates=["DATE","LISTING_DATE"]).sort_values(["SYMBOL","DATE"])
    rows=[]
    for sym,g in df.groupby("SYMBOL",sort=False):
        g=g.dropna(subset=["CLOSE_PRICE"]).copy()
        n=len(g)
        if n<1 or n>4:continue
        listing=g["LISTING_DATE"].iloc[-1];first=g["DATE"].iloc[0]
        # Only treat a 1-4 session record as IPO-like when the listing-date
        # evidence is recent; otherwise retain it as incomplete data, not an IPO.
        if pd.notna(listing) and (first-listing).days>20:continue
        c=g["CLOSE_PRICE"];v=g["TTL_TRD_QNTY"].fillna(0)
        base=v.iloc[:-1].mean() if n>1 else np.nan
        rvol=v.iloc[-1]/base if pd.notna(base) and base>0 else np.nan
        vwap=(c*v).sum()/v.sum() if v.sum()>0 else np.nan
        first_close=float(c.iloc[0]);last_close=float(c.iloc[-1]);high=float(c.max());low=float(c.min())
        expansion=max(pct(high,first_close),pct(last_close,first_close))
        vwap_hold=bool(last_close>=vwap) if pd.notna(vwap) else False
        hh=bool(high==last_close);hl=bool(last_close>=low)
        if vwap_hold and hh and pd.notna(expansion) and expansion>=5:
            status="EXPANSION ACTIVE"
        elif vwap_hold and pd.notna(rvol) and rvol>=1.5:
            status="WATCH / RE-IGNITION"
        elif pd.notna(expansion) and expansion>=5 and vwap_hold:
            status="ALREADY EXPANDED — NOT EXHAUSTED"
        else:
            status="NON-WINNER PROFILE"
        rows.append({
            "SYMBOL":sym,"LISTING_DATE":listing.date() if pd.notna(listing) else None,
            "AVAILABLE_SESSIONS":n,"HISTORY_DEPTH":n,
            "ANALYSIS_MODE":g["ANALYSIS_MODE"].iloc[-1],
            "DATA_CONFIDENCE":g["DATA_CONFIDENCE"].iloc[-1],
            "FIRST_CLOSE":first_close,"LAST_CLOSE":last_close,"HIGH":high,"LOW":low,
            "VWAP_PROXY":vwap,"RVOL_PROXY":rvol,"EXPANSION_PCT":expansion,
            "VWAP_HOLD":vwap_hold,"HH":hh,"HL":hl,"STATUS":status,
            "VECTOR":"L-F-D-R-A-V-B-P-S-C-X-E",
            "DATA_NOTE":"Foundation uses available Bhavcopy OHLCV only. Subscription, GMP, effective float, anchor lock-up, first-hour RVOL/VWAP/ORB, queue and catalyst remain UNKNOWN until dedicated sources are wired."
        })
    out=pd.DataFrame(rows)
    if not out.empty:out=out.sort_values(["EXPANSION_PCT","RVOL_PROXY"],ascending=False,na_position="last")
    out.to_csv(OUT/"ipo_plx_candidates.csv",index=False)
    print(f"IPO_PLX_ROWS={len(out)}")
    if not out.empty:print(out.head(20).to_string(index=False))

if __name__=="__main__":main()
