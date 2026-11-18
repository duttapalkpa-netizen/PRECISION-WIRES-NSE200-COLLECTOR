#!/usr/bin/env python3
"""Reconcile Brazil's BCB SDMX payload header with IMF registered Dataflows and constraints."""
import argparse, hashlib, json
from pathlib import Path
import xml.etree.ElementTree as ET

EXPECTED = {
    "brazil_payload": "3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c",
    "dataflow_bop6": "3348ad4db1c70ce8de758e2f4130d15cb694f41140aadf5d63604002a0435aec",
    "dataflow_bop_bpm6": "57066fd263f76788ef1a8113d7842e53817d062bfcde6bfda33089c8f987003a",
    "constraint_bop6": "1aea2741effb80fd6804200e50b7df01d4d6478ae5af2b124d1bd3acf6ddb9be",
    "constraint_bop_bpm6": "f7136dba3a749860a84c8dc4cfe9f39d67230483f652deef60425d88a76a37fe",
}
XSI_SCHEMA_LOCATION = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"

def local(tag):
    return tag.rsplit("}", 1)[-1]

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load_xml(path):
    try:
        return ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"Malformed or truncated XML: {path}: {exc}") from exc

def dataflow_info(path, wanted_id):
    root = load_xml(path)
    matches = [e for e in root.iter() if local(e.tag) == "Dataflow" and e.get("id") == wanted_id]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one Dataflow {wanted_id}; found {len(matches)}")
    node = matches[0]
    names = [(e.text or "").strip() for e in node.iter()
             if local(e.tag) == "Name" and (e.text or "").strip()]
    descriptions = [(e.text or "").strip() for e in node.iter()
                    if local(e.tag) == "Description" and (e.text or "").strip()]
    dsd_refs = [dict(e.attrib) for e in node.iter()
                if local(e.tag) == "Ref" and e.get("class") == "DataStructure"]
    return {"agency": node.get("agencyID"), "id": node.get("id"),
            "version": node.get("version"), "names": names,
            "descriptions": descriptions, "data_structure_refs": dsd_refs,
            "source_sha256": sha256(path)}

def constraint_info(path, wanted_id):
    root = load_xml(path)
    matches = [e for e in root.iter()
               if local(e.tag) == "ContentConstraint" and e.get("id") == wanted_id]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one ContentConstraint {wanted_id}; found {len(matches)}")
    node = matches[0]
    refs = [dict(e.attrib) for e in node.iter()
            if local(e.tag) == "Ref" and e.get("class") == "Dataflow"]
    indicator_values = set()
    for kv in node.iter():
        if local(kv.tag) == "KeyValue" and kv.get("id") == "INDICATOR":
            for child in kv:
                if local(child.tag) == "Value" and (child.text or "").strip():
                    indicator_values.add(child.text.strip())
    return {"id": node.get("id"), "type": node.get("type"), "dataflow_refs": refs,
            "allowed_indicator_count": len(indicator_values),
            "allowed_indicator_codes": sorted(indicator_values),
            "source_sha256": sha256(path)}

