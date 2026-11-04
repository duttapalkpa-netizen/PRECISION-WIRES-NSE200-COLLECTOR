import unittest
from pipeline.macro_geo_finalize_manifest import REQUIRED_P0, reconcile


class FinalManifestReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {
            "operational_status": "PASS_WITH_CRITICAL_DATA_GAPS",
            "p0_coverage": {
                "required_series_available": False,
                "fpi_dii_status": "UNKNOWN/BLOCKED",
                "corporate_events_status": "UNKNOWN/BLOCKED",
            },
        }
        self.groups = {
            name: {"status": "AVAILABLE", "rows": 10}
            for name in REQUIRED_P0
        }
        self.coverage = {"p0_coverage": {"status": "P0_COMPLETE", "groups": self.groups}}

    def test_final_evidence_reconciles_stale_pre_repair_manifest(self):
        repair = {"groups": {"corporate_events": {"status": "AVAILABLE", "rows": 12}}}
        result = reconcile(self.manifest, self.coverage, repair, {"status": "AVAILABLE"})
        self.assertEqual(result["operational_status"], "PASS_WITH_GAPS")
        self.assertTrue(result["p0_coverage"]["required_series_available"])
        self.assertEqual(result["p0_coverage"]["fpi_dii_status"], "AVAILABLE")
        self.assertEqual(result["p0_coverage"]["corporate_events_status"], "AVAILABLE")
        self.assertEqual(result["final_manifest_reconciliation"]["blocked_p0_groups"], [])

    def test_any_missing_group_remains_blocked(self):
        self.groups["fpi_dii_flows"] = {"status": "INSUFFICIENT_HISTORICAL_COVERAGE", "rows": 199}
        result = reconcile(self.manifest, self.coverage)
        self.assertEqual(result["operational_status"], "PASS_WITH_CRITICAL_DATA_GAPS")
        self.assertFalse(result["p0_coverage"]["required_series_available"])
        self.assertEqual(result["p0_coverage"]["fpi_dii_status"], "BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE")
        self.assertIn("fpi_dii_flows", result["final_manifest_reconciliation"]["blocked_p0_groups"])

    def test_corporate_events_require_repair_provenance(self):
        result = reconcile(self.manifest, self.coverage, {"groups": {}}, {"status": "AVAILABLE"})
        self.assertEqual(result["p0_coverage"]["corporate_events_status"], "BLOCKED_SOURCE_OR_SCHEMA_UNVERIFIED")
        self.assertEqual(result["operational_status"], "PASS_WITH_CRITICAL_DATA_GAPS")

    def test_missing_coverage_group_is_not_assumed_available(self):
        del self.groups["geopolitical_events"]
        result = reconcile(self.manifest, self.coverage)
        self.assertFalse(result["p0_coverage"]["required_series_available"])
        self.assertIn("geopolitical_events", result["final_manifest_reconciliation"]["blocked_p0_groups"])


if __name__ == "__main__":
    unittest.main()
