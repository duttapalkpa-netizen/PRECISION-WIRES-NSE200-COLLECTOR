# Solomon Islands SLB Q2-2026 — CBSI portfolio dual-leg source gate and sign-conflict audit
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-4 / Continuation 99
Decision: **SLB fixed-cohort membership PASS; official CBSI BPM6 quarterly BOP source PASS; Q2-2026 table reports portfolio financial-asset transactions SBD 38m and liability dash (general note defines dash as nil); narrative says portfolio investment deficit SBD 38m, creating unresolved sign/presentation conflict; exact IMF rows and SBD/USD transaction bridge NOT_CAPTURED; SLB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched current Master Continuity Ledger (blob SHA `1194f809a00a214913a5535969d3f80111e5fd1e`), GCR Master Priority Queue (blob SHA `15501663d5fbb531e220c5cc2546400477e550b2`), Rwanda Continuation 98 (blob SHA `001cc1fc2d6f698566206a7e746871d9eba1ee90`), and immutable 63-country Q2-2026 both-leg cohort (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- Reused existing Saudi Arabia (SAU) reconciliation and source-vintage follow-up: numeric two-leg check had already passed at displayed rounding, but exact same-vintage identity remains unresolved; did not repeat SAU.
- SLB (Solomon Islands) is the next fixed-cohort member after RWA and is present with both IMF A_NFA_T and L_NIL_T entries.
- Repository searches for SLB / Solomon Islands Q2-2026 national portfolio reconciliation found no dedicated prior country report. No cohort rebuild and no new IMF request.

## 2. Official CBSI source and BPM6 basis
- Central Bank of Solomon Islands (CBSI) official Balance of Payments page states the quarterly and annual BOP series covers current, capital and financial accounts and is based on BPM6. It states latest BOP statistics are 2026-Q2.
- CBSI Quarterly Review, June 2026, Chapter IV and Statistical Annex Table 1.17, “Capital Account and Financial Account”, reports annual and quarterly data, unit SBD million, quarterly columns through 2026-Q2, source CBSI.
- The publication general note says “-” means nil and warns that data are subject to periodic revision as updated information becomes available.
- Official page and PDF are cited below. Web text extraction exposed the table content. A direct container download attempt failed; no original PDF bytes, response headers, retrieval receipt, byte count or SHA-256 are claimed.

## 3. Q2-2026 national portfolio transaction table
CBSI Quarterly Review June 2026, Table 1.17 (SBD million), column 2026-Q2:
- Financial Assets total: 540.
- Portfolio investment under Financial Assets: +38.
- Financial Liabilities total: 539.
- Portfolio investment under Financial Liabilities: “-”, which the report's general note defines as nil.
- Other relevant rows: net lending (+)/borrowing (-) from Financial Account = +2.
- This is transaction/financial-account table, not the IIP stock table. Do not use Table 1.14's portfolio IIP asset position of SBD 373m as a transaction flow.

## 4. Material internal sign/presentation conflict — not resolved
- Chapter IV narrative says: “portfolio investment recorded a wider deficit of $38 million” in Q2-2026, compared with deficit of $1 million in Q1-2026.
- Table 1.17 instead displays portfolio financial assets +38 and portfolio financial liabilities nil for Q2-2026.
- The report does not, in the extracted table/narrative context, explain whether the narrative “deficit” refers to a reverse sign convention, net balance, transaction direction or an editorial inconsistency.
- Do not silently choose a sign, flip +38 to -38, or assign a zero liability to IMF L_NIL_T without confirming the CBSI methodology and table semantics. The nil symbol is clear as published, but the crosswalk to IMF's “net incurrence of liabilities” remains unestablished.
- Table 1.17 aggregate financial assets 540 and liabilities 539 with net lending +2 is not a sufficient algebraic proof of portfolio leg sign; other financial-account items and rounding contribute. No inference from aggregate identity is permitted.

## 5. Gate matrix
| Gate | Status |
|---|---|
| SLB in immutable 63-country Q2-2026 both-leg cohort | PASS |
| No prior dedicated SLB Q2 country report found | PASS |
| Official CBSI quarterly BOP source / BPM6 | PASS |
| Latest source period Q2-2026 | PASS |
| Table 1.17 quarterly frequency and SBD million unit | PASS |
| Q2 portfolio financial-asset row | PUBLISHED: +38 SBDm |
| Q2 portfolio financial-liability row | PUBLISHED: nil (“-”) |
| Narrative sign/presentation agreement | BLOCKED / CONFLICT |
| CBSI methodology definition of sign for this table | NOT_ESTABLISHED |
| Exact IMF A_NFA_T and L_NIL_T row values from archived raw panel | NOT_CAPTURED (large panel GitHub fetch returned empty content; no re-query) |
| SBD-to-USD transaction conversion basis | NOT_ESTABLISHED |
| Same-vintage comparison | NOT_DONE |
| SLB national validation | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 6. Next exact action
1. Locate CBSI official methodology/metadata notes for Table 1.17 and portfolio transaction sign convention; specifically resolve narrative “deficit 38” versus Table 1.17 asset +38/liability nil.
2. Retrieve exact archived IMF SLB 2026-Q2 A_NFA_T and L_NIL_T rows from existing raw/panel evidence without a new IMF query. The committed large panel `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv` has blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`; GitHub text fetch returned zero characters, so the exact rows are not currently exposed by that route.
3. Establish official transaction-period SBD/USD conversion method and source vintage before any currency comparison. Do not use a quarter-end IIP exchange rate or infer conversion.
4. Archive the original CBSI PDF bytes and SHA-256 through a supported direct route before treating this as a fully reproducible numeric source capture.
5. Only after sign, period, units, currency and vintage are established, compare the two legs independently within published precision. Otherwise preserve PARTIAL / NOT PASS and advance within fixed cohort.

## 7. Official evidence
- CBSI Balance of Payments statistics page (BPM6; latest 2026-Q2): https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments
- CBSI Quarterly Review — June 2026 (Chapter IV; Table 1.17, pp. 12 and 44; source PDF): https://www.cbsi.com.sb/sites/default/files/2026-10/June%202026%20Qarterly%20Report%20final.pdf
- CBSI Quarterly Reviews index: https://www.cbsi.com.sb/publications/major-reports/quarterly-reviews
- Solomon Islands National Statistics Office BOP page (states CBSI is compiler/disseminator): https://statistics.gov.sb/balance-of-payments/

## 8. Protected invariants
No cohort rebuild, no IMF re-query, no net-to-leg inference, no sign flip, no IIP-stock-as-flow, no inferred FX, no netting, no synthetic data, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Research spend ₹0.
