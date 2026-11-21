# Samoa WSM — Q2-2026 CBS quarterly BOP portfolio source-boundary audit (Continuation 125)
Date: 2026-11-21

## Decision
The Central Bank of Samoa (CBS) publishes a quarterly bulletin with a dedicated BOP Table B-1 that explicitly separates Portfolio Investment (net), Assets and Liabilities, uses BPM6, and reports Tala millions. This is the correct official source family. However, the latest inspected June 2026 Quarterly Bulletin explicitly covers the March 2026 quarter (Q1 2026); Table B-1's final period column is 2026-I. It does not contain Q2 2026. Therefore no Q2-2026 national portfolio asset/liability values are captured. WSM remains PARTIAL / NOT PASS; dual-leg comparison NOT_DONE; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity Ledger, pre-task blob SHA `102208e5e1d8cf5f127484479eef0089e008d59e`.
- Re-fetched GCR Master Priority Queue, pre-task blob SHA `967b4e7d968811c6e9d6d9d117ba285897750b6b`.
- Re-fetched immutable 63-country cohort report, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`; WSM follows VNM in the fixed order.
- Scoped repository search for Samoa/WSM Q2-2026 national dual-leg report returned no dedicated prior report.
- No IMF re-query, no cohort rebuild, no reuse of annual forecast or IIP stock as BOP transactions.

## 2. Official CBS quarterly publication and coverage
- CBS Quarterly Bulletin index: https://cbs.gov.ws/quarterly-bulletin
- CBS index says quarterly bulletins provide data to the end of the quarter under review and are published with a three-month delay. The index lists June 2026 as latest.
- June 2026 Quarterly Bulletin PDF (CBS source, mirrored document): https://docs.publicnow.com/viewDoc?filename=8206%5CEXT%5C159BE72D593A154372A2DE971402265894F32B7E_23E93C95A79A56F777925FFF5F41BEDBB8BAE1CA.PDF
- Cover/title identifies “Quarterly Bulletin June 2026”, Vol XLV No.2. Contents and narrative explicitly identify the period as “first quarter of 2026” / March quarter 2026.
- Table B-1, Balance of Payments, PDF printed page 34, unit “Amounts in Tala Million”. It has annual columns and quarterly columns for 2021, 2022, 2023, 2024, 2025 and 2026-I only. It separately labels:
  - Portfolio Investment (net)
  - Assets
  - Liabilities
- Table note: based on IMF Balance of Payments Manual 6th Edition (BPM6).
- Therefore the publication demonstrates an official quarterly BOP portfolio dual-leg series, but latest available quarter in this bulletin is 2026-I, not 2026-II (Q2).
- Do not read the Q2/June label in the bulletin title as the reporting quarter. The bulletin is published in June but reports the March quarter.

## 3. Adjacent sources rejected
- CBS Monetary Policy Statement 2025/2027 gives annual financial-year BOP estimates/forecasts and portfolio investment net only; it is not Q2-2026 quarterly dual-leg evidence.
- IMF 2026 Article IV table presents annual financial account and portfolio net estimates/projections, not Q2 national asset/liability transactions.
- CBS IIP table reports positions/stocks and latest Q1 2026; it is not a BOP flow substitute.
- No annual-to-quarter allocation, net-to-leg back-solving, Tala/USD conversion, or use of estimates/projections is permitted.

## 4. Gate matrix
| Gate | Status |
|---|---|
| WSM membership in fixed 63-country cohort | PASS |
| No prior dedicated WSM Q2-2026 report found in scoped repo search | PASS (scoped search only) |
| Official CBS quarterly BOP source family | PASS |
| Separate portfolio net/assets/liabilities labels | PASS |
| BPM6 note | PASS |
| Latest inspected CBS bulletin | June 2026 bulletin |
| Actual reporting quarter in latest bulletin | Q1 2026 / March 2026 |
| Q2-2026 national portfolio asset leg | NOT_CAPTURED |
| Q2-2026 national portfolio liability leg | NOT_CAPTURED |
| Q2-2026 source vintage / revision timestamp | NOT_ESTABLISHED |
| Numeric dual-leg comparison | NOT_DONE |
| WSM validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Next exact action
- Do not repeat the June 2026 bulletin extraction. Wait for/locate the next CBS quarterly bulletin covering June 2026 (Q2), expected according to CBS's stated three-month publication lag; the calendar expectation is not evidence of publication.
- When the Q2 bulletin appears, archive exact official bytes, URL, retrieval timestamp, byte count and SHA-256 before parsing; extract Q2-II asset/liability values, confirm Tala-million unit, sign convention and revision notes; compare to already archived IMF Q2 rows without a new IMF query.
- If Q2 release is not yet published, retain WSM PARTIAL / NOT PASS and advance to the next eligible fixed-cohort member after preflight.

## 6. Protected constraints
₹0; official/free sources only. No synthetic values, fabricated timestamps, annual forecast/estimate substitution, IIP stock-as-flow, net-to-leg back-solving, FX conversion, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
