#!/usr/bin/env python3
"""Create truly prospective, label-free watchlists from the latest observed NSE session.

Audit branch only. Reuses the walk-forward engine's features and calibrated model,
fits only labels whose full forward horizon ended before the latest cutoff, and
never reads future outcomes for today's picks.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from pipeline import walk_forward_backtest as wf

SRC = Path("data/processed/nse_eq_200_sessions.csv")
OUT = Path("outputs/prospective/latest_picks.csv")
WATCH_N, TOP_N = 5, 30
FEATURES = ["TOMORROW_EXPANSION_SCORE", "REPRICING_PRESSURE", "READINESS",
            "NOT_YET_MOVED", "EXPANSION_READY", "EXHAUSTION", "RVOL20",
            "RS5", "RS20", "RET5", "DIST_HIGH20", "COMPRESSION", "ACCEL"]


def build_latest_picks():
    if not SRC.exists():
        raise SystemExit(f"Required normalized dataset missing: {SRC}")
    df = pd.read_csv(SRC, parse_dates=["DATE"])
    df = wf.add_features(df)
    df = wf.add_tomorrow_features(df)
    df = wf._transition_features(df)
    df = wf._robust_return_filter(df)
    df = wf.future_outcomes(df)
    dates = sorted(df["DATE"].dropna().unique())
    if len(dates) < 10:
        raise SystemExit(f"Not enough dates to form a prospective cutoff: {len(dates)}")
    cutoff = pd.Timestamp(dates[-1])
    x = df[df["DATE"].eq(cutoff)].dropna(subset=["TOMORROW_EXPANSION_SCORE"]).copy()
    x = x[x["HISTORY_DEPTH_AT_T"].fillna(0) >= 20]
    if x.empty:
        raise SystemExit(f"No eligible symbols at latest cutoff {cutoff.date()}")

    prior = df[(df["DATE"] < cutoff) & (df["HISTORY_DEPTH_AT_T"].fillna(0) >= 20)].copy()
    prior = prior[~prior["ABNORMAL_RETURN_FLAG"]].copy()
    for target, h, threshold in [("WIN5_H1", 1, 5), ("WIN10_H3", 3, 10), ("WIN20_H5", 5, 20)]:
        outcome = prior[f"FUT{h}_HIGH_PCT"]
        matured = prior[f"FUT{h}_END_DATE"].notna() & (prior[f"FUT{h}_END_DATE"] < cutoff)
        prior[target] = np.where(outcome.notna() & matured, (outcome >= threshold).astype(float), np.nan)
    train = prior.dropna(subset=FEATURES + ["WIN5_H1", "WIN10_H3", "WIN20_H5"])
    for target, col in [("WIN5_H1", "P5_H1"), ("WIN10_H3", "P10_H3"), ("WIN20_H5", "P20_H5")]:
        probs, _ = wf._calibrated_probability(train, x, target, FEATURES)
        x[col] = probs
        if x[col].isna().all():
            x[col] = x["TOMORROW_EXPANSION_SCORE"] / 100.0
    x["WINNER_PROBABILITY"] = .30*x["P5_H1"] + .40*x["P10_H3"] + .30*x["P20_H5"]
    for src, dst in [("P5_H1", "P5_H1_PCTL"), ("P10_H3", "P10_H3_PCTL"),
                     ("P20_H5", "P20_H5_PCTL"), ("WINNER_PROBABILITY", "WINNER_PROBABILITY_PCTL")]:
        x[dst] = x[src].rank(pct=True) * 100
    x["RECOVERY_SCORE"] = x.apply(wf._hidden_recovery_score, axis=1)
    x["SEPARATION_SCORE"] = x.apply(wf._distribution_separation_score, axis=1)
    x["RARE20_SPECIALIST_SCORE"] = x.apply(wf._rare20_specialist_score, axis=1)
    x["WINNER_INTERACTION_SCORE"] = x.apply(wf._winner_interaction_score, axis=1)
    scores = x.apply(wf._continuation_exhaustion_scores, axis=1)
    x["CONTINUATION_SCORE"] = [s[0] for s in scores]
    x["EXHAUSTION_RISK"] = [s[1] for s in scores]
    x["LATENT_WINNER_EVIDENCE"] = x.apply(wf._latent_winner_evidence, axis=1)
    x["STATE"] = x.apply(wf._state_transition_v4, axis=1)
    state_adj = np.select([
        x["STATE"].eq("CONTINUATION_READY"), x["STATE"].eq("HIDDEN_WINNER_RECOVERY"),
        x["STATE"].eq("EXHAUSTION"), x["STATE"].eq("FALSE_STRENGTH"),
        x["STATE"].eq("DATA_CONTAMINATED"), x["STATE"].eq("ALREADY_EXPANDED")],
        [4, 3, -10, -6, -20, -3], default=0)
    state_adj = state_adj + np.where(x["TRANSITION_SIGNATURE"].eq("PRESSURE_FADE"), 1, 0)
    x["RANKING_SCORE"] = (.4375*x["SEPARATION_SCORE"] +
                          .3750*x["RARE20_SPECIALIST_SCORE"] +
                          .1875*x["WINNER_PROBABILITY_PCTL"] + state_adj)
    x = x[x["RANKING_SCORE"].notna()].copy()
    x["BASE_RANK"] = x["RANKING_SCORE"].rank(ascending=False, method="first")
    outside = x[x["BASE_RANK"] > TOP_N].copy()
    outside["CURRENT_WINNER_PROB_SCORE"] = outside["WINNER_PROBABILITY_PCTL"]
    outside["P10_P20_MEAN_SCORE"] = (outside["P10_H3_PCTL"] + outside["P20_H5_PCTL"]) / 2
    records = []
    for selector, score_col in [("CURRENT_WINNER_PROB", "CURRENT_WINNER_PROB_SCORE"),
                                 ("P10_P20_MEAN", "P10_P20_MEAN_SCORE")]:
        chosen = outside.sort_values([score_col, "RANKING_SCORE", "SYMBOL"],
                                     ascending=[False, False, True], kind="stable").head(WATCH_N)
        for rank, (_, row) in enumerate(chosen.iterrows(), 1):
            records.append({
                "CUT_OFF": cutoff.date().isoformat(), "SYMBOL": str(row["SYMBOL"]).upper(),
                "SELECTOR": selector, "WATCH_RANK": rank, "BASE_RANK": int(row["BASE_RANK"]),
                "SELECTION_SCORE_VALUE": float(row[score_col])
            })
    result = pd.DataFrame(records)
    if result.empty or result.duplicated(["CUT_OFF", "SYMBOL", "SELECTOR"]).any():
        raise SystemExit("Live selector produced no picks or duplicate pick keys")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT, index=False)
    print(f"LIVE_CUTOFF={cutoff.date()} PICKS={len(result)} LABELS=NOT_READ FROM_FUTURE")
    return result


if __name__ == "__main__":
    build_latest_picks()
