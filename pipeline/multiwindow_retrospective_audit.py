#!/usr/bin/env python3
"""Multi-window retrospective selector audit; exploratory only, never promotes a selector."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

SRC = Path("outputs/backtest/walk_forward_universe_probabilities.csv")
OUT = Path("outputs/prospective/multiwindow_retrospective_audit.json")
DAILY = Path("outputs/prospective/multiwindow_retrospective_daily.csv")
ANCHOR = pd.Timestamp("2026-09-16")
WINDOW_SIZE = 20
MAX_PRE_ANCHOR_WINDOWS = 4
TOP_N, WATCH_N = 30, 5
BOOTSTRAPS, SEED = 10000, 1610
TARGETS = {
    "T5_H1": ("FUT1_HIGH_PCT", 5.0),
    "T10_H3": ("FUT3_HIGH_PCT", 10.0),
    "T20_H5": ("FUT5_HIGH_PCT", 20.0),
}
REQUIRED = {"CUT_OFF", "SYMBOL", "RANKING_SCORE", "WINNER_PROBABILITY_PCTL",
            "P10_H3_PCTL", "P20_H5_PCTL", "FUT1_HIGH_PCT",
            "FUT3_HIGH_PCT", "FUT5_HIGH_PCT"}

def bootstrap_ci(values, rng):
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
    dates = sorted(pd.Timestamp(d) for d in df["CUT_OFF"].unique())
    pre = [d for d in dates if d < ANCHOR]
    post = [d for d in dates if d >= ANCHOR]
    windows = []
    # Anchor-and-forward block first; it may be shorter than 20 if the data has fewer matured cutoffs.
    if post:
        windows.append({"window_id": "anchor_forward", "description": "2026-09-16 onward",
                        "dates": post[:WINDOW_SIZE], "requested_cutoffs": WINDOW_SIZE})
    # Walk backward in non-overlapping chunks, nearest prior block first.
    remaining = pre[:]
    for i in range(1, MAX_PRE_ANCHOR_WINDOWS + 1):
        if not remaining:
            break
        chunk = remaining[-WINDOW_SIZE:]
        remaining = remaining[:-len(chunk)]
        windows.append({"window_id": f"pre_anchor_{i}",
                        "description": f"20-session block immediately preceding {'2026-09-16' if i == 1 else f'pre_anchor_{i-1}'}",
                        "dates": chunk, "requested_cutoffs": WINDOW_SIZE})
    if not windows:
        raise SystemExit("No cutoff dates available for retrospective audit")

    df["BASE_RANK"] = df.groupby("CUT_OFF")["RANKING_SCORE"].rank(ascending=False, method="first")
    df = df[df["RANKING_SCORE"].notna()].copy()
    df["CURRENT_WINNER_PROB"] = pd.to_numeric(df["WINNER_PROBABILITY_PCTL"], errors="coerce")
    df["P10_P20_MEAN"] = (pd.to_numeric(df["P10_H3_PCTL"], errors="coerce") +
                           pd.to_numeric(df["P20_H5_PCTL"], errors="coerce")) / 2
    rng = np.random.default_rng(SEED)
    all_daily = []
    window_results = []
    for window in windows:
        window_dates = window["dates"]
        daily_rows = []
        for target, (label, threshold) in TARGETS.items():
            for cutoff in window_dates:
                day = df[df["CUT_OFF"].eq(cutoff)].copy()
                outside = day[day["BASE_RANK"] > TOP_N].copy()
                labeled = outside[outside[label].notna()]
                winners = int((labeled[label] >= threshold).sum())
                row = {"WINDOW_ID": window["window_id"], "CUT_OFF": cutoff.date().isoformat(),
                       "TARGET": target, "THRESHOLD_PCT": threshold,
                       "OUTSIDE_LABELED_N": int(len(labeled)), "OUTSIDE_WINNERS": winners,
                       "OUTSIDE_UNRESOLVED_N": int(len(outside) - len(labeled))}
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
                    row[f"{selector}_CAPTURE"] = hits / winners if winners else np.nan
                daily_rows.append(row)
        daily = pd.DataFrame(daily_rows)
        all_daily.append(daily)
        target_results = {}
        for target, (_, threshold) in TARGETS.items():
            d = daily[daily["TARGET"].eq(target)].copy()
            paired = d.dropna(subset=["CURRENT_WINNER_PROB_PRECISION", "P10_P20_MEAN_PRECISION"])
            pdelta = paired["P10_P20_MEAN_PRECISION"] - paired["CURRENT_WINNER_PROB_PRECISION"]
            cpaired = d.dropna(subset=["CURRENT_WINNER_PROB_CAPTURE", "P10_P20_MEAN_CAPTURE"])
            cdelta = cpaired["P10_P20_MEAN_CAPTURE"] - cpaired["CURRENT_WINNER_PROB_CAPTURE"]
            metrics = {}
            for selector in ("CURRENT_WINNER_PROB", "P10_P20_MEAN"):
                valid_n = int(d[f"{selector}_VALID_N"].sum())
                hits = int(d[f"{selector}_HITS"].sum())
                precision = d[f"{selector}_PRECISION"]
                capture = d[f"{selector}_CAPTURE"]
                metrics[selector] = {
                    "valid_picks": valid_n, "hits": hits,
                    "pooled_precision": hits / valid_n if valid_n else None,
                    "mean_daily_precision": float(precision.mean()) if precision.notna().any() else None,
                    "mean_daily_capture": float(capture.mean()) if capture.notna().any() else None,
                    "unresolved_picks": int(d[f"{selector}_UNRESOLVED_N"].sum())
                }
            precision_delta = float(pdelta.mean()) if len(pdelta) else None
            capture_delta = float(cdelta.mean()) if len(cdelta) else None
            p_ci = bootstrap_ci(pdelta, rng)
            c_ci = bootstrap_ci(cdelta, rng)
            target_results[target] = {
                "threshold_pct": threshold,
                "paired_cutoffs_precision": int(len(paired)),
                "paired_cutoffs_capture": int(len(cpaired)),
                "CURRENT_WINNER_PROB": metrics["CURRENT_WINNER_PROB"],
                "P10_P20_MEAN": metrics["P10_P20_MEAN"],
                "paired_delta_challenger_minus_baseline": {
                    "mean_daily_precision_delta": precision_delta,
                    "precision_delta_95ci": p_ci,
                    "mean_daily_capture_delta": capture_delta,
                    "capture_delta_95ci": c_ci,
                    "exploratory_signal_only": bool(
                        precision_delta is not None and capture_delta is not None
                        and p_ci[0] is not None and c_ci[0] is not None
                        and precision_delta > 0 and p_ci[0] > 0
                        and capture_delta >= 0 and c_ci[0] >= 0),
                    "promotion_eligible": False
                }
            }
        window_results.append({
            "window_id": window["window_id"],
            "description": window["description"],
            "requested_cutoffs": window["requested_cutoffs"],
            "cutoffs_evaluated": len(window_dates),
            "complete_20_cutoff_window": len(window_dates) == WINDOW_SIZE,
            "cutoff_start": window_dates[0].date().isoformat(),
            "cutoff_end": window_dates[-1].date().isoformat(),
            "targets": target_results
        })
    combined = pd.concat(all_daily, ignore_index=True) if all_daily else pd.DataFrame()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "status": "RETROSPECTIVE_EXPLORATORY_NOT_PROSPECTIVE",
        "anchor_date": ANCHOR.date().isoformat(),
        "window_size": WINDOW_SIZE,
        "selector_pair": ["CURRENT_WINNER_PROB", "P10_P20_MEAN"],
        "selection": "Top 5 outside frozen RANKING_SCORE Top 30 per cutoff; selection before outcome evaluation",
        "maturity_rule": "For each target, only picks with non-null target forward-high label are valid; unresolved labels are not negatives.",
        "bootstrap": {"method": "paired cutoff-date percentile bootstrap", "replicates": BOOTSTRAPS,
                      "seed": SEED, "ci": "95%"},
        "production_main_changed": False,
        "promotion_eligible": False,
        "caveat": "Historical blocks are exploratory only and never count toward the 20-new-prospective-cutoff promotion gate. Blocks may be shorter than 20 when source cutoff dates are unavailable.",
        "available_cutoff_dates": len(dates),
        "windows": window_results
    }
    OUT.write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    combined.to_csv(DAILY, index=False)
    print(json.dumps({"status": report["status"], "available_cutoff_dates": len(dates),
        "windows": [{"window_id": w["window_id"], "cutoffs_evaluated": w["cutoffs_evaluated"],
                     "cutoff_start": w["cutoff_start"], "cutoff_end": w["cutoff_end"]}
                    for w in window_results],
        "output": str(OUT), "daily_output": str(DAILY)}, indent=2))

if __name__ == "__main__":
    main()
