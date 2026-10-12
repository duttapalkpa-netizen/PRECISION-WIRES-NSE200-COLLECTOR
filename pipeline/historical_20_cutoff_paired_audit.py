#!/usr/bin/env python3
"""Retrospective, strictly cutoff-grouped paired selector audit.

This reuses only point-in-time per-cutoff features/probabilities and corrected
forward labels. It is explicitly exploratory because these historical periods
were previously inspected; it does NOT count toward the prospective promotion
gate. Frozen production Top-30 remains unchanged.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/prospective/historical_20_cutoff_paired_comparison.json")
TOP_N, WATCH_N, N_CUTOFFS = 30, 5, 20
BOOTSTRAPS, SEED = 10000, 113
TARGETS = {
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
SCORE_COLS = {
    "CURRENT_WINNER_PROB": "WINNER_PROBABILITY_PCTL",
    "P10_P20_MEAN": None,
}
REQUIRED = {"CUT_OFF", "SYMBOL", "RANKING_SCORE", "WINNER_PROBABILITY_PCTL",
            "P10_H3_PCTL", "P20_H5_PCTL", "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"}


def ci_mean(x, rng, reps=BOOTSTRAPS):
    a = pd.Series(x, dtype="float64").dropna().to_numpy()
    if len(a) < 2:
        return [None, None]
    ix = rng.integers(0, len(a), size=(reps, len(a)))
    means = a[ix].mean(axis=1)
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]


def main():
    if not SRC.exists():
        raise SystemExit(f"Missing corrected walk-forward output: {SRC}")
    df = pd.read_csv(SRC)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="raise")
    df = df.drop_duplicates(["CUT_OFF", "SYMBOL"]).copy()
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(ascending=False, method="first")
    df = df[df["RANKING_SCORE"].notna()].copy()
    outside = df[df["BASE_RANK"] > TOP_N].copy()
    outside["CURRENT_WINNER_PROB"] = pd.to_numeric(outside["WINNER_PROBABILITY_PCTL"], errors="coerce")
    outside["P10_P20_MEAN"] = (pd.to_numeric(outside["P10_H3_PCTL"], errors="coerce") +
                               pd.to_numeric(outside["P20_H5_PCTL"], errors="coerce")) / 2
    all_dates = sorted(pd.Timestamp(x) for x in df["CUT_OFF"].dropna().unique())
    # Only dates where both labels are complete for the full evaluated universe count as matured.
    mature_dates = []
    for d in all_dates:
        g = df[df["CUT_OFF"].eq(d)]
        if all(g[label].notna().all() for label, _ in TARGETS.values()):
            mature_dates.append(d)
    if len(mature_dates) < N_CUTOFFS:
        raise SystemExit(f"Need {N_CUTOFFS} fully matured cutoff dates; found {len(mature_dates)}")
    dates = mature_dates[-N_CUTOFFS:]
    rng = np.random.default_rng(SEED)
    summary = {
        "status": "RETROSPECTIVE_EXPLORATORY_NOT_PROSPECTIVE",
        "production_main_changed": False,
        "cutoff_count": len(dates),
        "cutoff_start": dates[0].date().isoformat(),
        "cutoff_end": dates[-1].date().isoformat(),
        "selector_pair": ["CURRENT_WINNER_PROB", "P10_P20_MEAN"],
        "selection": "Top 5 outside frozen RANKING_SCORE Top 30 at each cutoff",
        "bootstrap": {"method": "paired cutoff-date bootstrap", "replicates": BOOTSTRAPS,
                      "seed": SEED, "ci": "95% percentile interval"},
        "caveat": "Historical cutoffs were already inspected in exploratory work. This result is not confirmatory and does not replace 20 new prospective matured cutoffs.",
        "targets": {}
    }
    daily_records = []
    for target, (label, threshold) in TARGETS.items():
        rows = []
        for d in dates:
            day = df[df["CUT_OFF"].eq(d)].copy()
            out = day[day["BASE_RANK"] > TOP_N].copy()
            n_winners = int((out[label] >= threshold).sum())
            row = {"CUT_OFF": d.date().isoformat(), "OUTSIDE_WINNERS": n_winners}
            for sel in SCORE_COLS:
                score = out[sel] if sel in out.columns else (out["P10_H3_PCTL"] + out["P20_H5_PCTL"]) / 2
                picks = out.assign(_score=score).sort_values(
                    ["_score", "RANKING_SCORE", "SYMBOL"], ascending=[False, False, True], kind="stable"
                ).head(WATCH_N)
                hits = int((picks[label] >= threshold).sum())
                row[f"{sel}_n"] = int(len(picks))
                row[f"{sel}_hits"] = hits
                row[f"{sel}_precision"] = hits / len(picks) if len(picks) else np.nan
                row[f"{sel}_capture"] = hits / n_winners if n_winners else np.nan
            rows.append(row)
            daily_records.append({"TARGET": target, **row})
        ddf = pd.DataFrame(rows)
        pdelta = (ddf["P10_P20_MEAN_precision"] - ddf["CURRENT_WINNER_PROB_precision"]).to_numpy()
        cdelta = (ddf["P10_P20_MEAN_capture"] - ddf["CURRENT_WINNER_PROB_capture"]).to_numpy()
        def metrics(sel):
            total_n = int(ddf[f"{sel}_n"].sum())
            total_hits = int(ddf[f"{sel}_hits"].sum())
            return {
                "valid_picks": total_n, "hits": total_hits,
                "pooled_precision": total_hits / total_n if total_n else None,
                "mean_daily_precision": float(ddf[f"{sel}_precision"].mean()),
                "mean_daily_capture": float(ddf[f"{sel}_capture"].dropna().mean()) if ddf[f"{sel}_capture"].notna().any() else None,
                "mean_daily_precision_95ci": ci_mean(ddf[f"{sel}_precision"], rng),
                "mean_daily_capture_95ci": ci_mean(ddf[f"{sel}_capture"], rng),
            }
        summary["targets"][target] = {
            "label": label, "threshold_pct": threshold,
            "CURRENT_WINNER_PROB": metrics("CURRENT_WINNER_PROB"),
            "P10_P20_MEAN": metrics("P10_P20_MEAN"),
            "paired_delta_P10_P20_minus_current": {
                "mean_daily_precision_delta": float(np.nanmean(pdelta)),
                "precision_delta_95ci": ci_mean(pdelta, rng),
                "mean_daily_capture_delta": float(np.nanmean(cdelta)),
                "capture_delta_95ci": ci_mean(cdelta, rng),
                "precision_point_estimate_improvement_at_least_1_percentage_point": bool(np.nanmean(pdelta) >= .01),
                "precision_ci_lower_nonnegative": bool(ci_mean(pdelta, rng)[0] is not None and ci_mean(pdelta, rng)[0] >= 0),
                "capture_not_declining": bool(np.nanmean(cdelta) >= 0),
                "production_promotion": False,
            }
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2, allow_nan=False), encoding="utf-8")
    pd.DataFrame(daily_records).to_csv(OUT.with_name("historical_20_cutoff_daily.csv"), index=False)
    print(json.dumps({"cutoffs": summary["cutoff_count"], "start": summary["cutoff_start"],
                      "end": summary["cutoff_end"], "status": summary["status"],
                      "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
