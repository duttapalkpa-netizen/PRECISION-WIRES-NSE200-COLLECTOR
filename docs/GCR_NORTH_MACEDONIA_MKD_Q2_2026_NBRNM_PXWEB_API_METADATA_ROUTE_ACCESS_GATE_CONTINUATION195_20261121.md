# North Macedonia (MKD) Q2-2026 — NBRNM PxWeb API metadata-route access gate (Continuation 195)
Date: 2026-11-21 (Asia/Kolkata)
Decision: A distinct PxWeb v1 metadata API route was constructed from the verified official ES-001 table locator and tested; the retrieval surface reports the exact URL inaccessible. No API JSON, item codebook, selected cells, raw payload, or SHA-256 captured. MKD remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-fetched current main Master Continuity Ledger, GCR Master Priority Queue and Historical Task Registry.
- Re-fetched the complete scoped MKD history. Repository inventory contains only the dedicated MKD national-source audit C184; no later MKD continuation was found.
- C184's precise open action: resolve the 210-item codebook and Q2-2026 portfolio asset/liability observations from NBRNM's official quarterly financial-account PxWeb table through an official API/export route.
- Reused the immutable 63-country cohort; no cohort rebuild, IMF re-query, or raw panel modification.
- Rejected completed PASS work: fixed cohort membership, existing IMF dual-leg panel coverage, official ES-001 table identity, table source/unit/dimensions, and SSO portfolio net reference. No repetition of SSO net extraction or blocked methodology/revision PDF requests.

## 2. Existing official source facts retained from C184
- NBRNM official table: https://nbstat.nbrm.mk/pxweb/en/Eksterni%20statistiki/Eksterni%20statistiki__Platen%20Bilans__Platen%20bilans%20trimesecni/6_FinansiskaSmetkaTrimesecniEN.px/
- Table: Balance of Payments, Republic of North Macedonia, financial account, by quarters; matrix ES-001; creation date 23-Sep-2026; source NBRNM; units millions EUR and millions USD; 210 item values and 114 quarter values, including Q2-2026.
- Existing SSO Bulletin 10/2026 net portfolio investment +USD227.7m is net-only and cannot be decomposed into the two required legs. Financial-account-wide assets/liabilities are not portfolio-only legs.
- Existing IMF panel coverage is available for both Q2 legs; no new IMF access was performed.

## 3. Distinct PxWeb v1 metadata API route test
- Constructed the standard PxWeb v1 metadata path from the exact official table path (including the .px table filename):
- https://nbstat.nbrm.mk/PxWeb/api/v1/en/Eksterni%20statistiki/Eksterni%20statistiki__Platen%20Bilans__Platen%20bilans%20trimesecni/6_FinansiskaSmetkaTrimesecniEN.px
- The web retrieval surface returned URL is not accessible for this exact API path. No HTTP status/body/headers were available. A direct container download attempt was also unavailable because the URL had not been accepted as a viewed resource by that transfer tool; no bytes were created.
- This is a distinct API-path test, not evidence that NBRNM has no API or that data are absent. No guessed query payload, item code, or observation value is recorded.
- API route result: BLOCKED / NOT_CAPTURED. Do not repeat this exact URL through the same retrieval surfaces unless the access capability changes.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Ledger / Queue / Registry / full MKD history preflight | PASS |
| C184 official ES-001 table identity and metadata | PASS (reused) |
| Fixed cohort and archived IMF dual-leg presence | PASS (reused) |
| PxWeb v1 metadata API URL constructed from exact table path | PASS — route syntax only |
| API metadata JSON / response body / headers | BLOCKED / NOT_CAPTURED |
| Complete 210-item codebook / portfolio A-L item identifiers | NOT_CAPTURED |
| Q2-2026 separate portfolio asset observation | NOT_CAPTURED |
| Q2-2026 separate portfolio liability observation | NOT_CAPTURED |
| Raw national export bytes / MIME / UTC receipt / SHA-256 | NOT_CAPTURED |
| Sign, scale, observation vintage and IMF bridge | NOT_ESTABLISHED |
| MKD national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Decision and next action
- C184's specific API metadata route has now been tested once and is inaccessible through the current retrieval surface. Do not repeat it through the same surface.
- Preserve MKD PARTIAL. Do not use net-to-leg back-solving, IIP stocks, or financial-account-wide totals.
- Advance to the next eligible fixed-cohort member only after full historical report and route-fingerprint preflight; prioritize a genuinely distinct official data route with separate quarterly portfolio asset/liability rows.
- No IMF GET, no cohort rebuild, no production changes, ₹0 spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.