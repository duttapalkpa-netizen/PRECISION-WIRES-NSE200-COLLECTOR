#!/usr/bin/env python3
"""Cutoff-safe, research-only historical signal adapter for V11.3.

This does not import or mutate the production selector, RANKING_SCORE,
+1 PRESSURE_FADE, or CORE-672 implementation. Features are causal at cutoff T.
Historical state calibration uses only labels whose full H+3 window matured
before T. The output is a top-30-per-cutoff signal ledger for the isolated
cost-aware replay.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform

import numpy as np
import pandas as pd

from pipeline.walk_forward_backtest import add_features, add_tomorrow_features

REQUIRED = {
    "SYMBOL", "DATE", "OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE",
    "CLOSE_PRICE", "TTL_TRD_QNTY", "DELIV_PER",
}
MIN_CALIBRATION_SAMPLES = 100
TOP_N = 30
MATURATION_SESSIONS = 3
COST_PCT_POINTS = 0.22


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def signal_time_fields(cutoff):
    """Date-only as-of key; exact availability timestamp is unknown, never midnight."""
    return {"SIGNAL_AS_OF_DATE": pd.Timestamp(cutoff).date().isoformat(), "SIGNAL_TIMESTAMP": None}


def dynamic_ret20_v11_3(close_group, history_depth: pd.Series) -> pd.Series:
    """Match V11.3's ret_window=min(20, n-1) at every historical cutoff."""
    result = pd.Series(np.nan, index=history_depth.index, dtype=float)
    for window in range(1, 21):
        candidate = close_group.pct_change(window) * 100
        mask = history_depth.eq(window + 1) if window < 20 else history_depth.ge(21)
        result.loc[mask] = candidate.loc[mask]
    return result


def calibration_for_cutoff(date_state: pd.DataFrame, cutoff_idx: int,
                           min_samples: int = MIN_CALIBRATION_SAMPLES):
    """Return cutoff-safe state calibration; only outcomes matured by T count."""
    matured = date_state[date_state["SESSION_IDX"] <= cutoff_idx - MATURATION_SESSIONS]
    if matured.empty:
        return {}, {"matured_samples": 0, "eligible_states": 0, "max_rate": None}
    stats = matured.groupby("STATE", sort=True).agg(
        samples=("SAMPLES", "sum"), hits=("HITS", "sum")
    )
    stats["rate"] = stats["hits"] / stats["samples"]
    eligible = stats[stats["samples"] >= min_samples]
    if eligible.empty:
        return {}, {"matured_samples": int(stats["samples"].sum()),
                    "eligible_states": 0, "max_rate": None}
    max_rate = float(eligible["rate"].max())
    if not np.isfinite(max_rate) or max_rate <= 0:
        return {}, {"matured_samples": int(stats["samples"].sum()),
                    "eligible_states": int(len(eligible)), "max_rate": max_rate}
    mapping = {
        str(state): {
            "samples": int(row["samples"]),
            "hit_rate": float(row["rate"]),
            "calibration_score": float(np.clip(50.0 + 50.0 * row["rate"] / max_rate, 0, 100)),
        }
        for state, row in eligible.iterrows()
    }
    return mapping, {
        "matured_samples": int(stats["samples"].sum()),
        "eligible_states": int(len(eligible)),
        "max_rate": max_rate,
    }


def _validate_input(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"OHLC input missing columns: {sorted(missing)}")
    x = df.copy()
    x["DATE"] = pd.to_datetime(x["DATE"], errors="coerce")
    if x["DATE"].isna().any():
        raise ValueError("Invalid DATE values; refusing implicit date repair")
    x["SYMBOL"] = x["SYMBOL"].astype(str).str.strip().str.upper()
    if x["SYMBOL"].eq("").any():
        raise ValueError("Blank SYMBOL values")
    if x.duplicated(["SYMBOL", "DATE"]).any():
        raise ValueError("Duplicate SYMBOL/DATE keys; fail closed")
    for c in ["OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE", "TTL_TRD_QNTY"]:
        x[c] = pd.to_numeric(x[c], errors="coerce")
    o, h, l, c = (x[k] for k in ["OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE"])
    valid = (
        o.notna() & h.notna() & l.notna() & c.notna()
        & np.isfinite(o) & np.isfinite(h) & np.isfinite(l) & np.isfinite(c)
        & (o > 0) & (h > 0) & (l > 0) & (c > 0)
        & (h >= np.maximum.reduce([o.to_numpy(), l.to_numpy(), c.to_numpy()]))
        & (l <= np.minimum.reduce([o.to_numpy(), h.to_numpy(), c.to_numpy()]))
        & x["TTL_TRD_QNTY"].gt(0)
    )
    if not valid.all():
        raise ValueError(f"Invalid/non-traded OHLC rows: {int((~valid).sum())}; fail closed")
    return x.sort_values(["SYMBOL", "DATE"]).reset_index(drop=True)


