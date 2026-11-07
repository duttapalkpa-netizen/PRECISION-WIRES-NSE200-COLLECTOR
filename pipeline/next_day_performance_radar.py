#!/usr/bin/env python3
"""Leakage-safe next-session radar; supplemental to immutable V11.3 production.

Consumes the complete latest normalized official NSE UDiFF EQ file from data/raw,
replaces any partial same-date processed panel, and fails closed on incomplete data.
No changes to selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Hard Gate.
"""
from pathlib import Path
import hashlib, json, re
import numpy as np
import pandas as pd
from pipeline.walk_forward_backtest import (
    add_features, add_tomorrow_features, future_outcomes,
    _robust_return_filter, _calibrated_probability,
)

SRC = Path("data/processed/nse_eq_200_sessions.csv")
RAW_DIR = Path("data/raw")
CANDIDATES = Path("outputs/finalists/v11_3_candidates.csv")
OUT = Path("outputs/finalists")
FEATURES = ["TOMORROW_EXPANSION_SCORE","REPRICING_PRESSURE","READINESS","NOT_YET_MOVED",
            "EXPANSION_READY","EXHAUSTION","RVOL20","RS5","RS20","RET5","DIST_HIGH20","COMPRESSION","ACCEL"]
TARGETS = [("WIN5_H1","P5_H1",1,5),("WIN10_H3","P10_H3",3,10),("WIN20_H5","P20_H5",5,20)]
MIN_DAILY_EQ_ROWS = 1000

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def latest_official_daily():
    candidates=[]
    for p in RAW_DIR.glob("sec_bhavdata_full_*.csv"):
        m=re.fullmatch(r"sec_bhavdata_full_(\d{8})\.csv",p.name)
        if not m: continue
        dt=pd.to_datetime(m.group(1),format="%d%m%Y",errors="coerce")
        if pd.notna(dt): candidates.append((dt,p))
    if not candidates:
        raise FileNotFoundError("No normalized official NSE daily UDiFF EQ source in data/raw")
    dt,path=max(candidates,key=lambda z:z[0])
    daily=pd.read_csv(path,dtype=str)
    daily.columns=[str(c).strip().upper() for c in daily.columns]
    required={"SYMBOL","SERIES","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"}
    missing=sorted(required-set(daily.columns))
    if missing: raise ValueError(f"Latest official daily source schema incomplete: {missing}")
    daily=daily[daily.SERIES.astype(str).str.strip().str.upper().eq("EQ")].copy()
    daily["SYMBOL"]=daily.SYMBOL.astype(str).str.strip().str.upper()
    if "DATE1" in daily:
        source_dates=pd.to_datetime(daily.DATE1,errors="coerce",dayfirst=True).dropna().dt.normalize().unique()
        if len(source_dates)!=1 or pd.Timestamp(source_dates[0])!=dt.normalize():
            raise ValueError(f"Raw daily source date mismatch: filename={dt.date()} dates={list(source_dates)}")
    if len(daily)<MIN_DAILY_EQ_ROWS:
        raise ValueError(f"Latest EQ source incomplete: {len(daily)} rows < fail-closed floor {MIN_DAILY_EQ_ROWS}")
    if daily.SYMBOL.eq("").any() or daily.SYMBOL.duplicated().any():
        raise ValueError("Latest EQ source has blank or duplicate symbols")
    for c in ["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]:
        daily[c]=pd.to_numeric(daily[c].astype(str).str.replace(",","",regex=False),errors="coerce")
        if daily[c].isna().any(): raise ValueError(f"Latest EQ source contains missing/non-numeric {c}")
    if (daily[["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE"]]<=0).any().any():
        raise ValueError("Latest EQ source contains non-positive OHLC")
    if (daily.HIGH_PRICE<daily.LOW_PRICE).any() or (daily.CLOSE_PRICE>daily.HIGH_PRICE).any() or (daily.CLOSE_PRICE<daily.LOW_PRICE).any():
        raise ValueError("Latest EQ source violates OHLC bounds")
    if (daily.TTL_TRD_QNTY<0).any(): raise ValueError("Latest EQ source has negative traded quantity")
    daily["DATE"]=dt
    for c in ["PREV_CLOSE","LAST_PRICE","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER"]:
        if c not in daily: daily[c]=np.nan
        else: daily[c]=pd.to_numeric(daily[c],errors="coerce")
    if "ISIN" not in daily: daily["ISIN"]=""
    return daily,dt,path

def main():
    if not SRC.is_file(): raise FileNotFoundError(f"Required historical dataset missing: {SRC}")
    hist=pd.read_csv(SRC,parse_dates=["DATE"])
    required={"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"}
    missing=sorted(required-set(hist.columns))
    if missing: raise ValueError(f"Historical market dataset schema incomplete: {missing}")
    if hist.empty: raise ValueError("Historical market dataset is empty")
    hist["SYMBOL"]=hist.SYMBOL.astype(str).str.strip().str.upper()
    hist=hist.drop_duplicates(["SYMBOL","DATE"],keep=False)
    if hist.empty: raise ValueError("No unique historical symbol/date rows after strict duplicate exclusion")
    daily,latest,raw_path=latest_official_daily()
    if latest < hist.DATE.max().normalize():
        raise ValueError(f"Latest raw NSE source {latest.date()} is older than processed history {hist.DATE.max().date()}")
    # The complete official daily file is authoritative for its date. Remove a
    # partial processed same-date panel before appending; never mix stale rows.
    hist=hist[hist.DATE.dt.normalize()!=latest].copy()
    combined=pd.concat([hist,daily,],ignore_index=True,sort=False)
    combined=combined.sort_values(["SYMBOL","DATE"]).drop_duplicates(["SYMBOL","DATE"],keep=False)
    if combined.empty: raise ValueError("No unique observations after official daily-source replacement")
    combined=combined.sort_values(["SYMBOL","DATE"])
    combined["DELIV_PER"]=pd.to_numeric(combined.get("DELIV_PER",pd.Series(np.nan,index=combined.index)),errors="coerce")
    x=add_features(combined)
    x=add_tomorrow_features(x)
    x=_robust_return_filter(x)
    x=future_outcomes(x)
    dates=sorted(x.DATE.dropna().unique())
    if len(dates)<26: raise ValueError("At least 26 distinct sessions required for features and matured T+5 labels")
    if pd.Timestamp(dates[-1]).normalize()!=latest.normalize(): raise ValueError("Latest model date does not equal verified raw NSE date")
    current=x[(x.DATE==dates[-1])&(x.HISTORY_DEPTH_AT_T>=20)].copy()
    if current.empty: raise ValueError("No eligible latest-session symbols with >=20 observations")
    history_counts=combined.groupby("SYMBOL").DATE.nunique()
    expected_eligible=int(daily.SYMBOL.isin(history_counts[history_counts>=20].index).sum())
    if current.SYMBOL.nunique()!=expected_eligible:
        raise ValueError(f"Eligible latest-session coverage mismatch: modeled={current.SYMBOL.nunique()} expected={expected_eligible}")
    cutoff=dates[-6]
    train=x[(x.DATE<=cutoff)&(x.HISTORY_DEPTH_AT_T>=20)].copy()
    train=train[~train.ABNORMAL_RETURN_FLAG].copy()
    for target,_,h,threshold in TARGETS:
        vals=train[f"FUT{h}_HIGH_PCT"]
        train[target]=np.where(vals.notna(),(vals>=threshold).astype(float),np.nan)
    train=train.dropna(subset=FEATURES+[t[0] for t in TARGETS])
    calibration={}; all_probs=True
    for target,col,_,_ in TARGETS:
        probs,meta=_calibrated_probability(train,current,target,FEATURES)
        calibration[col]=meta; current[col]=probs
        if meta.get("method")=="UNAVAILABLE" or not np.isfinite(probs).all(): all_probs=False
    if all_probs:
        current["PROBABILITY_STATUS"]="CALIBRATED_OUT_OF_SAMPLE"
        current["RADAR_RANK_BASIS"]="CALIBRATED_P5_H1_THEN_TOMORROW_SCORE"
        current["RADAR_SCORE"]=100*current.P5_H1
    else:
        current[["P5_H1","P10_H3","P20_H5"]]=np.nan
        current["PROBABILITY_STATUS"]="UNKNOWN_INSUFFICIENT_CALIBRATION"
        current["RADAR_RANK_BASIS"]="SIGNAL_ONLY_NOT_PROBABILITY"
        current["RADAR_SCORE"]=current.TOMORROW_EXPANSION_SCORE
    candidate_join="NOT_AVAILABLE"
    if CANDIDATES.is_file():
        cand=pd.read_csv(CANDIDATES)
        if "SYMBOL" in cand and "DATE" in cand:
            cand["DATE"]=pd.to_datetime(cand.DATE,errors="coerce")
            if cand.DATE.max().normalize()==latest.normalize():
                keep=[c for c in ["SYMBOL","V11_3_CORE_SCORE","SCORE","A","B","C","D","E","ANALYSIS_MODE","DATA_CONFIDENCE"] if c in cand]
                if len(keep)>1:
                    current=current.merge(cand[keep].drop_duplicates("SYMBOL"),on="SYMBOL",how="left",validate="one_to_one")
                    candidate_join="SAME_DATE_V11_3_CANDIDATES"
            else: candidate_join="SKIPPED_DATE_MISMATCH"
    current["NEXT_SESSION_DIRECTION"]=np.select(
        [current.TOMORROW_EXPANSION_SCORE>=65,current.TOMORROW_EXPANSION_SCORE<=35],
        ["POSITIVE_SETUP","NEGATIVE_SETUP"],default="NEUTRAL_OR_UNCLEAR")
    current["DATA_ASOF"]=latest.date().isoformat()
    current["TRAINING_MATURED_THROUGH"]=pd.Timestamp(cutoff).date().isoformat()
    current["TRAINING_ROWS"]=int(len(train))
    current["UNIVERSE_SCOPE"]="All EQ symbols in latest official normalized NSE CM UDiFF daily file; scored only with >=20 history sessions"
    current["LIMITATION"]="Intrahorizon HIGH-touch probability, not close-to-close return or guarantee. Delivery excluded when absent."
    cols=["SYMBOL","DATA_ASOF","NEXT_SESSION_DIRECTION","PROBABILITY_STATUS","P5_H1","P10_H3","P20_H5",
          "TOMORROW_EXPANSION_SCORE","RADAR_SCORE","RADAR_RANK_BASIS","REPRICING_PRESSURE","READINESS",
          "NOT_YET_MOVED","EXHAUSTION","RVOL20","RS5","STATE","HISTORY_DEPTH_AT_T","TRAINING_ROWS",
          "TRAINING_MATURED_THROUGH","UNIVERSE_SCOPE","LIMITATION"]
    cols += [c for c in ["V11_3_CORE_SCORE","SCORE","A","B","C","D","E","ANALYSIS_MODE","DATA_CONFIDENCE"] if c in current]
    radar=current[cols].sort_values(["RADAR_SCORE","TOMORROW_EXPANSION_SCORE","SYMBOL"],ascending=[False,False,True])
    OUT.mkdir(parents=True,exist_ok=True)
    out_csv=OUT/"next_day_performance_radar.csv"
    radar.to_csv(out_csv,index=False)
    summary={
      "status":"PASS_SIGNAL_ONLY" if not all_probs else "PASS_CALIBRATED",
      "as_of":latest.date().isoformat(),"raw_source":str(raw_path),"raw_source_sha256":sha256(raw_path),
      "raw_eq_rows":int(len(daily)),"raw_unique_symbols":int(daily.SYMBOL.nunique()),
      "eligible_symbols":int(len(radar)),"history_insufficient_symbols":int(len(daily)-len(radar)),
      "candidate_join_status":candidate_join,"training_matured_through":pd.Timestamp(cutoff).date().isoformat(),
      "calibrated_probabilities_available":bool(all_probs),"calibration":calibration,"training_rows":int(len(train)),
      "unknown_probability_rows":int(radar.P5_H1.isna().sum()),
      "selector_changed":False,"ranking_score_changed":False,"pressure_fade_changed":False,"core_672_changed":False,
      "hard_gate":"UNCHANGED","output":str(out_csv),"output_sha256":sha256(out_csv),
      "universe_scope":"All EQ symbols in latest official normalized NSE CM UDiFF daily file; not all NSE listings"
    }
    (OUT/"next_day_performance_radar_summary.json").write_text(json.dumps(summary,indent=2,default=str)+"\n")
    print(json.dumps(summary,indent=2,default=str))

if __name__=="__main__": main()
