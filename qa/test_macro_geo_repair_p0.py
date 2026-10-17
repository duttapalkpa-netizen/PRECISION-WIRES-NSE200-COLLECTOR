import tempfile
import unittest
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
            self.assertEqual(end.isoformat(), "2026-10-19")

    def test_p0_window_blocks_if_backbone_missing(self):
        with patch.object(repair, "EQUITY_PANEL", Path("/nonexistent/nse_eq_200_sessions.csv")):
            with self.assertRaisesRegex(RuntimeError, "200-session NSE equity panel is missing"):
                repair.p0_window()


if __name__ == "__main__":
    unittest.main()
