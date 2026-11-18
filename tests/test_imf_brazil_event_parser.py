import unittest
from scripts.research.imf_brazil_event_parser import (
    inspect_bytes, RI_NS, REG_NS, BCB_URL, BRAZIL_PA_URN
)


def doc(body):
    return (f'<RegistryInterface xmlns="{RI_NS}"><Header/><{body}</RegistryInterface>').encode()


def registration(action="Replace", pa="", datasource=""):
    return (f'<SubmitRegistrationsRequest xmlns:r="{REG_NS}"><r:RegistrationRequest action="{action}">'
            f'<r:Registration><r:ProvisionAgreement>{pa}</r:ProvisionAgreement>'
            f'<r:Datasource>{datasource}</r:Datasource></r:Registration>'
            f'</r:RegistrationRequest></SubmitRegistrationsRequest>')


class ParserTests(unittest.TestCase):
    def test_exact_brazil_pa_candidate_never_auto_pass(self):
        r = inspect_bytes(doc(registration(pa=f'<Ref>{BRAZIL_PA_URN}</Ref>')))
        self.assertTrue(r["brazil_registration_candidate"])
        self.assertEqual(r["acceptance"], "REQUIRES_MANUAL_EVIDENCE_REVIEW")
        self.assertTrue(r["registrations"][0]["action_enum_valid"])

    def test_exact_bcb_datasource_candidate(self):
        r = inspect_bytes(doc(registration(datasource=f'<SimpleDataSource>{BCB_URL}</SimpleDataSource>')))
        self.assertTrue(r["brazil_registration_candidate"])
        self.assertTrue(r["registrations"][0]["bcb_url_exact_match"])

    def test_narrative_outside_registration_does_not_match(self):
        inner = registration().replace(f'<SubmitRegistrationsRequest xmlns:r="{REG_NS}">', '', 1).replace('</SubmitRegistrationsRequest>', '', 1)
        body = f'<SubmitRegistrationsRequest xmlns:r="{REG_NS}"><Description>{BCB_URL}</Description>{inner}</SubmitRegistrationsRequest>'
        self.assertFalse(inspect_bytes(doc(body))["brazil_registration_candidate"])

    def test_brazil_pa_text_outside_registration_does_not_match(self):
        inner = registration().replace(f'<SubmitRegistrationsRequest xmlns:r="{REG_NS}">', '', 1).replace('</SubmitRegistrationsRequest>', '', 1)
        body = f'<SubmitRegistrationsRequest xmlns:r="{REG_NS}"><Annotation>{BRAZIL_PA_URN}</Annotation>{inner}</SubmitRegistrationsRequest>'
        self.assertFalse(inspect_bytes(doc(body))["brazil_registration_candidate"])

    def test_message_namespace_children_are_not_mistaken_for_registry_elements(self):
        body = f'<SubmitRegistrationsRequest><RegistrationRequest action="Replace"><Registration><ProvisionAgreement><Ref>{BRAZIL_PA_URN}</Ref></ProvisionAgreement><Datasource><SimpleDataSource>{BCB_URL}</SimpleDataSource></Datasource></Registration></RegistrationRequest></SubmitRegistrationsRequest>'
        result = inspect_bytes(doc(body))
        self.assertEqual(result["classification"], "QUARANTINE")
        self.assertFalse(result["brazil_registration_candidate"])

    def test_action_enum_is_preserved_and_checked(self):
        for action in ("Append", "Replace", "Delete", "Information"):
            r = inspect_bytes(doc(registration(action=action, pa=f'<Ref>{BRAZIL_PA_URN}</Ref>')))
            self.assertTrue(r["registrations"][0]["action_enum_valid"], action)
            self.assertEqual(r["registrations"][0]["action_raw"], action)
        r = inspect_bytes(doc(registration(action="ReRegister", pa=f'<Ref>{BRAZIL_PA_URN}</Ref>')))
        self.assertFalse(r["registrations"][0]["action_enum_valid"])

    def test_source_last_updated_not_renamed_as_event_timestamp(self):
        body = registration(pa=f'<Ref>{BRAZIL_PA_URN}</Ref>').replace(
            '<Registration>', '<Registration lastUpdated="2026-10-26T11:47:29Z">')
        r = inspect_bytes(doc(body))
        self.assertEqual(r["registrations"][0]["source_last_updated"], "2026-10-26T11:47:29Z")
        self.assertNotIn("transaction_timestamp", r["registrations"][0])

    def test_structure_request_is_not_registration(self):
        r = inspect_bytes(doc('<SubmitStructureRequest><Text>Brazil IMF:BR1</Text></SubmitStructureRequest>'))
        self.assertEqual(r["classification"], "STRUCTURE_EVENT")
        self.assertFalse(r["brazil_registration_candidate"])

    def test_chile_is_not_brazil(self):
        r = inspect_bytes(doc(registration(datasource='<SimpleDataSource>https://si3.bcentral.cl/data.xml</SimpleDataSource>')))
        self.assertFalse(r["brazil_registration_candidate"])

    def test_bop6_alone_is_not_brazil(self):
        r = inspect_bytes(doc(registration(pa='<Ref>IMF:BOP6(1.0)</Ref>')))
        self.assertFalse(r["brazil_registration_candidate"])

    def test_wrong_namespace_quarantined(self):
        self.assertEqual(inspect_bytes(b'<RegistryInterface><SubmitRegistrationsRequest/></RegistryInterface>')["classification"], "QUARANTINE")

    def test_malformed_xml_quarantined(self):
        self.assertEqual(inspect_bytes(b'<RegistryInterface>')["classification"], "QUARANTINE")

    def test_nested_fake_request_not_accepted(self):
        body = f'<SubmitRegistrationsRequest><Annotation><SubmitRegistrationsRequest>{registration(pa=f"<Ref>{BRAZIL_PA_URN}</Ref>")}</SubmitRegistrationsRequest></Annotation></SubmitRegistrationsRequest>'
        self.assertFalse(inspect_bytes(doc(body))["brazil_registration_candidate"])


if __name__ == "__main__":
    unittest.main()
