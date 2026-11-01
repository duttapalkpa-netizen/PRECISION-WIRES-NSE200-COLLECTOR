import unittest
from datetime import datetime
from pipeline.collect_oea_wpi_itemwise import period_label, parse_sheet_rows

class OEAItemwiseTests(unittest.TestCase):
    def test_month_period_variants(self):
        self.assertEqual(period_label("Apr-2023"), "2023-04")
        self.assertEqual(period_label("October 2026"), "2026-10")
        self.assertEqual(period_label(datetime(2024, 2, 1)), "2024-02")
        self.assertIsNone(period_label("Annual Average"))
    def test_wide_item_month_extraction(self):
        result = parse_sheet_rows("Test", [
            ["Commodity Code", "Commodity Description", "Apr-2023", "May-2023"],
            ["01", "All Commodities", 150.1, 151.2],
            ["02", "Food Articles", 160.0, None],
        ])
        self.assertEqual(result["parse_status"], "ITEM_PERIODS_PARSED")
        self.assertEqual(result["item_keys"], 2)
        self.assertEqual(result["observation_count"], 3)
        self.assertEqual(result["period_columns"][0]["period"], "2023-04")
        self.assertEqual(result["observations"][0]["item_code"], "01")
    def test_no_invented_code(self):
        result = parse_sheet_rows("Test", [
            ["Commodity Description", "Apr-2023"],
            ["All Commodities", 150.1],
        ])
        self.assertIsNone(result["item_code_column"])
        self.assertIsNone(result["observations"][0]["item_code"])
    def test_empty_sheet_is_not_pass(self):
        result = parse_sheet_rows("Empty", [])
        self.assertEqual(result["parse_status"], "EMPTY_SHEET")
        self.assertEqual(result["observations"], [])

if __name__ == "__main__":
    unittest.main()
