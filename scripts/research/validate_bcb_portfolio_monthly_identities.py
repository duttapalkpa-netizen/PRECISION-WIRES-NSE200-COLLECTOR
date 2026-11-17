#!/usr/bin/env python3
"""Fail-closed monthly BCB portfolio investment accounting-identity audit."""
from __future__ import annotations
import argparse, csv, hashlib, json
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAPTURES = {
    "priority": ROOT / "data/raw/bcb/priority_series_capture_20261117",
    "instrument": ROOT / "data/raw/bcb/instrument_net_capture_20261117",
}
MANIFESTS = {k: v / "manifest.json" for k, v in CAPTURES.items()}
SERIES_FILES = {
    "22905": ("priority", "sgs_22905.csv"), "22906": ("priority", "sgs_22906.csv"),
    "22907": ("priority", "sgs_22907.csv"), "22908": ("priority", "sgs_22908.csv"),
    "22924": ("priority", "sgs_22924.csv"), "22925": ("priority", "sgs_22925.csv"),
    "22926": ("priority", "sgs_22926.csv"), "22909": ("instrument", "sgs_22909.csv"),
    "22912": ("instrument", "sgs_22912.csv"), "22915": ("instrument", "sgs_22915.csv"),
    "22927": ("instrument", "sgs_22927.csv"), "22936": ("instrument", "sgs_22936.csv"),
    "22939": ("instrument", "sgs_22939.csv"), "22942": ("instrument", "sgs_22942.csv"),
    "22945": ("instrument", "sgs_22945.csv"),
}
TOLERANCE = Decimal("0.11")
IDENTITIES = [
    ("assets_net_from_gross", "22906 = 22908 - 22907", ("22906","22908","22907"),
     lambda s,p: s["22906"][p] - (s["22908"][p] - s["22907"][p])),
    ("liabilities_net_from_gross", "22924 = 22925 - 22926", ("22924","22925","22926"),
     lambda s,p: s["22924"][p] - (s["22925"][p] - s["22926"][p])),
    ("portfolio_net_assets_minus_liabilities", "22905 = 22906 - 22924", ("22905","22906","22924"),
     lambda s,p: s["22905"][p] - (s["22906"][p] - s["22924"][p])),
    ("assets_instrument_components", "22906 = 22909 + 22912 + 22915", ("22906","22909","22912","22915"),
     lambda s,p: s["22906"][p] - (s["22909"][p] + s["22912"][p] + s["22915"][p])),
    ("liabilities_instrument_components", "22924 = 22927 + 22936 + 22939", ("22924","22927","22936","22939"),
     lambda s,p: s["22924"][p] - (s["22927"][p] + s["22936"][p] + s["22939"][p])),
    ("debt_liability_market_split", "22939 = 22942 + 22945", ("22939","22942","22945"),
     lambda s,p: s["22939"][p] - (s["22942"][p] + s["22945"][p])),
]

def parse_decimal(value: str) -> Decimal:
    normalized = value.strip().replace(".", "").replace(",", ".")
    try:
        result = Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError(f"invalid numeric value: {value!r}") from exc
    if not result.is_finite():
        raise ValueError("non-finite numeric value")
    return result

def load_manifest(group: str) -> dict:
    payload = json.loads(MANIFESTS[group].read_text(encoding="utf-8"))
    expected = "RAW_CAPTURE_7_OF_7_PASS" if group == "priority" else "RAW_CAPTURE_8_OF_8_PASS"
    if payload.get("status") != expected:
        raise ValueError(f"{group} manifest status mismatch")
    if payload.get("provider") != "Banco Central do Brasil / BCData SGS":
        raise ValueError(f"{group} manifest provider mismatch")
    return payload

