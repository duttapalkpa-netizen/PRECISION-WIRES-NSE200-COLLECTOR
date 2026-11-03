import unittest
from pipeline.sector_fundamentals_source_coverage_reconcile import reconcile

class SectorFundamentalsCoverageTests(unittest.TestCase):
    def test_nic2_iip_updates_only_to_warning_and_never_available(self):
        cov={"as_of_utc":"2026-11-03T04:00:00Z","sources_total":2,"available":1,
             "not_connected":1,"quality_warn":0,"blocked":0,
             "sources":[
               {"source":"benchmark_index","status":"AVAILABLE","rows":10},
               {"source":"sector_fundamentals","status":"NOT_CONNECTED","rows":0}
             ]}
        report={"status":"PARTIAL_SOURCE_COVERAGE","promotion_allowed":False,"observed_rows":966,
          "nic2_groups":23,"date_min":"2023-04","date_max":"2026-09",
          "catalogue_table_id":"IIPMFY26018AUG","catalogue_release_date":"28 Sep 2026",
          "catalogue_release_vintage":"Aug 2026","pib_release_url":"https://www.pib.gov.in/test",
          "observed_at_utc":"2026-11-03T06:16:32Z","output_sha256":"a"*64}
        out=reconcile(cov,report)
        row=next(x for x in out["sources"] if x["source"]=="sector_fundamentals")
        self.assertEqual(row["status"],"DATA_QUALITY_WARN")
        self.assertEqual(row["rows"],0)
        self.assertEqual(row["observed_rows"],966)
        self.assertEqual(out["available"],1)
        self.assertEqual(out["not_connected"],0)
        self.assertEqual(out["quality_warn"],1)
        self.assertFalse(out["sector_fundamentals_adapter"]["promotion_allowed"])

    def test_adapter_report_cannot_be_promoted_if_not_partial(self):
        cov={"sources":[{"source":"sector_fundamentals","status":"NOT_CONNECTED","rows":0}]}
        with self.assertRaises(ValueError):
            reconcile(cov,{"status":"PASS","promotion_allowed":True,"observed_rows":966,"nic2_groups":23})

if __name__=="__main__":
    unittest.main()
