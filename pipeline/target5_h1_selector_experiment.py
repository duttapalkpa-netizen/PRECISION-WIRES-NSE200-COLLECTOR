#!/usr/bin/env python3
"""Audit-only target-first selector experiment for +5% within H+1.

Historical exploratory diagnostics only. Does not change the frozen ranking,
live prospective selector, or prospective ledger. All picks are selected from
the frozen RANKING_SCORE outside-Top-30 pool; outcomes are used only after picks
are determined, for retrospective evaluation.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/prospective")
TOP_N, WATCH_N, CUTOFFS = 30, 5, 30
BOOTSTRAPS, SEED = 10000, 5101
TARGET, THRESHOLD = "FUT1_HIGH_PCT", 5.0
SELECTORS = {
    "CURRENT_WINNER_PROB": lambda d: d["WINNER_PROBABILITY_PCTL"],
    "P10_P20_MEAN": lambda d: (d["P10_H3_PCTL"] + d["P20_H5_PCTL"]) / 2,
    "P5_H1_ONLY": lambda d: d["P5_H1_PCTL"],
    "P5_H1_EXHAUSTION_GUARDED": lambda d: (
        d["P5_H1_PCTL"] - 0.35 * d["EXHAUSTION_RISK"].clip(0, 100)
    ),
}
NEEDED = {
    "CUT_OFF", "SYMBOL", "RANKING_SCORE", "WINNER_PROBABILITY_PCTL",
    "P5_H1_PCTL", "P10_H3_PCTL", "P20_H5_PCTL", "EXHAUSTION_RISK",
    "FUT1_HIGH_PCT",
}


def bootstrap_ci(values, seed):
    x = np.asarray(values, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) < 2:
        return [None, None]
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(x), size=(BOOTSTRAPS, len(x)))
    means = x[ix].mean(axis=1)
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]


def main():
    if not SRC.exists():
        raise SystemExit(f"Required walk-forward output missing: {SRC}")
    df = pd.read_csv(SRC)
    missing = sorted(NEEDED - set(df.columns))
    if missing:
        raise SystemExit(f"Required columns missing: {missing}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="coerce")
    df["RANKING_SCORE"] = pd.to_numeric(df["RANKING_SCORE"], errors="coerce")
    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")
    df = df.dropna(subset=["CUT_OFF", "SYMBOL", "RANKING_SCORE"]).drop_duplicates(
        ["CUT_OFF", "SYMBOL"]
    ).copy()
    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(
        ascending=False, method="first"
    )
    outside = df[df["BASE_RANK"] > TOP_N].copy()
    for col in NEEDED - {"CUT_OFF", "SYMBOL"}:
        outside[col] = pd.to_numeric(outside[col], errors="coerce")
    valid_dates = []
    for cutoff, day in outside.groupby("CUT_OFF", sort=True):
        eligible = day.dropna(subset=[TARGET])
        if len(eligible) < WATCH_N:
            continue
        if any(day.dropna(subset=[score_fn(day).name] if hasattr(score_fn(day), "name") else []).empty
               for score_fn in []):
            continue
        if all(day.assign(_SCORE=fn(day)).dropna(subset=["_SCORE", TARGET]).shape[0] >= WATCH_N
               for fn in SELECTORS.values()):
            valid_dates.append(pd.Timestamp(cutoff))
    chosen_dates = valid_dates[-CUTOFFS:]
    if len(chosen_dates) < 10:
        raise SystemExit(f"Insufficient fully labelled historical cutoffs for exploratory audit: {len(chosen_dates)}")
    daily_rows, pick_rows = [], []
    for cutoff in chosen_dates:
        day = outside[outside["CUT_OFF"].eq(cutoff)].copy()
        labelled_universe = day.dropna(subset=[TARGET])
        winners = int((labelled_universe[TARGET] >= THRESHOLD).sum())
        row = {"CUT_OFF": cutoff.date().isoformat(), "TARGET": "T5_H1",
               "THRESHOLD_PCT": THRESHOLD, "OUTSIDE_TOP30_N": int(len(labelled_universe)),
               "OUTSIDE_TOP30_WINNERS": winners}
        for selector, score_fn in SELECTORS.items():
            candidate = day.assign(_SCORE=score_fn(day)).dropna(subset=["_SCORE", TARGET])
            picks = candidate.sort_values(
                ["_SCORE", "RANKING_SCORE", "SYMBOL"],
                ascending=[False, False, True], kind="stable"
            ).head(WATCH_N).copy()
            if len(picks) != WATCH_N:
                raise SystemExit(f"Incomplete picks at {cutoff.date()} for {selector}")
            hits = int((picks[TARGET] >= THRESHOLD).sum())
            precision = hits / WATCH_N
            capture = hits / winners if winners else np.nan
            row[f"{selector}_HITS"] = hits
            row[f"{selector}_PRECISION"] = precision
            row[f"{selector}_CAPTURE"] = capture
            for rank, (_, p) in enumerate(picks.iterrows(), 1):
                pick_rows.append({
                    "CUT_OFF": cutoff.date().isoformat(), "TARGET": "T5_H1",
                    "SELECTOR": selector, "WATCH_RANK": rank,
                    "SYMBOL": str(p["SYMBOL"]).upper(),
                    "BASE_RANK": int(p["BASE_RANK"]),
                    "SELECTOR_SCORE": float(p["_SCORE"]),
                    "FUT1_HIGH_PCT_RETROSPECTIVE": float(p[TARGET]),
                    "HIT_PLUS5_H1_RETROSPECTIVE": bool(p[TARGET] >= THRESHOLD),
                    "STATUS": "HISTORICAL_EXPLORATORY_NOT_PROSPECTIVE",
                })
        for selector in list(SELECTORS)[1:]:
            row[f"{selector}_PRECISION_DELTA_VS_BASE"] = (
                row[f"{selector}_PRECISION"] - row["CURRENT_WINNER_PROB_PRECISION"]
            )
            a, b = row[f"{selector}_CAPTURE"], row["CURRENT_WINNER_PROB_CAPTURE"]
            row[f"{selector}_CAPTURE_DELTA_VS_BASE"] = (
                a - b if np.isfinite(a) and np.isfinite(b) else np.nan
            )
        daily_rows.append(row)
    daily = pd.DataFrame(daily_rows)
    picks_df = pd.DataFrame(pick_rows)
    summaries = {}
    for selector in SELECTORS:
        p = daily[f"{selector}_PRECISION"].to_numpy(float)
        c = daily[f"{selector}_CAPTURE"].to_numpy(float)
        summaries[selector] = {
            "total_picks": int(len(chosen_dates) * WATCH_N),
            "hits": int(daily[f"{selector}_HITS"].sum()),
            "pooled_precision": float(daily[f"{selector}_HITS"].sum() / (len(chosen_dates) * WATCH_N)),
            "mean_daily_precision": float(np.nanmean(p)),
            "mean_daily_precision_95ci": bootstrap_ci(p, SEED + list(SELECTORS).index(selector)),
            "mean_daily_capture": float(np.nanmean(c)) if np.isfinite(c).any() else None,
            "mean_daily_capture_95ci": bootstrap_ci(c, SEED + 100 + list(SELECTORS).index(selector)),
        }
        if selector != "CURRENT_WINNER_PROB":
            dp = daily[f"{selector}_PRECISION_DELTA_VS_BASE"].to_numpy(float)
            dc = daily[f"{selector}_CAPTURE_DELTA_VS_BASE"].to_numpy(float)
            summaries[selector]["paired_precision_delta_vs_baseline"] = float(np.nanmean(dp))
            summaries[selector]["paired_precision_delta_95ci"] = bootstrap_ci(dp, SEED + 200 + list(SELECTORS).index(selector))
            summaries[selector]["paired_capture_delta_vs_baseline"] = float(np.nanmean(dc)) if np.isfinite(dc).any() else None
            summaries[selector]["paired_capture_delta_95ci"] = bootstrap_ci(dc, SEED + 300 + list(SELECTORS).index(selector))
    result = {
        "status": "HISTORICAL_EXPLORATORY_ONLY_NOT_PROSPECTIVE",
        "target": "T5_H1", "target_definition": "next-session high >= +5% from cutoff close",
        "selection_scope": "top 5 candidates outside frozen RANKING_SCORE Top 30",
        "matured_historical_cutoffs_used": len(chosen_dates),
        "cutoff_dates": [d.date().isoformat() for d in chosen_dates],
        "bootstrap_replicates": BOOTSTRAPS,
        "selectors": summaries,
        "guardrails": [
            "No production ranking or live selector changes",
            "No prospective ledger writes",
            "Historical labels used only for retrospective evaluation",
            "Not a claim of future 5% probability or guaranteed return",
        ],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "target5_h1_selector_experiment.json").write_text(
        json.dumps(result, indent=2, allow_nan=False), encoding="utf-8"
    )
    daily.to_csv(OUT / "target5_h1_selector_experiment_daily.csv", index=False)
    picks_df.to_csv(OUT / "target5_h1_selector_experiment_picks.csv", index=False)
    print("TARGET5_H1_AUDIT=HISTORICAL_EXPLORATORY_ONLY")
    print(f"CUTOFFS={len(chosen_dates)} SELECTORS={len(SELECTORS)}")
    for name, data in summaries.items():
        print(f"{name}: precision={data['pooled_precision']:.4f}, "
              f"mean_daily_precision={data['mean_daily_precision']:.4f}, "
              f"mean_capture={data['mean_daily_capture']}")
    return result


if __name__ == "__main__":
    main()
