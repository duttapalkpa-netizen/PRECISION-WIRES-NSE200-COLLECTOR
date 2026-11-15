"""Strict forward-only outcome labels for research validation.

This module is intentionally isolated from the V11.4 production walk-forward
pipeline. It emits a label only when the complete future horizon exists.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED = {"SYMBOL", "DATE", "HIGH_PRICE", "CLOSE_PRICE"}
DEFAULT_HORIZONS = (1, 3, 5)


def add_forward_outcomes(df: pd.DataFrame, horizons=DEFAULT_HORIZONS) -> pd.DataFrame:
    """Add FUT{h}_HIGH_PCT and FUT{h}_CLOSE_PCT using exactly T+1..T+h.

    Output preserves the input row order and index. Incomplete horizons or
    invalid prices yield NaN (UNKNOWN), never a partial-horizon label.
    Duplicate symbol/date keys and invalid dates fail closed.
    """
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"missing required columns: {sorted(missing)}")
    if df["SYMBOL"].isna().any():
        raise ValueError("null SYMBOL values are not allowed")

    parsed_dates = pd.to_datetime(df["DATE"], errors="coerce")
    if parsed_dates.isna().any():
        raise ValueError("invalid DATE values; refusing implicit date repair")
    if df.assign(_DATE=parsed_dates).duplicated(["SYMBOL", "_DATE"]).any():
        raise ValueError("duplicate SYMBOL/DATE keys")

    checked_horizons = []
    for horizon in horizons:
        if isinstance(horizon, bool) or not isinstance(horizon, (int, np.integer)) or horizon <= 0:
            raise ValueError("horizons must be positive integers")
        if horizon in checked_horizons:
            raise ValueError("duplicate horizons are not allowed")
        checked_horizons.append(int(horizon))

    high = pd.to_numeric(df["HIGH_PRICE"], errors="coerce").to_numpy(dtype=float)
    close = pd.to_numeric(df["CLOSE_PRICE"], errors="coerce").to_numpy(dtype=float)
    date_values = parsed_dates.to_numpy()
    result = df.copy()

    for horizon in checked_horizons:
        high_pct = np.full(len(df), np.nan, dtype=float)
        close_pct = np.full(len(df), np.nan, dtype=float)

        groups = df.groupby("SYMBOL", sort=False, dropna=False).indices
        for positions in groups.values():
            positions = np.asarray(positions, dtype=int)
            ordered = positions[np.argsort(date_values[positions], kind="stable")]
            for offset, row_pos in enumerate(ordered):
                future_positions = ordered[offset + 1: offset + horizon + 1]
                if len(future_positions) != horizon:
                    continue
                entry_close = close[row_pos]
                future_highs = high[future_positions]
                future_closes = close[future_positions]
                if not np.isfinite(entry_close) or entry_close <= 0:
                    continue
                if (not np.isfinite(future_highs).all() or
                        not np.isfinite(future_closes).all() or
                        (future_highs <= 0).any() or (future_closes <= 0).any()):
                    continue
                high_pct[row_pos] = (future_highs.max() / entry_close - 1.0) * 100.0
                close_pct[row_pos] = (future_closes.max() / entry_close - 1.0) * 100.0

        result[f"FUT{horizon}_HIGH_PCT"] = high_pct
        result[f"FUT{horizon}_CLOSE_PCT"] = close_pct

    return result
