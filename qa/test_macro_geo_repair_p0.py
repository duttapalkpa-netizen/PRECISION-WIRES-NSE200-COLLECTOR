import tempfile
import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pipeline.macro_geo_repair_p0 as repair


class MacroGeoP0WindowTests(unittest.TestCase):
    def test_p0_window_tracks_nse_200_session_panel_not_2006(self):
        with tempfile.TemporaryDirectory() as tmp:
            panel = Path(tmp) / "equity.csv"
            pd.DataFrame({"DATE": ["2026-01-05", "2026-10-16"]}).to_csv(panel, index=False)
            with patch.object(repair, "EQUITY_PANEL", panel):
                start, end = repair.p0_window()
            self.assertEqual(start.isoformat(), "2025-12-06")
            self.assertEqual(end, pd.Timestamp("2026-10-16").date())

    def test_p0_window_uses_observed_benchmark_when_equity_panel_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            benchmark = Path(tmp) / "benchmark.csv"
            pd.DataFrame({"DATE": ["2026-01-05", "2026-10-16", "2026-10-16"]}).to_csv(benchmark, index=False)
            with patch.object(repair, "EQUITY_PANEL", Path(tmp) / "missing_equity.csv"):
                with patch.object(repair, "BENCHMARK_PANEL", benchmark):
                    start, end = repair.p0_window()
            self.assertEqual(start.isoformat(), "2025-12-06")
            self.assertEqual(end, pd.Timestamp("2026-10-16").date())

    def test_p0_window_blocks_if_both_backbones_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(repair, "EQUITY_PANEL", Path(tmp) / "missing_equity.csv"):
                with patch.object(repair, "BENCHMARK_PANEL", Path(tmp) / "missing_benchmark.csv"):
                    with self.assertRaisesRegex(RuntimeError, "neither NSE equity panel nor benchmark index archive"):
                        repair.p0_window()


if __name__ == "__main__":
    unittest.main()
