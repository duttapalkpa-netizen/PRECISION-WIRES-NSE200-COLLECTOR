#!/usr/bin/env python3
"""Exploratory walk-forward audit anchored at 2026-09-16; never promotes a selector."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/prospective/sep16_anchor_retrospective_audit.json")
DAILY = Path("outputs/prospective/sep16_anchor_retrospective_daily.csv")
ANCHOR = pd.Timestamp("2026-09-16")
MAX_CUTOFFS = 20
TOP_N, WATCH_N = 30, 5
BOOTSTRAPS, SEED = 10000, 1609
TARGETS = {
    "T5_H1": ("FUT1_HIGH_PCT", 5.0),
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
REQUIRED = {"CUT_OFF", "SYMBOL", "RANKING_SCORE", "WINNER_PROBABILITY_PCTL",
            "P10_H3_PCTL", "P20_H5_PCTL", "FUT1_HIGH_PCT",
            "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"}

def ci_mean(values, rng):
    x = pd.to_numeric(pd.Series(values), errors="coerce").dropna().to_numpy(float)
    if len(x) < 2:
        return [None, None]
    idx = rng.integers(0, len(x), size=(BOOTSTRAPS, len(x)))
    means = x[idx].mean(axis=1)
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]

def main():
    if not SRC.exists():
        raise SystemExit(f"Required input missing: {SRC}")
    df = pd.read_csv(SRC)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="coerce")
    df = df.dropna(subset=["CUT_OFF", "SYMBOL"]).drop_duplicates(["CUT_OFF", "SYMBOL"]).copy()
    observed_dates = sorted(pd.Timestamp(d) for d in df["CUT_OFF"].unique())
    in_window = [d for d in observed_dates if ANCHOR <= d <= max(observed_dates)]
    dates = in_window[:MAX_CUTOFFS]
    if not dates:
        raise SystemExit("No cutoff dates at or after the 2026-09-16 anchor")
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(ascending=False, method="first")
    df = df[df["RANKING_SCORE"].notna()].copy()
    df["CURRENT_WINNER_PROB"] = pd.to_numeric(df["WINNER_PROBABILITY_PCTL"], errors="coerce")
    df["P10_P20_MEAN"] = (pd.to_numeric(df["P10_H3_PCTL"], errors="coerce") +
                           pd.to_numeric(df["P20_H5_PCTL"], errors="coerce")) / 2
    rng = np.random.default_rng(SEED)
    daily_rows = []
    result = {
        "status": "RETROSPECTIVE_EXPLORATORY_NOT_PROSPECTIVE",
        "anchor_date": ANCHOR.date().isoformat(),
        "requested_cutoffs": MAX_CUTOFFS,
        "observed_cutoffs_in_window": len(in_window),
        "cutoffs_evaluated": len(dates),
        "cutoff_start": dates[0].date().isoformat(),
        "cutoff_end": dates[-1].date().isoformat(),
        "all_20_cutoffs_available": len(dates) >= MAX_CUTOFFS,
        "production_main_changed": False,
        "selector_pair": ["CURRENT_WINNER_PROB", "P10_P20_MEAN"],
        "selection": "Top 5 outside frozen RANKING_SCORE Top 30 per cutoff; selection before outcome evaluation",
        "maturity_rule": "For each target, evaluate only picks with complete T+1, T+3 or T+5 forward high data; unresolved outcomes are not negatives.",
        "bootstrap": {"method": "paired cutoff-date percentile bootstrap", "replicates": BOOTSTRAPS,
                      "seed": SEED, "ci": "95%"},
        "caveat": "Retrospective exploratory evidence only. These cutoffs do not count toward the 20-new-prospective-cutoff promotion gate.",
        "targets": {}
    }
    for target, (label, threshold) in TARGETS.items():
        for cutoff in dates:
            day = df[df["CUT_OFF"].eq(cutoff)].copy()
            outside = day[day["BASE_RANK"] > TOP_N].copy()
            labeled_universe = outside[outside[label].notna()]
            winner_count = int((labeled_universe[label] >= threshold).sum())
            row = {"CUT_OFF": cutoff.date().isoformat(), "TARGET": target,
                   "OUTSIDE_LABELED_N": int(len(labeled_universe)),
                   "OUTSIDE_WINNERS": winner_count,
                   "OUTSIDE_UNRESOLVED_N": int(len(outside) - len(labeled_universe))}
            for selector in ("CURRENT_WINNER_PROB", "P10_P20_MEAN"):
                picks = outside.sort_values([selector, "RANKING_SCORE", "SYMBOL"],
                    ascending=[False, False, True], kind="stable").head(WATCH_N)
                valid = picks[picks[label].notna()]
                hits = int((valid[label] >= threshold).sum())
                row[f"{selector}_SELECTED_N"] = int(len(picks))
                row[f"{selector}_VALID_N"] = int(len(valid))
                row[f"{selector}_UNRESOLVED_N"] = int(len(picks) - len(valid))
                row[f"{selector}_HITS"] = hits
                row[f"{selector}_PRECISION"] = hits / len(valid) if len(valid) else np.nan
                row[f"{selector}_CAPTURE"] = hits / winner_count if winner_count else np.nan
            daily_rows.append(row)
    daily = pd.DataFrame(daily_rows)
    for target in TARGETS:
        threshold = TARGETS[target][1]
        d = daily[daily["TARGET"].eq(target)].copy()
        paired = d.dropna(subset=["CURRENT_WINNER_PROB_PRECISION", "P10_P20_MEAN_PRECISION"])
        pdelta = paired["P10_P20_MEAN_PRECISION"] - paired["CURRENT_WINNER_PROB_PRECISION"]
        cpaired = d.dropna(subset=["CURRENT_WINNER_PROB_CAPTURE", "P10_P20_MEAN_CAPTURE"])
        cdelta = cpaired["P10_P20_MEAN_CAPTURE"] - cpaired["CURRENT_WINNER_PROB_CAPTURE"]
        metrics = {}
        for selector in ("CURRENT_WINNER_PROB", "P10_P20_MEAN"):
            valid_n = int(d[f"{selector}_VALID_N"].sum())
            hits = int(d[f"{selector}_HITS"].sum())
            prec = d[f"{selector}_PRECISION"]
            capture = d[f"{selector}_CAPTURE"]
            metrics[selector] = {
                "valid_picks": valid_n, "hits": hits,
                "pooled_precision": hits / valid_n if valid_n else None,
                "mean_daily_precision": float(prec.mean()) if prec.notna().any() else None,
                "mean_daily_capture": float(capture.mean()) if capture.notna().any() else None,
                "mean_daily_precision_95ci": ci_mean(prec, rng),
                "mean_daily_capture_95ci": ci_mean(capture, rng),
                "unresolved_picks": int(d[f"{selector}_UNRESOLVED_N"].sum())
            }
        result["targets"][target] = {
            "threshold_pct": threshold,
            "paired_cutoffs_precision": int(len(paired)),
            "paired_cutoffs_capture": int(len(cpaired)),
            "CURRENT_WINNER_PROB": metrics["CURRENT_WINNER_PROB"],
            "P10_P20_MEAN": metrics["P10_P20_MEAN"],
            "paired_delta_challenger_minus_baseline": {
                "mean_daily_precision_delta": float(pdelta.mean()) if len(pdelta) else None,
                "precision_delta_95ci": ci_mean(pdelta, rng),
                "mean_daily_capture_delta": float(cdelta.mean()) if len(cdelta) else None,
                "capture_delta_95ci": ci_mean(cdelta, rng),
                "promotion_eligible": False
            }
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, allow_nan=False), encoding="utf-8")
    daily.to_csv(DAILY, index=False)
    print(json.dumps({"status": result["status"], "anchor": result["anchor_date"],
        "cutoffs_evaluated": result["cutoffs_evaluated"], "cutoff_start": result["cutoff_start"],
        "cutoff_end": result["cutoff_end"], "all_20_cutoffs_available": result["all_20_cutoffs_available"],
        "output": str(OUT), "daily_output": str(DAILY)}, indent=2))

if __name__ == "__main__":
    main()
