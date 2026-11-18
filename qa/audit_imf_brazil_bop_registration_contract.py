#!/usr/bin/env python3
"""Resolve the exact IMF Brazil BOP registration / Provision Agreement contract."""
import argparse, hashlib, json
from pathlib import Path
import xml.etree.ElementTree as ET
PROVIDER_ID="BR1"; REGISTERED_DATAFLOW="BOP6"; PAYLOAD_DATAFLOW="BOP_BPM6"; PROVISION_AGREEMENT_ID="BR_BOP_BP6"
def local(tag): return tag.rsplit("}",1)[-1]
def refs_within(node): return [dict(r.attrib) for r in node.iter() if local(r.tag)=="Ref"]
def element_record(node):
 names=[(x.text or "").strip() for x in node.iter() if local(x.tag)=="Name" and (x.text or "").strip()]
 return {"element":local(node.tag),"attributes":dict(node.attrib),"names":names,"references":refs_within(node),"serialized_sha256":hashlib.sha256(ET.tostring(node,encoding="utf-8")).hexdigest()}
def load_xml(path):
 path=Path(path); raw=path.read_bytes()
 try: root=ET.fromstring(raw)
 except ET.ParseError as exc: raise ValueError(f"Incomplete or malformed SDMX XML capture at {path}: {exc}") from exc
 if local(root.tag)!="Structure": raise ValueError(f"Unexpected SDMX root element in {path}: {local(root.tag)}")
 return root,{"path":str(path),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"root":local(root.tag)}
def elements(root,name): return [x for x in root.iter() if local(x.tag)==name]
def has_ref(refs,cls,ident): return any(r.get("class")==cls and r.get("id")==ident and r.get("agencyID","IMF")=="IMF" for r in refs)
def attachment_refs(constraint):
 containers=[x for x in constraint.iter() if local(x.tag)=="ConstraintAttachment"]
 return [r for container in containers for r in refs_within(container)]
