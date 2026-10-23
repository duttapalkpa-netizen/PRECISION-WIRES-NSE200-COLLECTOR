#!/usr/bin/env python3
"""Fail-closed, read-only provenance reconciliation for alternate-source leads.

The source news ledger is never overwritten. Match event identity using cutoff,
symbol, original timestamp and headline; separately verify that the publisher-native
resolved URL equals the ledger canonical URL. Preserve RSS discovery provenance.
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
    # RSS discovery URL and publisher canonical URL are different provenance fields.
    # Match event identity first, then independently compare verified publisher URL.
    keys = ["_cut","_symbol","_published","_headline"]
    identity = l.groupby(keys, dropna=False).agg(
        _ledger_match_count=("_headline", "size"),
        _ledger_canonical_urls=("CANONICAL_URL", lambda x: " || ".join(sorted(set(v.strip() for v in x if v.strip())))),
    ).reset_index()
    j = c.merge(identity, on=keys, how="left", validate="many_to_one")
    j["_ledger_match_count"] = j["_ledger_match_count"].fillna(0).astype(int)
    j["_ledger_canonical_urls"] = j["_ledger_canonical_urls"].fillna("")
    j["LEDGER_RECONCILIATION_STATUS"] = j["_ledger_match_count"].map(
        lambda n: "UNIQUE_EVENT_IDENTITY_MATCH" if n == 1 else ("AMBIGUOUS_EVENT_IDENTITY_MATCH" if n > 1 else "NO_EVENT_IDENTITY_MATCH"))
    resolved_url_map = {}
    for _, rr in resolved.iterrows():
        key = (str(rr.get("CUT_OFF", "")), str(rr.get("SYMBOL", "")).upper().strip(),
               str(rr.get("ORIGINAL_PUBLISHED_AT", "")), str(rr.get("ORIGINAL_HEADLINE", "")).strip())
        resolved_url_map[key] = str(rr.get("RESOLVED_URL", "")).strip()
    def publisher_url_status(row):
        if int(row["_ledger_match_count"]) != 1:
            return "NOT_CHECKED_NO_UNIQUE_EVENT_MATCH"
        key = (str(row["CUT_OFF"]), str(row["SYMBOL"]).upper().strip(),
               str(row["ORIGINAL_PUBLISHED_AT"]), str(row["ORIGINAL_HEADLINE"]).strip())
        resolved_url = resolved_url_map.get(key, "")
        ledger_urls = [u.strip() for u in str(row["_ledger_canonical_urls"]).split(" || ") if u.strip()]
        if not resolved_url:
            return "BLOCKED_NO_VERIFIED_PUBLISHER_URL"
        return "PUBLISHER_URL_MATCHES_LEDGER_CANONICAL" if resolved_url in ledger_urls else "PUBLISHER_URL_MISMATCH"
    j["PUBLISHER_CANONICAL_URL_STATUS"] = j.apply(publisher_url_status, axis=1)
    j["LEDGER_RECONCILIATION_STATUS"] = j.apply(
        lambda r: "MATCHED_EVENT_AND_CANONICAL_URL" if r["_ledger_match_count"] == 1 and r["PUBLISHER_CANONICAL_URL_STATUS"] == "PUBLISHER_URL_MATCHES_LEDGER_CANONICAL" else r["LEDGER_RECONCILIATION_STATUS"], axis=1)
    # Explicitly report verified RACE/RIIL rows; no promotion or source-field mutation occurs here.
    focus = j[j["SYMBOL"].str.upper().isin(["RACE","RIIL"])].copy()
    focus["VERIFICATION_STATUS"] = ""
    if "VERIFICATION_STATUS" in verified.columns:
        join_keys = [k for k in ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL"] if k in verified.columns and k in focus.columns]
        if join_keys:
            v = verified[join_keys + ["VERIFICATION_STATUS"]].drop_duplicates()
            focus = focus.drop(columns=["VERIFICATION_STATUS"]).merge(v, on=join_keys, how="left", validate="many_to_one")
    focus_cols = [x for x in ["SOURCE_ROW_INDEX","CUT_OFF","SYMBOL","ORIGINAL_PUBLISHED_AT","ORIGINAL_HEADLINE","ORIGINAL_URL","ALTERNATE_ARTICLE_URL","VERIFICATION_STATUS","_ledger_match_count","_ledger_canonical_urls","PUBLISHER_CANONICAL_URL_STATUS","LEDGER_RECONCILIATION_STATUS"] if x in focus.columns]
    focus[focus_cols].to_csv(CSV, index=False)
    expected_pairs = int(len(pd.read_csv("outputs/news_24h/stock_news_24h_cutoff_join.csv", dtype=str).drop_duplicates(["CUT_OFF","SYMBOL"]))) if Path("outputs/news_24h/stock_news_24h_cutoff_join.csv").is_file() else None
    ready_pairs = readiness.get("unique_cutoff_symbol_pairs")
    join_rows = readiness.get("cutoff_symbol_rows")
    count_consistent = expected_pairs is not None and ready_pairs == expected_pairs and join_rows == expected_pairs
    unmatched = int((j["_ledger_match_count"] == 0).sum())
    ambiguous = int((j["_ledger_match_count"] > 1).sum())
    canonical_mismatches = int((j["PUBLISHER_CANONICAL_URL_STATUS"] != "PUBLISHER_URL_MATCHES_LEDGER_CANONICAL").sum())
    report = {
        "status": "PASS_LEDGER_RECONCILIATION" if unmatched == 0 and ambiguous == 0 and canonical_mismatches == 0 and count_consistent else "BLOCKED_LEDGER_RECONCILIATION",
        "ledger_rows": int(len(ledger)), "coverage_rows": int(len(coverage)),
        "candidate_rows": int(len(candidates)), "verified_rows": int(verified.get("VERIFICATION_STATUS", pd.Series(dtype=str)).astype(str).str.upper().eq("VERIFIED").sum()),
        "matched_ledger_rows": int((j["_ledger_match_count"] == 1).sum()),
        "unmatched_candidate_rows": unmatched, "ambiguous_candidate_rows": ambiguous,
        "publisher_canonical_url_mismatches": canonical_mismatches,
        "race_riil_candidate_rows": int(len(focus)),
        "race_riil_exact_unique_matches": int(focus["LEDGER_RECONCILIATION_STATUS"].eq("MATCHED_EVENT_AND_CANONICAL_URL").sum()),
        "readiness_cutoff_symbol_rows": join_rows, "readiness_unique_cutoff_symbol_pairs": ready_pairs,
        "recomputed_join_unique_pairs": expected_pairs, "readiness_pair_counts_consistent": bool(count_consistent),
        "readiness_status": readiness.get("status"), "research_status": "BLOCKED",
        "event_identity_keys": ["cutoff date","symbol","original published timestamp","original headline"],
        "publisher_canonical_url_validation": "Verified publisher-native RESOLVED_URL must equal ledger CANONICAL_URL; ORIGINAL_URL RSS link remains discovery provenance.",
        "source_ledger_modified": False,
        "policy": "Publisher verification is an audit overlay only. Original ledger provenance is not rewritten; unmatched or ambiguous leads cannot be promoted."
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("NEWS_LEDGER_RECONCILIATION=" + json.dumps(report, sort_keys=True))
    if report["status"] != "PASS_LEDGER_RECONCILIATION":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
