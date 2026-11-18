import json, tempfile, unittest
from pathlib import Path
from qa.audit_imf_brazil_bop_registration_contract import audit

class BrazilRegistrationContractTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
  (self.root/"provider.xml").write_text('<Structure><DataProviderSchemes><DataProviderScheme agencyID="IMF" id="DATA_PROVIDERS" version="1.0"><DataProvider id="BR1"><Name>Central Bank of Brazil</Name></DataProvider></DataProviderScheme></DataProviderSchemes></Structure>')
  (self.root/"provision.xml").write_text('<Structure><ProvisionAgreements><ProvisionAgreement agencyID="IMF" id="BR_BOP" version="1.0"><Name>Brazil BOP</Name><StructureUsage><Ref agencyID="IMF" id="BOP6" version="1.0"/></StructureUsage><StructureProvider><Ref agencyID="IMF" id="DATA_PROVIDERS" version="1.0" class="DataProviderScheme"/><Ref id="BR1"/></StructureProvider></ProvisionAgreement></ProvisionAgreements></Structure>')
  (self.root/"constraint.xml").write_text('<Structure><ContentConstraints><ContentConstraint agencyID="IMF" id="BR1_CONSTRAINT" version="1.0"><ConstraintAttachment><DataProvider><Ref agencyID="IMF" id="DATA_PROVIDERS" version="1.0" class="DataProviderScheme"/><Ref id="BR1"/></DataProvider></ConstraintAttachment></ContentConstraint></ContentConstraints></Structure>')
  (self.root/"snapshot.json").write_text(json.dumps({"row":{"dataflow":"IMF:BOP6(1.0)","provider":"IMF:BR1","registered_url":"https://bcb.gov.br/example.xml","last_updated":"2026-10-26T11:47:29.000Z"}}))
 def tearDown(self): self.tmp.cleanup()
 def test_finds_provider_and_linked_provision_and_constraint(self):
  r=audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
  self.assertEqual(r["provider"]["status"],"FOUND"); self.assertEqual(r["provision_agreements"]["relevant_count"],1)
  self.assertEqual(r["content_constraints"]["relevant_count"],1); self.assertEqual(r["decision"]["constraint_substitution"],"PROHIBITED")
 def test_no_provider_match_not_promoted_to_pass(self):
  (self.root/"provider.xml").write_text("<Structure><DataProviderSchemes/></Structure>")
  r=audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
  self.assertEqual(r["provider"]["status"],"NOT_FOUND_IN_RETURNED_SCHEME")
  self.assertEqual(r["decision"]["provision_agreement_semantics"],"UNKNOWN_PENDING_STRUCTURE_INTERPRETATION")
 def test_truncated_xml_fails_closed_with_capture_path(self):
  (self.root/"provision.xml").write_text("<Structure><ProvisionAgreements>")
  with self.assertRaisesRegex(ValueError,"Incomplete or malformed SDMX XML capture"):
   audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
 def test_snapshot_identity_fail_closed(self):
  (self.root/"snapshot.json").write_text(json.dumps({"row":{"dataflow":"IMF:BOP_BPM6(1.0)","provider":"IMF:BR1","registered_url":"https://bcb.gov.br/example.xml","last_updated":"2026-10-26T11:47:29.000Z"}}))
  with self.assertRaises(ValueError): audit(self.root/"provider.xml",self.root/"provision.xml",self.root/"constraint.xml",self.root/"snapshot.json")
if __name__=="__main__": unittest.main()
