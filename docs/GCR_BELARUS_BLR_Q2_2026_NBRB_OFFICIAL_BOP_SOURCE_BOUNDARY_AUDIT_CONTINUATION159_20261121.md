# GCR Q2-2026 — Belarus (BLR) National Bank official BOP source-boundary audit
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 7
Continuation sequence: 159
Status: FIXED-COHORT / IMF RAW ROW PRESENCE PASS; OFFICIAL NBRB BPM6 AND QUARTERLY DISSEMINATION METADATA PASS; Q2 NATIONAL DUAL-LEG VALUES/RAW BYTES NOT_CAPTURED; BLR PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and selection
- Re-fetched Master Continuity Ledger, GCR Priority Queue and immutable 63-country Q2-2026 both-legs cohort before selection. BLR is a member; both IMF raw Q2 rows are present. Repository search found no dedicated BLR Q2-2026 national dual-leg audit. Previous BOL (Continuation 158) and BLZ (157) reports were not repeated.
- No IMF re-query, cohort rebuild, paid source or production-code modification.

## 2. Official national source and methodology
- National Bank of the Republic of Belarus (NBRB) official metadata identifies BOP as an NBRB responsibility and BPM6 methodology: https://www.nb-rb.by/statistics/sstandard/metadata/balance.pdf
- Metadata states quarterly BOP dissemination, standard and analytical presentations, and separate financial-account net acquisition of assets and net incurrence of liabilities by functional category. It explicitly defines portfolio investment as a functional category. The financial account is recorded net separately for each asset/liability; plus means increase, minus means decrease. This is NOT a gross credit/debit presentation.
- Official English NBRB methodology states quarterly compilation, BPM6, USD and BYN publication, and that financial-account assets represent resident investment abroad while liabilities represent nonresident investment in Belarus: https://www.nb-rb.by/engl/statistics/BalPay/Methodology/Methodology6.pdf
- Official metadata says quarterly BOP is released around 75 days after quarter-end and first-published observations are preliminary, with revisions possible. This makes vintage capture essential.
- The official NBRB live BOP page https://www.nbrb.by/engl/statistics/balpay timed out in browser retrieval; Russian page https://www.nbrb.by/statistics/balpay was inaccessible. The public bulletin catalogue did not yield a verified Q2-2026 portfolio dual-leg table in this audit. No unsupported URL guessing or fabricated workbook retrieval was used.

## 3. Reused archived IMF raw rows (no conversion)
- Asset file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv; exact BLR 2026-Q2 row: A_NFA_T, P_F, USD, Q, OBS_VALUE=6414501.08999999, SCALE=6.
- Liability file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv; exact BLR 2026-Q2 row: L_NIL_T, P_F, USD, Q, OBS_VALUE=-325487157.39, SCALE=6.
- Immutable raw-panel Git blob SHAs remain asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1. These are Git blob identifiers, not represented as raw-file SHA-256.
- Values and SCALE are transcribed exactly; no scale conversion, sign normalization or comparison was performed.

## 4. Acceptance matrix
| Gate | Result |
|---|---|
| Fixed 63-country cohort membership | PASS |
| IMF asset and liability Q2 rows present | PASS |
| NBRB official BPM6 methodology | PASS |
| Quarterly BOP and revision policy metadata | PASS |
| Q2-2026 national portfolio asset transaction value | NOT_CAPTURED |
| Q2-2026 national portfolio liability transaction value | NOT_CAPTURED |
| National raw bytes, retrieval receipt and SHA-256 | NOT_CAPTURED |
| Q2 observation vintage and exact item/scale/sign bridge | NOT_ESTABLISHED |
| Numeric comparison | NOT_DONE |
| BLR national validation | PARTIAL / NOT PASS |
| Cross-country aggregate authorization | NOT_AUTHORIZED |

## 5. Decision and next bounded action
- BLR remains PARTIAL. Metadata confirms a suitable official quarterly BPM6 dissemination framework, but this audit did not capture the actual Q2 national portfolio transaction values or underlying source bytes. Do not substitute IIP positions, capital-flow net totals, annual data or adjacent-quarter values.
- Next action: retrieve the NBRB Q2-2026 quarterly BOP bulletin or live data export through a supported official raw-byte route; capture the separate portfolio asset and liability net transaction rows, publication/revision vintage, unit, item labels, retrieval timestamp and SHA-256. If no supported route yields bytes, retain PARTIAL and advance to the next eligible cohort member.
- ₹0 spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is never PASS.
