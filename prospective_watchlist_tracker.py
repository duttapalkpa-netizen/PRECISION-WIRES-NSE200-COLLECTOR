#!/usr/bin/env python3
"""Audit-only immutable prospective watchlist ledger. Never changes ranking."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import pandas as pd

PICKS_DEFAULT = Path("outputs/prospective/latest_picks.csv")
PRICES_DEFAULT = Path("data/processed/nse_eq_200_sessions.csv")
LEDGER_DEFAULT = Path("outputs/prospective/watchlist_ledger.csv")
SELECTORS = {"CURRENT_WINNER_PROB", "P10_P20_MEAN"}
KEY = ["CUT_OFF", "SYMBOL", "SELECTOR"]
COLUMNS = [
    "CUT_OFF", "SYMBOL", "SELECTOR", "WATCH_RANK", "BASE_RANK",
    "SELECTION_SCORE_VALUE", "PICK_SOURCE_SHA256", "T1_HIGH_PCT", "T3_HIGH_PCT",
    "T5_HIGH_PCT", "T5_H1_HIT", "T10_H3_HIT", "T20_H5_HIT", "MATURED_T1",
    "MATURED_T3", "MATURED_T5", "OUTCOME_LAST_DATE",
]

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def outcome(prices: pd.DataFrame, cutoff: str, symbol: str) -> dict:
    d = prices[prices["SYMBOL"].astype(str).str.upper().eq(str(symbol).upper())].copy()
    d["DATE"] = pd.to_datetime(d["DATE"], errors="coerce")
    d = d.dropna(subset=["DATE"]).sort_values("DATE").drop_duplicates("DATE").reset_index(drop=True)
    ct = pd.to_datetime(cutoff, errors="raise")
    positions = d.index[d["DATE"].eq(ct)]
    if not len(positions):
        return {}
    i = int(positions[0])
    close = pd.to_numeric(pd.Series([d.iloc[i]["CLOSE_PRICE"]]), errors="coerce").iloc[0]
    if pd.isna(close) or close <= 0:
        return {}
    out = {}
    for h in (1, 3, 5):
        future = d.iloc[i + 1:i + h + 1]
        if len(future) < h:
            out[f"T{h}_HIGH_PCT"] = None
            out[f"MATURED_T{h}"] = False
            continue
        highs = pd.to_numeric(future["HIGH_PRICE"], errors="coerce")
        if highs.isna().any():
            out[f"T{h}_HIGH_PCT"] = None
            out[f"MATURED_T{h}"] = False
            continue
        pct = float((highs.max() / close - 1.0) * 100.0)
        out[f"T{h}_HIGH_PCT"] = pct
        out[f"MATURED_T{h}"] = True
        hit_col, threshold = {1: ("T5_H1_HIT", 5.0), 3: ("T10_H3_HIT", 10.0), 5: ("T20_H5_HIT", 20.0)}[h]
        out[hit_col] = pct >= threshold
        if h == 5:
            out["OUTCOME_LAST_DATE"] = pd.to_datetime(future.iloc[-1]["DATE"]).date().isoformat()
    return out

def run_tracker(picks_path=PICKS_DEFAULT, prices_path=PRICES_DEFAULT, ledger_path=LEDGER_DEFAULT):
    picks_path, prices_path, ledger_path = map(Path, (picks_path, prices_path, ledger_path))
    for path in (picks_path, prices_path):
        if not path.exists():
            raise SystemExit(f"Required input missing: {path}")
    picks = pd.read_csv(picks_path, dtype={"SYMBOL": str, "SELECTOR": str})
    prices = pd.read_csv(prices_path, dtype={"SYMBOL": str})
    need_picks = {"CUT_OFF", "SYMBOL", "SELECTOR", "WATCH_RANK", "BASE_RANK", "SELECTION_SCORE_VALUE"}
    need_prices = {"DATE", "SYMBOL", "CLOSE_PRICE", "HIGH_PRICE"}
    if need_picks - set(picks.columns):
        raise SystemExit(f"Picks missing columns: {sorted(need_picks - set(picks.columns))}")
    if need_prices - set(prices.columns):
        raise SystemExit(f"Prices missing columns: {sorted(need_prices - set(prices.columns))}")
    picks["CUT_OFF"] = pd.to_datetime(picks["CUT_OFF"], errors="raise").dt.date.astype(str)
    picks = picks[picks["SELECTOR"].isin(SELECTORS)].copy()
    if picks.empty:
        raise SystemExit("No rows for frozen selectors CURRENT_WINNER_PROB / P10_P20_MEAN")
    if picks.duplicated(KEY).any():
        raise SystemExit("Duplicate pick keys in latest picks input")
    src_hash = sha256_file(picks_path)
    additions = []
    for r in picks.to_dict("records"):
        additions.append({
            "CUT_OFF": r["CUT_OFF"], "SYMBOL": str(r["SYMBOL"]).upper(), "SELECTOR": r["SELECTOR"],
            "WATCH_RANK": int(r["WATCH_RANK"]), "BASE_RANK": int(r["BASE_RANK"]),
            "SELECTION_SCORE_VALUE": float(r["SELECTION_SCORE_VALUE"]), "PICK_SOURCE_SHA256": src_hash,
            "T1_HIGH_PCT": pd.NA, "T3_HIGH_PCT": pd.NA, "T5_HIGH_PCT": pd.NA,
            "T5_H1_HIT": pd.NA, "T10_H3_HIT": pd.NA, "T20_H5_HIT": pd.NA,
            "MATURED_T1": False, "MATURED_T3": False, "MATURED_T5": False, "OUTCOME_LAST_DATE": "",
        })
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger = pd.read_csv(ledger_path, dtype={"CUT_OFF": str, "SYMBOL": str, "SELECTOR": str}) if ledger_path.exists() else pd.DataFrame(columns=COLUMNS)
    for c in COLUMNS:
        if c not in ledger.columns:
            ledger[c] = pd.NA
    ledger = ledger[COLUMNS]
    if not ledger.empty and ledger.duplicated(KEY).any():
        raise SystemExit("Existing ledger has duplicate keys; refusing to mutate")
    existing = set(map(tuple, ledger[KEY].astype(str).to_numpy())) if not ledger.empty else set()
    appended = [r for r in additions if tuple(str(r[k]) for k in KEY) not in existing]
    if appended:
        ledger = pd.concat([ledger, pd.DataFrame(appended)], ignore_index=True)
    prices["DATE"] = pd.to_datetime(prices["DATE"], errors="coerce")
    prices["SYMBOL"] = prices["SYMBOL"].astype(str).str.upper()
    # Captured pick/rank/score fields are immutable. Only previously empty outcomes can mature.
    for ix, row in ledger.iterrows():
        result = outcome(prices, str(row["CUT_OFF"]), str(row["SYMBOL"]))
        if not result:
            continue
        for h in (1, 3, 5):
            pct_col, matured_col = f"T{h}_HIGH_PCT", f"MATURED_T{h}"
            value = result.get(pct_col)
            if pd.isna(row[pct_col]) and value is not None:
                ledger.at[ix, pct_col] = value
                ledger.at[ix, matured_col] = True
                hit_col = {1: "T5_H1_HIT", 3: "T10_H3_HIT", 5: "T20_H5_HIT"}[h]
                ledger.at[ix, hit_col] = bool(result[hit_col])
        if not str(row.get("OUTCOME_LAST_DATE", "")).strip() and result.get("OUTCOME_LAST_DATE"):
            ledger.at[ix, "OUTCOME_LAST_DATE"] = result["OUTCOME_LAST_DATE"]
    ledger = ledger[COLUMNS].sort_values(KEY).reset_index(drop=True)
    ledger.to_csv(ledger_path, index=False)
    unresolved = {f"T{h}": int(ledger[f"MATURED_T{h}"].astype(str).str.lower().ne("true").sum()) for h in (1, 3, 5)}
    print(f"LEDGER={ledger_path} rows={len(ledger)} appended={len(appended)} unresolved={unresolved}")
    return ledger

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--picks", default=str(PICKS_DEFAULT))
    p.add_argument("--prices", default=str(PRICES_DEFAULT))
    p.add_argument("--ledger", default=str(LEDGER_DEFAULT))
    a = p.parse_args()
    run_tracker(a.picks, a.prices, a.ledger)

if __name__ == "__main__":
    main()
