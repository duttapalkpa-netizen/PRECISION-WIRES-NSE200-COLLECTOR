import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

from collector.nse_warm_cache_benchmark import audit_cache


def seed_sessions(root, count):
    dates = []
    day = date(2026, 10, 30)
    while len(dates) < count:
        if day.weekday() < 5:
            dates.append(day.isoformat())
            (root / f"sec_bhavdata_full_{day.strftime('%d%m%Y')}.csv").write_text("fixture")
        day -= timedelta(days=1)
    (root / "sessions.txt").write_text("\\n".join(dates) + "\\n")


class WarmCacheBenchmarkTests(unittest.TestCase):
    def test_reports_requested_hits_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_sessions(root, 3)
            with patch("collector.nse_warm_cache_benchmark.validate_cached_file", return_value=True) as validate:
                result = audit_cache(root, 3)
        self.assertEqual(result["valid_cache_hits"], 3)
        self.assertEqual(result["cache_misses"], 0)
        self.assertEqual(result["network_requests"], 0)
        self.assertEqual(result["sessions_checked"], 3)
        self.assertEqual(validate.call_count, 3)

    def test_reports_misses_instead_of_claiming_warm_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_sessions(root, 2)
            with patch("collector.nse_warm_cache_benchmark.validate_cached_file", return_value=False):
                result = audit_cache(root, 2)
        self.assertEqual(result["valid_cache_hits"], 0)
        self.assertEqual(result["cache_misses"], 2)
        self.assertEqual(result["network_requests"], 0)

    def test_rejects_zero_sessions(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit_cache(Path(tmp), 0)

    def test_rejects_missing_session_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RuntimeError):
                audit_cache(Path(tmp), 2)


if __name__ == "__main__":
    unittest.main()
