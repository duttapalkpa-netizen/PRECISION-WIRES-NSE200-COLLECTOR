import csv
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from pipeline.join_bis_usd_inr_panel import join_panel


FIELDS = ["FREQ", "REF_AREA", "CURRENCY", "COLLECTION", "UNIT_MULT", "DECIMALS", "AVAILABILITY", "TITLE", "TIME_PERIOD", "OBS_VALUE", "OBS_STATUS", "OBS_PRE_BREAK", "OBS_CONF"]


class TestJoinBisUsdInrPanel(unittest.TestCase):
    def make_inputs(self, tmp: Path):
        panel = tmp / "h10.csv"
        with panel.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["date", "usd_inr", "usd_inr_status", "broad_usd_index", "broad_usd_index_status"])
            w.writeheader()
            w.writerow({"date": "2026-11-04", "usd_inr": "94.64", "usd_inr_status": "A", "broad_usd_index": "121.4", "broad_usd_index_status": "A"})
            w.writerow({"date": "2026-11-05", "usd_inr": "", "usd_inr_status": "ND", "broad_usd_index": "121.5", "broad_usd_index_status": "A"})
            w.writerow({"date": "2026-11-06", "usd_inr": "93.91", "usd_inr_status": "A", "broad_usd_index": "121.8", "broad_usd_index_status": "A"})
        bis = tmp / "bis.csv"
        rows = [
            ["D", "IN", "INR", "A", "0", "6", "A", "daily average", "2026-11-04", "94.640809", "A", "", "F"],
            ["D", "IN", "INR", "A", "0", "6", "A", "daily average", "2026-11-05", "NaN", "M", "", "F"],
        ]
        with bis.open("w", newline="") as f:
            w = csv.writer(f); w.writerow(FIELDS); w.writerows(rows)
        raw = bis.read_bytes()
        manifest = tmp / "bis.manifest.json"
        manifest.write_text(json.dumps({
            "sha256": hashlib.sha256(raw).hexdigest(),
            "source_class": "OFFICIAL_INTERNATIONAL_ORGANIZATION",
            "series": "D.IN.INR.A",
            "dataflow": "BIS,WS_XRU,1.0",
            "retrieved_at_utc": "2026-11-12T00:00:00Z",
        }))
        return panel, bis, manifest

    def test_join_preserves_missing_and_absent_bis_dates(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            panel, bis, manifest = self.make_inputs(tmp)
            result = join_panel(panel, bis, manifest, tmp / "out")
            with (tmp / "out" / "fed_h10_bis_usd_inr_daily_panel.csv").open(newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(rows[0]["bis_usd_inr"], "94.640809")
            self.assertEqual(rows[0]["bis_usd_inr_status"], "A")
            self.assertEqual(rows[1]["bis_usd_inr"], "")
            self.assertEqual(rows[1]["bis_usd_inr_status"], "M")
            self.assertEqual(rows[2]["bis_usd_inr"], "")
            self.assertEqual(rows[2]["bis_usd_inr_status"], "NO_OBSERVATION")
            self.assertEqual(result["bis_status_counts_on_h10_calendar"], {"A": 1, "M": 1, "NO_OBSERVATION": 1})
            self.assertEqual(result["both_sources_active_comparison_pairs"], 1)

    def test_rejects_bis_raw_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            panel, bis, manifest = self.make_inputs(tmp)
            m = json.loads(manifest.read_text()); m["sha256"] = "0" * 64
            manifest.write_text(json.dumps(m))
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                join_panel(panel, bis, manifest, tmp / "out")


if __name__ == "__main__":
    unittest.main()
