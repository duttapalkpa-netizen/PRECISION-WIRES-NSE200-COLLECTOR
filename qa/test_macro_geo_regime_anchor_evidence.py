import csv,unittest
from pathlib import Path
class RegimeAnchorEvidenceTests(unittest.TestCase):
 def test_two_missing_anchors_have_primary_sources(self):
  p=Path("config/macro_geo_historical_regime_anchor_evidence.csv")
  rows=list(csv.DictReader(p.open()))
  self.assertEqual({r["regime_id"] for r in rows},{"R01","R02"})
  for row in rows:
   self.assertTrue(row["source_url"].startswith("https://"))
   self.assertEqual(row["anchor_date"],row["source_publication_date"])
   self.assertEqual(row["market_panel_status"],"PRICE_PANEL_NOT_AVAILABLE_IN_CURRENT_2015_ONWARD_PANEL")
if __name__=="__main__": unittest.main()
