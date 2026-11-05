#!/usr/bin/env python3
"""Research-only candidate freshness audit. Does not rank, filter, or alter selector outputs."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--universe",default="data/processed/nse_eq_200_sessions.csv")
    p.add_argument("--candidates",default="outputs/finalists/v11_3_risk_adjusted.csv")
    p.add_argument("--out",default="outputs/qa/candidate_freshness")
    a=p.parse_args()
    u=pd.read_csv(a.universe,usecols=["SYMBOL","DATE"],dtype={"SYMBOL":str,"DATE":str})
    c=pd.read_csv(a.candidates,usecols=["SYMBOL","DATE","RISK_ADJUSTED_SCORE"],dtype={"SYMBOL":str,"DATE":str})
    for d in (u,c):
        d["SYMBOL"]=d.SYMBOL.str.strip().str.upper()
        d["DATE"]=pd.to_datetime(d.DATE,errors="coerce")
    if u.empty or c.empty or u.DATE.isna().any() or c.DATE.isna().any():
        raise SystemExit("BLOCKED: empty input or invalid session dates")
    if u.duplicated(["SYMBOL","DATE"]).any():
        raise SystemExit("BLOCKED: duplicate symbol/session keys in universe")
    latest_session=u.DATE.max()
    latest_by_symbol=u.groupby("SYMBOL").DATE.max().rename("SOURCE_LATEST_DATE")
    x=c.merge(latest_by_symbol,on="SYMBOL",how="left",validate="many_to_one")
    x["DATA_LAG_SESSIONS"]=x.SOURCE_LATEST_DATE.map(lambda d: int((u.loc[u.DATE>d,"DATE"].drop_duplicates().nunique())) if pd.notna(d) else None)
    x["FRESHNESS_STATUS"]="STALE"
    x.loc[x.SOURCE_LATEST_DATE.eq(latest_session),"FRESHNESS_STATUS"]="CURRENT"
    x.loc[x.SOURCE_LATEST_DATE.isna(),"FRESHNESS_STATUS"]="SYMBOL_NOT_IN_UNIVERSE"
    x["CANDIDATE_ROW_DATE_MATCHES_SOURCE_LATEST"]=x.DATE.eq(x.SOURCE_LATEST_DATE)
    stale=x[(x.FRESHNESS_STATUS!="CURRENT") | (~x.CANDIDATE_ROW_DATE_MATCHES_SOURCE_LATEST)].copy()
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    x.to_csv(out/"candidate_freshness_all.csv",index=False)
    stale.to_csv(out/"candidate_freshness_exceptions.csv",index=False)
    top={}
    for n in (30,10,3):
        t=x.sort_values(["RISK_ADJUSTED_SCORE","SYMBOL"],ascending=[False,True]).head(n)
        top[str(n)]={"rows":len(t),"current_rows":int(t.FRESHNESS_STATUS.eq("CURRENT").sum()),
                     "stale_rows":int(t.FRESHNESS_STATUS.ne("CURRENT").sum()),
                     "all_candidate_dates_match_latest":bool(t.CANDIDATE_ROW_DATE_MATCHES_SOURCE_LATEST.all())}
    report={"status":"PASS_AUDIT_ONLY" if not stale.empty else "PASS_NO_STALE_CANDIDATES",
            "latest_market_session":latest_session.strftime("%Y-%m-%d"),
            "universe_symbols":int(u.SYMBOL.nunique()),"candidate_rows":int(len(c)),
            "candidate_symbols":int(c.SYMBOL.nunique()),"current_candidate_rows":int(x.FRESHNESS_STATUS.eq("CURRENT").sum()),
            "stale_or_unmatched_rows":int(len(stale)),"top_n":top,
            "interpretation":"Audit-only. No rows are removed and no ranking or production selector is changed.",
            "required_action":"Investigate stale source coverage and apply freshness eligibility only in a separately reviewed readiness gate; preserve ranking scores and CORE-672."}
    (out/"candidate_freshness_report.json").write_text(json.dumps(report,indent=2)+"\\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
