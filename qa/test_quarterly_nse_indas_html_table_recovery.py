import unittest
from pathlib import Path

from pipeline.quarterly_nse_indas_html_table_recovery import (
    EVIDENCE_DIR,
    extract_indas_html_table_metrics,
    validate_official_ixbrl_url,
)

CASES = [
    {
        "sha": "ec03bf103a78e74f2c9126f8b49ac47b921986d7dfdc3a953e6ab2107e9ccb72",
        "symbol": "UPL", "isin": "INE628A01036",
        "revenue": 18260000000.0, "pat": 990000000.0, "eps": 1.17,
    },
    {
        "sha": "b0edaa012723d083381f5b48843afa7bd114f3456cf430519f503cad68c1628c",
        "symbol": "ADANIENT", "isin": "INE423A01024",
        "revenue": 59675700000.0, "pat": 12244500000.0, "eps": 9.07,
    },
    {
        "sha": "65158c0a0793cddab1b622c8b0951d51c8b43e3cd4211e36b85c9e5a012448f2",
        "symbol": "JSWENERGY", "isin": "INE121E01018",
        "revenue": 9222600000.0, "pat": 2612100000.0, "eps": 1.43,
    },
    {
        "sha": "a646e445a681b211e29f27c2d59975cff8c381ed839afb072197bbd649aab901",
        "symbol": "ADANIGREEN", "isin": "INE364U01010",
        "revenue": 78900000000.0, "pat": 330000000.0, "eps": 0.20,
    },
]

class NSEIndASHtmlTableRecoveryTests(unittest.TestCase):
    def load_case(self, case):
        path = EVIDENCE_DIR / (case["sha"] + ".bin")
        if not path.is_file():
            self.skipTest("pinned NSE source artifact has not been downloaded")
        blob = path.read_bytes()
        import hashlib
        self.assertEqual(hashlib.sha256(blob).hexdigest(), case["sha"])
        return blob

    def test_four_official_source_pages_parse_exact_quarterly_metrics(self):
        for case in CASES:
            with self.subTest(symbol=case["symbol"]):
                blob = self.load_case(case)
                result = extract_indas_html_table_metrics(blob, {
                    "SYMBOL": case["symbol"],
                    "ISIN": case["isin"],
                    "BASIS": "STANDALONE",
                    "PERIOD_END": "2026-09-30",
                })
                self.assertEqual(result["BASIS"], "STANDALONE")
                self.assertEqual(result["PERIOD_END"], "2026-09-30")
                self.assertEqual(result["REVENUE_UNIT"], "INR")
                self.assertEqual(result["PAT_UNIT"], "INR")
                self.assertEqual(result["EPS_UNIT"], "INR_PER_SHARE")
                self.assertEqual(result["REVENUE_CONTEXT_START"], "2026-07-01")
                self.assertAlmostEqual(result["REVENUE"], case["revenue"], places=2)
                self.assertAlmostEqual(result["PAT"], case["pat"], places=2)
                self.assertAlmostEqual(result["EPS"], case["eps"], places=4)

    def test_symbol_mismatch_fails_closed(self):
        case = CASES[0]
        with self.assertRaisesRegex(ValueError, "symbol"):
            extract_indas_html_table_metrics(self.load_case(case), {
                "SYMBOL": "WRONG", "ISIN": case["isin"],
                "BASIS": "STANDALONE", "PERIOD_END": "2026-09-30",
            })

    def test_period_mismatch_fails_closed(self):
        case = CASES[0]
        with self.assertRaisesRegex(ValueError, "period end"):
            extract_indas_html_table_metrics(self.load_case(case), {
                "SYMBOL": case["symbol"], "ISIN": case["isin"],
                "BASIS": "STANDALONE", "PERIOD_END": "2026-06-30",
            })

    def test_basis_mismatch_fails_closed(self):
        case = CASES[0]
        with self.assertRaisesRegex(ValueError, "basis"):
            extract_indas_html_table_metrics(self.load_case(case), {
                "SYMBOL": case["symbol"], "ISIN": case["isin"],
                "BASIS": "CONSOLIDATED", "PERIOD_END": "2026-09-30",
            })

    def test_exact_official_ixbrl_origin_required(self):
        self.assertEqual(
            validate_official_ixbrl_url(
                "https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_208232_02112026172019_iXBRL_WEB.html"
            ),
            "https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_208232_02112026172019_iXBRL_WEB.html",
        )
        for unsafe in (
            "http://nsearchives.nseindia.com/corporate/ixbrl/a.html",
            "https://nsearchives.nseindia.com.attacker.invalid/corporate/ixbrl/a.html",
            "https://example.com/corporate/ixbrl/a.html",
            "https://nsearchives.nseindia.com/other/a.html",
        ):
            with self.subTest(url=unsafe), self.assertRaises(ValueError):
                validate_official_ixbrl_url(unsafe)

if __name__ == "__main__":
    unittest.main()
