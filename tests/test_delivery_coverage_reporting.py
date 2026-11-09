import unittest
import pandas as pd
from qa.validate_dataset import _coverage

class DeliveryCoverageTests(unittest.TestCase):
    def test_two_missing_values_are_not_rounded_to_full_coverage(self):
        values = pd.Series([1] * 500806 + [None, None], dtype="float64")
        present, missing, pct = _coverage(values, 500808)
        self.assertEqual(present, 500806)
        self.assertEqual(missing, 2)
        self.assertLess(pct, 100.0)
        self.assertAlmostEqual(pct, 99.9996001663, places=8)

    def test_empty_dataset_reports_zero_coverage(self):
        present, missing, pct = _coverage(pd.Series([], dtype="float64"), 0)
        self.assertEqual((present, missing, pct), (0, 0, 0.0))

if __name__ == "__main__":
    unittest.main()
