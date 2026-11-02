import unittest
from pipeline.collect_cga_capex_fy2026_27_smoke import EXPECTED,capex_row_matches,capex_row_values
class CapexTests(unittest.TestCase):
 def test_ytd_ratio_reconciles(self):
  self.assertEqual(round(EXPECTED["actual_ytd_crore"]/EXPECTED["budget_estimate_crore"]*100,1),EXPECTED["be_utilization_percent"])
 def test_scope_is_cumulative_not_monthly(self):
  self.assertEqual(EXPECTED["actual_ytd_crore"],654547)
  self.assertEqual(EXPECTED["budget_estimate_crore"],1221821)
 def test_cga_table_row_values(self):
  s="10 | Capital Expenditure | (Details) | 1221821 | 654547 | 53.6% | (51.8%)"
  self.assertEqual(capex_row_values(s),["1221821","654547","53.6","51.8"])
  self.assertTrue(capex_row_matches(s))
 def test_wrong_actual_rejected(self):
  self.assertFalse(capex_row_matches("10 | Capital Expenditure | (Details) | 1221821 | 654548 | 53.6% | (51.8%)"))
if __name__=="__main__":unittest.main()

# Evidence-only trigger: preserve test assertions; no production logic or QA expectations changed.
