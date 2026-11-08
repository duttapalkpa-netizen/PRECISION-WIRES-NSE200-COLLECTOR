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

    def test_quarantined_ledger_passes(self):
        self.assertEqual(validate(LEDGER), [])

    def test_out_of_order_vintages_are_rejected(self):
        fields, rows = self.load_rows()
        rows[0]["later_vintage_release_dates"] = "28 Jul 2026;29 Jun 2026;28 Sep 2026"
        self.assertTrue(any("release dates/order mismatch" in e for e in validate(self.write_temp(fields, rows))))

    def test_cross_base_year_revision_must_remain_unknown(self):
        fields, rows = self.load_rows()
        rows[0]["revision_detected"] = "TRUE"
        rows[0]["latest_later_index"] = "100.5"
        rows[0]["revision_delta_latest_minus_first"] = "-0.5"
        errors = validate(self.write_temp(fields, rows))
        self.assertTrue(any("revision_detected must equal 'UNKNOWN'" in e for e in errors))
        self.assertTrue(any("latest_later_index must be blank" in e for e in errors))

    def test_2011_12_observation_cannot_be_relabelled_2022_23(self):
        fields, rows = self.load_rows()
        rows[0]["later_vintage_source_base_year"] = "2022-23"
        errors = validate(self.write_temp(fields, rows))
        self.assertTrue(any("later_vintage_source_base_year must equal '2011-12'" in e for e in errors))

    def test_run245_old_base_vintage_cannot_be_claimed_as_nic2025_crosscheck(self):
        fields, rows = self.load_rows()
        rows[0]["evidence_status"] = rows[0]["evidence_status"].replace(
            "RUN245_XLSX_NOT_COMPARABLE_BASEYEAR_CLASSIFICATION_MISMATCH",
            "RUN245_XLSX_CROSSCHECKED",
        )
        errors = validate(self.write_temp(fields, rows))
        self.assertTrue(any("must retain RUN245_XLSX_NOT_COMPARABLE" in e for e in errors))


    def test_wpi_first_release_must_be_marked_superseded_by_ppi(self):
        fields, rows = self.load_rows()
        rows[0]["first_release_series_status"] = "CURRENT"
        errors = validate(self.write_temp(fields, rows))
        self.assertTrue(any("first_release_series_status must equal 'SUPERSEDED_BY_OUTPUT_PPI_SERIES'" in e for e in errors))

    def test_current_ppi_april_value_cannot_be_claimed_without_source_extraction(self):
        fields, rows = self.load_rows()
        rows[0]["current_series_apr2026_index_status"] = "VERIFIED"
        errors = validate(self.write_temp(fields, rows))
        self.assertTrue(any("current_series_apr2026_index_status must equal 'NOT_YET_EXTRACTED_FROM_COMPARABLE_CURRENT_SERIES_SOURCE'" in e for e in errors))

    def test_missing_raw_hash_must_remain_provisional(self):
        fields, rows = self.load_rows()
        rows[0]["raw_pdf_sha256"] = ""
        rows[0]["evidence_status"] = rows[0]["evidence_status"].replace("RAW_PDF_SHA256_PENDING", "")
        self.assertTrue(any("must retain RAW_PDF_SHA256_PENDING" in e for e in validate(self.write_temp(fields, rows))))


if __name__ == "__main__":
    unittest.main()
