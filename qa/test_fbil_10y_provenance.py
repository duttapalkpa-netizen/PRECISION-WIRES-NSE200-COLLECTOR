import unittest
from datetime import datetime
class TestFbilTimestampSemantics(unittest.TestCase):
    def test_ist_to_utc_conversion(self):
        from zoneinfo import ZoneInfo
        dt=datetime.fromisoformat("2026-10-16T18:30:00+05:30")
        self.assertEqual(dt.astimezone(ZoneInfo("UTC")).isoformat(),"2026-10-16T13:00:00+00:00")
    def test_no_observation_time_substitution(self):
        source=open("pipeline/audit_fbil_10y_provenance.py",encoding="utf-8").read()
        self.assertIn("Publisher Date + Time",source)
        self.assertIn("refusing to infer timestamp",source)
        self.assertIn("NOT_PROMOTED_PENDING_WRITTEN_USE_PERMISSION",source)
if __name__=="__main__": unittest.main()
