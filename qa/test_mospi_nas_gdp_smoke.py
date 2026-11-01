import tempfile
import unittest
from pathlib import Path
from openpyxl import Workbook
from pipeline.collect_mospi_nas_gdp_smoke import workbook_inventory, extract_gdp_observation

class GDPWorkbookSmokeTests(unittest.TestCase):
    def test_inventory_requires_real_numeric_quarterly_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.xlsx"
            wb = Workbook()
            ws = wb.active
            ws.title = "GDP"
            ws.append(["Statement 1: GDP Q1 FY2026-27 (Constant Prices)", None, None, None])
            ws.append([None, "Sector", "Quarterly Levels", None, None,
                       "Percentage Change Over Previous Year", None])
            ws.append([None, None, "2024-25", "2025-26", "2026-27", "2025-26", "2026-27"])
            ws.append([None, "GDP", 7061843.45, 7546229.74, 8136153.44, 6.85, 7.817])
            ws.append([None, None, "sparse trailing value"])
            wb.save(path)
            result = workbook_inventory(path)
            self.assertGreater(result["numeric_cells"], 0)
            self.assertIn("Q1", result["quarter_tokens_found"])
            observation = extract_gdp_observation(path)
            self.assertAlmostEqual(observation["value"], 8136153.44, places=2)
            self.assertAlmostEqual(observation["yoy_growth_percent"], 7.817, places=3)

    def test_empty_workbook_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.xlsx"
            Workbook().save(path)
            with self.assertRaises(RuntimeError):
                workbook_inventory(path)

if __name__ == "__main__":
    unittest.main()
