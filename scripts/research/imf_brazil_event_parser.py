#!/usr/bin/env python3
"""Conservative, offline parser for IMF SDMX RegistryInterface 2.1 event payloads.

It never fetches URLs and never promotes a record to Brazil PASS: it emits a
candidate only when exact provider/BCB URL evidence is present in a genuine
SubmitRegistrationRequest. Missing semantics remain UNKNOWN.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import xml.etree.ElementTree as ET

RI_NS = "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message"
BCB_URL = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
BRAZIL_PROVIDER = "IMF:BR1"

def lname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]

def namespace(tag: str) -> str:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") else ""

def inspect_bytes(raw: bytes) -> dict:
    digest = hashlib.sha256(raw).hexdigest()
    base = {"sha256": digest, "byte_count": len(raw), "classification": "UNKNOWN",
            "brazil_registration_candidate": False, "acceptance": "UNKNOWN",
            "reasons": []}
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "reasons": [f"malformed_xml:{exc}"]}
    if lname(root.tag) != "RegistryInterface" or namespace(root.tag) != RI_NS:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "root": lname(root.tag), "root_namespace": namespace(root.tag),
                "reasons": ["unexpected_root_or_registryinterface_namespace"]}
    requests = [e for e in root.iter() if lname(e.tag) in
                ("SubmitRegistrationRequest", "SubmitRegistrationsRequest", "SubmitStructureRequest")]
    kinds = sorted({lname(e.tag) for e in requests})
    if len(requests) != 1:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "root": "RegistryInterface", "request_types": kinds,
                "reasons": ["expected_exactly_one_supported_submit_request"]}
    request = requests[0]
    kind = lname(request.tag)
    if namespace(request.tag) != RI_NS:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "request_types": [kind], "reasons": ["request_namespace_mismatch"]}
    if kind == "SubmitStructureRequest":
        return {**base, "classification": "STRUCTURE_EVENT", "acceptance": "NOT_APPLICABLE",
                "request_types": [kind], "reasons": ["structure_submission_is_not_data_registration"]}
    # Inspect request subtree only. Namespace-aware XML parse; retain exact values.
    values = []
    for elem in request.iter():
        for key, value in elem.attrib.items():
            if value.strip():
                values.append({"element": lname(elem.tag), "field": "@" + lname(key), "value": value.strip()})
        if elem.text and elem.text.strip():
            values.append({"element": lname(elem.tag), "field": "text", "value": elem.text.strip()})
    flat = "\n".join(v["value"] for v in values)
    provider_match = any(v["value"] == BRAZIL_PROVIDER for v in values)
    url_match = BCB_URL in flat
    # Also accept URI-escaped/case-insensitive exact URL only; no host substring matching.
    if not url_match:
        url_match = any(v["value"].lower() == BCB_URL.lower() for v in values)
    dataflows = sorted({v["value"] for v in values if "BOP6" in v["value"] or "BOP_BPM6" in v["value"]})
    actions = sorted({v["value"] for v in values if v["field"].lower() in ("@action", "@type")
                      and v["value"].lower() in ("register", "reregister", "re-register", "delete", "replace")})
    candidate = provider_match or url_match
    reasons = []
    if not candidate:
        reasons.append("no_exact_brazil_provider_or_bcb_url_in_registration_request")
    if provider_match and not url_match:
        reasons.append("provider_exact_match_but_bcb_url_not_present")
    if url_match and not provider_match:
        reasons.append("bcb_url_exact_match_but_provider_not_present")
    if not actions:
        reasons.append("event_action_not_extracted_from_payload")
    if not dataflows:
        reasons.append("bop_dataflow_identifier_not_present")
    # Candidate is deliberately not PASS; downstream PA/dataflow/provenance review required.
    return {**base, "classification": "REGISTRATION_EVENT_CANDIDATE" if candidate else "REGISTRATION_EVENT",
            "brazil_registration_candidate": candidate, "acceptance": "REQUIRES_MANUAL_EVIDENCE_REVIEW" if candidate else "NOT_BRAZIL",
            "root": "RegistryInterface", "request_types": [kind],
            "provider_exact_match": provider_match, "bcb_url_exact_match": url_match,
            "dataflow_identifiers": dataflows, "action_candidates": actions,
            "evidence_values": values, "reasons": reasons + (["provision_agreement_and_transaction_time_must_be_verified"] if candidate else [])}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="Local XML files; no network access")
    ap.add_argument("--output", default="imf_event_parse_results.json")
    args = ap.parse_args()
    results = []
    for name in args.inputs:
        path = Path(name)
        results.append({"file": str(path), **inspect_bytes(path.read_bytes())})
    Path(args.output).write_text(json.dumps({"mode": "offline_conservative_parse", "results": results},
                                             indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": args.output, "count": len(results),
                      "candidates": sum(r["brazil_registration_candidate"] for r in results),
                      "all_acceptance_pass": False}, ensure_ascii=False))
if __name__ == "__main__":
    main()
