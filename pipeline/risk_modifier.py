from pathlib import Path
import pandas as pd

SRC=Path("outputs/finalists/v11_3_candidates.csv")
OUT=Path("outputs/finalists/v11_3_risk_adjusted.csv")
REQUIRED=["SYMBOL","SCORE","HISTORY_DEPTH","ANALYSIS_MODE","DATA_CONFIDENCE"]

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(SRC)
    for c in REQUIRED:
        if c not in df.columns:
            if c=="SCORE" and "V11_3_CORE_SCORE" in df.columns:
                df["SCORE"]=df["V11_3_CORE_SCORE"]
            elif c=="HISTORY_DEPTH":
                df[c]=0
            elif c=="ANALYSIS_MODE":
                df[c]="DATA UNAVAILABLE"
            else:
                df[c]="NONE"
    for c in ["RISK_MACRO","RISK_FII_DII","RISK_GEO"]:
        df[c]="UNKNOWN"
    df["RISK_MODIFIER"]="NEUTRAL_DATA_UNAVAILABLE"
    df["RISK_ADJUSTED_SCORE"]=df["SCORE"]
    cols=REQUIRED+[c for c in df.columns if c not in REQUIRED]
    df=df[cols]
    df.to_csv(OUT,index=False)
    print(f"RISK_ROWS={len(df)}; preserved schema={REQUIRED}")

if __name__=="__main__":
    main()
