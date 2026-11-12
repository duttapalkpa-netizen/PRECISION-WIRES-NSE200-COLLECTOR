import unittest
from pathlib import Path
from pipeline.macro_geo_same_snapshot_reconcile import digest, FILES


class SameSnapshotTests(unittest.TestCase):
    def test_required_outputs_include_all_layers(self):
        self.assertIn("outputs/macro_geo/source_coverage.json", FILES.values())
        self.assertIn("outputs/macro_geo/factor_coverage_audit.json", FILES.values())
        self.assertIn("outputs/macro_geo/event_study_report.json", FILES.values())
        self.assertIn("outputs/macro_geo/hard_gate_report.json", FILES.values())

    def test_digest_is_deterministic(self):
        path = Path("qa/test_macro_geo_same_snapshot_reconcile.py")
        self.assertEqual(digest(path), digest(path))

    def test_source_coverage_status_check_requires_exact_unique_key_sets(self):
        source = Path("pipeline/macro_geo_same_snapshot_reconcile.py").read_text()
        self.assertIn("len(csv_names)==len(set(csv_names))", source)
        self.assertIn("len(json_names)==len(set(json_names))", source)
        self.assertIn("set(csv_status)==set(json_status)", source)


if __name__ == "__main__":
    unittest.main()
