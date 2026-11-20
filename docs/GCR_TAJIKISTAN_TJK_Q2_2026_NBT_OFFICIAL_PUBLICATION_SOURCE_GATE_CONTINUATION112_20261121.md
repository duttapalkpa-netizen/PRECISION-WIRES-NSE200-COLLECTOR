# Tajikistan TJK Q2-2026 — NBT official publication source gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 112
Decision: **After parking Serbia's inaccessible July-vintage retrieval (without false PASS), the next fixed-cohort country TJK was screened. Official National Bank of Tajikistan (NBT) publication page exposes a dedicated 2026 “FOR THE 2 QUARTER” issue link for its BOP/IIP/external-debt publication. The exact linked PDF URL was resolved, but PDF retrieval timed out in the available channel. A public quarterly publication route is confirmed; the document contents and portfolio dual legs are NOT_CAPTURED. A separate NBT IIP report found by search is stock/position-change material, not a substitute for quarterly BOP portfolio transaction legs. TJK remains NOT_VALIDATED / NOT PASS.**

## 1. Continuity preflight and selection
- Re-fetched current Master Ledger and GCR Priority Queue before selecting new country task.
- Serbia SRB July-vintage header retrieval remains OPEN/BLOCKED after repeated official archive routes; no more identical URL retries. Its September-vintage May values remain PASS only for that vintage.
- Existing fixed Q2-2026 cohort remains immutable (63 countries). TJK (Tajikistan) is explicitly a cohort member; no cohort rebuild and no IMF re-query.
- Repository search returned no dedicated TJK Q2-2026 national portfolio dual-leg reconciliation report. TJK selected as next eligible country after THA/SRB sequence; THA numeric dual legs already PASS but its vintage bridge remains open.

## 2. Official NBT source locator
- National Bank of Tajikistan official BOP page: https://www.nbt.tj/en/payments_balance/
  - Describes NBT's statutory role in compiling Tajikistan's Balance of Payments.
  - States BOP is compiled according to IMF BPM5/BPM6 methodological recommendations.
  - Exposes annual and quarterly statistical publication navigation.
- Official external-sector publication page: https://nbt.tj/en/statistics/tavozuni-pardokhti-jt/tavozuni-pardokhti-jumhurii-tojikiston/nashriyai_tavozuni_pardoht_mavkei.php
  - Page shows year 2026 and a distinct “FOR THE 2 QUARTER” link.
  - Clicking the Q2-2026 link resolves to:
    https://nbt.tj/upload/iblock/ae9/9465qfirvabk79vi27r11sykrgn37xen/%D0%9F%D0%91-%D0%BD%D0%B8%D0%BC%D1%81%D0%BE%D0%BB%D0%B0%D0%B8%201%20%D1%81.2026.pdf
  - Web PDF fetch returned TimeoutError. No PDF bytes, page count, table contents, byte count or SHA-256 captured.
- The locator is the official Q2-2026 half-year publication. Its title/period link is evidence of publication route, not proof the document contains separately reported Q2 portfolio flow legs. Need inspect table frequency and period columns after retrieval.

## 3. Related source rejected for Q2 BOP flow validation
- NBT IIP 9-month 2025 PDF (found via search) reports portfolio investment under changes in IIP, including operations/revaluation/other changes. These are IIP position-reconciliation entries and do not establish Q2-2026 BOP transaction legs.
- IMF Country Report No. 26/001 contains annual staff projections/estimates, including annual portfolio investment; it is not a national quarterly observed dual-leg source.
- No annual aggregate, IIP stock, IIP change, forecast or net-only number is promoted to quarterly BOP assets/liabilities.

## 4. Updated gate matrix
- TJK fixed-cohort Q2-2026 both-leg membership: PASS (reused; no rebuild).
- NBT official BOP compilation responsibility and BPM6 reference: PASS (source-route/method context).
- Official NBT 2026 Q2 publication locator: PASS.
- Exact PDF content / raw bytes / hash: NOT_CAPTURED (timeout).
- Quarterly portfolio asset and liability legs: NOT_CAPTURED.
- BOP sign convention / units / revision vintage: NOT_ESTABLISHED.
- Same-vintage IMF-NBT dual-leg comparison: NOT_DONE.
- TJK: NOT_VALIDATED / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact action
1. Obtain the exact official Q2-2026 PDF through an available byte-preserving browser/download route; record response status/headers, UTC retrieval timestamp, byte count and SHA-256 before parsing.
2. Inspect BOP standard presentation tables and identify whether Q2 flows are separately reported for portfolio assets and liabilities, with explicit USD/unit and sign note.
3. Distinguish H1 cumulative figures from standalone Q2. If only H1 is published, do not subtract Q1 unless an independently verified, same-vintage Q1 source exists and revision alignment is proven.
4. Only after exact period, two legs, sign, unit and vintage are established, compare with existing archived IMF TJK A_NFA_T/L_NIL_T rows. No IMF re-query or cohort rebuild.
5. If PDF route remains inaccessible, retain BLOCKED and advance to next eligible country; do not use IIP stocks or annual projections as substitutes.

## 6. Official sources
- NBT Balance of Payments page: https://www.nbt.tj/en/payments_balance/
- NBT external-sector publication archive: https://nbt.tj/en/statistics/tavozuni-pardokhti-jt/tavozuni-pardokhti-jumhurii-tojikiston/nashriyai_tavozuni_pardoht_mavkei.php
- Exact NBT Q2-2026 PDF locator (retrieval timed out): https://nbt.tj/upload/iblock/ae9/9465qfirvabk79vi27r11sykrgn37xen/%D0%9F%D0%91-%D0%BD%D0%B8%D0%BC%D1%81%D0%BE%D0%BB%D0%B0%D0%B8%201%20%D1%81.2026.pdf
- NBT IIP 9-month 2025 PDF (rejected as Q2 BOP flow source): https://nbt.tj/files/Omor/2025/%D0%9F%D0%91%20%D0%B1%D0%B0%D1%80%D0%BE%D0%B8%209%20%D0%BC%D0%BE%D2%B3%D0%B8%202025.pdf
- IMF Country Report No. 26/001 (annual staff estimates; not quarterly national source): https://www.imf.org/-/media/files/publications/cr/2026/english/1tjkea2026001-source-pdf.pdf

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
