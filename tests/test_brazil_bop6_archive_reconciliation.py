import tempfile
import unittest
import zipfile
from pathlib import Path

import openpyxl

from qa.audit_brazil_bop6_archive_reconciliation import read_archive, compare


class BCBArchiveReconciliationTests(unittest.TestCase):
    def make_archive(self, path, duplicate=False):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Balance"
        ws.cell(6, 1, "Itemization")
        ws.cell(6, 2, 2010)
        ws.cell(6, 5, "SGS Code")
        for col, month in enumerate(["Jan", "Feb", "Mar"], 2):
            ws.cell(7, col, month)
        rows = [
            (9, "Portfolio investment", 22905, [10.0, 20.0, 30.0]),
            (10, "Net acquisition of financial assets", 22906, [15.0, 25.0, 35.0]),
            (11, "Net incurrence of liabilities", 22924, [5.0, 5.0, 5.0]),
        ]
        for row, label, code, vals in rows:
            ws.cell(row, 1, label)
            for col, val in enumerate(vals, 2):
                ws.cell(row, col, val)
            ws.cell(row, 5, code)
        if duplicate:
            ws.cell(12, 1, "Portfolio investment")
            ws.cell(12, 2, 1)
            ws.cell(12, 5, 22905)
        buf = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        buf.close()
        wb.save(buf.name)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(buf.name, "BalPayM.xlsx")
        Path(buf.name).unlink()

    def test_extracts_three_series_and_periods(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "archive.zip"
            self.make_archive(p)
            data, meta = read_archive(p)
        self.assertEqual(data["22905"], {"2010-01": 10.0, "2010-02": 20.0, "2010-03": 30.0})
        self.assertEqual(meta["period_count_by_series"]["22906"], 3)

    def test_duplicate_series_row_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "archive.zip"
            self.make_archive(p, duplicate=True)
            with self.assertRaises(ValueError):
                read_archive(p)

    def test_rounding_tolerance(self):
        r = compare({"2010-01": 1.0}, {"2010-01": 1.04})
        self.assertEqual(r["mismatch_count"], 0)

    def test_material_difference_detected(self):
        r = compare({"2010-01": -4441.7}, {"2010-01": 88.383})
        self.assertEqual(r["mismatch_count"], 1)
        self.assertEqual(r["mismatch_2010_onward_count"], 1)


if __name__ == "__main__":
    unittest.main()
