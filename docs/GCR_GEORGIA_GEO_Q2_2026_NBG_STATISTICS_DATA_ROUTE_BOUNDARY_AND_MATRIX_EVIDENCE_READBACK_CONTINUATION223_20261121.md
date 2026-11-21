# Georgia (GEO) Q2-2026 — NBG statistics-data route boundary and matrix evidence read-back
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 223
Status: MATRIX EVIDENCE LINK CORRECTED; NEW OFFICIAL STATISTICS-DATA LANDING ROUTE VERIFIED; Q2 PORTFOLIO TRANSACTION LEGS NOT_CAPTURED; GEO PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate prevention
Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country cohort, national validation matrix, and controlling GEO C154 report before selection. The fixed cohort includes GEO. C154's Q2 release/BPM5 boundary, stale NSDP Q3/21 display and existing IMF rows were reused; none were recalculated or re-requested. HUN C138/C139 was also inspected and excluded because the monthly portfolio-flow route was already bounded/closed. No IMF re-query or cohort rebuild.

## 2. New official NBG route evidence
- Official NBG Statistics landing page: https://nbg.gov.ge/en/page/statistics
- Official NBG Statistics Data page: https://nbg.gov.ge/en/statistics/statistics-data
- The landing page states NBG produces financial/external-sector statistics and disseminates data as static Excel tables and interactive dashboards, with external-sector among the statistical categories.
- The Statistics Data page exposes a title/code search interface in the rendered page. It does not expose, in the inspected accessible content, a BOP table identifier, a downloadable Q2-2026 workbook URL, an API schema, or a data response.
- The official NSDP route remains a different page and its visible BOP observations are stale at Q3/21; this was already documented in C154 and was not treated as Q2 data.
- A third-party Fiscal.ge page indexes a NBG-origin BPM6 workbook with coverage labelled 2000–2025; because this is a third-party mirror and does not cover Q2 2026, it is not admitted as a national Q2 source or substitute.

## 3. Result and access boundary
The new NBG statistics-data landing/search route is verified as a distinct official discovery surface, but the current rendered retrieval does not expose an executable BOP dataset locator or payload. No endpoint, workbook URL, series code, or API request has been guessed. No national Q2 portfolio asset/liability values, raw bytes, retrieval receipt, byte count or SHA-256 were captured. C154 remains the controlling evidence for national Q2 release and stale NSDP boundaries.

## 4. Matrix correction
The GEO matrix row already correctly preserved SOURCE_FOUND, national data capture NO, asset/liability NOT_CAPTURED, vintage UNKNOWN, FULL_PASS NO and aggregate NOT_AUTHORIZED. Its evidence_ref was stale (NO_DEDICATED_REPORT_REF_IN_BASELINE) despite C154. Correct only the descriptive note and evidence_ref to:
- note: Official NBG Q2-2026 release is BPM5 and does not publish separate portfolio legs in accessible text; NBG statistics-data page confirms static Excel/interactive dashboards but no Q2 BOP export locator or payload captured; NSDP visible observations stale Q3/21.
- evidence_ref: GCR_GEORGIA_GEO_Q2_2026_NBG_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION154_20261121
Preserve all gate/status fields.

## 5. Acceptance
| Gate | Status |
|---|---|
| Fixed cohort membership / C154 reused | PASS |
| Distinct official NBG Statistics Data discovery surface verified | PASS |
| Q2 national portfolio asset/liability rows captured | NO |
| GEO full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Protected invariants
₹0; official sources only for national evidence. No IMF re-query, cohort rebuild, synthetic data, fabricated timestamps, guessed API/export, stock-flow substitution, net-to-leg back-solving, sign/scale inference, tolerance widening or production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
