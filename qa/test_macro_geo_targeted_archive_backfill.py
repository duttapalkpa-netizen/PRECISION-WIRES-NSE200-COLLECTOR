import unittest
from datetime import date
import pandas as pd
from pipeline.macro_geo_targeted_archive_backfill import parse_nse_history_data, normalize_index_name

class NSEOfficialHistoryTests(unittest.TestCase):
    def test_official_history_parser_preserves_exact_identity_and_date(self):
        data=[{"EOD_INDEX_NAME":"NIFTY 50","EOD_TIMESTAMP":"15-SEP-2008","EOD_CLOSE_INDEX_VAL":"4210.15"}]
        frame=parse_nse_history_data(data,"NIFTY 50","NIFTY 50",date(2008,9,1),date(2008,9,30),"https://www.nseindia.com/api/historicalOR/indicesHistory?indexType=NIFTY%2050")
        self.assertEqual(len(frame),1)
        self.assertEqual(frame.iloc[0]["DATE"],"2008-09-15")
        self.assertEqual(frame.iloc[0]["SOURCE"],"NSE India official historicalOR indicesHistory API")
    def test_wrong_index_identity_fails_closed(self):
        data=[{"EOD_INDEX_NAME":"NIFTY BANK","EOD_TIMESTAMP":"15-SEP-2008","EOD_CLOSE_INDEX_VAL":"4210.15"}]
        with self.assertRaises(ValueError):
            parse_nse_history_data(data,"NIFTY 50","NIFTY 50",date(2008,9,1),date(2008,9,30),"https://www.nseindia.com/api/historicalOR/indicesHistory")
    def test_normalization_is_exact_punctuation_only(self):
        self.assertEqual(normalize_index_name("NIFTY 50"),"NIFTY50")
if __name__=="__main__": unittest.main()
