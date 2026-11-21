# Guinea GIN — Q2-2026 BCRG official BOP source-boundary and reporting-route audit (Continuation 170)
Date: 2026-11-21 (Asia/Kolkata)
Status: FIXED-COHORT MEMBERSHIP PASS; NO PRIOR DEDICATED GIN Q2 NATIONAL PORTFOLIO DUAL-LEG REPORT FOUND IN SCOPED REPOSITORY SEARCH; OFFICIAL BCRG Q2-2026 MACRO UPDATE CONFIRMS EXTERNAL-SECTOR CONTEXT; PUBLICLY INSPECTABLE Q2 SOURCE DOES NOT EXPOSE PORTFOLIO ASSET/LIABILITY LEGS; BCRG STATISTICS PAGE RESOLVES TO DYNAMIC/EMPTY CONTENT; GIN PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `1d4e26b9aace8fa7252b68556e10a2fd029263bc`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `eb89a9120ab1f0777786d9915b23819478e85b0d`.
- Re-fetched Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `7daefb0a2fc1b8c2c2a456d901d4398a76efa83b`.
- Re-fetched prior Continuation 169 GMB report: `docs/GCR_GAMBIA_GMB_Q2_2026_CBG_BOP_QUARTERLY_REPORT_AND_DATAWAREHOUSE_SOURCE_GATE_CONTINUATION169_20261121.md`, blob SHA `d7cd36142243c7079634162eedbf31a964b9b1f9`. GMB remains PARTIAL; its route is closed. No repeat GMB task.
- Reused immutable cohort `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. Exact row: GIN, Guinea, 2026-Q2, A_NFA_T_PRESENT, L_NIL_T_PRESENT, BOTH_LEGS_PRESENT_IN_IMF_PANEL, NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING, NOT_AUTHORIZED.
- Repository search `GIN Guinea Q2-2026 BOP portfolio assets liabilities`, `Guinea BCRG Q2 2026 balance of payments portfolio investment`, and `GIN Guinea Q2-2026 national source` returned no dedicated GIN Q2 national portfolio dual-leg report in the scoped repository. No cohort rebuild, IMF re-query or new IMF raw extraction.

## 2. Official BCRG Q2-2026 evidence located
- BCRG 2026 official publication index: https://www.bcrg-guinee.org/2026/ . It lists the 22nd ordinary Monetary Policy Committee meeting dated 22-Sep-2026.
- Official 22nd MPC page: https://www.bcrg-guinee.org/22eme-reunion-ordinaire-du-comite-de-politique-monetaire-de-la-republique-de-guinee/ . Page has a “Télécharger” label but the rendered public page did not expose a retrievable document URL in the inspected content.
- The BCRG 18-Sep-2026 Q2 update is also summarized by a dated secondary report; that summary attributes to BCRG a Q2 current-account surplus USD671.1m. This is macro context only, not national portfolio transaction-leg evidence and is not used as validation.
- Official BCRG statistics index: https://www.bcrg-guinee.org/satistiques/ .
- Official Balance des paiements page: https://www.bcrg-guinee.org/satistiques/balance-des-paiements/ . The rendered page exposes its title but no visible dataset/table/download links or series observations. Treat it as a locator only; no API endpoint or data bytes extracted.

## 3. Prior official BCRG reporting format — source boundary
- Inspected official BCRG “Rapport sur la Politique Monétaire du premier trimestre 2025” (June 2025): https://www.bcrg-guinee.org/wp-content/uploads/2025/07/Rapport-sur-la-Politique-Monetaire-T12025-Vf-08-07-25_-docx-Obs-DG.pdf .
- Table 11 (pages around 48–49) and Appendix Table 17 show “Investissements de portefeuille” as one net category only. It does not split portfolio into net acquisition of financial assets and net incurrence of liabilities.
- Table 11 reports quarterly financial-account and functional-category balances in USD million. Example historical portfolio net values are 2024 Q1 0.21, Q2 24.32, Q3 -7.24, Q4 -10.72, and 2025 Q1 provisional -7.31 USDm. These are historical net balances only and MUST NOT be used as Q2-2026 values or dual legs.
- The same report narrative describes financial-account net liabilities/inflows and says portfolio investment contributed positively; again it does not provide the two separate transaction legs.
- This establishes a source-format limitation in that historical report vintage only; it does not prove that the 2026 detailed BOP dataset lacks a separate split. Q2-2026 workbook/API remains NOT_CAPTURED.

## 4. Route fingerprint and retrieval result
- Primary reporting route fingerprint: `GIN | BCRG | https://www.bcrg-guinee.org/22eme-reunion-ordinaire-du-comite-de-politique-monetaire-de-la-republique-de-guinee/ | 22nd MPC report/download (Sep 2026) | page + hidden/unresolved download | Q2-2026 | portfolio assets and liabilities transactions`.
- Secondary dataset route fingerprint: `GIN | BCRG | https://www.bcrg-guinee.org/satistiques/balance-des-paiements/ | BOP statistics dynamic page | browser page | Q2-2026 | portfolio asset/liability series`.
- Page inspection did not expose a retrievable download/API for the September 2026 MPC report or the Q2 BOP statistics page. No raw Q2 workbook/PDF bytes, response metadata, observations, series IDs, SHA-256, portfolio leg labels, or values captured.
- Do not infer that the Q2 data are absent from BCRG's internal/public data systems merely because the rendered pages do not expose them. Status is NOT_CAPTURED / NOT_EXTRACTED, not zero.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| GIN membership in immutable 63-country Q2-2026 both-leg cohort | PASS |
| Prior dedicated GIN Q2 national dual-leg report absent in scoped repo search | PASS (scoped search only) |
| Official BCRG 2026 publication index and September MPC page located | PASS |
| Official BCRG BOP statistics page located | PASS |
| Historical official BCRG report inspected for table structure | PASS |
| Q2-2026 national portfolio asset transaction leg | NOT_CAPTURED |
| Q2-2026 national portfolio liability transaction leg | NOT_CAPTURED |
| September 2026 MPC report downloadable bytes / SHA-256 | NOT_CAPTURED |
| Current BOP statistics API/export / raw data | NOT_EXTRACTED |
| Q2 sign, unit, instrument classification and revision vintage | NOT_ESTABLISHED |
| Comparison to archived IMF exact rows | NOT_DONE |
| GIN full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Rejected list
- Historical 2024–2025 portfolio net balances are not Q2-2026 data.
- A single net portfolio row cannot be substituted for separate asset/liability transactions or back-solved.
- Q2 current-account surplus is not evidence of portfolio investment flows.
- IIP positions/stocks, annual or adjacent-quarter values, IMF-only rows and financial-account totals are not admitted as national dual-leg evidence.
- Do not repeatedly inspect the same static BOP page or MPC page unless a distinct document URL, public API/export, or new data payload is found.

## 7. Next exact action
1. Identify the actual downloadable file URL behind the official 22nd MPC page “Télécharger” element or a distinct BCRG official BOP series/export endpoint.
2. If a new locator is found, preserve exact URL, retrieval timestamp, HTTP status, content type, byte count and SHA-256 before parsing.
3. Inspect Q2-2026 portfolio series for separate asset and liability transaction legs, classification, sign, unit, and revision vintage.
4. If the official source continues to expose only net portfolio data, retain GIN PARTIAL / NOT PASS and advance to another unvalidated cohort member after a fresh ledger/queue/report preflight.
5. Only after national legs are captured, reuse archived IMF rows and reconcile both legs independently.

## 8. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or relaxation of acceptance criteria. Research spend ₹0. UNKNOWN is never PASS.
