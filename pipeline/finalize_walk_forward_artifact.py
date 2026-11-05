#!/usr/bin/env python3
"""Rebuild final walk-forward metrics from the exact persisted CSVs before upload."""
import hashlib, json
from pathlib import Path
import pandas as pd

ROOT=Path("outputs/backtest")
pred=pd.read_csv(ROOT/"walk_forward_predictions.csv")
uni=pd.read_csv(ROOT/"walk_forward_universe_probabilities.csv")
for name,df in [("predictions",pred),("universe",uni)]:
    if df.duplicated(["CUT_OFF","SYMBOL"]).any():
        raise SystemExit(f"BLOCKED: duplicate {name} keys")
if len(pred)!=900 or pred.CUT_OFF.nunique()!=30 or not pred.groupby("CUT_OFF").size().eq(30).all():
    raise SystemExit("BLOCKED: Top-30 must contain 30 rows for each of 30 cutoffs")
if set(pred.CUT_OFF.unique())!=set(uni.CUT_OFF.unique()):
    raise SystemExit("BLOCKED: cutoff mismatch")

metrics_path=ROOT/"walk_forward_metrics.json"
metrics=json.loads(metrics_path.read_text())
report_path=ROOT/"walk_forward_maturity_reconciliation.json"
report=json.loads(report_path.read_text())
metrics["precision"]={}; metrics["recall"]={}; metrics["base_rate"]={}; metrics["lift"]={}
metrics["outcome_maturity_counts"]={}
report["metrics"]={}
for h,t in [(1,5),(3,10),(5,20)]:
    col=f"FUT{h}_HIGH_PCT"; key=f"T{t}_H{h}"
    pe=pred[pred[col].notna()]; ue=uni[uni[col].notna()]
    hits=int((pe[col]>=t).sum()); winners=int((ue[col]>=t).sum())
    precision=hits/len(pe) if len(pe) else None
    base=winners/len(ue) if len(ue) else None
    recall=hits/winners if winners else None
    lift=precision/base if precision is not None and base else None
    counts={"top30_selected":int(len(pred)),"top30_matured":int(len(pe)),
            "top30_hits":hits,"universe_rows":int(len(uni)),
            "universe_matured":int(len(ue)),"universe_winners":winners}
    metrics["precision"][key]=precision; metrics["recall"][key]=recall
    metrics["base_rate"][key]=base; metrics["lift"][key]=lift
    metrics["outcome_maturity_counts"][key]=counts
    report["metrics"][key]={"precision":precision,"recall":recall,
                            "base_rate":base,"lift":lift,"maturity":counts}
# Replace stale reconciliation values only from disk-recomputed CSV counts.
metrics["maturity_reconciled"]=True
metrics["audit_note"]="Final metrics recomputed from persisted prediction/universe CSVs after write; complete matured windows only. 30-cutoff research pilot, not production validation."
report["status"]="PASS_PERSISTED_CSV_RECOMPUTED"
report["cutoffs"]=int(pred.CUT_OFF.nunique())
report["top30_rows"]=int(len(pred)); report["universe_rows"]=int(len(uni))
metrics_path.write_text(json.dumps(metrics,indent=2)+"\\n")
report_path.write_text(json.dumps(report,indent=2)+"\\n")
# Mandatory independent read-back after rewriting both JSON files.
m2=json.loads(metrics_path.read_text()); r2=json.loads(report_path.read_text())
for key in r2["metrics"]:
    if m2["outcome_maturity_counts"][key]!=r2["metrics"][key]["maturity"]:
        raise SystemExit(f"BLOCKED: final JSON mismatch {key}")
    if m2["precision"][key]!=r2["metrics"][key]["precision"]:
        raise SystemExit(f"BLOCKED: final precision mismatch {key}")
hashes={}
for p in sorted(ROOT.iterdir()):
    if p.is_file(): hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/"walk_forward_artifact_file_hashes.json").write_text(json.dumps(hashes,indent=2)+"\\n")
print(json.dumps({"status":"PASS_PERSISTED_CSV_RECOMPUTED",
                  "pred_rows":len(pred),"universe_rows":len(uni),
                  "metrics":r2["metrics"],"file_hashes":hashes},indent=2))
