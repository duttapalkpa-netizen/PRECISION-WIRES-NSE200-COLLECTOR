# South Africa (ZAF) Q2-2026 — official SARB KBP5339M monthly USD/ZAR series verification
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 218 / Research Verification 52
Status: OFFICIAL SARB MONTHLY USD/ZAR MIDDLE-RATE SERIES AND ALL THREE Q2 MONTHLY OBSERVATIONS VERIFIED; DAILY EXCX135D HISTORY AND BOP TRANSACTION-CONVERSION RULE REMAIN OPEN.

## 1. Mandatory continuity preflight and duplicate prevention
- Re-fetched Master Continuity & Acceptance Ledger; pre-task blob SHA-1: b4ef5d706d380464edbe5dc55ab482ed651288cd.
- Re-fetched GCR Master Priority Queue; pre-task blob SHA-1: 441eff0a4664465a4b0675025b4b34ead0f41f89.
- Re-fetched Historical Task Registry; pre-task blob SHA-1: 712b60a188cb4ddda3dd305ef49071dc1642d6f3.
- Reopened C216 and C217. Excluded completed daily API route discovery, matrix gate correction, Selected Historical Rates UI discovery and KBP export-family boundary audit.
- Existing ZAF liability PASS is retained. Asset REVIEW, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED remain unchanged.

## 2. Official series identity established from SARB Quarterly Bulletin
- Opened SARB Quarterly Bulletin — September 2026, Statistical tables: External economic accounts, page S-114 (PDF page 30).
- The table is titled 'Exchange rates' and specifies 'Middle rates in cents (R1 = 100 cents) per foreign currency unit'.
- The USA Dollar column explicitly identifies the monthly series code `(5339M)`; the row heading is `Average for`.
- The same table footnote 1 states: 'Weighted average of the banks’ daily rates at approximately 10:30. Weights are based on the banks’ foreign-exchange transactions.'
- This establishes the SARB published monthly-average middle-rate series as KBP5339M / USA Dollar in SA cents per US dollar. It is a different frequency and statistical object from daily API series EXCX135D.

## 3. Q2-2026 observations transcribed from the official SARB table
| Month | Official table value (SA cents per USD) | Rand per USD (divide by 100) |
|---|---:|---:|
| April 2026 | 1,653.90 | 16.5390 |
| May 2026 | 1,648.06 | 16.4806 |
| June 2026 | 1,639.70 | 16.3970 |
- These three observations are independently consistent with the SARB Monthly Release of Selected Data No. 449 (July 2026) and No. 451 (September 2026), which show April–June monthly values.
- The table is explicitly monthly average, not daily observation rows. No quarterly mean was calculated: a defensible quarter aggregation would require the correct daily/transaction weighting and the applicable BOP compilation rule.

## 4. Critical methodology boundary
- The 10:30 weighted-average footnote describes the bank daily-rate construction of this monthly middle-rate series. It does NOT by itself prove that SARB uses this series to convert portfolio investment transactions in the BOP, nor that the monthly average is the required quarter conversion convention.
- This series cannot replace the requested daily `EXCX135D` observations. It is a verified official monthly benchmark and potential cross-check only.
- No daily observations, response headers, raw API payload or raw-file SHA-256 were captured in this continuation. PDF text was inspected through the official SARB publication surface; no claim of byte-level archival is made.
- No unverified KBP daily code, hidden export URL or query parameter was invented.

## 5. Acceptance disposition
| Gate | Status |
|---|---|
| Current ledger/queue/registry preflight | PASS |
| Official SARB KBP USA Dollar monthly-average series identity | PASS |
| Series frequency and unit | PASS — monthly, SA cents per USD |
| Q2 2026 April/May/June monthly observations | PASS — 3/3 |
| Conversion from cents to rand | PASS — arithmetic only |
| SARB 10:30 weighted-average footnote captured | PASS |
| Daily EXCX135D Q2 observations | NOT_CAPTURED |
| Raw daily payload / headers / UTC / SHA-256 | NOT_CAPTURED |
| BOP portfolio transaction FX conversion convention | NOT_ESTABLISHED |
| ZAF asset reconciliation | REVIEW / NOT PASS |
| ZAF liability reconciliation | Existing PASS retained |
| ZAF full country validation / aggregate admission | PARTIAL / NOT PASS; NOT_AUTHORIZED |

## 6. Next exact action (C219)
1. Use the exact official monthly series identity KBP5339M only for its documented monthly frequency; inspect whether SARB's official query facility offers any separate daily USD/ZAR middle-rate series, without assuming KBP5339M is daily.
2. Continue to inspect the Selected Historical Rates client-side export contract for daily EXCX135D; retrieve only after an exact official request is observed.
3. Independently locate a current SARB BOP compilation methodology statement identifying the FX conversion convention for portfolio investment flows. Keep the 10:30 note scoped to the published rate series only.
4. Do not calculate or promote the ZAF asset reconciliation until the source frequency and BOP convention are fit for purpose.

## 7. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, synthetic data, fabricated timestamps, guessed daily series code, unapproved FX/sign/scale transform, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 8. Official source references
- SARB Quarterly Bulletin September 2026, Statistical tables — External economic accounts, p. S-114: https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/quarterly-bulletin-publications/2026/september/8-tables-external-economic-accounts.pdf
- SARB Monthly Release No. 449, July 2026: https://www.resbank.co.za/content/dam/sarb/publications/monthly-releases/monthly-release-of-selected-data/2026/Eng%20449.pdf
- SARB Monthly Release No. 451, September 2026: https://www.resbank.co.za/content/dam/sarb/publications/monthly-releases/monthly-release-of-selected-data/2026/Eng%20451.pdf
- SARB Online Statistical Query: https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query
- Controlling prior report: docs/GCR_ZAF_Q2_2026_SARB_ONLINE_STATISTICAL_QUERY_EXPORT_FAMILY_BOUNDARY_CONTINUATION217_20261121.md