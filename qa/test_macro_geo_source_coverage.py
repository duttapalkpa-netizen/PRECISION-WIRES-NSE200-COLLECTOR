import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pipeline.macro_geo_source_coverage as coverage


class MacroGeoSourceCoverageTests(unittest.TestCase):
    def test_two_row_fpi_snapshot_is_not_counted_as_available_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            flows = root / "data/external/fpi_dii_flows.csv"
            flows.parent.mkdir(parents=True)
            flows.write_text(
                "DATE,GROUP,NET_VALUE\n2026-11-20,FPI,100\n2026-11-20,DII,200\n",
                encoding="utf-8",
            )
            out = root / "outputs/macro_geo"
            report_path = out / "source_coverage.json"
            with patch.object(coverage, "ROOT", root), patch.object(coverage, "OUT", out), patch.object(coverage, "REPORT", report_path):
                coverage.main()
            report = json.loads(report_path.read_text(encoding="utf-8"))
            flow = next(row for row in report["sources"] if row["source"] == "fpi_dii_flows")
            self.assertEqual(flow["status"], "DATA_QUALITY_WARN")
            self.assertEqual(flow["rows"], 2)
            self.assertEqual(report["p0_coverage"]["groups"]["fpi_dii_flows"]["status"], "INSUFFICIENT_HISTORICAL_COVERAGE")
            self.assertNotIn("fpi_dii_flows", report["p0_coverage"]["available_groups"])
            self.assertEqual(report["quality_warn"], 1)


if __name__ == "__main__":
    unittest.main()
