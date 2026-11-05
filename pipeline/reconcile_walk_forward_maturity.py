#!/usr/bin/env python3
"""Reconcile V11.4 walk-forward metrics strictly on matured, key-aligned outcomes."""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

def calibration(y,p,bins=10):
    y=np.asarray(y,dtype=float); p=np.asarray(p,dtype=float)
    ok=np.isfinite(y)&np.isfinite(p); y=y[ok]; p=p[ok]
    if not len(y): return {"n":0,"brier":None,"ece":None,"bins":[]}
    edges=np.linspace(0,1,bins+1); ece=0.0; rows=[]
    for i in range(bins):
        m=(p>=edges[i])&((p<edges[i+1]) if i<bins-1 else (p<=edges[i+1]))
        if m.any():
            n=int(m.sum()); obs=float(y[m].mean()); pred=float(p[m].mean())
            ece+=(n/len(y))*abs(obs-pred)
            rows.append({"bin":i+1,"n":n,"mean_pred":pred,"observed_rate":obs})
    return {"n":int(len(y)),"brier":float(np.mean((p-y)**2)),"ece":float(ece),"bins":rows}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="outputs/backtest")
    a=ap.parse_args(); root=Path(a.input)
    pred=pd.read_csv(root/"walk_forward_predictions.csv")
    uni=pd.read_csv(root/"walk_forward_universe_probabilities.csv")
    diag=pd.read_csv(root/"diagnostic_separation_672.csv")
    for x,name in [(pred,"predictions"),(uni,"universe"),(diag,"diagnostics")]:
        for c in ["CUT_OFF","SYMBOL"]:
            if c not in x: raise SystemExit(f"BLOCKED: {name} missing {c}")
        if x.duplicated(["CUT_OFF","SYMBOL"]).any(): raise SystemExit(f"BLOCKED: duplicate {name} cutoff/symbol keys")
    counts=pred.groupby("CUT_OFF").size()
    if len(counts)!=30 or not counts.eq(30).all():
        raise SystemExit("BLOCKED: expected exactly 30 Top-30 candidates for each of 30 cutoffs")
    if set(pred.CUT_OFF.unique())!=set(uni.CUT_OFF.unique()):
        raise SystemExit("BLOCKED: predictions/universe cutoff mismatch")
    # Every selected row must exist in the corresponding scored universe and align to its outcome labels.
    chk=pred[["CUT_OFF","SYMBOL","FUT1_HIGH_PCT","FUT3_HIGH_PCT","FUT5_HIGH_PCT"]].merge(
        uni[["CUT_OFF","SYMBOL","FUT1_HIGH_PCT","FUT3_HIGH_PCT","FUT5_HIGH_PCT"]],
        on=["CUT_OFF","SYMBOL"],how="left",suffixes=("_top","_universe"),validate="one_to_one")
    if chk.filter(like="_universe").isna().all(axis=None):
        raise SystemExit("BLOCKED: selected candidates cannot be reconciled to universe")
    for h in [1,3,5]:
        x=chk[f"FUT{h}_HIGH_PCT_top"]; y=chk[f"FUT{h}_HIGH_PCT_universe"]
        both=x.notna()&y.notna()
        if not np.allclose(x[both],y[both],rtol=0,atol=1e-9):
            raise SystemExit(f"BLOCKED: selected outcome mismatch at H+{h}")
    metrics_path=root/"walk_forward_metrics.json"
    metrics=json.loads(metrics_path.read_text())
    metrics["maturity_reconciled"]=True
    metrics["outcome_maturity_counts"]={}
    metrics["precision"]={}; metrics["recall"]={}; metrics["base_rate"]={}; metrics["lift"]={}
    metrics["full_universe_probability_calibration"]={}
    for h,t,pcol in [(1,5,"P5_H1"),(3,10,"P10_H3"),(5,20,"P20_H5")]:
        col=f"FUT{h}_HIGH_PCT"
        pe=pred[pred[col].notna()].copy(); ue=uni[uni[col].notna()].copy()
        hits=int((pe[col]>=t).sum()); winners=int((ue[col]>=t).sum())
        precision=float(hits/len(pe)) if len(pe) else None
        base=float(winners/len(ue)) if len(ue) else None
        key=f"T{t}_H{h}"
        metrics["precision"][key]=precision
        metrics["recall"][key]=float(hits/winners) if winners else None
        metrics["base_rate"][key]=base
        metrics["lift"][key]=float(precision/base) if precision is not None and base else None
        metrics["outcome_maturity_counts"][key]={
            "top30_selected":int(len(pred)),"top30_matured":int(len(pe)),
            "top30_hits":hits,"universe_rows":int(len(uni)),
            "universe_matured":int(len(ue)),"universe_winners":winners}
        y=(ue[col]>=t).astype(int).to_numpy()
        p=pd.to_numeric(ue[pcol],errors="coerce").to_numpy()
        cal=calibration(y,p)
        cal["winner_mean"]=float(np.nanmean(p[y==1])) if (y==1).any() else None
        cal["nonwinner_mean"]=float(np.nanmean(p[y==0])) if (y==0).any() else None
        cal["mean_gap"]=cal["winner_mean"]-cal["nonwinner_mean"] if cal["winner_mean"] is not None and cal["nonwinner_mean"] is not None else None
        metrics["full_universe_probability_calibration"][key]=cal
    # Target-specific Top-30 state and probability separation on matured labels only.
    metrics["state_performance_maturity_reconciled"]={}
    for state,g in pred.groupby("STATE"):
        item={"rows":int(len(g))}
        for h,t in [(1,5),(3,10),(5,20)]:
            m=g[g[f"FUT{h}_HIGH_PCT"].notna()]
            item[f"hit{t}_h{h}"]=float((m[f"FUT{h}_HIGH_PCT"]>=t).mean()) if len(m) else None
            item[f"n_matured_h{h}"]=int(len(m))
        metrics["state_performance_maturity_reconciled"][state]=item
    h3=pred[pred.FUT3_HIGH_PCT.notna()]
    win=h3.FUT3_HIGH_PCT>=10
    metrics["winner_probability_separation_matured"]={
        "n_matured":int(len(h3)),"winners":int(win.sum()),"nonwinners":int((~win).sum()),
        "winner_mean":float(h3.loc[win,"WINNER_PROBABILITY"].mean()) if win.any() else None,
        "nonwinner_mean":float(h3.loc[~win,"WINNER_PROBABILITY"].mean()) if (~win).any() else None,
        "winner_median":float(h3.loc[win,"WINNER_PROBABILITY"].median()) if win.any() else None,
        "nonwinner_median":float(h3.loc[~win,"WINNER_PROBABILITY"].median()) if (~win).any() else None}
    # Align diagnostics by key; never assume row order.
    joined=diag.merge(pred[["CUT_OFF","SYMBOL","FUT3_HIGH_PCT"]],on=["CUT_OFF","SYMBOL"],how="inner",validate="one_to_one")
    joined=joined[joined.FUT3_HIGH_PCT.notna()].copy()
    sep=[]; base=float((joined.FUT3_HIGH_PCT>=10).mean()) if len(joined) else np.nan
    for col in [c for c in diag.columns if c not in ("CUT_OFF","SYMBOL")]:
        for state in ["POSITIVE","NEGATIVE","UNKNOWN","NOT_APPLICABLE"]:
            g=joined[joined[col].eq(state)]
            if len(g):
                rate=float((g.FUT3_HIGH_PCT>=10).mean())
                sep.append({"diagnostic":col,"state":state,"n":int(len(g)),
                            "winner_rate":rate,"base_winner_rate":base,
                            "lift":float(rate/base) if base and np.isfinite(base) else None})
    pd.DataFrame(sep).to_csv(root/"diagnostic_winner_separation_matured.csv",index=False)
    metrics["diagnostic_winner_separation_matured"]={"n":int(len(joined)),"base_winner_rate":base,
                                                       "rows":len(sep)}
    metrics["audit_note"]="All precision/recall/lift/calibration and diagnostic separation metrics in this reconciliation use only complete, matured target windows. This is a 30-cutoff research pilot, not production validation."
    metrics_path.write_text(json.dumps(metrics,indent=2)+"\n")
    report={"status":"PASS_MATURITY_RECONCILIATION","cutoffs":int(len(counts)),
            "top30_rows":int(len(pred)),"universe_rows":int(len(uni)),
            "metrics":{k:{"precision":metrics["precision"][k],"recall":metrics["recall"][k],
                          "base_rate":metrics["base_rate"][k],"lift":metrics["lift"][k],
                          "maturity":metrics["outcome_maturity_counts"][k]}
                       for k in metrics["precision"]}}
    (root/"walk_forward_maturity_reconciliation.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
