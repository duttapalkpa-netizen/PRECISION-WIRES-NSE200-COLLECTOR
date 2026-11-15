import subprocess
import sys
import unittest


class BoundedShardArgumentTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "collector/nse_download.py", *args],
            text=True, capture_output=True, timeout=5,
        )

    def test_rejects_start_without_end(self):
        result = self.run_cli("--start-date", "2026-02-09")
        self.assertEqual(result.returncode, 2)
        self.assertIn("must be supplied together", result.stderr)

    def test_rejects_end_without_start(self):
        result = self.run_cli("--end-date", "2026-11-13")
        self.assertEqual(result.returncode, 2)
        self.assertIn("must be supplied together", result.stderr)

    def test_rejects_non_iso_date(self):
        result = self.run_cli("--start-date", "09-02-2026", "--end-date", "2026-11-13")
        self.assertEqual(result.returncode, 2)
        self.assertIn("YYYY-MM-DD", result.stderr)

    def test_rejects_reversed_date_range(self):
        result = self.run_cli("--start-date", "2026-11-13", "--end-date", "2026-02-09")
        self.assertEqual(result.returncode, 2)
        self.assertIn("on or before", result.stderr)


if __name__ == "__main__":
    unittest.main()
