import unittest
from pathlib import Path
import pandas as pd

from pipeline.macro_geo_factor_coverage_reconcile import latest_evidence_timestamp


class SameSnapshotTests(unittest.TestCase):
    def test_latest_observed_row_timestamp_wins_over_stale_inventory_timestamp(self):
        import tempfile
        import json
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"data/external").mkdir(parents=True)
            pd.DataFrame([
                {"DATE":"2026-10-29","OBSERVED_AT_UTC":"2026-10-30T10:19:49.544190Z"},
                {"DATE":"2026-10-30","OBSERVED_AT_UTC":"2026-10-30T10:26:10.796257Z"},
            ]).to_csv(root/"data/external/us_yields.csv",index=False)
            value=latest_evidence_timestamp(
                {"as_of_utc":"2026-10-30T09:20:51Z"},
                {"observed_at_utc":"2026-10-30T10:19:49Z"},
                root=root)
            self.assertEqual(value,"2026-10-30T10:26:10.796257Z")

    def test_missing_all_timestamps_fails_closed(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(RuntimeError,"No valid UTC evidence timestamp"):
                latest_evidence_timestamp({}, {}, root=Path(tmp))

    def test_workflow_uses_exact_triggering_run_not_latest_independent_runs(self):
        workflow=Path(".github/workflows/macro_geo_factor_coverage_reconciliation.yml").read_text()
        self.assertIn("github.event.workflow_run.id",workflow)
        self.assertIn("github.event.workflow_run.head_sha",workflow)
        self.assertIn('gh run download "$TRIGGER_RUN_ID" -n macro-geo-factor-source-repair',workflow)
        self.assertNotIn("sort_by(.created_at) | last",workflow)
        self.assertNotIn("status=success&per_page",workflow)
        self.assertIn('audit.get("source_coverage_as_of") == coverage["as_of_utc"]',workflow)


if __name__ == "__main__":
    unittest.main()
