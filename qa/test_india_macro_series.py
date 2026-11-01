import unittest
from pipeline.collect_india_macro_series import SOURCES,select,sha
class Tests(unittest.TestCase):
 def test_sources_are_separate(self):
  self.assertTrue({"gdp","cpi","wpi","government_capex","pmi"}.issubset(SOURCES))
  self.assertIn("not Government",SOURCES["pmi"]["provider"])
 def test_catalogue_requires_source_identity(self):
  rows=[{"table_name":"Quarterly estimates of GDP","file_path":"x/","file_name":"a.xlsx","unique_id":"A","release_date":"2026-08-31"},{"table_name":"Quarterly estimates of GDP","file_path":"x/","file_name":"b.xlsx","release_date":"2026-07-31"}]
  self.assertEqual([x["unique_id"] for x in select(rows,["quarterly estimates of gdp"])],["A"])
 def test_sha(self):
  self.assertEqual(sha(b"x"),sha(b"x"));self.assertNotEqual(sha(b"x"),sha(b"y"))
if __name__=="__main__": unittest.main()
