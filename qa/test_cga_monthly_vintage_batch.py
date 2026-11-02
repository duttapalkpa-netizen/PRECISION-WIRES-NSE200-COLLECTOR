import unittest
from pathlib import Path

SCRIPT=Path("pipeline/fetch_cga_monthly_vintage_batch.py").read_text()

class CGAVintageBatchContracts(unittest.TestCase):
    def test_bounded_month_batch_and_official_allowlist(self):
        self.assertIn('MONTHS={"April":4,"May":5,"June":6,"July":7,"August":8,"September":9}',SCRIPT)
        self.assertIn('parsed.hostname not in ("cga.gov.in","www.cga.gov.in")',SCRIPT)
        self.assertIn('"/writereaddata/MonthAccount/" not in parsed.path',SCRIPT)

    def test_internal_document_dates_never_become_release_timestamp(self):
        self.assertIn('"release_timestamp":None',SCRIPT)
        self.assertIn('"UNKNOWN_NOT_SUPPLIED_AS_PUBLICATION_TIMESTAMP"',SCRIPT)
        self.assertIn('"INTERNAL_DOCUMENT_METADATA_ONLY_NOT_RELEASE_TIMESTAMP"',SCRIPT)

    def test_no_registry_promotion_or_synthetic_vintage(self):
        self.assertIn('"No data is promoted to Factor Registry by this batch."',SCRIPT)
        self.assertIn('No archived historical vintage is certified',SCRIPT)
        self.assertIn('hashlib.sha256(body).hexdigest()',SCRIPT)

if __name__=="__main__": unittest.main()
