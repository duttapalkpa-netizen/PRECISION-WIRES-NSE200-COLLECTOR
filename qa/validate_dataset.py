from pathlib import Path
import json, pandas as pd

RAW=Path("data/raw"); PROC=Path("data/processed"); QA=Path("data/qa")

def main():
    QA.mkdir(parents=True,exist_ok=True); issues=[]
    files=list(RAW.glob("sec_bhavdata_full_*.csv"))
    sessions=len([x for x in (RAW/"sessions.txt").read_text().splitlines() if x.strip()]) if (RAW/"sessions.txt").exists() else 0
    f=PROC/"nse_eq_200_sessions.csv"; dates=symbols=0
    if not f.exists(): issues.append("processed dataset missing")
    else:
        df=pd.read_csv(f)
        req={"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY","DELIV_QTY","DELIV_PER"}
        miss=req-set(df.columns)
        if miss: issues.append("missing columns: "+",".join(sorted(miss)))
        if df.empty: issues.append("dataset empty")
        if df.duplicated(["SYMBOL","DATE"]).any(): issues.append("duplicate SYMBOL+DATE")
        if (df[["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE"]].le(0).any().any()): issues.append("non-positive OHLC")
        if (df["HIGH_PRICE"] < df["LOW_PRICE"]).any(): issues.append("HIGH < LOW")
        if (df["DELIV_QTY"] < 0).any(): issues.append("negative delivery")
        dp=df["DELIV_PER"].dropna()
        if ((dp<0)|(dp>100)).any(): issues.append("DELIV_PER outside 0..100")
        dates=df["DATE"].nunique(); symbols=df["SYMBOL"].nunique()
    result={"status":"PASS" if sessions>=200 and not issues else "FAIL","raw_files":len(files),"sessions":sessions,"processed_dates":dates,"symbols":symbols,"issues":issues}
    (QA/"qa_report.json").write_text(json.dumps(result,indent=2,default=str)); print(json.dumps(result,indent=2))
    if result["status"]!="PASS": raise SystemExit(1)

if __name__=="__main__": main()