def build(data_path: str, out_dir: str, min_samples: int = MIN_CALIBRATION_SAMPLES,
          top_n: int = TOP_N):
    if min_samples < 1 or top_n < 1:
        raise ValueError("min_samples and top_n must be positive integers")
    source = Path(data_path)
    raw = _validate_input(pd.read_csv(source))
    sessions = sorted(raw["DATE"].drop_duplicates())
    session_map = {d: i for i, d in enumerate(sessions)}
    raw["_SESSION_IDX"] = raw["DATE"].map(session_map).astype(int)

    # These feature builders are causal: all rolling/EMA/cross-sectional inputs
    # for row T use only observations dated <= T. Do not call future_outcomes().
    x = add_features(raw)
    x = add_tomorrow_features(x)
    x = x.sort_values(["SYMBOL", "DATE"]).reset_index(drop=True)
    g = x.groupby("SYMBOL", sort=False)
    x["HISTORY_DEPTH_AT_T"] = g.cumcount() + 1
    prior_volume = g["TTL_TRD_QNTY"].transform(
        lambda s: s.shift(1).rolling(20, min_periods=1).mean()
    )
    x["RVOL20_V11_3"] = x["TTL_TRD_QNTY"] / prior_volume.replace(0, np.nan)
    close = g["CLOSE_PRICE"]
    x["CLOSE_LOW20"] = close.transform(lambda s: s.rolling(20, min_periods=1).min())
    x["RET20_V11_3"] = dynamic_ret20_v11_3(close, x["HISTORY_DEPTH_AT_T"])
    x["ENERGY_V11_3"] = x["ENERGY"].astype(float)
    x["LEAD_TIME_V11_3"] = np.clip(
        50 + (x["RVOL20_V11_3"] - 1) * 15
        + (x["CLOSE_PRICE"] / x["EMA20"] - 1) * 500, 0, 100
    )
    x["A"] = (x["ENERGY_V11_3"] >= 60) & (x["LEAD_TIME_V11_3"] >= 60)
    x["B"] = (x["RVOL20_V11_3"] >= 1.5) & (
        x["RET20_V11_3"].isna() | (x["RET20_V11_3"] >= 2)
    )
    x["C"] = (x["CLOSE_PRICE"] >= x["EMA20"]) & (
        (x["HISTORY_DEPTH_AT_T"] < 50) | (x["CLOSE_PRICE"] >= x["EMA50"])
    )
    x["D"] = (x["CLOSE_PRICE"] >= x["EMA20"]) & (
        x["CLOSE_PRICE"] / x["CLOSE_LOW20"].replace(0, np.nan) - 1 >= 0.05
    )
    x["E"] = (~(x["A"] & x["B"] & x["C"])) & (
        (x["ENERGY_V11_3"] >= 55) | (x["LEAD_TIME_V11_3"] >= 55)
    )
    base = (
        0.25 * x["ENERGY_V11_3"]
        + 0.20 * x["LEAD_TIME_V11_3"]
        + 0.20 * np.minimum(x["RVOL20_V11_3"] * 25, 100)
        + 0.15 * x["C"].astype(float) * 100
        + 0.10 * x["D"].astype(float) * 100
        + 0.10 * x["E"].astype(float) * 100
    )
    x["BASE_SCORE_V11_3_RESEARCH"] = base
    x["BEHAVIOR_SCORE_V11_3_RESEARCH"] = x["BEHAVIOR_SCORE"].astype(float)
    x["TOMORROW_SCORE_V11_3_RESEARCH"] = x["TOMORROW_EXPANSION_SCORE"].astype(float)
    x["SESSION_IDX"] = x["_SESSION_IDX"]

    # Labels are used exclusively for historical calibration. A label is valid
    # only when the symbol has rows on each of the next 3 global market sessions.
    future_highs = []
    future_indices = []
    for k in (1, 2, 3):
        future_highs.append(g["HIGH_PRICE"].shift(-k))
        future_indices.append(g["_SESSION_IDX"].shift(-k))
    x["_FUT3_HIGH"] = pd.concat(future_highs, axis=1).max(axis=1)
    consecutive = pd.Series(True, index=x.index)
    for k, idxs in enumerate(future_indices, start=1):
        consecutive &= idxs.eq(x["_SESSION_IDX"] + k)
    x["_FUT3_LABEL_VALID"] = consecutive & x["_FUT3_HIGH"].notna()
    x["_FUT3_HIT10"] = (
        (x["_FUT3_HIGH"] / x["CLOSE_PRICE"] - 1) * 100 >= 10
    ).where(x["_FUT3_LABEL_VALID"])

    labelled = x[x["_FUT3_LABEL_VALID"]].groupby(
        ["SESSION_IDX", "STATE"], sort=True
    )["_FUT3_HIT10"].agg(SAMPLES="count", HITS="sum").reset_index()

    # For cutoff T, only labels from cutoffs <= T-3 sessions are eligible.
    coverage_rows = []
    selected_rows = []
    score_parts = []
    for idx, date in enumerate(sessions):
        mapping, stats = calibration_for_cutoff(labelled, idx, min_samples)
        day = x[x["SESSION_IDX"].eq(idx)].copy()
        day["CALIBRATION_SAMPLE_N"] = day["STATE"].map(
            {k: v["samples"] for k, v in mapping.items()}
        )
        day["CALIBRATION_HIT10_H3_RATE"] = day["STATE"].map(
            {k: v["hit_rate"] for k, v in mapping.items()}
        )
        day["CALIBRATION_SCORE"] = day["STATE"].map(
            {k: v["calibration_score"] for k, v in mapping.items()}
        )
        day["CALIBRATION_STATUS"] = np.where(
            day["CALIBRATION_SCORE"].notna(), "AVAILABLE", "UNKNOWN"
        )
        day["V11_3_RESEARCH_SCORE"] = (
            0.20 * day["BASE_SCORE_V11_3_RESEARCH"]
            + 0.20 * day["BEHAVIOR_SCORE_V11_3_RESEARCH"]
            + 0.50 * day["TOMORROW_SCORE_V11_3_RESEARCH"]
            + 0.10 * day["CALIBRATION_SCORE"]
        )
        eligible = day[day["CALIBRATION_STATUS"].eq("AVAILABLE")].copy()
        eligible = eligible.replace([np.inf, -np.inf], np.nan).dropna(
            subset=["V11_3_RESEARCH_SCORE"]
        )
        eligible = eligible.sort_values(
            ["V11_3_RESEARCH_SCORE", "TOMORROW_SCORE_V11_3_RESEARCH",
             "REPRICING_PRESSURE", "RS5", "SYMBOL"],
            ascending=[False, False, False, False, True],
            kind="mergesort",
        )
        top = eligible.head(top_n).copy()
        top["CUT_OFF"] = pd.Timestamp(date).date().isoformat()
        time_fields = signal_time_fields(date)
        top["SIGNAL_AS_OF_DATE"] = time_fields["SIGNAL_AS_OF_DATE"]
        top["SIGNAL_TIMESTAMP"] = time_fields["SIGNAL_TIMESTAMP"]
        top["SIGNAL_ENGINE"] = "V11.3_RESEARCH_CUTOFF_SAFE_ADAPTER"
        top["SIGNAL_RANK"] = np.arange(1, len(top) + 1)
        selected_rows.append(top[[
            "CUT_OFF", "SYMBOL", "SIGNAL_AS_OF_DATE", "SIGNAL_TIMESTAMP", "SIGNAL_ENGINE",
            "SIGNAL_RANK", "V11_3_RESEARCH_SCORE", "STATE",
            "CALIBRATION_SAMPLE_N", "CALIBRATION_HIT10_H3_RATE",
            "CALIBRATION_SCORE", "A", "B", "C", "D", "E",
        ]])
        coverage_rows.append({
            "CUT_OFF": pd.Timestamp(date).date().isoformat(),
            "SESSION_IDX": idx,
            "UNIVERSE_ROWS": int(len(day)),
            "CALIBRATION_AVAILABLE_ROWS": int(day["CALIBRATION_STATUS"].eq("AVAILABLE").sum()),
            "CALIBRATION_UNKNOWN_ROWS": int(day["CALIBRATION_STATUS"].eq("UNKNOWN").sum()),
            "SELECTED_TOP_N": int(len(top)),
            "MATURED_CALIBRATION_SAMPLES": stats["matured_samples"],
            "ELIGIBLE_CALIBRATION_STATES": stats["eligible_states"],
            "MAX_STATE_HIT_RATE": stats["max_rate"],
            "MIN_CALIBRATION_SAMPLES": min_samples,
        })
        score_parts.append(day[[
            "CUT_OFF" if "CUT_OFF" in day else "DATE", "SYMBOL", "STATE",
            "CALIBRATION_STATUS", "CALIBRATION_SAMPLE_N",
            "CALIBRATION_HIT10_H3_RATE", "CALIBRATION_SCORE",
            "V11_3_RESEARCH_SCORE",
        ]].rename(columns={"DATE": "CUT_OFF"}))

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    signals = pd.concat(selected_rows, ignore_index=True) if selected_rows else pd.DataFrame()
    coverage = pd.DataFrame(coverage_rows)
    signal_path = out / "v11_3_historical_signals_top30.csv"
    coverage_path = out / "v11_3_historical_signal_coverage.csv"
    calibration_path = out / "v11_3_historical_calibration_audit.csv"
    signals.to_csv(signal_path, index=False)
    coverage.to_csv(coverage_path, index=False)
    pd.concat(score_parts, ignore_index=True).to_csv(calibration_path, index=False)

    manifest = {
        "status": "PASS" if len(signals) > 0 else "BLOCKED",
        "engine": "V11.3_RESEARCH_CUTOFF_SAFE_ADAPTER",
        "input_file": str(source),
        "input_sha256": sha256(source),
        "input_rows": int(len(raw)),
        "unique_symbols": int(raw["SYMBOL"].nunique()),
        "unique_sessions": int(raw["DATE"].nunique()),
        "first_session": str(pd.Timestamp(sessions[0]).date()),
        "last_session": str(pd.Timestamp(sessions[-1]).date()),
        "signals": int(len(signals)),
        "cutoffs_with_signals": int(signals["CUT_OFF"].nunique()) if len(signals) else 0,
        "top_n_per_cutoff": top_n,
        "minimum_matured_samples_per_state": min_samples,
        "calibration_maturity_sessions": MATURATION_SESSIONS,
        "calibration_label": "next 3 consecutive global sessions HIGH excursion >=10% from cutoff CLOSE",
        "signal_timestamp_policy": "SIGNAL_AS_OF_DATE is date-only; SIGNAL_TIMESTAMP is null because exact official data-availability time is not present in input",
        "execution_convention": {
            "entry": "next global trading session OPEN",
            "target": "intraday HIGH touch",
            "stop_loss_pct": 3.0,
            "same_bar_ambiguity": "stop first",
            "no_target_exit": "horizon final-session CLOSE",
            "round_trip_cost_pct_points": COST_PCT_POINTS,
            "cost_applied": "once per completed round trip",
            "slippage": "not modelled",
        },
        "source_engine_note": "Research-only reproduction of V11.3 A/B/C/D/E feature and score structure; no production selector or RANKING_SCORE invocation.",
        "unknown_policy": "State calibration below minimum sample threshold remains UNKNOWN; no numeric calibration score or signal rank is assigned.",
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "outputs": {},
    }
    for p in [signal_path, coverage_path, calibration_path]:
        manifest["outputs"][p.name] = {"sha256": sha256(p), "bytes": p.stat().st_size}
    manifest_path = out / "v11_3_historical_signal_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, default=str))
    print(json.dumps(manifest, indent=2))
    if manifest["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/processed/nse_eq_200_sessions.csv")
    ap.add_argument("--out", default="outputs/backtest/v11_3_historical_signals")
    ap.add_argument("--min-calibration-samples", type=int, default=MIN_CALIBRATION_SAMPLES)
    ap.add_argument("--top-n", type=int, default=TOP_N)
    args = ap.parse_args()
    build(args.data, args.out, args.min_calibration_samples, args.top_n)