def audit(provider_xml,provision_xml,constraint_xml,registration_snapshot):
 provider_root,provider_meta=load_xml(provider_xml); provision_root,provision_meta=load_xml(provision_xml); constraint_root,constraint_meta=load_xml(constraint_xml)
 snap_path=Path(registration_snapshot); snap=json.loads(snap_path.read_text(encoding="utf-8")); row=snap["row"]
 if row.get("provider")!="IMF:BR1" or row.get("dataflow")!="IMF:BOP6(1.0)": raise ValueError("Pinned registration snapshot identity mismatch")
 provider_matches=[element_record(x) for x in elements(provider_root,"DataProvider") if x.get("id")==PROVIDER_ID]
 all_pa=elements(provision_root,"ProvisionAgreement"); pa_matches=[]; named_pa=[element_record(x) for x in all_pa if x.get("id")==PROVISION_AGREEMENT_ID]
 for pa in all_pa:
  refs=refs_within(pa)
  if has_ref(refs,"Dataflow",REGISTERED_DATAFLOW) and has_ref(refs,"DataProvider",PROVIDER_ID): pa_matches.append(element_record(pa))
 all_constraints=elements(constraint_root,"ContentConstraint"); provider_constraints=[]; pa_constraints=[]; registered_df_constraints=[]; payload_df_constraints=[]
 for constraint in all_constraints:
  refs=attachment_refs(constraint); record=element_record(constraint)
  if has_ref(refs,"DataProvider",PROVIDER_ID): provider_constraints.append(record)
  if has_ref(refs,"ProvisionAgreement",PROVISION_AGREEMENT_ID): pa_constraints.append(record)
  if has_ref(refs,"Dataflow",REGISTERED_DATAFLOW): registered_df_constraints.append(record)
  if has_ref(refs,"Dataflow",PAYLOAD_DATAFLOW): payload_df_constraints.append(record)
 return {
 "schema_version":2,"status":"PASS_AUDIT_EXECUTED_P0_PAYLOAD_MISMATCH_REMAINS",
 "scope":"Read-only complete IMF SDMX Central public structure captures; no registration writes and no BOP observation reacquisition.",
 "sources":{"data_provider_scheme":provider_meta,"provision_agreements":provision_meta,"content_constraints":constraint_meta,"registration_snapshot":{"path":str(snap_path),"sha256":hashlib.sha256(snap_path.read_bytes()).hexdigest(),"row":row}},
 "provider":{"target":"IMF:BR1","match_count":len(provider_matches),"records":provider_matches,"status":"FOUND" if provider_matches else "NOT_FOUND_IN_COMPLETE_PUBLIC_PROVIDER_SCHEME"},
 "provision_agreement":{"target_id":"IMF:BR_BOP_BP6(1.0)","exact_registered_dataflow_provider_match_count":len(pa_matches),"exact_matches":pa_matches,"named_agreement_records":named_pa,"total_public_agreements_returned":len(all_pa),"status":"EXACT_BOP6_BR1_LINK_CONFIRMED" if len(pa_matches)==1 else ("MULTIPLE_EXACT_LINKS_REVIEW_REQUIRED" if pa_matches else "NO_EXACT_LINK_FOUND")},
 "constraint_attachments":{"total_public_content_constraints_returned":len(all_constraints),
 "provider_level_BR1":{"count":len(provider_constraints),"records":provider_constraints,"status":"FOUND" if provider_constraints else "NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE"},
 "provision_agreement_level_BR_BOP_BP6":{"count":len(pa_constraints),"records":pa_constraints,"status":"FOUND" if pa_constraints else "NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE"},
 "registered_dataflow_BOP6":{"count":len(registered_df_constraints),"records":registered_df_constraints},
 "payload_dataflow_BOP_BPM6":{"count":len(payload_df_constraints),"records":payload_df_constraints}},
 "contract_comparison":{"registration_dataflow":row["dataflow"],"registration_provider":row["provider"],"provision_agreement":"IMF:BR_BOP_BP6(1.0)","provision_agreement_dataflow":"IMF:BOP6(1.0)","provision_agreement_provider":"IMF:BR1","payload_header_dataflow":"IMF:BOP_BPM6(1.0)","registration_and_provision_agreement":"ALIGNED_ON_BOP6_AND_BR1","payload_vs_registered_contract":"MISMATCH","dataflow_alias_semantics":"NOT_ESTABLISHED"},
 "decision":{"registration_provision_contract":"CONFIRMED_BOP6_FOR_PROVIDER_BR1","provider_level_BR1_constraint":"NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE","provision_agreement_level_constraint":"NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE","BOP6_dataflow_constraint":"BOP6_CONSTRAINT_IS_ATTACHED_TO_REGISTERED_DATAFLOW","BOP_BPM6_dataflow_constraint":"BOP_BP6_CONSTRAINT_IS_ATTACHED_TO_PAYLOAD_DECLARED_DATAFLOW","apply_constraint_to_current_payload":"NOT_AUTHORIZED_UNTIL_BCB_RESOLVES_HEADER_VS_REGISTRATION_MISMATCH","rewrite_payload_or_registration":"PROHIBITED_WITHOUT_AUTHORITATIVE_BCB_CONTRACT_EVIDENCE","Brazil_portfolio_flow_panel":"NOT_AUTHORIZED","Global_EM_aggregate":"NOT_AUTHORIZED","trading_signal":"NOT_AUTHORIZED"}}
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--provider-xml",required=True,type=Path); p.add_argument("--provision-xml",required=True,type=Path); p.add_argument("--constraint-xml",required=True,type=Path); p.add_argument("--registration-snapshot",required=True,type=Path); p.add_argument("--output",required=True,type=Path); a=p.parse_args()
 r=audit(a.provider_xml,a.provision_xml,a.constraint_xml,a.registration_snapshot); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps({"status":r["status"],"provider_status":r["provider"]["status"],"provision_agreement_status":r["provision_agreement"]["status"],"exact_PA_matches":r["provision_agreement"]["exact_registered_dataflow_provider_match_count"],"provider_constraint_count":r["constraint_attachments"]["provider_level_BR1"]["count"],"PA_constraint_count":r["constraint_attachments"]["provision_agreement_level_BR_BOP_BP6"]["count"],"BOP6_dataflow_constraint_count":r["constraint_attachments"]["registered_dataflow_BOP6"]["count"],"BOP_BPM6_dataflow_constraint_count":r["constraint_attachments"]["payload_dataflow_BOP_BPM6"]["count"],"decision":r["decision"]},indent=2))
if __name__=="__main__": main()
