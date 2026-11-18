import unittest
from scripts.research.imf_brazil_event_parser import inspect_bytes, RI_NS, BCB_URL

def doc(body):
    return (f'<RegistryInterface xmlns="{RI_NS}">{body}</RegistryInterface>').encode()

class ParserTests(unittest.TestCase):
    def test_exact_provider_candidate_never_auto_pass(self):
        x = doc('<SubmitRegistrationsRequest><Registration><DataProviderRef>IMF:BR1</DataProviderRef><DataflowRef>IMF:BOP6(1.0)</DataflowRef></Registration></SubmitRegistrationsRequest>')
        r = inspect_bytes(x)
        self.assertTrue(r["brazil_registration_candidate"])
        self.assertEqual(r["acceptance"], "REQUIRES_MANUAL_EVIDENCE_REVIEW")

    def test_exact_bcb_url_candidate(self):
        x = doc(f'<SubmitRegistrationsRequest><Registration><SimpleDataSource>{BCB_URL}</SimpleDataSource></Registration></SubmitRegistrationsRequest>')
        self.assertTrue(inspect_bytes(x)["brazil_registration_candidate"])

    def test_url_embedded_in_narrative_is_not_exact_match(self):
        x = doc(f'<SubmitRegistrationsRequest><Registration><Description>See {BCB_URL} for context</Description></Registration></SubmitRegistrationsRequest>')
        self.assertFalse(inspect_bytes(x)["brazil_registration_candidate"])

    def test_registration_action_attribute_is_captured(self):
        x = doc('<SubmitRegistrationsRequest><RegistrationRequest action="Replace"><DataProviderRef>IMF:BR1</DataProviderRef><DataflowRef>IMF:BOP6(1.0)</DataflowRef></RegistrationRequest></SubmitRegistrationsRequest>')
        r = inspect_bytes(x)
        self.assertTrue(r["brazil_registration_candidate"])
        self.assertIn("Replace", r["action_candidates"])

    def test_structure_request_is_not_registration(self):
        x = doc('<SubmitStructureRequest><Text>Brazil IMF:BR1</Text></SubmitStructureRequest>')
        r = inspect_bytes(x)
        self.assertEqual(r["classification"], "STRUCTURE_EVENT")
        self.assertFalse(r["brazil_registration_candidate"])

    def test_chile_is_not_brazil(self):
        x = doc('<SubmitRegistrationsRequest><Registration><DataProviderRef>IMF:CL2</DataProviderRef><SimpleDataSource>https://si3.bcentral.cl/data.xml</SimpleDataSource></Registration></SubmitRegistrationsRequest>')
        self.assertFalse(inspect_bytes(x)["brazil_registration_candidate"])

    def test_bop6_alone_is_not_brazil(self):
        x = doc('<SubmitRegistrationsRequest><Registration><DataflowRef>IMF:BOP6(1.0)</DataflowRef></Registration></SubmitRegistrationsRequest>')
        self.assertFalse(inspect_bytes(x)["brazil_registration_candidate"])

    def test_wrong_namespace_quarantined(self):
        x = b'<RegistryInterface><SubmitRegistrationsRequest/></RegistryInterface>'
        self.assertEqual(inspect_bytes(x)["classification"], "QUARANTINE")

    def test_malformed_xml_quarantined(self):
        self.assertEqual(inspect_bytes(b'<RegistryInterface>')["classification"], "QUARANTINE")

if __name__ == "__main__":
    unittest.main()
