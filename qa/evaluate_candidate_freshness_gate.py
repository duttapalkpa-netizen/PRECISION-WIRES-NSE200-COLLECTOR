#!/usr/bin/env python3
"""Research-only freshness readiness overlay. Never changes ranking or production selection."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import pandas as pd

ELIGIBLE = "ELIGIBLE"
NOT_ELIGIBLE = "NOT_ELIGIBLE"
UNKNOWN = "UNKNOWN"

def evaluate(universe: pd.DataFrame, candidates: pd.DataFrame):
    required_u = {"SYMBOL", "DATE"}
    required_c = {"SYMBOL", "DATE", "RISK_ADJUSTED_SCORE"}
    if not required_u.issubset(universe.columns) or not required_c.issubset(candidates.columns):
        raise ValueError("BLOCKED: required columns missing")
    u = universe.loc[:, ["SYMBOL", "DATE"]].copy()
    c = candidates.copy()
    for frame in (u, c):
        frame["SYMBOL"] = frame["SYMBOL"].astype("string").str.strip().str.upper()
        frame["DATE"] = pd.to_datetime(frame["DATE"], errors="coerce")
    if u.empty or c.empty or u[["SYMBOL", "DATE"]].isna().any().any() or c[["SYMBOL", "DATE"]].isna().any().any():
        raise ValueError("BLOCKED: empty input or invalid symbol/date")
    if u.duplicated(["SYMBOL", "DATE"]).any():
        raise ValueError("BLOCKED: duplicate universe symbol/session keys")
    sessions = pd.Index(u["DATE"].drop_duplicates().sort_values())
    latest_session = sessions.max()
    latest_by_symbol = u.groupby("SYMBOL", dropna=False)["DATE"].max()
    x = c.copy()
    x["SOURCE_LATEST_DATE"] = x["SYMBOL"].map(latest_by_symbol)
    x["CANDIDATE_DATE_MATCHES_SOURCE_LATEST"] = x["DATE"].eq(x["SOURCE_LATEST_DATE"])
    ranks = {d: i for i, d in enumerate(sessions)}
    x["DATA_LAG_SESSIONS"] = x["SOURCE_LATEST_DATE"].map(
        lambda d: int(ranks[latest_session] - ranks[d]) if pd.notna(d) and d in ranks else pd.NA
    ).astype("Int64")
    x["FRESHNESS_READINESS"] = UNKNOWN
    known = x["SOURCE_LATEST_DATE"].notna()
    x.loc[known, "FRESHNESS_READINESS"] = NOT_ELIGIBLE
    current = known & x["SOURCE_LATEST_DATE"].eq(latest_session) & x["CANDIDATE_DATE_MATCHES_SOURCE_LATEST"]
    x.loc[current, "FRESHNESS_READINESS"] = ELIGIBLE
    x["FRESHNESS_REASON"] = "SOURCE_SYMBOL_NOT_FOUND"
    x.loc[known & x["SOURCE_LATEST_DATE"].ne(latest_session), "FRESHNESS_REASON"] = "SOURCE_NOT_CURRENT_MARKET_SESSION"
    x.loc[known & x["SOURCE_LATEST_DATE"].eq(latest_session) & ~x["CANDIDATE_DATE_MATCHES_SOURCE_LATEST"], "FRESHNESS_REASON"] = "CANDIDATE_ROW_DATE_MISMATCH"
    x.loc[current, "FRESHNESS_REASON"] = "MATCHES_LATEST_MARKET_SESSION"
    report = {
        "status": "PASS_RESEARCH_READINESS_OVERLAY" if x["FRESHNESS_READINESS"].eq(ELIGIBLE).any() else "BLOCKED_NO_ELIGIBLE_CANDIDATES",
        "latest_market_session": latest_session.strftime("%Y-%m-%d"),
        "candidate_rows": int(len(x)),
        "eligible_rows": int(x["FRESHNESS_READINESS"].eq(ELIGIBLE).sum()),
        "not_eligible_rows": int(x["FRESHNESS_READINESS"].eq(NOT_ELIGIBLE).sum()),
        "unknown_rows": int(x["FRESHNESS_READINESS"].eq(UNKNOWN).sum()),
        "top_n": {},
        "ranking_preserved": True,
        "production_selector_modified": False,
        "score_modified": False,
        "core_672_modified": False,
        "note": "Research-only overlay. Input row order and all score columns are preserved; no reranking or filtering is performed."
    }
    # Top-N are assessed in the existing candidate row order; no alternate ranking is created here.
    for n in (30, 10, 3):
        top = x.head(n)
        report["top_n"][str(n)] = {
            "rows": int(len(top)),
            "eligible": int(top["FRESHNESS_READINESS"].eq(ELIGIBLE).sum()),
            "not_eligible": int(top["FRESHNESS_READINESS"].eq(NOT_ELIGIBLE).sum()),
            "unknown": int(top["FRESHNESS_READINESS"].eq(UNKNOWN).sum())
        }
    return x, report

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--universe", default="data/processed/nse_eq_200_sessions.csv")
    p.add_argument("--candidates", default="outputs/finalists/v11_3_risk_adjusted.csv")
    p.add_argument("--out", default="outputs/qa/freshness_readiness")
    a = p.parse_args()
    u = pd.read_csv(a.universe, dtype={"SYMBOL": "string", "DATE": "string"})
    c = pd.read_csv(a.candidates, dtype={"SYMBOL": "string", "DATE": "string"})
    result, report = evaluate(u, c)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    result.to_csv(out / "freshness_readiness_overlay.csv", index=False)
    (out / "freshness_readiness_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
