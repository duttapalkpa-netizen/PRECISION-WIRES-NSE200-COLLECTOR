# GCR Continuation 231 — Rwanda RWA BNR WebDash alternate-route and Q2 source-boundary audit
Date: 2026-11-25 (Asia/Kolkata)
Status: ALTERNATE OFFICIAL PORTAL SURFACE IDENTIFIED; Q2-2026 PORTFOLIO DUAL-LEG DATA NOT_CAPTURED; RWA PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Mandatory continuity and Library preflight
- Re-fetched the GitHub Master Continuity & Acceptance Ledger, GCR Master Priority Queue, 63-country Historical Task Registry, RWA source-gate report (C97/C130), NPL route closures (C58/C94/C130), SLV source-family report (C100/C131), and fixed 63-country matrix.
- Library semantic search surfaced and the full Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and `Global_Capital_Rotation_Overlay_Acceptance_Gap_Matrix_page27.csv` were read. These preserve historic project constraints and GCR-01..GCR-13 gap definitions; they do not override newer GitHub ledger/queue evidence.
- Existing PASS work was not repeated: no IMF query, no cohort rebuild, no fiscal-year recalculation, no repeat of the C97/C130 JS-shell probe or the already inspected H1/annual figures.

## 2. NPL handoff closure check — no new supported official route
- Current NRB External Sector page still lists monthly BOP BPM6 and the known September-2026 official XLSX locator:
  https://www.nrb.org.np/database-on-nepalese-economy/external-sector/
  https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx
- Current NRB NSDP page separately lists BOP Browse Data and Download in SDMX:
  https://www.nrb.org.np/nsdp/
- Following the current NSDP BOP SDMX link resolves to the already known stale XML:
  https://www.nrb.org.np/contents/uploads/2024/05/NEPAL_BOP_2024_Q1.xml
  Retrieval returns unsupported application/xml (400) through this reader. This is the same stale locator recorded in C58/C94/C130, not a new Q2 route.
- Decision: no new official NPL API/export locator found; do not repeat the known XLSX or stale XML requests. NPL remains PARTIAL / BLOCKED.

## 3. RWA — distinct BNR WebDash route fingerprint
- Reopened BNR External Sector Statistics:
  https://www.bnr.rw/esstatistics
  Official search-indexed text continues to list a “Balance of Payment” item dated 30-Jun-2026 and describes external-sector statistics as BPM6-based. Direct page rendering remains a JavaScript application shell; the June item’s exact downloadable file URL/bytes remain unresolved.
- Inspected a distinct official BNR subdomain data surface:
  https://webdash.bnr.rw/
  The page itself returns no readable text through the current retrieval bridge. Official-domain search indexing exposes its “Balance Of Payment” table with USD-million values for annual years 2019–2023 and a combined portfolio investment row. This is an alternate source surface, but the indexed content does not expose Q2-2026, separate asset and liability transaction legs, a downloadable dataset/API contract, or a dated observation vintage.
- Rechecked BNR October-2026 Monetary Policy and Financial Stability Statement, Table 12:
  https://www.bnr.rw/documents/MPFSS_Report_October_2026.pdf
  It reports 2026H1 portfolio investment net +USD14m only; it does not provide separate H1 asset/liability legs or standalone Q2. It cannot be differenced into Q2 or used to back-solve either leg.
- Rechecked BNR August-2026 Monetary Policy Report:
  https://www.bnr.rw/documents/Monetary_Policy_Report_August_2026.pdf
  Its Table 2 is a summary BOP table and omits Q2 portfolio transaction legs. Do not use its financial-account, direct-investment, government-borrowing or reserve rows as proxies.
- Existing BNR Annual Report 2024-25 Appendix 14 fiscal-year portfolio asset/liability figures remain historical methodology/crosswalk context only. They are not calendar-quarter observations and are not reprocessed here.

## 4. Acceptance matrix
| Gate | Result |
|---|---|
| Fixed 63-country RWA membership / both IMF legs present | PASS (existing cohort only) |
| Existing official BNR BPM6 source discovery | PASS (C97) |
| New official WebDash surface identified | PASS (locator only) |
| WebDash Q2-2026 separate portfolio asset/liability values | NOT_CAPTURED |
| WebDash exact data/API/export contract and raw bytes | NOT_CAPTURED |
| BNR June-30 portal item exact URL/bytes | NOT_RESOLVED |
| October 2026 H1 net-only +USD14m | CONTEXT ONLY; NOT Q2 / NOT dual-leg |
| Annual fiscal-year asset/liability rows | CONTEXT ONLY; NOT Q2 |
| Q2 asset and liability national observations | NOT_CAPTURED |
| Sign/concept crosswalk and same-vintage bridge | NOT_ESTABLISHED |
| Numeric dual-leg comparison | NOT_DONE |
| RWA national validation | PARTIAL / NOT PASS |
| 63-country aggregate / production admission | NOT_AUTHORIZED |

## 5. Matrix and next-action decision
- The fixed-cohort matrix RWA row remains BLOCKED with both national legs NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO and aggregate NOT_AUTHORIZED. Only its evidence reference is updated to this new route-boundary report; no gate is promoted.
- C100/C131 already closed the SLV BCR quarterly database timeout and rejected stock/annual substitutes; that work is not repeated.
- Next fixed-cohort follow-up should resume at SLB's unresolved official transaction-FX conversion-method boundary from C132, after a fresh route-history preflight. Do not infer the CBSI rate from a generic quarterly FX series or convert candidate figures without an official transaction conversion rule.
- NPL may reopen only on a genuinely distinct NRB official BOP API/export or XLSX-capable byte route. RWA may reopen only if BNR exposes the June-30 item through an exact downloadable official URL/API/export with Q2 separate transaction legs and metadata.

## 6. Protected invariants
₹0; official/free sources only; no IMF re-query, cohort rebuild, fabricated values/timestamps, fiscal-year proration, net-to-leg back-solving, stocks-as-flows, net-only Q2 inference, generic FX conversion, paid data, external contact, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
