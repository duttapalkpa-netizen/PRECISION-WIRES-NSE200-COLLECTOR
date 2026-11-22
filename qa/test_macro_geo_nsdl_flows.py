import unittest
from datetime import date
import pandas as pd

from pipeline.macro_geo_nsdl_flows import coverage_audit, derive_collection_status


class NsdlCoverageAuditTests(unittest.TestCase):
    def test_failed_dii_query_is_visible_even_when_fpi_has_no_row_for_that_date(self):
        # Test-only fixtures; these are not research observations.
        frame = pd.DataFrame([
            {"DATE": "2026-07-16", "GROUP": "FPI"},
            {"DATE": "2026-07-16", "GROUP": "DII"},
            {"DATE": "2026-07-17", "GROUP": "FPI"},
        ])
        attempts = [
            {"date": "2026-07-16", "status": "SUCCESS"},
            {"date": "2026-07-17", "status": "FAILED", "error": "schema not recognized"},
            {"date": "2026-08-26", "status": "FAILED", "error": "schema not recognized"},
        ]
        audit = coverage_audit(frame, date(2026, 6, 23), date(2026, 11, 20), attempts)
        self.assertEqual(audit["dii_query_attempts"], 3)
        self.assertEqual(audit["dii_query_successes"], 1)
        self.assertEqual(audit["dii_query_failures"], 2)
        self.assertEqual(audit["dii_query_failed_dates"], ["2026-07-17", "2026-08-26"])
        self.assertEqual(audit["dii_missing_fpi_archive_dates"], ["2026-07-17"])
        self.assertEqual(audit["quality"], "AVAILABLE_WITH_GAPS")

    def test_collection_status_never_calls_partial_or_failed_collection_available(self):
        self.assertEqual(derive_collection_status(False, [], {"quality": "AVAILABLE"}), "BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE")
        self.assertEqual(derive_collection_status(True, ["DII date query failed"], {"quality": "AVAILABLE_WITH_GAPS"}), "AVAILABLE_WITH_GAPS")
        self.assertEqual(derive_collection_status(True, [], {"quality": "AVAILABLE"}), "AVAILABLE")


if __name__ == "__main__":
    unittest.main()
