#!/usr/bin/env python3
"""Independent row-level reconciliation for V11.3 cost-aware replay outputs."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

COST_PCT = 0.22
TARGETS = {(5.0, 1), (10.0, 3), (20.0, 5)}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def close(a, b, tol=1e-8):
    return a is not None and b is not None and np.isfinite(float(a)) and np.isfinite(float(b)) and abs(float(a)-float(b)) <= tol


def audit(data_path, signals_path, trade_path, metrics_path, signal_manifest_path, hash_path, out_dir):
    blockers = []
    data_file, signal_file, trade_file = map(Path, [data_path, signals_path, trade_path])
    metrics_file, signal_manifest_file, hashes_file = map(Path, [metrics_path, signal_manifest_path, hash_path])
    bars = pd.read_csv(data_file)
    bars["DATE"] = pd.to_datetime(bars["DATE"], errors="coerce")
    if bars["DATE"].isna().any():
        blockers.append("INVALID_OHLC_DATE")
    if bars.duplicated(["SYMBOL", "DATE"]).any():
        blockers.append("DUPLICATE_OHLC_SYMBOL_DATE")
    global_dates = sorted(bars["DATE"].drop_duplicates())
    date_idx = {d: i for i, d in enumerate(global_dates)}
    symbol_bars = {
        str(sym): group.set_index("DATE").to_dict("index")
        for sym, group in bars.groupby("SYMBOL", sort=False)
    }
    signals = pd.read_csv(signal_file)
    trades = pd.read_csv(trade_file)
    metrics = json.loads(metrics_file.read_text())
    signal_manifest = json.loads(signal_manifest_file.read_text())
    expected_hashes = json.loads(hashes_file.read_text())

    if sha256(data_file) != signal_manifest.get("input_sha256"):
        blockers.append("SIGNAL_MANIFEST_INPUT_SHA_MISMATCH")
    if sha256(data_file) != metrics.get("data_sha256"):
        blockers.append("BACKTEST_MANIFEST_INPUT_SHA_MISMATCH")
    if sha256(signal_file) != metrics.get("signals_sha256"):
        blockers.append("BACKTEST_MANIFEST_SIGNAL_SHA_MISMATCH")
    if sha256(trade_file) != expected_hashes.get(trade_file.name):
        blockers.append("TRADE_LEDGER_SHA_MISMATCH")
    if sha256(metrics_file) != expected_hashes.get(metrics_file.name):
        blockers.append("METRICS_SHA_MISMATCH")

    # Exact clock time is unknown for date-only OHLC inputs. Midnight must never be presented as an observed signal timestamp.
    for label, frame in [("SIGNAL", signals), ("TRADE", trades)]:
        if "SIGNAL_TIMESTAMP" not in frame.columns or frame["SIGNAL_TIMESTAMP"].notna().any():
            blockers.append(f"{label}_TIMESTAMP_MUST_REMAIN_NULL")
        if "SIGNAL_AS_OF_DATE" not in frame.columns:
            blockers.append(f"{label}_AS_OF_DATE_MISSING")
        else:
            expected_dates = pd.to_datetime(frame["CUT_OFF"], errors="coerce").dt.strftime("%Y-%m-%d")
            actual_dates = pd.to_datetime(frame["SIGNAL_AS_OF_DATE"], errors="coerce").dt.strftime("%Y-%m-%d")
            if expected_dates.isna().any() or actual_dates.isna().any() or not expected_dates.equals(actual_dates):
                blockers.append(f"{label}_AS_OF_DATE_MISMATCH")

    if signals.duplicated(["CUT_OFF", "SYMBOL"]).any():
        blockers.append("DUPLICATE_SIGNAL_CUTOFF_SYMBOL")
    if signals.empty:
        blockers.append("EMPTY_SIGNAL_LEDGER")
    if signals.groupby("CUT_OFF").size().max() > 30:
        blockers.append("TOP30_LIMIT_EXCEEDED")
    if signals["CALIBRATION_SAMPLE_N"].isna().any() or (signals["CALIBRATION_SAMPLE_N"] < 100).any():
        blockers.append("CALIBRATION_UNKNOWN_OR_BELOW_MINIMUM_IN_SELECTED_SIGNALS")
    if not signals["SIGNAL_ENGINE"].eq("V11.3_RESEARCH_CUTOFF_SAFE_ADAPTER").all():
        blockers.append("UNEXPECTED_SIGNAL_ENGINE")
    if trades.duplicated(["CUT_OFF", "SYMBOL", "TARGET_PCT", "HORIZON_SESSIONS"]).any():
        blockers.append("DUPLICATE_TRADE_KEY")
    if len(trades) != len(signals) * 3:
        blockers.append("TRADE_ROWS_DO_NOT_EQUAL_SIGNALS_X3")
    if set(zip(trades["TARGET_PCT"].astype(float), trades["HORIZON_SESSIONS"].astype(int))) != TARGETS:
        blockers.append("TARGET_HORIZON_SET_MISMATCH")

    executable_count = 0
    excluded_count = 0
    arithmetic_errors = 0
    execution_errors = 0
    exclusion_errors = 0
    for row in trades.itertuples(index=False):
        if not bool(row.EXECUTABLE):
            excluded_count += 1
            if any(pd.notna(getattr(row, k)) for k in [
                "ENTRY_PRICE", "EXIT_PRICE", "GROSS_RETURN_PCT", "NET_RETURN_PCT",
                "ENTRY_SESSION", "EXIT_SESSION"
            ]):
                exclusion_errors += 1
            if row.ENTRY_STATUS not in {"SYMBOL_SESSION_MISSING", "HORIZON_NOT_MATURED",
                                         "CUTOFF_SYMBOL_ROW_MISSING", "INVALID_OR_NONTRADED_OHLC",
                                         "INVALID_ENTRY_PRICE", "DUPLICATE_SYMBOL_DATE"}:
                exclusion_errors += 1
            continue

        executable_count += 1
        cutoff = pd.Timestamp(row.CUT_OFF)
        symbol = str(row.SYMBOL)
        horizon = int(row.HORIZON_SESSIONS)
        target_pct = float(row.TARGET_PCT)
        if cutoff not in date_idx or symbol not in symbol_bars:
            execution_errors += 1
            continue
        idx = date_idx[cutoff]
        window = global_dates[idx + 1:idx + 1 + horizon]
        if len(window) != horizon:
            execution_errors += 1
            continue
        sb = symbol_bars[symbol]
        if any(d not in sb for d in window):
            execution_errors += 1
            continue

        entry_date = window[0]
        entry_price = float(sb[entry_date]["OPEN_PRICE"])
        if not close(row.ENTRY_PRICE, entry_price) or pd.Timestamp(row.ENTRY_SESSION) != entry_date:
            execution_errors += 1
            continue
        target = entry_price * (1 + target_pct / 100)
        stop = entry_price * (1 - 3.0 / 100)
        exit_price = None
        exit_date = None
        reason = None
        for d in window:
            o = float(sb[d]["OPEN_PRICE"])
            h = float(sb[d]["HIGH_PRICE"])
            l = float(sb[d]["LOW_PRICE"])
            if o <= stop:
                exit_price, exit_date, reason = o, d, "STOP_GAP"
                break
            stop_hit = l <= stop
            target_hit = h >= target
            if stop_hit:
                exit_price, exit_date, reason = stop, d, "STOP_LOSS"
                break
            if target_hit:
                exit_price = max(target, o) if o >= target else target
                exit_date, reason = d, "TARGET"
                break
        if exit_price is None:
            exit_price = float(sb[window[-1]]["CLOSE_PRICE"])
            exit_date, reason = window[-1], "HORIZON_CLOSE"

        gross = (exit_price / entry_price - 1) * 100
        net = gross - COST_PCT
        if (str(row.EXIT_REASON) != reason or pd.Timestamp(row.EXIT_SESSION) != exit_date
            or not close(row.EXIT_PRICE, exit_price)
            or not close(row.GROSS_RETURN_PCT, gross)
            or not close(row.COST_PCT, COST_PCT)
            or not close(row.NET_RETURN_PCT, net)):
            execution_errors += 1
        if bool(row.TARGET_HIT) != (reason == "TARGET" and net >= 0):
            execution_errors += 1
        if bool(row.STOP_HIT) != reason.startswith("STOP"):
            execution_errors += 1
        if not close(row.NET_RETURN_PCT, float(row.GROSS_RETURN_PCT) - COST_PCT):
            arithmetic_errors += 1

    if execution_errors:
        blockers.append(f"EXECUTION_RECONCILIATION_ERRORS:{execution_errors}")
    if arithmetic_errors:
        blockers.append(f"NET_ARITHMETIC_ERRORS:{arithmetic_errors}")
    if exclusion_errors:
        blockers.append(f"EXCLUSION_POLICY_ERRORS:{exclusion_errors}")

    recomputed = []
    stored = {(float(m["TARGET_PCT"]), int(m["HORIZON_SESSIONS"])): m for m in metrics["metrics"]}
    for target, horizon in sorted(TARGETS):
        group = trades[(trades["TARGET_PCT"].astype(float) == target)
                       & (trades["HORIZON_SESSIONS"].astype(int) == horizon)]
        ex = group[group["EXECUTABLE"].astype(bool)]
        gross = pd.to_numeric(ex["GROSS_RETURN_PCT"], errors="coerce")
        net = pd.to_numeric(ex["NET_RETURN_PCT"], errors="coerce").dropna()
        gross_hit_count = int((gross >= target - 1e-8).sum())
        target_exit_count = int(ex["EXIT_REASON"].eq("TARGET").sum())
        calc = {
            "TARGET_PCT": target, "HORIZON_SESSIONS": horizon,
            "SIGNALS": int(len(group)), "EXECUTABLE": int(len(ex)),
            "EXCLUDED": int((~group["EXECUTABLE"].astype(bool)).sum()),
            "GROSS_HIT_COUNT": gross_hit_count,
            "GROSS_HIT_RATE": float(gross_hit_count / len(ex)) if len(ex) else None,
            "TARGET_EXIT_COUNT": target_exit_count,
            "TARGET_EXIT_RATE": float(target_exit_count / len(ex)) if len(ex) else None,
            "MEAN_NET_RETURN_PCT": float(net.mean()) if len(net) else None,
            "MEDIAN_NET_RETURN_PCT": float(net.median()) if len(net) else None,
            "NET_Q05": float(net.quantile(.05)) if len(net) else None,
            "NET_Q25": float(net.quantile(.25)) if len(net) else None,
            "NET_Q75": float(net.quantile(.75)) if len(net) else None,
            "NET_Q95": float(net.quantile(.95)) if len(net) else None,
        }
        recomputed.append(calc)
        original = stored.get((target, horizon), {})
        for key in ["SIGNALS", "EXECUTABLE", "EXCLUDED", "GROSS_HIT_COUNT", "TARGET_EXIT_COUNT"]:
            if key in original and int(original[key]) != int(calc[key]):
                blockers.append(f"METRIC_COUNT_MISMATCH:{target}:{horizon}:{key}")
        for key in ["GROSS_HIT_RATE", "TARGET_EXIT_RATE", "MEAN_NET_RETURN_PCT", "MEDIAN_NET_RETURN_PCT"]:
            if key in original and original[key] is not None and not close(original[key], calc[key], 1e-9):
                blockers.append(f"METRIC_VALUE_MISMATCH:{target}:{horizon}:{key}")

    report = {
        "status": "PASS" if not blockers else "FAIL",
        "blockers": blockers,
        "input_sha256": sha256(data_file),
        "signals_sha256": sha256(signal_file),
        "trade_ledger_sha256": sha256(trade_file),
        "metrics_sha256": sha256(metrics_file),
        "signal_rows": int(len(signals)),
        "signal_cutoffs": int(signals["CUT_OFF"].nunique()),
        "trade_rows": int(len(trades)),
        "executable_rows": executable_count,
        "excluded_rows": excluded_count,
        "execution_reconciliation_errors": execution_errors,
        "net_arithmetic_errors": arithmetic_errors,
        "exclusion_policy_errors": exclusion_errors,
        "recomputed_metrics": recomputed,
    }
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    report_path = out / "independent_replay_audit.json"
    report_path.write_text(json.dumps(report, indent=2, default=str))
    (out / "independent_replay_audit_sha256.json").write_text(
        json.dumps({report_path.name: sha256(report_path)}, indent=2)
    )
    print(json.dumps(report, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--signals", required=True)
    ap.add_argument("--trades", required=True)
    ap.add_argument("--metrics", required=True)
    ap.add_argument("--signal-manifest", required=True)
    ap.add_argument("--hashes", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    audit(a.data, a.signals, a.trades, a.metrics, a.signal_manifest, a.hashes, a.out)
