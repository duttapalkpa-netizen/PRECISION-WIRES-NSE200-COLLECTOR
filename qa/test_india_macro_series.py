import unittest
from pipeline.collect_india_macro_series import SOURCES,select,sha,extract_gdp_row,GDP_PERIODS,GDP_GROWTH_PERIODS
class Tests(unittest.TestCase):
 def test_sources_are_separate(self):
  self.assertTrue({"gdp","cpi","wpi","government_capex","pmi"}.issubset(SOURCES))
  self.assertIn("not Government",SOURCES["pmi"]["provider"])
 def test_catalogue_requires_source_identity(self):
  rows=[{"table_name":"Quarterly estimates of GDP","file_path":"x/","file_name":"a.xlsx","unique_id":"A","release_date":"2026-08-31"},{"table_name":"Quarterly estimates of GDP","file_path":"x/","file_name":"b.xlsx","release_date":"2026-07-31"}]
  self.assertEqual([x["unique_id"] for x in select(rows,["quarterly estimates of gdp"])],["A"])
 def test_official_quarterly_gdp_pdf_row_parser(self):
  values=extract_gdp_row("Statement 5A\\nGDP\\n61,59,720 60,61,357 68,19,597 70,76,953 65,65,079 65,24,195 73,03,045 76,08,448 70,54,579 69,53,870 78,40,573 81,39,598 75,28,887 75,38,658 84,53,555",15)
  self.assertEqual(len(values),15)
  self.assertEqual(values[0],6159720)
  self.assertEqual(values[-1],8453555)
 def test_gdp_quarterly_series_window_is_explicit(self):
  self.assertEqual(len(GDP_PERIODS),15)
  self.assertEqual(GDP_PERIODS[0],"FY2022-23-Q1")
  self.assertEqual(GDP_PERIODS[-1],"FY2025-26-Q3")
  self.assertEqual(len(GDP_GROWTH_PERIODS),11)
  self.assertEqual(extract_gdp_row("Statement 6A\\nGDP\\n6.6 7.6 7.1 7.5 7.5 6.6 7.4 7.0 6.7 8.4 7.8",11,decimal=True)[-1],7.8)
 def test_sha(self):
  self.assertEqual(sha(b"x"),sha(b"x"));self.assertNotEqual(sha(b"x"),sha(b"y"))
if __name__=="__main__": unittest.main()
