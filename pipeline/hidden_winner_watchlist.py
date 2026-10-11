#!/usr/bin/env python3
"""Audit-only Hidden-Winner Watchlist; never changes the frozen Top-30.

For each cutoff, select five names outside the fixed RANKING_SCORE Top-30,
ordered by the existing out-of-sample WINNER_PROBABILITY_PCTL (fallback:
RANKING_SCORE percentile only if that column is unavailable). Score the
watchlist as a separate list, never as Top-30 replacements. Outcomes are
used only after selection. Writes historical diagnostics and a label-free
latest-cutoff watchlist suitable for prospective tracking.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/backtest")
TOP_N = 30
WATCH_N = 5
TARGETS = {
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}


def main():
    if not SRC.exists():
        raise SystemExit(f"Required audit output missing: {SRC}")
    df = pd.read_csv(SRC)
    required = {"CUT_OFF", "SYMBOL", "RANKING_SCORE", *[v[0] for v in TARGETS.values()]}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f"Required columns missing: {sorted(missing)}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="raise")
    df = df.drop_duplicates(["CUT_OFF", "SYMBOL"]).copy()
    rank_col = "WINNER_PROBABILITY_PCTL"
    if rank_col not in df:
        # This is explicitly a fallback, not an independently discovered signal.
        rank_col = "RANKING_SCORE"
    dates = sorted(df["CUT_OFF"].dropna().unique())
    if len(dates) < 30:
        raise SystemExit(f"Need at least 30 cutoff dates; got {len(dates)}")
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(
        ascending=False, method="first"
    )
    df["WATCH_SCORE"] = df.groupby("CUT_OFF")[rank_col].rank(
        ascending=False, method="first"
    )
    daily_rows, picks = [], []
    for cutoff, g0 in df.groupby("CUT_OFF", sort=True):
        g = g0[g0["RANKING_SCORE"].notna()].copy()
        outside = g[g["BASE_RANK"] > TOP_N].copy()
        watch = outside.sort_values(
            [rank_col, "RANKING_SCORE"], ascending=[False, False], kind="stable"
        ).head(WATCH_N)
        base = g[g["BASE_RANK"] <= TOP_N]
        for _, row in watch.iterrows():
            rec = {"CUT_OFF": cutoff, "SYMBOL": row["SYMBOL"],
                   "WATCH_RANK": len(picks) + 1, "BASE_RANK": int(row["BASE_RANK"]),
                   "SELECTION_SCORE": rank_col,
                   "SELECTION_SCORE_VALUE": row.get(rank_col, np.nan)}
            # Only the historical diagnostic file contains outcomes.
            for target, (label, threshold) in TARGETS.items():
                rec[label] = row.get(label, np.nan)
                rec[target + "_HIT"] = (
                    bool(row[label] >= threshold) if pd.notna(row.get(label, np.nan)) else None
                )
            picks.append(rec)
        for target, (label, threshold) in TARGETS.items():
            valid_watch = watch[watch[label].notna()]
            valid_base = base[base[label].notna()]
            valid_universe = g[g[label].notna()]
            whits = int((valid_watch[label] >= threshold).sum())
            bhits = int((valid_base[label] >= threshold).sum())
            uhits = int((valid_universe[label] >= threshold).sum())
            daily_rows.append({
                "CUT_OFF": cutoff, "TARGET": target,
                "WATCH_N": len(valid_watch), "WATCH_HITS": whits,
                "WATCH_PRECISION": whits / len(valid_watch) if len(valid_watch) else np.nan,
                "BASELINE_TOP30_N": len(valid_base), "BASELINE_TOP30_HITS": bhits,
                "BASELINE_TOP30_PRECISION": bhits / len(valid_base) if len(valid_base) else np.nan,
                "OUTSIDE_TOP30_N": len(outside),
                "OUTSIDE_BASE_RATE": uhits / len(valid_universe) if len(valid_universe) else np.nan,
                "OUTSIDE_WINNERS": uhits,
                "WATCH_WINNER_CAPTURE": whits / uhits if uhits else np.nan,
                "WATCH_EXTRA_HITS_VS_BASELINE": whits,
                "SELECTION_SCORE": rank_col,
            })
    daily = pd.DataFrame(daily_rows)
    hist = pd.DataFrame(picks)
    daily.to_csv(OUT / "hidden_winner_watchlist_daily.csv", index=False)
    hist.to_csv(OUT / "hidden_winner_watchlist_historical_picks.csv", index=False)

    # Prospective file: latest cutoff only, and deliberately no future outcomes.
    latest_date = pd.Timestamp(dates[-1])
    latest = df[df["CUT_OFF"] == latest_date].copy()
    latest = latest[latest["RANKING_SCORE"].notna()]
    latest = latest[latest["BASE_RANK"] > TOP_N].sort_values(
        [rank_col, "RANKING_SCORE"], ascending=[False, False], kind="stable"
    ).head(WATCH_N)
    output_cols = ["CUT_OFF", "SYMBOL", "BASE_RANK", "RANKING_SCORE"]
    for col in ["WINNER_PROBABILITY_PCTL", "P10_H3_PCTL", "P20_H5_PCTL",
                "LATENT_WINNER_EVIDENCE", "RARE20_SPECIALIST_SCORE",
                "SEPARATION_SCORE", "CONTINUATION_SCORE", "EXHAUSTION_RISK"]:
        if col in latest.columns:
            output_cols.append(col)
    latest[output_cols].assign(
        WATCH_RANK=np.arange(1, len(latest) + 1),
        SELECTION_SCORE=rank_col,
        STATUS="PROSPECTIVE_UNRESOLVED",
    ).to_csv(OUT / "hidden_winner_watchlist_latest.csv", index=False)

    summary = {
        "status": "AUDIT_ONLY_NO_PRODUCTION_CHANGE",
        "selection": f"Top {WATCH_N} outside frozen RANKING_SCORE Top {TOP_N}",
        "selector": rank_col,
        "latest_cutoff": str(latest_date.date()),
        "latest_watchlist_size": int(len(latest)),
        "historical_cutoffs": int(len(dates)),
        "prospective_tracking_required": 20,
        "note": "Do not merge/promote based on retrospective results alone. Keep Top-30 unchanged; prospectively accumulate at least 20 new matured cutoffs, ideally 30.",
        "targets": {}
    }
    for target, (label, threshold) in TARGETS.items():
        d = daily[daily["TARGET"] == target]
        last30 = d[d["CUT_OFF"].isin(pd.to_datetime(dates[-30:]))]
        summary["targets"][target] = {
            "threshold_pct": threshold,
            "last30_watch_precision": float(last30["WATCH_PRECISION"].mean()),
            "last30_outside_base_rate": float(last30["OUTSIDE_BASE_RATE"].mean()),
            "last30_mean_winner_capture": float(last30["WATCH_WINNER_CAPTURE"].mean()),
            "last30_baseline_top30_precision": float(last30["BASELINE_TOP30_PRECISION"].mean()),
            "interpretation": "Descriptive only; no ranking replacement or causal claim."
        }
    (OUT / "hidden_winner_watchlist_summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
