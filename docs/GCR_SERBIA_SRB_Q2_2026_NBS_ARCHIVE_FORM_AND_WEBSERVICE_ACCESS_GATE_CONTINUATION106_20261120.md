# Serbia SRB Q2-2026 — NBS archive form and web-service access gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: 106
Decision: **Official NBS archive UI is confirmed on the Balance of Payments page, with two archive forms (monthly BPM6 and detailed BPM6), each exposing Select + five Input controls + Show. However, the web text interface does not expose form names, option values, submit action, or the generated download endpoint; no executable browser/form inspection or binary retrieval capability was available in this pass. NBS separately documents a web-service system that requires a completed certified application and NBS-issued username/password/licence code. This is an authenticated service route, not a public anonymous endpoint and not used. Raw XLS and May revision remain NOT_CAPTURED.**

## 1. Continuity preflight
Re-fetched Master Ledger blob SHA b3d818fa8ad5d5ea3a2c5c2efad82cdd7c222edc, GCR Priority Queue blob SHA aa260f77f4a282db6246ebdd6ecc147a1b2489eb, and Continuation 105 blob SHA 916a9d07c1e15f36a24bfe3d28b11c7958e6c90a. PASS work excluded: NBS sign/transaction FX methodology, IMF code semantics, exact IMF rows and Q2 aggregation.

## 2. NBS archive UI inspection
- Official English NBS Balance of Payments page displays two archive blocks:
  1) “Balance of payments - monthly (BPM6)”
  2) “Balance of payments - monthly, details (BPM6)”
- Each block renders a Select control, five Input controls, and a Show button in the web-extracted page.
- The extracted web page exposes no form field names, selectable values, form action, query parameters, generated URL, or linked downloadable output for those archive controls. The page text alone cannot establish an underlying endpoint or reconstruct a valid request.
- The same page lists direct September-2026 monthly and detailed XLS files. These remain the only verified current-vintage downloadable artifacts from the public page; earlier retrieval failed on unsupported application/vnd.ms-excel content type.
- Do not invent an endpoint or guess query parameters. Do not claim that the archive form is a REST API.

## 3. NBS web-service access gate
- The official NBS “NBS web-service system” page states an application form must be completed and certified and sent to NBS IT Department, 17 Nemanjina Street, 11000 Belgrade.
- It states NBS opens a user account based on the application and sends username, password and licence code to the contact address in the application.
- This confirms the web-service route is gated by NBS account issuance. No application was submitted, no external contact made, and no credentials sought or used. User constraints of no external contact / ₹0 preserved.
- This service page does not establish that the archive UI requires the same credentials; that relationship is UNKNOWN.

## 4. Updated gate matrix
- Public archive UI exists: PASS.
- Archive UI field schema / generated endpoint: NOT_EXPOSED in inspected web text.
- NBS web-service account requirements: DOCUMENTED; account not available / route not used.
- Anonymous binary XLS retrieval: BLOCKED by unsupported content type.
- September 2026 workbook bytes/sheets/values/hash: NOT_CAPTURED.
- May 2026 later-vintage separate asset/liability values: NOT_CAPTURED / NOT_DONE.
- USD separate BOP legs: NOT_LOCATED.
- USD/EUR transaction-weighted bridge: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact actions
1. Use an actual browser/form-inspection capability to inspect the archive form DOM, selected options, field names, submit method and generated download URL; do not infer these from text extraction.
2. If the archive form returns an XLS, capture the raw binary through a byte-preserving download path and record response headers, retrieval timestamp, byte count and SHA-256 before parsing.
3. Parse the workbook locally; identify the monthly and detailed tables and exact May 2026 asset/liability cells. Preserve source vintage separately.
4. Do not use the NBS authenticated web-service route without explicit user authorization and account access; no application or external contact.
5. Keep USD/EUR comparison blocked unless an official USD series or transaction-level weighted conversion data is actually obtained.

## 6. Official sources
- NBS Balance of Payments page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/index.html
- NBS web-service system: https://www.nbs.rs/en/drugi-nivo-navigacije/servisi/sistem-veb-servisa-NBS/

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
