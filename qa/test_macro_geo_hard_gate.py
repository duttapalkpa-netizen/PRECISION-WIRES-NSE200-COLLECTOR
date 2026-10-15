import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pipeline.macro_geo_hard_gate as gate


class MacroGeoHardGateTests(unittest.TestCase):
    def _inputs(self, root, p0_status="P0_COMPLETE"):
        coverage = root / "coverage.json"
        event = root / "event.json"
        panel = root / "market_panel.csv"
        equity = root / "equity.csv"
        groups = {
            name: {"status": "AVAILABLE", "rows": 2}
            for name in ["benchmark_index", "sector_indices", "volatility", "crude_oil",
                         "usd_inr", "fpi_dii_flows", "corporate_events", "geopolitical_events"]
        }
        if p0_status != "P0_COMPLETE":
            groups["fpi_dii_flows"] = {"status": "NOT_CONNECTED", "rows": 0}
        coverage.write_text(json.dumps({"p0_coverage": {
            "status": p0_status, "available_count": 8 if p0_status == "P0_COMPLETE" else 7,
            "required_count": 8, "groups": groups
        }}))
        event.write_text(json.dumps({"research_status": "COMPUTED_EXPLORATORY",
                                     "eligible_event_rows": 3, "window_rows": 9}))
        panel.write_text("DATE,SERIES,CLOSE\n2026-10-14,NIFTY 50,25000\n2026-10-14,INDIA VIX,15\n")
        equity.write_text("DATE,SYMBOL,CLOSE_PRICE\n2026-10-14,ABC,100\n")
        return coverage, event, panel, equity

    def test_blocks_when_p0_coverage_is_incomplete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            coverage, event, panel, equity = self._inputs(root, "P0_INCOMPLETE")
            out = root / "gate.json"
            with patch.object(gate, "COVERAGE", coverage), patch.object(gate, "EVENT_REPORT", event), \
                 patch.object(gate, "PANEL", panel), patch.object(gate, "EQUITY", equity), patch.object(gate, "OUT", out):
                with redirect_stdout(StringIO()):
                    self.assertEqual(gate.main(), 1)
                report = json.loads(out.read_text())
                self.assertEqual(report["status"], "BLOCKED")
                self.assertFalse(report["candidate_release_allowed"])

    def test_passes_only_when_all_gate_inputs_are_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            coverage, event, panel, equity = self._inputs(root, "P0_COMPLETE")
            out = root / "gate.json"
            with patch.object(gate, "COVERAGE", coverage), patch.object(gate, "EVENT_REPORT", event), \
                 patch.object(gate, "PANEL", panel), patch.object(gate, "EQUITY", equity), patch.object(gate, "OUT", out):
                with redirect_stdout(StringIO()):
                    self.assertEqual(gate.main(), 0)
                report = json.loads(out.read_text())
                self.assertEqual(report["status"], "PASS")
                self.assertTrue(report["candidate_release_allowed"])


if __name__ == "__main__":
    unittest.main()
