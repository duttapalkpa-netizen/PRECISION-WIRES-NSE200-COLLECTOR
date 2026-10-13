#!/usr/bin/env python3
"""Target-specific 30-cutoff paired audit. Historical exploratory only; never promotes a selector."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/prospective/strict_30_matured_cutoff_audit.json")
DAILY = Path("outputs/prospective/strict_30_matured_cutoff_daily.csv")
TOP_N, WATCH_N, REQUIRED_CUTOFFS = 30, 5, 30
BOOTSTRAPS, SEED = 10000, 3058
TARGETS = {
    "T5_H1": ("FUT1_HIGH_PCT", 5.0),
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
SELECTORS = ("CURRENT_WINNER_PROB", "P10_P20_MEAN")
NEEDED = {"CUT_OFF","SYMBOL","RANKING_SCORE","WINNER_PROBABILITY_PCTL",
          "P10_H3_PCTL","P20_H5_PCTL","FUT1_HIGH_PCT","FUT3_HIGH_PCT","FUT5_HIGH_PCT"}

def ci(values, rng):
    x = np.asarray(values, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) < 2:
        return [None, None]
    ix = rng.integers(0, len(x), size=(BOOTSTRAPS, len(x)))
    means = x[ix].mean(axis=1)
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]

def main():
    if not SRC.exists():
        raise SystemExit(f"Required walk-forward input missing: {SRC}")
    df = pd.read_csv(SRC)
    missing = sorted(NEEDED - set(df.columns))
    if missing:
        raise SystemExit(f"Required columns missing: {missing}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="coerce")
    df = df.dropna(subset=["CUT_OFF","SYMBOL"]).drop_duplicates(["CUT_OFF","SYMBOL"]).copy()
    df["RANKING_SCORE"] = pd.to_numeric(df["RANKING_SCORE"], errors="coerce")
    df = df[df["RANKING_SCORE"].notna()].copy()
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(ascending=False, method="first")
    df["CURRENT_WINNER_PROB"] = pd.to_numeric(df["WINNER_PROBABILITY_PCTL"], errors="coerce")
    df["P10_P20_MEAN"] = (pd.to_numeric(df["P10_H3_PCTL"], errors="coerce") +
                           pd.to_numeric(df["P20_H5_PCTL"], errors="coerce")) / 2
    rng = np.random.default_rng(SEED)
    summaries, daily_all = {}, []
    for target, (label, threshold) in TARGETS.items():
        x = df[df["BASE_RANK"] > TOP_N].copy()
        x[label] = pd.to_numeric(x[label], errors="coerce")
        valid_dates = []
        for cutoff, day in x.groupby("CUT_OFF", sort=True):
            if day[label].notna().sum() == 0:
                continue
            eligible = True
            for selector in SELECTORS:
                picks = day.dropna(subset=[selector]).sort_values(
                    [selector,"RANKING_SCORE","SYMBOL"], ascending=[False,False,True], kind="stable").head(WATCH_N)
                if len(picks) != WATCH_N or picks[label].isna().any():
                    eligible = False
                    break
            if eligible:
                valid_dates.append(pd.Timestamp(cutoff))
        chosen_dates = valid_dates[-REQUIRED_CUTOFFS:]
        daily = []
        for cutoff in chosen_dates:
            day = x[x["CUT_OFF"].eq(cutoff)].copy()
            labeled = day.dropna(subset=[label])
            universe_winners = int((labeled[label] >= threshold).sum())
            row = {"TARGET":target,"THRESHOLD_PCT":threshold,"CUT_OFF":cutoff.date().isoformat(),
                   "LABELED_OUTSIDE_TOP30":int(len(labeled)),"OUTSIDE_WINNERS":universe_winners}
            for selector in SELECTORS:
                picks = day.dropna(subset=[selector]).sort_values(
                    [selector,"RANKING_SCORE","SYMBOL"], ascending=[False,False,True], kind="stable").head(WATCH_N)
                hits = int((picks[label] >= threshold).sum())
                row[f"{selector}_N"] = int(len(picks))
                row[f"{selector}_HITS"] = hits
                row[f"{selector}_PRECISION"] = hits / len(picks) if len(picks) else None
                row[f"{selector}_CAPTURE"] = hits / universe_winners if universe_winners else None
            row["PRECISION_DELTA_P10_MINUS_BASE"] = row["P10_P20_MEAN_PRECISION"] - row["CURRENT_WINNER_PROB_PRECISION"]
            row["CAPTURE_DELTA_P10_MINUS_BASE"] = (
                row["P10_P20_MEAN_CAPTURE"] - row["CURRENT_WINNER_PROB_CAPTURE"]
                if row["CURRENT_WINNER_PROB_CAPTURE"] is not None and row["P10_P20_MEAN_CAPTURE"] is not None else None)
            daily.append(row)
            daily_all.append(row)
        n = len(daily)
        result = {"target":target,"threshold_pct":threshold,"required_matured_cutoffs":REQUIRED_CUTOFFS,
                  "eligible_matured_cutoffs_found":len(valid_dates),"cutoffs_tested":n,
                  "cutoff_dates":[r["CUT_OFF"] for r in daily],
                  "status":"HISTORICAL_EXPLORATORY_30_CUTOFFS_AVAILABLE" if n >= REQUIRED_CUTOFFS else "INSUFFICIENT_MATURED_CUTOFFS",
                  "selectors":{}}
        for selector in SELECTORS:
            picks_n = sum(r.get(f"{selector}_N",0) for r in daily)
            hits = sum(r.get(f"{selector}_HITS",0) for r in daily)
            captures = [r[f"{selector}_CAPTURE"] for r in daily if r[f"{selector}_CAPTURE"] is not None]
            result["selectors"][selector] = {"picks":picks_n,"hits":hits,
                "pooled_precision":hits/picks_n if picks_n else None,
                "mean_cutoff_precision":float(np.mean([r[f"{selector}_PRECISION"] for r in daily])) if daily else None,
                "mean_cutoff_capture":float(np.mean(captures)) if captures else None}
        pdelta = [r["PRECISION_DELTA_P10_MINUS_BASE"] for r in daily]
        cdelta = [r["CAPTURE_DELTA_P10_MINUS_BASE"] for r in daily if r["CAPTURE_DELTA_P10_MINUS_BASE"] is not None]
        result["paired_mean_precision_delta"] = float(np.mean(pdelta)) if pdelta else None
        result["paired_precision_delta_95pct_ci"] = ci(pdelta, rng) if pdelta else [None,None]
        result["paired_mean_capture_delta"] = float(np.mean(cdelta)) if cdelta else None
        result["paired_capture_delta_95pct_ci"] = ci(cdelta, rng) if cdelta else [None,None]
        result["promotion_authorized"] = False
        result["prospective_validation"] = False
        summaries[target] = result
    OUT.parent.mkdir(parents=True, exist_ok=True)
    DAILY.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(daily_all).to_csv(DAILY,index=False)
    report = {"status":"HISTORICAL_EXPLORATORY_ONLY","audit_type":"target-specific matured historical cutoffs; not prospective",
              "input":str(SRC),"required_cutoffs_per_target":REQUIRED_CUTOFFS,
              "selection":"Top 5 outside frozen RANKING_SCORE Top 30; both selectors must have 5 fully labeled picks on a cutoff",
              "bootstrap_repetitions":BOOTSTRAPS,"bootstrap_seed":SEED,
              "production_selector_changed":False,"production_promotion_authorized":False,
              "targets":summaries}
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,sort_keys=True))
    if any(v["cutoffs_tested"] < REQUIRED_CUTOFFS for v in summaries.values()):
        raise SystemExit("Strict 30-cutoff historical audit incomplete for one or more targets")

if __name__ == "__main__":
    main()
