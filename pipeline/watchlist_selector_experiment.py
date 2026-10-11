#!/usr/bin/env python3
"""Audit-only fixed-selector comparison for the Hidden-Winner Watchlist.

The frozen RANKING_SCORE Top-30 is never altered. This script compares a
small, pre-declared set of selectors on names outside that Top-30. Historical
outcomes are used only for evaluation. Since selector ideas were explored
after seeing Run #10's holdout, retrospective comparisons are explicitly
exploratory; promotion requires a fresh prospective period.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/backtest")
TOP_N, WATCH_N = 30, 5
BOOTSTRAPS = 5000
SEED = 113
TARGETS = {
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
SCORES = {
    "CURRENT_WINNER_PROB": lambda d: d["WINNER_PROBABILITY_PCTL"],
    "P10_H3_ONLY": lambda d: d["P10_H3_PCTL"],
    "P20_H5_ONLY": lambda d: d["P20_H5_PCTL"],
    "P10_P20_MEAN": lambda d: (d["P10_H3_PCTL"] + d["P20_H5_PCTL"]) / 2,
    "P20_RARE20_BLEND": lambda d: (d["P20_H5_PCTL"] + d["RARE20_SPECIALIST_SCORE"]) / 2,
    "LATENT_RARE_SEPARATION": lambda d: (
        d["LATENT_WINNER_EVIDENCE"] + d["RARE20_SPECIALIST_SCORE"] + d["SEPARATION_SCORE"]
    ) / 3,
}
REQUIRED = {
    "CUT_OFF", "SYMBOL", "RANKING_SCORE", "WINNER_PROBABILITY_PCTL",
    "P10_H3_PCTL", "P20_H5_PCTL", "RARE20_SPECIALIST_SCORE",
    "LATENT_WINNER_EVIDENCE", "SEPARATION_SCORE",
    "FUT3_HIGH_PCT", "FUT5_HIGH_PCT",
}


def bootstrap_ci(daily, value_col, reps=BOOTSTRAPS, seed=SEED):
    """Percentile CI for a mean daily metric, resampling paired cutoff dates."""
    x = pd.to_numeric(daily[value_col], errors="coerce").dropna().to_numpy(float)
    if len(x) < 2:
        return [None, None]
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(reps, len(x)))
    means = x[idx].mean(axis=1)
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]


def main():
    if not SRC.exists():
        raise SystemExit(f"Required audit output missing: {SRC}")
    df = pd.read_csv(SRC)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SystemExit(f"Required columns missing: {sorted(missing)}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="raise")
    df = df.drop_duplicates(["CUT_OFF", "SYMBOL"]).copy()
    dates = sorted(df["CUT_OFF"].dropna().unique())
    if len(dates) < 50:
        raise SystemExit(f"Need >=50 cutoff dates; got {len(dates)}")
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(
        ascending=False, method="first"
    )
    df = df[df["RANKING_SCORE"].notna()].copy()
    outside = df[df["BASE_RANK"] > TOP_N].copy()
    train_dates, test_dates = set(dates[:70]), set(dates[-30:])
    all_picks, daily_rows, latest_rows = [], [], []

    # Select picks without consulting outcomes; score lists are fixed in code.
    for selector, score_fn in SCORES.items():
        outside["_SELECTOR_SCORE"] = score_fn(outside)
        outside["_SELECTOR_SCORE"] = pd.to_numeric(outside["_SELECTOR_SCORE"], errors="coerce")
        ordered = outside.sort_values(
            ["CUT_OFF", "_SELECTOR_SCORE", "RANKING_SCORE", "SYMBOL"],
            ascending=[True, False, False, True], kind="stable"
        )
        picks = ordered.groupby("CUT_OFF", sort=True).head(WATCH_N).copy()
        picks["SELECTOR"] = selector
        picks["WATCH_RANK"] = picks.groupby("CUT_OFF")["_SELECTOR_SCORE"].rank(
            ascending=False, method="first"
        ).astype(int)
        all_picks.append(picks)

        latest_date = pd.Timestamp(dates[-1])
        for _, row in picks[picks["CUT_OFF"] == latest_date].iterrows():
            latest_rows.append({
                "CUT_OFF": latest_date.date().isoformat(),
                "TARGET": "BOTH_TARGETS_DIAGNOSTIC",
                "SELECTOR": selector,
                "SYMBOL": row["SYMBOL"],
                "BASE_RANK": int(row["BASE_RANK"]),
                "WATCH_RANK": int(row["WATCH_RANK"]),
                "SELECTION_SCORE_VALUE": float(row["_SELECTOR_SCORE"]),
                "STATUS": "PROSPECTIVE_UNRESOLVED",
            })

        for target, (label, threshold) in TARGETS.items():
            for split, date_set in (("DEVELOPMENT_70", train_dates), ("EXPLORATORY_LAST30", test_dates)):
                target_picks = picks[picks["CUT_OFF"].isin(date_set)].copy()
                valid = target_picks[target_picks[label].notna()].copy()
                valid["_HIT"] = valid[label] >= threshold
                for cutoff, pg in valid.groupby("CUT_OFF"):
                    g = outside[(outside["CUT_OFF"] == cutoff) & outside[label].notna()]
                    top30 = df[(df["CUT_OFF"] == cutoff) & (df["BASE_RANK"] <= TOP_N) & df[label].notna()]
                    hits_universe = int((g[label] >= threshold).sum())
                    hit_watch = int(pg["_HIT"].sum())
                    hit_top30 = int((top30[label] >= threshold).sum())
                    daily_rows.append({
                        "CUT_OFF": pd.Timestamp(cutoff).date().isoformat(),
                        "SPLIT": split, "TARGET": target, "SELECTOR": selector,
                        "VALID_WATCH_N": int(len(pg)), "WATCH_HITS": hit_watch,
                        "WATCH_PRECISION": float(pg["_HIT"].mean()) if len(pg) else np.nan,
                        "TOP30_N": int(len(top30)), "TOP30_HITS": hit_top30,
                        "TOP30_PRECISION": float((top30[label] >= threshold).mean()) if len(top30) else np.nan,
                        "OUTSIDE_N": int(len(g)), "OUTSIDE_WINNERS": hits_universe,
                        "OUTSIDE_BASE_RATE": float((g[label] >= threshold).mean()) if len(g) else np.nan,
                        "WATCH_WINNER_CAPTURE": hit_watch / hits_universe if hits_universe else np.nan,
                        "WATCH_EXTRA_HITS_VS_TOP30": hit_watch - hit_top30,
                    })

    hist = pd.concat(all_picks, ignore_index=True)
    hist["FUT3_HIGH_PCT"] = hist["FUT3_HIGH_PCT"]
    hist["FUT5_HIGH_PCT"] = hist["FUT5_HIGH_PCT"]
    daily = pd.DataFrame(daily_rows)
    latest = pd.DataFrame(latest_rows)
    # Keep a clean, label-free prospective list; historical picks are a separate file.
    hist_cols = ["CUT_OFF", "SYMBOL", "SELECTOR", "WATCH_RANK", "BASE_RANK",
                 "_SELECTOR_SCORE", "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"]
    hist[hist_cols].rename(columns={"_SELECTOR_SCORE": "SELECTION_SCORE_VALUE"}).to_csv(
        OUT / "watchlist_selector_experiment_historical.csv", index=False
    )
    daily.to_csv(OUT / "watchlist_selector_experiment_daily.csv", index=False)
    latest.to_csv(OUT / "watchlist_selector_experiment_latest.csv", index=False)

    summary = {
        "status": "AUDIT_ONLY_NO_PRODUCTION_CHANGE",
        "frozen_top30_changed": False,
        "historical_cutoffs": len(dates),
        "development_cutoffs": len(train_dates),
        "exploratory_last30_cutoffs": len(test_dates),
        "important_caveat": (
            "Last-30 selector ideas were inspected during exploratory work before this formalized comparison. "
            "These retrospective figures are not a clean confirmatory holdout. Freeze a selector and assess "
            "at least 20 new matured prospective cutoffs, ideally 30, before promotion."
        ),
        "selection": f"Top {WATCH_N} outside frozen RANKING_SCORE Top {TOP_N}",
        "bootstrap": {"method": "cutoff-date bootstrap", "replicates": BOOTSTRAPS, "seed": SEED,
                      "ci": "95% percentile CI on paired daily precision/capture deltas vs CURRENT_WINNER_PROB"},
        "targets": {},
    }
    for target in TARGETS:
        summary["targets"][target] = {}
        for split in ("DEVELOPMENT_70", "EXPLORATORY_LAST30"):
            s = daily[(daily["TARGET"] == target) & (daily["SPLIT"] == split)]
            pivot = s.pivot(index="CUT_OFF", columns="SELECTOR", values="WATCH_PRECISION")
            cap = s.pivot(index="CUT_OFF", columns="SELECTOR", values="WATCH_WINNER_CAPTURE")
            base = s.groupby("CUT_OFF")["OUTSIDE_BASE_RATE"].mean()
            top30 = s.groupby("CUT_OFF")["TOP30_PRECISION"].mean()
            metrics = {}
            for selector in SCORES:
                q = s[s["SELECTOR"] == selector]
                prec = q["WATCH_PRECISION"].dropna()
                capture = q["WATCH_WINNER_CAPTURE"].dropna()
                delta_prec = (pivot[selector] - pivot["CURRENT_WINNER_PROB"]).dropna() if selector != "CURRENT_WINNER_PROB" else pd.Series([0.0])
                delta_cap = (cap[selector] - cap["CURRENT_WINNER_PROB"]).dropna() if selector != "CURRENT_WINNER_PROB" else pd.Series([0.0])
                metrics[selector] = {
                    "valid_picks": int(q["VALID_WATCH_N"].sum()),
                    "hits": int(q["WATCH_HITS"].sum()),
                    "pooled_precision": float(q["WATCH_HITS"].sum() / q["VALID_WATCH_N"].sum()) if q["VALID_WATCH_N"].sum() else None,
                    "mean_daily_precision": float(prec.mean()) if len(prec) else None,
                    "mean_daily_precision_95ci": bootstrap_ci(q, "WATCH_PRECISION"),
                    "mean_daily_capture": float(capture.mean()) if len(capture) else None,
                    "mean_daily_capture_95ci": bootstrap_ci(q, "WATCH_WINNER_CAPTURE"),
                    "mean_precision_delta_vs_current": float(delta_prec.mean()) if len(delta_prec) else None,
                    "precision_delta_95ci_vs_current": bootstrap_ci(pd.DataFrame({"delta": delta_prec}), "delta"),
                    "mean_capture_delta_vs_current": float(delta_cap.mean()) if len(delta_cap) else None,
                    "capture_delta_95ci_vs_current": bootstrap_ci(pd.DataFrame({"delta": delta_cap}), "delta"),
                    "mean_outside_base_rate": float(base.mean()) if len(base) else None,
                    "mean_top30_precision": float(top30.mean()) if len(top30) else None,
                    "acceptance_gate_pass": bool(
                        selector != "CURRENT_WINNER_PROB" and len(delta_prec) >= 20
                        and len(delta_cap) >= 20 and bootstrap_ci(pd.DataFrame({"delta": delta_prec}), "delta")[0] >= 0
                        and float(delta_cap.mean()) > 0
                    ) if selector != "CURRENT_WINNER_PROB" and len(delta_prec) >= 20 and len(delta_cap) >= 20 else False,
                }
            summary["targets"][target][split] = metrics
    (OUT / "watchlist_selector_experiment_summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
