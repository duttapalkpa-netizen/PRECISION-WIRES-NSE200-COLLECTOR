import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pipeline.stock_news_24h_join as stage


class StockNews24hReadinessTests(unittest.TestCase):
    def test_missing_stock_news_sources_are_blocked_not_no_news(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "out"
            with patch.object(stage, "CUTS", root / "missing_cutoffs.csv"), \
                 patch.object(stage, "NEWS", root / "missing_news.csv"), \
                 patch.object(stage, "COVERAGE", root / "missing_coverage.csv"), \
                 patch.object(stage, "OUT", output):
                stream = StringIO()
                with redirect_stdout(stream):
                    self.assertEqual(stage.main(), 0)
                report = json.loads((output / "stock_news_24h_readiness.json").read_text())
                self.assertEqual(report["status"], "BLOCKED_MISSING_INPUTS")
                self.assertEqual(report["research_status"], "BLOCKED")
                self.assertIn("UNKNOWN", report["no_news_semantics"])
                self.assertFalse(report["production_selector_changed"])
                self.assertFalse(report["ranking_score_changed"])
                self.assertFalse(report["pressure_fade_changed"])


if __name__ == "__main__":
    unittest.main()
