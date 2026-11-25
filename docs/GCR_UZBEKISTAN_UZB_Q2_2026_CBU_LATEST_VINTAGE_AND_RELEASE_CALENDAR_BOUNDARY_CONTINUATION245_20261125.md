# Uzbekistan (UZB) Q2-2026 — CBU latest-vintage and release-calendar boundary (Continuation 245)

Date: 2026-11-25 (Asia/Kolkata)

## Decision
A distinct official-source freshness and release-calendar audit was completed for UZB. CBU's official standard-presentation Q2-2026 BOP dataset page is indexed as updated 29-Sep-2026 and contains a 649.2 KB XLSX download locator. The official e-GDDS release calendar schedules Q2/2026 BOP publication for 30-Sep and Q3/2026 BOP publication for 31-Dec. A separate official H1-2026 review published 29-Sep discusses net portfolio investment inflows (around USD 2bn) but does not expose the separate Q2 portfolio asset/liability transaction legs or an observation-specific revision timestamp. The standard dataset page's displayed unit string is “million USD, end of period”; without workbook headers/metadata, transaction-vs-stock time basis remains unresolved. No raw XLSX bytes or hash were captured. UZB remains DATA_CAPTURED; existing numeric asset/liability PASSes retained; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.

## 1. Continuity and duplicate-prevention preflight
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country Q2-2026 matrix.
- Re-read Library Mother File continuation 1–53, including GCR pages 46–53 context.
- Re-opened controlling UZB C123 report and checked the existing CBU route fingerprint.
- Reused existing archived IMF exact rows and numeric comparisons. No IMF re-query, no cohort rebuild, no repeat of completed numeric arithmetic, and no repeat of the already attempted identical CBU workbook-byte retrieval.
- MEX C244 post-release task remains scheduled for after 20:30 IST on 25-Nov-2026; it is not replaced by this independent UZB task.

## 2. New official CBU source evidence
1. CBU official statistics page (mobile surface) search-indexed update date: 24-Nov-2026. It lists “Statistical bulletin of the Central bank - first half of 2026” as an XLSX item (1.4 MB). The dynamically opened cached page returned an older 19-May-2026 version and did not expose that new item; therefore the search-indexed 24-Nov item is recorded as a locator lead, not as inspected workbook evidence.
2. Official CBU H1-2026 review announcement, dated 29-Sep-2026, states that net portfolio investment inflows were around USD 2bn for the first half. This is a half-year net figure and cannot validate Q2-only portfolio asset/liability legs. It also discusses IIP stocks, which are not transaction-flow substitutes.
3. Official CBU standard-presentation BOP dataset page identifies update date 29-Sep-2026, XLSX 649.2 KB, and Q2 2026 as the latest displayed quarter. The official e-GDDS dataset locator identifies XLSX 70.2 KB, unit text “million USD, end of period”, and periods through 2026-Q2.
4. Official CBU e-GDDS release calendar lists BOP reporting periods Q4/2025, Q1/2026, Q2/2026, Q3/2026 with scheduled publication dates 31, 30, 30, 31 respectively. Therefore the Q3/2026 publication is scheduled for 31-Dec-2026. This is a schedule, not proof of future publication.

## 3. Existing C123 numeric evidence reused — no recalculation
- Existing official CBU Q2 preview: portfolio assets USD 0.01m; liabilities USD 1,960.49m.
- Existing archived IMF exact Q2 observations: A_NFA_T 9,793.61706018728 (SCALE=6); L_NIL_T 1,960,492,267.78624 (SCALE=6).
- Existing bounded display /1,000,000 comparisons passed at the published precision; exact prior residuals and source attributes remain in C123.
- CBU unit text “million USD, end of period” creates an unresolved time-basis ambiguity for transaction-flow rows. Do not infer that the values are stocks or flows solely from the page-level unit string.
- CBU page update/retrieval date and IMF panel retrieval date do not establish observation-specific revision identity.

## 4. Gate matrix
| Gate | Status |
|---|---|
| Ledger / Queue / Registry / Matrix preflight | PASS |
| Library Mother File GCR context checked | PASS |
| UZB fixed-cohort membership and C123 report reuse | PASS |
| Existing national dual-leg numeric comparison | PASS (reused; not recalculated) |
| New official H1-2026 review inspected via indexed announcement | PASS (net-only context; not A/L proof) |
| Official CBU standard BOP page update 29-Sep-2026 | PASS |
| Official CBU release-calendar Q3 date 31-Dec-2026 | PASS (scheduled) |
| New official workbook bytes / headers / SHA-256 | NOT_CAPTURED |
| Q2 transaction-vs-stock time basis from workbook | NOT_ESTABLISHED |
| Observation-specific Q2 revision/vintage bridge | NOT_ESTABLISHED |
| UZB full national validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 5. Next exact action
- Reopen only if a supported byte-preserving route exposes the distinct official CBU first-half-2026 statistical bulletin XLSX or a new CBU Q2 BOP workbook. Capture exact bytes, headers, workbook sheets, retrieval UTC, size and SHA-256.
- Inspect the exact Q2 portfolio asset/liability series headers and notes to resolve “end of period” time-basis ambiguity; do not treat IIP stock rows or H1 net portfolio totals as transaction-leg evidence.
- Capture any Q2 observation revision/cutoff metadata and compare against the archived IMF observation vintage. Do not re-query IMF.
- If no workbook/vintage bridge is available, preserve UZB pending/unknown and advance the next eligible fixed-cohort member after fresh preflight.

## 6. Protected invariants
₹0; free official sources only. No IMF re-query, no cohort rebuild, no net-to-leg back-solving, no stock-as-flow substitution, no inferred sign/scale/time-basis conversion, no synthetic timestamps, and no aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. UNKNOWN is never PASS.

## Sources
- CBU official standard BOP dataset: https://cbu.uz/en/statistics/bop/4616923/
- CBU official e-GDDS BOP data locator: https://cbu.uz/en/statistics/e-gdds/data/127982/?mobile=Y
- CBU official statistics page: https://cbu.uz/en/statistics/?mobile=Y
- CBU official e-GDDS release calendar: https://cbu.uz/en/statistics/calendar/
- CBU official H1-2026 review: https://cbu.uz/en/press_center/releases/4616748/
- Controlling prior UZB report: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION123_20261121.md
- Web evidence: turn838512search3, turn838512search4, turn838512search5, turn838512search7, turn838512search10, turn806368view0, turn458199view0.
