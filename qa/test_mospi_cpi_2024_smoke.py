import tempfile,unittest
from pathlib import Path
from openpyxl import Workbook
from pipeline.collect_mospi_cpi_2024_smoke import inspect

class CPISmokeTests(unittest.TestCase):
 def test_cpi_2024_headline_values_required(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"cpi.xlsx"; w=Workbook(); s=w.active
   s.append(["September 2026","CPI 2024=100"]); s.append(["Combined index",109.49]); s.append(["Combined inflation",5.54]); w.save(p)
   self.assertTrue(all(inspect(p)["domain_checks"].values()))
 def test_wrong_series_values_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"old.xlsx"; w=Workbook(); w.active.append(["CPI 2012=100",198.0,1.33]); w.save(p)
   with self.assertRaises(RuntimeError): inspect(p)
if __name__=="__main__": unittest.main()
