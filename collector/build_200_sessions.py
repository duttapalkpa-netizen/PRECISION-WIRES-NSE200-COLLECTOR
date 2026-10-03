#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

RAW=Path("data/raw"); OUT=Path("data/processed")
COLS=["SYMBOL","SERIES","ISIN","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","LAST_PRICE","PREV_CLOSE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER"]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    frames=[]
    for f in sorted(RAW.glob("sec_bhavdata_full_*.csv")):
        try:
            df=pd.read_csv(f,dtype=str)
            df.columns=[str(c).strip().upper() for c in df.columns]
            if "SERIES" not in df.columns or "SYMBOL" not in df.columns:
                print(f"WARN {f}: missing SYMBOL/SERIES")
                continue
            df=df[df["SERIES"].astype(str).str.strip().eq("EQ")].copy()
            df["DATE"]=pd.to_datetime(f.stem[-8:],format="%d%m%Y")
            keep=[c for c in COLS if c in df.columns]+["DATE"]
            df=df[keep]
            for c in keep:
                if c not in ("SYMBOL","SERIES","ISIN","DATE"):
                    df[c]=pd.to_numeric(df[c].astype(str).str.replace(",","",regex=False).str.strip(),errors="coerce")
            frames.append(df)
        except Exception as e:
            print(f"WARN {f}: {e}")
    if not frames:
        raise SystemExit("No valid raw NSE files")

    all_df=(pd.concat(frames,ignore_index=True)
              .drop_duplicates(["SYMBOL","DATE"])
              .sort_values(["SYMBOL","DATE"]))

    # 200+ sessions is the MARKET historical backbone, not a stock-level eligibility gate.
    # Security age is measured from the first observed session in the acquired backbone.
    # When an NSE Security Master listing date is later wired in, it should replace this proxy.
    coverage=(all_df.groupby("SYMBOL")["DATE"]
              .agg(AVAILABLE_SESSIONS="count", FIRST_OBSERVED_SESSION="min", LAST_OBSERVED_SESSION="max")
              .reset_index())
    coverage["LISTING_DATE"]=coverage["FIRST_OBSERVED_SESSION"]
    coverage["LISTING_DATE_SOURCE"]="FIRST_OBSERVED_SESSION_PROXY"
    coverage["AGE_SESSIONS"]=coverage["AVAILABLE_SESSIONS"]

    def mode(n):
        if n >= 200: return "FULL V11.3"
        if n >= 100: return "EXTENDED V11.3"
        if n >= 50: return "DEVELOPING V11.3"
        if n >= 20: return "EARLY V11.3"
        if n >= 5: return "EARLY EXPANSION ENGINE"
        if n >= 1: return "IPO-PLX V2.0"
        return "DATA UNAVAILABLE"

    def confidence(n):
        if n >= 200: return "HIGH"
        if n >= 100: return "MEDIUM-HIGH"
        if n >= 50: return "MEDIUM"
        if n >= 20: return "DEVELOPING"
        if n >= 5: return "EARLY"
        if n >= 1: return "IPO-EARLY"
        return "NONE"

    coverage["HISTORY_DEPTH"]=coverage["AVAILABLE_SESSIONS"]
    coverage["ANALYSIS_MODE"]=coverage["AVAILABLE_SESSIONS"].map(mode)
    coverage["DATA_CONFIDENCE"]=coverage["AVAILABLE_SESSIONS"].map(confidence)

    all_df=all_df.merge(
        coverage[["SYMBOL","LISTING_DATE","LISTING_DATE_SOURCE","AGE_SESSIONS","HISTORY_DEPTH","ANALYSIS_MODE","DATA_CONFIDENCE"]],
        on="SYMBOL",how="left"
    )

    all_df.to_csv(OUT/"nse_eq_200_sessions.csv",index=False)
    coverage.to_csv(OUT/"symbol_session_coverage.csv",index=False)
    print(f"ROWS={len(all_df)} SYMBOLS={all_df.SYMBOL.nunique()} DATES={all_df.DATE.nunique()}")
    print(coverage["ANALYSIS_MODE"].value_counts().to_string())

if __name__=="__main__":
    main()
