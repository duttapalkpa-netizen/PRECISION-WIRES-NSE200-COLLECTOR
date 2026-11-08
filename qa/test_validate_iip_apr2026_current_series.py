"""Regression tests for the April-2026 current-series IIP CSV validator."""
import csv, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "qa"))
from validate_iip_apr2026_current_series import validate

LEDGER = ROOT / "audit_inputs" / "iip_apr2026_current_output_ppi_nic2025_monthly_values.csv"

class CurrentSeriesTests(unittest.TestCase):
    def load(self):
        with LEDGER.open(encoding="utf-8-sig", newline="") as f:
            r = csv.DictReader(f)
            return r.fieldnames, list(r)
    def run_rows(self, fields, rows):
        tmp = tempfile.NamedTemporaryFile("w", encoding="utf-8-sig", newline="", suffix=".csv", delete=False)
        with tmp:
            w = csv.DictWriter(tmp, fieldnames=fields); w.writeheader(); w.writerows(rows)
        p = Path(tmp.name); self.addCleanup(p.unlink, missing_ok=True)
        return validate(p)
    def test_official_current_series_ledger_passes(self):
        self.assertEqual(validate(LEDGER), [])
    def test_missing_nic_code_is_rejected(self):
        fields, rows = self.load(); rows.pop()
        self.assertTrue(any("expected 23 rows" in e for e in self.run_rows(fields, rows)))
    def test_duplicate_or_out_of_order_nic_is_rejected(self):
        fields, rows = self.load(); rows[0]["nic_code"] = "11"
        self.assertTrue(any("NIC codes must be exactly" in e for e in self.run_rows(fields, rows)))
    def test_cross_base_year_relabel_is_rejected(self):
        fields, rows = self.load(); rows[0]["base_year"] = "2011-12"
        self.assertTrue(any("base_year must equal" in e for e in self.run_rows(fields, rows)))
    def test_wrong_official_release_is_rejected(self):
        fields, rows = self.load(); rows[0]["official_crosscheck_release_id"] = "IIPMFY26006MAY"
        self.assertTrue(any("official_crosscheck_release_id must equal" in e for e in self.run_rows(fields, rows)))
    def test_invalid_source_hash_is_rejected(self):
        fields, rows = self.load(); rows[0]["source_workbook_sha256"] = "pending"
        self.assertTrue(any("source_workbook_sha256 must be 64" in e for e in self.run_rows(fields, rows)))
    def test_non_numeric_index_is_rejected(self):
        fields, rows = self.load(); rows[0]["monthly_index"] = "UNKNOWN"
        self.assertTrue(any("monthly_index must be numeric" in e for e in self.run_rows(fields, rows)))

if __name__ == "__main__":
    unittest.main()
