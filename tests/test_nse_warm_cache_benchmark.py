import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from collector.nse_warm_cache_benchmark import audit_cache


class WarmCacheBenchmarkTests(unittest.TestCase):
    def test_reports_requested_hits_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch("collector.nse_warm_cache_benchmark.validate_cached_file", return_value=True) as validate:
                result = audit_cache(Path(tmp), 3)
        self.assertEqual(result["valid_cache_hits"], 3)
        self.assertEqual(result["cache_misses"], 0)
        self.assertEqual(result["network_requests"], 0)
        self.assertEqual(result["benchmark_type"], "local_warm_cache_validation_only")
        self.assertEqual(validate.call_count, 3)

    def test_reports_misses_instead_of_claiming_warm_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch("collector.nse_warm_cache_benchmark.validate_cached_file", return_value=False):
                result = audit_cache(Path(tmp), 2)
        self.assertEqual(result["valid_cache_hits"], 0)
        self.assertEqual(result["cache_misses"], 2)
        self.assertEqual(result["network_requests"], 0)

    def test_rejects_zero_sessions(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit_cache(Path(tmp), 0)


if __name__ == "__main__":
    unittest.main()
