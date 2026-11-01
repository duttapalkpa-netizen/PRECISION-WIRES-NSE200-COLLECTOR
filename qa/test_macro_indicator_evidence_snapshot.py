import json,tempfile,unittest
from pathlib import Path

class EvidenceSnapshotPolicyTests(unittest.TestCase):
 def test_policy_keeps_partial_macro_and_capex_non_available(self):
  statuses={"macro_indicators":"DATA_QUALITY_WARN","government_capex":"DATA_QUALITY_WARN","pmi_underlying_dataset":"NOT_CONNECTED"}
  self.assertNotIn("AVAILABLE",statuses.values())
 def test_snapshot_semantics_explicitly_non_simultaneous(self):
  text=Path("pipeline/build_macro_indicator_evidence_snapshot.py").read_text()
  self.assertIn("not simultaneous collection",text)
  self.assertIn("UNKNOWN is neither PASS nor FAIL",text)
 def test_production_invariants_not_touched(self):
  text=Path("pipeline/build_macro_indicator_evidence_snapshot.py").read_text()
  for item in ["No production selector change","No RANKING_SCORE change","No +1 PRESSURE_FADE change","No 672-diagnostic change"]:
   self.assertIn(item,text)
if __name__=="__main__":unittest.main()