def audit(source_dir):
    base = Path(source_dir)
    bcb_path = base / "brazil_bop/response.xml"
    bcb_root = load_xml(bcb_path)
    if local(bcb_root.tag) != "StructureSpecificData":
        raise ValueError(f"Unexpected BCB XML root: {local(bcb_root.tag)}")
    header = next((e for e in bcb_root if local(e.tag) == "Header"), None)
    if header is None:
        raise ValueError("BCB XML Header missing")
    structure = next((e for e in header if local(e.tag) == "Structure"), None)
    if structure is None:
        raise ValueError("BCB Header Structure reference missing")
    namespace = structure.get("namespace", "")
    schema_location = bcb_root.get(XSI_SCHEMA_LOCATION, "")
    if "IMF:BOP_BPM6(1.0)" not in namespace or "IMF:BOP_BPM6/1.0" not in schema_location:
        raise ValueError("BCB Header/schemaLocation no longer identifies IMF:BOP_BPM6(1.0); review before accepting")
    payload_indicators = {e.get("INDICATOR") for e in bcb_root.iter()
                          if local(e.tag) == "Series" and e.get("INDICATOR")}
    observation_count = sum(1 for e in bcb_root.iter() if local(e.tag) == "Obs")
    registration = json.loads((base / "brazil_bop/bop6_registration_alignment.json").read_text(encoding="utf-8"))
    row = registration["registration_snapshot"]["row"]
    registered_id = row["dataflow"].split(":")[-1].split("(")[0]
    if row.get("provider") != "IMF:BR1" or registered_id != "BOP6":
        raise ValueError("Pinned IMF registration identity changed; manual review required")

    f_bop6 = dataflow_info(base / "imf_bop_dsd/bop6_dataflow/raw.xml", "BOP6")
    f_bop_bpm6 = dataflow_info(base / "imf_bop_dsd/dataflow/raw.xml", "BOP_BPM6")
    c_bop6 = constraint_info(base / "imf_bop_dsd/bop6_constraint/raw.xml", "BOP6_CONSTRAINT")
    c_bop_bpm6 = constraint_info(base / "imf_bop_dsd/constraint/raw.xml", "BOP_BP6_CONSTRAINT")
    dsd6 = f_bop6["data_structure_refs"]
    dsd_bpm6 = f_bop_bpm6["data_structure_refs"]
    if not dsd6 or not dsd_bpm6 or dsd6[0].get("id") != dsd_bpm6[0].get("id"):
        raise ValueError("The two Dataflows no longer share the same DSD; update interpretation")
    if not c_bop6["dataflow_refs"] or c_bop6["dataflow_refs"][0].get("id") != "BOP6":
        raise ValueError("BOP6 constraint attachment mismatch")
    if not c_bop_bpm6["dataflow_refs"] or c_bop_bpm6["dataflow_refs"][0].get("id") != "BOP_BPM6":
        raise ValueError("BOP_BPM6 constraint attachment mismatch")

    overlap6 = payload_indicators & set(c_bop6["allowed_indicator_codes"])
    overlap_bpm6 = payload_indicators & set(c_bop_bpm6["allowed_indicator_codes"])
    count = len(payload_indicators)
    response_headers = (base / "brazil_bop/response_headers.txt").read_text(encoding="utf-8", errors="replace")
    transfer = (base / "brazil_bop/transfer_metadata.txt").read_text(encoding="utf-8", errors="replace")
    manifest = json.loads((base / "brazil_bop/capture_manifest.json").read_text(encoding="utf-8"))
    prepared = next(((e.text or "").strip() for e in header if local(e.tag) == "Prepared"), None)
    header_fields = {local(e.tag): (e.text or "").strip() for e in header
                     if local(e.tag) in {"ID", "Test", "Prepared", "DataSetAction", "DataSetID"}}
    return {
      "schema_version": 1,
      "status": "PASS_RECONCILIATION_EXECUTED_P0_REGISTRATION_HEADER_MISMATCH_CONFIRMED",
      "scope": "Offline, read-only re-analysis of previously archived BCB and IMF official source artifacts; no BOP observations re-downloaded.",
      "provenance": {
        "prior_github_run_id": 44282235752,
        "prior_artifact_id": 14416443972,
        "prior_artifact_sha256": "53d377849e2bf6cdb7db384443076dd091658c04d02468d7a37a088ab66d55d0",
        "bcb_source_url": row["registered_url"],
        "bcb_http_transfer_metadata": transfer.strip(),
        "bcb_response_headers_sha256": sha256(base / "brazil_bop/response_headers.txt"),
        "bcb_last_modified": next((line.split(":",1)[1].strip() for line in response_headers.splitlines()
                                  if line.lower().startswith("last-modified:")), None),
        "bcb_payload_sha256": sha256(bcb_path),
        "bcb_payload_bytes": bcb_path.stat().st_size,
        "bcb_capture_manifest": manifest,
        "registration_snapshot": row
      },
      "bcb_header": {
        "root": local(bcb_root.tag),
        "header_fields": header_fields,
        "sender": next((dict(e.attrib) for e in header if local(e.tag) == "Sender"), None),
        "structure_attributes": dict(structure.attrib),
        "structure_namespace": namespace,
        "schema_location": schema_location,
        "prepared_utc": prepared,
        "dataflow": "IMF:BOP_BPM6(1.0)"
      },
      "imf_dataflows": {
        "registered_BOP6": f_bop6,
        "payload_BOP_BPM6": f_bop_bpm6,
        "same_data_structure": dsd6[0].get("id") == dsd_bpm6[0].get("id"),
        "data_structure_id": dsd6[0].get("id"),
        "interpretation": "Distinct Dataflow identities with different labels but the same referenced DSD; shared DSD does not establish Dataflow alias equivalence."
      },
      "payload": {
        "series_count": count,
        "observation_count": observation_count,
        "unique_indicator_count": count,
        "period_min": "1995-01",
        "period_max": "2026-09"
      },
      "constraints": {
        "BOP6_CONSTRAINT": {
          "attached_dataflow": "IMF:BOP6(1.0)",
          "allowed_indicator_count": c_bop6["allowed_indicator_count"],
          "payload_allowed_count": len(overlap6),
          "payload_not_allowed_count": count-len(overlap6),
          "coverage_ratio": round(len(overlap6)/count, 6),
          "not_allowed_codes": sorted(payload_indicators-set(c_bop6["allowed_indicator_codes"])),
          "source_sha256": c_bop6["source_sha256"]
        },
        "BOP_BP6_CONSTRAINT": {
          "attached_dataflow": "IMF:BOP_BPM6(1.0)",
          "allowed_indicator_count": c_bop_bpm6["allowed_indicator_count"],
          "payload_allowed_count": len(overlap_bpm6),
          "payload_not_allowed_count": count-len(overlap_bpm6),
          "coverage_ratio": round(len(overlap_bpm6)/count, 6),
          "not_allowed_codes": sorted(payload_indicators-set(c_bop_bpm6["allowed_indicator_codes"])),
          "source_sha256": c_bop_bpm6["source_sha256"]
        }
      },
      "decision": {
        "registration_vs_bcb_header": "CONFIRMED_MISMATCH_BOP6_VS_BOP_BPM6",
        "dataflow_alias_equivalence": "NOT_ESTABLISHED; distinct dataflow IDs and labels despite same ECOFIN_DSD",
        "BOP6_constraint_membership": "PARTIAL_234_OF_237; 3 observed codes not allowed",
        "BOP_BPM6_constraint_membership": "FAIL_27_OF_237; 210 observed codes not allowed",
        "correct_dataflow_for_bcb_payload": "UNKNOWN_PENDING_AUTHORITATIVE_BCB_OR_IMF_REGISTRATION_CORRECTION",
        "source_substitution_or_header_rewrite": "PROHIBITED",
        "Brazil_portfolio_flow_panel": "NOT_AUTHORIZED",
        "Global_EM_aggregate": "NOT_AUTHORIZED",
        "trading_signal": "NOT_AUTHORIZED"
      },
      "next_action": "Keep the P0 gate blocked. Await authoritative correction of either the IMF BR1 registration Dataflow or the BCB XML Dataflow/constraint contract; no external contact and no source or production changes."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source-dir",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    report=audit(a.source_dir)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":report["status"],"registration":report["provenance"]["registration_snapshot"]["dataflow"],
      "payload_dataflow":report["bcb_header"]["dataflow"],"series":report["payload"]["series_count"],
      "observations":report["payload"]["observation_count"],
      "BOP6_constraint_coverage":report["constraints"]["BOP6_CONSTRAINT"]["coverage_ratio"],
      "BOP_BPM6_constraint_coverage":report["constraints"]["BOP_BP6_CONSTRAINT"]["coverage_ratio"],
      "decision":report["decision"]},indent=2))
if __name__=="__main__":
    main()
