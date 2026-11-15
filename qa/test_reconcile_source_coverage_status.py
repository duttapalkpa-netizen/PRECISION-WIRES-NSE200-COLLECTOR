import json
import tempfile
import unittest
from pathlib import Path
import pandas as pd

from pipeline.reconcile_source_coverage_status import reconcile


class TestSourceCoverageStatusReconciliation(unittest.TestCase):
    def fixture(self, root: Path):
        out = root / "outputs" / "macro_geo"
        out.mkdir(parents=True)
        cov = {
            "as_of_utc": "2026-11-01T07:22:57.779919+00:00",
            "p0_workflow_run_id": "41283471559",
            "sources": [
                {"source": "macro_indicators", "status": "DATA_QUALITY_WARN", "rows": 490,
                 "selected_path": "data/external/macro_indicators.csv",
                 "reason": "Partial historical coverage; do not promote."},
                {"source": "inflation_components", "status": "DATA_QUALITY_WARN", "rows": 432,
                 "selected_path": "data/external/inflation_components.csv",
                 "reason": "Partial CPI/WPI backseries; do not promote."},
                {"source": "government_capex", "status": "DATA_QUALITY_WARN", "rows": 143,
                 "selected_path": "data/external/government_capex.csv",
                 "reason": "Release timestamp not verified."},
            ],
        }
        jp = out / "source_coverage.json"
        jp.write_text(json.dumps(cov))
        cp = out / "source_coverage.csv"
        pd.DataFrame([
            {"source": "macro_indicators", "status": "AVAILABLE", "rows": "490",
             "selected_path": "old", "notes": "old note"},
            {"source": "inflation_components", "status": "AVAILABLE", "rows": "432",
             "selected_path": "old", "notes": "old note"},
            {"source": "government_capex", "status": "DATA_QUALITY_WARN", "rows": "143",
             "selected_path": "old", "notes": "old note"},
        ]).to_csv(cp, index=False)
        return jp, cp

    def test_canonical_json_statuses_are_mirrored_without_promotion(self):
        with tempfile.TemporaryDirectory() as d:
            jp, cp = self.fixture(Path(d))
            result = reconcile(jp, cp, Path(d) / "report")
            frame = pd.read_csv(cp, dtype=str)
            self.assertEqual(result["status"], "PASS_EXACT_SOURCE_KEY_AND_STATUS_PARITY")
            self.assertEqual(result["rows_changed"], [
                {"source": "macro_indicators", "csv_status_before": "AVAILABLE", "canonical_json_status": "DATA_QUALITY_WARN"},
                {"source": "inflation_components", "csv_status_before": "AVAILABLE", "canonical_json_status": "DATA_QUALITY_WARN"},
            ])
            self.assertTrue((frame["status"] == "DATA_QUALITY_WARN").all())
            self.assertEqual(result["status_mismatches_after_reconciliation"], 0)

    def test_rejects_missing_csv_source_key(self):
        with tempfile.TemporaryDirectory() as d:
            jp, cp = self.fixture(Path(d))
            frame = pd.read_csv(cp, dtype=str).iloc[:2]
            frame.to_csv(cp, index=False)
            with self.assertRaisesRegex(ValueError, "source key sets differ"):
                reconcile(jp, cp, Path(d) / "report")

    def test_rejects_duplicate_json_source_key(self):
        with tempfile.TemporaryDirectory() as d:
            jp, cp = self.fixture(Path(d))
            cov = json.loads(jp.read_text())
            cov["sources"].append(dict(cov["sources"][0]))
            jp.write_text(json.dumps(cov))
            with self.assertRaisesRegex(ValueError, "duplicate canonical source key"):
                reconcile(jp, cp, Path(d) / "report")


if __name__ == "__main__":
    unittest.main()
