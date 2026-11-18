import json, tempfile, unittest
from pathlib import Path
from qa.audit_imf_brazil_bop_registration_contract import audit
class BrazilRegistrationContractTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
  (self.root/"provider.xml").write_text('<Structure><DataProviderSchemes><DataProviderScheme agencyID="IMF" id="DATA_PROVIDERS" version="1.0"><DataProvider id="BR1"><Name>Central Bank of Brazil</Name></DataProvider></DataProviderScheme></DataProviderSchemes></Structure>')
  (self.root/"provision.xml").write_text('<Structure><ProvisionAgreements><ProvisionAgreement agencyID="IMF" id="BR_BOP_BP6" version="1.0"><Name>Brazil Balance of Payments</Name><StructureUsage><Ref agencyID="IMF" id="BOP6" version="1.0" class="Dataflow"/></StructureUsage><DataProvider><Ref agencyID="IMF" id="BR1" class="DataProvider"/></DataProvider></ProvisionAgreement></ProvisionAgreements></Structure>')
  (self.root/"constraint.xml").write_text('<Structure><ContentConstraints><ContentConstraint agencyID="IMF" id="BOP6_CONSTRAINT" version="1.0"><ConstraintAttachment><Dataflow><Ref agencyID="IMF" id="BOP6" version="1.0" class="Dataflow"/></Dataflow></ConstraintAttachment></ContentConstraint><ContentConstraint agencyID="IMF" id="BR1_CONSTRAINT" version="1.0"><ConstraintAttachment><DataProvider><Ref agencyID="IMF" id="BR1" class="DataProvider"/></DataProvider></ConstraintAttachment></ContentConstraint></ContentConstraints></Structure>')
  (self.root/"snapshot.json").write_text(json.dumps({"row":{"dataflow":"IMF:BOP6(1.0)","provider":"IMF:BR1","registered_url":"https://bcb.gov.br/example.xml","last_updated":"2026-10-26T11:47:29.000Z"}}))
 def tearDown(self): self.tmp.cleanup()
 def test_exact_provider_dataflow_provision_contract(self):
  r=audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
  self.assertEqual(r["provider"]["status"],"FOUND"); self.assertEqual(r["provision_agreement"]["status"],"EXACT_BOP6_BR1_LINK_CONFIRMED")
  self.assertEqual(r["constraint_attachments"]["provider_level_BR1"]["count"],1); self.assertEqual(r["constraint_attachments"]["registered_dataflow_BOP6"]["count"],1)
 def test_provider_and_agreement_constraints_not_found_explicit(self):
  (self.root/"constraint.xml").write_text('<Structure><ContentConstraints><ContentConstraint agencyID="IMF" id="BOP6_CONSTRAINT"><ConstraintAttachment><Dataflow><Ref agencyID="IMF" id="BOP6" class="Dataflow"/></Dataflow></ConstraintAttachment></ContentConstraint></ContentConstraints></Structure>')
  r=audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
  self.assertEqual(r["constraint_attachments"]["provider_level_BR1"]["status"],"NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE")
  self.assertEqual(r["constraint_attachments"]["provision_agreement_level_BR_BOP_BP6"]["status"],"NOT_FOUND_IN_COMPLETE_PUBLIC_CATALOGUE")
 def test_mismatched_provider_does_not_match_exact_PA(self):
  (self.root/"provision.xml").write_text('<Structure><ProvisionAgreements><ProvisionAgreement agencyID="IMF" id="BR_BOP_BP6"><StructureUsage><Ref agencyID="IMF" id="BOP6" class="Dataflow"/></StructureUsage><DataProvider><Ref agencyID="IMF" id="US3" class="DataProvider"/></DataProvider></ProvisionAgreement></ProvisionAgreements></Structure>')
  r=audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
  self.assertEqual(r["provision_agreement"]["exact_registered_dataflow_provider_match_count"],0)
 def test_truncated_xml_fails_closed(self):
  (self.root/"provision.xml").write_text("<Structure><ProvisionAgreements>")
  with self.assertRaisesRegex(ValueError,"Incomplete or malformed SDMX XML capture"): audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
 def test_snapshot_identity_fails_closed(self):
  (self.root/"snapshot.json").write_text(json.dumps({"row":{"dataflow":"IMF:BOP_BPM6(1.0)","provider":"IMF:BR1","registered_url":"https://bcb.gov.br/example.xml","last_updated":"2026-10-26T11:47:29.000Z"}}))
  with self.assertRaises(ValueError): audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
if __name__=="__main__": unittest.main()
