from pathlib import Path
import json
import pandas as pd

RAW=Path("data/raw"); PROC=Path("data/processed"); QA=Path("data/qa")

def _coverage(series, total):
    present = int(series.notna().sum())
    missing = int(total - present)
    pct = (100.0 * present / total) if total else 0.0
    return present, missing, pct

def main():
    QA.mkdir(parents=True,exist_ok=True); issues=[]; warnings=[]
    files=list(RAW.glob("sec_bhavdata_full_*.csv"))
    sessions=len([x for x in (RAW/"sessions.txt").read_text().splitlines() if x.strip()]) if (RAW/"sessions.txt").exists() else 0
    f=PROC/"nse_eq_200_sessions.csv"; dates=symbols=0
    total_rows=0
    delivery_qty_present=delivery_qty_missing=0
    delivery_pct_present=delivery_pct_missing=0
    delivery_qty_coverage=delivery_pct_coverage=0.0
    delivery_ready=False
    delivery_row_complete=False
    if not f.exists():
        issues.append("processed dataset missing")
    else:
        df=pd.read_csv(f)
        total_rows=int(len(df))
        req={"SYMBOL","DATE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","TTL_TRD_QNTY","DELIV_QTY","DELIV_PER"}
        miss=req-set(df.columns)
        if miss: issues.append("missing columns: "+",".join(sorted(miss)))
        if df.empty: issues.append("dataset empty")
        if {"SYMBOL","DATE"}.issubset(df.columns) and df.duplicated(["SYMBOL","DATE"]).any():
            issues.append("duplicate SYMBOL+DATE")
        price_cols=["OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE"]
        if set(price_cols).issubset(df.columns) and df[price_cols].le(0).any().any():
            issues.append("non-positive OHLC")
        if {"HIGH_PRICE","LOW_PRICE"}.issubset(df.columns) and (df["HIGH_PRICE"] < df["LOW_PRICE"]).any():
            issues.append("HIGH < LOW")
        if "DELIV_QTY" in df:
            delivery_qty_present,delivery_qty_missing,delivery_qty_coverage=_coverage(df["DELIV_QTY"],total_rows)
            if (df["DELIV_QTY"].dropna() < 0).any(): issues.append("negative delivery")
        if "DELIV_PER" in df:
            delivery_pct_present,delivery_pct_missing,delivery_pct_coverage=_coverage(df["DELIV_PER"],total_rows)
            dp=df["DELIV_PER"].dropna()
            if ((dp<0)|(dp>100)).any(): issues.append("DELIV_PER outside 0..100")
        delivery_ready=bool(delivery_qty_coverage>=95 and delivery_pct_coverage>=95)
        delivery_row_complete=bool(total_rows>0 and delivery_qty_missing==0 and delivery_pct_missing==0)
        if delivery_qty_missing or delivery_pct_missing:
            warnings.append("delivery fields contain missing values; aggregate >=95% readiness does not mean every row is complete")
        dates=df["DATE"].nunique() if "DATE" in df else 0
        symbols=df["SYMBOL"].nunique() if "SYMBOL" in df else 0
    result={"status":"PASS" if sessions>=200 and not issues else "FAIL",
            "raw_files":len(files),"sessions":sessions,"processed_dates":dates,"symbols":symbols,
            "rows":total_rows,
            "delivery_qty_present_rows":delivery_qty_present,
            "delivery_qty_missing_rows":delivery_qty_missing,
            "delivery_qty_coverage_pct":delivery_qty_coverage,
            "delivery_pct_present_rows":delivery_pct_present,
            "delivery_pct_missing_rows":delivery_pct_missing,
            "delivery_pct_coverage_pct":delivery_pct_coverage,
            "delivery_row_complete":delivery_row_complete,
            "delivery_ready_for_final_selection":delivery_ready if f.exists() else False,
            "final_selection_data_ready":bool(f.exists() and delivery_ready),
            "warnings":warnings,"issues":issues}
    (QA/"qa_report.json").write_text(json.dumps(result,indent=2,default=str)); print(json.dumps(result,indent=2))
    if result["status"]!="PASS": raise SystemExit(1)

if __name__=="__main__": main()
