import unittest

from pipeline.quarterly_pdf_xbrl_metrics import ALIASES, choose, parse_xbrl, fetch_attachment, basis_from_xbrl_facts


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

    def test_basis_is_resolved_only_from_matching_explicit_xbrl_dimensions(self):
        xml = b"""<?xml version="1.0" encoding="UTF-8"?>
        <xbrl xmlns="http://www.xbrl.org/2003/instance"
              xmlns:xbrldi="http://xbrl.org/2006/xbrldi">
          <context id="QTR"><entity><identifier scheme="https://example.test">INE123A01011</identifier>
            <segment><xbrldi:explicitMember dimension="ind:StatementTypeAxis">ind:ConsolidatedMember</xbrldi:explicitMember></segment>
          </entity><period><startDate>2026-04-01</startDate><endDate>2026-06-30</endDate></period></context>
          <unit id="INR"><measure>INR</measure></unit>
          <unit id="INRPS"><measure>INRPerShare</measure></unit>
          <RevenueFromOperations contextRef="QTR" unitRef="INR">123</RevenueFromOperations>
          <ProfitLossForPeriod contextRef="QTR" unitRef="INR">45</ProfitLossForPeriod>
          <BasicEarningsPerShare contextRef="QTR" unitRef="INRPS">2</BasicEarningsPerShare>
        </xbrl>"""
        facts = parse_xbrl(xml)
        selected = [
            choose(facts, ALIASES["REVENUE"], "2026-06-30"),
            choose(facts, ALIASES["PAT"], "2026-06-30"),
            choose(facts, ALIASES["EPS"], "2026-06-30"),
        ]
        self.assertEqual(basis_from_xbrl_facts(selected), "CONSOLIDATED")
        selected[1] = dict(selected[1], dimensions=[])
        self.assertEqual(basis_from_xbrl_facts(selected), "")

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


    def test_official_archive_host_fallback_on_403(self):
        from unittest.mock import MagicMock
        import requests
        first = MagicMock()
        first.status_code = 403
        second = MagicMock()
        second.status_code = 200
        second.content = b"<xbrl/>"
        second.headers = {"Content-Type": "application/xml"}
        second.raise_for_status.return_value = None
        session = MagicMock()
        session.get.side_effect = [first, second]
        response, fetched_url = fetch_attachment(
            session,
            "https://nsearchives.nseindia.com/corporate/xbrl/sample.xml",
        )
        self.assertIs(response, second)
        self.assertEqual(
            fetched_url,
            "https://archives.nseindia.com/corporate/xbrl/sample.xml",
        )
        self.assertEqual(session.get.call_count, 2)

if __name__ == "__main__":
    unittest.main()
