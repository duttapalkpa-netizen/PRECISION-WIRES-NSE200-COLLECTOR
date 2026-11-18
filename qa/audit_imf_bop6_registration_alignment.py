#!/usr/bin/env python3
"""Compare IMF Brazil registration snapshot, dataflows, constraints and BCB payload.

A registration/payload ID difference and constraint coverage gaps are recorded
as unresolved diagnostics. They are not silently normalized or treated as aliases.
"""
import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

EXPECTED_URL = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
EXPECTED_DSD = {"agencyID": "IMF", "id": "ECOFIN_DSD", "version": "1.0"}


def local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_registration_snapshot(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    row = d["row"]
    if row.get("dataflow") != "IMF:BOP6(1.0)" or row.get("provider") != "IMF:BR1":
        raise ValueError("Registration snapshot does not identify IMF:BOP6(1.0) / IMF:BR1")
    if row.get("registered_url") != EXPECTED_URL:
        raise ValueError("Registration snapshot URL does not match the BCB payload URL")
    if d.get("source_url") != "https://sdmxcentral.imf.org/data/registrations.html":
        raise ValueError("Unexpected registration source URL")
    return d


def parse_dataflow(path, expected_id):
    root = ET.parse(path).getroot()
    nodes = [e for e in root.iter() if local(e.tag) == "Dataflow"
             and e.get("agencyID") == "IMF" and e.get("id") == expected_id and e.get("version") == "1.0"]
    if len(nodes) != 1:
        raise ValueError(f"Expected exactly one IMF:{expected_id}:1.0 dataflow; found {len(nodes)}")
    refs = []
    for node in nodes[0].iter():
        if local(node.tag) == "Structure":
            for ref in node.iter():
                if local(ref.tag) == "Ref":
                    refs.append({k: ref.get(k) for k in ("agencyID", "id", "version")})
    return {"agencyID": "IMF", "id": expected_id, "version": "1.0",
            "data_structure_refs": refs}


def parse_constraint(path, expected_id):
    root = ET.parse(path).getroot()
    nodes = [e for e in root.iter() if local(e.tag) == "ContentConstraint"
             and e.get("agencyID") == "IMF" and e.get("id") == expected_id and e.get("version") == "1.0"]
    if len(nodes) != 1:
        raise ValueError(f"Expected exactly one IMF:{expected_id}:1.0 constraint; found {len(nodes)}")
    node = nodes[0]
    refs = []
    for item in node.iter():
        if local(item.tag) == "Dataflow":
            for ref in item:
                if local(ref.tag) == "Ref":
                    refs.append({k: ref.get(k) for k in ("agencyID", "id", "version")})
    allowed, excluded = set(), set()
    for region in [x for x in node.iter() if local(x.tag) == "CubeRegion"]:
        region_include = region.get("include", "true") == "true"
        for key in [x for x in region if local(x.tag) == "KeyValue" and x.get("id") == "INDICATOR"]:
            key_include = key.get("include", "true") == "true"
            vals = {v.text for v in key if local(v.tag) == "Value" and v.text}
            if region_include and key_include:
                allowed.update(vals)
            else:
                excluded.update(vals)
    allowed.difference_update(excluded)
    return {"agencyID": "IMF", "id": expected_id, "version": "1.0",
            "attached_dataflow_refs": refs, "allowed_indicator_count": len(allowed),
            "allowed_indicator_codes": sorted(allowed)}


def parse_bcb_payload(path):
    root = ET.parse(path).getroot()
    structures = [e for e in root.iter() if local(e.tag) == "Structure"]
    refs = []
    for node in structures:
        match = re.search(r"Dataflow=([^:]+):([^:(]+)\(([^)]+)\)", node.get("namespace", ""))
        if match:
            refs.append({"agencyID": match.group(1), "id": match.group(2), "version": match.group(3)})
    if len(refs) != 1:
        raise ValueError(f"Expected one BCB payload Dataflow namespace; found {refs}")
    observed = sorted({e.get("INDICATOR") for e in root.iter()
                       if local(e.tag) == "Series" and e.get("INDICATOR")})
    if not observed:
        raise ValueError("BCB payload contains no INDICATOR series")
    return refs[0], observed


def coverage(observed, allowed):
    obs, allow = set(observed), set(allowed)
    missing = sorted(obs - allow)
    return {"observed_count": len(obs), "allowed_count": len(allow),
            "observed_and_allowed_count": len(obs & allow),
            "observed_not_allowed_count": len(missing),
            "coverage_ratio": round(len(obs & allow) / len(obs), 6) if obs else 0,
            "missing_observed_codes": missing,
            "status": "PASS_FULL_COVERAGE" if not missing else "FAIL_PARTIAL_COVERAGE"}


def audit(registration_snapshot, registration_html, bop6_dataflow, bop6_constraint,
          bop_bpm6_dataflow, bop_bp6_constraint, bcb_payload):
    registration = parse_registration_snapshot(registration_snapshot)
    reg_flow = parse_dataflow(bop6_dataflow, "BOP6")
    reg_constraint = parse_constraint(bop6_constraint, "BOP6_CONSTRAINT")
    payload_flow = parse_bcb_payload(bcb_payload)
    payload_dataflow = parse_dataflow(bop_bpm6_dataflow, "BOP_BPM6")
    payload_constraint = parse_constraint(bop_bp6_constraint, "BOP_BP6_CONSTRAINT")
    reg_cov = coverage(payload_flow[1], reg_constraint["allowed_indicator_codes"])
    payload_cov = coverage(payload_flow[1], payload_constraint["allowed_indicator_codes"])
    html_raw = Path(registration_html).read_bytes()
    return {
        "status": "PASS_REGISTRATION_PAYLOAD_ALIGNMENT_AUDIT_EXECUTED",
        "scope": "Versioned official registry snapshot, BOP6/BOP_BPM6 dataflows and constraints, and BCB payload reference/observed indicators compared. Raw registration HTML is retained but its table is client-rendered.",
        "registration_snapshot": registration,
        "registration_html_capture": {"bytes": len(html_raw), "sha256": hashlib.sha256(html_raw).hexdigest(),
                                      "table_body_machine_readable": False},
        "registered_dataflow": reg_flow,
        "registered_constraint": {k: v for k, v in reg_constraint.items() if k != "allowed_indicator_codes"},
        "bcb_payload_dataflow_reference": payload_flow[0],
        "payload_observed_indicator_count": len(payload_flow[1]),
        "payload_dataflow_metadata": payload_dataflow,
        "payload_constraint_metadata": {k: v for k, v in payload_constraint.items() if k != "allowed_indicator_codes"},
        "constraint_coverage": {"BOP6_CONSTRAINT": reg_cov, "BOP_BP6_CONSTRAINT": payload_cov},
        "data_structure_alignment": {
            "BOP6_dataflow_refs": reg_flow["data_structure_refs"],
            "BOP_BPM6_dataflow_refs": payload_dataflow["data_structure_refs"],
            "both_reference_ECOFIN_DSD_1_0": reg_flow["data_structure_refs"] == [EXPECTED_DSD]
                and payload_dataflow["data_structure_refs"] == [EXPECTED_DSD]
        },
        "alignment": {
            "registry_dataflow_id": "BOP6",
            "bcb_payload_dataflow_id": payload_flow[0]["id"],
            "ids_equal": payload_flow[0]["id"] == "BOP6",
            "relationship": "MATCH" if payload_flow[0]["id"] == "BOP6" else "UNRESOLVED_REGISTRY_PAYLOAD_ID_DIFFERENCE",
            "alias_or_mapping_proven": False
        },
        "admission": {"brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
                      "global_em_aggregate": "NOT_AUTHORIZED", "trading_signal": "NOT_AUTHORIZED"}
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--registration-snapshot", required=True, type=Path)
    p.add_argument("--registration-html", required=True, type=Path)
    p.add_argument("--bop6-dataflow", required=True, type=Path)
    p.add_argument("--bop6-constraint", required=True, type=Path)
    p.add_argument("--bop-bpm6-dataflow", required=True, type=Path)
    p.add_argument("--bop-bp6-constraint", required=True, type=Path)
    p.add_argument("--bcb-payload", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    try:
        result = audit(a.registration_snapshot, a.registration_html, a.bop6_dataflow,
                       a.bop6_constraint, a.bop_bpm6_dataflow, a.bop_bp6_constraint, a.bcb_payload)
    except (OSError, ValueError, KeyError, ET.ParseError, json.JSONDecodeError) as exc:
        result = {"status": "FAIL", "error": str(exc), "admission": "NOT_AUTHORIZED"}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS_REGISTRATION_PAYLOAD_ALIGNMENT_AUDIT_EXECUTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
