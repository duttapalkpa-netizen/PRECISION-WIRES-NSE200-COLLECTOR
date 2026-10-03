#!/usr/bin/env python3
from pathlib import Path
import io
import pandas as pd
import requests

OUT=Path("data/reference/security_master.csv")
URLS=[
 "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
 "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
]
HEAD={"User-Agent":"Mozilla/5.0","Accept":"text/csv,text/plain,*/*","Referer":"https://www.nseindia.com/"}

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update(HEAD)
    for url in URLS:
        try:
            r=s.get(url,timeout=(10,30))
            if r.status_code!=200 or r.content[:1]==b"<":continue
            df=pd.read_csv(io.BytesIO(r.content),dtype=str)
            df.columns=[str(c).strip().upper() for c in df.columns]
            if "SYMBOL" not in df.columns:continue
            listing=next((c for c in ["LISTING DATE","LISTING_DATE"] if c in df.columns),None)
            isin=next((c for c in ["ISIN NUMBER","ISIN"] if c in df.columns),None)
            out=pd.DataFrame({"SYMBOL":df["SYMBOL"].astype(str).str.strip().str.upper()})
            out["ISIN"]=df[isin] if isin else ""
            out["LISTING_DATE"]=df[listing] if listing else ""
            out=out.drop_duplicates("SYMBOL")
            out.to_csv(OUT,index=False)
            print(f"SECURITY_MASTER_OK rows={len(out)} source={url}")
            return
        except Exception as e:
            print(f"SECURITY_MASTER_WARN {type(e).__name__}: {e}")
    raise SystemExit("Security Master acquisition failed")

if __name__=="__main__":main()
