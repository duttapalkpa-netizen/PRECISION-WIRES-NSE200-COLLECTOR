"""Fail-closed contracts for official macro release/vintage evidence.

These tests intentionally validate conservative source semantics; they do not
claim that historical publication vintages have been recovered.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def source(path):
    return (ROOT / path).read_text(encoding="utf-8")

class ReleaseVintageFailClosedContracts(unittest.TestCase):
    def test_rbi_observation_release_time_is_not_fabricated(self):
        s = source("pipeline/collect_rbi_dbie_bond_yields.py")
        self.assertIn('"RELEASED_AT":""', s)
        self.assertIn('"RELEASE_STATUS":"UNKNOWN_NOT_SUPPLIED_PER_OBSERVATION"', s)
        self.assertIn('"release_timestamp_status":"UNKNOWN_NOT_SUPPLIED_PER_OBSERVATION"', s)
        self.assertIn("not daily FBIL 10-year par-yield benchmark", s)
        self.assertNotIn('RELEASED_AT"] = metadata["loaded_at"]', s)

    def test_cga_latest_dashboard_is_not_misrepresented_as_historical_vintage(self):
        s = source("pipeline/collect_cga_monthly_historical_series.py")
        self.assertIn('"workbook_publication_date":"NOT_STATED_ON_SOURCE_PAGE"', s)
        self.assertIn('"vintage_status":"VINTAGE_UNVERIFIED_SINGLE_LATEST_SNAPSHOT"', s)
        self.assertIn("source page last-updated date is not treated as workbook publication timestamp", s)

    def test_gdp_single_quarter_smoke_does_not_claim_full_history(self):
        s = source("pipeline/collect_mospi_nas_gdp_smoke.py")
        self.assertIn('TABLE_ID = "AEQEAFY2607QTR"', s)
        self.assertIn("single first-page exact-ID lookup; no full catalogue crawl", s)
        self.assertIn("not a complete", s.lower())

    def test_cpi_base_break_and_bounded_scope_are_explicit(self):
        s = source("pipeline/collect_mospi_cpi_2024_smoke.py")
        self.assertIn('"release_date_precision":"date"', s)
        self.assertIn("not a complete monthly historical series", s)
        self.assertIn("CPI 2012=100 data are not merged", s)

    def test_wpi_item_values_do_not_claim_item_level_revision_status(self):
        itemwise = source("pipeline/collect_oea_wpi_itemwise.py")
        crosswalk = source("pipeline/build_oea_wpi_release_status_crosswalk.py")
        self.assertIn('"revision_status": "NOT_STATED_IN_WORKBOOK"', itemwise)
        self.assertIn("Month-level official revision status only", crosswalk)
        self.assertIn("UNKNOWN_NOT_COVERED_BY_REVIEWED_RELEASE", crosswalk)
        self.assertIn("SOURCE_EVIDENCE_ONLY_NOT_PROMOTED_TO_FACTOR_REGISTRY", crosswalk)

    def test_hard_gate_and_production_logic_are_not_weakened_by_evidence_register(self):
        s = source("research/evidence/official_release_vintage_source_audit_2026-11-02.md")
        self.assertIn("Hard Gate remains BLOCKED", s)
        self.assertIn("No production changes", s)
        self.assertIn("All source gaps remain UNKNOWN", s)

if __name__ == "__main__":
    unittest.main()
