"""Regression tests for the April-2026 IIP PDF cross-check ledger validator."""
from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "qa"))
from validate_iip_apr2026_pdf_crosscheck import validate  # noqa: E402

LEDGER = ROOT / "audit_inputs" / "iip_apr2026_nic2025_pdf_first_release_crosscheck.csv"


class LedgerValidatorTests(unittest.TestCase):
    def load_rows(self):
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return reader.fieldnames, list(reader)

    def write_temp(self, fields, rows):
        tmp = tempfile.NamedTemporaryFile("w", encoding="utf-8-sig", newline="", suffix=".csv", delete=False)
        with tmp:
            writer = csv.DictWriter(tmp, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        self.addCleanup(Path(tmp.name).unlink, missing_ok=True)
        return Path(tmp.name)

    def test_committed_ledger_passes(self):
        self.assertEqual(validate(LEDGER), [])

    def test_out_of_order_vintages_are_rejected(self):
        fields, rows = self.load_rows()
        rows[0]["later_vintage_release_dates"] = "28 Jul 2026;29 Jun 2026;28 Sep 2026"
        self.assertTrue(any("dates/order mismatch" in e for e in validate(self.write_temp(fields, rows))))

    def test_revision_arithmetic_mismatch_is_rejected(self):
        fields, rows = self.load_rows()
        rows[0]["revision_delta_latest_minus_first"] = "0.0"
        self.assertTrue(any("revision delta arithmetic mismatch" in e for e for e in validate(self.write_temp(fields, rows))))

    def test_missing_raw_hash_must_remain_provisional(self):
        fields, rows = self.load_rows()
        rows[0]["raw_pdf_sha256"] = ""
        rows[0]["evidence_status"] = "VERIFIED"
        self.assertTrue(any("must remain explicitly pending" in e for e in validate(self.write_temp(fields, rows))))


if __name__ == "__main__":
    unittest.main()
