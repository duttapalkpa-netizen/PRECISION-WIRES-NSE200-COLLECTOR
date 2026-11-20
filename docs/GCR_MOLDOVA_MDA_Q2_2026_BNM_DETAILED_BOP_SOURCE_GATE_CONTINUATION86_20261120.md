# GCR Moldova (MDA) Q2-2026 — BNM detailed BOP source gate
Date: 2026-11-20 (Asia/Kolkata)
Decision: **Official Q2 publication and detailed interactive BPM6 source route identified; Q2 net-only aggregate is NOT a dual-leg observation; exact asset/liability values NOT_EXTRACTED; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and selection
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue and relevant prior country reports before selection.
- Reused the immutable 63-country 2026-Q2 both-leg cohort at docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). MDA (Moldova) is a member with both IMF panel legs present. No cohort rebuild, no IMF re-query.
- Repository search found no dedicated MDA Q2-2026 national portfolio dual-leg reconciliation report. MDA selected as the next executable official-source gate; no previous PASS country task repeated.

## 2. Official Q2 release boundary
- National Bank of Moldova (BNM) official release “Balance of payments of the Republic of Moldova in Quarter II, 2026 (preliminary data)”, dated 30-Sep-2026.
- Release links three distinct BPM6 presentations: standard, detailed and analytic; also links the quarterly tables/charts workbook 02_Tables_Charts_2026_q2.xlsx, statistical bulletin workbook and annex workbook.
- The release's graphical main-aggregate display reports portfolio investment EUR -24.9 million as a single net component. It does not display separate portfolio asset and liability transaction legs. Do not treat -24.9 as either leg, do not back-solve the legs and do not compare this net-only figure as a substitute for A_NFA_T/L_NIL_T.
- The page's headline financial-account net figure and current/capital account aggregates are not portfolio legs.

## 3. Detailed BOP interactive database route
Official BNM Reports Generator page:
https://www.bnm.md/bdi/pages/reports/dbp/DBP16.xhtml
- The official BNM page describes the interactive database as allowing statistical-series selection and export.
- The report title is “Balance of Payments of the Republic of Moldova (BPM6), detailed presentation” (Romanian UI label: “Balanţa de plăţi ... în prezentare desfășurată”).
- Visible controls in the captured page include indicator selection, parameter selection, start/end years 2009–2026, periodicity options (annual, 9 months, 6 months, quarterly), quarter selectors I–IV, currency options EUR/USD, and “Export” / “Generate” controls.
- Page also exposes “Statistical series” and “Metadata” tabs. These are a promising official route for exact indicator definitions and series selection.
- Current read-only page extraction does not execute the controls, choose 2026/Q2, generate a report, or return export bytes. Therefore this audit confirms the user-facing route and controls only; it does not claim that the Q2 detailed table was generated or that a successful XLS/CSV export was captured.
- Q2 release XLSX locator: https://www.bnm.md/files/02_Tables_Charts_2026_q2.xlsx. Browser retrieval in this environment did not provide workbook contents/raw bytes; no workbook hash or parsed row is claimed.

## 4. Method and interpretation boundary
- BNM's official methodology landing page is linked directly from the detailed report generator. Official methodology standards describe portfolio investment as a financial-account category and distinguish assets (claims on non-residents) from liabilities (obligations to non-residents); instrument scope includes equity securities and debt securities.
- The Q2 press-release net aggregate cannot establish the two gross directional legs. Any generated detailed report must preserve its native sign convention, unit, currency, quarterly period, preliminary status and release vintage.
- EUR and USD output options are separate native export choices. Do not convert one to the other without a dated official conversion series and a documented convention.
- Existing IMF panel values are not copied into this source-gate report; exact row comparison is deferred until national detailed legs and metadata are captured.

## 5. Acceptance
| Gate | Status |
|---|---|
| MDA is in fixed 63-country Q2-2026 both-leg cohort | PASS |
| Official BNM Q2-2026 release identified (30-Sep-2026) | PASS |
| Official quarterly net portfolio aggregate visible (-EUR 24.9m) | PASS — net only |
| Separate portfolio asset and liability legs in release graphic | NOT_REPORTED |
| Detailed BPM6 interactive report route identified | PASS |
| Quarterly period and EUR/USD selectors visible | PASS |
| Export/Generate controls visible | PASS |
| Q2 detailed report generated | NOT_DONE |
| Exact indicator names/series IDs and metadata captured | NOT_DONE |
| Raw export bytes + headers + retrieval UTC + SHA-256 | NOT_DONE |
| Asset/liability sign, unit, scope and revision vintage | NOT_ESTABLISHED |
| IMF national dual-leg comparison | NOT_DONE |
| MDA national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |
| Production integration | NOT_AUTHORIZED |

## 6. Next exact action
Using a supported interactive browser, operate only the visible official BNM Reports Generator controls: select detailed BPM6 BOP; choose 2026 start/end, quarterly periodicity, quarter II, and a native currency; inspect Metadata and Statistical Series; generate/export once. Preserve untouched output bytes, URL, headers, retrieval UTC and SHA-256 before parsing. Identify separate Portfolio Investment Assets and Liabilities, their sign/credit-debit semantics, units and preliminary/revision status. If interactive execution/export is unavailable, request the user to attach the official BNM Q2 XLSX or generated export; do not retry the same unsupported XLSX download path or infer legs from net -24.9.
- Official sources:
  * BNM Q2 release: https://www.bnm.md/en/content/balance-payments-republic-moldova-quarter-ii-2026-preliminary-data
  * BNM detailed report generator: https://www.bnm.md/bdi/pages/reports/dbp/DBP16.xhtml
  * BNM compilation methodology: https://bnm.md/ro/content/conturile-internationale-metodologia-de-compilare-si-baza-informationala
  * BNM Q2 tables/charts workbook locator: https://www.bnm.md/files/02_Tables_Charts_2026_q2.xlsx
- Protected invariants unchanged: ₹0, official/free sources only, no synthetic data, no fabricated timestamps, no net-only substitution, no unsupported FX conversion, no netting of legs, no production changes, fixed 63-country cohort unchanged. UNKNOWN is never PASS.
