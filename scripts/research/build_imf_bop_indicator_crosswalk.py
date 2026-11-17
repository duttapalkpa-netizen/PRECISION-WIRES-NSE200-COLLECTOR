#!/usr/bin/env python3
"""Build a fail-closed IMF BOP_BPM6 to BOP DSD portfolio indicator crosswalk.

This is a metadata-only semantic candidate crosswalk. It does not assert that
IMF:BOP:2.6.0 and IMF:ECOFIN_DSD:1.0 are the same DSD, and it does not admit
any observations or production features.
"""
from __future__ import annotations
import argparse, csv, hashlib, json
import xml.etree.ElementTree as ET
from pathlib import Path

EXPECTED_FLOW = ("IMF", "BOP_BPM6", "1.0")
EXPECTED_CONSTRAINT = ("IMF", "BOP_BP6_CONSTRAINT", "1.0")
EXPECTED_BOP_DSD = ("IMF", "BOP", "2.6.0")
EXPECTED_GENERIC_DSD = ("IMF", "ECOFIN_DSD", "1.0")
PORTFOLIO_PREFIXES = ("BFP_BP6_", "BFPA_BP6_", "BFPL_BP6_")
CURRENCIES = ("USD", "EUR", "XDC")


def local(tag): return tag.rsplit("}", 1)[-1]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def unique(nodes, predicate, label):
    found = [n for n in nodes if predicate(n)]
    if len(found) != 1:
        raise ValueError(f"{label}: expected exactly one, found {len(found)}")
    return found[0]


def parse_code_list(root, code_list_id):
    cl = unique(list(root.iter()), lambda e: local(e.tag) == "Codelist" and e.attrib.get("id") == code_list_id,
                f"codelist {code_list_id}")
    out = {}
    for code in cl:
        if local(code.tag) != "Code": continue
        names = [" ".join((x.text or "").split()) for x in code if local(x.tag) == "Name"]
        descriptions = [" ".join((x.text or "").split()) for x in code if local(x.tag) == "Description"]
        out[code.attrib.get("id")] = {"name": names[0] if names else "", "description": descriptions[0] if descriptions else ""}
    return out, {k: cl.attrib.get(k) for k in ("agencyID", "id", "version")}


