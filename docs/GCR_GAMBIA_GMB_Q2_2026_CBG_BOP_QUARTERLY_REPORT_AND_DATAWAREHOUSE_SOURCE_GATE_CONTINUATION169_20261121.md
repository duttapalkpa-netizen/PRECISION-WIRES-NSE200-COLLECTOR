# The Gambia GMB — Q2-2026 CBG BOP quarterly report and data-warehouse source gate (Continuation 169)
Date: 2026-11-21 (Asia/Kolkata)
Status: FIXED-COHORT MEMBERSHIP PASS; NO PRIOR DEDICATED GMB NATIONAL PORTFOLIO DUAL-LEG REPORT FOUND IN SCOPED REPOSITORY SEARCH; OFFICIAL Q2 REPORT VERIFIED; CURRENT PUBLIC REPORT HAS FINANCIAL-ACCOUNT NET TOTAL ONLY, NOT PORTFOLIO ASSET/LIABILITY LEGS; DATA-WAREHOUSE INTERACTIVE PAYLOAD NOT_EXTRACTED; GMB PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `3b1241c8bf69641eb4f3cdb525325050feaba9fb`.
- Re-fetched Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `8744640182eadbdafa99ffc0161535b1b3bf6010`.
- Re-fetched Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `a2e840d023810c098c00eee222c640f8ed7531f2`.
- Repository search for `GMB Gambia Q2-2026 portfolio investment` and `GMB Gambia BOP Q2 2026 source official` found no dedicated GMB Q2 national portfolio dual-leg report; results were cohort membership only. No duplicate country report found in scoped repository search.
- Reused immutable cohort `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. Exact row: GMB, The Gambia, 2026-Q2, A_NFA_T_PRESENT, L_NIL_T_PRESENT, BOTH_LEGS_PRESENT_IN_IMF_PANEL, NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING, NOT_AUTHORIZED.
- No cohort rebuild, IMF re-query, or new extraction of archived IMF raw rows.

## 2. Official national source evidence
- Central Bank of The Gambia (CBG), Monetary Policy Report August 2026, official PDF: https://www.cbg.gm/downloads-file/a89fbf16-b8fc-11f1-8725-02e599c15748 .
- The report explicitly discusses preliminary Q2-2026 BOP estimates and gives current account deficit US$34.6m; capital account surplus US$26.2m; net financial-account inflow US$95.4m. In the narrative, direct investment inflows US$83.3m, other investment net inflows US$24.1m and net acquisition of reserve assets US$12.0m are identified.
- Appendix Table 2 shows Q2-2026 financial account -95.4 (US$ million); Appendix Table 5 shows current account, capital account and net lending/borrowing, not portfolio investment asset/liability components.
- A full-text search within the official August 2026 report found no “Portfolio investment” row. The report does not expose separate portfolio net acquisition of financial assets and net incurrence of liabilities for Q2-2026.
- IMF DSBB metadata search result states that the CBG Economic Research Department compiles The Gambia's BOP quarterly, using BPM5. This establishes quarterly compilation metadata, not Q2-2026 portfolio dual-leg values or BPM6 equivalence.

## 3. Official data-warehouse route
- CBG official Statistics page: https://www.cbg.gm/statistics-1 .
- It directs users to “CBG DATA WAREHOUSE”: https://gambia.datawarehousepro.com/ (redirects to https://app.datawarehousepro.com/go/cbg).
- The accessible rendering resolves to an interactive application shell with generic editor instructions and CSV upload interface, but no visible catalogue, BOP series identifiers, downloadable data payload, observations, or metadata. No API/export endpoint or workbook bytes were exposed by the page inspection.
- This is an official linked data-warehouse locator but not a successful data retrieval. No credentials or paid access were used.
- CBG Quarterly Bulletins index: https://www.cbg.gm/quarterly-bulletins . The currently accessible page rendering lists bulletin downloads through 2018; it does not expose a Q2-2026 detailed BOP workbook in the retrieved page.
- Historical CBG BOP tables from 2017–2018 include a portfolio-investment net line, but they are historical, not Q2-2026, and do not establish separate transaction legs. They are rejected as current-period evidence.

## 4. Route fingerprint and bounded access result
- Primary route fingerprint: `GMB | Central Bank of The Gambia | https://www.cbg.gm/downloads-file/a89fbf16-b8fc-11f1-8725-02e599c15748 | Monetary Policy Report August 2026 | PDF | Q2-2026 | separate portfolio A_NFA_T/L_NIL_T transactions`.
- Secondary route fingerprint: `GMB | CBG | https://gambia.datawarehousepro.com/ → https://app.datawarehousepro.com/go/cbg | Macroeconomic Data Warehouse interactive application | browser app | Q2-2026 | portfolio transaction series split by assets/liabilities`.
- The PDF route is readable, but its published Q2 table is aggregated at financial-account/net level and omits portfolio investment. The warehouse route resolves only to an app shell in this access path; no dataset export or series payload captured.
- No claim that the national portfolio legs are zero. Absence from the report is NOT evidence of zero transactions.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| GMB membership in immutable Q2-2026 both-leg cohort | PASS |
| Prior dedicated GMB national dual-leg report absent in scoped repo search | PASS (scoped search only) |
| Official CBG Q2-2026 BOP report located and inspected | PASS |
| Quarterly compilation metadata | PASS (IMF DSBB metadata) |
| Q2-2026 national portfolio asset transaction leg | NOT_CAPTURED |
| Q2-2026 national portfolio liability transaction leg | NOT_CAPTURED |
| Portfolio instrument row in current Q2 report | NOT_PRESENT |
| Data-warehouse catalogue/API/export payload | NOT_EXTRACTED |
| Sign / unit / classification / revision vintage for portfolio legs | NOT_ESTABLISHED |
| Numeric comparison to archived IMF exact rows | NOT_DONE |
| GMB full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Rejected list
- Do not use Q2 financial-account net total (-US$95.4m) as a portfolio investment leg or as a substitute for two legs.
- Do not back-solve assets/liabilities from net totals, FDI, other investment, reserves or the overall BOP identity.
- Do not infer zero portfolio transactions from omission in the MPC report.
- Do not substitute old 2017/2018 quarterly BOP tables, H1/annual totals, IIP stocks or IMF-only rows for Q2-2026 national transaction evidence.
- Do not repeat the same data-warehouse app-shell inspection absent a genuinely new public export/API payload or distinct supported access capability.

## 7. Next exact action
1. Seek a distinct public CBG BOP quarterly statistical table or documented data-warehouse export/API payload that exposes Q2-2026 portfolio investment separately for assets and liabilities.
2. Require exact series names, period header, instrument/functional-category classification, units, sign convention, publication/revision vintage, raw bytes and SHA-256.
3. If no distinct supported route exists, close GMB as PARTIAL / NOT PASS and advance to the next unvalidated fixed-cohort member after full preflight.
4. Only after national legs are captured, reuse archived IMF Q2 rows and reconcile each leg separately.

## 8. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or relaxation of acceptance criteria. Research spend ₹0. UNKNOWN is never PASS.
