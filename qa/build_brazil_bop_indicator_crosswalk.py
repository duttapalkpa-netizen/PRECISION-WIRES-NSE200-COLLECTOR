#!/usr/bin/env python3
"""Build an evidence-bound Brazil BOP_BPM6 -> IMF CL_INDICATOR crosswalk."""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET


def local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_cl_indicator(path):
    raw = Path(path).read_bytes()
    root = ET.fromstring(raw)
    lists = [e for e in root.iter() if local(e.tag) == "Codelist" and e.get("id") == "CL_INDICATOR"]
    if len(lists) != 1:
        raise ValueError(f"Expected exactly one CL_INDICATOR; got {len(lists)}")
    cl = lists[0]
    identity = {k: cl.get(k) for k in ("agencyID", "id", "version")}
    if identity != {"agencyID": "IMF", "id": "CL_INDICATOR", "version": "1.0"}:
        raise ValueError(f"Unexpected codelist identity {identity}")
    codes = {}
    for node in cl:
        if local(node.tag) != "Code":
            continue
        code = node.get("id")
        if not code or code in codes:
            raise ValueError(f"Missing/duplicate codelist code {code!r}")
        names = [(x.text or "").strip() for x in node if local(x.tag) == "Name" and (x.text or "").strip()]
        descriptions = [(x.text or "").strip() for x in node if local(x.tag) == "Description" and (x.text or "").strip()]
        codes[code] = {"names": names, "descriptions": descriptions}
    if not codes:
        raise ValueError("CL_INDICATOR is empty")
    return codes, {
        "identity": identity, "code_count": len(codes), "raw_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest()
    }


def semantic_fields(label):
    domain = "OTHER_BOP"
    if "Balance of Payments, Current Account," in label:
        domain = "CURRENT_ACCOUNT"
    elif "Balance of Payments, Capital Account," in label:
        domain = "CAPITAL_ACCOUNT"
    elif "Balance of Payments, Financial Account," in label:
        domain = "FINANCIAL_ACCOUNT"
    elif "International Investment Position" in label:
        domain = "IIP"

    is_pi_fa = domain == "FINANCIAL_ACCOUNT" and "Portfolio investment" in label
    side = "NOT_APPLICABLE"
    if is_pi_fa:
        if "Net acquisition of financial assets" in label:
            side = "ASSET_ACQUISITION"
        elif "Net incurrence of liabilities" in label:
            side = "LIABILITY_INCURRENCE"
        else:
            side = "TOTAL_OR_UNSPECIFIED_SIDE"

    pi_income = domain == "CURRENT_ACCOUNT" and "Investment income, Portfolio investment" in label
    instrument = "UNSPECIFIED"
    if "Debt securities" in label:
        instrument = "DEBT_SECURITIES"
    elif "Equity securities other than investment fund shares" in label:
        instrument = "EQUITY_SECURITIES_EX_INVESTMENT_FUNDS"
    elif "Investment fund shares or units" in label:
        instrument = "INVESTMENT_FUND_SHARES_UNITS"
    elif "Equity and investment fund shares" in label:
        instrument = "EQUITY_AND_INVESTMENT_FUND_SHARES"
    return {
        "bop_domain": domain,
        "portfolio_investment_financial_account": is_pi_fa,
        "portfolio_investment_income_current_account": pi_income,
        "financial_account_side": side,
        "instrument_class": instrument,
        "classification_basis": "EXACT_IMF_CL_INDICATOR_ENGLISH_LABEL_RULES_REVIEW_REQUIRED"
    }


