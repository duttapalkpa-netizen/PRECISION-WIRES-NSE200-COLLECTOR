from pathlib import Path
import json, pandas as pd, numpy as np

SRC=Path("outputs/finalists/v11_3_candidates.csv")
OUT=Path("outputs/finalists/v11_3_risk_adjusted.csv")
CTX=Path("data/context/market_context.json")
REQUIRED=["SYMBOL","SCORE","HISTORY_DEPTH","ANALYSIS_MODE","DATA_CONFIDENCE"]

def num(v):
    try:return float(v)
    except:return np.nan

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(SRC)
    for c in REQUIRED:
        if c not in df:
            if c=="SCORE" and "V11_3_CORE_SCORE" in df: df[c]=df["V11_3_CORE_SCORE"]
            elif c=="HISTORY_DEPTH": df[c]=0
            elif c=="ANALYSIS_MODE": df[c]="DATA UNAVAILABLE"
            else: df[c]="NONE"
    ctx=json.loads(CTX.read_text()) if CTX.exists() else {}
    flows=ctx.get("fii_dii",[])
    fii=[num(x.get("net_value")) for x in flows if x.get("group")=="FII_FPI" and x.get("net_value") is not None]
    dii=[num(x.get("net_value")) for x in flows if x.get("group")=="DII" and x.get("net_value") is not None]
    fii20=float(np.nansum(fii[:20])) if len(fii)>=1 else np.nan
    dii20=float(np.nansum(dii[:20])) if len(dii)>=1 else np.nan
    geo_n=ctx.get("geo_news",{}).get("article_count")
    indices=ctx.get("indices",[])
    vixchg=np.nan
    for x in indices:
        if x.get("index")=="INDIA VIX": vixchg=num(x.get("percentChange"))
    macro_state="UNKNOWN"
    if indices:
        n=[num(x.get("percentChange")) for x in indices if x.get("index")=="NIFTY 50"]
        if n and not pd.isna(n[0]): macro_state="POSITIVE" if n[0]>0 else "NEGATIVE"
    fii_state="UNKNOWN" if pd.isna(fii20) else ("POSITIVE" if fii20>0 else "NEGATIVE")
    dii_state="UNKNOWN" if pd.isna(dii20) else ("POSITIVE" if dii20>0 else "NEGATIVE")
    geo_state="UNKNOWN" if geo_n is None else ("NEGATIVE" if geo_n>=40 else "POSITIVE")
    df["RISK_MACRO"]=macro_state
    df["RISK_FII_DII"]="UNKNOWN" if (fii_state=="UNKNOWN" or dii_state=="UNKNOWN") else (fii_state+"|"+dii_state)
    df["RISK_GEO"]=geo_state
    # Risk is a modifier, never a hard reject. Keep stock weakness separate from market weakness.
    adj=[]
    for _,r in df.iterrows():
        score=num(r["SCORE"]); mod=0.0
        if macro_state=="NEGATIVE": mod-=2.0
        if fii_state=="NEGATIVE": mod-=0.5
        if dii_state=="NEGATIVE": mod-=0.5
        if geo_state=="NEGATIVE": mod-=1.0
        adj.append(score+mod)
    df["RISK_MODIFIER"]=(df["RISK_MACRO"]+"|"+df["RISK_FII_DII"]+"|"+df["RISK_GEO"])
    df["RISK_ADJUSTED_SCORE"]=adj
    df["FII_20D_NET_CRORE"]=fii20; df["DII_20D_NET_CRORE"]=dii20
    df["GEO_NEWS_ARTICLES"]=geo_n
    df["MACRO_SOURCE"]="NSE indices"
    df["FII_DII_SOURCE"]="NSE fiidiiTradeReact category-normalized"
    df["GEO_SOURCE"]=str(ctx.get("sources",{}).get("geo_news","UNKNOWN"))
    cols=REQUIRED+[c for c in df.columns if c not in REQUIRED]
    df[cols].to_csv(OUT,index=False)
    print(f"RISK_ROWS={len(df)}; macro={macro_state}; fii_dii={fii_state}; geo={geo_state}")

if __name__=="__main__": main()
