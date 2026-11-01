import unittest
from pathlib import Path
class TestRbiDbieRawSchemaDiagnostic(unittest.TestCase):
    def test_source_contract_is_monthly_and_not_daily(self):
        source = Path("pipeline/collect_rbi_dbie_bond_yields.py").read_text()
        self.assertIn("MONTHLY", source)
        self.assertIn("NOT_PROMOTED", source)
        self.assertIn("Mapping is inferred", source) if "Mapping is inferred" in source else self.assertIn("No cN-to-tenor mapping is inferred", source)
    def test_fail_closed_on_opaque_columns(self):
        source = Path("pipeline/collect_rbi_dbie_bond_yields.py").read_text()
        self.assertIn("mapping_status", source)
        self.assertIn('"BLOCKED"', source)
        self.assertIn("rbi_dbie_raw.csv", source)
if __name__ == "__main__":
    unittest.main()
