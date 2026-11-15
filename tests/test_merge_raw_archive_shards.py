import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/research/merge_raw_archive_shards.py"
SPEC = importlib.util.spec_from_file_location("merge_shards", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MergeRawArchiveShardsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.inputs = self.root / "artifacts"
        self.output = self.root / "merged"

    def tearDown(self):
        self.tmp.cleanup()

    def shard(self, name, entries):
        folder = self.inputs / name
        folder.mkdir(parents=True)
        (folder / "sessions.txt").write_text("".join(day + "\n" for day, _ in entries), encoding="utf-8")
        for day, payload in entries:
            stamp = day[8:10] + day[5:7] + day[:4]
            (folder / f"sec_bhavdata_full_{stamp}.csv").write_bytes(payload)
        return folder

    def test_merges_exact_sessions_and_preserves_bytes(self):
        one = b"original raw bytes one\n"
        two = b"original raw bytes two\n"
        self.shard("shard-01", [("2026-11-12", one)])
        self.shard("shard-02", [("2026-11-13", two)])
        self.assertEqual(MODULE.merge(self.inputs, self.output, 2), 0)
        self.assertEqual((self.output / "sec_bhavdata_full_12112026.csv").read_bytes(), one)
        self.assertEqual((self.output / "sec_bhavdata_full_13112026.csv").read_bytes(), two)
        self.assertEqual((self.output / "sessions.txt").read_text(), "2026-11-12\n2026-11-13\n")

    def test_rejects_duplicate_date_across_shards(self):
        entry = [("2026-11-13", b"raw\n")]
        self.shard("shard-01", entry)
        self.shard("shard-02", entry)
        self.assertEqual(MODULE.merge(self.inputs, self.output, 1), 1)

    def test_rejects_missing_expected_session(self):
        self.shard("shard-01", [("2026-11-13", b"raw\n")])
        self.assertEqual(MODULE.merge(self.inputs, self.output, 2), 1)

    def test_rejects_raw_file_not_listed_in_sessions(self):
        folder = self.shard("shard-01", [("2026-11-13", b"raw\n")])
        (folder / "sessions.txt").write_text("2026-11-12\n", encoding="utf-8")
        self.assertEqual(MODULE.merge(self.inputs, self.output, 1), 1)


if __name__ == "__main__":
    unittest.main()
