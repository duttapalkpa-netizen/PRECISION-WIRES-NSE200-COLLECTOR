#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

RAW=Path("data/raw"); OUT=Path("data/processed")
COLS=["SYMBOL","SERIES","ISIN","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","LAST_PRICE","PREV_CLOSE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER"]

def main():
    OUT.mkdir(parents=True, exist_ok=True); frames=[]
    for f in sorted(RAW.glob("sec_bhavdata_full_*.csv")):
        try:
            df=pd.read_csv(f,dtype=str); df.columns=[str(c).strip().upper() for c in df.columns]
            df=df[df["SERIES"].astype(str).str.strip().eq("EQ")].copy()
            df["DATE"]=pd.to_datetime(f.stem[-8:],format="%d%m%Y")
            keep=[c for c in COLS if c in df.columns]+["DATE"]; df=df[keep]
            for c in keep:
                if c not in ("SYMBOL","SERIES","ISIN","DATE"):
                    df[c]=pd.to_numeric(df[c].astype(str).str.replace(",","",regex=False).str.strip(),errors="coerce")
            frames.append(df)
        except Exception as e: print(f"WARN {f}: {e}")
    if not frames: raise SystemExit("No valid raw NSE files")
    all_df=pd.concat(frames,ignore_index=True).drop_duplicates(["SYMBOL","DATE"]).sort_values(["SYMBOL","DATE"])
    all_df.to_csv(OUT/"nse_eq_200_sessions.csv",index=False)
    all_df.groupby("SYMBOL")["DATE"].agg(["count","min","max"]).reset_index().to_csv(OUT/"symbol_session_coverage.csv",index=False)
    print(f"ROWS={len(all_df)} SYMBOLS={all_df.SYMBOL.nunique()} DATES={all_df.DATE.nunique()}")

if __name__=="__main__": main()
