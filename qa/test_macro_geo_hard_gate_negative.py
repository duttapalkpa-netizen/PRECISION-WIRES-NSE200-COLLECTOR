import contextlib
import json
import tempfile
from io import StringIO
import unittest
from pathlib import Path
from unittest.mock import patch

import pipeline.macro_geo_hard_gate as gate


class HardGateNegativeContractTests(unittest.TestCase):
    def _fixture(self, root, panel_date="2026-10-30", equity_date="2026-10-30"):
        paths = {
            "COVERAGE": root / "coverage.json",
            "EVENT_REPORT": root / "event.json",
            "EVENT_AUDIT": root / "event_audit.json",
            "PANEL": root / "market_panel.csv",
            "EQUITY": root / "equity.csv",
            "MANIFEST": root / "manifest.json",
            "REPAIR": root / "repair.json",
            "FACTOR_COVERAGE": root / "factor_coverage.json",
            "REGIME_REPORT": root / "regime.json",
            "NSDL_REPORT": root / "nsdl.json",
            "FACTOR_ROWS": root / "factor_rows.csv",
            "OUT": root / "hard_gate_report.json",
        }
        groups = {name: {"status": "AVAILABLE", "rows": 2} for name in (
            "benchmark_index", "sector_indices", "volatility", "crude_oil",
            "usd_inr", "fpi_dii_flows", "corporate_events", "geopolitical_events")}
        paths["COVERAGE"].write_text(json.dumps({"p0_coverage": {
            "status": "P0_COMPLETE", "available_count": 8, "required_count": 8, "groups": groups}}))
        paths["EVENT_REPORT"].write_text(json.dumps({
            "research_status": "COMPUTED_EXPLORATORY", "eligible_event_rows": 1, "window_rows": 1}))
        paths["EVENT_AUDIT"].write_text(json.dumps({
            "unique_events_with_mature_h1": 1, "unique_events_with_mature_h5": 1}))
        paths["PANEL"].write_text(
            "DATE,SERIES,CLOSE\n" + panel_date + ",NIFTY 50,25000\n" + panel_date + ",INDIA VIX,15\n")
        paths["EQUITY"].write_text(
            "DATE,SYMBOL,CLOSE_PRICE\n" + equity_date + ",ABC,100\n")
        required = list(groups)
        paths["MANIFEST"].write_text(json.dumps({
            "operational_status": "PASS",
            "p0_coverage": {
                "required_series_available": True,
                "fpi_dii_status": "AVAILABLE",
                "corporate_events_status": "AVAILABLE",
                "required_groups": required,
                "group_availability_after_repair": {name: True for name in required}},
            "final_manifest_reconciliation": {"status": "RECONCILED"}}))
        paths["REPAIR"].write_text(json.dumps({"groups": {
            "fpi_dii_flows": {"status": "AVAILABLE"},
            "corporate_events": {"status": "AVAILABLE"}}}))
        paths["NSDL_REPORT"].write_text(json.dumps({"status": "AVAILABLE", "groups": {
            "FPI": {"unique_dates": 60, "span_days": 90},
            "DII": {"unique_dates": 60, "span_days": 90}}}))
        paths["FACTOR_COVERAGE"].write_text(json.dumps({
            "factor_groups": 1, "fully_available_schema_groups": 1, "not_connected": 0}))
        paths["FACTOR_ROWS"].write_text("factor_id,status\nF01,AVAILABLE\n")
        paths["REGIME_REPORT"].write_text(json.dumps({
            "research_status": "COMPUTED_EXPLORATORY", "window_rows": 1,
            "regime_anchors": 1, "regimes_with_windows": 1, "anchor_coverage_complete": True}))
        return paths

    def _run(self, paths):
        stack = contextlib.ExitStack()
        for name, path in paths.items():
            stack.enter_context(patch.object(gate, name, path))
        with stack, contextlib.redirect_stdout(StringIO()):
            rc = gate.main()
        return rc, json.loads(paths["OUT"].read_text())

    def test_missing_required_input_fails_closed_and_stays_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = self._fixture(root)
            paths["COVERAGE"] = root / "missing_coverage.json"
            rc, report = self._run(paths)
            self.assertEqual(rc, 1)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertFalse(report["candidate_release_allowed"])
            self.assertEqual(report["missing_data_semantics"], "UNKNOWN/BLOCKED; never interpreted as negative evidence")
            self.assertFalse(report["production_selector_changed"])
            self.assertFalse(report["ranking_score_changed"])
            self.assertFalse(report["pressure_fade_changed"])
            self.assertTrue(any(x.startswith("MISSING_REQUIRED_INPUT:") for x in report["blockers"]))

    def test_stale_or_misaligned_market_panel_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = self._fixture(root, panel_date="2026-10-01", equity_date="2026-10-14")
            rc, report = self._run(paths)
            self.assertEqual(rc, 1)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertFalse(report["candidate_release_allowed"])
            self.assertIn("MARKET_PANEL_STALE_OR_DATE_MISALIGNED", report["blockers"])
            self.assertFalse(report["production_selector_changed"])
            self.assertFalse(report["ranking_score_changed"])
            self.assertFalse(report["pressure_fade_changed"])

    def test_aligned_complete_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = self._fixture(root)
            rc, report = self._run(paths)
            self.assertEqual(rc, 0)
            self.assertEqual(report["status"], "PASS")
            self.assertTrue(report["candidate_release_allowed"])


if __name__ == "__main__":
    unittest.main()
