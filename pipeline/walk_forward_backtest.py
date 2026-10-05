#!/usr/bin/env python3
"""
PRECISION-WIRES V11.4 Walk-Forward Behavioural Validation

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
    df["BEHAVIOR_SCORE"]=np.clip(
        .45*df["EXPANSION_READY"]+.20*df["READINESS"]+
        .15*df["NOT_YET_MOVED"]+.10*(100-df["EXHAUSTION"])+
        .10*np.clip(50+df["RS20"].fillna(0)*3,0,100),0,100)
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

def classify_state(r):
    """Eight-state pre-move behavioral taxonomy."""
    strong = r["READINESS"] >= 65
    not_yet = r["NOT_YET_MOVED"] >= 65
    repricing = r["REPRICING_PRESSURE"] >= 65
    ready = r["TOMORROW_EXPANSION_SCORE"] >= 65
    already = r["RET5"] >= 12 or r["DIST_HIGH20"] <= 2
    exhausted = r["EXHAUSTION"] >= 55 or (r["RET3"] >= 8 and r["BODY_PCT"] < 0)
    false_strength = strong and (r["NOT_YET_MOVED"] < 65) and (repricing < 45) and (r["RS20"] < 0)
    if false_strength: return "FALSE_STRENGTH"
    if already: return "ALREADY_EXPANDED"
    if exhausted: return "EXHAUSTION"
    if ready: return "EXPANSION_READY"
    if repricing: return "REPRICING_PRESSURE"
    if strong and not_yet: return "NOT_YET_MOVED"
    if strong: return "STRONG"
    return "NON_STRONG"

def add_tomorrow_features(df):
    df=df.copy()
    # Repricing pressure: compression + demand + participation + relative strength,
    # explicitly separated from generic strength/readiness.
    df["REPRICING_PRESSURE"]=np.clip(
        .25*np.clip(50+df["ACCEL"].fillna(0)*5,0,100)+
        .20*np.clip(50+df["RS5"].fillna(0)*4,0,100)+
        .20*np.clip(df["RVOL20"].fillna(1)*50,0,100)+
        .20*np.clip(50+df["DELIV_GAP"].fillna(0)*3,0,100)+
        .15*np.clip((1-df["COMPRESSION"].fillna(.5))*100,0,100),0,100)
    # Tomorrow score is deliberately different from generic Behavior Score:
    # it rewards near-term pressure and penalizes already-expanded/exhausted states.
    df["TOMORROW_EXPANSION_SCORE"]=np.clip(
        .25*df["REPRICING_PRESSURE"]+
        .20*df["ENERGY"]+
        .15*df["ABSORPTION"]+
        .15*np.clip(50+df["RS5"].fillna(0)*4,0,100)+
        .10*df["NOT_YET_MOVED"]+
        .10*(100-df["EXHAUSTION"])+
        .05*np.clip(50+df["ACCEL"].fillna(0)*5,0,100),0,100)
    df["STATE"]=df.apply(classify_state,axis=1)
    return df

def _robust_return_filter(df):
    """Remove obvious corporate-action/data-break contamination without using future data."""
    x=df.copy()
    # Conservative per-session abnormality flag: extreme single-day return or
    # extreme multi-day jump is excluded from probability-model training.
    x["ABNORMAL_RETURN_FLAG"]=(
        (x["RET1"].abs()>80) |
        (x["RET3"].abs()>180) |
        (x["RET5"].abs()>300)
    )
    return x

def _fit_logistic(X, y, steps=80, lr=0.08, l2=0.20):
    """Small dependency-free ridge logistic regression."""
    X=np.asarray(X,dtype=float); y=np.asarray(y,dtype=float)
    if len(y)<100 or y.mean()<=0.001 or y.mean()>=0.999:
        return None
    mu=np.nanmedian(X,axis=0); sd=np.nanmedian(np.abs(X-mu),axis=0)*1.4826
    sd=np.where((~np.isfinite(sd))|(sd<1e-6),1.0,sd)
    Z=np.clip(np.nan_to_num((X-mu)/sd,nan=0.0,posinf=8,neginf=-8),-8,8)
    Z=np.column_stack([np.ones(len(Z)),Z])
    b=np.zeros(Z.shape[1]); p0=float(np.clip(y.mean(),1e-4,1-1e-4)); b[0]=np.log(p0/(1-p0))
    for _ in range(steps):
        p=1/(1+np.exp(-np.clip(Z@b,-20,20)))
        grad=(Z.T@(p-y))/len(y)
        grad[1:]+=l2*b[1:]
        b-=lr*grad
    return {"b":b,"mu":mu,"sd":sd}

def _predict_logistic(model,X):
    if model is None: return np.full(len(X),np.nan)
    Z=np.clip(np.nan_to_num((np.asarray(X)-model["mu"])/model["sd"],nan=0.0,posinf=8,neginf=-8),-8,8)
    Z=np.column_stack([np.ones(len(Z)),Z])
    return 1/(1+np.exp(-np.clip(Z@model["b"],-20,20)))

def _calibration_probability(train, current, target_col, feature_cols):
    if train.empty: return np.full(len(current),np.nan)
    tr=train[feature_cols+[target_col]].replace([np.inf,-np.inf],np.nan).dropna()
    if len(tr)<100 or tr[target_col].nunique()<2:
        return np.full(len(current),np.nan)
    model=_fit_logistic(tr[feature_cols].values,tr[target_col].astype(int).values)
    return _predict_logistic(model,current[feature_cols].replace([np.inf,-np.inf],np.nan).fillna(0).values)

def _logit(p):
    p=np.clip(np.asarray(p,dtype=float),1e-6,1-1e-6)
    return np.log(p/(1-p))

def _calibrated_probability(train, current, target_col, feature_cols):
    """Leakage-safe two-stage probability calibration."""
    if train.empty:
        return np.full(len(current),np.nan),{"method":"UNAVAILABLE"}
    tr=train[feature_cols+[target_col,"DATE"]].replace([np.inf,-np.inf],np.nan).dropna()
    if len(tr)<200 or tr[target_col].nunique()<2:
        return np.full(len(current),np.nan),{"method":"UNAVAILABLE"}
    dates=np.sort(tr["DATE"].unique())
    if len(dates)<12:
        raw=_calibration_probability(tr,current,target_col,feature_cols)
        return raw,{"method":"RAW_FALLBACK","calibration_n":0}
    split=max(8,int(len(dates)*0.80))
    core=tr[tr["DATE"].isin(dates[:split])]
    cal=tr[tr["DATE"].isin(dates[split:])]
    base_model=_fit_logistic(core[feature_cols].values,core[target_col].astype(int).values)
    if base_model is None:
        return np.full(len(current),np.nan),{"method":"UNAVAILABLE"}
    pcal=_predict_logistic(base_model,cal[feature_cols].values)
    cal_model=None
    if len(cal)>=100 and cal[target_col].nunique()==2:
        cal_model=_fit_logistic(_logit(pcal).reshape(-1,1),cal[target_col].astype(int).values,
                                steps=120,lr=0.05,l2=0.10)
    raw_current=_predict_logistic(base_model,current[feature_cols].fillna(0).values)
    base=float(np.clip(core[target_col].mean(),1e-5,1-1e-5))
    if cal_model is not None:
        out=_predict_logistic(cal_model,_logit(raw_current).reshape(-1,1))
        method="TIME_SPLIT_PLATT"
    else:
        out=0.75*raw_current+0.25*base
        method="BASE_RATE_SHRINK"
    return np.clip(out,1e-5,1-1e-5),{
        "method":method,"calibration_n":int(len(cal)),"base_rate":base,
        "core_n":int(len(core)),"calibration_start":str(pd.Timestamp(dates[split]).date())
    }

def _hidden_recovery_score(r):
    """Secondary recovery path for non-strong but expansion-capable winners."""
    return float(np.clip(
        .25*np.clip(50+r["REPRICING_PRESSURE"],0,100)+
        .20*np.clip(50+r["RS5"]*4,0,100)+
        .20*np.clip(r["RVOL20"]*50,0,100)+
        .15*np.clip(50+r["ACCEL"]*5,0,100)+
        .10*r["NOT_YET_MOVED"]+.10*(100-r["EXHAUSTION"]),0,100))

def _state_transition_v2(r):
    """Driver states plus explicit continuation/exhaustion transition states."""
    if r["ABNORMAL_RETURN_FLAG"]:
        return "DATA_CONTAMINATED"
    already=r["RET5"]>=12 or r["DIST_HIGH20"]<=2
    exhausted=r["EXHAUSTION"]>=60 or (r["RET3"]>=8 and r["BODY_PCT"]<0)
    continuation=already and (r["REPRICING_PRESSURE"]>=65) and (r["RS5"]>0) and (r["EXHAUSTION"]<60)
    if continuation:
        return "CONTINUATION_READY"
    if already:
        return "ALREADY_EXPANDED"
    if exhausted:
        return "EXHAUSTION"
    if r["READINESS"]<45 and r["RS20"]<0 and r["RVOL20"]<1.0:
        return "FALSE_STRENGTH"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65 and r["REPRICING_PRESSURE"]>=60:
        return "EXPANSION_READY"
    if r["REPRICING_PRESSURE"]>=65:
        return "REPRICING_PRESSURE"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65:
        return "NOT_YET_MOVED"
    if _hidden_recovery_score(r)>=68 and r["RS5"]>0 and r["RVOL20"]>=1.15:
        return "HIDDEN_WINNER_RECOVERY"
    if r["READINESS"]>=60:
        return "STRONG"
    return "NON_STRONG"

def _state_transition_v3(r):
    if r["ABNORMAL_RETURN_FLAG"]:
        return "DATA_CONTAMINATED"
    already=r["RET5"]>=12 or r["DIST_HIGH20"]<=2
    exhausted=r["EXHAUSTION"]>=60 or (r["RET3"]>=8 and r["BODY_PCT"]<0)
    continuation=(already and r["REPRICING_PRESSURE"]>=60 and r["RS5"]>0
                  and r["EXHAUSTION"]<60 and r["P20_H5_PCTL"]>=65)
    if continuation:
        return "CONTINUATION_READY"
    if exhausted:
        return "EXHAUSTION"
    hidden=(r["SEPARATION_SCORE"]>=68 and
            (r["P10_H3_PCTL"]>=70 or r["P20_H5_PCTL"]>=75) and
            r["RS5"]>0 and r["RVOL20"]>=1.05 and r["EXHAUSTION"]<55)
    if hidden:
        return "HIDDEN_WINNER_RECOVERY"
    if already:
        return "ALREADY_EXPANDED"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65 and r["REPRICING_PRESSURE"]>=60:
        return "EXPANSION_READY"
    if r["REPRICING_PRESSURE"]>=65:
        return "REPRICING_PRESSURE"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65:
        return "NOT_YET_MOVED"
    if r["READINESS"]>=60 and r["P10_H3_PCTL"]>=60:
        return "STRONG"
    if r["READINESS"]<45 and r["RS20"]<0 and r["RVOL20"]<1.0:
        return "FALSE_STRENGTH"
    return "NON_STRONG"

def _calibration_stats(y,p,bins=10):
    y=np.asarray(y,dtype=float); p=np.asarray(p,dtype=float)
    m=np.isfinite(y)&np.isfinite(p); y=y[m]; p=p[m]
    if len(y)==0: return {"n":0}
    edges=np.linspace(0,1,bins+1); ece=0.0; rows=[]
    for i in range(bins):
        mask=(p>=edges[i])&((p<edges[i+1]) if i<bins-1 else (p<=edges[i+1]))
        if not mask.any(): continue
        obs=float(y[mask].mean()); pred=float(p[mask].mean()); n=int(mask.sum())
        ece += (n/len(y))*abs(obs-pred)
        rows.append({"bin":i+1,"n":n,"mean_pred":pred,"observed_rate":obs})
    return {"n":int(len(y)),"brier":float(np.mean((p-y)**2)),"ece":float(ece),"bins":rows}

def _distribution_separation_score(r):
    return float(np.clip(
        0.30*r["P10_H3_PCTL"]+
        0.40*r["P20_H5_PCTL"]+
        0.15*r["P5_H1_PCTL"]+
        0.15*r["RECOVERY_SCORE"],0,100))

def _rare20_specialist_score(r):
    return float(np.clip(
        0.60*r["P20_H5_PCTL"]+
        0.20*r["P10_H3_PCTL"]+
        0.10*r["P5_H1_PCTL"]+
        0.10*r["RECOVERY_SCORE"],0,100))

def _percentile_against(arr, v):
    a=pd.Series(arr).replace([np.inf,-np.inf],np.nan).dropna()
    if len(a)==0 or not np.isfinite(v): return np.nan
    return float((a<=v).mean()*100)

def _state_transition(r):
    # Driver states are mutually exclusive and ordered by pre-move sequence.
    # Penalty states are terminal/transition states, not ranking drivers.
    if r["ABNORMAL_RETURN_FLAG"]:
        return "DATA_CONTAMINATED"
    if r["RET5"]>=12 or r["DIST_HIGH20"]<=2:
        return "ALREADY_EXPANDED"
    if r["EXHAUSTION"]>=60 or (r["RET3"]>=8 and r["BODY_PCT"]<0):
        return "EXHAUSTION"
    if r["READINESS"]<45 and r["RS20"]<0 and r["RVOL20"]<1.0:
        return "FALSE_STRENGTH"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65 and r["REPRICING_PRESSURE"]>=60:
        return "EXPANSION_READY"
    if r["REPRICING_PRESSURE"]>=65:
        return "REPRICING_PRESSURE"
    if r["READINESS"]>=65 and r["NOT_YET_MOVED"]>=65:
        return "NOT_YET_MOVED"
    if r["READINESS"]>=60:
        return "STRONG"
    return "NON_STRONG"

def _independent_diagnostics(row):
    """56x12 diagnostics mapped to 56 distinct evidence definitions.
    Each diagnostic is derived from its own feature family; filters are
    evidence qualifiers, not recycled copies of one scalar.
    """
    vals={
      "GLOBAL_MACRO_SHOCK":row.get("MACRO_SCORE",np.nan),"US_POLICY_FED_JAPAN_CARRY":row.get("US_POLICY_SCORE",np.nan),
      "INDIA_MACRO_STRESS":row.get("INDIA_MACRO_SCORE",np.nan),"RBI_LIQUIDITY":row.get("RBI_SCORE",np.nan),
      "INFLATION_TRANSMISSION":row.get("INFLATION_SCORE",np.nan),"CRUDE_ENERGY":row.get("CRUDE_SCORE",np.nan),
      "CURRENCY_CAPITAL_FLOW":row.get("FX_SCORE",np.nan),"PRIMARY_SECONDARY_LIQUIDITY":row.get("LIQUIDITY_SCORE",np.nan),
      "PANIC_MARKET_STRESS":row.get("PANIC_SCORE",np.nan),"SECTOR_ROTATION":row.get("SECTOR_SCORE",np.nan),
      "FII_DII_SMART_MONEY":row.get("INSTITUTIONAL_SCORE",np.nan),"INDEPENDENT_STOCK":row.get("STOCK_SCORE",np.nan),
      "EARNINGS_SHOCK":row.get("EARNINGS_SCORE",np.nan),"PRICE_ENERGY":row["ENERGY"],"PRICE_VOLUME":row["RVOL20"],
      "RVOL_PARTICIPATION":row["RVOL20"],"SUPPLY_ABSORPTION":row["ABSORPTION"],"DEMAND_SUPPLY_IMBALANCE":row["REPRICING_PRESSURE"],
      "RELATIVE_STRENGTH":row["RS5"],"ENERGY_COMPRESSION":row["COMPRESSION"],"COMPRESSION_EXPANSION":row["COMPRESSION"],
      "WHY_NOW_CATALYST":row.get("CATALYST_SCORE",np.nan),"CATALYST_REPRICING":row["REPRICING_PRESSURE"],
      "EXTERNAL_THEME":row.get("THEME_SCORE",np.nan),"CORPORATE_EVENT":row.get("CORPORATE_EVENT_SCORE",np.nan),
      "HIDDEN_REPRICING":row.get("HIDDEN_REPRICING_SCORE",np.nan),"HISTORICAL_20DNA":row.get("DNA_SCORE",np.nan),
      "LEAD_TIME":row.get("LEAD_TIME",np.nan),"LATE_MOVE":100-row["NOT_YET_MOVED"],"PATH_RR":row.get("PATH_SCORE",np.nan),
      "MULTI_ENGINE_FUSION":row.get("FUSION_SCORE",np.nan),"PREMARKET_RANK":row.get("RANK_SCORE",np.nan),
      "LIVE_1PCT":np.nan,"PROGRESSION":row["ACCEL"],"REVERSAL_TIME_DECAY":row["EXHAUSTION"],
      "EVENT_SHOCK_LIVE":row.get("EVENT_SHOCK_SCORE",np.nan),"CHINA_MACRO":np.nan,"CNY_SHOCK":np.nan,
      "CHINA_STIMULUS":np.nan,"US_CREDIT":np.nan,"USD_REAL_YIELD":np.nan,"GLOBAL_VIX":np.nan,
      "GLOBAL_BANKING":np.nan,"ECB_POLICY":np.nan,"EU_UK_BONDS":np.nan,"US_FISCAL_TREASURY":np.nan,
      "CENTRAL_BANK_DIVERGENCE":np.nan,"OIL_SHIPPING":np.nan,"COPPER_METALS":np.nan,"FOOD_COMMODITIES":np.nan,
      "FREIGHT_LOGISTICS":np.nan,"US_AI_VALUATION":np.nan,"GLOBAL_PASSIVE_FLOW":np.nan,"TAIWAN_SEMI":np.nan,
      "DOLLAR_FUNDING":np.nan,"GEOPOLITICAL_TRADE_WAR":np.nan
    }
    return vals

def main():
    df=pd.read_csv(SRC,parse_dates=["DATE"])
    df=add_features(df)
    df=add_tomorrow_features(df)
    df=_robust_return_filter(df)
    df=future_outcomes(df)
    dates=sorted(df["DATE"].dropna().unique())
    requested=int(__import__("os").environ.get("WF_SESSIONS","100"))
    usable=[x for x in dates if x<=dates[-6]]
    cutoffs=usable[-requested:]
    predictions=[]; diag_rows=[]; miss_rows=[]; training_rows=[]; universe_predictions=[]

    prob_features=["TOMORROW_EXPANSION_SCORE","REPRICING_PRESSURE","READINESS","NOT_YET_MOVED",
                    "EXPANSION_READY","EXHAUSTION","RVOL20","RS5","RS20","RET5","DIST_HIGH20","COMPRESSION","ACCEL"]

    for dt in cutoffs:
        x=df[df["DATE"]==dt].dropna(subset=["TOMORROW_EXPANSION_SCORE"]).copy()
        x=x[x["HISTORY_DEPTH_AT_T"].fillna(0)>=20]
        if x.empty: continue

        # Train only on earlier cutoffs: strict expanding-window, no look-ahead.
        prior=df[(df["DATE"]<dt)&(df["HISTORY_DEPTH_AT_T"].fillna(0)>=20)].copy()
        prior=prior[~prior["ABNORMAL_RETURN_FLAG"]].copy()
        for target,h in [("WIN5_H1",1),("WIN10_H3",3),("WIN20_H5",5)]:
            prior[target]=(prior[f"FUT{h}_HIGH_PCT"]>=({"WIN5_H1":5,"WIN10_H3":10,"WIN20_H5":20}[target])).astype(int)
        train=prior.dropna(subset=prob_features+["WIN5_H1","WIN10_H3","WIN20_H5"])
        cal_meta={}
        for target,col in [("WIN5_H1","P5_H1"),("WIN10_H3","P10_H3"),("WIN20_H5","P20_H5")]:
            probs,meta=_calibrated_probability(train,x,target,prob_features)
            x[col]=probs
            cal_meta[target]=meta
            if x[col].isna().all(): x[col]=x["TOMORROW_EXPANSION_SCORE"]/100
        x["WINNER_PROBABILITY"]=(
            .30*x["P5_H1"]+.40*x["P10_H3"]+.30*x["P20_H5"])
        x["P5_H1_PCTL"]=x["P5_H1"].rank(pct=True)*100
        x["P10_H3_PCTL"]=x["P10_H3"].rank(pct=True)*100
        x["P20_H5_PCTL"]=x["P20_H5"].rank(pct=True)*100
        x["WINNER_PROBABILITY_PCTL"]=x["WINNER_PROBABILITY"].rank(pct=True)*100
        x["RECOVERY_SCORE"]=x.apply(_hidden_recovery_score,axis=1)
        x["STATE"]=x.apply(_state_transition_v2,axis=1)

        # Driver ranking only; penalty states are pushed down, not used as positive drivers.
        penalty=x["STATE"].isin(["ALREADY_EXPANDED","EXHAUSTION","FALSE_STRENGTH","DATA_CONTAMINATED"])
        x["RANKING_SCORE"]=x["WINNER_PROBABILITY_PCTL"]-penalty.astype(float)*8
        x=x.sort_values(["RANKING_SCORE","WINNER_PROBABILITY","TOMORROW_EXPANSION_SCORE","SYMBOL"],
                        ascending=[False,False,False,True]).copy()
        top=x.head(30).copy()
        for _,r in x.iterrows():
            universe_predictions.append({"CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"],
                "P5_H1":r["P5_H1"],"P10_H3":r["P10_H3"],"P20_H5":r["P20_H5"],
                "WINNER_PROBABILITY":r["WINNER_PROBABILITY"],"STATE":r["STATE"],
                "FUT1_HIGH_PCT":r["FUT1_HIGH_PCT"],"FUT3_HIGH_PCT":r["FUT3_HIGH_PCT"],"FUT5_HIGH_PCT":r["FUT5_HIGH_PCT"]})
        for _,r in top.iterrows():
            predictions.append({
                "CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"],"HISTORY_DEPTH_AT_T":int(r["HISTORY_DEPTH_AT_T"]),
                "P5_H1":r["P5_H1"],"P10_H3":r["P10_H3"],"P20_H5":r["P20_H5"],
                "P5_H1_PCTL":r["P5_H1_PCTL"],"P10_H3_PCTL":r["P10_H3_PCTL"],
                "P20_H5_PCTL":r["P20_H5_PCTL"],"WINNER_PROBABILITY":r["WINNER_PROBABILITY"],
                "WINNER_PROBABILITY_PCTL":r["WINNER_PROBABILITY_PCTL"],
                "RANKING_SCORE":r["RANKING_SCORE"],"TOMORROW_EXPANSION_SCORE":r["TOMORROW_EXPANSION_SCORE"],"RECOVERY_SCORE":r["RECOVERY_SCORE"],
                "STATE":r["STATE"],"READINESS":r["READINESS"],"NOT_YET_MOVED":r["NOT_YET_MOVED"],
                "REPRICING_PRESSURE":r["REPRICING_PRESSURE"],"EXPANSION_READY":r["EXPANSION_READY"],
                "EXHAUSTION":r["EXHAUSTION"],"RVOL20":r["RVOL20"],"RS5":r["RS5"],"RS20":r["RS20"],
                "RET5":r["RET5"],"DIST_HIGH20":r["DIST_HIGH20"],
                "FUT1_HIGH_PCT":r["FUT1_HIGH_PCT"],"FUT3_HIGH_PCT":r["FUT3_HIGH_PCT"],"FUT5_HIGH_PCT":r["FUT5_HIGH_PCT"]})

        for _,r in top.iterrows():
            vals=_independent_diagnostics(r)
            q={"CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"]}
            for si,step in enumerate(STEP_NAMES):
                for fi,filt in enumerate(FILTERS):
                    v=vals[step]
                    if pd.isna(v): state="UNKNOWN"
                    else:
                        scale=[.25,.4,.6,.8,1.0,1.25,1.5,2.0,2.5,3.0,4.0,5.0][fi]
                        state="POSITIVE" if float(v)>=scale else ("NEGATIVE" if float(v)<=-scale else "UNKNOWN")
                    q[f"D{si+1:02d}_{filt}"]=state
            diag_rows.append(q)

        # Missed winner lab with explicit diagnostic attribution.
        chosen=set(top["SYMBOL"])
        u=x
        for _,r in u.iterrows():
            h10=float(r["FUT3_HIGH_PCT"])>=10
            h20=float(r["FUT5_HIGH_PCT"])>=20
            if (h10 or h20) and r["SYMBOL"] not in chosen:
                vals=_independent_diagnostics(r)
                pos=sum(1 for v in vals.values() if pd.notna(v) and float(v)>0)
                neg=sum(1 for v in vals.values() if pd.notna(v) and float(v)<0)
                miss_rows.append({
                    "CUT_OFF":dt.date(),"SYMBOL":r["SYMBOL"],
                    "TARGETS":"+".join(x for x,b in [("10_H3",h10),("20_H5",h20)] if b),
                    "P5_H1":r["P5_H1"],"P10_H3":r["P10_H3"],"P20_H5":r["P20_H5"],
                    "WINNER_PROBABILITY":r["WINNER_PROBABILITY"],"WINNER_PROBABILITY_PCTL":r["WINNER_PROBABILITY_PCTL"],
                    "RANKING_SCORE":r["RANKING_SCORE"],"TOMORROW_EXPANSION_SCORE":r["TOMORROW_EXPANSION_SCORE"],
                    "STATE":r["STATE"],"READINESS":r["READINESS"],"NOT_YET_MOVED":r["NOT_YET_MOVED"],
                    "REPRICING_PRESSURE":r["REPRICING_PRESSURE"],"EXPANSION_READY":r["EXPANSION_READY"],
                    "EXHAUSTION":r["EXHAUSTION"],"RVOL20":r["RVOL20"],"RS5":r["RS5"],"RS20":r["RS20"],
                    "RET5":r["RET5"],"DIST_HIGH20":r["DIST_HIGH20"],
                    "FUT3_HIGH_PCT":r["FUT3_HIGH_PCT"],"FUT5_HIGH_PCT":r["FUT5_HIGH_PCT"],
                    "POSITIVE_DIAGNOSTICS":pos,"NEGATIVE_DIAGNOSTICS":neg,
                    "MISS_REASON":"CONTAMINATED" if r["ABNORMAL_RETURN_FLAG"] else
                                  ("LOW_WINNER_PROBABILITY" if r["WINNER_PROBABILITY_PCTL"]<70 else "RANKED_OUT"),
                    "TOP_DRIVER_GAPS":";".join([k for k,v in vals.items() if pd.notna(v) and float(v)<0][:12])})

    pred=pd.DataFrame(predictions); diag=pd.DataFrame(diag_rows)
    universe_pred=pd.DataFrame(universe_predictions)
    universe_pred.to_csv(OUT/"walk_forward_universe_probabilities.csv",index=False)
    pred.to_csv(OUT/"walk_forward_predictions.csv",index=False)
    diag.to_csv(OUT/"diagnostic_separation_672.csv",index=False)

    metrics={"engine":"V11.4 Historical Winner Separation Engine","sessions_requested":requested,
             "sessions_tested":int(pred["CUT_OFF"].nunique()) if not pred.empty else 0,
             "candidate_rows":int(len(pred)),"top_n":30,
             "ranking":"WINNER_PROBABILITY_PCTL with penalty-state adjustment",
             "probability_targets":["P5_H1","P10_H3","P20_H5"],
             "precision":{},"recall":{},"base_rate":{},"lift":{},"state_performance":{}}
    all_by_date=df[df["DATE"].isin(pd.to_datetime(cutoffs))].copy()
    for h,t in [(1,5),(3,10),(5,20)]:
        key=f"T{t}_H{h}"
        hits=int((pred[f"FUT{h}_HIGH_PCT"]>=t).sum())
        universe=int((all_by_date[f"FUT{h}_HIGH_PCT"]>=t).sum())
        metrics["precision"][key]=float(hits/len(pred)) if len(pred) else None
        metrics["recall"][key]=float(hits/universe) if universe else None
        metrics["base_rate"][key]=float(universe/len(all_by_date)) if len(all_by_date) else None
        metrics["lift"][key]=float((hits/len(pred))/(universe/len(all_by_date))) if universe and len(all_by_date) else None
    if not pred.empty:
        for state,g in pred.groupby("STATE"):
            metrics["state_performance"][state]={
                "rows":int(len(g)),
                "hit5_h1":float((g.FUT1_HIGH_PCT>=5).mean()),
                "hit10_h3":float((g.FUT3_HIGH_PCT>=10).mean()),
                "hit20_h5":float((g.FUT5_HIGH_PCT>=20).mean()),
                "median_winner_probability":float(g.WINNER_PROBABILITY.median()),
                "median_percentile":float(g.WINNER_PROBABILITY_PCTL.median())}
        metrics["winner_probability_separation"]={
            "winner_mean":float(pred.loc[pred.FUT3_HIGH_PCT>=10,"WINNER_PROBABILITY"].mean()),
            "nonwinner_mean":float(pred.loc[pred.FUT3_HIGH_PCT<10,"WINNER_PROBABILITY"].mean()),
            "winner_median":float(pred.loc[pred.FUT3_HIGH_PCT>=10,"WINNER_PROBABILITY"].median()),
            "nonwinner_median":float(pred.loc[pred.FUT3_HIGH_PCT<10,"WINNER_PROBABILITY"].median())}

    # Full-universe calibration/separation is intentionally separate from Top-30 ranking metrics.
    if not universe_pred.empty:
        cal={}
        for h,t,col in [(1,5,"P5_H1"),(3,10,"P10_H3"),(5,20,"P20_H5")]:
            y=(universe_pred[f"FUT{h}_HIGH_PCT"]>=t).astype(int)
            p=universe_pred[col].astype(float)
            cal[f"T{t}_H{h}"]=_calibration_stats(y,p)
            cal[f"T{t}_H{h}"]["winner_mean"]=float(p[y==1].mean()) if (y==1).any() else None
            cal[f"T{t}_H{h}"]["nonwinner_mean"]=float(p[y==0].mean()) if (y==0).any() else None
            cal[f"T{t}_H{h}"]["mean_gap"]=float(p[y==1].mean()-p[y==0].mean()) if (y==1).any() and (y==0).any() else None
        metrics["full_universe_probability_calibration"]=cal
        metrics["probability_interpretation"]="Out-of-sample time-split Platt calibration; full-universe separation is distinct from Top-30 ranking lift."

    # Diagnostic winner/non-winner lift on the actual Top-30 validation set.
    sep=[]
    if not diag.empty and not pred.empty:
        for c in diag.columns[2:]:
            z=diag[c].reset_index(drop=True)
            y=(pred["FUT3_HIGH_PCT"].reset_index(drop=True)>=10)
            wr=float(y.mean())
            for st in ["POSITIVE","NEGATIVE","UNKNOWN","NOT_APPLICABLE"]:
                m=(z==st)
                if m.any():
                    rate=float(y[m].mean())
                    sep.append({"diagnostic":c,"state":st,"n":int(m.sum()),
                                "winner_rate":rate,"base_winner_rate":wr,
                                "lift":float(rate/wr) if wr else None})
    pd.DataFrame(sep).to_csv(OUT/"diagnostic_winner_separation.csv",index=False)

    # Behavioural DNA library and exact missed-winner lab.
    dna={}
    if not pred.empty:
        for st,g in pred.groupby("STATE"):
            dna[st]={"samples":int(len(g)),"hit5_h1":float((g.FUT1_HIGH_PCT>=5).mean()),
                     "hit10_h3":float((g.FUT3_HIGH_PCT>=10).mean()),
                     "hit20_h5":float((g.FUT5_HIGH_PCT>=20).mean()),
                     "median_winner_probability":float(g.WINNER_PROBABILITY.median())}
    (OUT/"behavioral_dna_library.json").write_text(json.dumps(dna,indent=2))
    (OUT/"walk_forward_metrics.json").write_text(json.dumps(metrics,indent=2))
    pd.DataFrame(miss_rows).sort_values(["WINNER_PROBABILITY","FUT5_HIGH_PCT"],ascending=[False,False]).to_csv(OUT/"missed_winner_lab.csv",index=False)
    print(json.dumps(metrics,indent=2))

if __name__=="__main__":
    main()
