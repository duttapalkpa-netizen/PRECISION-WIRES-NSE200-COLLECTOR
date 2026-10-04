from pathlib import Path
import numpy as np, pandas as pd\nimport json\nfrom pipeline.walk_forward_backtest import add_features

SRC=Path("data/processed/nse_eq_200_sessions.csv")
OUT=Path("outputs/finalists")

def pct(a,b):
    return (a/b-1)*100 if pd.notna(a) and pd.notna(b) and b else np.nan

def analysis_mode(n):
    if n >= 200: return "FULL V11.3"
    if n >= 100: return "EXTENDED V11.3"
    if n >= 50: return "DEVELOPING V11.3"
    if n >= 20: return "EARLY V11.3"
    if n >= 5: return "EARLY EXPANSION ENGINE"
    if n >= 1: return "IPO-PLX V2.0"
    return "DATA UNAVAILABLE"

def data_confidence(n):
    if n >= 200: return "HIGH"
    if n >= 100: return "MEDIUM-HIGH"
    if n >= 50: return "MEDIUM"
    if n >= 20: return "DEVELOPING"
    if n >= 5: return "EARLY"
    if n >= 1: return "IPO-EARLY"
    return "NONE"

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(SRC,parse_dates=["DATE"]).sort_values(["SYMBOL","DATE"])
    rows=[]

    for sym,g in df.groupby("SYMBOL",sort=False):
        g=g.dropna(subset=["CLOSE_PRICE"]).copy()
        n=len(g)
        if n < 1:
            continue

        mode=analysis_mode(n)
        confidence=data_confidence(n)
        c=g["CLOSE_PRICE"]
        v=g["TTL_TRD_QNTY"].fillna(0)
        ema20=c.ewm(span=20,adjust=False).mean().iloc[-1]
        ema50=c.ewm(span=50,adjust=False).mean().iloc[-1]
        baseline=v.iloc[:-1].tail(min(20,max(n-1,1))).mean()
        rvol=v.iloc[-1]/max(baseline,1e-9)
        ret_window=min(20,n-1)
        ret20=pct(c.iloc[-1],c.iloc[-1-ret_window]) if ret_window else np.nan
        delivery=g["DELIV_PER"].tail(min(20,n)).mean()

        energy=float(np.clip(50+(0 if pd.isna(ret20) else ret20)*2,0,100))
        lead=float(np.clip(50+(rvol-1)*15+(c.iloc[-1]/ema20-1)*500,0,100))

        # Adaptive diagnostics: short histories are analysed, not rejected.
        A=energy>=60 and lead>=60
        B=rvol>=1.5 and (pd.isna(ret20) or ret20>=2)
        C=c.iloc[-1]>=ema20 and (n<50 or c.iloc[-1]>=ema50)
        D=c.iloc[-1]>=ema20 and c.iloc[-1]/max(c.tail(min(20,n)).min(),1e-9)-1>=.05
        E=not(A and B and C) and (energy>=55 or lead>=55)

        base_score=.25*energy+.20*lead+.20*min(rvol*25,100)+.15*(100 if C else 0)+.10*(100 if D else 0)+.10*(100 if E else 0)
        if sym in latest.index:
            br=latest.loc[sym]
            behavior_score=float(br["BEHAVIOR_SCORE"]) if "BEHAVIOR_SCORE" in br else float(br["READINESS"])
            behavior_state=str(br["STATE"])
            hist_rate=float(calib.get(behavior_state,{}).get("hit10_h3",0)) if calib else 0.0
            calibration_score=float(np.clip(50+50*(hist_rate/max_rate if max_rate>0 else 0),0,100))
        else:
            behavior_score=50.0; behavior_state="UNKNOWN"; hist_rate=0.0; calibration_score=50.0
        score=.50*base_score+.35*behavior_score+.15*calibration_score

        rows.append({
            "SYMBOL":sym,
            "DATE":g["DATE"].iloc[-1].date(),
            "CLOSE":c.iloc[-1],
            "EMA20":ema20,
            "EMA50":ema50,
            "RVOL20":rvol,
            "RET20_PCT":ret20,
            "DELIV20_AVG":delivery,
            "ENERGY":energy,
            "LEAD_TIME":lead,
            "A":A,"B":B,"C":C,"D":D,"E":E,
            "V11_3_CORE_SCORE":score,
            "SCORE":score,
            "HISTORY_DEPTH":n,
            "ANALYSIS_MODE":mode,
            "DATA_CONFIDENCE":confidence,
            "LISTING_DATE":g["LISTING_DATE"].iloc[0] if "LISTING_DATE" in g else g["DATE"].iloc[0],
            "LISTING_DATE_SOURCE":g["LISTING_DATE_SOURCE"].iloc[0] if "LISTING_DATE_SOURCE" in g else "FIRST_OBSERVED_SESSION_PROXY",
            "PIPELINE_FLOW":"NSE Historical Backbone -> Security Listing-Age Detection -> Adaptive History Engine -> A/B/C/D/E -> Risk Modifier -> Live 1% -> Finalist",
            "DATA_NOTE":"Technical-core implementation only. Catalyst, macro/FII-DII/research-house/live-1% remain unavailable and are not fabricated."
        })

    out=pd.DataFrame(rows).sort_values("SCORE",ascending=False)
    out.to_csv(OUT/"v11_3_candidates.csv",index=False)
    out.head(30).to_csv(OUT/"v11_3_top30.csv",index=False)
    print(out.head(10).to_string(index=False))

if __name__=="__main__":
    main()
