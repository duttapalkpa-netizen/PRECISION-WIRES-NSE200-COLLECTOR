import unittest
import pandas as pd
from pipeline.nse_market_microstructure_coverage_reconcile import reconcile

def panel():
    rows=[]
    for i in range(200):
        rows.append({"DATE":f"session-{i:03d}","SYMBOL":f"S{i}","SERIES":"EQ",
          "CIRCUIT_STATUS":"UNKNOWN","SURVEILLANCE_STATUS":"UNKNOWN","FREE_FLOAT":"UNKNOWN",
          "BHAVCOPY_SOURCE_URL":"https://archives.nseindia.com/products/content/sec_bhavdata_full_x.csv",
          "BHAVCOPY_SOURCE_SHA256":"a"*64,"PRICE_BAND_SOURCE_URL":"https://nsearchives.nseindia.com/content/equities/sec_list_x.csv",
          "PRICE_BAND_SOURCE_SHA256":"b"*64,"REG_IND_SOURCE_URL":"https://nsearchives.nseindia.com/content/cm/REG_INDx.csv",
          "REG_IND_SOURCE_SHA256":"c"*64,"REG1_IND_SOURCE_URL":"https://nsearchives.nseindia.com/content/cm/REG1_INDx.csv",
          "REG1_IND_SOURCE_SHA256":"d"*64})
    return pd.DataFrame(rows)

def report(d):
    return {"status":"PARTIAL_SOURCE_COVERAGE","sessions":200,"panel_rows":len(d),
      "promotion_allowed":False,"snapshot_id":"1f6d79d9bcdf3a6aa11dd9a80033276061447401dac6c708ab6622b6258b7534",
      "date_min":"2026-01-09","date_max":"2026-11-02","bhavcopy_sha256_revalidated_sessions":200,
      "price_band_files":200,"surveillance_old_files":200,"surveillance_new_files":200,
      "price_band_join_coverage":0.96,"reg_ind_join_coverage":0.86,"reg1_ind_join_coverage":0.86,
      "circuit_status_unknown_rows":len(d),"surveillance_status_unknown_rows":len(d),
      "free_float_unknown_rows":len(d),"observed_at_utc":"2026-11-03T06:48:10Z"}

class MarketMicrostructureReconcileTests(unittest.TestCase):
    def test_valid_panel_stays_warning_and_not_available(self):
        d=panel(); cov={"sources":[{"source":"market_microstructure","status":"NOT_CONNECTED","rows":0}]}
        out=reconcile(cov,report(d),d,"e"*64)
        x=out["sources"][0]
        self.assertEqual(x["status"],"DATA_QUALITY_WARN")
        self.assertEqual(x["rows"],0)
        self.assertEqual(x["observed_rows"],200)
    def test_unknown_fields_cannot_be_promoted(self):
        d=panel(); d.loc[0,"FREE_FLOAT"]="100"
        with self.assertRaises(ValueError): reconcile({"sources":[]},report(d),d,"e"*64)
    def test_duplicate_security_session_rejected(self):
        d=panel(); d.loc[1,["DATE","SYMBOL","SERIES"]]=d.loc[0,["DATE","SYMBOL","SERIES"]]
        with self.assertRaises(ValueError): reconcile({"sources":[]},report(d),"", "e"*64)
    def test_snapshot_identity_is_pinned(self):
        d=panel(); r=report(d); r["snapshot_id"]="wrong"
        with self.assertRaises(ValueError): reconcile({"sources":[]},r,d,"e"*64)

if __name__=="__main__": unittest.main()
