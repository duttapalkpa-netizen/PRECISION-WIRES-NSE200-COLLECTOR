# BCB September-2026 Domestic Portfolio Country-Period Cross-Check
Date: 2026-11-17
Status: PASS — COUNTRY-PERIOD QA VERIFIED AND RAW 22930 COMMITTED

## Independent official release
BCB's 26 October 2026 external-sector release reports for September 2026:
- Domestic-market portfolio investment net outflows: USD 2.1 billion.
- Domestic-market equity and investment-fund net outflows: USD 1.7 billion.
- Domestic-market debt-security net outflows: USD 0.4 billion.
Official release page: https://www.bcb.gov.br/estatisticas/estatisticassetorexterno?mode=light

## SGS mapping
- 22930: equities, domestic market, liabilities, monthly net.
- 22936: investment funds, liabilities, monthly net (previously captured/archived).
- 22942: debt securities, liabilities, domestic market, monthly net (previously captured/archived).

Candidate comparison:
- Equity + funds domestic outflow = -(22930 + 22936), USD million / 1000.
- Domestic debt outflow = -22942, USD million / 1000.
- Total = sum of the above.
The derived values are compared after rounding to USD 0.1 billion, matching the release's published precision. This is a specific country-period validation, not a general-purpose rounding tolerance.

## Workflow
Capture only the missing SGS 22930 raw CSV; reuse archived 22936 and 22942 bytes (do not re-fetch them). Record HTTP metadata, UTC retrieval, byte length, SHA-256; calculate and compare with the release; commit the raw file and report; re-fetch the committed blob and verify SHA-256. Timeout 5 minutes.

## Acceptance
- 22930 metadata: verified from official BCB dataset page.
- 22930 raw capture: pending runtime.
- September-2026 country-period comparison: pending runtime.
- This one-month validation does not establish all-period country-level equivalence or full Brazil pilot acceptance.
- EM-wide panel and production integration remain NOT_DONE / NOT_AUTHORIZED.


## Verified runtime result
- Workflow Run #1 / ID `44077864021`: SUCCESS.
- Permanent data commit: `446971a0da670d69e6dcb2c9efe0208ea50db572`.
- Archived path: `bcb_domestic_market_crosscheck_202609/` with `sgs_22930.csv`, `manifest.json`, `crosscheck_report.json`, `.gitattributes`.
- SGS 22930 raw CSV: HTTP 200; 8,669 bytes; SHA-256 `c4730c84ee81765a1c5ae41d91c1ea6f153bcb51ac70ee14b45b453b4dcab776`.
- September 2026 input values (USD million): 22930 domestic equity liabilities net = -2,110.8; 22936 investment-fund liabilities net = +416.8; 22942 domestic debt liabilities net = -382.4.
- Derived domestic equity + funds net outflow = USD 1.694bn; rounded to 0.1bn = USD 1.7bn.
- Derived domestic debt net outflow = USD 0.3824bn; rounded to 0.1bn = USD 0.4bn.
- Derived total domestic portfolio net outflow = USD 2.0764bn; rounded to 0.1bn = USD 2.1bn.
- All three rounded figures match BCB's 26-Oct-2026 official release exactly. Country-period QA: PASS for this September-2026 release comparison.
- The release's precision is USD 0.1bn; this validation does not establish a general series-level rounding tolerance or all-period equivalence.
