# Kosovo KOS — Q2-2026 BQK official ROW transaction-matrix source gate (Continuation 168)
Date: 2026-11-21 (Asia/Kolkata)
Status: FIXED-COHORT MEMBERSHIP PASS; PRIOR DEDICATED KOS REPORT NOT FOUND IN REPOSITORY SEARCH; OFFICIAL BQK FINANCIAL-ACCOUNT TRANSACTION MATRIX LOCATOR / METHODOLOGY PASS; RAW XLS NOT_CAPTURED (HTTP 403); Q2 PORTFOLIO DUAL-LEG EXPOSURE NOT_VERIFIED; KOS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `60c3be224768c3e3afd4b227bca7fa5f3625fdc3`.
- Re-fetched current GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `83e0b62e779aea432e7ead785a0e0fc66725c92d`.
- Re-fetched Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `634e7e235b1b2899aa8d5d1c4d6a716eabfb04d3`.
- Repository search for `KOS Kosovo Q2-2026 BOP portfolio` returned no dedicated KOS national portfolio dual-leg report. No prior KOS task is claimed as completed.
- Reused immutable Q2-2026 both-leg cohort at `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. Exact row: KOS, Kosovo, 2026-Q2, A_NFA_T_PRESENT, L_NIL_T_PRESENT, BOTH_LEGS_PRESENT_IN_IMF_PANEL, national validation pending, aggregate NOT_AUTHORIZED.
- No cohort rebuild, IMF re-query, or extraction of already archived IMF values was performed.

## 2. New official route fingerprint
- Country: KOS — Kosovo.
- Authority: Central Bank of the Republic of Kosovo (BQK / CBK).
- New dataset family: External Sector Statistics → Financial Accounts Statistics → Rest of the World (S.2) Matrix — Transactions.
- Exact official locator: https://bqk-kos.org/wp-content/uploads/2024/09/ROW%20Matrix%20%E2%80%93%20Transactions.xls
- Official time-series index: https://bqk-kos.org/statistikat/serite-kohore/?lang=en
- Period shown by the official index: Q2 2026.
- Separate BOP route locator also visible: https://bqk-kos.org/repository/docs/time_series/30%20Financial%20account.xls (monthly financial-account series, latest listed August 2026).
- Route fingerprint: `KOS | BQK | /wp-content/uploads/2024/09/ROW Matrix – Transactions.xls | ROW Matrix (S.2) | XLS download | Q2 2026 | transaction rows by financial instrument and assets/liabilities`.
- This is a new source family for this project; it is not the previously rejected Honduras WOPI/XLSX route or the same BQK monthly financial-account XLS locator.

## 3. Official source and methodology evidence
- BQK Time Series index places “ROW Matrix – Transactions” under REST OF THE WORLD (S.2), with period Q2 2026 and a Download link.
- BQK Financial Accounts Statistics description says financial-account statistics record flows of financial assets and liabilities; they disclose current transactions by financial instruments for relations with non-residents. It states that BQK publishes external-sector financial-account statistics by financial instrument for both assets and liabilities, on a from-whom-to-whom basis.
- BQK describes the methodology as aligned with ESA 2010 / SNA 2008 and IMF BPM6.
- These facts justify investigating the ROW transaction matrix as a distinct flow source. They do NOT yet prove that the downloaded table contains a separately labelled portfolio-investment asset and liability pair for Q2-2026. That requires workbook inspection.

## 4. Byte-retrieval tests and result
- Browser click on the official ROW Matrix — Transactions download link resolved to the exact XLS URL but returned HTTP 403 Forbidden. No workbook bytes, response headers, byte count, workbook sheets, rows, series keys, values, or SHA-256 were captured.
- Browser click on the official monthly “Financial account” XLS locator returned HTTP 400 Unsupported content-type (application/vnd.ms-excel).
- A separate container download attempt for the monthly Financial account XLS failed. This is a failed retrieval attempt, not evidence that the file is empty or absent.
- Do not retry these identical URLs through the same failed retrieval path. Reopen only if a genuinely new supported XLS byte-transfer capability or a distinct official export endpoint is available.
- Q2-2026 International Investment Portfolio under IIP is a stock/position product and is explicitly NOT_ADMITTED as a substitute for Q2 transaction flows.
- Do not use financial-account net totals, net-only portfolio balance, annual/H1 values, IIP stocks, or IMF-only observations as national dual-leg validation.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| KOS membership in immutable 63-country Q2-2026 both-leg cohort | PASS |
| Prior dedicated KOS report absent in scoped repository search | PASS (search scope recorded; not exhaustive claim beyond repository search) |
| Official BQK ROW Matrix — Transactions Q2-2026 locator | PASS |
| BQK financial-account transaction / instrument / assets-liabilities methodology | PASS |
| Actual XLS bytes / sheets / raw hash | NOT_CAPTURED |
| Q2 portfolio asset and liability labels in workbook | NOT_VERIFIED |
| Q2 separate national portfolio asset/liability values | NOT_CAPTURED |
| Sign / unit / scope / revision vintage | NOT_ESTABLISHED |
| Numeric comparison to archived IMF exact rows | NOT_DONE |
| KOS full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Next exact action
1. Obtain the exact official ROW Matrix — Transactions XLS bytes using a genuinely supported public byte-transfer capability; preserve URL, retrieval timestamp, HTTP status, byte count, content type, and SHA-256.
2. Inspect workbook sheet names, period headers, S.2 counterpart sector, instrument classification and transaction/stock distinction.
3. Confirm that portfolio investment is separately exposed for both net acquisition of financial assets and net incurrence of liabilities for Q2-2026; do not infer or back-solve.
4. Only after raw workbook verification, reuse the already archived IMF KOS Q2 rows and compare the two legs independently with source-supported signs, units, scale and vintage.
5. If no new supported transfer capability exists, retain KOS PARTIAL / NOT PASS and advance to another unvalidated fixed-cohort member after the same full preflight.

## 7. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or relaxation of acceptance criteria. Research spend ₹0. UNKNOWN is never PASS.
