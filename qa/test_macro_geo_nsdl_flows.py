import unittest
from datetime import date
import pandas as pd

from pipeline.macro_geo_nsdl_flows import clip_to_window, coverage_audit

class NsdlFlowWindowTests(unittest.TestCase):
    def test_monthly_fpi_rows_are_clipped_to_declared_window(self):
        frame = pd.DataFrame([
            {"DATE": "2026-06-01", "GROUP": "FPI", "NET_VALUE": 10},
            {"DATE": "2026-06-23", "GROUP": "FPI", "NET_VALUE": 20},
            {"DATE": "2026-11-20", "GROUP": "FPI", "NET_VALUE": 30},
            {"DATE": "2026-11-21", "GROUP": "FPI", "NET_VALUE": 40},
            {"DATE": "not-a-date", "GROUP": "FPI", "NET_VALUE": 50},
        ])
        clipped = clip_to_window(frame, date(2026, 6, 23), date(2026, 11, 20))
        self.assertEqual(clipped["DATE"].tolist(), ["2026-06-23", "2026-11-20"])

    def test_coverage_audit_reports_exact_dii_gap_without_filling_it(self):
        frame = pd.DataFrame([
            {"DATE": "2026-06-23", "GROUP": "FPI"},
            {"DATE": "2026-06-24", "GROUP": "FPI"},
            {"DATE": "2026-06-23", "GROUP": "DII"},
        ])
        result = coverage_audit(frame, date(2026, 6, 23), date(2026, 11, 20))
        self.assertEqual(result["dii_missing_fpi_archive_dates"], ["2026-06-24"])
        self.assertEqual(result["dii_coverage_vs_fpi_archive_dates_pct"], 50.0)
        self.assertEqual(result["quality"], "AVAILABLE_WITH_GAPS")
        self.assertEqual(len(frame), 3)

    def test_complete_date_alignment_is_reported_separately(self):
        frame = pd.DataFrame([
            {"DATE": "2026-06-23", "GROUP": "FPI"},
            {"DATE": "2026-06-23", "GROUP": "DII"},
        ])
        result = coverage_audit(frame, date(2026, 6, 23), date(2026, 11, 20))
        self.assertEqual(result["quality"], "AVAILABLE")
        self.assertEqual(result["dii_missing_fpi_archive_dates"], [])

if __name__ == "__main__":
    unittest.main()