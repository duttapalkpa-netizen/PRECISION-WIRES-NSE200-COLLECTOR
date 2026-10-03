from pathlib import Path
import pandas as pd
SRC=Path("outputs/finalists/v11_3_candidates.csv"); OUT=Path("outputs/finalists/v11_3_risk_adjusted.csv")
def main():
    df=pd.read_csv(SRC)
    for c in ["RISK_MACRO","RISK_FII_DII","RISK_GEO"]: df[c]="UNKNOWN"
    df["RISK_MODIFIER"]="NEUTRAL_DATA_UNAVAILABLE"; df["RISK_ADJUSTED_SCORE"]=df["V11_3_CORE_SCORE"]
    df.to_csv(OUT,index=False); print(f"RISK_ROWS={len(df)}; external modifiers remain UNKNOWN")
if __name__=="__main__": main()
