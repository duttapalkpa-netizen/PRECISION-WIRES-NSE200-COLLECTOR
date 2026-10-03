from pathlib import Path
import numpy as np, pandas as pd

SRC=Path("data/processed/nse_eq_200_sessions.csv"); OUT=Path("outputs/finalists")
def pct(a,b): return (a/b-1)*100 if pd.notna(a) and pd.notna(b) and b else np.nan

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(SRC,parse_dates=["DATE"]).sort_values(["SYMBOL","DATE"]); rows=[]
    for sym,g in df.groupby("SYMBOL",sort=False):
        g=g.dropna(subset=["CLOSE_PRICE"]).copy()
        if len(g)<50: continue
        c=g.CLOSE_PRICE; v=g.TTL_TRD_QNTY.fillna(0)
        ema20=c.ewm(span=20,adjust=False).mean().iloc[-1]; ema50=c.ewm(span=50,adjust=False).mean().iloc[-1]
        rvol=v.iloc[-1]/max(v.tail(20).iloc[:-1].mean(),1e-9); ret20=pct(c.iloc[-1],c.iloc[-21])
        delivery=g.DELIV_PER.tail(20).mean()
        energy=float(np.clip(50+ret20*2,0,100))
        lead=float(np.clip(50+(rvol-1)*15+(c.iloc[-1]/ema20-1)*500,0,100))
        A=energy>=60 and lead>=60; B=rvol>=1.5 and ret20>=2; C=rvol>=1.5 and c.iloc[-1]>=ema20 and c.iloc[-1]>=ema50
        D=c.iloc[-1]>=ema20 and c.iloc[-1]/c.tail(20).min()-1>=.05; E=not(A and B and C) and (energy>=55 or lead>=55)
        score=.25*energy+.20*lead+.20*min(rvol*25,100)+.15*(100 if C else 0)+.10*(100 if D else 0)+.10*(100 if E else 0)
        rows.append({"SYMBOL":sym,"DATE":g.DATE.iloc[-1].date(),"CLOSE":c.iloc[-1],"EMA20":ema20,"EMA50":ema50,"RVOL20":rvol,"RET20_PCT":ret20,"DELIV20_AVG":delivery,"ENERGY":energy,"LEAD_TIME":lead,"A":A,"B":B,"C":C,"D":D,"E":E,"V11_3_CORE_SCORE":score,"DATA_NOTE":"Technical core only; catalyst/macro/FII-DII/research-house/live-1% unavailable"})
    out=pd.DataFrame(rows).sort_values("V11_3_CORE_SCORE",ascending=False)
    out.to_csv(OUT/"v11_3_candidates.csv",index=False); out.head(30).to_csv(OUT/"v11_3_top30.csv",index=False)
    print(out.head(10).to_string(index=False))

if __name__=="__main__": main()
