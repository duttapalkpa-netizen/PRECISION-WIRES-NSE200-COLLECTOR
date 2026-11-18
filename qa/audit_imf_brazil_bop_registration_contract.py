#!/usr/bin/env python3
"""Audit IMF SDMX Central public registry structures for Brazil BOP registration contract."""
import argparse, hashlib, json
from pathlib import Path
import xml.etree.ElementTree as ET

TARGET_PROVIDER = "BR1"
TARGET_DATAFLOWS = {"BOP6", "BOP_BPM6"}

def local(tag):
    return tag.rsplit("}", 1)[-1]

def attr_record(node):
    return {local(k): v for k, v in node.attrib.items()}

def element_record(node):
    refs, names = [], []
    for child in node.iter():
        if child is node: continue
        name, attrs = local(child.tag), attr_record(child)
        if name.lower().endswith("ref") or name in {"Structure","StructureUsage","StructureProvider","Dataflow","DataProvider","ConstraintAttachment","ContentConstraint"}:
            refs.append({"element":name,"attributes":attrs,"text":(child.text or "").strip()[:500]})
        if name == "Name" and (child.text or "").strip():
            names.append((child.text or "").strip())
    return {"element":local(node.tag),"attributes":attr_record(node),"names":names,"references":refs,
            "serialized_sha256":hashlib.sha256(ET.tostring(node,encoding="utf-8")).hexdigest()}

def load_xml(path):
    raw=Path(path).read_bytes()
    root=ET.fromstring(raw)
    return root,{"path":str(path),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"root":local(root.tag)}

def find_elements(root,target):
    return [n for n in root.iter() if local(n.tag)==target]

def audit(provider_xml,provision_xml,constraint_xml,registration_snapshot):
    pr,pm=load_xml(provider_xml); ar,am=load_xml(provision_xml); cr,cm=load_xml(constraint_xml)
    snap_path=Path(registration_snapshot); snap=json.loads(snap_path.read_text(encoding="utf-8"))
    providers=[element_record(n) for n in find_elements(pr,"DataProvider") if n.get("id")==TARGET_PROVIDER]
    all_pa=find_elements(ar,"ProvisionAgreement")
    relevant_pa=[element_record(n) for n in all_pa if TARGET_PROVIDER in ET.tostring(n,encoding="unicode") or any(x in ET.tostring(n,encoding="unicode") for x in TARGET_DATAFLOWS)]
    all_cc=find_elements(cr,"ContentConstraint")
    relevant_cc=[element_record(n) for n in all_cc if TARGET_PROVIDER in ET.tostring(n,encoding="unicode") or any(x in ET.tostring(n,encoding="unicode") for x in TARGET_DATAFLOWS)]
    row=snap["row"]
    if row.get("provider")!="IMF:BR1" or row.get("dataflow")!="IMF:BOP6(1.0)":
        raise ValueError("Pinned registration snapshot identity mismatch")
    return {
      "schema_version":1,"status":"PASS_PUBLIC_REGISTRY_METADATA_CAPTURED",
      "scope":"Read-only public IMF SDMX Central structure queries. No data registration or source data changed.",
      "official_api":"https://sdmxcentral.imf.org/sdmx/v2/",
      "sources":{"data_provider_scheme":pm,"provision_agreements":am,"content_constraints":cm,
        "registration_snapshot":{"path":str(snap_path),"sha256":hashlib.sha256(snap_path.read_bytes()).hexdigest(),"row":row}},
      "provider":{"target":"IMF:BR1","matching_provider_records":providers,"match_count":len(providers),"status":"FOUND" if providers else "NOT_FOUND_IN_RETURNED_SCHEME"},
      "provision_agreements":{"total_returned":len(all_pa),"relevant_records_containing_BR1_or_BOP6_ids":relevant_pa,"relevant_count":len(relevant_pa),"status":"RELEVANT_RECORDS_FOUND" if relevant_pa else "NO_RELEVANT_RECORD_IN_RETURNED_PUBLIC_STRUCTURE"},
      "content_constraints":{"total_returned":len(all_cc),"relevant_records_containing_BR1_or_BOP6_ids":relevant_cc,"relevant_count":len(relevant_cc),"status":"RELEVANT_RECORDS_FOUND" if relevant_cc else "NO_RELEVANT_RECORD_IN_RETURNED_PUBLIC_STRUCTURE"},
      "registration_vs_payload":{"registered_dataflow":row["dataflow"],"provider":row["provider"],"payload_dataflow":"IMF:BOP_BPM6(1.0)","registered_url":row["registered_url"],"last_updated":row["last_updated"],
        "interpretation":"Public registration row records Dataflow, Provider, URL and update time. Provision Agreement and provider-level constraints must be established from returned structures; absence in a public structure response does not prove no private or unexposed agreement."},
      "decision":{"provision_agreement_semantics":"UNKNOWN_PENDING_STRUCTURE_INTERPRETATION","provider_level_constraint":"UNKNOWN_PENDING_STRUCTURE_INTERPRETATION","constraint_substitution":"PROHIBITED","brazil_portfolio_flow_panel":"NOT_AUTHORIZED","global_em_aggregate":"NOT_AUTHORIZED","trading_signal":"NOT_AUTHORIZED"}
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--provider-xml",required=True,type=Path); p.add_argument("--provision-xml",required=True,type=Path)
    p.add_argument("--constraint-xml",required=True,type=Path); p.add_argument("--registration-snapshot",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path); a=p.parse_args()
    r=audit(a.provider_xml,a.provision_xml,a.constraint_xml,a.registration_snapshot)
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":r["status"],"provider":r["provider"]["status"],"provision_agreement_status":r["provision_agreements"]["status"],"provision_agreement_count":r["provision_agreements"]["total_returned"],"constraint_status":r["content_constraints"]["status"],"constraint_count":r["content_constraints"]["total_returned"],"decision":r["decision"]},indent=2))
if __name__=="__main__": main()
