import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/research/build_raw_archive_manifest.py"
SPEC = importlib.util.spec_from_file_location("raw_manifest", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RawArchiveManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.raw = self.root / "data/raw"
        self.qa = self.root / "data/qa"
        self.raw.mkdir(parents=True)
        self.qa.mkdir(parents=True)
        self.raw_file = self.raw / "sec_bhavdata_full_13112026.csv"
        self.raw_file.write_text(
            "SYMBOL,SERIES,DATE1,CLOSE_PRICE\nABC,EQ,13-11-2026,100\nXYZ,EQ,13-11-2026,200\n",
            encoding="utf-8",
        )
        (self.raw / "sessions.txt").write_text("2026-11-13\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def run_audit(self):
        with patch.object(MODULE, "RAW", self.raw), patch.object(MODULE, "OUT", self.qa / "manifest.json"):
            return MODULE.main(), json.loads((self.qa / "manifest.json").read_text())

    def test_valid_file_date_and_sha256_pass(self):
        code, report = self.run_audit()
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["raw_file_count"], 1)
        self.assertEqual(len(report["files"][0]["sha256"]), 64)

    def test_mixed_eq_dates_fail(self):
        self.raw_file.write_text(
            "SYMBOL,SERIES,DATE1,CLOSE_PRICE\nABC,EQ,13-11-2026,100\nXYZ,EQ,14-11-2026,200\n",
            encoding="utf-8",
        )
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "FAIL")
        self.assertGreater(report["files"][0]["date_mismatch_rows"], 0)

    def test_missing_date_column_fails_without_crashing(self):
        self.raw_file.write_text("SYMBOL,SERIES,CLOSE_PRICE\nABC,EQ,100\n", encoding="utf-8")
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertEqual(report["files"][0]["status"], "FAIL")

    def test_duplicate_session_entries_fail(self):
        (self.raw / "sessions.txt").write_text("2026-11-13\n2026-11-13\n", encoding="utf-8")
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        self.assertTrue(any("duplicate dates" in x for x in report["blockers"]))

    def test_invalid_filename_date_fails_without_crashing(self):
        invalid = self.raw / "sec_bhavdata_full_32132026.csv"
        invalid.write_text("SYMBOL,SERIES,DATE1\nABC,EQ,13-11-2026\n", encoding="utf-8")
        code, report = self.run_audit()
        self.assertEqual(code, 1)
        bad = next(x for x in report["files"] if x["file"].endswith("32132026.csv"))
        self.assertEqual(bad["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