def load_series(code: str, group: str, filename: str, manifests: dict) -> tuple[dict, dict]:
    path = CAPTURES[group] / filename
    raw = path.read_bytes()
    entry = manifests[group].get("series", {}).get(code)
    if not isinstance(entry, dict) or entry.get("raw_capture_status") != "PASS":
        raise ValueError(f"series {code}: missing or non-PASS manifest entry")
    if len(raw) != entry.get("byte_length"):
        raise ValueError(f"series {code}: raw byte length mismatch")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != entry.get("sha256"):
        raise ValueError(f"series {code}: raw SHA-256 mismatch")
    if entry.get("http_status") != 200 or "text/csv" not in entry.get("content_type", "").lower():
        raise ValueError(f"series {code}: HTTP/content type mismatch")
    rows, previous = {}, None
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        if reader.fieldnames != ["data", "valor"]:
            raise ValueError(f"series {code}: unexpected CSV columns {reader.fieldnames}")
        for row in reader:
            day, month, year = row["data"].strip().split("/")
            period = f"{year}-{month}"
            if previous is not None and period <= previous:
                raise ValueError(f"series {code}: duplicate or non-ascending month {period}")
            rows[period] = parse_decimal(row["valor"])
            previous = period
    if len(rows) != 381 or not rows:
        raise ValueError(f"series {code}: expected 381 observations, got {len(rows)}")
    return rows, {"bytes": len(raw), "sha256": digest, "rows": len(rows),
                  "first_period": next(iter(rows)), "last_period": next(reversed(rows)),
                  "title": entry.get("title"), "requested_url": entry.get("requested_url"),
                  "final_url": entry.get("final_url"), "retrieved_at_utc": entry.get("retrieved_at_utc")}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", default="data/qa/BCB_PORTFOLIO_MONTHLY_ACCOUNTING_IDENTITIES_20261117.json")
    parser.add_argument("--markdown", default="docs/BCB_PORTFOLIO_MONTHLY_ACCOUNTING_IDENTITIES_20261117.md")
    args = parser.parse_args()
    manifests = {group: load_manifest(group) for group in CAPTURES}
    series, provenance = {}, {}
    for code, (group, filename) in SERIES_FILES.items():
        series[code], provenance[code] = load_series(code, group, filename, manifests)
    periods = sorted(set.intersection(*(set(v) for v in series.values())))
    if len(periods) != 381 or periods[0] != "1995-01" or periods[-1] != "2026-09":
        raise ValueError(f"unexpected common coverage: {len(periods)} {periods[:1]} {periods[-1:]}")
    results = []
    for key, formula, codes, fn in IDENTITIES:
        residuals = [(period, fn(series, period)) for period in periods]
        failures = [(p, str(v)) for p,v in residuals if abs(v) > TOLERANCE]
        max_period, max_value = max(residuals, key=lambda x: abs(x[1]))
        results.append({
            "id": key, "formula": formula, "series": list(codes),
            "period_count": len(residuals), "pass_count": len(residuals)-len(failures),
            "fail_count": len(failures), "tolerance_usd_million": str(TOLERANCE),
            "max_abs_residual_usd_million": str(abs(max_value)),
            "max_residual_period": max_period, "first_failures": failures[:10],
            "status": "PASS" if not failures else "FAIL",
        })
    passed = all(x["status"] == "PASS" for x in results)
    report = {
        "schema_version": 1,
        "purpose": "research_only_multi_period_BCB_portfolio_investment_accounting_identity_audit",
        "provider": "Banco Central do Brasil / BCData SGS",
        "unit": "USD million",
        "coverage": {"period_count": len(periods), "first_period": periods[0], "last_period": periods[-1]},
        "tolerance": {"usd_million": str(TOLERANCE), "basis": "0.1 USD million displayed precision plus 0.01 guard"},
        "raw_manifest_sha256": {g: hashlib.sha256(MANIFESTS[g].read_bytes()).hexdigest() for g in MANIFESTS},
        "series_provenance": provenance, "identity_results": results,
        "acceptance": "PASS_ALL_6_IDENTITIES" if passed else "FAIL_ONE_OR_MORE_IDENTITIES",
        "interpretation": {
            "assets_net": "22906 = 22908 outflows minus 22907 inflows; observed BCB series sign convention.",
            "liabilities_net": "22924 = 22925 inflows minus 22926 outflows.",
            "portfolio_net": "22905 = net acquisition of financial assets (22906) minus net incurrence of liabilities (22924).",
            "scope": "monthly BOP accounting identities only; not a forecast, trading trigger or production feature."
        },
        "production_integration": "NOT_AUTHORIZED",
        "trusted_feature_admission": "NOT_AUTHORIZED",
    }
    out_json, out_md = ROOT / args.json, ROOT / args.markdown
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# BCB Portfolio Investment — Monthly Accounting Identity Audit",
        "Date: 2026-11-17 | Research-only | Unit: USD million",
        "",
        f"Coverage: {len(periods)} common monthly observations, {periods[0]} to {periods[-1]}.",
        f"Acceptance: **{report['acceptance']}**. Raw CSV bytes and SHA-256 revalidated against both archived manifests.",
        "",
        "| Identity | Pass / Total | Max absolute residual (USD mn) | Status |",
        "|---|---:|---:|---|",
    ]
    for item in results:
        lines.append(f"| {item['formula']} | {item['pass_count']} / {item['period_count']} | {item['max_abs_residual_usd_million']} | {item['status']} |")
    lines += [
        "", "## Sign conventions observed",
        "- Assets net acquisition: 22906 = 22908 (outflows) − 22907 (inflows).",
        "- Liabilities net incurrence: 22924 = 22925 (inflows) − 22926 (outflows).",
        "- Portfolio investment net: 22905 = 22906 − 22924.",
        "", "## Guardrails",
        "- Reconciliation tolerance: USD 0.11 million, reflecting one-decimal-million SGS series precision.",
        "- No forward-fill, imputation, fabricated observations or timestamps.",
        "- Identities validate accounting consistency only; no causality, attractiveness, predictive power or 1–3 day signal eligibility.",
        "- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E remain unchanged. Production integration NOT_AUTHORIZED.",
        "", "## Raw provenance",
    ]
    for code, meta in provenance.items():
        lines.append(f"- SGS {code}: {meta['rows']} rows; {meta['first_period']}–{meta['last_period']}; {meta['bytes']} bytes; SHA-256 {meta['sha256']}; title: {meta['title']}.")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not passed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
