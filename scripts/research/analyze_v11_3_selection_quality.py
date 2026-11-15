#!/usr/bin/env python3
"""Full scored-universe precision/recall and cost sensitivity for V11.3 research replay."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def analyze(data_path, candidate_path, signal_path, trade_path, signal_manifest_path, out_dir):
    blockers = []
    data_file, candidate_file, signal_file, trade_file = map(
        Path, [data_path, candidate_path, signal_path, trade_path]
    )
    bars = pd.read_csv(data_file)
    bars["DATE"] = pd.to_datetime(bars["DATE"], errors="raise")
    if bars.duplicated(["SYMBOL", "DATE"]).any():
        blockers.append("DUPLICATE_OHLC_SYMBOL_DATE")
    dates = sorted(bars["DATE"].drop_duplicates())
    if len(dates) != 200:
        blockers.append(f"EXPECTED_200_SESSIONS_GOT_{len(dates)}")
    date_idx = {d: i for i, d in enumerate(dates)}
    bars = bars.sort_values(["SYMBOL", "DATE"]).reset_index(drop=True)
    bars["_SESSION_IDX"] = bars["DATE"].map(date_idx).astype(int)
    raw_sha = sha256(data_file)

    candidates = pd.read_csv(candidate_file)
    candidates["CUT_OFF"] = pd.to_datetime(candidates["CUT_OFF"], errors="raise")
    candidates = candidates[
        candidates["CALIBRATION_STATUS"].eq("AVAILABLE")
        & candidates["V11_3_RESEARCH_SCORE"].notna()
    ].copy()
    candidates["SESSION_IDX"] = candidates["CUT_OFF"].map(date_idx)
    signals = pd.read_csv(signal_file)
    signals["CUT_OFF"] = pd.to_datetime(signals["CUT_OFF"], errors="raise")
    signals["SESSION_IDX"] = signals["CUT_OFF"].map(date_idx)
    trades = pd.read_csv(trade_file)
    signal_manifest = json.loads(Path(signal_manifest_path).read_text())

    if raw_sha != signal_manifest.get("input_sha256"):
        blockers.append("CANDIDATE_INPUT_SHA_MISMATCH")
    if signals.duplicated(["CUT_OFF", "SYMBOL"]).any():
        blockers.append("DUPLICATE_SIGNAL_KEY")
    if candidates.duplicated(["CUT_OFF", "SYMBOL"]).any():
        blockers.append("DUPLICATE_CANDIDATE_KEY")
    if signals.groupby("CUT_OFF").size().max() > 30:
        blockers.append("TOP30_LIMIT_EXCEEDED")
    if signals["CALIBRATION_SAMPLE_N"].isna().any() or (signals["CALIBRATION_SAMPLE_N"] < 100).any():
        blockers.append("SELECTED_SIGNAL_CALIBRATION_NOT_AVAILABLE")
    if len(trades) != len(signals) * 3:
        blockers.append("TRADE_LEDGER_NOT_SIGNALS_X3")

    # Confirm every selected signal is a member of the scored cutoff universe.
    selected_membership = signals[["CUT_OFF", "SYMBOL"]].merge(
        candidates[["CUT_OFF", "SYMBOL", "V11_3_RESEARCH_SCORE"]],
        on=["CUT_OFF", "SYMBOL"], how="left", validate="one_to_one"
    )
    if selected_membership["V11_3_RESEARCH_SCORE"].isna().any():
        blockers.append("SELECTED_SIGNAL_NOT_IN_SCORED_UNIVERSE")

    # Build forward execution outcomes for the entire scored universe using
    # the same global-session calendar and stop-first fill convention.
    n = len(bars)
    session_idx = bars["_SESSION_IDX"].to_numpy()
    group = bars.groupby("SYMBOL", sort=False)
    future = {}
    future_idx = {}
    for k in range(1, 6):
        future_idx[k] = group["_SESSION_IDX"].shift(-k).to_numpy()
        for col in ["OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE", "TTL_TRD_QNTY"]:
            future[(k, col)] = group[col].shift(-k).to_numpy(dtype=float)

    outcome_frame = pd.DataFrame({
        "CUT_OFF": bars["DATE"],
        "SYMBOL": bars["SYMBOL"].astype(str),
        "SESSION_IDX": session_idx,
    })
    horizons = [(5.0, 1), (10.0, 3), (20.0, 5)]
    for target_pct, horizon in horizons:
        valid = np.ones(n, dtype=bool)
        for k in range(1, horizon + 1):
            idxs = future_idx[k]
            valid &= np.isfinite(idxs) & (idxs == session_idx + k)
            for col in ["OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE", "TTL_TRD_QNTY"]:
                a = future[(k, col)]
                valid &= np.isfinite(a) & (a > 0)

        entry = future[(1, "OPEN_PRICE")]
        valid &= np.isfinite(entry) & (entry > 0)
        target = entry * (1 + target_pct / 100)
        stop = entry * (1 - 0.03)
        active = valid.copy()
        reason = np.full(n, "", dtype=object)
        exit_price = np.full(n, np.nan)
        for k in range(1, horizon + 1):
            o = future[(k, "OPEN_PRICE")]
            hi = future[(k, "HIGH_PRICE")]
            lo = future[(k, "LOW_PRICE")]
            close = future[(k, "CLOSE_PRICE")]
            gap = active & (o <= stop)
            reason[gap] = "STOP_GAP"
            exit_price[gap] = o[gap]
            active[gap] = False
            stop_hit = active & (lo <= stop)
            reason[stop_hit] = "STOP_LOSS"
            exit_price[stop_hit] = stop[stop_hit]
            active[stop_hit] = False
            target_hit = active & (hi >= target)
            reason[target_hit] = "TARGET"
            exit_price[target_hit] = np.maximum(target[target_hit], o[target_hit])
            active[target_hit] = False
            if k == horizon:
                remaining = active.copy()
                reason[remaining] = "HORIZON_CLOSE"
                exit_price[remaining] = close[remaining]
                active[remaining] = False

        key = f"T{int(target_pct)}_H{horizon}"
        outcome_frame[f"{key}_EXECUTABLE"] = valid
        outcome_frame[f"{key}_HIT"] = np.where(valid, reason == "TARGET", np.nan)

    universe = candidates.merge(
        outcome_frame, on=["CUT_OFF", "SYMBOL", "SESSION_IDX"],
        how="left", validate="one_to_one"
    )
    selected = signals.merge(
        outcome_frame, on=["CUT_OFF", "SYMBOL", "SESSION_IDX"],
        how="left", validate="one_to_one"
    )

    quality = []
    sensitivity = []
    for target_pct, horizon in horizons:
        key = f"T{int(target_pct)}_H{horizon}"
        exec_col, hit_col = f"{key}_EXECUTABLE", f"{key}_HIT"
        u = universe[universe[exec_col].eq(True)]
        s = selected[selected[exec_col].eq(True)]
        universe_hit = u[hit_col].astype(bool)
        selected_hit = s[hit_col].astype(bool)
        tp = int(selected_hit.sum())
        fp = int((~selected_hit).sum())
        total_winners = int(universe_hit.sum())
        fn = total_winners - tp
        tn = int(len(u) - total_winners - fp)
        precision = tp / len(s) if len(s) else None
        recall = tp / total_winners if total_winners else None
        base_rate = total_winners / len(u) if len(u) else None
        fpr = fp / (fp + tn) if (fp + tn) else None
        fdr = fp / len(s) if len(s) else None
        lift = precision / base_rate if precision is not None and base_rate else None

        trade_group = trades[
            (trades["TARGET_PCT"].astype(float) == target_pct)
            & (trades["HORIZON_SESSIONS"].astype(int) == horizon)
        ]
        executable_trades = trade_group[trade_group["EXECUTABLE"].astype(bool)]
        if len(executable_trades) != len(s):
            blockers.append(f"SELECTED_EXECUTABLE_COUNT_MISMATCH:{target_pct}:{horizon}")
        ledger_hits = int(executable_trades["TARGET_HIT"].fillna(False).astype(bool).sum())
        if ledger_hits != tp:
            blockers.append(f"SELECTED_TARGET_HIT_COUNT_MISMATCH:{target_pct}:{horizon}")

        # Non-overlapping cutoff cohorts. This is a cohort-equity proxy, not
        # a fully capital-constrained overlapping-position portfolio backtest.
        cohort = executable_trades.copy()
        cohort["SESSION_IDX"] = pd.to_datetime(cohort["CUT_OFF"]).map(date_idx)
        first_idx = int(cohort["SESSION_IDX"].min()) if len(cohort) else 0
        cohort = cohort[((cohort["SESSION_IDX"] - first_idx) % (horizon + 1)) == 0]
        cohort_returns = cohort.groupby("CUT_OFF")["NET_RETURN_PCT"].mean().sort_index()
        equity = (1 + cohort_returns / 100).cumprod()
        drawdown = (equity / equity.cummax() - 1) * 100

        quality.append({
            "TARGET_PCT": target_pct, "HORIZON_SESSIONS": horizon,
            "SCORED_UNIVERSE_ROWS": int(len(candidates)),
            "EXECUTABLE_UNIVERSE_ROWS": int(len(u)),
            "UNIVERSE_WINNERS": total_winners,
            "SELECTED_SIGNALS": int(len(trade_group)),
            "SELECTED_EXECUTABLE": int(len(s)),
            "TRUE_POSITIVES": tp, "FALSE_POSITIVES": fp,
            "MISSED_WINNERS": fn, "TRUE_NEGATIVES": tn,
            "PRECISION": precision, "RECALL": recall,
            "BASE_WINNER_RATE": base_rate, "SELECTION_LIFT": lift,
            "FALSE_POSITIVE_RATE": fpr, "FALSE_DISCOVERY_RATE": fdr,
            "NON_OVERLAPPING_COHORTS": int(len(cohort_returns)),
            "COHORT_MEAN_NET_RETURN_PCT": float(cohort_returns.mean()) if len(cohort_returns) else None,
            "COHORT_PROXY_MAX_DRAWDOWN_PCT": float(drawdown.min()) if len(drawdown) else None,
        })

        for cost in [0.0, 0.22, 0.44]:
            gross = pd.to_numeric(executable_trades["GROSS_RETURN_PCT"], errors="coerce")
            net = gross - cost
            sensitivity.append({
                "COST_PCT_POINTS": cost,
                "TARGET_PCT": target_pct, "HORIZON_SESSIONS": horizon,
                "EXECUTABLE": int(len(executable_trades)),
                "TARGET_EXIT_RATE": float(executable_trades["EXIT_REASON"].eq("TARGET").mean()) if len(executable_trades) else None,
                "MEAN_NET_RETURN_PCT": float(net.mean()) if len(net) else None,
                "MEDIAN_NET_RETURN_PCT": float(net.median()) if len(net) else None,
                "PROFITABLE_TRADE_RATE": float((net > 0).mean()) if len(net) else None,
                "NET_Q05": float(net.quantile(.05)) if len(net) else None,
                "NET_Q25": float(net.quantile(.25)) if len(net) else None,
                "NET_Q75": float(net.quantile(.75)) if len(net) else None,
                "NET_Q95": float(net.quantile(.95)) if len(net) else None,
            })

    report = {
        "status": "PASS" if not blockers else "FAIL",
        "blockers": blockers,
        "input_sha256": raw_sha,
        "candidate_sha256": sha256(candidate_file),
        "signal_sha256": sha256(signal_file),
        "trade_ledger_sha256": sha256(trade_file),
        "sessions": len(dates), "first_session": str(dates[0].date()),
        "last_session": str(dates[-1].date()),
        "scored_universe_rows": int(len(candidates)),
        "selected_signals": int(len(signals)),
        "selection_cutoffs": int(signals["CUT_OFF"].nunique()),
        "selection_quality": quality,
        "cost_sensitivity": sensitivity,
        "drawdown_note": "Cohort proxy uses non-overlapping cutoff cohorts spaced horizon+1 sessions apart; not a capital-constrained portfolio drawdown.",
        "precision_recall_note": "Universe denominator is all cutoff-symbol rows with AVAILABLE calibration and non-null V11.3 research score; outcomes require complete next global-session OHLC windows.",
    }
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    report_path = out / "v11_3_selection_quality_and_cost_sensitivity.json"
    report_path.write_text(json.dumps(report, indent=2, default=str))
    hash_path = out / "v11_3_selection_quality_sha256.json"
    hash_path.write_text(json.dumps({report_path.name: sha256(report_path)}, indent=2))
    print(json.dumps(report, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/processed/nse_eq_200_sessions.csv")
    ap.add_argument("--candidates", default="outputs/backtest/v11_3_historical_signals/v11_3_historical_calibration_audit.csv")
    ap.add_argument("--signals", default="outputs/backtest/v11_3_historical_signals/v11_3_historical_signals_top30.csv")
    ap.add_argument("--trades", default="outputs/backtest/v11_3_cost_aware_replay/cost_aware_trade_ledger.csv")
    ap.add_argument("--signal-manifest", default="outputs/backtest/v11_3_historical_signals/v11_3_historical_signal_manifest.json")
    ap.add_argument("--out", default="outputs/backtest/v11_3_selection_quality")
    a = ap.parse_args()
    analyze(a.data, a.candidates, a.signals, a.trades, a.signal_manifest, a.out)