def build(brazil_path, codelist_path):
    codes, cl_meta = parse_cl_indicator(codelist_path)
    raw = Path(brazil_path).read_bytes()
    root = ET.fromstring(raw)
    if local(root.tag) != "StructureSpecificData":
        raise ValueError("Brazil XML root is not StructureSpecificData")

    structures = [e for e in root.iter() if local(e.tag) == "Structure"]
    refs = []
    for node in structures:
        match = re.search(r"Dataflow=([^:]+):([^:(]+)\(([^)]+)\)", node.get("namespace", ""))
        if match:
            refs.append({"agencyID": match.group(1), "id": match.group(2), "version": match.group(3)})
    expected = {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"}
    if refs != [expected]:
        raise ValueError(f"Brazil payload dataflow reference mismatch: {refs}")

    series = [e for e in root.iter() if local(e.tag) == "Series"]
    by_code = {}
    for node in series:
        code = node.get("INDICATOR")
        if not code or code in by_code:
            raise ValueError(f"Missing or duplicate series indicator {code!r}")
        if node.get("REF_AREA") != "BR":
            raise ValueError(f"Unexpected REF_AREA {node.get('REF_AREA')!r}")
        if code not in codes:
            raise ValueError(f"Indicator not found in CL_INDICATOR: {code}")
        observations = [e for e in node if local(e.tag) == "Obs"]
        periods = [e.get("TIME_PERIOD") for e in observations]
        if not observations or any(not p for p in periods):
            raise ValueError(f"Empty/missing observations for {code}")
        label = codes[code]["names"][0] if codes[code]["names"] else ""
        by_code[code] = {
            "series_attributes": node.attrib,
            "observation_count": len(observations),
            "first_period": min(periods),
            "last_period": max(periods),
            "period_count": len(set(periods)),
            "observation_attribute_names": sorted({
                k for obs in observations for k in obs.attrib if k not in {"TIME_PERIOD", "OBS_VALUE"}
            }),
            "label": label,
            **semantic_fields(label)
        }

    rows = []
    for code in sorted(by_code):
        row = by_code[code]
        rows.append({
            "indicator": code, "imf_codelist_match": "PASS",
            "imf_label": row.pop("label"), **row
        })

    observation_total = sum(row["observation_count"] for row in rows)
    domain_counts = Counter(row["bop_domain"] for row in rows)
    portfolio_fa = [row for row in rows if row["portfolio_investment_financial_account"]]
    portfolio_income = [row for row in rows if row["portfolio_investment_income_current_account"]]
    quality_keys = sorted({k for row in rows for k in row["observation_attribute_names"]})

    return {
        "schema_version": 1,
        "status": "PASS_CODELIST_CROSSWALK_ONLY",
        "scope": "Exact code-list join and transparent label classification; not an approved investment signal.",
        "source_provenance": {
            "brazil_payload_sha256": hashlib.sha256(raw).hexdigest(),
            "brazil_payload_bytes": len(raw),
            "brazil_dataflow": expected,
            "ref_area": "BR", "data_domain": "BOP6", "counterpart_area": "W1",
            "frequency": "M", "unit_multiplier": "6", "time_format": "P1M",
            "unit_from_official_label": "USD", "raw_values_not_rescaled": True,
            "imf_codelist": cl_meta
        },
        "coverage": {
            "series_count": len(series), "unique_indicator_count": len(by_code),
            "observation_count": observation_total,
            "period_min": min(row["first_period"] for row in rows),
            "period_max": max(row["last_period"] for row in rows),
            "series_observation_count_distribution": dict(Counter(
                str(row["observation_count"]) for row in rows
            )),
            "bop_domain_counts": dict(domain_counts)
        },
        "portfolio_candidates": {
            "financial_account_portfolio_investment_count": len(portfolio_fa),
            "financial_account_portfolio_investment_codes": [row["indicator"] for row in portfolio_fa],
            "portfolio_investment_income_current_account_count": len(portfolio_income),
            "portfolio_investment_income_codes": [row["indicator"] for row in portfolio_income]
        },
        "quality_and_units": {
            "series_attributes_observed": [
                "DATA_DOMAIN", "REF_AREA", "INDICATOR", "COUNTERPART_AREA",
                "FREQ", "UNIT_MULT", "TIME_FORMAT"
            ],
            "observation_quality_attributes_observed": quality_keys,
            "observation_quality_status": "NOT_PRESENT_IN_CAPTURED_PAYLOAD",
            "unit_measure_attribute": "NOT_PRESENT_AS_EXPLICIT_ATTRIBUTE",
            "unit_from_label": "USD", "unit_multiplier": "6",
            "value_rescaling": "NOT_PERFORMED", "quality_gate": "UNKNOWN_NOT_PASS"
        },
        "admission": {
            "brazil_portfolio_flow_panel": "NOT_AUTHORIZED_PENDING_SIGN_AND_QUALITY_REVIEW",
            "global_em_aggregate": "NOT_AUTHORIZED",
            "trading_signal": "NOT_AUTHORIZED"
        },
        "indicators": rows
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brazil-xml", required=True)
    parser.add_argument("--codelist-dsd-xml", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = build(args.brazil_xml, args.codelist_dsd_xml)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in (
        "status", "coverage", "portfolio_candidates", "quality_and_units", "admission"
    )}, indent=2))


if __name__ == "__main__":
    main()
