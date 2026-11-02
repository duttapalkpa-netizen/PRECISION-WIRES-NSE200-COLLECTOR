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

    def test_policy_event_row_validation_cannot_override_incomplete_collector_domain_qa(self):
        from pipeline.macro_geo_factor_coverage_reconcile import policy_events_promotable
        row_qa={"status":"VALIDATED","rows_eligible_for_event_study":4}
        self.assertFalse(policy_events_promotable(row_qa,"COLLECTED_NEEDS_DOMAIN_QA"))
        self.assertFalse(policy_events_promotable(row_qa,"AVAILABLE_WITH_SOURCE_FAILURES"))
        self.assertFalse(policy_events_promotable(row_qa,"BLOCKED"))
        self.assertTrue(policy_events_promotable(row_qa,"COLLECTED_AND_DOMAIN_QA_PASSED"))

    def test_workflow_uses_exact_triggering_run_not_latest_independent_runs(self):
        workflow=Path(".github/workflows/macro_geo_factor_coverage_reconciliation.yml").read_text()
        self.assertIn("github.event.workflow_run.id",workflow)
        self.assertIn("github.event.workflow_run.head_sha",workflow)
        self.assertIn('RUN_ID="$EVENT_RUN_ID"',workflow)
        self.assertIn('gh run download "$RUN_ID" -n macro-geo-factor-source-repair',workflow)
        self.assertIn("inputs.factor_source_run_id",workflow)
        self.assertIn('d.get("conclusion")=="success"',workflow)
        self.assertNotIn("sort_by(.created_at) | last",workflow)
        self.assertNotIn("status=success&per_page",workflow)
        self.assertIn('audit.get("source_coverage_as_of") == coverage["as_of_utc"]',workflow)


if __name__ == "__main__":
    unittest.main()


class ProductionInvariantRegressionTests(unittest.TestCase):
    def test_frozen_production_files_match_pr13_base_git_blobs(self):
        import hashlib
        frozen = {
            "pipeline/final_selection.py": "8bf216c866030d92f8066e9183c9636880577910",
            "pipeline/diagnostics_672.py": "af0a8ddc17d72024509167533585713600a4b845",
            "pipeline/walk_forward_backtest.py": "df6e55a72f0e62e59d8de58eff7c58d17e2ec34b",
            "config/macro_factor_registry.csv": "7d6f87ddd263a4ec5f883633724b7fa5974d5a88",
        }
        for name, expected in frozen.items():
            raw = Path(name).read_bytes()
            git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
            self.assertEqual(git_blob, expected, name)

    def test_diagnostic_matrix_remains_exactly_672_and_unknown_is_explicit(self):
        import ast
        tree = ast.parse(Path("pipeline/diagnostics_672.py").read_text())
        values = {}
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in {"STEP_NAMES", "FILTERS", "STATES"}:
                        values[target.id] = ast.literal_eval(node.value)
        self.assertEqual(len(values["STEP_NAMES"]), 56)
        self.assertEqual(len(values["FILTERS"]), 12)
        self.assertEqual(len(values["STEP_NAMES"]) * len(values["FILTERS"]), 672)
        self.assertIn("UNKNOWN", values["STATES"])

    def test_ranking_and_pressure_fade_logic_are_present_in_frozen_scoring_file(self):
        source = Path("pipeline/walk_forward_backtest.py").read_text()
        self.assertIn('"RANKING_SCORE"', source)
        self.assertIn('"PRESSURE_FADE"', source)
        self.assertIn('np.where(x["TRANSITION_SIGNATURE"].eq("PRESSURE_FADE"),1,0)', source)
