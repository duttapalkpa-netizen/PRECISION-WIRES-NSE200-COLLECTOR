import unittest
from pathlib import Path
class SnapshotTests(unittest.TestCase):
 def test_partial_macro_sources_fail_closed(self):
  s=Path("pipeline/macro_indicators_snapshot_reconcile.py").read_text()
  for name in ["macro_indicators","inflation_components","government_capex"]:
   self.assertIn('setrow("'+name+'","DATA_QUALITY_WARN"',s)
  self.assertIn('setrow("pmi","NOT_CONNECTED"',s)
 def test_factor_audit_same_snapshot_contract(self):
  w=Path(".github/workflows/macro_indicators_factor_snapshot_reconciliation.yml").read_text()
  self.assertIn('a["source_coverage_as_of"]==c["as_of_utc"]',w)
  self.assertIn('a["factor_groups"]==35',w)
  self.assertIn('"hard_gate":"BLOCKED"',w)
 def test_production_invariants_explicitly_untouched(self):
  w=Path(".github/workflows/macro_indicators_factor_snapshot_reconciliation.yml").read_text()
  for term in ["RANKING_SCORE","PRODUCTION_SELECTOR","PRESSURE_FADE","672"]:
   self.assertIn(term,w)
if __name__=="__main__":unittest.main()
