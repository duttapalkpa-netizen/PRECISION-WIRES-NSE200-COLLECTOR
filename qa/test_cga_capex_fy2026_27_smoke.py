import unittest
from pipeline.collect_cga_capex_fy2026_27_smoke import EXPECTED,capex_row_matches
class CapexTests(unittest.TestCase):
 def test_ytd_ratio_reconciles(self):
  self.assertEqual(round(EXPECTED["actual_ytd_crore"]/EXPECTED["budget_estimate_crore"]*100,1),EXPECTED["be_utilization_percent"])
 def test_scope_is_cumulative_not_monthly(self):
  self.assertEqual(EXPECTED["actual_ytd_crore"],654547)
  self.assertEqual(EXPECTED["budget_estimate_crore"],1221821)
 def test_cga_table_cell_separators_tolerated(self):
  self.assertTrue(capex_row_matches("10 | Capital Expenditure | (Details) | 1221821 | 654547 | 53.6% | (51.8%)"))
 def test_wrong_actual_rejected(self):
  self.assertFalse(capex_row_matches("10 | Capital Expenditure | (Details) | 1221821 | 654548 | 53.6% | (51.8%)"))
if __name__=="__main__":unittest.main()
