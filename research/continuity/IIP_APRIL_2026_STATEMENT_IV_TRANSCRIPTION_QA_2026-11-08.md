# April 2026 IIP Statement IV — transcription and QA
Date: 2026-11-08
Status: PASS_TRANSCRIPTION_AND_WEIGHTED_AGGREGATE_QA_WITH_SOURCE_TYPE_LIMITATION

## Source and scope
- Primary source: PIB / MoSPI Release ID 2278961, posted 2026-06-29 16:00 IST.
- URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
- Statement IV, "INDEX OF INDUSTRIAL PRODUCTION - MONTHWISE", source-rendered lines 157–199.
- Table heading: base 2011-12=100; NIC 2025; month columns May-25 through May-26. April-26 is the 13th month column.
- Release lines 21–25 and 40–41 establish that the entire 2022-23 IIP series was superseded using Output PPI and the 29-Jun release replaces the earlier 1-Jun WPI-based series. Statement IV is the historical month-wise panel.
- Transcription ledger: research/data/iip_april_2026_statement_iv_output_ppi_pib_transcription.csv
- This is a separately typed PIB HTML release transcription, NOT a recovered native MoSPI catalogue XLSX and NOT the e-Sankhyiki API response.

## Extraction
- Extracted 37 April-2026 index rows: 23 manufacturing NIC-2 classes, manufacturing aggregate, 4 mining rows, 5 electricity/gas rows, 3 water/waste rows, and General Index.
- Each row retains release ID/date, Statement IV, reference month, base, classification, deflator context, series type, NIC code, description, weight, April index, source line range, and source type.
- No missing values were imputed. No catalogue ID inferred. No source type substitution.

## QA results
- Row count: 37; duplicate NIC-code keys: 0.
- All April index values are numeric and positive; missing April values: 0.
- Manufacturing component weights sum to 76.065 vs published aggregate weight 76.062 (difference +0.003, consistent with displayed weight rounding); weighted April index = 118.6934, rounds to published manufacturing aggregate 118.7.
- Mining component weights sum to 11.053; weighted April index = 106.0877, rounds to published Mining & Quarrying aggregate 106.1.
- Electricity generation component weights sum to 10.171; weighted April index = 122.9177, rounds to published Electricity aggregate 122.9.
- Electricity + Gas component weights sum to 10.865; weighted April index = 121.7285, rounds to published Electricity & Gas Supply aggregate 121.7.
- Water component weights sum to 2.020; weighted April index = 146.0667, rounds to published Water Supply, Sewerage & Waste Management aggregate 146.1.
- General Index independently transcribed as 118.2.
- QA is a transcription/structure and weighted-aggregate consistency check. It is not an independent source-agency audit and does not prove native workbook/API equivalence.

## Source-type and methodology limitations
- Statement IV is explicitly headed Base 2011-12=100, while the superseding release explains that the revised IIP series uses Output PPI and updated source-agency data. Preserve both exact labels; do not silently relabel the Statement IV table as base 2022-23.
- The PIB release is a secondary official publication channel for this historical month-wise panel. Native April e-Sankhyiki catalogue table/XLSX remains NOT RECOVERED; old catalogue ID IIPMFY26002APR remains 404 in the preserved manifest.
- API schema and exact monthly API filters remain NOT VERIFIED.
- Do not join this ledger into the 2022-23 NIC-2025 monthly workbook panel without an explicit series/statement mapping and methodology review.

## Conclusion
April 2026 month-wise PIB Statement IV transcription and weighted aggregate consistency QA: PASS_WITH_SOURCE_TYPE_LIMITATION.
Native catalogue source recovery, API reconciliation, full observation-vintage audit, and master Hard Gate remain BLOCKED.

## Invariants
Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, and V11.3(A/B/C/D/E) unchanged. UNKNOWN remains neither PASS nor FAIL. Research spend ₹0.
