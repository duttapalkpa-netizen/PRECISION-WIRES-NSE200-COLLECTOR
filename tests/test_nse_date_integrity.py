import csv
import io
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

from collector.nse_download import normalize_udiff, validate_archived_daily_file, validate_full_delivery


class FullDeliveryDateIntegrityTests(unittest.TestCase):
    def make_csv(self, dates, date_column="DATE1"):
        headers = ["SYMBOL", "SERIES", "CLOSE_PRICE", "DELIV_QTY", "DELIV_PER"]
        headers.append(date_column)
        output = io.StringIO(newline="")
        writer = csv.writer(output)
        writer.writerow(headers)
        for i in range(30):  # comfortably exceeds the production 1,000-byte minimum
            row = [f"TEST{i:02d}", "EQ", "100.0", "1000", "50.0", dates[i % len(dates)]]
            writer.writerow(row)
        return output.getvalue().encode("utf-8")

    def test_accepts_exact_expected_date(self):
        raw = self.make_csv(["14-11-2026"])
        self.assertTrue(validate_full_delivery(raw, "14112026"))

    def test_rejects_previous_day(self):
        raw = self.make_csv(["13-11-2026"])
        self.assertFalse(validate_full_delivery(raw, "14112026"))

    def test_rejects_mixed_eq_dates(self):
        raw = self.make_csv(["14-11-2026", "13-11-2026"])
        self.assertFalse(validate_full_delivery(raw, "14112026"))

    def test_rejects_missing_date_column(self):
        output = io.StringIO(newline="")
        writer = csv.writer(output)
        writer.writerow(["SYMBOL", "SERIES", "CLOSE_PRICE", "DELIV_QTY", "DELIV_PER"])
        for i in range(30):
            writer.writerow([f"TEST{i:02d}", "EQ", "100.0", "1000", "50.0"])
        self.assertFalse(validate_full_delivery(output.getvalue().encode("utf-8"), "14112026"))

    def test_rejects_malformed_eq_date(self):
        raw = self.make_csv(["not-a-date"])
        self.assertFalse(validate_full_delivery(raw, "14112026"))

    def test_accepts_supported_alias_and_compact_format(self):
        raw = self.make_csv(["20261114"], date_column="TRADDT")
        self.assertTrue(validate_full_delivery(raw, "14112026"))

    def test_rejects_invalid_expected_stamp(self):
        raw = self.make_csv(["14-11-2026"])
        self.assertFalse(validate_full_delivery(raw, "not-a-date"))

    def test_archived_daily_accepts_exact_date_without_delivery_fields(self):
        output = io.StringIO(newline="")
        writer = csv.writer(output)
        writer.writerow(["SYMBOL", "SERIES", "CLOSE_PRICE", "DATE1"])
        for i in range(100):  # exceed the validator's production 1,000-byte minimum
            writer.writerow([f"TEST{i:03d}", "EQ", "100.0", "14-11-2026"])
        self.assertTrue(validate_archived_daily_file(output.getvalue().encode("utf-8"), "14112026"))

    def test_archived_daily_rejects_wrong_date(self):
        raw = self.make_csv(["13-11-2026"])
        self.assertFalse(validate_archived_daily_file(raw, "14112026"))

    def test_archived_daily_rejects_mixed_dates(self):
        raw = self.make_csv(["14-11-2026", "13-11-2026"])
        self.assertFalse(validate_archived_daily_file(raw, "14112026"))

    def test_archived_daily_rejects_missing_date_column(self):
        output = io.StringIO(newline="")
        writer = csv.writer(output)
        writer.writerow(["SYMBOL", "SERIES", "CLOSE_PRICE"])
        for i in range(30):
            writer.writerow([f"TEST{i:02d}", "EQ", "100.0"])
        self.assertFalse(validate_archived_daily_file(output.getvalue().encode("utf-8"), "14112026"))


    def make_udiff_zip(self, dates):
        output = io.StringIO(newline="")
        fields = ["TckrSymb", "SctySrs", "TradDt", "ClsPric", "OpnPric",
                  "HghPric", "LwPric", "TtlTradgVol"]
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for i in range(30):
            writer.writerow({
                "TckrSymb": f"TEST{i:03d}", "SctySrs": "EQ",
                "TradDt": dates[i % len(dates)], "ClsPric": "100",
                "OpnPric": "99", "HghPric": "101", "LwPric": "98",
                "TtlTradgVol": "10000",
            })
        raw = io.BytesIO()
        with zipfile.ZipFile(raw, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("cm_test.csv", output.getvalue())
        return raw.getvalue()

    def run_udiff(self, dates, stamp="14112026"):
        with TemporaryDirectory() as directory:
            return normalize_udiff(self.make_udiff_zip(dates), stamp, Path(directory))

    def test_udiff_accepts_exact_source_date(self):
        self.assertTrue(self.run_udiff(["14-11-2026"]))

    def test_udiff_rejects_missing_source_date(self):
        self.assertFalse(self.run_udiff([""]))

    def test_udiff_rejects_malformed_source_date(self):
        self.assertFalse(self.run_udiff(["not-a-date"]))

    def test_udiff_rejects_mixed_dates_even_when_expected_is_present(self):
        self.assertFalse(self.run_udiff(["14-11-2026", "13-11-2026"]))

    def test_udiff_rejects_all_wrong_dates(self):
        self.assertFalse(self.run_udiff(["13-11-2026"]))

    def test_udiff_rejects_invalid_expected_stamp(self):
        self.assertFalse(self.run_udiff(["14-11-2026"], stamp="invalid"))


if __name__ == "__main__":
    unittest.main()
