import tempfile
import unittest
from pathlib import Path
import pandas as pd

from scripts.research.audit_raw_processed_integrity import audit


class RawProcessedIntegrityTests(unittest.TestCase):
    def write_raw(self, root, date, rows):
        path = root / f"sec_bhavdata_full_{date}.csv"
        pd.DataFrame(rows, columns=["SYMBOL", "SERIES"]).to_csv(path, index=False)
        return path

    def test_exact_raw_processed_keys_pass(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "raw"
            root.mkdir()
            self.write_raw(root, "02012026", [["ABC", "EQ"], ["XYZ", "EQ"]])
            self.write_raw(root, "05012026", [["ABC", "EQ"], ["XYZ", "EQ"]])
            processed = Path(td) / "processed.csv"
            pd.DataFrame([
                ["ABC", "2026-01-02"], ["XYZ", "2026-01-02"],
                ["ABC", "2026-01-05"], ["XYZ", "2026-01-05"],
            ], columns=["SYMBOL", "DATE"]).to_csv(processed, index=False)
            result = audit(root, processed)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["raw_session_count"], 2)
            self.assertEqual(result["missing_raw_symbol_date_key_count"], 0)

    def test_duplicate_raw_key_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "raw"
            root.mkdir()
            self.write_raw(root, "02012026", [["ABC", "EQ"], ["ABC", "EQ"]])
            processed = Path(td) / "processed.csv"
            pd.DataFrame([["ABC", "2026-01-02"]], columns=["SYMBOL", "DATE"]).to_csv(processed, index=False)
            result = audit(root, processed)
            self.assertEqual(result["status"], "FAIL")
            self.assertIn("DUPLICATE_RAW_SYMBOL_DATE_KEYS", result["issues"])

    def test_missing_processed_session_and_key_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "raw"
            root.mkdir()
            self.write_raw(root, "02012026", [["ABC", "EQ"]])
            self.write_raw(root, "05012026", [["ABC", "EQ"]])
            processed = Path(td) / "processed.csv"
            pd.DataFrame([["ABC", "2026-01-02"]], columns=["SYMBOL", "DATE"]).to_csv(processed, index=False)
            result = audit(root, processed)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["missing_processed_session_dates"], ["2026-01-05"])
            self.assertEqual(result["missing_raw_symbol_date_key_count"], 1)

    def test_processed_extra_date_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "raw"
            root.mkdir()
            self.write_raw(root, "02012026", [["ABC", "EQ"]])
            processed = Path(td) / "processed.csv"
            pd.DataFrame([["ABC", "2026-01-03"]], columns=["SYMBOL", "DATE"]).to_csv(processed, index=False)
            result = audit(root, processed)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["extra_processed_session_dates"], ["2026-01-03"])

    def test_symbol_session_gaps_reported_without_inventing_rows(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "raw"
            root.mkdir()
            self.write_raw(root, "02012026", [["ABC", "EQ"], ["XYZ", "EQ"]])
            self.write_raw(root, "05012026", [["ABC", "EQ"]])
            processed = Path(td) / "processed.csv"
            pd.DataFrame([
                ["ABC", "2026-01-02"], ["XYZ", "2026-01-02"],
                ["ABC", "2026-01-05"],
            ], columns=["SYMBOL", "DATE"]).to_csv(processed, index=False)
            result = audit(root, processed)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["symbols_with_incomplete_raw_session_coverage"], 1)
            self.assertEqual(result["symbol_session_gaps"]["XYZ"]["missing_sessions"], 1)


if __name__ == "__main__":
    unittest.main()
