#!/usr/bin/env python3
"""Research-only rolling audit for the user's two portfolio holdings.

This does not change the production selector, ranking score, pressure fade,
CORE-672 diagnostics, or engines. It measures descriptive setup/outcome rates
on NSE daily OHLCV + deliverable history with strictly forward labels.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import pandas as pd

SRC=Path("data/processed/nse_eq_200_sessions.csv")
MASTER=Path("data/reference/security_master.csv")
OUT=Path("outputs/portfolio")
OUT.mkdir(parents=True, exist_ok=True)
HOLDINGS={
    "HINDCOPPER":{"isin":"INE531E01026","name":"Hindustan Copper Limited"},
    "EPACKPEB":{"isin":"INE0MLS01022","name":"EPack Prefab Technologies Limited"},
}
TARGETS=(2,3,5)
HORIZONS=(1,3,5)

def sha256(p:Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def main():
    if not SRC.exists() or not MASTER.exists():
        raise SystemExit("BLOCKED: normalized 200-session data or NSE security master missing")
    d=pd.read_csv(SRC,dtype={"SYMBOL":str,"ISIN":str})
    d.columns=[str(c).strip().upper() for c in d.columns]
    required={"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY","DELIV_QTY","DELIV_PER"}
    missing=sorted(required-set(d.columns))
    if missing: raise SystemExit(f"BLOCKED: missing normalized columns {missing}")
    m=pd.read_csv(MASTER,dtype=str)
    m.columns=[str(c).strip().upper() for c in m.columns]
    for sym,meta in HOLDINGS.items():
        row=m[m.SYMBOL.astype(str).str.upper().eq(sym)]
        if len(row)!=1 or str(row.iloc[0].get("ISIN","")).upper()!=meta["isin"]:
            raise SystemExit(f"BLOCKED: NSE Security Master identity mismatch for {sym}")
    d["SYMBOL"]=d.SYMBOL.astype(str).str.upper().str.strip()
    d["DATE"]=pd.to_datetime(d.DATE,errors="coerce")
    # Restrict the join to the two explicitly requested holdings first. The
    # normalized market-wide file also contains non-EQ/non-master symbols;
    # requiring an ISIN for every market row would create false failures.
    d=d[d.SYMBOL.isin(HOLDINGS)].copy()
    master_ids=m[["SYMBOL","ISIN"]].copy()
    master_ids["SYMBOL"]=master_ids.SYMBOL.astype(str).str.upper().str.strip()
    master_ids["ISIN"]=master_ids.ISIN.astype(str).str.upper().str.strip()
    if master_ids["SYMBOL"].duplicated().any():
        raise SystemExit("BLOCKED: duplicate SYMBOL rows in NSE Security Master")
    if "ISIN" in d.columns:
        source_isin=d["ISIN"].astype(str).str.upper().str.strip()
        check=d[["SYMBOL"]].copy()
        check["SOURCE_ISIN"]=source_isin
        check=check.merge(master_ids,on="SYMBOL",how="left",validate="many_to_one")
        mismatch=check.SOURCE_ISIN.ne("") & check.SOURCE_ISIN.ne(check.ISIN)
        if mismatch.any(): raise SystemExit("BLOCKED: daily source ISIN conflicts with NSE Security Master")
        d=d.drop(columns=["ISIN"])
    d=d.merge(master_ids,on="SYMBOL",how="left",validate="many_to_one")
    for sym,meta in HOLDINGS.items():
        rows=d[d.SYMBOL.eq(sym)]
        if rows.empty or rows.ISIN.isna().any() or not rows.ISIN.astype(str).str.upper().eq(meta["isin"]).all():
            raise SystemExit(f"BLOCKED: {sym} daily rows do not resolve to the expected NSE Security Master ISIN")
    for c in ["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY","DELIV_QTY","DELIV_PER"]:
        d[c]=pd.to_numeric(d[c],errors="coerce")
    d=d[d.SYMBOL.isin(HOLDINGS)].dropna(subset=["DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"])
    d=d.sort_values(["SYMBOL","DATE"]).drop_duplicates(["SYMBOL","DATE"],keep="last")
    if d.duplicated(["SYMBOL","DATE"]).any(): raise SystemExit("BLOCKED: duplicate symbol/session rows remain")
    if (d[["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY"]].dropna() <= 0).any().any(): raise SystemExit("BLOCKED: non-positive OHLCV value")
    if (d.HIGH_PRICE < d.LOW_PRICE).any(): raise SystemExit("BLOCKED: high below low")
    summaries=[]; daily=[]
    for sym,meta in HOLDINGS.items():
        x=d[d.SYMBOL.eq(sym)].copy().sort_values("DATE").reset_index(drop=True)
        n=len(x)
        if n<200:
            raise SystemExit(f"BLOCKED: {sym} has only {n} valid sessions; 200 required")
        c=x.CLOSE_PRICE; h=x.HIGH_PRICE; l=x.LOW_PRICE; v=x.TTL_TRD_QNTY
        x["EMA20"]=c.ewm(span=20,adjust=False,min_periods=20).mean()
        x["EMA50"]=c.ewm(span=50,adjust=False,min_periods=50).mean()
        x["VOL20"]=v.rolling(20,min_periods=20).mean()
        x["RVOL20"]=v/x.VOL20
        x["HIGH20"]=h.rolling(20,min_periods=20).max()
        x["DIST_HIGH20_PCT"]=(x.HIGH20-c)/c*100
        x["RET5_PCT"]=c.pct_change(5)*100
        x["RET20_PCT"]=c.pct_change(20)*100
        x["DELIV20"]=x.DELIV_PER.rolling(20,min_periods=20).mean()
        x["DELIV_GAP_PP"]=x.DELIV_PER-x.DELIV20
        x["TREND_OK"]=(c>x.EMA20)&(x.EMA20>x.EMA50)
        x["PARTICIPATION_OK"]=x.RVOL20>=1.2
        x["DELIVERY_OK"]=x.DELIV_GAP_PP>=0
        x["NOT_EXTENDED"]=(x.DIST_HIGH20_PCT<=7)&(x.RET5_PCT<8)
        x["SETUP_EVIDENCE_COMPLETE"]=x[["EMA20","EMA50","RVOL20","DELIV_GAP_PP","DIST_HIGH20_PCT","RET5_PCT"]].notna().all(axis=1)
        setup_condition=x.TREND_OK&x.PARTICIPATION_OK&x.DELIVERY_OK&x.NOT_EXTENDED
        x["RESEARCH_SETUP_2_5"]=pd.Series(pd.NA,index=x.index,dtype="boolean")
        x.loc[x.SETUP_EVIDENCE_COMPLETE,"RESEARCH_SETUP_2_5"]=setup_condition[x.SETUP_EVIDENCE_COMPLETE].astype(bool)
        # Future windows start at T+1. Incomplete tails are intentionally excluded.
        for k in HORIZONS:
            # Explicit forward windows T+1..T+k; min_count=k excludes incomplete tails.
            future_high=pd.concat([h.shift(-i) for i in range(1,k+1)],axis=1).max(axis=1,min_count=k)
            future_close=pd.concat([c.shift(-i) for i in range(1,k+1)],axis=1).max(axis=1,min_count=k)
            future_low=pd.concat([l.shift(-i) for i in range(1,k+1)],axis=1).min(axis=1,min_count=k)
            x[f"FUT{k}_HIGH_PCT"]=(future_high/c-1)*100
            x[f"FUT{k}_CLOSE_PCT"]=(future_close/c-1)*100
            x[f"FUT{k}_LOW_PCT"]=(future_low/c-1)*100
        matured=x.dropna(subset=[f"FUT{k}_HIGH_PCT" for k in HORIZONS]).copy()
        for cohort_name,cohort in [("ALL_CUTOFFS",matured),("RESEARCH_SETUP_2_5",matured[matured.RESEARCH_SETUP_2_5.fillna(False)])]:
            for k in HORIZONS:
                for t in TARGETS:
                    vals=cohort[f"FUT{k}_HIGH_PCT"]
                    closevals=cohort[f"FUT{k}_CLOSE_PCT"]
                    summaries.append({
                        "symbol":sym,"cohort":cohort_name,"horizon_sessions":k,"target_pct":t,
                        "cutoffs":int(len(cohort)),
                        "high_touch_hits":int((vals>=t).sum()),
                        "high_touch_rate_pct":round(float((vals>=t).mean()*100),3) if len(cohort) else None,
                        "close_confirmation_hits":int((closevals>=t).sum()),
                        "close_confirmation_rate_pct":round(float((closevals>=t).mean()*100),3) if len(cohort) else None,
                        "median_max_adverse_excursion_pct":round(float(cohort[f"FUT{k}_LOW_PCT"].median()),3) if len(cohort) else None,
                    })
        latest=x.iloc[-1]
        daily.append({
            "symbol":sym,"company":meta["name"],"isin":meta["isin"],
            "latest_session":latest.DATE.strftime("%Y-%m-%d"),
            "open":float(latest.OPEN_PRICE),"high":float(latest.HIGH_PRICE),
            "low":float(latest.LOW_PRICE),"close":float(latest.CLOSE_PRICE),
            "daily_change_pct":round(float((latest.CLOSE_PRICE/x.iloc[-2].CLOSE_PRICE-1)*100),3),
            "history_sessions":n,"ema20":round(float(latest.EMA20),3),
            "ema50":round(float(latest.EMA50),3),"rvol20":round(float(latest.RVOL20),3) if pd.notna(latest.RVOL20) else None,
            "delivery_pct":float(latest.DELIV_PER) if pd.notna(latest.DELIV_PER) else None,
            "delivery_gap_pp":round(float(latest.DELIV_GAP_PP),3) if pd.notna(latest.DELIV_GAP_PP) else None,
            "ret5_pct":round(float(latest.RET5_PCT),3),"ret20_pct":round(float(latest.RET20_PCT),3),
            "distance_from_20d_high_pct":round(float(latest.DIST_HIGH20_PCT),3),
            "trend_ok":bool(latest.TREND_OK),"participation_ok":bool(latest.PARTICIPATION_OK),
            "delivery_ok":bool(latest.DELIVERY_OK) if pd.notna(latest.DELIV_GAP_PP) else None,
            "not_extended":bool(latest.NOT_EXTENDED) if pd.notna(latest.DIST_HIGH20_PCT) and pd.notna(latest.RET5_PCT) else None,
            "research_setup_2_5":(bool(latest.RESEARCH_SETUP_2_5) if pd.notna(latest.RESEARCH_SETUP_2_5) else "UNKNOWN"),
            "latest_forward_outcomes":"NOT_MATURED; excluded from backtest hit-rate denominator",
        })
    pd.DataFrame(summaries).to_csv(OUT/"portfolio_rolling_metrics.csv",index=False)
    pd.DataFrame(daily).to_csv(OUT/"portfolio_daily_status.csv",index=False)
    report={
        "status":"PASS_RESEARCH_ONLY",
        "source_file":str(SRC),"source_sha256":sha256(SRC),
        "security_master_sha256":sha256(MASTER),
        "symbols":list(HOLDINGS),"history_sessions":{r["symbol"]:r["history_sessions"] for r in daily},
        "latest_session":max(r["latest_session"] for r in daily),
        "targets_pct":list(TARGETS),"horizons_sessions":list(HORIZONS),
        "setup_definition":"EMA20>EMA50 and close>EMA20; RVOL20>=1.2; delivery percentage >= its 20-session mean; within 7% of 20-session high and 5-session return <8%.",
        "outcome_definition":"T+1..T+H maximum high touch and maximum close confirmation; incomplete forward windows excluded; adverse excursion from minimum low.",
        "guardrails":["research-only overlay; not production selector","no portfolio quantity/cost basis used","no look-ahead in setup features","latest session is not included in matured outcome metrics","all 200-session minimum enforced separately for each symbol"],
    }
    (OUT/"portfolio_rolling_report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"report":report,"daily_status":daily,"metric_rows":len(summaries)},indent=2))

if __name__=="__main__": main()
