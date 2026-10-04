#!/usr/bin/env python3
"""Deterministic provisional 30/10/3 ranking with strict final-readiness gates."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(".")
SRC=Path("outputs/finalists/v11_3_risk_adjusted.csv")
OUT=Path("outputs/finalists")

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if not SRC.exists():
        raise SystemExit(f"Missing input: {SRC}")
    df=pd.read_csv(SRC)
    if df.empty:
        raise SystemExit("No V11.3 candidates")
    for col in ["RISK_ADJUSTED_SCORE","ENERGY","LEAD_TIME","RVOL20","DELIV20_AVG"]:
        if col not in df: df[col]=pd.NA
    # Tie-breaks are explicit and data-derived; never random or row-order based.
    df=df.sort_values(
        ["RISK_ADJUSTED_SCORE","ENERGY","LEAD_TIME","RVOL20","DELIV20_AVG","SYMBOL"],
        ascending=[False,False,False,False,False,True],na_position="last"
    ).reset_index(drop=True)
    df["SELECTION_RANK"]=range(1,len(df)+1)
    df["SELECTION_TIER"]="OUTSIDE_TOP30"
    df.loc[df.SELECTION_RANK<=30,"SELECTION_TIER"]="PROVISIONAL_TOP30"
    df.loc[df.SELECTION_RANK<=10,"SELECTION_TIER"]="PROVISIONAL_TOP10"
    df.loc[df.SELECTION_RANK<=3,"SELECTION_TIER"]="PROVISIONAL_TOP3"

    qa_path=Path("data/qa/qa_report.json")
    qa=json.loads(qa_path.read_text()) if qa_path.exists() else {}
    blockers=[]
    if not qa.get("delivery_ready_for_final_selection",False):
        blockers.append("DELIVERY_COVERAGE_BELOW_95_PERCENT_OR_MISSING")
    for col in ["RISK_MACRO","RISK_FII_DII","RISK_GEO"]:
        if col not in df or df[col].astype(str).str.upper().eq("UNKNOWN").all():
            blockers.append(f"{col}_NOT_AVAILABLE")
    diag=Path("outputs/diagnostics/diagnostics_672.csv")
    if not diag.exists():
        blockers.append("672_DIAGNOSTIC_ENGINE_OUTPUT_MISSING")
    live=Path("data/live/intraday_1m.csv")
    if not live.exists():
        blockers.append("LIVE_INTRADAY_1M_FEED_MISSING")
    else:
        try:
            ld=pd.read_csv(live)
            required={"SYMBOL","TIMESTAMP","CLOSE","DAY_VWAP","DAY_RVOL","ORB_HIGH_15"}
            if not required.issubset({str(c).upper() for c in ld.columns}):
                blockers.append("LIVE_INTRADAY_SCHEMA_INCOMPLETE")
            if len(ld)==0:
                blockers.append("LIVE_INTRADAY_NO_ROWS")
            status_path=Path("data/live/live_1m_status.json")
            if status_path.exists():
                ls=json.loads(status_path.read_text())
                if ls.get("status")!="LIVE_1M_CAPTURED":
                    blockers.append("LIVE_INTRADAY_CAPTURE_NOT_CONFIRMED")
                if int(ls.get("rows",0) or 0)<=0:
                    blockers.append("LIVE_INTRADAY_NO_CAPTURED_ROWS")
            else:
                blockers.append("LIVE_INTRADAY_STATUS_MISSING")
        except Exception:
            blockers.append("LIVE_INTRADAY_FEED_UNREADABLE")

    state="FINAL_SELECTION_READY" if not blockers else "PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED"
    df["FINAL_SELECTION_STATE"]=state
    df.to_csv(OUT/"ranked_candidates_all.csv",index=False)
    df.head(30).to_csv(OUT/"provisional_top30.csv",index=False)
    df.head(10).to_csv(OUT/"provisional_top10.csv",index=False)
    df.head(3).to_csv(OUT/"provisional_top3.csv",index=False)
    report={"state":state,"candidate_count":int(len(df)),
            "provisional_top30":min(30,len(df)),"provisional_top10":min(10,len(df)),
            "provisional_top3":min(3,len(df)),"blockers":blockers,
            "note":"Top-N files are ranked research shortlists, not actionable finalists, until every readiness gate passes."}
    (OUT/"final_selection_status.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
