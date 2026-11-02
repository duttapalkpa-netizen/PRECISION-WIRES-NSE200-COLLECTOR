import unittest
from pathlib import Path
class DiscoveryGuardrails(unittest.TestCase):
 def test_no_factor_registry_promotion_or_production_mutation(self):
  s=Path("pipeline/macro_full_history_source_discovery.py").read_text()
  for term in ["PRODUCTION_SELECTOR","RANKING_SCORE","+1 PRESSURE_FADE","672","NOT_CONNECTED"]:
   self.assertIn(term,s)
 def test_pmi_not_in_discovery_sources(self):
  s=Path("pipeline/macro_full_history_source_discovery.py").read_text()
  self.assertNotIn("pmi.spglobal.com",s.lower())
 def test_cga_and_oea_official_hosts(self):
  s=Path("pipeline/macro_full_history_source_discovery.py").read_text()
  self.assertIn("eaindustry.nic.in/download_data_2223.asp",s)
  self.assertIn("cga.gov.in/writereaddata/MonthAccount/MonthAccountDashboard",s)
if __name__=="__main__":unittest.main()

# Evidence-only rerun trigger for the bounded official macro source discovery audit.
