import unittest
from pipeline.audit_oea_wpi_factor_registry_eligibility import audit_eligibility

class WpiFactorEligibilityTests(unittest.TestCase):
    def fixture(self):
        registry=[{"factor_id":"F14","factor":"Global inflation and inflation expectations"}]
        source='"F14":["macro_indicators","us_yields","india_bond_yields","inflation_components"],'
        cross={"crosswalk_rows":43,"status_counts":{
          "UNKNOWN_NOT_COVERED_BY_REVIEWED_RELEASE":36,"FINAL":4,"PROVISIONAL":2,
          "NOT_YET_RELEASED_AS_OF_2026-11-01":1}}
        fields=["source_sheet","source_row","item_code","item_label","period","value","revision_status"]
        evidence={"publisher":"Press Information Bureau","source_url":"https://pib.gov.in/x",
          "published_date":"2026-10-14","official_month_status":{
            "2026-04":"FINAL","2026-05":"FINAL","2026-06":"FINAL","2026-07":"FINAL",
            "2026-08":"PROVISIONAL","2026-09":"PROVISIONAL"}}
        return registry,source,cross,fields,evidence
    def test_wpi_candidate_does_not_promote_without_release_provenance(self):
        result=audit_eligibility(*self.fixture())
        self.assertEqual(result["status"],"WPI_FACTOR_REGISTRY_ELIGIBILITY_AUDIT_PASS")
        self.assertEqual(result["candidate_factor"]["factor_id"],"F14")
        self.assertEqual(result["promotion_decision"],"NOT_ELIGIBLE")
        self.assertIn("RELEASED_AT",result["source_schema"]["missing_required_fields"])
        self.assertIn("SOURCE_URL",result["source_schema"]["missing_required_fields"])
        self.assertEqual(result["factor_registry_impact"],"NO_CHANGE_F14_REMAINS_UNPROMOTED")
        self.assertEqual(result["hard_gate"],"UNCHANGED_BLOCKED_UNTIL_ALL_REQUIRED_P0_AND_FACTOR_EVIDENCE_GATES_PASS")
    def test_missing_f14_or_mapping_fails_closed(self):
        registry,source,cross,fields,evidence=self.fixture()
        with self.assertRaises(ValueError): audit_eligibility([],source,cross,fields,evidence)
        with self.assertRaises(ValueError): audit_eligibility(registry,'"F14":["macro_indicators"],',cross,fields,evidence)
if __name__=="__main__": unittest.main()
