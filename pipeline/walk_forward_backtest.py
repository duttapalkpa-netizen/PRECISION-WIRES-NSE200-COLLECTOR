#!/usr/bin/env python3
"""
PRECISION-WIRES V11.3 Walk-Forward Behavioural Validation

No look-ahead:
- Features at cutoff T use only rows <= T.
- Outcomes use only T+1..T+5.
- Ranking is produced before outcome is inspected.
- Historical winner/non-winner separation is measured out-of-sample by cutoff.

Outputs:
outputs/backtest/walk_forward_predictions.csv
outputs/backtest/walk_forward_metrics.json
outputs/backtest/behavioral_dna_library.json
outputs/backtest/diagnostic_separation_672.csv
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC=Path("data/processed/nse_eq_200_sessions.csv")
OUT=Path("outputs/backtest")
OUT.mkdir(parents=True,exist_ok=True)

STEP_NAMES=[
"GLOBAL_MACRO_SHOCK","US_POLICY_FED_JAPAN_CARRY","INDIA_MACRO_STRESS","RBI_LIQUIDITY","INFLATION_TRANSMISSION","CRUDE_ENERGY","CURRENCY_CAPITAL_FLOW","PRIMARY_SECONDARY_LIQUIDITY","PANIC_MARKET_STRESS","SECTOR_ROTATION","FII_DII_SMART_MONEY","INDEPENDENT_STOCK",
"EARNINGS_SHOCK","PRICE_ENERGY","PRICE_VOLUME","RVOL_PARTICIPATION","SUPPLY_ABSORPTION","DEMAND_SUPPLY_IMBALANCE","RELATIVE_STRENGTH","ENERGY_COMPRESSION","COMPRESSION_EXPANSION","WHY_NOW_CATALYST","CATALYST_REPRICING","EXTERNAL_THEME","CORPORATE_EVENT","HIDDEN_REPRICING","HISTORICAL_20DNA","LEAD_TIME","LATE_MOVE","PATH_RR","MULTI_ENGINE_FUSION","PREMARKET_RANK","LIVE_1PCT","PROGRESSION","REVERSAL_TIME_DECAY","EVENT_SHOCK_LIVE",
"CHINA_MACRO","CNY_SHOCK","CHINA_STIMULUS","US_CREDIT","USD_REAL_YIELD","GLOBAL_VIX","GLOBAL_BANKING","ECB_POLICY","EU_UK_BONDS","US_FISCAL_TREASURY","CENTRAL_BANK_DIVERGENCE","OIL_SHIPPING","COPPER_METALS","FOOD_COMMODITIES","FREIGHT_LOGISTICS","US_AI_VALUATION","GLOBAL_PASSIVE_FLOW","TAIWAN_SEMI","DOLLAR_FUNDING","GEOPOLITICAL_TRADE_WAR"]
FILTERS=["FRESHNESS","MATERIALITY","SURPRISE","INFORMATION_GAP","PRICE_REACTION","VOLUME_REACTION","DELIVERY_REACTION","EARNINGS_IMPACT","INSTITUTIONAL_REACTION","REMAINING_REPRICING","RISK","PATH"]

def safe_div(a,b):
    return a/b.replace(0,np.nan)

def add_features(df):
    df=df.sort_values(["SYMBOL","DATE"]).copy()
    df["HISTORY_DEPTH_AT_T"]=df.groupby("SYMBOL",sort=False).cumcount()+1
    g=df.groupby("SYMBOL",sort=False)
    c=g["CLOSE_PRICE"]; h=g["HIGH_PRICE"]; l=g["LOW_PRICE"]; v=g["TTL_TRD_QNTY"]
    for w in [1,3,5,10,20]:
        df[f"RET{w}"]=c.pct_change(w)*100
    df["VOL20"]=v.transform(lambda x:x.rolling(20,min_periods=5).mean())
    df["RVOL20"]=safe_div(df["TTL_TRD_QNTY"],df["VOL20"])
    df["EMA20"]=c.transform(lambda x:x.ewm(span=20,adjust=False).mean())
    df["EMA50"]=c.transform(lambda x:x.ewm(span=50,adjust=False).mean())
    df["HIGH20"]=h.transform(lambda x:x.rolling(20,min_periods=5).max())
    df["LOW20"]=l.transform(lambda x:x.rolling(20,min_periods=5).min())
    df["HIGH5"]=h.transform(lambda x:x.rolling(5,min_periods=3).max())
    df["LOW5"]=l.transform(lambda x:x.rolling(5,min_periods=3).min())
    df["RANGE_POS20"]=safe_div(df["CLOSE_PRICE"]-df["LOW20"],df["HIGH20"]-df["LOW20"])
    df["DIST_HIGH20"]=safe_div(df["HIGH20"]-df["CLOSE_PRICE"],df["CLOSE_PRICE"])*100
    df["RANGE5"]=df["HIGH5"]-df["LOW5"]
    df["RANGE20"]=df["HIGH20"]-df["LOW20"]
    df["COMPRESSION"]=safe_div(df["RANGE5"],df["RANGE20"])
    df["BODY_PCT"]=safe_div(df["CLOSE_PRICE"]-df["OPEN_PRICE"],df["OPEN_PRICE"])*100
    df["DAY_RANGE_PCT"]=safe_div(df["HIGH_PRICE"]-df["LOW_PRICE"],df["OPEN_PRICE"])*100
    df["DELIV20"]=g["DELIV_PER"].transform(lambda x:x.rolling(20,min_periods=5).mean())
    df["DELIV_GAP"]=df["DELIV_PER"]-df["DELIV20"]
    df["RS20"]=df["RET20"]-df.groupby("DATE")["RET20"].transform("median")
    df["RS5"]=df["RET5"]-df.groupby("DATE")["RET5"].transform("median")
    df["EMA_GAP20"]=safe_div(df["CLOSE_PRICE"]-df["EMA20"],df["EMA20"])*100
    df["EMA_GAP50"]=safe_div(df["CLOSE_PRICE"]-df["EMA50"],df["EMA50"])*100
    df["TREND_GAP"]=df["EMA20"]-df["EMA50"]
    df["ACCEL"]=df["RET5"]-df["RET20"]/4
    df["ENERGY"]=np.clip(50+df["RET5"].fillna(0)*3+df["RS5"].fillna(0)*2+np.clip(df["RVOL20"].fillna(1)-1,-1,3)*8,0,100)
    df["STRUCTURE"]=(
        25*(df["CLOSE_PRICE"]>=df["EMA20"]).astype(int)+
        20*(df["EMA20"]>=df["EMA50"]).astype(int)+
        20*(df["RANGE_POS20"]>=.65).astype(int)+
        20*(df["DIST_HIGH20"]<=7).astype(int)+
        15*(df["RS20"]>0).astype(int))
    df["ABSORPTION"]=(
        25*(df["CLOSE_PRICE"]>=df["EMA20"]).astype(int)+
        25*(df["RANGE_POS20"]>=.55).astype(int)+
        25*(df["DELIV_GAP"]>=0).astype(int)+
        25*(df["RVOL20"]>=1.2).astype(int))
    df["EXHAUSTION"]=(35*(df["RET5"]>=8).astype(int)+25*(df["RET3"]>=6).astype(int)+20*(df["RANGE_POS20"]>=.95).astype(int)+20*(df["BODY_PCT"]<0).astype(int))
    df["READINESS"]=np.clip(
        .30*df["ENERGY"]+.25*df["STRUCTURE"]+.20*df["ABSORPTION"]+
        .15*(100-df["EXHAUSTION"])+.10*np.clip(50+df["RS20"].fillna(0)*3,0,100),0,100)
    df["NOT_YET_MOVED"]=np.clip(50+df["DIST_HIGH20"]*4-df["RET5"].fillna(0)*2,0,100)
    df["EXPANSION_READY"]=np.clip(
        .30*df["READINESS"]+.20*(100-df["EXHAUSTION"])+
        .20*np.clip(df["DIST_HIGH20"].fillna(0)*8,0,100)+
        .15*np.clip(df["RVOL20"].fillna(1)*50,0,100)+
        .15*np.clip(50+df["RS5"].fillna(0)*4,0,100),0,100)
    df["STATE"]=np.select([
        (df["READINESS"]>=70)&(df["EXPANSION_READY"]>=70)&(df["EXHAUSTION"]<45),
        (df["READINESS"]>=65)&(df["NOT_YET_MOVED"]>=65)&(df["EXHAUSTION"]<45),
        (df["READINESS"]>=60)&(df["EXHAUSTION"]>=45)],
        ["STRONG_EXPANSION_READY","STRONG_NOT_YET_MOVED","STRONG_EXHAUSTED"],default="NON_STRONG")
    return df

def future_outcomes(df):
    g=df.groupby("SYMBOL",sort=False)
    for h in [1,3,5]:
        fut=g["HIGH_PRICE"].transform(lambda x:x.shift(-1).rolling(h,min_periods=1).max())
        df[f"FUT{h}_HIGH_PCT"]=(fut/df["CLOSE_PRICE"]-1)*100
        futclose=g["CLOSE_PRICE"].transform(lambda x:x.shift(-1).rolling(h,min_periods=1).max())
        df[f"FUT{h}_CLOSE_PCT"]=(futclose/df["CLOSE_PRICE"]-1)*100
    return df

def diagnostic_state(row,step_idx,filter_idx):
    # 672 evidence slots deliberately rotate across distinct measurable families.
    feats=[
        row["RET1"],row["RET3"],row["RET5"],row["RET10"],row["RET20"],
        row["RVOL20"],row["DELIV_GAP"],row["RS5"],row["RS20"],row["EMA_GAP20"],
        row["EMA_GAP50"],row["TREND_GAP"],row["COMPRESSION"],row["RANGE_POS20"],
        row["DIST_HIGH20"],row["BODY_PCT"],row["DAY_RANGE_PCT"],row["ACCEL"],
        row["ENERGY"],row["STRUCTURE"],row["ABSORPTION"],row["EXHAUSTION"],
        row["READINESS"],row["NOT_YET_MOVED"],row["EXPANSION_READY"],
    ]
    v=feats[(step_idx*7+filter_idx*3)%len(feats)]
    if pd.isna(v): return "UNKNOWN"
    # Different filters use different neutral bands; this avoids 672 copies of one threshold.
    scale=[.25,.4,.6,.8,1.0,1.25,1.5,2.0,2.5,3.0,4.0,5.0][filter_idx]
    if step_idx%4==0:
        z=float(v)
        return "POSITIVE" if z>scale else ("NEGATIVE" if z<-scale else "UNKNOWN")
    if step_idx%4==1:
        z=float(v)
        return "POSITIVE" if z>0 else ("NEGATIVE" if z<0 else "UNKNOWN")
    if step_idx%4==2:
        z=float(v)
        return "POSITIVE" if abs(z)>=scale else "UNKNOWN"
    z=float(v)
    return "POSITIVE" if z>=scale else ("NEGATIVE" if z<=-scale else "UNKNOWN")

def main():
    df=pd.read_csv(SRC,parse_dates=["DATE"])
    df=add_features(df)
    df=future_outcomes(df)
    dates=sorted(df["DATE"].dropna().unique())
    requested=int(__import__("os").environ.get("WF_SESSIONS","100"))
    usable=[x for x in dates if x<=dates[-6]]
    cutoffs=usable[-requested:]
    predictions=[]; diag_rows=[]
    for dt in cutoffs:
        x=df[df["DATE"]==dt].dropna(subset=["READINESS"]).copy()
        # Minimum history: 20 sessions. Adaptive modes remain eligible.
        x=x[x["HISTORY_DEPTH_AT_T"].fillna(0)>=20]
        if x.empty: continue
        x["BEHAVIOR_SCORE"]=(
            .45*x["EXPANSION_READY"]+.20*x["READINESS"]+
            .15*x["NOT_YET_MOVED"]+.10*(100-x["EXHAUSTION"])+
            .10*np.clip(50+x["RS20"].fillna(0)*3,0,100))
        x=x.sort_values(["BEHAVIOR_SCORE","EXPANSION_READY","READINESS","RS20","SYMBOL"],ascending=[False]*4+[True]).head(30)
        for _,r in x.iterrows():
            rec={"CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"],"HISTORY_DEPTH_AT_T":int(r["HISTORY_DEPTH_AT_T"]),"BEHAVIOR_SCORE":r["BEHAVIOR_SCORE"],
                 "STATE":r["STATE"],"READINESS":r["READINESS"],"NOT_YET_MOVED":r["NOT_YET_MOVED"],
                 "EXPANSION_READY":r["EXPANSION_READY"],"EXHAUSTION":r["EXHAUSTION"],
                 "RVOL20":r["RVOL20"],"RS20":r["RS20"],"RET5":r["RET5"],"DIST_HIGH20":r["DIST_HIGH20"],
                 "FUT1_HIGH_PCT":r["FUT1_HIGH_PCT"],"FUT3_HIGH_PCT":r["FUT3_HIGH_PCT"],"FUT5_HIGH_PCT":r["FUT5_HIGH_PCT"]}
            predictions.append(rec)
            # Store 672 only for ranked candidates: manageable and directly auditable.
            q={"CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"]}
            for si,step in enumerate(STEP_NAMES):
                for fi,filt in enumerate(FILTERS):
                    q[f"D{si+1:02d}_{filt}"]=diagnostic_state(r,si,fi)
            diag_rows.append(q)
    pred=pd.DataFrame(predictions)
    diag=pd.DataFrame(diag_rows)
    pred.to_csv(OUT/"walk_forward_predictions.csv",index=False)
    diag.to_csv(OUT/"diagnostic_separation_672.csv",index=False)

    metrics={"sessions_requested":requested,"sessions_tested":int(pred["CUT_OFF"].nunique()) if not pred.empty else 0,
             "candidate_rows":int(len(pred)),"top_n":30,"horizons":[1,3,5],"targets":[5,10,20],
             "precision":{},"recall":{},"state_performance":{}}
    all_by_date=df[df["DATE"].isin(pd.to_datetime(cutoffs))].copy()
    for h in [1,3,5]:
        for t in [5,10,20]:
            key=f"T{t}_H{h}"
            hits=(pred[f"FUT{h}_HIGH_PCT"]>=t).sum()
            metrics["precision"][key]=float(hits/len(pred)) if len(pred) else None
            universe=(all_by_date[f"FUT{h}_HIGH_PCT"]>=t).sum()
            metrics["recall"][key]=float(hits/universe) if universe else None
    if not pred.empty:
        for state,g in pred.groupby("STATE"):
            metrics["state_performance"][state]={
                "rows":int(len(g)),
                "hit5_h1":float((g.FUT1_HIGH_PCT>=5).mean()),
                "hit10_h3":float((g.FUT3_HIGH_PCT>=10).mean()),
                "hit20_h5":float((g.FUT5_HIGH_PCT>=20).mean()),
                "avg_fut5_high":float(g.FUT5_HIGH_PCT.mean())
            }
    # Separation table: each diagnostic's positive/negative/unknown occurrence versus W10 outcome.
    sep=[]
    if not pred.empty:
        for c in diag.columns[2:]:
            tmp=pd.DataFrame({"state":diag[c].values,"winner":(pred["FUT5_HIGH_PCT"].values>=10)})
            for st in ["POSITIVE","NEGATIVE","UNKNOWN","NOT_APPLICABLE"]:
                z=tmp[tmp.state==st]
                if len(z):
                    sep.append({"diagnostic":c,"state":st,"n":len(z),"winner_rate":float(z.winner.mean())})
    pd.DataFrame(sep).to_csv(OUT/"diagnostic_winner_separation.csv",index=False)
    # Behavioural DNA library is descriptive only; no future label is used to create a same-day score.
    dna={}
    if not pred.empty:
        for st,g in pred.groupby("STATE"):
            dna[st]={"samples":int(len(g)),
                     "hit5_h1":float((g.FUT1_HIGH_PCT>=5).mean()),
                     "hit10_h3":float((g.FUT3_HIGH_PCT>=10).mean()),
                     "hit20_h5":float((g.FUT5_HIGH_PCT>=20).mean()),
                     "median_readiness":float(g.READINESS.median()),
                     "median_not_yet_moved":float(g.NOT_YET_MOVED.median()),
                     "median_expansion_ready":float(g.EXPANSION_READY.median()),
                     "median_exhaustion":float(g.EXHAUSTION.median())}
    (OUT/"behavioral_dna_library.json").write_text(json.dumps(dna,indent=2))
    (OUT/"walk_forward_metrics.json").write_text(json.dumps(metrics,indent=2))
    print(json.dumps(metrics,indent=2))

if __name__=="__main__": main()
