# Sri Lanka LKA Q2-2026 — Table 2.10 series cross-check and revision-risk gate (Continuation 176)
Date: 2026-11-21 (Asia/Kolkata)
Decision: SECONDARY CATALOGUE CROSS-CHECK CONFIRMS THE 30-SEP-2026 CBSL TABLE 2.10 SERIES VALUES AT Q2-2026 AND REVEALS MATERIAL HISTORICAL DISCREPANCIES BETWEEN TABLE 2.10 AND AN OLDER BOP MIRROR SERIES IN 2021; NO PRIMARY CBSL BYTES OR RAW CSV/JSON CAPTURED; SAME-VINTAGE BRIDGE STILL NOT_ESTABLISHED; LKA REMAINS STRONG DUAL-LEG RECONCILIATION / PROVISIONAL, NOT FINAL PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight
- Re-fetched Master Continuity Ledger (blob SHA `13826d2fca44c0684c3e3963ae3503f1ce8d14a8`), GCR Priority Queue (`f7f94aa954f0c66e418c8c0e9308cb37c89436f7`), Historical Task Registry (`65f3396d795d41479f899c2062d85c3f0c77a26c`), C175 (`e1d4c34c20e64fc87567499d777e511463cac4a2`), C174 (`36363f9a1e85cc1922ee96005f5f310b1bb6c67f`) and immutable cohort (`31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- LKA exact cohort row remains present; no cohort rebuild and no IMF re-query. No repeat of the identical blocked CBSL XLSX download.
- C174 national Table 7 Q2 values remain assets +26 USD mn and liabilities -351 USD mn, provisional; archived IMF values independently round to the same figures.

## 2. Independent secondary catalogue — source attribution and exact series
Macro Lab is explicitly not affiliated with CBSL or any government body; it describes its data as reproduced from agency publications. It is used here only as a secondary discovery/cross-check layer, not as primary evidence.
- Portfolio Investment Assets series: https://macrolab.lk/data/series/LK.EXT.BOP_Q.ASSETS_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS.Q/
  - Q2-2026 = +25.68 USD mn.
  - Page identifies CBSL as data source; quarterly BPM6 Table 2.10; source release “Balance of Payments (BPM6 Basis) - Quarterly” dated 30-Sep-2026; 58 observations.
  - Page lines 112–148 identify CBSL source, table 2.10, 30-Sep-2026 release and series metadata.
- Portfolio Investment Liabilities series: https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS.Q/
  - Q2-2026 = -350.9 USD mn.
  - Same source, table and release marker.
- Portfolio Investment Liabilities — Equity and investment fund shares: https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFO_S_EQUITY_AND_INVESTMENT_FUND_SHARES.Q/
  - Q2-2026 = -38.90 USD mn.
  - Same source and release marker.
- Portfolio Investment Liabilities — Debt securities: https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS_DEBT_SECURITIES.Q/
  - Q2-2026 = -312.0 USD mn.
- Portfolio Investment Assets — Debt securities: https://macrolab.lk/data/series/LK.EXT.BOP_Q.ASSETS_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS_DEBT_SECURITIES.Q/
  - Q2-2026 = +25.68 USD mn.
- These are secondary pages reproducing data attributed to CBSL. They corroborate the Q2 values but do not replace official CBSL workbook bytes.

## 3. Q2 dual-leg and component reconciliation
| Series | Q2-2026 USD mn | Source layer |
|---|---:|---|
| Portfolio Investment Assets — total | +25.68 | Secondary catalogue, attributed to CBSL Table 2.10 |
| Portfolio Investment Assets — debt securities | +25.68 | Secondary catalogue, attributed to CBSL Table 2.10 |
| Portfolio Investment Liabilities — total | -350.9 | Secondary catalogue, attributed to CBSL Table 2.10 |
| Portfolio Investment Liabilities — equity & investment fund shares | -38.90 | Secondary catalogue, attributed to CBSL Table 2.10 |
| Portfolio Investment Liabilities — debt securities | -312.0 | Secondary catalogue, attributed to CBSL Table 2.10 |
- Liability components sum to -350.90 USD mn, consistent with reported total -350.9 USD mn at displayed precision.
- Treasury Table 7 reports assets +26 and liabilities -351 USD mn, with liabilities components -39 and -312, provisional. Secondary series values agree at rounding.
- No net-to-leg back-solving, IIP stock substitution or unsupported conversion used.

## 4. Revision-risk finding — important
The Macro Lab liabilities page documents three historical discrepancies between the newer Table 2.10 series and an older BOP mirror series, explicitly associating them with a CBSL revision year:
- 2021 Q1: -742.213 vs -92.73 USD mn; difference -649.483 USD mn.
- 2021 Q2: +2.025 vs +3.24 USD mn; difference -1.215 USD mn.
- 2021 Q3: -794.206 vs -1,156.54 USD mn; difference +362.334 USD mn.
- The page labels these as table2.10 vs older EXT.BOP mirror discrepancies during a CBSL revision year. This is secondary catalogue QA evidence, not an independently inspected primary CBSL revision log.
- Implication: do not use an older BOP mirror series as a substitute for Table 2.10; version identity and revision vintage must be preserved at source level. This reinforces the C175 same-vintage blocker.

## 5. Download affordance / limitations
- The series pages expose CSV (“Period, value and source status flag”) and JSON (“values with metadata and source”) download affordances.
- Clicking the JSON affordance in this web session resolved back to the HTML series page, not a raw JSON payload. Therefore no machine-readable export bytes, headers, content length, local file, or SHA-256 were captured.
- Macro Lab states it is independent and not affiliated with CBSL or government. This catalogue cannot be promoted to official national raw-source evidence.
- The official CBSL XLSX remains inaccessible through the previously tested direct route (HTTP 403); do not repeat it absent a genuinely different supported route.

## 6. Acceptance status
| Gate | Status |
|---|---|
| Fixed cohort membership and continuity preflight | PASS |
| Q2 assets/liabilities corroborated by secondary series attributed to CBSL Table 2.10 | PASS — secondary corroboration only |
| Liability instrument subcomponents sum to total at displayed precision | PASS — secondary corroboration only |
| Treasury Table 7 provisional values match at rounding | PASS — already established C174 |
| Historical mirror-series revision discrepancies identified | PASS — secondary QA evidence |
| Primary CBSL workbook bytes / hash | NOT_CAPTURED |
| Machine-readable secondary CSV/JSON raw bytes / hash | NOT_CAPTURED |
| Exact Q2-2026 same-vintage bridge | NOT_ESTABLISHED |
| LKA final national-source validation | NOT_PASS / PENDING |
| Aggregate authorization | NOT_AUTHORIZED |

## 7. Rejected list
- Macro Lab is not primary national evidence and cannot satisfy primary-source acceptance.
- Older BOP mirror series is rejected as substitute for Table 2.10 because the catalogue itself reports 2021 discrepancies.
- IIP stocks are excluded.
- The displayed JSON/CSV affordance is not treated as downloaded raw evidence; click redirected to HTML.
- No revision date inferred from page crawl date; no third-party SHA accepted as verified.
- No paid API, synthetic data, annual/H1 substitution, net-to-leg back-solving or production change.

## 8. Next exact action
1. Seek a genuinely different official access route to the exact 30-Sep-2026 CBSL Table 2.10 workbook or official CSV/SDDS export.
2. If a machine-readable secondary export can be obtained, archive it separately as SECONDARY_ONLY with source URL, timestamp, bytes and SHA-256; never substitute it for official raw source.
3. Find official CBSL release/vintage metadata showing whether Table 2.10 was revised between 30-Sep-2026 and the 12-Nov-2026 Treasury report.
4. If no distinct official route appears, close LKA retrieval as PARTIAL and advance to the next unvalidated fixed-cohort country after full preflight.
5. Aggregate remains NOT_AUTHORIZED until all country acceptance requirements are met.

## 9. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or acceptance relaxation. Research spend ₹0. UNKNOWN is never PASS.
