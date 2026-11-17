#!/usr/bin/env python3
"""PRECISION-WIRES V11.3 duplicate guard; research-only, fail-closed."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd

def norm_symbol(s):
    return s.astype("string").str.strip().str.upper()

def norm_date(s):
    return pd.to_datetime(s, errors="coerce").dt.strftime("%Y-%m-%d")

def evaluate(universe, signals, candidates):
    if not {"SYMBOL","DATE"}.issubset(universe.columns):
        raise ValueError("historical universe requires SYMBOL, DATE")
    if not {"SYMBOL","CUT_OFF"}.issubset(signals.columns):
        raise ValueError("historical signals require SYMBOL, CUT_OFF")
    if "SYMBOL" not in candidates.columns:
        raise ValueError("candidate file requires SYMBOL")
    u=universe.copy(); h=signals.copy(); c=candidates.copy()
    u["SYMBOL_KEY"]=norm_symbol(u["SYMBOL"]); u["DATE_KEY"]=norm_date(u["DATE"])
    h["SYMBOL_KEY"]=norm_symbol(h["SYMBOL"]); h["DATE_KEY"]=norm_date(h["CUT_OFF"])
    c["SYMBOL_KEY"]=norm_symbol(c["SYMBOL"])
    c["DATE_KEY"]=norm_date(c["CUT_OFF"]) if "CUT_OFF" in c else pd.NA
    if u[["SYMBOL_KEY","DATE_KEY"]].isna().any().any() or h[["SYMBOL_KEY","DATE_KEY"]].isna().any().any():
        raise ValueError("invalid historical key; fail closed")
    if u.duplicated(["SYMBOL_KEY","DATE_KEY"]).any():
        raise ValueError("duplicate historical SYMBOL+DATE key; fail closed")
    if h.duplicated(["SYMBOL_KEY","DATE_KEY"]).any():
        raise ValueError("duplicate historical signal SYMBOL+CUT_OFF key; fail closed")
    seen=set(u["SYMBOL_KEY"])
    exact=set(zip(h["SYMBOL_KEY"],h["DATE_KEY"]))
    status=[]; reasons=[]
    for row in c.itertuples(index=False):
        sym=row.SYMBOL_KEY; day=row.DATE_KEY
        if pd.isna(sym) or not sym:
            status.append("UNKNOWN_BLOCK"); reasons.append("MISSING_OR_INVALID_SYMBOL")
        elif pd.notna(day) and (sym,day) in exact:
            status.append("DUPLICATE_BLOCK"); reasons.append("EXACT_SYMBOL_CUTOFF_ALREADY_SELECTED")
        elif sym in seen:
            status.append("REVISIT"); reasons.append("SYMBOL_ALREADY_IN_200_SESSION_ANALYZED_UNIVERSE")
        else:
            status.append("NEW_CANDIDATE"); reasons.append("SYMBOL_ABSENT_FROM_HISTORICAL_ANALYZED_UNIVERSE")
    c["DUPLICATE_STATUS"]=status; c["DUPLICATE_REASON"]=reasons
    report={"historical_processed_rows":int(len(u)),
      "historical_analyzed_symbols":int(len(seen)),"historical_sessions":int(u["DATE_KEY"].nunique()),
      "historical_top30_signal_rows":int(len(h)),"historical_top30_symbols":int(h["SYMBOL_KEY"].nunique()),
      "candidate_rows":int(len(c)),"new_candidates":int((c.DUPLICATE_STATUS=="NEW_CANDIDATE").sum()),
      "revisits":int((c.DUPLICATE_STATUS=="REVISIT").sum()),
      "exact_duplicates_blocked":int((c.DUPLICATE_STATUS=="DUPLICATE_BLOCK").sum()),
      "unknown_blocked":int((c.DUPLICATE_STATUS=="UNKNOWN_BLOCK").sum()),
      "normalization":"strip + uppercase only; no fuzzy/alias matching","production_selector_modified":False}
    return c,report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--historical-universe",required=True)
    p.add_argument("--historical-signals",required=True)
    p.add_argument("--new-candidates",required=True)
    p.add_argument("--out",default="outputs/duplicate_guard")
    a=p.parse_args()
    u=pd.read_csv(a.historical_universe,dtype={"SYMBOL":"string","DATE":"string"})
    h=pd.read_csv(a.historical_signals,dtype={"SYMBOL":"string","CUT_OFF":"string"})
    c=pd.read_csv(a.new_candidates,dtype={"SYMBOL":"string","CUT_OFF":"string"})
    result,report=evaluate(u,h,c)
    dest=Path(a.out); dest.mkdir(parents=True,exist_ok=True)
    result.to_csv(dest/"candidate_duplicate_status.csv",index=False)
    (dest/"duplicate_guard_report.json").write_text(json.dumps(report,indent=2)+"\\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
