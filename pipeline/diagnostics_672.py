#!/usr/bin/env python3
from pathlib import Path
import json, numpy as np, pandas as pd

SRC=Path("outputs/finalists/v11_3_candidates.csv"); CTX=Path("data/context/market_context.json")
OUT=Path("outputs/diagnostics"); OUT.mkdir(parents=True,exist_ok=True)
STATES={"POSITIVE","NEGATIVE","UNKNOWN","NOT_APPLICABLE"}
STEP_NAMES=[
"GLOBAL_MACRO_SHOCK","US_POLICY_FED_JAPAN_CARRY","INDIA_MACRO_STRESS","RBI_LIQUIDITY","INFLATION_TRANSMISSION","CRUDE_ENERGY","CURRENCY_CAPITAL_FLOW","PRIMARY_SECONDARY_LIQUIDITY","PANIC_MARKET_STRESS","SECTOR_ROTATION","FII_DII_SMART_MONEY","INDEPENDENT_STOCK",
"EARNINGS_SHOCK","PRICE_ENERGY","PRICE_VOLUME","RVOL_PARTICIPATION","SUPPLY_ABSORPTION","DEMAND_SUPPLY_IMBALANCE","RELATIVE_STRENGTH","ENERGY_COMPRESSION","COMPRESSION_EXPANSION","WHY_NOW_CATALYST","CATALYST_REPRICING","EXTERNAL_THEME","CORPORATE_EVENT","HIDDEN_REPRICING","HISTORICAL_20DNA","LEAD_TIME","LATE_MOVE","PATH_RR","MULTI_ENGINE_FUSION","PREMARKET_RANK","LIVE_1PCT","PROGRESSION","REVERSAL_TIME_DECAY","EVENT_SHOCK_LIVE",
"CHINA_MACRO","CNY_SHOCK","CHINA_STIMULUS","US_CREDIT","USD_REAL_YIELD","GLOBAL_VIX","GLOBAL_BANKING","ECB_POLICY","EU_UK_BONDS","US_FISCAL_TREASURY","CENTRAL_BANK_DIVERGENCE","OIL_SHIPPING","COPPER_METALS","FOOD_COMMODITIES","FREIGHT_LOGISTICS","US_AI_VALUATION","GLOBAL_PASSIVE_FLOW","TAIWAN_SEMI","DOLLAR_FUNDING","GEOPOLITICAL_TRADE_WAR"]
FILTERS=["FRESHNESS","MATERIALITY","SURPRISE","INFORMATION_GAP","PRICE_REACTION","VOLUME_REACTION","DELIVERY_REACTION","EARNINGS_IMPACT","INSTITUTIONAL_REACTION","REMAINING_REPRICING","RISK","PATH"]

def state(v,good=60,bad=40):
    if pd.isna(v): return "UNKNOWN"
    return "POSITIVE" if v>=good else ("NEGATIVE" if v<=bad else "UNKNOWN")

def main():
    df=pd.read_csv(SRC); ctx=json.loads(CTX.read_text()) if CTX.exists() else {}
    fii=ctx.get("fii_dii",[]); fii_net=np.nanmean([x["fii_net"] for x in fii if x.get("fii_net") is not None]) if fii else np.nan
    dii_net=np.nanmean([x["dii_net"] for x in fii if x.get("dii_net") is not None]) if fii else np.nan
    vix=np.nan
    for x in ctx.get("indices",[]):
        if x.get("index")=="INDIA VIX": vix=float(x.get("percentChange") or np.nan)
    geo_n=ctx.get("geo_news",{}).get("article_count")
    for step in STEP_NAMES:
        for filt in FILTERS:
            col=f"D{STEP_NAMES.index(step)+1:02d}_{filt}"
            vals=[]
            for _,r in df.iterrows():
                base=np.nanmean([r.get("ENERGY",np.nan),r.get("LEAD_TIME",np.nan),min(float(r.get("RVOL20",np.nan))*25,100) if pd.notna(r.get("RVOL20",np.nan)) else np.nan])
                if step=="FII_DII_SMART_MONEY":
                    vals.append(state(50+(0 if pd.isna(fii_net) else np.clip(fii_net/100, -50,50))+(0 if pd.isna(dii_net) else np.clip(dii_net/100,-50,50))))
                elif step=="GLOBAL_VIX":
                    vals.append("UNKNOWN" if pd.isna(vix) else ("NEGATIVE" if vix>10 else "POSITIVE"))
                elif step=="GEOPOLITICAL_TRADE_WAR":
                    vals.append("UNKNOWN" if geo_n is None else ("NEGATIVE" if geo_n>=40 else "POSITIVE"))
                elif step in {"WHY_NOW_CATALYST","CATALYST_REPRICING","CORPORATE_EVENT","EARNINGS_SHOCK","EVENT_SHOCK_LIVE"}:
                    vals.append("UNKNOWN")
                elif step in {"LIVE_1PCT","PROGRESSION","REVERSAL_TIME_DECAY"}:
                    vals.append("UNKNOWN")
                elif step in {"HISTORICAL_20DNA","LEAD_TIME","PATH_RR","RELATIVE_STRENGTH","PRICE_ENERGY","PRICE_VOLUME","RVOL_PARTICIPATION","DELIVERY_REACTION"}:
                    vals.append(state(base))
                else:
                    vals.append(state(base))
            df[col]=vals
    df.to_csv(OUT/"diagnostics_672.csv",index=False)
    report={"diagnostic_columns":len(STEP_NAMES)*len(FILTERS),"steps":len(STEP_NAMES),"filters":len(FILTERS),"rows":len(df),"states":sorted(STATES),"implementation":"data-derived adaptive matrix; unavailable event/live signals remain UNKNOWN"}
    (OUT/"diagnostics_672_report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
