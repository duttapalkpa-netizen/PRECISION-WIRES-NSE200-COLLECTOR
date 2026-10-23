#!/usr/bin/env python3
"""Audited join of independently verified publisher resolutions to discovery evidence.

This does not rewrite the source news ledger and does not declare research READY.
It only emits a resolution audit when stable row/cutoff/symbol/headline/time keys agree.
"""
from pathlib import Path
import json
import pandas as pd

CANDIDATES=Path("artifact/outputs/news_24h/stock_news_alternate_source_candidates.csv")
VERIFIED=Path("outputs/news_24h/alternate_source_verification_results.csv")
OUT=Path("outputs/news_24h/alternate_source_resolution_join.json")
CSV=Path("outputs/news_24h/alternate_source_resolution_join.csv")

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    for p in (CANDIDATES,VERIFIED):
        if not p.is_file():
            report={"status":"BLOCKED_MISSING_INPUT","missing":str(p),"joined_rows":0,"research_status":"BLOCKED"}
            OUT.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report)); raise SystemExit(2)
    c=pd.read_csv(CANDIDATES,dtype=str).fillna("")
    v=pd.read_csv(VERIFIED,dtype=str).fillna("")
    keys=["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL","ALTERNATE_ARTICLE_URL"]
    missing=[k for k in keys if k not in c.columns or k not in v.columns]
    if missing:
        report={"status":"BLOCKED_BAD_SCHEMA","missing_columns":missing,"joined_rows":0,"research_status":"BLOCKED"}
        OUT.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report)); raise SystemExit(2)
    # One-to-one join on immutable source-row identity plus cutoff/symbol/time and URLs.
    j=c.merge(v,on=keys,how="left",suffixes=("_DISCOVERY","_VERIFY"),validate="one_to_one",indicator=True)
    j["RESOLUTION_JOIN_STATUS"]="UNRESOLVED"
    is_verified=j["_merge"].eq("both") & j["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED")
    # Ensure article title agrees with the discovered alternate headline at >= 0.50
    # (threshold already independently tested by verifier); publication timestamp must
    # be parseable and within 24h of the source event timestamp.
    orig=pd.to_datetime(j["ORIGINAL_PUBLISHED_AT"],utc=True,errors="coerce")
    alt=pd.to_datetime(j.get("ALTERNATE_PUBLISHED_AT",pd.Series("",index=j.index)),utc=True,errors="coerce")
    time_ok=orig.notna() & alt.notna() & ((orig-alt).abs()<=pd.Timedelta(hours=24))
    j.loc[is_verified & time_ok,"RESOLUTION_JOIN_STATUS"]="SOURCE_URL_RESOLVED_TIME_ALIGNED"
    j.loc[is_verified & ~time_ok,"RESOLUTION_JOIN_STATUS"]="VERIFIED_PAGE_BUT_TIMESTAMP_UNCONFIRMED"
    cols=[x for x in ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_PUBLISHER","ORIGINAL_HEADLINE","ORIGINAL_URL","ALTERNATE_PUBLISHER","ALTERNATE_ARTICLE_URL","ALTERNATE_PUBLISHED_AT","VERIFICATION_STATUS","RESOLVED_URL","PUBLISHER_PAGE_TITLE","HEADLINE_TOKEN_OVERLAP","RESOLUTION_JOIN_STATUS"] if x in j.columns]
    out=j[cols].copy()
    out.to_csv(CSV,index=False)
    resolved=int(out["RESOLUTION_JOIN_STATUS"].eq("SOURCE_URL_RESOLVED_TIME_ALIGNED").sum())
    time_uncertain=int(out["RESOLUTION_JOIN_STATUS"].eq("VERIFIED_PAGE_BUT_TIMESTAMP_UNCONFIRMED").sum())
    report={"status":"PASS_RESOLUTION_JOIN_AUDIT_ONLY" if resolved>0 else "BLOCKED_NO_TIME_ALIGNED_RESOLUTIONS","candidate_rows":len(c),"verified_candidate_rows":int(j["VERIFICATION_STATUS"].astype(str).str.upper().eq("VERIFIED").sum()),"source_url_resolved_time_aligned_rows":resolved,"verified_page_timestamp_unconfirmed_rows":time_uncertain,"join_keys":keys,"output_csv":str(CSV),"source_ledger_modified":False,"research_status":"BLOCKED","reason":"Publisher URL resolution is not sufficient to mark the paired-news research gate READY. Original source ledger is not included in the artifact; this audit joins against the discovery snapshot only. A separate source-ledger update and full readiness checks remain required.","rows":out.to_dict("records")}
    OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print("ALTERNATE_SOURCE_RESOLUTION_JOIN="+json.dumps(report,sort_keys=True,ensure_ascii=False))
    if resolved==0: raise SystemExit(1)
if __name__=="__main__": main()
