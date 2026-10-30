#!/usr/bin/env python3
"""Rank shared Factor Registry source gaps from an existing audited snapshot.

This is a diagnostic only: it never promotes coverage or edits production inputs.
"""
from pathlib import Path
import csv, json
from collections import Counter, defaultdict

INPUT=Path("outputs/macro_geo/factor_coverage_audit.csv")
OUT=Path("outputs/macro_geo")
EXPECTED=35

def build_priority(rows):
    if len(rows)!=EXPECTED:
        raise ValueError(f"Expected {EXPECTED} factor rows, got {len(rows)}")
    factor_ids=[r.get("factor_id","") for r in rows]
    if len(set(factor_ids))!=EXPECTED or any(not x for x in factor_ids):
        raise ValueError("Factor registry IDs must be unique and complete")
    disconnected=Counter()
    partial=Counter()
    impacted=defaultdict(list)
    for row in rows:
        fid=row["factor_id"]
        state=row.get("coverage_status","")
        for item in filter(None,row.get("source_statuses","").split(";")):
            name,sep,status=item.rpartition(":")
            if not sep or not name:
                raise ValueError(f"Malformed source status for {fid}: {item}")
            if status=="NOT_CONNECTED":
                disconnected[name]+=1
                impacted[name].append(fid)
            elif status!="AVAILABLE":
                partial[name]+=1
    ranked=[]
    for name,count in disconnected.most_common():
        ranked.append({
            "source_group":name,
            "not_connected_factor_count":count,
            "affected_factors":sorted(impacted[name]),
            "additional_partial_factor_count":partial.get(name,0),
            "priority_basis":"shared NOT_CONNECTED mapping count; tie-break by partial exposure",
            "coverage_action":"SOURCE_REMEDIATION_REQUIRED",
            "promotion_rule":"Do not promote without source-specific provenance, timestamp, schema, domain QA and nonzero observed rows"
        })
    return {
        "status":"GAP_PRIORITY_AUDITED",
        "factor_groups":len(rows),
        "not_connected_factors":sum(r.get("coverage_status")=="NOT_CONNECTED" for r in rows),
        "partial_factors":sum(r.get("coverage_status")=="PARTIAL_SOURCE_COVERAGE" for r in rows),
        "source_groups_ranked":ranked,
        "recommended_first_source_group":ranked[0]["source_group"] if ranked else None,
        "safety":"Diagnostic ranking only. Does not change coverage status, factor states, selector, RANKING_SCORE, +1 PRESSURE_FADE or 672 diagnostics."
    }

def main():
    if not INPUT.exists():
        raise SystemExit(f"Missing audited input: {INPUT}")
    with INPUT.open(newline="",encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    report=build_priority(rows)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"factor_gap_priority_audit.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    with (OUT/"factor_gap_priority_audit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["rank","source_group","not_connected_factor_count","affected_factors","additional_partial_factor_count","coverage_action"])
        w.writeheader()
        for i,item in enumerate(report["source_groups_ranked"],1):
            w.writerow({"rank":i,"source_group":item["source_group"],"not_connected_factor_count":item["not_connected_factor_count"],"affected_factors":";".join(item["affected_factors"]),"additional_partial_factor_count":item["additional_partial_factor_count"],"coverage_action":item["coverage_action"]})
    print(json.dumps({"status":report["status"],"factor_groups":report["factor_groups"],"not_connected_factors":report["not_connected_factors"],"partial_factors":report["partial_factors"],"recommended_first_source_group":report["recommended_first_source_group"],"top_groups":report["source_groups_ranked"][:5]},indent=2))

if __name__=="__main__": main()
