import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class MacroGeoOfficialSourcePolicyTests(unittest.TestCase):
    def test_p0_required_series_reject_secondary_status(self):
        source = (ROOT / "pipeline/macro_geo_collect_p0.py").read_text(encoding="utf-8")
        self.assertIn('x.get("status")=="AVAILABLE"', source)
        self.assertNotIn('x.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY")', source)

    def test_secondary_index_rows_cannot_become_official(self):
        source = (ROOT / "pipeline/macro_geo_collect_p0.py").read_text(encoding="utf-8")
        self.assertIn('"AVAILABLE_SECONDARY" if found else "BLOCKED"', source)
        self.assertIn('"official_rows":len(official_found)', source)

    def test_community_usd_inr_mirror_is_removed(self):
        source = (ROOT / "pipeline/macro_geo_repair_p0.py").read_text(encoding="utf-8")
        self.assertNotIn("raw.githubusercontent.com/the-solipsist", source)
        self.assertIn("community mirror fallback disabled", source)

    def test_eia_brent_fallback_is_explicitly_official(self):
        source = (ROOT / "pipeline/macro_geo_repair_p0.py").read_text(encoding="utf-8")
        self.assertIn('startswith("US EIA")', source)
        self.assertIn('"status":status', source)

    def test_repair_acceptance_rejects_secondary(self):
        source = (ROOT / "pipeline/macro_geo_repair_p0.py").read_text(encoding="utf-8")
        self.assertIn('v.get("status")=="AVAILABLE"', source)
        self.assertNotIn('v.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY")', source)

if __name__ == "__main__":
    unittest.main()
