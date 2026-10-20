import unittest

from pipeline.quarterly_pdf_xbrl_metrics import ALIASES, choose, parse_xbrl


class QuarterlyXbrlMetricTests(unittest.TestCase):
    def test_sebi_taxonomy_revenue_pat_eps_facts_are_recognized(self):
        xml = b"""<?xml version="1.0" encoding="UTF-8"?>
        <xbrl xmlns="http://www.xbrl.org/2003/instance">
          <context id="QTR"><entity><identifier scheme="https://example.test">INE123A01011</identifier></entity>
            <period><startDate>2026-07-01</startDate><endDate>2026-09-30</endDate></period></context>
          <unit id="INR"><measure>INR</measure></unit>
          <unit id="INRPS"><measure>INRPerShare</measure></unit>
          <RevenueFromOperations contextRef="QTR" unitRef="INR">123456</RevenueFromOperations>
          <ProfitLossForPeriod contextRef="QTR" unitRef="INR">23456</ProfitLossForPeriod>
          <BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations contextRef="QTR" unitRef="INRPS">2.34</BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations>
        </xbrl>"""
        facts = parse_xbrl(xml)
        period = "2026-09-30"
        revenue = choose(facts, ALIASES["REVENUE"], period)
        pat = choose(facts, ALIASES["PAT"], period)
        eps = choose(facts, ALIASES["EPS"], period)
        self.assertIsNotNone(revenue)
        self.assertIsNotNone(pat)
        self.assertIsNotNone(eps)
        self.assertEqual(revenue["value"], 123456)
        self.assertEqual(pat["value"], 23456)
        self.assertEqual(eps["value"], 2.34)
        self.assertEqual(eps["tag"], "basicearningsloss-persharefromcontinuinganddiscontinuedoperations".replace("-", ""))

    def test_missing_period_or_unit_cannot_be_selected(self):
        facts = [{"tag": "revenuefromoperations", "value": 100, "context": "QTR",
                  "period_end": "", "unit": "INR", "instant": False}]
        self.assertIsNone(choose(facts, ALIASES["REVENUE"], "2026-09-30"))


    def test_iso_context_dates_are_not_reinterpreted_day_first(self):
        from pipeline.quarterly_pdf_xbrl_metrics import date_iso
        self.assertEqual(date_iso("2026-04-01"), "2026-04-01")
        self.assertEqual(date_iso("2026-06-30"), "2026-06-30")

    def test_nse_month_name_date_and_invalid_iso_date(self):
        from pipeline.quarterly_pdf_xbrl_metrics import date_iso
        self.assertEqual(date_iso("30-JUN-2026"), "2026-06-30")
        self.assertEqual(date_iso("2026-02-30"), "")


    def test_insurance_taxonomy_tags_are_recognized_without_pbt_substitution(self):
        from pipeline.quarterly_pdf_xbrl_metrics import ALIASES
        tags = {
            "operatingincome",
            "income",
            "profitlossaftertax",
            "profitlossaftertaxbeforeextraordinaryitems",
            "profitlossaftertaxandextraordinaryitems",
            "basicanddilutedepsbeforeextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized",
            "basicanddilutedepsafterextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized",
        }
        normalized = {item.lower().replace("_", "") for values in ALIASES.values() for item in values}
        self.assertTrue({"profitlossaftertax", "profitlossaftertaxbeforeextraordinaryitems",
                         "profitlossaftertaxandextraordinaryitems"}.issubset(normalized))
        self.assertTrue({"basicanddilutedepsbeforeextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized",
                         "basicanddilutedepsafterextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized"}.issubset(normalized))
        self.assertIn("operatingincome", tags)
        self.assertIn("income", tags)

if __name__ == "__main__":
    unittest.main()