def key_values(root):
    result = {}
    for kv in root.iter():
        if local(kv.tag) == "KeyValue":
            key = kv.attrib.get("id")
            if key:
                result.setdefault(key, []).extend((v.text or "").strip() for v in kv if local(v.tag) == "Value")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture-dir", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    d = args.capture_dir
    manifest = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("overall_status") != "PASS_STRUCTURE_METADATA_ONLY":
        raise ValueError("source capture manifest is not PASS_STRUCTURE_METADATA_ONLY")
    raw_files = {
        "bop_dsd": d / "dsd.xml",
        "dataflow": d / "dataflow.xml",
        "constraint": d / "constraint.xml",
        "referenced_dsd": d / "dataflow_referenced_dsd.xml",
    }
    for key, path in raw_files.items():
        meta_key = {"bop_dsd":"dsd","dataflow":"dataflow","constraint":"constraint","referenced_dsd":"dataflow_referenced_dsd"}[key]
        meta = manifest["sources"][meta_key]
        if not path.is_file() or path.stat().st_size != meta["byte_length"] or digest(path) != meta["sha256"]:
            raise ValueError(f"{key}: raw byte length or SHA-256 mismatch")
    roots = {k: ET.parse(v).getroot() for k, v in raw_files.items()}

    bop_dsd = unique(list(roots["bop_dsd"].iter()), lambda e: local(e.tag) == "DataStructure" and e.attrib.get("id") == "BOP", "BOP DSD")
    bop_identity = tuple(bop_dsd.attrib.get(k) for k in ("agencyID","id","version"))
    if bop_identity != EXPECTED_BOP_DSD: raise ValueError(f"unexpected BOP DSD: {bop_identity}")

    flow = unique(list(roots["dataflow"].iter()), lambda e: local(e.tag) == "Dataflow" and e.attrib.get("id") == "BOP_BPM6", "BOP_BPM6 dataflow")
    flow_identity = tuple(flow.attrib.get(k) for k in ("agencyID","id","version"))
    if flow_identity != EXPECTED_FLOW: raise ValueError(f"unexpected dataflow: {flow_identity}")
    flow_ref = unique([e for e in flow.iter() if local(e.tag) == "Ref" and e.attrib.get("class") == "DataStructure"], lambda e: True, "dataflow DSD reference")
    generic_identity = tuple(flow_ref.attrib.get(k) for k in ("agencyID","id","version"))
    if generic_identity != EXPECTED_GENERIC_DSD: raise ValueError(f"unexpected referenced DSD: {generic_identity}")

    constraint = unique(list(roots["constraint"].iter()), lambda e: local(e.tag) == "ContentConstraint" and e.attrib.get("id") == "BOP_BP6_CONSTRAINT", "BOP constraint")
    constraint_identity = tuple(constraint.attrib.get(k) for k in ("agencyID","id","version"))
    if constraint_identity != EXPECTED_CONSTRAINT: raise ValueError(f"unexpected constraint: {constraint_identity}")
    constraint_ref = unique([e for e in constraint.iter() if local(e.tag) == "Ref" and e.attrib.get("class") == "Dataflow"], lambda e: True, "constraint dataflow reference")
    if tuple(constraint_ref.attrib.get(k) for k in ("agencyID","id","version")) != EXPECTED_FLOW:
        raise ValueError("constraint does not attach to IMF:BOP_BPM6:1.0")

    bop_fc, fc_meta = parse_code_list(roots["bop_dsd"], "CL_FUNCTIONAL_CAT")
    bop_entry, entry_meta = parse_code_list(roots["bop_dsd"], "CL_ACCOUNT_ENTRY")
    indicator, indicator_meta = parse_code_list(roots["referenced_dsd"], "CL_INDICATOR")
    if bop_fc.get("P", {}).get("name") != "Portfolio Investment":
        raise ValueError("BOP DSD FUNCTIONAL_CAT P definition mismatch")
    if bop_entry.get("A", {}).get("name") != "Assets (Net Acquisition of)":
        raise ValueError("BOP DSD ACCOUNT_ENTRY A definition mismatch")
    if bop_entry.get("L", {}).get("name") != "Liabilities (Net Incurrence of)":
        raise ValueError("BOP DSD ACCOUNT_ENTRY L definition mismatch")

    allowed = key_values(roots["constraint"])
    indicators = allowed.get("INDICATOR", [])
    if len(indicators) != len(set(indicators)): raise ValueError("duplicate allowed indicator values")
    missing_codes = sorted(set(indicators) - set(indicator))
    if missing_codes: raise ValueError(f"constraint references indicators absent from CL_INDICATOR: {missing_codes[:10]}")
    selected = []
    for code in sorted(indicators):
        if code.startswith(PORTFOLIO_PREFIXES):
            selected.append({
                "indicator_code": code,
                "official_name": indicator[code]["name"],
                "official_annotation": indicator[code]["description"],
                "currency_suffix": code.rsplit("_", 1)[-1],
                "semantic_role": ("net_acquisition_of_financial_assets" if code.startswith("BFPA_")
                                  else "net_incurrence_of_liabilities" if code.startswith("BFPL_")
                                  else "aggregate_portfolio_investment"),
                "allowed_by_constraint": True,
            })
    required = {"BFPA_BP6_USD", "BFPL_BP6_USD"}
    if not required.issubset({x["indicator_code"] for x in selected}):
        raise ValueError(f"required USD asset/liability indicators not allowed: {sorted(required - {x['indicator_code'] for x in selected})}")
    if "BFP_BP6_USD" in indicators:
        raise ValueError("unexpected aggregate BFP USD indicator in current constraint")
    if "BFP_BP6_EUR" not in indicators:
        raise ValueError("expected EUR aggregate BFP indicator absent from current constraint")

    result = {
        "schema_version": 1,
        "status": "PASS_METADATA_SEMANTIC_CANDIDATES_NOT_OBSERVATION_ACCESS",
        "capture_id_utc": manifest["capture_id_utc"],
        "source_capture_manifest_sha256": digest(d / "manifest.json"),
        "source_raw_sha256": {k: digest(v) for k,v in raw_files.items()},
        "identities": {
            "BOP_DSD_2_6_0": {"agencyID": bop_identity[0], "id": bop_identity[1], "version": bop_identity[2]},
            "BOP_BPM6_dataflow": {"agencyID": flow_identity[0], "id": flow_identity[1], "version": flow_identity[2]},
            "BOP_BPM6_referenced_DSD": {"agencyID": generic_identity[0], "id": generic_identity[1], "version": generic_identity[2]},
            "BOP_constraint": {"agencyID": constraint_identity[0], "id": constraint_identity[1], "version": constraint_identity[2]},
        },
        "structural_relation": "DIFFERENT_DSD_REFERENCE_REQUIRES_EXPLICIT_CROSSWALK",
        "BOP_DSD_semantic_codes": {
            "CL_FUNCTIONAL_CAT": {"metadata": fc_meta, "P": bop_fc["P"]},
            "CL_ACCOUNT_ENTRY": {"metadata": entry_meta, "A": bop_entry["A"], "L": bop_entry["L"]},
        },
        "BOP_BPM6_dataflow": {
            "constraint_data_domain": allowed.get("DATA_DOMAIN", []),
            "constraint_counterpart_area": allowed.get("COUNTERPART_AREA", []),
            "allowed_indicator_count": len(indicators),
            "portfolio_indicator_candidates": selected,
            "portfolio_candidate_count": len(selected),
            "USD_asset_indicator_allowed": "BFPA_BP6_USD" in indicators,
            "USD_liability_indicator_allowed": "BFPL_BP6_USD" in indicators,
            "USD_aggregate_indicator_allowed": "BFP_BP6_USD" in indicators,
            "EUR_aggregate_indicator_allowed": "BFP_BP6_EUR" in indicators,
        },
        "interpretation_boundary": [
            "BFPA is defined as portfolio investment, net acquisition of financial assets; it is not a gross inflow measure.",
            "BFPL is defined as portfolio investment, net incurrence of liabilities; it is not an equity-only FPI measure.",
            "The BOP DSD P/A/L concepts and ECOFIN_DSD INDICATOR codes are separate structural representations; this is a definition-based semantic candidate crosswalk, not a formal same-DSD mapping.",
            "No observations, reporting-country coverage, actual-vs-estimate status, publication vintage or PIT freshness are validated here.",
            "No trading signal or production overlay admission is authorized."
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "portfolio_candidate_count": len(selected),
                      "usd_assets": result["BOP_BPM6_dataflow"]["USD_asset_indicator_allowed"],
                      "usd_liabilities": result["BOP_BPM6_dataflow"]["USD_liability_indicator_allowed"],
                      "usd_aggregate": result["BOP_BPM6_dataflow"]["USD_aggregate_indicator_allowed"],
                      "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
