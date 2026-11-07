#!/usr/bin/env python3
"""Leakage-safe next-trading-session radar; supplemental output only.

Does not alter the V11.3 selector, RANKING_SCORE, +1 PRESSURE_FADE or CORE-672.
Probabilities are emitted only when the existing walk-forward calibration method
has sufficient matured training data. Otherwise probability fields remain UNKNOWN.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from pipeline.walk_forward_backtest import (
    add_features, add_tomorrow_features, future_outcomes,
    _robust_return_filter, _calibrated_probability,
)

SRC = Path("data/processed/nse_eq_200_sessions.csv")
CANDIDATES = Path("outputs/finalists/v11_3_candidates.csv")
OUT = Path("outputs/finalists")
FEATURES = ["TOMORROW_EXPANSION_SCORE","REPRICING_PRESSURE","READINESS","NOT_YET_MOVED",
            "EXPANSION_READY","EXHAUSTION","RVOL20","RS5","RS20","RET5","DIST_HIGH20","COMPRESSION","ACCEL"]
TARGETS = [("WIN5_H1","P5_H1",1,5),("WIN10_H3","P10_H3",3,10),("WIN20_H5","P20_H5",5,20)]

def main():
    if not SRC.is_file():
        raise FileNotFoundError(f"Required verified market dataset missing: {SRC}")
    raw = pd.read_csv(SRC, parse_dates=["DATE"])
    required = {"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY","DELIV_PER"}
    missing = sorted(required - set(raw.columns))
    if missing:
        raise ValueError(f"Market dataset schema incomplete: {missing}")
    if raw.empty:
        raise ValueError("Market dataset is empty")
    raw = raw.sort_values(["SYMBOL","DATE"]).drop_duplicates(["SYMBOL","DATE"], keep=False)
    if raw.empty:
        raise ValueError("No unique symbol/date rows after strict duplicate exclusion")
    x = add_features(raw)
    x = add_tomorrow_features(x)
    x = _robust_return_filter(x)
    x = future_outcomes(x)
    dates = sorted(x.DATE.dropna().unique())
    if len(dates) < 26:
        raise ValueError("At least 26 distinct sessions are required for 20-session features and a matured 5-session label window")
    latest = dates[-1]
    cutoff = dates[-6]  # Last training cutoff with fully matured T+1..T+5 outcomes.
    current = x[(x.DATE == latest) & (x.HISTORY_DEPTH_AT_T >= 20)].copy()
    if current.empty:
        raise ValueError("No eligible current-session symbols with >=20 observations")
    train = x[(x.DATE <= cutoff) & (x.HISTORY_DEPTH_AT_T >= 20)].copy()
    train = train[~train.ABNORMAL_RETURN_FLAG].copy()
    for target, _, h, threshold in TARGETS:
        vals = train[f"FUT{h}_HIGH_PCT"]
        train[target] = np.where(vals.notna(), (vals >= threshold).astype(float), np.nan)
    train = train.dropna(subset=FEATURES + [t[0] for t in TARGETS])
    calibration = {}
    all_probabilities_available = True
    for target, col, _, _ in TARGETS:
        probs, meta = _calibrated_probability(train, current, target, FEATURES)
        calibration[col] = meta
        current[col] = probs
        if meta.get("method") == "UNAVAILABLE" or not np.isfinite(probs).all():
            all_probabilities_available = False
    if all_probabilities_available:
        current["PROBABILITY_STATUS"] = "CALIBRATED_OUT_OF_SAMPLE"
        current["RADAR_RANK_BASIS"] = "CALIBRATED_P5_H1_THEN_TOMORROW_SCORE"
        current["RADAR_SCORE"] = 100 * current["P5_H1"]
    else:
        current[["P5_H1","P10_H3","P20_H5"]] = np.nan
        current["PROBABILITY_STATUS"] = "UNKNOWN_INSUFFICIENT_CALIBRATION"
        current["RADAR_RANK_BASIS"] = "SIGNAL_ONLY_NOT_PROBABILITY"
        current["RADAR_SCORE"] = current["TOMORROW_EXPANSION_SCORE"]
    if CANDIDATES.is_file():
        cand = pd.read_csv(CANDIDATES)
        if "SYMBOL" in cand.columns:
            keep = [c for c in ["SYMBOL","V11_3_CORE_SCORE","SCORE","A","B","C","D","E","ANALYSIS_MODE","DATA_CONFIDENCE"] if c in cand.columns]
            if len(keep) > 1:
                current = current.merge(cand[keep].drop_duplicates("SYMBOL"), on="SYMBOL", how="left", validate="one_to_one")
    current["NEXT_SESSION_DIRECTION"] = np.select(
        [current.TOMORROW_EXPANSION_SCORE >= 65, current.TOMORROW_EXPANSION_SCORE <= 35],
        ["POSITIVE_SETUP","NEGATIVE_SETUP"], default="NEUTRAL_OR_UNCLEAR")
    current["DATA_ASOF"] = pd.Timestamp(latest).date().isoformat()
    current["TRAINING_MATURED_THROUGH"] = pd.Timestamp(cutoff).date().isoformat()
    current["TRAINING_ROWS"] = int(len(train))
    current["UNIVERSE_SCOPE"] = "All eligible symbols present in processed NSE 200-session source; not all NSE listings"
    current["LIMITATION"] = "Next-session outcomes are uncertain. P5_H1 is probability of a >=5% intrahorizon HIGH within next session, not a guaranteed close-to-close return."
    cols = ["SYMBOL","DATA_ASOF","NEXT_SESSION_DIRECTION","PROBABILITY_STATUS","P5_H1","P10_H3","P20_H5",
            "TOMORROW_EXPANSION_SCORE","RADAR_SCORE","RADAR_RANK_BASIS","REPRICING_PRESSURE","READINESS",
            "NOT_YET_MOVED","EXHAUSTION","RVOL20","RS5","STATE","HISTORY_DEPTH_AT_T","TRAINING_ROWS",
            "TRAINING_MATURED_THROUGH","UNIVERSE_SCOPE","LIMITATION"]
    cols += [c for c in ["V11_3_CORE_SCORE","SCORE","A","B","C","D","E","ANALYSIS_MODE","DATA_CONFIDENCE"] if c in current.columns]
    radar = current[cols].sort_values(["RADAR_SCORE","TOMORROW_EXPANSION_SCORE","SYMBOL"], ascending=[False,False,True])
    OUT.mkdir(parents=True,exist_ok=True)
    radar.to_csv(OUT/"next_day_performance_radar.csv",index=False)
    summary = {
        "status":"PASS_SIGNAL_ONLY" if not all_probabilities_available else "PASS_CALIBRATED",
        "as_of":pd.Timestamp(latest).date().isoformat(),
        "training_matured_through":pd.Timestamp(cutoff).date().isoformat(),
        "eligible_symbols":int(len(radar)),
        "calibrated_probabilities_available":bool(all_probabilities_available),
        "calibration":calibration,
        "training_rows":int(len(train)),
        "unknown_probability_rows":int(radar.P5_H1.isna().sum()),
        "universe_scope":"All eligible symbols in processed NSE 200-session source; not all NSE listings",
        "selector_changed":False,
        "ranking_score_changed":False,
        "pressure_fade_changed":False,
        "core_672_changed":False,
        "hard_gate":"UNCHANGED",
        "output":"outputs/finalists/next_day_performance_radar.csv"
    }
    (OUT/"next_day_performance_radar_summary.json").write_text(json.dumps(summary,indent=2,default=str)+"\n")
    print(json.dumps(summary,indent=2,default=str))
if __name__ == "__main__":
    main()
