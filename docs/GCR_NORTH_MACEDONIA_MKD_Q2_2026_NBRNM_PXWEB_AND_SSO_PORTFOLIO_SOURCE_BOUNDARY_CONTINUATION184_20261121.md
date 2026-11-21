# North Macedonia (MKD) Q2-2026 — NBRNM quarterly BOP table and national dual-leg source-boundary audit (Continuation 184)
Date: 2026-11-21 (Asia/Kolkata)

Decision: FIXED 63-COUNTRY COHORT MEMBERSHIP PASS; NO PRIOR DEDICATED MKD NATIONAL-VALIDATION REPORT FOUND IN REPOSITORY; OFFICIAL NBRNM QUARTERLY FINANCIAL-ACCOUNT PXWEB TABLE IDENTIFIED; OFFICIAL SSO BULLETIN 10/2026 EXPOSES Q2 PORTFOLIO NET ONLY; SEPARATE PORTFOLIO ASSET/LIABILITY OBSERVATIONS, RAW API PAYLOAD/HASH AND VINTAGE BRIDGE NOT CAPTURED; MKD PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and duplicate-prevention preflight
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, and immutable cohort evidence before selecting MKD.
- Reused the existing cohort file: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`.
- Cohort SHA-256 retained from prior verified ledger: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- Exact MKD row in the cohort: `MKD,"North Macedonia, Republic of",2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`.
- Archived coverage QA confirms MKD has 46 asset observations and 46 liability observations, both series through 2026-Q2. This is IMF-panel coverage only, not national-source validation.
- Repository tree and GitHub code search for `MKD` / `North Macedonia` returned the fixed cohort and general coverage files but no earlier dedicated MKD national-source report. No cohort rebuild, IMF re-query, or raw panel modification.

## 2. Official NBRNM source identified
- National Bank of the Republic of North Macedonia (NBRNM) Statistical Web Portal, table: “Balance of Payments, Republic of North Macedonia, financial account, by quarters”:
  https://nbstat.nbrm.mk/pxweb/en/Eksterni%20statistiki/Eksterni%20statistiki__Platen%20Bilans__Platen%20bilans%20trimesecni/6_FinansiskaSmetkaTrimesecniEN.px/
- Portal metadata visible in the official table page:
  - Source: National Bank of the Republic of North Macedonia.
  - Matrix: ES-001.
  - Creation date: 23-Sep-2026.
  - Units: millions EUR and millions USD.
  - Quarter dimension: 114 selectable quarter values; the table's quarterly history includes 2026 Q2 in the current published series.
  - Financial-account item dimension: 210 selectable items.
- This is a primary official quarterly financial-account data table and a materially better route than the SSO summary alone. However, the available web-rendered page exposes the variable-picker shell and example labels, not the complete 210-item codebook or selected Q2 observation rows. No API response, XLSX/CSV export bytes, MIME, retrieval timestamp, raw SHA-256, or selected portfolio subcomponent values were captured.
- NBRNM links its BOP Methodological Notes and Revision of Balance of Payment Data documents from this table. Both linked PDFs returned 403 Forbidden in the available retrieval path; their contents are not claimed or inferred.

## 3. Official SSO Bulletin 10/2026 — what it does establish
- Official State Statistical Office (SSO) Bulletin 10/2026 PDF:
  https://www.stat.mk/media/o5ifvzk5/bilten-10-ang.pdf
- Its “Balance of Payments — (annual and quarterly data series)” table is in million US dollars and reports:
  - Portfolio investment, net, 2026 II Q: **+227.7 USD million**.
  - Net acquisition of financial assets, 2026 II Q: **+144.9 USD million** — this is the total financial-account line, not portfolio assets.
  - Net incurrence of liabilities, 2026 II Q: **+431.0 USD million** — this is the total financial-account line, not portfolio liabilities.
- The table marks 2025 and 2026 data provisional. It also describes September 2026 revisions affecting 2025 and selected historical series. This is a revision/vintage warning, not a complete MKD Q2 portfolio vintage history.
- The +227.7 USDm portfolio figure is a net aggregate only. It cannot be decomposed into portfolio A_NFA_T and L_NIL_T. The two adjacent financial-account-wide asset/liability totals must not be mislabelled as portfolio legs. No subtraction, allocation, or back-solving was performed.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Master Ledger / Priority Queue / Historical Registry preflight | PASS |
| No prior dedicated MKD national validation report found in scoped repository inventory | PASS |
| MKD exact row in fixed 63-country cohort | PASS |
| Existing IMF panel has both Q2-2026 legs | PASS (panel coverage only) |
| Official NBRNM quarterly financial-account PxWeb table located | PASS |
| NBRNM source, matrix, creation date, units and dimensions recorded | PASS |
| SSO official Q2-2026 portfolio net reference | PASS (+227.7 USDm; net only) |
| Separate Q2-2026 portfolio asset transaction value | NOT_CAPTURED |
| Separate Q2-2026 portfolio liability transaction value | NOT_CAPTURED |
| Full 210-item codebook / selected observation payload | NOT_CAPTURED |
| Raw official API/export bytes, MIME, retrieval time and SHA-256 | NOT_CAPTURED |
| NBRNM methodology/revision PDFs | BLOCKED (403 via available retrieval path) |
| National↔IMF sign/scale/vintage reconciliation | NOT_DONE |
| MKD national-source validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Rejected substitutes and duplicate prevention
- Do not use the SSO +227.7 USDm net portfolio line as either separate asset or liability.
- Do not use the overall financial-account +144.9 asset and +431.0 liability lines as portfolio-only values.
- Do not use IIP portfolio positions/stocks as BOP transaction flows.
- Do not infer a sign convention, currency conversion, or vintage match from the net figure.
- Do not retry the same inaccessible NBRNM methodology/revision PDF URLs through the same retrieval path.
- Do not repeat the already completed cohort construction, IMF raw-panel acquisition, or unrelated country validations.

## 6. Next exact action
- Resolve the NBRNM PxWeb financial-account table's complete metadata/codebook and select only the Q2-2026 portfolio-investment asset and liability transaction series; retrieve original JSON/CSV/XLSX response bytes through a supported official export/API route and preserve exact URL, response headers/MIME, UTC retrieval timestamp, and SHA-256.
- Confirm the series labels, unit, sign convention, quarter, and revision/vintage before comparing with the already archived IMF Q2-2026 rows.
- If the official table does not expose separate portfolio legs or the export route remains inaccessible, retain MKD PARTIAL / NOT PASS and advance to the next eligible fixed-cohort country after a fresh full historical preflight. No net-to-leg back-solving.

## 7. Protected invariants
₹0; official free sources only. No synthetic data/timestamps, IMF re-query, cohort rebuild, net-to-leg back-solving, stock-as-flow substitution, unsupported sign/scale/FX conversion, or relaxed acceptance. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Aggregate remains NOT_AUTHORIZED.
