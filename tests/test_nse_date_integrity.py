import csv
import io
import unittest

from collector.nse_download import validate_full_delivery


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


if __name__ == "__main__":
    unittest.main()
