#!/usr/bin/env python3
"""Fail-closed, read-only provenance reconciliation for alternate-source leads.

The source news ledger is never overwritten. A verified alternate publisher page
is only linked to a ledger row when cutoff, symbol, original timestamp, headline,
and original URL all match the ledger's own fields. Otherwise the row stays an
unmatched discovery lead and research readiness remains blocked.
"""
from pathlib import Path
import json
import pandas as pd

LEDGER = Path("data/raw/stock_news_events.csv")
COVERAGE = Path("data/raw/stock_news_coverage.csv")
CANDIDATES = Path("artifact/outputs/news_24h/stock_news_alternate_source_candidates.csv")
VERIFIED = Path("outputs/news_24h/alternate_source_verification_results.csv")
RESOLVED = Path("outputs/news_24h/alternate_source_resolution_join.csv")
READINESS = Path("outputs/news_24h/stock_news_24h_readiness.json")
OUT = Path("outputs/news_24h/stock_news_ledger_reconciliation.json")
CSV = Path("outputs/news_24h/stock_news_ledger_reconciliation.csv")

def norm_date(s):
    return pd.to_datetime(s, errors="coerce").dt.date.astype("string")

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    required = [LEDGER, COVERAGE, CANDIDATES, VERIFIED, RESOLVED, READINESS]
    missing_files = [str(p) for p in required if not p.is_file()]
    if missing_files:
        report = {"status":"BLOCKED_MISSING_INPUTS","missing_files":missing_files,
                  "ledger_rows":None,"coverage_rows":None,"candidate_rows":None,
                  "matched_ledger_rows":0,"research_status":"BLOCKED",
                  "source_ledger_modified":False}
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("NEWS_LEDGER_RECONCILIATION=" + json.dumps(report, sort_keys=True))
        raise SystemExit(2)
    ledger = pd.read_csv(LEDGER, dtype=str).fillna("")
    coverage = pd.read_csv(COVERAGE, dtype=str).fillna("")
    candidates = pd.read_csv(CANDIDATES, dtype=str).fillna("")
    verified = pd.read_csv(VERIFIED, dtype=str).fillna("")
    resolved = pd.read_csv(RESOLVED, dtype=str).fillna("")
    readiness = json.loads(READINESS.read_text(encoding="utf-8"))
    ledger_required = {"CUT_OFF","SYMBOL","PUBLISHED_AT","HEADLINE","CANONICAL_URL","VERIFICATION_STATUS"}
    candidate_required = {"CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL","SOURCE_ROW_INDEX"}
    missing_ledger = sorted(ledger_required - set(ledger.columns))
    missing_candidate = sorted(candidate_required - set(candidates.columns))
    if missing_ledger or missing_candidate:
        report = {"status":"BLOCKED_BAD_SCHEMA","missing_ledger_columns":missing_ledger,
                  "missing_candidate_columns":missing_candidate,"ledger_rows":len(ledger),
                  "coverage_rows":len(coverage),"candidate_rows":len(candidates),
                  "matched_ledger_rows":0,"research_status":"BLOCKED",
                  "source_ledger_modified":False}
        OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("NEWS_LEDGER_RECONCILIATION=" + json.dumps(report, sort_keys=True))
        raise SystemExit(2)
    # Preserve source fields; use normalized temporary comparison keys only.
    l = ledger.copy()
    c = candidates.copy()
    l["_cut"] = norm_date(l["CUT_OFF"])
    c["_cut"] = norm_date(c["CUT_OFF"])
    l["_symbol"] = l["SYMBOL"].str.upper().str.strip()
    c["_symbol"] = c["SYMBOL"].str.upper().str.strip()
    l["_published"] = pd.to_datetime(l["PUBLISHED_AT"], utc=True, errors="coerce", format="mixed").astype("string")
    c["_published"] = pd.to_datetime(c["ORIGINAL_PUBLISHED_AT"], utc=True, errors="coerce", format="mixed").astype("string")
    l["_headline"] = l["HEADLINE"].str.strip()
    c["_headline"] = c["ORIGINAL_HEADLINE"].str.strip()
    l["_url"] = l["CANONICAL_URL"].str.strip()
    c["_url"] = c["ORIGINAL_URL"].str.strip()
    keys = ["_cut","_symbol","_published","_headline","_url"]
    # Many ledger rows may be duplicate source observations; duplicates are reported, never silently selected.
    counts = l.groupby(keys, dropna=False).size().rename("_ledger_match_count").reset_index()
    j = c.merge(counts, on=keys, how="left", validate="many_to_one")
    j["_ledger_match_count"] = j["_ledger_match_count"].fillna(0).astype(int)
    j["LEDGER_RECONCILIATION_STATUS"] = j["_ledger_match_count"].map(
        lambda n: "EXACT_UNIQUE_LEDGER_MATCH" if n == 1 else ("AMBIGUOUS_DUPLICATE_LEDGER_MATCH" if n > 1 else "NO_EXACT_LEDGER_MATCH"))
    # Explicitly report verified RACE/RIIL rows; no promotion or source-field mutation occurs here.
    focus = j[j["SYMBOL"].str.upper().isin(["RACE","RIIL"])].copy()
    focus["VERIFICATION_STATUS"] = ""
    if "VERIFICATION_STATUS" in verified.columns:
        join_keys = [k for k in ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL"] if k in verified.columns and k in focus.columns]
        if join_keys:
            v = verified[join_keys + ["VERIFICATION_STATUS"]].drop_duplicates()
            focus = focus.drop(columns=["VERIFICATION_STATUS"]).merge(v, on=join_keys, how="left", validate="many_to_one")
    focus_cols = [x for x in ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL","ALTERNATE_ARTICLE_URL","VERIFICATION_STATUS","_ledger_match_count","LEDGER_RECONCILIATION_STATUS"] if x in focus.columns]
    focus[focus_cols].to_csv(CSV, index=False)
    expected_pairs = int(len(pd.read_csv("outputs/news_24h/stock_news_24h_cutoff_join.csv", dtype=str).drop_duplicates(["CUT_OFF","SYMBOL"]))) if Path("outputs/news_24h/stock_news_24h_cutoff_join.csv").is_file() else None
    ready_pairs = readiness.get("unique_cutoff_symbol_pairs")
    join_rows = readiness.get("cutoff_symbol_rows")
    count_consistent = (expected_pairs is None or ready_pairs == expected_pairs) and (join_rows is None or int(join_rows) >= 0)
    unmatched = int((j["_ledger_match_count"] == 0).sum())
    ambiguous = int((j["_ledger_match_count"] > 1).sum())
    report = {
        "status": "PASS_LEDGER_RECONCILIATION" if unmatched == 0 and ambiguous == 0 and count_consistent else "BLOCKED_LEDGER_RECONCILIATION",
        "ledger_rows": int(len(ledger)), "coverage_rows": int(len(coverage)),
        "candidate_rows": int(len(candidates)), "verified_rows": int(verified.get("VERIFICATION_STATUS", pd.Series(dtype=str)).astype(str).str.upper().eq("VERIFIED").sum()),
        "matched_ledger_rows": int((j["_ledger_match_count"] == 1).sum()),
        "unmatched_candidate_rows": unmatched, "ambiguous_candidate_rows": ambiguous,
        "race_riil_candidate_rows": int(len(focus)),
        "race_riil_exact_unique_matches": int(focus["LEDGER_RECONCILIATION_STATUS"].eq("EXACT_UNIQUE_LEDGER_MATCH").sum()),
        "readiness_cutoff_symbol_rows": join_rows, "readiness_unique_cutoff_symbol_pairs": ready_pairs,
        "recomputed_join_unique_pairs": expected_pairs, "readiness_pair_counts_consistent": bool(count_consistent),
        "readiness_status": readiness.get("status"), "research_status": "BLOCKED",
        "join_keys": ["cutoff date","symbol","original published timestamp","original headline","original canonical URL"],
        "source_ledger_modified": False,
        "policy": "Publisher verification is an audit overlay only. Original ledger provenance is not rewritten; unmatched or ambiguous leads cannot be promoted."
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("NEWS_LEDGER_RECONCILIATION=" + json.dumps(report, sort_keys=True))
    if report["status"] != "PASS_LEDGER_RECONCILIATION":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
