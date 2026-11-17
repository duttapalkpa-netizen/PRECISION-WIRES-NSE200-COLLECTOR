#!/usr/bin/env python3
"""Research-only OHLC trade replay. Does not import or modify production selector logic."""
from __future__ import annotations
import argparse, hashlib, json, os, platform
from pathlib import Path
import numpy as np
import pandas as pd

COST_PCT = 0.22
TARGETS = ((5.0, 1), (10.0, 3), (20.0, 5))
REQUIRED = {"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"}

def _valid_bar(row):
    vals=[row[k] for k in ("OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE")]
    if not all(pd.notna(v) and np.isfinite(float(v)) and float(v)>0 for v in vals):
        return False
    o,h,l,c=map(float,vals)
    volume=float(row["TTL_TRD_QNTY"])
    return h >= max(o,l,c) and l <= min(o,h,c) and np.isfinite(volume) and volume > 0

def simulate_one(bars, cutoff, symbol, target_pct, horizon, cost_pct=COST_PCT):
    """Entry next global session OPEN; stop -3%; target intraday HIGH; stop-first on ambiguous OHLC bar."""
    if not np.isfinite(cost_pct) or cost_pct < 0:
        raise ValueError("cost_pct must be finite and non-negative")
    if not np.isfinite(target_pct) or target_pct <= 0:
        raise ValueError("target_pct must be finite and positive")
    if isinstance(horizon, bool) or int(horizon) != horizon or horizon <= 0:
        raise ValueError("horizon must be a positive integer")
    if not REQUIRED.issubset(bars.columns):
        raise ValueError(f"bars missing required columns: {sorted(REQUIRED-set(bars.columns))}")
    parsed_dates=pd.to_datetime(bars["DATE"],errors="coerce")
    if parsed_dates.isna().any():
        raise ValueError("invalid DATE values")
    if bars.assign(_DATE=parsed_dates).duplicated(["SYMBOL","_DATE"]).any():
        raise ValueError("duplicate SYMBOL/DATE keys")
    dates=sorted(parsed_dates.unique())
    cutoff=pd.Timestamp(cutoff)
    future=[d for d in dates if d>cutoff]
    if len(future)<horizon:
        return _empty(cutoff,symbol,target_pct,horizon,"HORIZON_NOT_MATURED",cost_pct)
    window_dates=future[:horizon]
    indexed=bars.copy()
    indexed["DATE"]=parsed_dates
    sym=indexed[indexed["SYMBOL"].astype(str).eq(str(symbol))].set_index("DATE")
    if cutoff not in sym.index:
        return _empty(cutoff,symbol,target_pct,horizon,"CUTOFF_SYMBOL_ROW_MISSING",cost_pct)
    if any(d not in sym.index for d in window_dates):
        return _empty(cutoff,symbol,target_pct,horizon,"SYMBOL_SESSION_MISSING",cost_pct)
    rows=[sym.loc[d] for d in window_dates]
    if any(isinstance(r,pd.DataFrame) for r in rows):
        return _empty(cutoff,symbol,target_pct,horizon,"DUPLICATE_SYMBOL_DATE",cost_pct)
    if any(not _valid_bar(r) for r in rows):
        return _empty(cutoff,symbol,target_pct,horizon,"INVALID_OR_NONTRADED_OHLC",cost_pct)
    entry=float(rows[0]["OPEN_PRICE"])
    if entry<=0 or not np.isfinite(entry):
        return _empty(cutoff,symbol,target_pct,horizon,"INVALID_ENTRY_PRICE",cost_pct)
    target=entry*(1+target_pct/100)
    stop=entry*(1-3.0/100)
    exit_price=None; exit_date=None; reason=None
    for d,r in zip(window_dates,rows):
        o,h,l=float(r["OPEN_PRICE"]),float(r["HIGH_PRICE"]),float(r["LOW_PRICE"])
        # Conservative gap handling: stop gap exits at open; target gap fills no worse than target limit.
        if o<=stop:
            exit_price=o; exit_date=d; reason="STOP_GAP"; break
        stop_hit=l<=stop
        target_hit=h>=target
        if stop_hit:  # stop-first if OHLC cannot reveal intraday sequence
            exit_price=stop; exit_date=d; reason="STOP_LOSS"; break
        if target_hit:
            exit_price=max(target,o) if o>=target else target
            exit_date=d; reason="TARGET"; break
    if exit_price is None:
        last=rows[-1]
        exit_price=float(last["CLOSE_PRICE"]); exit_date=window_dates[-1]; reason="HORIZON_CLOSE"
    gross=(exit_price/entry-1)*100
    net=gross-cost_pct
    return {"CUT_OFF":cutoff.date().isoformat(),"SYMBOL":str(symbol),"SIGNAL_TIMESTAMP":cutoff.isoformat(),
        "ENTRY_SESSION":window_dates[0].date().isoformat(),"ENTRY_PRICE":entry,"ENTRY_STATUS":"EXECUTED",
        "TARGET_PCT":float(target_pct),"HORIZON_SESSIONS":int(horizon),"EXIT_SESSION":exit_date.date().isoformat(),
        "EXIT_PRICE":float(exit_price),"EXIT_REASON":reason,"GROSS_RETURN_PCT":gross,"COST_PCT":float(cost_pct),
        "NET_RETURN_PCT":net,"TARGET_HIT":reason=="TARGET","STOP_HIT":reason.startswith("STOP"),
        "EXECUTABLE":True,"DATA_STATUS":"VERIFIED_OHLC","SOURCE_FILE":"","SOURCE_ROW_OR_KEY":f"{symbol}|{window_dates[0].date()}"}

