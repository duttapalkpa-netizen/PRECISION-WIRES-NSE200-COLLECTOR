import unittest
from pipeline.collect_oea_wpi_2022_23_smoke import domain_qa

FIXTURE="""Posted On: 14 OCT 2026 12:00PM by PIB Delhi
Provisional Estimates of Wholesale Price Index (Base Year 2022-23) for the month of September 2026
All India Wholesale Price Index (WPI) inflation for September 2026 is 11.39 per cent.
All Commodities index 112.5.
Primary Articles index 120.3 inflation 8.67 per cent.
Fuel and Power index 110.5 inflation 25.85 per cent.
Manufactured Products index 110.2 inflation 9.76 per cent.
The provisional index of WPI for September 2026 has been compiled with a weighted response rate of 83.4 per cent.
The final index for July 2026 remains 110.0; inflation 9.78 per cent.
Item-wise data https://eaindustry.nic.in/download_data_2223.asp
"""
class WPITests(unittest.TestCase):
 def test_official_release_headlines_and_domain_pass(self):
  self.assertTrue(all(domain_qa(FIXTURE).values()))
 def test_wrong_base_year_rejected(self):
  with self.assertRaises(RuntimeError):domain_qa(FIXTURE.replace("2022-23","2011-12"))
 def test_wrong_response_rate_rejected(self):
  with self.assertRaises(RuntimeError):domain_qa(FIXTURE.replace("83.4 per cent","84.4 per cent"))
if __name__=="__main__":unittest.main()
