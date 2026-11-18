import tempfile
import unittest
import zipfile
from pathlib import Path

from qa.inspect_brazil_bop6_archive import inspect_archive


class BCBArchiveInspectionTests(unittest.TestCase):
    def make_zip(self, path, members):
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for name, payload in members:
                z.writestr(name, payload)

    def test_valid_archive_inventory_and_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "monthly.zip"
            self.make_zip(p, [("BOP6_monthly.xlsx", b"workbook-placeholder"),
                              ("readme.txt", b"readme")])
            result = inspect_archive(p)
        self.assertEqual(result["status"], "PASS_ZIP_INTEGRITY_AND_INVENTORY_ONLY")
        self.assertEqual(result["archive"]["member_count"], 2)
        self.assertEqual(result["archive"]["data_candidate_count"], 2)
        self.assertEqual(len(result["archive"]["sha256"]), 64)

    def test_non_zip_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "not.zip"
            p.write_bytes(b"not a zip")
            with self.assertRaises(ValueError):
                inspect_archive(p)

    def test_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "unsafe.zip"
            self.make_zip(p, [("../escape.csv", b"bad")])
            with self.assertRaises(ValueError):
                inspect_archive(p)

    def test_empty_zip_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "empty.zip"
            with zipfile.ZipFile(p, "w"):
                pass
            with self.assertRaises(ValueError):
                inspect_archive(p)


if __name__ == "__main__":
    unittest.main()
