import unittest
from pathlib import Path
from pipeline.macro_geo_same_snapshot_reconcile import digest,REQUIRED
class SameSnapshotTests(unittest.TestCase):
 def test_required_outputs_include_all_layers(self):
  self.assertIn("outputs/macro_geo/source_coverage.json",REQUIRED)
  self.assertIn("outputs/macro_geo/factor_coverage_audit.json",REQUIRED)
  self.assertIn("outputs/macro_geo/event_study_report.json",REQUIRED)
  self.assertIn("outputs/macro_geo/hard_gate_report.json",REQUIRED)
 def test_digest_is_deterministic(self):
  p=Path("qa/test_macro_geo_same_snapshot_reconcile.py")
  self.assertEqual(digest(p),digest(p))
if __name__=="__main__": unittest.main()
