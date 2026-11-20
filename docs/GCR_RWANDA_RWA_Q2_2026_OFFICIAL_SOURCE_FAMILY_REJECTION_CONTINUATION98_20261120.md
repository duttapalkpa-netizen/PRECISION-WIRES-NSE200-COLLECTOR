# Rwanda RWA Q2-2026 — Official-source family rejection and quarter-boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-3
Decision: **New official Q2 trade-source discovery PASS; source-family rejection PASS; BNR Q2 BOP portfolio dual legs remain NOT_CAPTURED; RWA PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight
- Re-fetched Master Ledger (blob SHA 531da8638ca5cddde0af73687311a77272b3d5f7), GCR Priority Queue (blob SHA 4d382f5517699c78b6b5c5fee29e3836b53679cc), RWA Continuation 97 (blob SHA af725eba157789e16e65a783e886d96f66fdc727) and fixed cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8).
- RWA remains in the immutable cohort with both IMF entries present. Existing BNR annual dual-leg, 2026H1 net-only, and portal listing findings were reused; no repeated IMF request, no cohort rebuild, no re-parsing of historical rows.

## 2. New official Q2 source-family screening
- National Institute of Statistics of Rwanda (NISR) official “Formal external trade in Goods report - Q2, 2026” is publicly indexed. It reports Q2-2026 merchandise exports USD 548.98m, imports USD 1,606.39m, re-exports USD 179.59m, and trade balance -USD 877.81m.
- This is a goods-trade dataset, not Balance of Payments financial-account portfolio investment. It has no portfolio asset or liability transactions. Explicitly reject it for IMF A_NFA_T / L_NIL_T validation; do not treat trade deficit as BOP portfolio flow.
- BNR August 2026 Monetary Policy Report Table 2 is a 2026Q1 BOP summary with current account, capital account, total financial account, direct investment, government external borrowing and reserve assets. It does not report portfolio asset/liability legs and does not report Q2 financial-account components. Reject for portfolio dual-leg validation.
- BNR October 2026 MPFSS Table 12 provides 2026H1 aggregate net portfolio investment +14 USDm in the net-only table context previously recorded; it is half-year, net-only, not standalone Q2 and cannot supply either separate IMF leg.
- The BNR External Sector Statistics portal still lists a “Balance of Payment” item dated 30-Jun-2026, but its page is JavaScript-only to the current retrieval client (“You need to enable JavaScript to run this app”). Exact file URL, downloadable bytes, frequency and row structure remain unresolved. No new file capture is claimed.

## 3. Evidence boundary / rejected substitutions
| Candidate | What it actually contains | Decision for Q2 portfolio legs |
|---|---|---|
| NISR Formal External Trade Q2 2026 | Goods exports/imports/re-exports/trade balance | REJECT — wrong account/source family |
| BNR MPFSS August 2026, Table 2 | 2026Q1 BOP summary; no portfolio split | REJECT — wrong period and no dual legs |
| BNR MPFSS October 2026, Table 12 | 2026H1 BOP summary, net portfolio figure only | REJECT — half-year and net-only |
| BNR External Sector portal 30-Jun-2026 item | BOP document listed; file locator/bytes inaccessible | SOURCE_LISTED / NOT_CAPTURED |
| BNR Annual Report 2024-25 Appendix 14 | Fiscal-year portfolio assets and liabilities | CONTEXT ONLY — not calendar Q2 |

## 4. Gate matrix
- RWA fixed cohort membership: PASS.
- BNR BPM6 source discovery: PASS.
- Official Q2 goods-trade report discovery: PASS (rejected for BOP portfolio).
- Wrong-family / wrong-period rejection: PASS.
- Exact BNR 30-Jun-2026 BOP file locator and raw bytes: NOT_RESOLVED / NOT_CAPTURED.
- Q2-2026 national A_NFA_T: NOT_CAPTURED.
- Q2-2026 national L_NIL_T: NOT_CAPTURED.
- Q2 period, frequency, units, signs, revision vintage: NOT_ESTABLISHED.
- IMF exact RWA national comparison: NOT_DONE.
- RWA: PARTIAL / NOT PASS.
- Aggregate / production: NOT_AUTHORIZED.

## 5. Next action and route closure
- Close the current public BNR portal page route for this retrieval client; do not repeat the same JS-only page request.
- Reopen only if a genuinely new supported official file/API locator is identified (for example a direct BNR dataset URL or a supported NISR/BNR machine-readable BOP export containing financial-account components). Do not treat trade tables or half-year net-only figures as substitutes.
- If no new supported BNR route is available, advance to the next eligible member of the fixed 63-country cohort after full continuity preflight. Reuse archived IMF rows; no IMF re-query or cohort rebuild.

## 6. Official evidence
- BNR External Sector Statistics (BPM6; BOP item listed 30-Jun-2026): https://www.bnr.rw/esstatistics
- NISR Formal external trade in Goods report Q2-2026: https://www.gis.statistics.gov.rw/statistical-publications/business-establishment-finance-trade/business-establishment-finance-trade/formal-external-trade-goods-report-q2-2026
- BNR Monetary Policy Report August 2026: https://www.bnr.rw/documents/Monetary_Policy_Report_August_2026.pdf
- BNR MPFSS October 2026: https://www.bnr.rw/documents/MPFSS_Report_October_2026.pdf
- BNR Annual Report 2024-2025 Appendix 14: https://www.bnr.rw/documents/Annual_Report_2024_25_English_Full_Version_RwYAWN0.pdf

## 7. Protected invariants
No cohort rebuild, no IMF re-query, no trade-to-BOP substitution, no net-to-leg inference, no fiscal-year proration, no quarterly interpolation, no netting, no stocks-as-flows, no inferred FX, no synthetic data, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Research spend ₹0.
