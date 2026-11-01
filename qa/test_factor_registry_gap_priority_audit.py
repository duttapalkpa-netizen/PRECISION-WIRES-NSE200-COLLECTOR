import unittest
from pipeline.factor_registry_gap_priority_audit import build_priority

def rows():
    return [
      {"factor_id":f"F{i:02d}","coverage_status":"NOT_CONNECTED" if i<=10 else "PARTIAL_SOURCE_COVERAGE",
       "source_statuses":"macro_indicators:NOT_CONNECTED;sector_fundamentals:NOT_CONNECTED" if i<=4 else ("macro_indicators:NOT_CONNECTED;sector_fundamentals:AVAILABLE" if i<=6 else "macro_indicators:AVAILABLE;sector_fundamentals:AVAILABLE")}
      for i in range(1,36)
    ]

class GapPriorityTests(unittest.TestCase):
    def test_shared_gap_ranking_is_deterministic(self):
        r=build_priority(rows())
        self.assertEqual(r["factor_groups"],35)
        self.assertEqual(r["recommended_first_source_group"],"macro_indicators")
        self.assertEqual(r["source_groups_ranked"][0]["not_connected_factor_count"],6)
        self.assertEqual(r["source_groups_ranked"][1]["not_connected_factor_count"],4)
    def test_missing_factor_rows_fail_closed(self):
        with self.assertRaises(ValueError): build_priority(rows()[:-1])
    def test_duplicate_factor_ids_fail_closed(self):
        data=rows(); data[-1]["factor_id"]=data[0]["factor_id"]
        with self.assertRaises(ValueError): build_priority(data)

if __name__=="__main__": unittest.main()
