import unittest
from pathlib import Path
class CGAHistoricalGuardrails(unittest.TestCase):
 def test_monthly_derivation_and_vintage_limits_are_explicit(self):
  s=Path("pipeline/collect_cga_monthly_historical_series.py").read_text()
  self.assertIn("monthly_derived",s)
  self.assertIn("VINTAGE_UNVERIFIED_SINGLE_LATEST_SNAPSHOT",s)
  self.assertIn("source_page_last_updated_date",s)
 def test_official_cga_sources_only(self):
  s=Path("pipeline/collect_cga_monthly_historical_series.py").read_text()
  self.assertIn("https://cga.gov.in/MonthDashboardReport/Published/list.aspx",s)
  self.assertIn("https://cga.gov.in/writereaddata/MonthAccount/MonthAccountDashboard/",s)
 def test_no_pmi_or_production_mutation(self):
  s=Path("pipeline/collect_cga_monthly_historical_series.py").read_text()
  self.assertNotIn("pmi.spglobal.com",s)
  self.assertNotIn("RANKING_SCORE =",s)
if __name__=="__main__":unittest.main()
