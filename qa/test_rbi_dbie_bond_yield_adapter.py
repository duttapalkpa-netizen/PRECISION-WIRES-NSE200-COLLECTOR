import unittest
from pipeline.collect_rbi_dbie_bond_yields import month_end
class TestRbiDbieBondYieldAdapter(unittest.TestCase):
    def test_month_end(self): self.assertEqual(month_end("Aug-2026"),"2026-08-31")
    def test_year_rollover(self): self.assertEqual(month_end("Jan-2000"),"2000-01-31")
if __name__=="__main__": unittest.main()
