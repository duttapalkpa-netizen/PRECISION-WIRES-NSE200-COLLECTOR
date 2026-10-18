#!/usr/bin/env python3
"""Audit-only, fixed-Top-30 precision-constrained winner-recovery experiment.

Uses only precomputed cutoff-time scores to rank candidates. Future highs are
used only for scoring outcomes after selection. Chronological 70/30 split.
Does not modify production ranking or weights.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/backtest")
OUT.mkdir(parents=True, exist_ok=True)
TOP_N = 30
TARGETS = {
    "T5_H1": ("FUT1_HIGH_PCT", 5.0),
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
BASE = "RANKING_SCORE"
SCORE_COLS = [
    BASE, "RECOVERY_SCORE", "SEPARATION_SCORE", "RARE20_SPECIALIST_SCORE",
    "WINNER_INTERACTION_SCORE", "CONTINUATION_SCORE", "LATENT_WINNER_EVIDENCE",
    "EXHAUSTION_RISK",
]


def main():
    if not SRC.exists():
        raise SystemExit(f"Required audit output missing: {SRC}")
    df = pd.read_csv(SRC)
    required = {"CUT_OFF", "SYMBOL", BASE, *[x[0] for x in TARGETS.values()]}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f"Required columns missing: {sorted(missing)}")
    df["CUT_OFF"] = pd.to_datetime(df["CUT_OFF"], errors="raise")
    df = df.drop_duplicates(["CUT_OFF", "SYMBOL"]).copy()
    dates = sorted(df["CUT_OFF"].dropna().unique())
    if len(dates) < 20:
        raise SystemExit(f"Too few cutoffs for chronological holdout: {len(dates)}")
    split_idx = max(1, min(len(dates)-1, int(len(dates)*0.70)))
    split_date = pd.Timestamp(dates[split_idx])
    df["PERIOD"] = np.where(df["CUT_OFF"] < split_date, "TRAIN70", "HOLDOUT30")

    # Within-cutoff percentile ranks prevent score-scale differences from
    # dominating blends. Missing optional diagnostics remain unavailable.
    for col in SCORE_COLS:
        if col in df:
            df[col + "_PCTL"] = df.groupby("CUT_OFF")[col].rank(pct=True, method="average")
    base = BASE + "_PCTL"
    if base not in df:
        raise SystemExit("Could not derive baseline ranking percentile")

    variants = {
        "BASELINE": base,
        "BLEND_REC20": None,
        "BLEND_REC30": None,
        "BLEND_RARE_LATENT": None,
        "BLEND_REC_RARE": None,
        "BLEND_INTERACTION_CONT": None,
        "BLEND_REC_LATENT_RISK": None,
        "BLEND_SEPARATION_REC": None,
    }
    def col(name):
        return name + "_PCTL"
    df["BLEND_REC20"] = .80*df[base] + .20*df[col("RECOVERY_SCORE")]
    df["BLEND_REC30"] = .70*df[base] + .30*df[col("RECOVERY_SCORE")]
    df["BLEND_RARE_LATENT"] = .70*df[base] + .15*df[col("RARE20_SPECIALIST_SCORE")] + .15*df[col("LATENT_WINNER_EVIDENCE")]
    df["BLEND_REC_RARE"] = .70*df[base] + .15*df[col("RECOVERY_SCORE")] + .15*df[col("RARE20_SPECIALIST_SCORE")]
    df["BLEND_INTERACTION_CONT"] = .80*df[base] + .10*df[col("WINNER_INTERACTION_SCORE")] + .10*df[col("CONTINUATION_SCORE")]
    df["BLEND_REC_LATENT_RISK"] = .70*df[base] + .15*df[col("RECOVERY_SCORE")] + .10*df[col("LATENT_WINNER_EVIDENCE")] - .05*df[col("EXHAUSTION_RISK")]
    df["BLEND_SEPARATION_REC"] = .70*df[base] + .15*df[col("SEPARATION_SCORE")] + .15*df[col("RECOVERY_SCORE")]

    # Fixed Top-30 replacement experiments: preserve the top (30-k) baseline
    # rows and replace only the bottom k slots with candidates from outside it.
    for score in [x for x in SCORE_COLS[1:] if x != "EXHAUSTION_RISK"]:
        variants["SLOT_" + score.upper()] = score + "_PCTL"
    variants.update({
        "SLOT_RECOVERY_CONFIRMED": "RECOVERY_SCORE_PCTL",
        "SLOT_RARE20_CONFIRMED": "RARE20_SPECIALIST_SCORE_PCTL",
        "SLOT_RARE20_STRICT": "RARE20_SPECIALIST_SCORE_PCTL",
        "SLOT_INTERACTION_CONFIRMED": "WINNER_INTERACTION_SCORE_PCTL",
    })
    # Baseline ranks are cutoff-local and fixed before outcomes are examined.
    df["BASE_RANK"] = df.groupby("CUT_OFF")[BASE].rank(ascending=False, method="first")
    for score in SCORE_COLS[1:]:
        df[score + "_RANK"] = df.groupby("CUT_OFF")[score].rank(ascending=False, method="first")

    records = []
    def append_selection(cutoff, period, target, strategy, k, selected, universe, threshold):
        label = TARGETS[target][0]
        valid_sel = selected[selected[label].notna()]
        valid_univ = universe[universe[label].notna()]
        if len(valid_sel) == 0 or len(valid_univ) == 0:
            return
        hits = int((valid_sel[label] >= threshold).sum())
        winners = int((valid_univ[label] >= threshold).sum())
        records.append({
            "CUT_OFF": cutoff, "PERIOD": period, "TARGET": target,
            "STRATEGY": strategy, "K": k, "SELECTED_N": len(valid_sel),
            "HITS": hits, "UNIVERSE_WINNERS": winners,
            "PRECISION": hits/len(valid_sel),
            "RECALL": hits/winners if winners else np.nan,
            "BASE_RATE": winners/len(valid_univ),
        })

    for cutoff, group in df.groupby("CUT_OFF", sort=True):
        period = group["PERIOD"].iloc[0]
        group = group[group[BASE].notna()].copy()
        baseline = group.nsmallest(TOP_N, "BASE_RANK")
        if baseline.empty:
            continue
        for target, (_, threshold) in TARGETS.items():
            universe = group
            append_selection(cutoff, period, target, "BASELINE", 0, baseline, universe, threshold)
            # Blends still return exactly Top-30.
            for name in [x for x in variants if x.startswith("BLEND_")]:
                picked = group.nlargest(TOP_N, name)
                append_selection(cutoff, period, target, name, 0, picked, universe, threshold)
            # A few predeclared replacement counts; no outcome-based selection.
            for name, score in variants.items():
                if not name.startswith("SLOT_"):
                    continue
                outside = group[group["BASE_RANK"] > TOP_N].copy()
                if name.endswith("_CONFIRMED"):
                    outside = outside[
                        (outside["CONTINUATION_SCORE_PCTL"] >= .60)
                        & (outside["EXHAUSTION_RISK_PCTL"] <= .80)
                    ]
                elif name.endswith("_STRICT"):
                    outside = outside[
                        (outside["CONTINUATION_SCORE_PCTL"] >= .75)
                        & (outside["EXHAUSTION_RISK_PCTL"] <= .65)
                        & (outside["LATENT_WINNER_EVIDENCE_PCTL"] >= .75)
                    ]
                outside = outside.sort_values(score, ascending=False, kind="stable")
                for k in (1, 3, 5):
                    if len(outside) < k:
                        continue
                    recovered = outside.head(k)
                    kept = baseline[baseline["BASE_RANK"] <= TOP_N-k]
                    selected = pd.concat([kept, recovered], axis=0).drop_duplicates(["CUT_OFF", "SYMBOL"])
                    if len(selected) == TOP_N:
                        append_selection(cutoff, period, target, name, k, selected, universe, threshold)

    daily = pd.DataFrame(records)
    if daily.empty:
        raise SystemExit("No experiment metrics were produced")
    daily.to_csv(OUT / "precision_constrained_recovery_daily.csv", index=False)

    # Paired per-cutoff differences against baseline; bootstrap confidence
    # intervals resample dates, not individual symbols.
    rng = np.random.default_rng(20261011)
    paired_rows = []
    for period in ("ALL100", "TRAIN70", "HOLDOUT30"):
        d = daily if period == "ALL100" else daily[daily["PERIOD"] == period]
        for target in TARGETS:
            base_rows = d[(d["TARGET"] == target) & (d["STRATEGY"] == "BASELINE")][
                ["CUT_OFF", "PRECISION", "RECALL", "HITS"]
            ].rename(columns={"PRECISION":"BASE_PRECISION","RECALL":"BASE_RECALL","HITS":"BASE_HITS"})
            for (strategy, k), cand in d[(d["TARGET"] == target) & (d["STRATEGY"] != "BASELINE")].groupby(["STRATEGY","K"]):
                m = cand.merge(base_rows, on="CUT_OFF", how="inner")
                if m.empty:
                    continue
                dp = (m["PRECISION"] - m["BASE_PRECISION"]).to_numpy()
                dr = (m["RECALL"] - m["BASE_RECALL"]).to_numpy()
                idx = rng.integers(0, len(m), size=(5000, len(m)))
                pboot = dp[idx].mean(axis=1)
                rboot = dr[idx].mean(axis=1)
                paired_rows.append({
                    "PERIOD": period, "TARGET": target, "STRATEGY": strategy, "K": int(k),
                    "DATES": int(len(m)),
                    "MEAN_PRECISION": float(m["PRECISION"].mean()),
                    "MEAN_RECALL": float(m["RECALL"].mean()),
                    "DELTA_PRECISION_PP": float(dp.mean()*100),
                    "PRECISION_CI_LOW_PP": float(np.quantile(pboot,.025)*100),
                    "PRECISION_CI_HIGH_PP": float(np.quantile(pboot,.975)*100),
                    "DELTA_RECALL_PP": float(dr.mean()*100),
                    "RECALL_CI_LOW_PP": float(np.quantile(rboot,.025)*100),
                    "RECALL_CI_HIGH_PP": float(np.quantile(rboot,.975)*100),
                    "PRECISION_NONWORSE_DATES": int((dp >= -1e-12).sum()),
                    "RECALL_BETTER_DATES": int((dr > 1e-12).sum()),
                })
    paired = pd.DataFrame(paired_rows)
    paired.to_csv(OUT / "precision_constrained_recovery_comparison.csv", index=False)

    # Train-only selection: require non-negative mean Precision delta and
    # positive mean Recall delta. If none qualifies, record NO_VARIANT.
    train = paired[paired["PERIOD"] == "TRAIN70"].copy()
    choices = []
    for target in TARGETS:
        q = train[train["TARGET"] == target]
        q = q[(q["DELTA_PRECISION_PP"] >= 0) & (q["DELTA_RECALL_PP"] > 0)]
        if q.empty:
            choices.append({"TARGET": target, "TRAIN_SELECTED_VARIANT": "NO_VARIANT",
                            "TRAIN_PRECISION_DELTA_PP": None, "TRAIN_RECALL_DELTA_PP": None})
        else:
            q = q.sort_values(["DELTA_RECALL_PP", "DELTA_PRECISION_PP"], ascending=False)
            r = q.iloc[0]
            choices.append({"TARGET": target, "TRAIN_SELECTED_VARIANT": str(r["STRATEGY"]),
                            "K": int(r["K"]), "TRAIN_PRECISION_DELTA_PP": float(r["DELTA_PRECISION_PP"]),
                            "TRAIN_RECALL_DELTA_PP": float(r["DELTA_RECALL_PP"])})
    summary = {
        "status": "AUDIT_ONLY",
        "top_n": TOP_N,
        "cutoffs": len(dates),
        "train_cutoffs": split_idx,
        "holdout_cutoffs": len(dates)-split_idx,
        "holdout_start": str(split_date.date()),
        "baseline_unchanged": True,
        "acceptance_rule": "On untouched chronological holdout, mean paired Recall delta > 0 and lower 95% paired date-bootstrap CI for Precision delta >= 0 for each target; no production promotion from this experiment alone.",
        "train_only_choices": choices,
        "holdout_passes_all_targets": False,
    }
    hold = paired[paired["PERIOD"] == "HOLDOUT30"]
    # Only exact variants selected on train can qualify for a pass; each must
    # pass both precision and recall guardrails on its matching holdout row.
    pass_flags = []
    for choice in choices:
        target = choice["TARGET"]
        strategy = choice["TRAIN_SELECTED_VARIANT"]
        if strategy == "NO_VARIANT":
            pass_flags.append(False); continue
        k = choice.get("K", 0)
        match = hold[(hold["TARGET"] == target) & (hold["STRATEGY"] == strategy) & (hold["K"] == k)]
        pass_flags.append(bool(len(match) and (match.iloc[0]["DELTA_RECALL_PP"] > 0)
                               and (match.iloc[0]["PRECISION_CI_LOW_PP"] >= 0)))
    summary["holdout_target_passes"] = {c["TARGET"]: bool(v) for c,v in zip(choices,pass_flags)}
    summary["holdout_passes_all_targets"] = bool(pass_flags and all(pass_flags))
    with open(OUT / "precision_constrained_recovery_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))
    print(f"Wrote {OUT / 'precision_constrained_recovery_daily.csv'}")
    print(f"Wrote {OUT / 'precision_constrained_recovery_comparison.csv'}")


if __name__ == "__main__":
    main()
