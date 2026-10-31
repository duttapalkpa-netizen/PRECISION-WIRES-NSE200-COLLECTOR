from datetime import date
from pathlib import Path
import csv
import tempfile
import unittest

from collector.nse_download import validate_cached_file


class CacheDateValidationTests(unittest.TestCase):
    def _write_csv(self, path: Path, trade_date: str) -> None:
        # More than 1 KB so the production validator's minimum-size check is exercised.
        rows = [
            {"SYMBOL": f"TEST{i:03d}", "SERIES": "EQ", "DATE1": trade_date, "CLOSE_PRICE": "101.25"}
            for i in range(80)
        ]
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    def test_accepts_cache_only_for_expected_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sec_bhavdata_full_30102026.csv"
            self._write_csv(path, "30-Oct-2026")
            self.assertTrue(validate_cached_file(path, date(2026, 10, 30)))

    def test_rejects_wrong_trade_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sec_bhavdata_full_30102026.csv"
            self._write_csv(path, "29-Oct-2026")
            self.assertFalse(validate_cached_file(path, date(2026, 10, 30)))

    def test_rejects_mixed_trade_dates(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sec_bhavdata_full_30102026.csv"
            self._write_csv(path, "30-Oct-2026")
            with path.open("a", encoding="utf-8") as handle:
                handle.write("BAD999,EQ,29-Oct-2026,99.0\n")
            self.assertFalse(validate_cached_file(path, date(2026, 10, 30)))


if __name__ == "__main__":
    unittest.main()