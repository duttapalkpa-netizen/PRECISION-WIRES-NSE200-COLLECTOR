import unittest
class PMIAccessTests(unittest.TestCase):
 def test_no_license_means_not_connected(self):
  state={"underlying_dataset_status":"NOT_CONNECTED","observed_rows":0,"promotable_rows":0}
  self.assertEqual(state["underlying_dataset_status"],"NOT_CONNECTED")
  self.assertEqual(state["observed_rows"],0)
  self.assertEqual(state["promotable_rows"],0)
 def test_headline_access_not_equal_history(self):
  label="PUBLIC_RELEASE_HEADLINES_AND_CALENDAR; FULL_HISTORICAL_SERIES_LICENSE_OR_SUBSCRIPTION_REQUIRED"
  self.assertIn("PUBLIC_RELEASE_HEADLINES",label)
  self.assertIn("FULL_HISTORICAL_SERIES_LICENSE",label)
if __name__=="__main__":unittest.main()
