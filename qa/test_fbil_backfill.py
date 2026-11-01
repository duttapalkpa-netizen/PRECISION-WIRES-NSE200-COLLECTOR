import unittest
from datetime import date
from pipeline.backfill_fbil_gsec_history import month_ranges

class TestFbilBackfillRanges(unittest.TestCase):
    def test_month_windows_are_contiguous_and_exclusive(self):
        windows=list(month_ranges(date(2025,11,1),date(2026,2,1)))
        self.assertEqual([(a.isoformat(),b.isoformat()) for a,b in windows],
                         [("2025-11-01","2025-12-01"),("2025-12-01","2026-01-01"),("2026-01-01","2026-02-01")])
if __name__=="__main__": unittest.main()
