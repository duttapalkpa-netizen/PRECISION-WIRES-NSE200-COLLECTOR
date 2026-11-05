#!/usr/bin/env python3
"""Build a research-only, publication-time-safe IIP-to-company join.

No guessed company mappings, no reference-month backdating, no interpolation.
Only VERIFIED mappings with primary-source provenance are eligible.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import pandas as pd

REQUIRED_MAP = {
    "symbol", "isin", "company_name", "nic_2025_2digit",
    "segment_description", "segment_revenue_share_pct",
    "effective_from", "effective_to", "mapping_status",
    "evidence_source_type", "evidence_source_url",
    "evidence_publication_timestamp_ist", "evidence_document_id",
    "evidence_sha256", "verification_note",
}
REQUIRED_IIP = {
    "reference_month", "release_timestamp_ist", "base_year",
    "estimate_stage", "nic_2025_2digit", "description",
    "weight_pct", "sep_2025_index", "sep_2026_index",
    "apr_sep_2025_cumulative_index", "apr_sep_2026_cumulative_index",
    "sep_yoy_growth_pct", "apr_sep_yoy_growth_pct",
    "source_statement", "source_url",
}

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mapping", required=True)
    ap.add_argument("--iip", required=True)
    ap.add_argument("--decision-cutoff", required=True,
                    help="Timezone-aware ISO-8601 decision timestamp")
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", required=True)
    a = ap.parse_args()
    mp, ip = Path(a.mapping), Path(a.iip)
    cutoff = pd.Timestamp(a.decision_cutoff)
    if cutoff.tzinfo is None:
        raise SystemExit("BLOCKED: decision-cutoff must include timezone")
    m, i = pd.read_csv(mp, dtype=str).fillna(""), pd.read_csv(ip, dtype=str).fillna("")
    errors = []
    for label, frame, required in [("mapping", m, REQUIRED_MAP), ("iip", i, REQUIRED_IIP)]:
        missing = sorted(required - set(frame.columns))
        if missing: errors.append(f"{label}: missing columns {missing}")
    if errors:
        print(json.dumps({"status":"BLOCKED","errors":errors}, indent=2)); return 2

    # An empty template is valid as a schema check but yields no joined observations.
    if m.empty:
        out = pd.DataFrame(columns=[
            "symbol","isin","company_name","nic_2025_2digit","segment_revenue_share_pct",
            "reference_month","release_timestamp_ist","estimate_stage","iip_growth_pct",
            "mapping_evidence_url","mapping_evidence_sha256","iip_source_url","eligibility"
        ])
        out.to_csv(a.out, index=False)
        report = {"status":"NO_VERIFIED_MAPPINGS","mapping_rows":0,"joined_rows":0,
                  "reason":"Template only; no company exposure has been asserted."}
        Path(a.report).write_text(json.dumps(report, indent=2)+"\n")
        print(json.dumps(report, indent=2)); return 0

    m["nic_2025_2digit"] = m["nic_2025_2digit"].str.strip()
    valid_codes = {str(x) for x in range(10,33)}
    bad_codes = m[~m.nic_2025_2digit.isin(valid_codes | {"UNKNOWN"})]
    if not bad_codes.empty: errors.append("mapping contains invalid NIC-2025 2-digit codes")
    bad_status = m[~m.mapping_status.isin(["VERIFIED","UNKNOWN","REJECTED"])]
    if not bad_status.empty: errors.append("mapping_status must be VERIFIED, UNKNOWN, or REJECTED")
    dup = m.duplicated(["symbol","isin","nic_2025_2digit","effective_from"], keep=False)
    if dup.any(): errors.append("duplicate symbol/ISIN/NIC/effective_from mapping keys")
    verified = m[m.mapping_status == "VERIFIED"].copy()
    for col in ["symbol","isin","company_name","segment_description","evidence_source_url",
                "evidence_publication_timestamp_ist","evidence_document_id","evidence_sha256",
                "verification_note","effective_from"]:
        if (verified[col].str.strip() == "").any(): errors.append(f"VERIFIED mapping missing {col}")
    if not verified.empty:
        pct = pd.to_numeric(verified.segment_revenue_share_pct, errors="coerce")
        if pct.isna().any() or ((pct <= 0) | (pct > 100)).any():
            errors.append("VERIFIED segment_revenue_share_pct must be numeric in (0,100]")
        verified["share_num"] = pct
        totals = verified.groupby(["symbol","isin","effective_from"], dropna=False).share_num.sum()
        if (totals > 100.0001).any(): errors.append("segment shares exceed 100% for a symbol/effective_from")
        try:
            verified["eff_from"] = pd.to_datetime(verified.effective_from, errors="raise", utc=True)
            verified["eff_to"] = pd.to_datetime(verified.effective_to.replace("", pd.NA), errors="coerce", utc=True)
            verified["evidence_ts"] = pd.to_datetime(verified.evidence_publication_timestamp_ist, errors="raise", utc=True)
        except Exception as e: errors.append(f"invalid mapping date/timestamp: {e}")
    try:
        i["nic_2025_2digit"] = i.nic_2025_2digit.astype(str).str.strip()
        i["release_ts"] = pd.to_datetime(i.release_timestamp_ist, errors="raise", utc=True)
        i["iip_growth_pct"] = pd.to_numeric(i.sep_yoy_growth_pct, errors="raise")
    except Exception as e: errors.append(f"invalid IIP vintage/timestamp/growth: {e}")
    if errors:
        report={"status":"BLOCKED","errors":errors,"mapping_sha256":sha256_file(mp),"iip_sha256":sha256_file(ip)}
        Path(a.report).write_text(json.dumps(report,indent=2)+"\n")
        print(json.dumps(report,indent=2)); return 2

    eligible = verified[
        (verified.eff_from <= cutoff.tz_convert("UTC")) &
        (verified.eff_to.isna() | (verified.eff_to >= cutoff.tz_convert("UTC"))) &
        (verified.evidence_ts <= cutoff.tz_convert("UTC")) &
        (verified.nic_2025_2digit.isin(valid_codes))
    ]
    # Release timestamp, not reference month, controls information availability.
    vintages = i[i.release_ts <= cutoff.tz_convert("UTC")].copy()
    joined = eligible.merge(vintages, on="nic_2025_2digit", how="inner", validate="many_to_many")
    if joined.empty:
        out = pd.DataFrame(columns=[
            "symbol","isin","company_name","nic_2025_2digit","segment_revenue_share_pct",
            "reference_month","release_timestamp_ist","estimate_stage","iip_growth_pct",
            "mapping_evidence_url","mapping_evidence_sha256","iip_source_url","eligibility"
        ])
    else:
        joined["eligibility"] = "RESEARCH_ONLY_TIME_SAFE"
        out = joined.rename(columns={
            "evidence_source_url":"mapping_evidence_url",
            "evidence_sha256":"mapping_evidence_sha256",
            "source_url":"iip_source_url",
        })[[
            "symbol","isin","company_name","nic_2025_2digit","segment_revenue_share_pct",
            "reference_month","release_timestamp_ist","estimate_stage","iip_growth_pct",
            "mapping_evidence_url","mapping_evidence_sha256","iip_source_url","eligibility"
        ]]
    out.to_csv(a.out,index=False)
    report={
        "status":"PASS" if len(out) else "NO_ELIGIBLE_JOIN_ROWS",
        "mapping_rows":len(m),"verified_mapping_rows":len(verified),
        "eligible_mapping_rows":len(eligible),"iip_vintage_rows":len(i),
        "eligible_iip_vintage_rows":len(vintages),"joined_rows":len(out),
        "decision_cutoff":a.decision_cutoff,
        "mapping_sha256":sha256_file(mp),"iip_sha256":sha256_file(ip),
        "output_sha256":sha256_file(Path(a.out)),
        "guardrails":["release timestamp <= decision cutoff","mapping evidence timestamp <= decision cutoff",
          "effective interval covers decision cutoff","UNKNOWN/REJECTED mappings excluded",
          "no reference-month backdating","no inferred NIC concordance","research-only; no production score change"]
    }
    Path(a.report).write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
