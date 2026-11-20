# Romania (ROU) Q2-2026 — BNR / ECB portfolio-flow source gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-1
Decision: **ROU cohort membership PASS; official methodology/source-family discovery PASS; exact Q2-2026 national portfolio asset/liability observations NOT_CAPTURED; numeric comparison NOT_DONE; ROU PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate rejection
- Re-fetched the current Master Continuity & Acceptance Ledger (blob SHA `d913928ec432d55d4cccfc6c0e9783ff9000a94f`) and GCR Master Priority Queue (blob SHA `37d17a2b4ffe3350c446af41acbf2d6f4a146d61`).
- Reused the immutable fixed 63-country Q2-2026 both-leg cohort at `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv` (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`). ROU is present with both IMF entries marked PRESENT.
- Repository search found no dedicated ROU Q2-2026 national portfolio dual-leg reconciliation report. NPL's exact NRB XLSX route is closed after two distinct failed byte-retrieval routes; it was not retried. No cohort rebuild or IMF re-query.

## 2. Official national methodology boundary
- IMF SDDS/DQAF Romania metadata identifies the National Bank of Romania (NBR/BNR) as the responsible compiler and says BOP is compiled largely under BPM6.
- The same metadata states BOP is disseminated monthly and quarterly; quarterly data are released approximately 85 days after quarter-end. It explicitly says financial-account transactions are compiled gross but disseminated net, separately for individual asset and liability components. This is the required conceptual shape for separate A_NFA_T and L_NIL_T checks; it does not provide the Q2-2026 values.
- The metadata also states that BOP data are revised monthly as additional transactions and sources become available, and quarters are subsequently revised. Therefore an observation vintage / revision cutoff must be captured before any comparison.

## 3. Official data catalogue observations
- ECB BPS (Balance of Payments and International Investment Position, BPM6) catalogue identifies Romania national-source series. The monthly total-economy portfolio-liability transaction series key observed in the catalogue is `BPS.M.N.RO.W1.S1.S1.T.L.FA.P.F._Z.RON._T.M.N.ALL`; it is denominated in millions of RON, quarterly/monthly metadata identifies transaction flow, and the series page reports source as National Bank of Romania.
- A separate monthly total-economy portfolio-liability series in EUR was also indexed. The catalogue describes the collection indicator as “summed through period”; this must be interpreted from the series metadata/API before any monthly aggregation. Do not assume the monthly observations can simply be summed.
- The search index also exposes quarterly Romania portfolio series, but the inspected quarterly transaction listing was last updated 17-Apr-2026, before the target Q2-2026 observation could be established. It is not evidence of Q2 availability.
- Exact ECB SDW API CSV requests for the matching monthly total-economy asset and liability RON series for 2026-04 through 2026-06 were attempted through the current web retrieval bridge. Both endpoints were inaccessible in this execution. No response body, headers, values, retrieval receipt or raw-file SHA-256 was obtained.
- A BNR historical XLS download locator surfaced in search, but it was not proven to be the current Q2-2026 portfolio flow table and was not admitted as a valid Q2 source.

## 4. Gate matrix
| Gate | Status |
|---|---|
| ROU in fixed 63-country Q2-2026 both-leg cohort | PASS |
| Existing ROU national report duplicate search | PASS (no dedicated report found) |
| BNR responsible compiler / BPM6 metadata | PASS |
| Financial-account gross compilation / net separate asset-liability dissemination | PASS |
| Revision practice / Q2 release timing recorded | PASS |
| Official national-source Q2-2026 asset observation | NOT_CAPTURED |
| Official national-source Q2-2026 liability observation | NOT_CAPTURED |
| Monthly-vs-quarterly / cumulative basis verified for target rows | NOT_ESTABLISHED |
| RON/EUR unit, signs and instrument scope crosswalk at Q2 | NOT_ESTABLISHED |
| Raw source bytes, retrieval metadata and SHA-256 | NOT_CAPTURED |
| Same-vintage comparison to archived IMF Q2 rows | NOT_DONE |
| ROU national validation | PARTIAL / NOT PASS |
| 63-country aggregate / production | NOT_AUTHORIZED |

## 5. Next exact action
- Use a supported official BNR or ECB SDW download/API route to retrieve both separate total-economy portfolio transaction legs for 2026-Q2 (or the three April–June monthly observations only if the source explicitly confirms the monthly flow semantics and summation basis).
- Archive untouched source bytes and response metadata first; record retrieval timestamp, exact series keys, source vintage, byte count and SHA-256. Then inspect the original observation period, unit, sign, BPM6 concept, sector and instrument coverage.
- Reuse only the already archived IMF exact ROU Q2 rows; no new IMF GET. Compare assets and liabilities separately, never net them. If the official raw route remains inaccessible, preserve ROU PARTIAL / NOT PASS and advance to the next eligible fixed-cohort member.

## 6. Evidence links
- IMF SDDS/DQAF Romania BOP metadata: https://dsbb.imf.org/sdds/dqaf-base/country/ROU/category/BOP00
- ECB BPS Romania monthly portfolio-liability series (RON): https://data.ecb.europa.eu/data/datasets/BPS/BPS.M.N.RO.W1.S1.S1.T.L.FA.P.F._Z.RON._T.M.N.ALL
- ECB BPS catalogue / portfolio investment: https://data.ecb.europa.eu/data/data-categories/balance-payments-and-other-external-statistics/balance-payments-and-international-investment-position/financial-account/portfolio-investment
- ECB BPS revision policy: https://data.ecb.europa.eu/data/data-categories/2771575/data-information
- ECB SDW API attempted asset endpoint: https://data-api.ecb.europa.eu/service/data/BPS/BPS.M.N.RO.W1.S1.S1.T.A.FA.P.F._Z.RON._T.M.N.ALL?startPeriod=2026-04&endPeriod=2026-06&format=csvdata
- ECB SDW API attempted liability endpoint: https://data-api.ecb.europa.eu/service/data/BPS/BPS.M.N.RO.W1.S1.S1.T.L.FA.P.F._Z.RON._T.M.N.ALL?startPeriod=2026-04&endPeriod=2026-06&format=csvdata

## 7. Protected invariants
No cohort rebuild, no IMF re-query, no netting, no stock-as-flow substitution, no unverified monthly aggregation, no inferred FX conversion, no fabricated timestamp/value, no paid API, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Research spend ₹0.
