#!/usr/bin/env python3
"""Conservative offline parser for SDMX 2.1 RegistryInterface registration events.

No network access. A Brazil candidate requires an exact Brazil PA URN or exact
BCB URL inside a schema-shaped RegistrationRequest/Registration subtree.
This is candidate extraction only; it never establishes transaction chronology
or promotes a record to PASS.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

RI_NS = "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message"
BCB_URL = "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
BRAZIL_PROVIDER = "IMF:BR1"
BRAZIL_PA_URN = "urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)"
ACTION_ENUM = {"Append", "Replace", "Delete", "Information"}


def lname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def namespace(tag: str) -> str:
    return tag[1:].split("}", 1)[0] if tag.startswith("{") else ""


def children_named(parent: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(parent) if lname(child.tag) == name and namespace(child.tag) == RI_NS]


def element_values(element: ET.Element) -> list[str]:
    values = []
    for node in element.iter():
        if node.text and node.text.strip():
            values.append(node.text.strip())
        for value in node.attrib.values():
            if value and value.strip():
                values.append(value.strip())
    return values


def inspect_bytes(raw: bytes) -> dict:
    digest = hashlib.sha256(raw).hexdigest()
    base = {"sha256": digest, "byte_count": len(raw), "classification": "UNKNOWN",
            "brazil_registration_candidate": False, "acceptance": "UNKNOWN", "reasons": []}
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "reasons": [f"malformed_xml:{exc}"]}
    if lname(root.tag) != "RegistryInterface" or namespace(root.tag) != RI_NS:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "root": lname(root.tag), "root_namespace": namespace(root.tag),
                "reasons": ["unexpected_root_or_registryinterface_namespace"]}

    # The SDMX 2.1 RegistryInterface payload is a direct child of the root.
    payloads = [child for child in list(root) if namespace(child.tag) == RI_NS and
                lname(child.tag) in ("SubmitRegistrationsRequest", "SubmitStructureRequest")]
    if len(payloads) != 1:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "request_types": sorted(lname(x.tag) for x in payloads),
                "reasons": ["expected_exactly_one_direct_supported_request_payload"]}
    request = payloads[0]
    kind = lname(request.tag)
    if kind == "SubmitStructureRequest":
        return {**base, "classification": "STRUCTURE_EVENT", "acceptance": "NOT_APPLICABLE",
                "request_types": [kind], "reasons": ["structure_submission_is_not_data_registration"]}

    registration_requests = children_named(request, "RegistrationRequest")
    if not registration_requests:
        return {**base, "classification": "QUARANTINE", "acceptance": "FAIL",
                "request_types": [kind], "reasons": ["no_direct_RegistrationRequest_children"]}

    records = []
    for rr in registration_requests:
        registrations = children_named(rr, "Registration")
        action = rr.attrib.get("action")
        for registration in registrations:
            pa_nodes = children_named(registration, "ProvisionAgreement")
            ds_nodes = children_named(registration, "Datasource")
            pa_values = [v for node in pa_nodes for v in element_values(node)]
            ds_values = [v for node in ds_nodes for v in element_values(node)]
            # Exact whole-value matching only, and only in schema-relevant subtrees.
            pa_match = BRAZIL_PA_URN in pa_values
            url_match = any(v.lower() == BCB_URL.lower() for v in ds_values)
            provider_match = any(v == BRAZIL_PROVIDER for v in pa_values + ds_values)
            candidate = pa_match or url_match or provider_match
            records.append({
                "action_raw": action,
                "action_enum_valid": action in ACTION_ENUM,
                "provision_agreement_values": pa_values,
                "datasource_values": ds_values,
                "brazil_pa_exact_match": pa_match,
                "provider_exact_match": provider_match,
                "bcb_url_exact_match": url_match,
                "brazil_registration_candidate": candidate,
                "source_last_updated": registration.attrib.get("lastUpdated"),
            })

    candidates = [r for r in records if r["brazil_registration_candidate"]]
    reasons = []
    if not candidates:
        reasons.append("no_exact_brazil_pa_provider_or_bcb_url_in_schema_shaped_registration")
    if any(not r["action_enum_valid"] for r in records):
        reasons.append("one_or_more_actions_missing_or_outside_sdmx21_action_enum")
    if candidates:
        reasons.append("candidate_requires_external_pa_resolution_and_transaction_time_evidence")
    return {**base,
            "classification": "REGISTRATION_EVENT_CANDIDATE" if candidates else "REGISTRATION_EVENT",
            "brazil_registration_candidate": bool(candidates),
            "acceptance": "REQUIRES_MANUAL_EVIDENCE_REVIEW" if candidates else "NOT_BRAZIL",
            "root": "RegistryInterface", "request_types": [kind],
            "registration_count": len(records), "registrations": records,
            "reasons": reasons}


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
