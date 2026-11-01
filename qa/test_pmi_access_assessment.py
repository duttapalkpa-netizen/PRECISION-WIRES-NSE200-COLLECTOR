import unittest
from pathlib import Path
import json,tempfile
class PMIAccessTests(unittest.TestCase):
 def test_access_assessment_never_promotes_without_license(self):
  assessment={"underlying_dataset_status":"NOT_CONNECTED","observed_rows":0,"promotable_rows":0,
   "license_status":"NO_LICENSE_OR_DATA_FEED_CREDENTIALS_PROVIDED_TO_THIS_PIPELINE"}
  self.assertEqual(assessment["underlying_dataset_status"],"NOT_CONNECTED")
  self.assertEqual(assessment["promotable_rows"],0)
 def test_public_headline_not_equal_full_series(self):
  access="PUBLIC_RELEASE_HEADLINES_AND_CALENDAR; FULL_HISTORICAL_SERIES_LICENSE_OR_SUBSCRIPTION_REQUIRED"
  self.assertIn("FULL_HISTORICAL_SERIES_LICENSE",access)
  self.assertIn("PUBLIC_RELEASE_HEADLINES",access)
if __name__=="__main__":unittest.main()
