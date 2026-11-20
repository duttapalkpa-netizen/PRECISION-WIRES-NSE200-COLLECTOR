# Türkiye TUR — TCMB September-2026 ZIP exact-endpoint access gate (Continuation 118)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The official TCMB Balance of Payments Statistics page exposes the September-2026 data ZIP at the exact URL below. The browser retrieval attempt timed out. No ZIP bytes, archive members, workbook sheets, raw SHA-256, or revision metadata were captured. This confirms the public locator, not successful data capture. TUR remains PARTIAL / NOT PASS; aggregate admission remains NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `8f6c07a3367f03868dbd64b06d3b127e85584ba8`.
- Re-fetched current GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `f96b0285089875bf80a20119c87d9e57e4147af6`.
- Re-opened the queue's existing TUR sections O and P. Prior work already captured Q2 assets USD 5,749m and liabilities USD 9,183m in August/September PDF snapshots; IMF exact values are assets USD 5,749m and liabilities USD 9,270m. Asset matches at displayed precision; liability residual is USD 87m.
- Existing two-snapshot comparison found no Q2 liability revision between the August and September PDF snapshots. The prior work explicitly leaves the September ZIP raw bytes/hash and full revision metadata NOT_INSPECTED.
- No IMF re-query, cohort rebuild, or repeat of the prior monthly aggregation/PDF comparison was performed.

## 2. Official ZIP locator
- Official source page: https://tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Statistics/Balance%2Bof%2BPayments%2Band%2BRelated%2BStatistics/Balance%2Bof%2BPayments%2BStatisticss/
- Page labels the current section “Data - September 2026” and exposes “ZIP Link”.
- Exact resolved URL: https://tcmb.gov.tr/wps/wcm/connect/08454646-62d8-4188-bfbe-1c8c01d83fc4/bop.zip?CACHEID=ROOTWORKSPACE-08454646-62d8-4188-bfbe-1c8c01d83fc4-q7jJcOm&MOD=AJPERES
- Retrieval result: timeout. No raw response body or binary bytes returned. Do not invent byte count, archive contents, revision metadata, or SHA-256.
- The current official September 2026 developments PDF is available as a separate narrative/report surface; its summary table contains Jan–Sep aggregate figures, not a substitute for the raw monthly ZIP revision history.

## 3. Gate status
| Check | Status |
|---|---|
| Official TCMB source page | PASS |
| Exact September-2026 ZIP URL resolved | PASS |
| ZIP binary bytes | NOT_CAPTURED |
| ZIP archive members / workbook sheets | NOT_CAPTURED |
| Raw ZIP SHA-256 / byte count | NOT_CAPTURED |
| Revision metadata / vintage history | NOT_CAPTURED |
| Q2 2026 assets | Existing PDF capture: USD 5,749m |
| Q2 2026 liabilities | Existing PDF capture: USD 9,183m |
| IMF exact Q2 assets/liabilities | Existing receipt: USD 5,749m / USD 9,270m |
| Liability residual | USD 87m; beyond published whole-million rounding |
| Same-vintage bridge | NOT_ESTABLISHED |
| TUR full dual-leg validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 4. Next action
- Do not repeat the same web ZIP fetch after timeout. Obtain the exact ZIP through an actual supported browser/Computer Use or another byte-preserving official route, then archive the raw bytes, retrieval timestamp, byte count, SHA-256, ZIP member list, and relevant monthly workbook tables.
- Inspect whether the official September 2026 ZIP contains Q2 historical revisions and revision/vintage metadata. Compare April–June 2026 asset and liability legs independently with the already archived IMF exact rows; do not attribute the USD 87m residual to revisions without evidence.
- If no browser/byte-preserving capability is available, keep TUR PARTIAL / NOT PASS and advance to the next eligible member in the fixed cohort after checking the immutable roster and existing country reports. No IMF re-query or cohort rebuild.

## 5. Protected constraints
₹0 spend; official free sources only. No synthetic values, no generic FX, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- Official TCMB BOP statistics page: https://tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Statistics/Balance%2Bof%2BPayments%2Band%2BRelated%2BStatistics/Balance%2Bof%2BPayments%2BStatisticss/
- Exact official September-2026 ZIP URL: https://tcmb.gov.tr/wps/wcm/connect/08454646-62d8-4188-bfbe-1c8c01d83fc4/bop.zip?CACHEID=ROOTWORKSPACE-08454646-62d8-4188-bfbe-1c8c01d83fc4-q7jJcOm&MOD=AJPERES
- September-2026 TCMB developments PDF: https://www.tcmb.gov.tr/wps/wcm/connect/4329826e-067d-44b6-8748-620900d91741/BalanceofPayments_September2026.pdf?MOD=AJPERES
