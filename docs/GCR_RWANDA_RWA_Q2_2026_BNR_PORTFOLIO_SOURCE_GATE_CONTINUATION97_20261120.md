# Rwanda RWA Q2-2026 — BNR National BOP Portfolio Source Gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, next country after ROU
Decision: **RWA fixed-cohort membership PASS; official BNR BPM6 source discovery PASS; historical fiscal-year separate portfolio legs found (methodology/crosswalk evidence only); 2026H1 net-only portfolio figure found; Q2-2026 national A_NFA_T/L_NIL_T values NOT_CAPTURED; RWA PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight and duplicate rejection
- Re-fetched the Master Continuity Ledger (blob SHA `1c99bc983be5ecc2f78f2ecf4f7ee6ac52b276d5`), GCR Master Priority Queue (blob SHA `b5f66fc867c1cce3645256f4067cafc035a3c18e`), fixed 63-country Q2-2026 both-leg cohort (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`), and ROU Continuations 95 and 96 (blob SHAs `37f744511aeab33539d1fca15be0bce08536cd90` and `6f3c046255ada664589286bdae276606588cc9a4`).
- RWA is the next country after ROU in the fixed cohort and is present with both IMF A_NFA_T and L_NIL_T legs.
- Repository searches for RWA BNR Q2-2026, Rwanda portfolio assets/liabilities and a prior RWA source gate returned no dedicated country report. No existing RWA report was repeated.
- Reused the immutable cohort and existing IMF archive; no cohort rebuild and no new IMF query.

## 2. Official BNR source discovery
- BNR External Sector Statistics portal states Rwanda's external-sector statistics, including BOP and IIP, are compiled in line with IMF BPM6. The page lists a “Balance of Payment” document dated 30-Jun-2026, but the page itself is a JavaScript application and the exact listed file URL/bytes could not be resolved through the current retrieval path.
- BNR Annual Report 2024-2025, Appendix 14, “Balance of Payments (in USD million)”, publishes fiscal-year values FY2019/20–FY2024/25 and separates portfolio investment into assets and liabilities.
- BNR Monetary Policy and Financial Stability Statement, October 2026, Table 12, publishes 2026H1 portfolio investment net balance only; it does not publish separate 2026H1 asset and liability legs in that table.

## 3. Historical fiscal-year separate-leg evidence — not Q2 evidence
BNR Annual Report 2024-2025 Appendix 14, BOP in USD million:
| Fiscal year | Portfolio net | Portfolio assets | Portfolio liabilities |
|---|---:|---:|---:|
| FY2019/20 | -4.7 | 30.9 | 35.6 |
| FY2020/21 | +8.0 | 9.9 | 1.9 |
| FY2021/22 | -260.9 | 21.3 | 282.2 |
| FY2022/23 | +108.6 | 50.2 | -58.4 |
| FY2023/24 | +12.9 | 18.8 | 5.9 |
| FY2024/25 | +5.8 | 12.1 | 6.3 |
- In every displayed fiscal-year row, the published portfolio net equals assets minus liabilities (e.g., FY2024/25: 12.1 − 6.3 = 5.8; FY2022/23: 50.2 − (−58.4) = 108.6). This is a useful country-specific historical arithmetic/sign diagnostic, not by itself proof of the exact IMF A_NFA_T/L_NIL_T definitions or a 2026-Q2 bridge.
- The periods are fiscal years, not calendar quarters. Do not split, prorate, interpolate, or use these annual figures as 2026-Q2 observations.
- The current browser retrieval exposed report text and tables, but a direct byte download attempt of the official PDF failed. No raw PDF bytes, response headers, retrieval timestamp receipt, byte count or SHA-256 are claimed or archived.

## 4. 2026H1 official publication boundary
- BNR MPFSS October 2026, Table 12 (USD million), lists portfolio investment net: 2023=52; 2024=21; 2025=42; 2025H1=-10; 2026H1=+14.
- This is an H1 net portfolio balance only. It does not contain separate asset and liability legs or a standalone Q2 value. It cannot be split into Q1/Q2 by subtraction because the Q1 value for the same portfolio net series and matching vintage was not established in this source route; even if found, net-only would still not supply both IMF legs.
- BNR August 2026 Monetary Policy Report's Table 2 is a summary financial-account table and does not provide portfolio investment legs. Do not substitute its total financial-account, direct investment, government borrowing or reserves rows.

## 5. Retrieval and admission gate
| Gate | Status |
|---|---|
| RWA in fixed 63-country Q2-2026 both-leg cohort | PASS |
| No prior dedicated RWA Q2 source-gate report found | PASS |
| BNR official BPM6 external-sector source | PASS |
| BNR 30-Jun-2026 BOP document locator on portal | SOURCE_LISTED |
| Exact locator/file URL and downloadable bytes for 30-Jun dataset | NOT_RESOLVED |
| Historical fiscal-year separate portfolio asset/liability rows | PASS (methodology/crosswalk evidence only) |
| Historical report raw PDF bytes / SHA-256 | NOT_CAPTURED |
| 2026H1 portfolio net balance | PASS (net-only context; USDm +14) |
| 2026H1 separate asset/liability legs | NOT_CAPTURED |
| 2026Q2 national A_NFA_T | NOT_CAPTURED |
| 2026Q2 national L_NIL_T | NOT_CAPTURED |
| Fiscal-year to calendar-quarter conversion | NOT_ALLOWED |
| Sign/concept crosswalk to exact IMF keys | PARTIAL / NOT_ESTABLISHED |
| Same-vintage comparison | NOT_DONE |
| RWA national validation | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 6. Next exact action
- Resolve the BNR External Sector Statistics portal's 30-Jun-2026 “Balance of Payment” item through a supported downloadable document or dataset route. Capture exact URL, original bytes, HTTP metadata, retrieval timestamp, byte count and SHA-256 before parsing.
- Inspect whether that dataset includes calendar Q2 2026 or quarterly series, and whether it reports separate portfolio assets and liabilities, period/frequency, USD unit, signs and vintage.
- If the 30-Jun item is an IIP stock table or net-only BOP summary, reject it for A_NFA_T/L_NIL_T validation and record the exact source-family mismatch. Do not substitute the October H1 net-only +14 USDm figure or annual FY rows.
- Reuse existing IMF exact RWA rows; no IMF re-query. If the portal file route remains inaccessible, close that exact route and advance to the next eligible country in the fixed cohort after preflight.

## 7. Official evidence links
- BNR External Sector Statistics (BPM6; BOP document listed 30-Jun-2026): https://www.bnr.rw/esstatistics
- BNR Annual Report 2024-2025 (Appendix 14; fiscal-year separate portfolio asset/liability rows): https://www.bnr.rw/documents/Annual_Report_2024_25_English_Full_Version_RwYAWN0.pdf
- BNR MPFSS October 2026 (Table 12; 2026H1 net-only portfolio investment): https://www.bnr.rw/documents/MPFSS_Report_October_2026.pdf
- BNR Monetary Policy Report August 2026 (Table 2; summary BOP only): https://www.bnr.rw/documents/Monetary_Policy_Report_August_2026.pdf
- Rwanda Statistical Yearbook 2025: https://statistics.gov.rw/sites/default/files/documents/2026-01/RWANDA_STATISTICAL_YEARBOOK_2025_0.pdf

## 8. Protected invariants
No cohort rebuild, no IMF re-query, no synthetic data, no fiscal-year proration, no quarterly interpolation, no net-to-leg inference, no netting, no stocks-as-flows, no inferred FX, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Research spend ₹0.


## Continuation 130 — RWA official portal locator recheck (2026-11-21)
- Re-fetched the current Master Ledger, GCR Priority Queue, fixed cohort, Batch-1 report, NPL report and this RWA report. NPL's distinct NSDP route did not yield current Q2 data; per fixed batch order, advanced to RWA.
- Rechecked the official National Bank of Rwanda External Sector Statistics portal. Search-indexed official portal text lists a “Balance of Payment” document dated 30-Jun-2026 and states BOP/IIP statistics are compiled under IMF BPM6. Direct portal open returns only “You need to enable JavaScript to run this app”; the document's exact downloadable URL/bytes remain unresolved.
- Rechecked official BNR Monetary Policy Report August 2026: Table 2 is a summary BOP table for 2025Q1/2026Q1 and omits portfolio investment assets/liabilities. It mentions Q2 merchandise export developments but does not publish Q2 portfolio transaction legs. Rejected as non-matching scope.
- No new raw Q2 transaction rows, URL, bytes, hash or separate A_NFA_T/L_NIL_T values obtained. Existing fiscal-year separate-leg rows remain crosswalk/methodology evidence only; 2026H1 net-only +14 USDm is not Q2 and cannot be split into legs.
- RWA remains PARTIAL / NOT PASS; Q2 asset/liability legs NOT_CAPTURED; same-vintage/sign crosswalk NOT_ESTABLISHED; aggregate NOT_AUTHORIZED. Next exact action: resolve the BNR portal's June-30 item via an actually supported document/API route; if unavailable, close that route once and advance to SLV.
- Evidence: https://www.bnr.rw/esstatistics ; https://www.bnr.rw/documents/Monetary_Policy_Report_August_2026.pdf . No IMF re-query/cohort rebuild. ₹0; production unchanged; UNKNOWN is never PASS.
