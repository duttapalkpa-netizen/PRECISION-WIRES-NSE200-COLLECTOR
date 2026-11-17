#!/usr/bin/env python3
"""Acceptance tests for an archived Federal Reserve H.10 XML ZIP.

Run:
  H10_XML_ZIP=/path/to/fed_h10_xml.zip python -m unittest qa.test_h10_xml_acceptance -v

The archive is supplied explicitly; tests never download, normalize, impute, or rewrite
source observations. Expected counts are vintage-specific and must be updated only
with a documented source-vintage change.
"""
from __future__ import annotations

import collections
import math
import os
import unittest
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ARCHIVE = os.environ.get("H10_XML_ZIP")
TARGET_SERIES = "JRXWTFB_N.B"
EXPECTED_OBSERVATIONS = 5445
EXPECTED_ACTIVE = 5231
EXPECTED_ND = 214
EXPECTED_FIRST_DATE = "2006-01-02"
EXPECTED_LAST_DATE = "2026-11-13"
ND_SENTINEL = "-9999"


@unittest.skipUnless(ARCHIVE, "set H10_XML_ZIP to an archived official H.10 XML ZIP")
class H10XMLAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = Path(ARCHIVE)
        if not cls.archive.is_file():
            raise FileNotFoundError(cls.archive)
        with zipfile.ZipFile(cls.archive) as zf:
            bad_member = zf.testzip()
            if bad_member is not None:
                raise AssertionError(f"corrupt ZIP member: {bad_member}")
            if "H10_data.xml" not in zf.namelist():
                raise AssertionError("H10_data.xml missing from source ZIP")
            root = ET.fromstring(zf.read("H10_data.xml"))

        matches = []
        for element in root.iter():
            if element.tag.endswith("Series") and element.attrib.get("SERIES_NAME") == TARGET_SERIES:
                observations = [child for child in element if child.tag.endswith("Obs")]
                matches.append((element.attrib, observations))
        if len(matches) != 1:
            raise AssertionError(f"expected one {TARGET_SERIES} series, found {len(matches)}")
        cls.attributes, cls.observations = matches[0]
        cls.dates = [o.attrib.get("TIME_PERIOD", "") for o in cls.observations]
        cls.statuses = collections.Counter(o.attrib.get("OBS_STATUS", "") for o in cls.observations)

    def test_target_series_identity_and_metadata_are_present(self):
        self.assertEqual(self.attributes.get("SERIES_NAME"), TARGET_SERIES)
        self.assertTrue(self.attributes.get("UNIT"))
        self.assertTrue(self.attributes.get("UNIT_MULT"))

    def test_observation_count_and_status_distribution(self):
        self.assertEqual(len(self.observations), EXPECTED_OBSERVATIONS)
        self.assertEqual(self.statuses.get("A", 0), EXPECTED_ACTIVE)
        self.assertEqual(self.statuses.get("ND", 0), EXPECTED_ND)
        self.assertEqual(sum(self.statuses.values()), EXPECTED_OBSERVATIONS)

    def test_dates_are_chronological_unique_and_cover_expected_vintage(self):
        self.assertEqual(self.dates, sorted(self.dates))
        self.assertEqual(len(self.dates), len(set(self.dates)))
        self.assertEqual(self.dates[0], EXPECTED_FIRST_DATE)
        self.assertEqual(self.dates[-1], EXPECTED_LAST_DATE)

    def test_active_observations_are_finite_numeric_values(self):
        active = [o for o in self.observations if o.attrib.get("OBS_STATUS") == "A"]
        self.assertEqual(len(active), EXPECTED_ACTIVE)
        for observation in active:
            value = float(observation.attrib["OBS_VALUE"])
            self.assertTrue(math.isfinite(value), observation.attrib)

    def test_not_defined_observations_remain_missing_sentinels(self):
        nd = [o for o in self.observations if o.attrib.get("OBS_STATUS") == "ND"]
        self.assertEqual(len(nd), EXPECTED_ND)
        self.assertTrue(all(o.attrib.get("OBS_VALUE") == ND_SENTINEL for o in nd))
        # ND values are status-coded missing data, never numeric zero or imputations.

    def test_january_2006_monthly_average_is_reindexed_to_100(self):
        # Board Technical Q&A: from 2019-06-24 the monthly average of Jan-2006
        # is the base. Check raw daily observations, without applying the factor again.
        january = [
            float(o["OBS_VALUE"]) for o in self.observations
            if o.get("TIME_PERIOD", "").startswith("2006-01")
            and o.get("OBS_STATUS") == "A"
        ]
        self.assertEqual(len(january), 22)
        self.assertAlmostEqual(sum(january) / len(january), 100.0, delta=0.00001)

    def test_no_unexpected_status_codes(self):
        self.assertEqual(set(self.statuses), {"A", "ND"})


if __name__ == "__main__":
    unittest.main()
