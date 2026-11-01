import tempfile, unittest
from pathlib import Path
from openpyxl import Workbook
from pipeline.collect_mospi_cpi_2024_smoke import inspect_workbook

class CPISmokeTests(unittest.TestCase):
    def test_requires_both_official_headline_values(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"cpi.xlsx"; w=Workbook(); s=w.active
            s.append(["September 2026 CPI 2024=100","Combined General"])
            s.append(["Index",109.49,"Inflation",5.54]); w.save(p)
            result=inspect_workbook(p)
            self.assertTrue(all(result["domain_checks"].values()))
    def test_wrong_series_values_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"wrong.xlsx"; w=Workbook(); s=w.active
            s.append(["CPI 2012=100",198.0,1.33]); w.save(p)
            with self.assertRaises(RuntimeError): inspect_workbook(p)

if __name__=="__main__": unittest.main()
