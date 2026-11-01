import unittest
from pipeline.collect_rbi_dbie_bond_yields import period_date, FIELDS
class TestRbiDbieBondYieldAdapter(unittest.TestCase):
 def test_month_end_date(self): self.assertEqual(period_date("Aug-2026"),"2026-08-31")
 def test_iso_month(self): self.assertEqual(period_date("2026-08"),"2026-08-31")
 def test_required_provenance_and_frequency(self):
  self.assertTrue({"DATE","COUNTRY","TERM_YEARS","YIELD_PCT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC","RELEASED_AT","FREQUENCY"}.issubset(set(FIELDS)))
if __name__=="__main__": unittest.main()
