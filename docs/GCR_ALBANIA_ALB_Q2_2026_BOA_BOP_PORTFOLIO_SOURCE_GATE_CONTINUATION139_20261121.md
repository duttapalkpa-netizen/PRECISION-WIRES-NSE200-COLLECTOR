# Albania (ALB) Q2-2026 — Bank of Albania portfolio BOP source gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 139
Status: Fixed-cohort and official quarterly BOP route PASS; separate portfolio asset/liability taxonomy PASS; exact Q2 numeric extraction NOT_DONE; national sign/scale/vintage crosswalk NOT_ESTABLISHED; ALB PARTIAL / NOT PASS.

## 1. Continuity preflight and selection
- Reopened current Master Continuity Ledger (blob SHA b90cd6d7937e9f5a4ecb7c9b179fd4365089a41a), Master Priority Queue (blob SHA dcc0f758b6b5bfd4bdf1cb7b571123e521d451bc), immutable 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), HUN C138 report and existing archived IMF raw panels.
- HUN's MNB monthly portfolio route was bounded and closed: MNB says monthly time series are not published and its monthly page contains selected estimated components, not monthly portfolio legs. No further identical MNB monthly route retry.
- ALB is in the immutable 63-country Q2 both-leg cohort and no dedicated ALB Q2-2026 national portfolio report was present in the repository tree during preflight. Selected as the next candidate with a distinct official central-bank quarterly BOP route exposing portfolio assets and liabilities.
- No cohort rebuild and no IMF re-query.

## 2. Official Bank of Albania Q2-2026 BOP publication gate
- Official Statistics Calendar 2026 lists “Balance of payments and gross external debt — Q II 2026” for 10-Sep-2026.
- Official Bank of Albania Time Series — Balance of Payments page identifies the source as quarterly, Bank of Albania, and reports data update 10-Sep-2026.
- Official page: https://www.bankofalbania.org/Statistics/External_sector_statistics/Balance_of_Payments/Time_Series-Balance_of_Payments.html
- The table metadata describes values in millions of euros and quarterly basis. It exposes Financial account / Portfolio investment with distinct parent rows and component hierarchy:
  - C.2 Portfolio investment
  - C.2.A Assets, including C.2.A.1 equity and investment fund shares and C.2.A.2 debt instruments
  - C.2.L Liabilities, including C.2.L.1 equity and investment fund shares and C.2.L.2 debt instruments
- This is a national BOP transaction table, not an IIP stock table. Bank of Albania's external-sector overview distinguishes BOP transactions from IIP stocks and states that Albania's BOP is compiled under BPM6.
- Numeric rows for 2026-Q2 were not exposed in the browser-readable page response; the page's interactive controls/table data could not be captured as raw rows in this bounded task. Do not infer or invent values from table taxonomy.

## 3. Existing archived IMF exact ALB Q2 rows — reused
- Existing raw IMF panel files and hashes:
  - Asset panel blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8.
  - Liability panel blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Exact archived rows:
  - A_NFA_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=181700604.8387097, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
  - L_NIL_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=145011618.7096774, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Values and attributes remain raw and unchanged. No new IMF request, no rescaling or sign transformation.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| ALB fixed 63-country cohort membership | PASS |
| Official Bank of Albania Q2 BOP publication calendar | PASS |
| Official quarterly BOP table/data update 10-Sep-2026 | PASS |
| Quarterly EUR million presentation | PASS (table metadata) |
| Portfolio asset/liability hierarchy | PASS (C.2.A / C.2.L) |
| Equity/debt subcomponents | PASS (taxonomy only) |
| Exact Q2-2026 national asset/liability observations | NOT_DONE |
| Raw national export/bytes/retrieval receipt/SHA-256 | NOT_DONE |
| Country-specific sign and aggregation crosswalk | NOT_ESTABLISHED |
| Existing IMF exact Q2 raw rows | PASS (reused) |
| Numeric dual-leg reconciliation | NOT_DONE |
| Same-vintage alignment | NOT_ESTABLISHED |
| Full ALB national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Exact next actions
1. Retrieve the Bank of Albania interactive quarterly BOP table's machine-readable export or underlying official dataset response for Q2-2026; preserve exact raw bytes, response metadata, retrieval UTC and SHA-256.
2. Extract both C.2.A and C.2.L parent totals and their equity/debt child rows; determine whether parent totals are directly reported or must be derived from the children. Never double-count parent and child rows.
3. Capture the official sign convention and verify whether the source uses assets-minus-liabilities and whether the two legs correspond to IMF A_NFA_T and L_NIL_T.
4. Compare separately with the archived IMF raw observations, preserving original USD raw values and any admitted EUR conversion/tolerance method.
5. Seek an exact publication-vintage/revision bridge. If unavailable, retain PARTIAL / NOT PASS and advance.
6. No IMF re-query, no cohort rebuild.

## 6. Protected invariants
₹0; free official sources only. No synthetic data, no fabricated values/timestamps, no IIP stocks as BOP flows, no net-to-leg back-solving, no unsupported FX/sign/scale transform, no repeated IMF requests. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
