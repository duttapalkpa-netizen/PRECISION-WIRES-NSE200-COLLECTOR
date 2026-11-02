import unittest
from pathlib import Path

class CGAArchiveDiscoveryContracts(unittest.TestCase):
    def test_discovery_is_official_host_only_and_evidence_only(self):
        s=Path("pipeline/discover_cga_monthly_report_archive.py").read_text()
        self.assertIn('("cga.gov.in","www.cga.gov.in")',s)
        self.assertIn("Candidate assets are not downloaded",s)
        self.assertIn("No source is promoted into Factor Registry",s)
    def test_timestamp_limits_are_explicit(self):
        s=Path("pipeline/discover_cga_monthly_report_archive.py").read_text()
        self.assertIn("not treated as report release timestamps",s)
        self.assertIn("crawl timestamps",s)
    def test_bounded_financial_year_scope_and_timeout(self):
        s=Path("pipeline/discover_cga_monthly_report_archive.py").read_text()
        self.assertIn("range(2014,2026)",s)
        self.assertIn("timeout=22",s)
        self.assertIn("max_workers=4",s)

if __name__=="__main__": unittest.main()
