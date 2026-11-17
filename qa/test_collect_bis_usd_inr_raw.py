import csv
import hashlib
import io
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from pipeline import collect_bis_usd_inr_raw as collector


def csv_bytes():
    return (
        "STRUCTURE,STRUCTURE_ID,ACTION,FREQ,REF_AREA,CURRENCY,OBS_VALUE,OBS_STATUS,TIME_PERIOD\n"
        "dataflow,BIS:WS_XRU(1.0),I,D,IN,INR,83.5,A,2026-11-06\n"
    ).encode()


class FakeResponse:
    def __init__(self, raw, url=collector.SOURCE_URL, content_type="text/csv"):
        self.raw, self.url = raw, url
        self.headers = {"Content-Type": content_type}
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def geturl(self): return self.url
    def read(self, limit): return self.raw[:limit]


class TestBisUsdInrCollector(unittest.TestCase):
    def test_archives_exact_csv_bytes_and_hash_manifest(self):
        raw = csv_bytes()
        with tempfile.TemporaryDirectory() as d:
            with patch.object(collector, "urlopen", return_value=FakeResponse(raw)):
                result = collector.archive(Path(d), datetime(2026, 11, 12, tzinfo=timezone.utc))
            saved = Path(result["archive"]).read_bytes()
            manifest = json.loads(Path(result["manifest"]).read_text())
            self.assertEqual(saved, raw)
            self.assertEqual(manifest["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(manifest["series"], "D.IN.INR.A")
            self.assertFalse(manifest["raw_payload_parsed"])

    def test_rejects_lookalike_initial_host(self):
        with patch.object(collector, "urlopen") as mocked:
            with self.assertRaises(ValueError):
                collector.retrieve("https://stats.bis.org.attacker.example/data.csv")
            mocked.assert_not_called()

    def test_rejects_non_https_redirect(self):
        response = FakeResponse(csv_bytes(), "http://stats.bis.org/data.csv")
        with patch.object(collector, "urlopen", return_value=response):
            with self.assertRaises(ValueError):
                collector.retrieve()

    def test_rejects_non_sdmx_csv(self):
        response = FakeResponse(b"<html>not data</html>", content_type="text/html")
        with patch.object(collector, "urlopen", return_value=response):
            with self.assertRaisesRegex(ValueError, "expected SDMX-CSV"):
                collector.retrieve()


if __name__ == "__main__":
    unittest.main()