def _empty(cutoff,symbol,target,horizon,status,cost):
    return {"CUT_OFF":pd.Timestamp(cutoff).date().isoformat(),"SYMBOL":str(symbol),"SIGNAL_TIMESTAMP":pd.Timestamp(cutoff).isoformat(),
        "ENTRY_SESSION":None,"ENTRY_PRICE":None,"ENTRY_STATUS":status,"TARGET_PCT":float(target),"HORIZON_SESSIONS":int(horizon),
        "EXIT_SESSION":None,"EXIT_PRICE":None,"EXIT_REASON":status,"GROSS_RETURN_PCT":None,"COST_PCT":float(cost),
        "NET_RETURN_PCT":None,"TARGET_HIT":None,"STOP_HIT":None,"EXECUTABLE":False,"DATA_STATUS":status,
        "SOURCE_FILE":"","SOURCE_ROW_OR_KEY":None}

def run(data_path, signals_path, out_dir, cost_pct=COST_PCT):
    bars=pd.read_csv(data_path)
    missing=REQUIRED-set(bars.columns)
    if missing: raise ValueError(f"OHLC input missing columns: {sorted(missing)}")
    bars["DATE"]=pd.to_datetime(bars["DATE"],errors="coerce")
    if bars["DATE"].isna().any(): raise ValueError("Invalid DATE values; refusing implicit date repair")
    if bars.duplicated(["SYMBOL","DATE"]).any(): raise ValueError("Duplicate SYMBOL/DATE keys; fail closed")
    signals=pd.read_csv(signals_path)
    if not {"CUT_OFF","SYMBOL"}.issubset(signals.columns): raise ValueError("Signals require CUT_OFF and SYMBOL")
    signals["CUT_OFF"]=pd.to_datetime(signals["CUT_OFF"],errors="coerce")
    if signals["CUT_OFF"].isna().any(): raise ValueError("Invalid signal cutoff")
    signal_keys=signals.assign(_SYMBOL=signals["SYMBOL"].astype(str))
    if signal_keys.duplicated(["CUT_OFF","_SYMBOL"]).any():
        raise ValueError("Duplicate CUT_OFF/SYMBOL signal keys; fail closed")
    rows=[]
    for s in signals[["CUT_OFF","SYMBOL"]].itertuples(index=False):
        for target,horizon in TARGETS:
            row=simulate_one(bars,s.CUT_OFF,s.SYMBOL,target,horizon,cost_pct)
            row["SOURCE_FILE"]=str(data_path)
            rows.append(row)
    trades=pd.DataFrame(rows)
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    trade_path=out/"cost_aware_trade_ledger.csv"
    trades.to_csv(trade_path,index=False)
    metrics=[]
    for (target,horizon),g in trades.groupby(["TARGET_PCT","HORIZON_SESSIONS"]):
        ex=g[g["EXECUTABLE"]]
        net=pd.to_numeric(ex["NET_RETURN_PCT"],errors="coerce").dropna()
        metrics.append({"TARGET_PCT":target,"HORIZON_SESSIONS":horizon,"SIGNALS":len(g),
            "EXECUTABLE":len(ex),"EXCLUDED":int((~g["EXECUTABLE"]).sum()),
            "EXCLUSION_REASONS":g.loc[~g["EXECUTABLE"],"DATA_STATUS"].value_counts().to_dict(),
            "GROSS_HIT_RATE":float((pd.to_numeric(ex["GROSS_RETURN_PCT"])>=target).mean()) if len(ex) else None,
            "TARGET_EXIT_RATE":float((ex["EXIT_REASON"]=="TARGET").mean()) if len(ex) else None,
            "NET_PROFITABLE_TARGET_EXIT_RATE":float(((ex["EXIT_REASON"]=="TARGET") & (pd.to_numeric(ex["NET_RETURN_PCT"])>0)).mean()) if len(ex) else None,
            "MEAN_NET_RETURN_PCT":float(net.mean()) if len(net) else None,
            "MEDIAN_NET_RETURN_PCT":float(net.median()) if len(net) else None})
    manifest={"engine":"V11.3_RESEARCH_ONLY_COST_AWARE_OHLC_REPLAY","cost_pct_points":cost_pct,
        "cost_convention":"total round-trip deduction applied once","entry":"next global trading session OPEN",
        "target":"intraday HIGH touch","stop_loss_pct":3.0,"same_bar_ambiguity":"stop first",
        "no_target_exit":"horizon final session CLOSE","slippage":"not modelled",
        "data_path":str(data_path),"signals_path":str(signals_path),
        "data_sha256":hashlib.sha256(Path(data_path).read_bytes()).hexdigest(),
        "signals_sha256":hashlib.sha256(Path(signals_path).read_bytes()).hexdigest(),
        "rows":len(trades),"metrics":metrics,"python":platform.python_version(),"pandas":pd.__version__,"numpy":np.__version__}
    mp=out/"cost_aware_backtest_metrics.json"; mp.write_text(json.dumps(manifest,indent=2,default=str))
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [trade_path,mp]}
    (out/"cost_aware_output_sha256.json").write_text(json.dumps(hashes,indent=2))
    print(json.dumps({"trade_rows":len(trades),"metrics":metrics,"output_sha256":hashes},indent=2))

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--data",default="data/processed/nse_eq_200_sessions.csv")
    ap.add_argument("--signals",default="outputs/backtest/walk_forward_predictions.csv")
    ap.add_argument("--out",default="outputs/backtest/cost_aware_v11_3")
    ap.add_argument("--cost-pct",type=float,default=COST_PCT)
    a=ap.parse_args()
    run(a.data,a.signals,a.out,a.cost_pct)
