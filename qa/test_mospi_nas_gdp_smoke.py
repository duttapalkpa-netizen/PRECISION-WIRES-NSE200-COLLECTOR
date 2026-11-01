import tempfile
import unittest
from pathlib import Path
from openpyxl import Workbook
from pipeline.collect_mospi_nas_gdp_smoke import workbook_inventory

class GDPWorkbookSmokeTests(unittest.TestCase):
    def test_inventory_requires_real_numeric_quarterly_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.xlsx"
            wb = Workbook()
            ws = wb.active
            ws.title = "GDP"
            ws.append(["Quarter", "GDP at constant prices"])
            ws.append(["Q1 FY 2026-27", 81.36])
            wb.save(path)
            result = workbook_inventory(path)
            self.assertGreater(result["numeric_cells"], 0)
            self.assertIn("Q1", result["quarter_tokens_found"])

    def test_empty_workbook_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.xlsx"
            Workbook().save(path)
            with self.assertRaises(RuntimeError):
                workbook_inventory(path)

if __name__ == "__main__":
    unittest.main()
