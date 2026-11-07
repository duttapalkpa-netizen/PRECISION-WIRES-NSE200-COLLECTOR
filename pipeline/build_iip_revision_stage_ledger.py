#!/usr/bin/env python3
"""Build policy-derived IIP estimate-stage joins; never changes source data or Hard Gate."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path("artifacts/iip_41_vintage_audit")
OUT = ROOT

def build_stage(period, release_ref_period, release_date):
    obs = pd.to_datetime(period, errors="coerce")
    ref = pd.to_datetime(release_ref_period, errors="coerce")
    rd = pd.to_datetime(release_date, errors="coerce")
    if pd.isna(obs) or pd.isna(ref) or pd.isna(rd):
        return "UNKNOWN", "MISSING_REQUIRED_DATE_OR_PERIOD"
    gap = (ref.to_period("M") - obs.to_period("M")).n
    if rd.date() < pd.Timestamp("2025-04-28").date():
        policy = "LEGACY_QUICK_FIRST_FINAL"
        return ({0:"QUICK",1:"FIRST_REVISION",3:"FINAL"}.get(gap,"HISTORICAL_PANEL"), policy)
    if rd.date() == pd.Timestamp("2025-04-28").date():
        policy = "TRANSITION_QUICK_FINAL_BACKLOG"
        if gap == 0: return "QUICK", policy
        if gap in (1,2,3): return "FINAL_TRANSITION_BACKLOG", policy
        return "HISTORICAL_PANEL", policy
    policy = "QUICK_FINAL"
    return ({0:"QUICK",1:"FINAL"}.get(gap,"HISTORICAL_PANEL"), policy)

def main():
    manifest = pd.read_csv(OUT/"vintage_ingestion_manifest.csv", dtype=str).fillna("")
    obs = pd.read_csv(OUT/"all_vintage_observations.csv", dtype=str).fillna("")
    diffs = pd.read_csv(OUT/"revision_differences.csv", dtype=str).fillna("")
    meta = manifest[["unique_id","release_date","ref_period","base_year","classification","sha256","file_name","http_status","download_status","parse_status"]].drop_duplicates("unique_id")
    meta = meta.rename(columns={"unique_id":"table_id","ref_period":"release_ref_period","sha256":"manifest_sha256","file_name":"manifest_file_name"})
    joined = obs.merge(meta,on="table_id",how="left",suffixes=("","_manifest"))
    for field in ("release_date","base_year","classification"):
        other=field+"_manifest"
        if other in joined:
            mismatch=(joined[field]!="")&(joined[other]!="")&(joined[field]!=joined[other])
            if mismatch.any(): raise SystemExit(f"manifest mismatch {field}: {int(mismatch.sum())}")
    # Calculate stage once per unique (release vintage, period), then map to all rows.
    unique=joined[["table_id","period","release_ref_period","release_date","base_year"]].drop_duplicates()
    stage_pairs=unique.apply(lambda r:build_stage(r.period,r.release_ref_period,r.release_date),axis=1)
    unique["estimate_stage"]=[x[0] for x in stage_pairs]
    unique["release_policy"]=[x[1] for x in stage_pairs]
    unique["methodology_vintage"]="LEGACY_BASE_SERIES_METHOD_VINTAGE_NOT_RETAGGED"
    new=unique.base_year.eq("2022-23")
    unique.loc[new,"methodology_vintage"]="NEW_BASE_SERIES_METHOD_VINTAGE_NOT_FULLY_JOINED"
    ppi=new & (pd.to_datetime(unique.release_date,errors="coerce")>=pd.Timestamp("2026-06-29"))
    unique.loc[ppi,"methodology_vintage"]="OUTPUT_PPI_SUPERSEDING_SERIES"
    joined=joined.merge(unique[["table_id","period","estimate_stage","release_policy","methodology_vintage"]],on=["table_id","period"],how="left")
    cols=["table_id","release_date","release_ref_period","period","nic_code","base_year","classification","estimate_stage","release_policy","methodology_vintage","value","measure","source_sha256","source_file","http_status","download_status","parse_status"]
    joined[cols].to_csv(OUT/"iip_observation_estimate_stage_ledger.csv",index=False)
    lookup=joined[["table_id","period","nic_code","estimate_stage","release_policy","methodology_vintage","source_sha256"]].drop_duplicates(["table_id","period","nic_code"])
    prev=lookup.rename(columns={"table_id":"previous_table_id","estimate_stage":"previous_stage","release_policy":"previous_policy","methodology_vintage":"previous_methodology_vintage","source_sha256":"previous_joined_sha256"})
    cur=lookup.rename(columns={"table_id":"current_table_id","estimate_stage":"current_stage","release_policy":"current_policy","methodology_vintage":"current_methodology_vintage","source_sha256":"current_joined_sha256"})
    diffs.period=diffs.period.astype(str); diffs.nic_code=diffs.nic_code.astype(str)
    out=diffs.merge(prev,on=["previous_table_id","period","nic_code"],how="left").merge(cur,on=["current_table_id","period","nic_code"],how="left")
    for side in ("previous","current"):
        expected=side+"_sha256"; got=side+"_joined_sha256"
        bad=(out[expected]!="")&(out[got]!="")&(out[expected]!=out[got])
        if bad.any(): raise SystemExit(f"SHA join mismatch {side}: {int(bad.sum())}")
    allowed={"QUICK","FIRST_REVISION","FINAL","FINAL_TRANSITION_BACKLOG"}
    out["transition_review_status"]=out.apply(lambda r:"POLICY_STAGE_ALIGNED_CANDIDATE_NOT_CERTIFIED" if r.previous_stage in allowed and r.current_stage in allowed else "UNRESOLVED_HISTORICAL_PANEL_OR_OUT_OF_WINDOW",axis=1)
    out.to_csv(OUT/"iip_revision_stage_join.csv",index=False)
    summary={
      "input_observation_rows":int(len(obs)),
      "joined_observation_rows":int(len(joined)),
      "unique_vintage_ids":int(joined.table_id.nunique()),
      "observation_stage_counts":{str(k):int(v) for k,v in joined.estimate_stage.value_counts().to_dict().items()},
      "revision_difference_rows":int(len(diffs)),
      "revision_stage_join_rows":int(len(out)),
      "revision_stage_pair_counts":{f"{a} -> {b}":int(v) for (a,b),v in out.groupby(["previous_stage","current_stage"]).size().to_dict().items()},
      "revision_methodology_pair_counts":{f"{a} -> {b}":int(v) for (a,b),v in out.groupby(["previous_methodology_vintage","current_methodology_vintage"]).size().to_dict().items()},
      "unjoined_revision_rows":int(out[["previous_stage","current_stage"]].isna().any(axis=1).sum()),
      "policy_stage_aligned_candidate_transitions_not_certified":int((out.transition_review_status=="POLICY_STAGE_ALIGNED_CANDIDATE_NOT_CERTIFIED").sum()),
      "unresolved_historical_panel_or_out_of_window_transitions":int((out.transition_review_status=="UNRESOLVED_HISTORICAL_PANEL_OR_OUT_OF_WINDOW").sum()),
      "unknown_observation_stage_rows":int((joined.estimate_stage=="UNKNOWN").sum()),
      "hard_gate":"BLOCKED",
      "interpretation":"Policy-derived stage join only. Candidate transitions are not certified revisions until each source release and methodology vintage is independently joined. This sidecar does not alter the source audit or Hard Gate."
    }
    (OUT/"iip_revision_stage_ledger_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
