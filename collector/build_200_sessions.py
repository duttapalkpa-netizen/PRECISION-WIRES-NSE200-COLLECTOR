#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

RAW=Path("data/raw"); OUT=Path("data/processed"); MASTER=Path("data/reference/security_master.csv")
COLS=["SYMBOL","SERIES","ISIN","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","LAST_PRICE","PREV_CLOSE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER"]

def mode(n):
    if n>=200:return "FULL V11.3"
    if n>=100:return "EXTENDED V11.3"
    if n>=50:return "DEVELOPING V11.3"
    if n>=20:return "EARLY V11.3"
    if n>=5:return "EARLY EXPANSION ENGINE"
    if n>=1:return "IPO-PLX V2.0"
    return "DATA UNAVAILABLE"

def confidence(n):
    if n>=200:return "HIGH"
    if n>=100:return "MEDIUM-HIGH"
    if n>=50:return "MEDIUM"
    if n>=20:return "DEVELOPING"
    if n>=5:return "EARLY"
    if n>=1:return "IPO-EARLY"
    return "NONE"

def load_master():
    if not MASTER.exists():
        return pd.DataFrame(columns=["SYMBOL","ISIN","LISTING_DATE"])
    m=pd.read_csv(MASTER,dtype=str)
    m.columns=[str(c).strip().upper() for c in m.columns]
    if "SYMBOL" not in m.columns:return pd.DataFrame(columns=["SYMBOL","ISIN","LISTING_DATE"])
    listing=next((c for c in ["LISTING_DATE","LISTING DATE"] if c in m.columns),None)
    isin=next((c for c in ["ISIN","ISIN NUMBER"] if c in m.columns),None)
    out=pd.DataFrame({"SYMBOL":m["SYMBOL"].astype(str).str.strip().str.upper()})
    out["ISIN"]=m[isin] if isin else ""
    out["LISTING_DATE"]=pd.to_datetime(m[listing],errors="coerce",dayfirst=True) if listing else pd.NaT
    return out.drop_duplicates("SYMBOL")

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    frames=[]
    for f in sorted(RAW.glob("sec_bhavdata_full_*.csv")):
        try:
            df=pd.read_csv(f,dtype=str)
            df.columns=[str(c).strip().upper() for c in df.columns]
            if not {"SERIES","SYMBOL"}.issubset(df.columns):
                print(f"WARN {f}: missing SYMBOL/SERIES");continue
            df=df[df["SERIES"].astype(str).str.strip().eq("EQ")].copy()
            df["DATE"]=pd.to_datetime(f.stem[-8:],format="%d%m%Y",errors="coerce")
            keep=[c for c in COLS if c in df.columns]+["DATE"]
            df=df[keep]
            for c in keep:
                if c not in ("SYMBOL","SERIES","ISIN","DATE"):
                    df[c]=pd.to_numeric(df[c].astype(str).str.replace(",","",regex=False).str.strip(),errors="coerce")
            df["SYMBOL"]=df["SYMBOL"].astype(str).str.strip().str.upper()
            frames.append(df)
        except Exception as e: print(f"WARN {f}: {e}")
    if not frames: raise SystemExit("No valid raw NSE files")
    all_df=pd.concat(frames,ignore_index=True).drop_duplicates(["SYMBOL","DATE"]).sort_values(["SYMBOL","DATE"]).reset_index(drop=True)

    cov=(all_df.groupby("SYMBOL")["DATE"].agg(AVAILABLE_SESSIONS="count",FIRST_OBSERVED_SESSION="min",LAST_OBSERVED_SESSION="max").reset_index())
    cov=cov.merge(load_master(),on="SYMBOL",how="left")
    cov["LISTING_DATE_SOURCE"]=cov["LISTING_DATE"].notna().map({True:"NSE_SECURITY_MASTER",False:"FIRST_OBSERVED_SESSION_PROXY"})
    cov["LISTING_DATE"]=cov["LISTING_DATE"].fillna(cov["FIRST_OBSERVED_SESSION"])

    market_dates=pd.Series(sorted(all_df["DATE"].dropna().unique()))
    cov["AGE_SESSIONS"]=cov["LISTING_DATE"].apply(lambda d:int((market_dates>=d).sum()) if pd.notna(d) else 0)
    cov["HISTORY_DEPTH"]=cov["AVAILABLE_SESSIONS"]
    cov["ANALYSIS_MODE"]=cov["AVAILABLE_SESSIONS"].map(mode)
    cov["DATA_CONFIDENCE"]=cov["AVAILABLE_SESSIONS"].map(confidence)
    cov["OBSERVATION_COVERAGE_PCT"]=(100*cov["AVAILABLE_SESSIONS"]/cov["AGE_SESSIONS"].clip(lower=1)).round(2)

    all_df=all_df.merge(cov[["SYMBOL","LISTING_DATE","LISTING_DATE_SOURCE","AGE_SESSIONS","HISTORY_DEPTH","ANALYSIS_MODE","DATA_CONFIDENCE","OBSERVATION_COVERAGE_PCT"]],on="SYMBOL",how="left")
    all_df.to_csv(OUT/"nse_eq_200_sessions.csv",index=False)
    cov.to_csv(OUT/"symbol_session_coverage.csv",index=False)
    print(f"ROWS={len(all_df)} SYMBOLS={all_df.SYMBOL.nunique()} DATES={all_df.DATE.nunique()}")
    print(cov["ANALYSIS_MODE"].value_counts().to_string())

if __name__=="__main__": main()
