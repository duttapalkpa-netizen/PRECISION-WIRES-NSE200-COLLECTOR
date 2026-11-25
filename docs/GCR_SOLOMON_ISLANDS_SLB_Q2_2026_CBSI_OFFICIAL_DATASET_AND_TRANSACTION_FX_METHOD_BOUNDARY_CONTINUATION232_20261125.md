# GCR Continuation 232 — Solomon Islands SLB CBSI official dataset locator and transaction-FX method boundary
Date: 2026-11-25 (Asia/Kolkata)
Decision: OFFICIAL Q2 BOP DATASET LOCATOR + BPM6/FREQUENCY/UNIT METADATA DISCOVERED; XLSX RAW BYTES NOT_CAPTURED; CBSI TRANSACTION-FX CONVERSION METHOD NOT_ESTABLISHED; SLB PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Mandatory preflight / duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Priority Queue, 63-country Historical Task Registry, fixed 63-country matrix, C99 SLB sign-conflict report, C128 batch handoff containing C132, C231 RWA handoff and Library Mother File 1–53 plus GCR Acceptance Gap Matrix.
- C132 work reused: CBSI Table 1.17 Q2 portfolio asset +38 SBDm and liability nil; existing IMF raw rows and blob SHAs; provisional 8.08 SBD/USD plausibility arithmetic. No IMF query, cohort rebuild, sign re-interpretation, or repeat of existing numeric arithmetic.
- Existing accepted evidence is not promoted or recalculated.

## 2. New official CBSI Balance of Payments route
- Official CBSI Balance of Payments page:
  https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments
- The page defines BOP as transactions between residents and non-residents over a period; says the series covers current, capital and financial accounts quarterly and annually; explicitly says BPM6; presents BOP/IIP in SB$ millions; and identifies latest BOP data as 2026-Q2.
- Its Download link resolves to this exact official workbook:
  https://www.cbsi.com.sb/sites/default/files/2026-09/Balance-of-Payment-Statistics-2006-2026-Q2.xlsx
- Retrieval attempt through the available web reader returned HTTP 400 / unsupported XLSX content-type. A direct byte-download attempt also failed. Consequently no original XLSX bytes, workbook sheets, workbook row values, HTTP response headers, retrieval receipt, byte count or SHA-256 are claimed.
- This is a distinct official Q2 dataset locator not captured in C99/C132; it improves route discovery, but is not raw-data capture or a validated dual-leg comparison.

## 3. FX methodology boundary — new evidence does not close the gap
- CBSI Quarterly Review June 2026, Chapter IV, reports the quarterly-average SBD/USD rate as SBD 8.08 per USD for Q2 2026. The same report's Table 1.17 is in SBD million and reports Q2 portfolio financial assets +38 and portfolio financial liabilities nil.
- The Quarterly Review's general note says dash means nil, data are subject to periodic revision, and its Table 1.17 footnote states BPM6 statistics include reserve assets and IMF Program. The report does not state that the quarterly-average 8.08 rate is the compiler's conversion rate for portfolio transaction flows; it does not specify transaction-date, daily average, monthly average, quarterly average, or other source-specific conversion rule for the portfolio rows.
- CBSI's official “Today's Exchange Rates” page says the Bank calculates SBD daily against USD as intervention currency and publishes rates around 9:00am except Solomon Islands public/bank holidays. This is an official exchange-rate publication policy, not proof that the same daily series is used to convert BOP transactions.
- CBSI's official BOP page confirms BPM6 and SBD-million presentation, but no linked compilation methodology note or FX conversion convention was exposed in the inspected page.
- The IMF 2026 Article IV exchange-rate-arrangement description concerns the SBD currency basket/peg, not the CBSI BOP compiler's transaction conversion rule. It cannot fill the source-specific method gap.
- Therefore 8.08 remains a quarterly-average contextual rate only. Do not use it to admit an FX conversion or numeric PASS.

## 4. Existing C132 diagnostic retained unchanged
- CBSI Q2 Table 1.17: portfolio assets +38 SBDm; liabilities nil.
- Existing IMF archive exact Q2 rows: A_NFA_T OBS_VALUE 4675384.136569459, SCALE=6, USD; L_NIL_T OBS_VALUE 0, SCALE=6, USD. Existing raw blob SHAs remain asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8, liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Prior diagnostic 38/8.08 = 4.702970297 USDm vs candidate IMF display 4.675384137 USDm; residual -0.027586160 USDm, within SBD table rounding ±0.061881188 USDm. This remains plausibility-only; it is not re-run, not a conversion PASS and not an admitted /1e6 scale rule for SLB.
- Conceptual narrative sign reconciliation remains unchanged: positive asset acquisition contributes to net lending (assets minus liabilities); a “portfolio deficit” phrase can be the reverse net-inflow perspective. CBSI has not explicitly defined that narrative convention. Do not flip Table 1.17 sign.

## 5. Gate decision
| Gate | Result |
|---|---|
| Official CBSI Q2-2026 BOP page / BPM6 / quarterly series metadata | PASS (discovery only) |
| Exact official Q2 workbook locator | PASS (locator only) |
| Workbook original bytes / sheets / hash | NOT_CAPTURED |
| Q2 Table 1.17 portfolio asset +38 SBDm / liability nil | Existing PDF evidence retained; not recalculated |
| Quarterly average SBD/USD 8.08 | PASS as published FX context only |
| CBSI BOP transaction-specific FX conversion method | NOT_ESTABLISHED |
| SLB-specific IMF SCALE/display bridge | NOT_ESTABLISHED |
| Matched-vintage dual-leg numeric comparison | NOT_DONE / NOT PASS |
| SLB national validation | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 6. Next exact action / handoff
- SLB method task is closed at a documented source boundary: the official current-Q2 workbook exists at an exact locator, but raw XLSX bytes cannot be retrieved through the available reader; the public evidence does not state the BOP transaction FX conversion rule.
- Do not retry the same XLSX URL through the same unsupported retrieval path; do not use 8.08 quarterly average as if CBSI declared it the transaction rate; do not contact CBSI without explicit user authorization.
- Continue to the next unresolved fixed-cohort item after the already audited SLV and existing SRB source-gate reports: inspect SRB's open same-vintage/revision bridge only after reading C101/C103/C104/C109/C112 and the current queue/matrix; do not repeat its accepted monthly dual-leg arithmetic or sign/FX work.
- If CBSI later publishes a dated official BOP compilation-method note or an accessible original Q2 workbook through a distinct supported route, reopen SLB against that evidence.

## 7. Protected invariants
₹0; official/free sources only; no IMF re-query, cohort rebuild, synthetic data, fabricated metadata, generic FX substitution, sign flip, net-to-leg inference, stock-as-flow, paid source, external contact, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
