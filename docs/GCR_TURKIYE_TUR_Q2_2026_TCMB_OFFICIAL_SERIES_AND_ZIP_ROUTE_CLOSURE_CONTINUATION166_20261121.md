# Türkiye TUR Q2-2026 — official series and ZIP route closure
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 14
Continuation sequence: 166
Decision: NO NEW Q2 DUAL-LEG EVIDENCE CAPTURED; OFFICIAL MONTHLY SERIES/EVDS SURFACE CONFIRMED BUT DOES NOT ITSELF PROVIDE A VERIFIED Q2 TRANSACTION EXTRACT; SEPTEMBER ZIP ROUTE REMAINS UNAVAILABLE THROUGH TESTED FETCH; TUR PARTIAL / NOT PASS; ADVANCE TO NEXT FIXED-COHORT MEMBER NPL.

## 1. Continuity preflight
- Re-fetched Master Continuity Ledger, GCR Priority Queue, POL Part-13 report, TUR reconciliation report and exact prior TCMB September ZIP access-gate report.
- Reused existing TCMB Q2 PDF snapshot calculations and IMF raw receipt. No duplicate Q2 monthly aggregation, no repeated August/September PDF comparison, no IMF re-query and no cohort rebuild.
- POL official USD-table search performed with official NBP-domain queries; no matched Q2 USD dual-leg result surfaced. Existing PLN observations retained; no FX inference. POL handoff condition therefore met; advance in fixed queue.

## 2. Official TCMB publication architecture rechecked
- Official TCMB Balance of Payments Statistics page says Türkiye BOP is issued monthly, compiled under BPM6, and time-series data are available through EVDS. The page exposes separate “Balance of Payments Developments”, “Data” ZIP/PDF, metadata and revision-policy resources.
- Official September 2026 developments PDF Table 2 is denominated in million USD and provides the current month (September), Jan–September cumulative columns and 12-month columns. It displays portfolio assets and portfolio liabilities as separate rows. These are not Q2-only values.
- This publication architecture is useful for source discovery, but the September summary table alone cannot supply the April–June transaction rows or exact September ZIP revision metadata.

## 3. Q2 values and existing discrepancy — reused, not re-derived
| Leg | TCMB Q2 monthly PDF sum | Existing IMF Q2 | Difference |
|---|---:|---:|---:|
| Portfolio assets | +5,749 USDm | +5,749 USDm | 0 |
| Portfolio liabilities | +9,183 USDm | +9,270 USDm | +87 USDm |
- Prior August and September TCMB PDF snapshots showed identical April/May/June rows. That limited comparison did not establish full revision history or same-vintage equivalence.
- USD 87m liability residual remains beyond whole-million display rounding; no tolerance widening, netting, imputation or revision attribution.

## 4. ZIP retrieval gate and decision
- Prior Continuation 118 resolved the exact official September-2026 ZIP URL from TCMB's own statistics page; fetch timed out. No binary bytes, archive members, workbook sheets, response headers, byte count, revision metadata or SHA-256 were captured.
- Current official page recheck confirms the data/EVDS publication architecture, but does not yield a new byte-preserving route. Do not retry the same timed-out ZIP endpoint or claim a new capture.
- Official TCMB page and September report are useful evidence of monthly frequency and separate portfolio asset/liability publication, but do not resolve the USD 87m residual or vintage bridge.
- TUR remains: asset leg PASS at displayed precision; liability leg REVIEW / NOT PASS; full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 5. Next country handoff
- Advance to NPL (Nepal), the next eligible fixed-cohort member already prioritized in the earlier BCRP/PER source-boundary audit. Before NPL extraction, re-fetch its prior report/ledger/queue and avoid the already-failed NRB XLSX and stale NSDP/SDMX routes.
- Seek only a genuinely supported official NRB workbook/API export route; verify separate Q2 portfolio asset and liability transaction rows, Apr–Jun period alignment, units, sign and revision vintage. If no new route exists, close once and advance to RWA.
- No IMF re-query or cohort rebuild.

## 6. Acceptance matrix
| Gate | Result |
|---|---|
| TCMB official BOP page and monthly frequency | PASS |
| TCMB EVDS time-series availability documented | PASS |
| September report separate portfolio asset/liability rows | PASS |
| Q2 asset PDF snapshot sum | Existing evidence +5,749 USDm |
| Q2 liability PDF snapshot sum | Existing evidence +9,183 USDm |
| IMF Q2 asset/liability values | Existing archived receipt +5,749 / +9,270 USDm |
| Liability residual explanation | NOT_ESTABLISHED |
| ZIP raw bytes / SHA-256 / revision metadata | NOT_CAPTURED |
| Same-vintage bridge | NOT_ESTABLISHED |
| TUR full national validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 7. Protected constraints
₹0; official/free sources only. No synthetic data, fabricated timestamps, net-to-leg inference, stock-as-flow, unsupported scale/sign conversion, ad-hoc tolerance, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Official sources
- TCMB BOP Statistics: https://tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Statistics/Balance%2Bof%2BPayments%2Band%2BRelated%2BStatistics/Balance%2Bof%2BPayments%2BStatisticss/
- TCMB September 2026 BOP developments: https://www.tcmb.gov.tr/wps/wcm/connect/4329826e-067d-44b6-8748-620900d91741/BalanceofPayments_September2026.pdf?MOD=AJPERES
- Exact September ZIP URL already captured in Continuation 118 report; retrieval timed out, do not repeat.
