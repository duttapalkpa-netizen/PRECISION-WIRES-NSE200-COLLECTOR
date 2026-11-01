import unittest
from pipeline.collect_cga_capex_fy2026_27_smoke import EXPECTED
class CapexTests(unittest.TestCase):
 def test_ytd_ratio_reconciles(self):
  self.assertEqual(round(EXPECTED["actual_ytd_crore"]/EXPECTED["budget_estimate_crore"]*100,1),EXPECTED["be_utilization_percent"])
 def test_scope_is_cumulative_not_monthly(self):
  self.assertEqual(EXPECTED["actual_ytd_crore"],654547)
  self.assertEqual(EXPECTED["budget_estimate_crore"],1221821)
if __name__=="__main__":unittest.main()
