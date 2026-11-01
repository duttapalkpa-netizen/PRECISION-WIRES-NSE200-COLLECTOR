import tempfile,unittest
from pathlib import Path
from openpyxl import Workbook
from pipeline.collect_mospi_cpi_2024_smoke import inspect

def fixture(path,index=109.49,inflation=5.54,status="P",decoy=False):
 w=Workbook(); g=w.active; g.title="General"
 g.append(["Base Year","State Code","State Name","Sector","Year","Month","Index","Inflation","Status"])
 if decoy: g.append(["2024","19","West Bengal","Combined",2026,"September",109.49,5.54,"P"])
 g.append(["2024","00","All India","Combined",2026,"September",index,inflation,status])
 other=w.create_sheet("Item"); other.append(["Base Year","State","Index","Inflation"])
 other.append(["2024","Some item",109.49,5.54])
 w.save(path)

class CPISmokeTests(unittest.TestCase):
 def test_exact_all_india_combined_september_row_passes(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"cpi.xlsx"; fixture(p)
   q=inspect(p); self.assertEqual(q["headline_observation"]["index"],109.49)
   self.assertTrue(all(q["domain_checks"].values()))
 def test_other_rows_cannot_satisfy_headline(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"decoy.xlsx"; fixture(p,index=108.73,inflation=4.04,decoy=True)
   with self.assertRaises(RuntimeError): inspect(p)
 def test_non_provisional_or_wrong_period_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"wrong.xlsx"; fixture(p,status="F")
   with self.assertRaises(RuntimeError): inspect(p)
if __name__=="__main__": unittest.main()
