# GCR Ukraine (UKR) Q2-2026 — NBU IIP transaction-to-BOP financial-account methodology bridge
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 257
Decision: OFFICIAL NBU METHODOLOGY EXPLICITLY CONFIRMS THAT IIP TRANSACTION COLUMN REPRESENTS FINANCIAL-ACCOUNT TRANSACTIONS AND IIP FINANCIAL-COMPONENT ROWS CORRESPOND TO BOP FINANCIAL-ACCOUNT STRUCTURE. EXISTING Q2 PORTFOLIO DUAL-LEG NUMERIC CHECKS CAN BE ACCEPTED AS BOP FINANCIAL-ACCOUNT TRANSACTION COMPONENTS. SAME-VINTAGE / Q2 REVISION IDENTITY REMAINS NOT_ESTABLISHED; UKR PARTIAL / NOT PASS.

## 1. Mandatory preflight and selection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and immutable 63-country matrix before selection. Read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and controlling UKR C120/C134/C135 report history.
- The fixed-cohort matrix showed UKR DATA_CAPTURED, asset REVIEW, liability REVIEW, vintage PENDING, aggregate NOT_AUTHORIZED. C134 already contains separate Q2 transaction-column values and archived IMF exact rows; repeated extraction/arithmetic was rejected.
- Selected the unresolved formal IIP transaction-column ↔ BOP financial-account definition/mapping gate. No IMF re-query, cohort rebuild, repeated NBU IIP PDF extraction, stale BOP PDF retry, or production workflow dispatch.

## 2. New official NBU methodology evidence
Official NBU document: “External Sector Statistics of Ukraine: Methodology and Data Sources (according to BPM6)”
URL: https://p4.bank.gov.ua/admin_uploads/article/BoP_methodological_notes_en.pdf
- Lines 12–16: NBU compiles and publishes external-sector statistics under BPM6.
- Lines 189–202: financial-account assets and liabilities are recorded as net acquisition of financial assets and net incurrence of liabilities; plus means increase, minus means decrease; financial-account balance is assets minus liabilities.
- Lines 1030–1031: IIP data sources are the same as those used to compile the BOP financial account.
- Lines 1037–1041: IIP is an integrated statement containing beginning/end stocks and flows resulting from BOP transactions plus other changes.
- Lines 1068–1076: IIP table rows are the basic financial components of external assets/liabilities and correspond to the BOP financial-account structure; column 3 is the result from financial-account transactions; separate columns capture exchange-rate, price and other adjustments.
- This directly validates the use of the IIP “Transactions (8−4)” column as financial-account transaction evidence, while keeping stocks and non-transaction adjustments excluded. It is not a claim that a separate standalone Q2 BOP PDF was retrieved.

## 3. Reuse of existing Q2 observations — no recalculation
Controlling report C134:
`docs/GCR_UKRAINE_UKR_Q2_2026_NBU_IIP_TRANSACTION_BRIDGE_AND_IMF_DUAL_LEG_CHECK_CONTINUATION134_20261121.md`
- NBU Q2-2026 IIP, USDm, last updated 23-Sep-2026:
  - Portfolio investment assets, transaction column: +159 USDm.
  - Portfolio investment liabilities, transaction column: +34 USDm.
  - Opening/closing positions and all valuation/other-change columns are excluded.
- Existing archived IMF exact-key rows (19-Nov-2026 snapshot; reused, not re-fetched):
  - A_NFA_T OBS_VALUE=159000000, SCALE=6, USD, quarterly, 2026-Q2.
  - L_NIL_T OBS_VALUE=34000000, SCALE=6, USD, quarterly, 2026-Q2.
- C134's country-specific displayed comparisons: assets 159 vs 159 USDm, residual 0.000; liabilities 34 vs 34 USDm, residual 0.000 at NBU whole-million precision. Both leg numeric checks remain PASS.
- The official NBU methodology now supplies the missing semantic bridge: these IIP transaction-column observations are financial-account transactions and the row structure corresponds to the BOP financial-account structure. Do not treat them as IIP closing stocks.

## 4. Independent vintage boundary retained
Official NBU changes notice:
https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf
- Last updated 23-Sep-2026.
- The notice lists BOP revisions through Q1-2026 and does not list Q2-2026 portfolio observations/revisions. The absence of Q2 in this notice is not proof that Q2 was unrevised or that the 19-Nov IMF transport snapshot shares the same source vintage as the NBU IIP Q2 publication.
- NBU methodology lines 300–306 states previous BOP periods may be revised quarterly; lines 322–323 states IIP can be revised within two years with comments about changes.
- NBU IIP file C134 identifies the Q2 document as last updated 23-Sep-2026. No later Q2 observation-specific revision ID, timestamp, versioned snapshot or IMF↔NBU vintage bridge was found in this bounded task.
- Therefore vintage remains PENDING / NOT_ESTABLISHED. No same-vintage promotion.

## 5. Acceptance result
| Gate | Result |
|---|---|
| UKR fixed 63-country Q2 cohort | PASS (reused) |
| NBU BPM6 compiler and financial-account sign concepts | PASS |
| IIP data-source / BOP financial-account relationship | PASS |
| IIP table row-to-BOP financial-account structure mapping | PASS |
| IIP transaction column explicitly represents financial-account transactions | PASS |
| Q2 portfolio assets +159 USDm / liabilities +34 USDm | PASS (C134 evidence reused) |
| Archived IMF exact-key dual-leg displayed comparison | PASS (C134 evidence reused; no re-query) |
| Formal IIP-transaction-to-BOP financial-account semantic bridge | PASS |
| Q2 same-vintage / observation-specific revision identity | PENDING / NOT_ESTABLISHED |
| UKR full national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Matrix change and next action
- Update UKR asset_gate and liability_gate from REVIEW to PASS, and the corresponding status_ASSET_PASS/status_LIABILITY_PASS flags to YES, because C134's separate numeric comparisons were already PASS and C257 now closes the formal transaction-to-financial-account methodology mapping.
- Keep current_stage DATA_CAPTURED, source gate FOUND, data_capture YES, vintage PENDING, full_pass NO, aggregate NOT_AUTHORIZED. Keep overall status DATA_CAPTURED / PARTIAL; do not mark full country PASS.
- Next exact action: inspect only a new official NBU Q2 revision/version notice or later official IIP/BOP release that explicitly identifies Q2 portfolio transaction revisions, and compare its observation-specific vintage with the archived IMF receipt. Do not repeat the IIP extraction, stale BOP PDF, or IMF query.

## 7. Protected invariants
₹0; free official sources only; no IMF re-query/cohort rebuild; no synthetic values, stock-as-flow, net-to-leg inference, unsupported sign/scale conversion, or fabricated timestamps. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.
