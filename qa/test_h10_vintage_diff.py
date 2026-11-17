import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.h10_vintage_diff import TARGET_SERIES, VintageError, load_snapshot, compare


class H10VintageDiffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write_snapshot(self, name, rows, timestamp, label="unspecified"):
        csv_path = self.root / f"{name}.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["date", "series_id", "value", "status"])
            writer.writeheader()
            writer.writerows(rows)
        digest = hashlib.sha256(csv_path.read_bytes()).hexdigest()
        manifest = {
            "source_url": "https://www.federalreserve.gov/releases/h10/",
            "source_publication_timestamp": timestamp,
            "retrieved_at": "2026-11-17T10:00:00+00:00",
            "raw_byte_length": 100,
            "raw_sha256": "a" * 64,
            "normalized_csv_sha256": digest,
            "series_id": TARGET_SERIES,
            "vintage_label": label,
        }
        manifest_path = self.root / f"{name}.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return csv_path, manifest_path

    def row(self, day, value, status="A"):
        return {"date": day, "series_id": TARGET_SERIES, "value": value, "status": status}

    def test_diff_classifies_all_row_outcomes_without_imputing_nd(self):
        old_csv, old_manifest = self.write_snapshot("old", [
            self.row("2026-08-03", "100.0"),
            self.row("2026-08-04", "-9999", "ND"),
            self.row("2026-08-05", "101.0"),
        ], "2026-08-10T16:15:00-04:00", "pre_correction")
        new_csv, new_manifest = self.write_snapshot("new", [
            self.row("2026-08-03", "100.5"),
            self.row("2026-08-04", "-9999", "ND"),
            self.row("2026-08-06", "102.0"),
        ], "2026-08-12T16:15:00-04:00", "post_correction")
        old_rows, _ = load_snapshot(old_csv, old_manifest)
        new_rows, _ = load_snapshot(new_csv, new_manifest)
        records, counts = compare(old_rows, new_rows)
        self.assertEqual(counts, {
            "unchanged": 1, "changed": 1, "added": 1,
            "removed": 1, "missing_or_status_changed": 0,
        })
        changed = next(x for x in records if x["classification"] == "changed")
        self.assertEqual(changed["absolute_delta"], "0.5")
        self.assertEqual(changed["relative_delta_pct"], "0.5")
        self.assertEqual(next(x for x in records if x["date"] == "2026-08-04")["old_value"], "")

    def test_rejects_duplicate_or_unsorted_dates(self):
        csv_path, manifest_path = self.write_snapshot("bad", [
            self.row("2026-08-04", "1"), self.row("2026-08-03", "2")
        ], "2026-08-10T16:15:00-04:00")
        with self.assertRaisesRegex(VintageError, "chronological"):
            load_snapshot(csv_path, manifest_path)

    def test_rejects_hash_mismatch(self):
        csv_path, manifest_path = self.write_snapshot("bad_hash", [
            self.row("2026-08-03", "1")
        ], "2026-08-10T16:15:00-04:00")
        manifest = json.loads(manifest_path.read_text())
        manifest["normalized_csv_sha256"] = "0" * 64
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(VintageError, "SHA-256 mismatch"):
            load_snapshot(csv_path, manifest_path)

    def test_rejects_naive_publication_timestamp(self):
        csv_path, manifest_path = self.write_snapshot("bad_time", [
            self.row("2026-08-03", "1")
        ], "2026-08-10T16:15:00-04:00")
        manifest = json.loads(manifest_path.read_text())
        manifest["source_publication_timestamp"] = "2026-08-10T16:15:00"
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(VintageError, "timezone"):
            load_snapshot(csv_path, manifest_path)

    def test_rejects_nd_values_other_than_missing_sentinel(self):
        csv_path, manifest_path = self.write_snapshot("bad_nd", [
            self.row("2026-08-03", "0", "ND")
        ], "2026-08-10T16:15:00-04:00")
        with self.assertRaisesRegex(VintageError, "ND value"):
            load_snapshot(csv_path, manifest_path)


if __name__ == "__main__":
    unittest.main()
