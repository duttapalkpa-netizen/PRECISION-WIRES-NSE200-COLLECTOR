import unittest
from pipeline.validate_india_market_source_registry import validate

def row(**overrides):
    x={"source_id":"X","source_name":"Example","owner":"Owner","official_url":"https://example.gov.in/","data_domains":"macro","factor_groups":"macro_indicators","access_mode":"public download","auth_requirement":"endpoint-specific","priority":"P0","validation_status":"DISCOVERED_NOT_LIVE_VALIDATED","validation_note":"pending"}
    x.update(overrides)
    return x

class TestIndiaMarketSourceRegistry(unittest.TestCase):
    def test_valid_inventory_is_discovery_only(self):
        r=validate([row()])
        self.assertEqual(r["status"],"REGISTRY_SCHEMA_PASS")
        self.assertEqual(r["live_validated_count"],0)
        self.assertEqual(r["promoted_count"],0)
    def test_duplicate_ids_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate"):
            validate([row(),row()])
    def test_http_rejected(self):
        with self.assertRaisesRegex(ValueError,"HTTPS"):
            validate([row(official_url="http://example.gov.in/")])
    def test_manual_promotion_rejected(self):
        with self.assertRaisesRegex(ValueError,"promotion"):
            validate([row(validation_status="DOMAIN_QA_PASS")])

if __name__ == "__main__":
    unittest.main()
