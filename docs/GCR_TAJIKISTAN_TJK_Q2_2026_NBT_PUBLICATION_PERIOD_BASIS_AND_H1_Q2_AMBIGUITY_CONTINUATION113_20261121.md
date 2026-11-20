# Tajikistan TJK Q2-2026 — NBT publication period-basis and H1/Q2 ambiguity (Continuation 113)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **The official NBT archive's 2026 link label says “FOR THE 2 QUARTER”, but the resolved PDF filename is “ПБ-нимсолаи 1 с.2026.pdf”, i.e. a first-half-year/half-year-1 label. The issue is not proven to be a standalone Q2 flow report. PDF fetch still times out, so the document's internal cover/table period cannot be inspected. Treat period basis as AMBIGUOUS / likely H1 based on filename, not confirmed Q2. Do not derive Q2 by subtracting Q1. TJK remains NOT_VALIDATED / NOT PASS.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA e7222e8e08233bb2f94decb543f7213a553465e8
- GCR Priority Queue blob SHA 5ca1d0c7fbbc24e8686b9577ffe12c96d7f28195
- Continuation 112 blob SHA dbc7ff164bf05d54e7898365ff6f2359f6bed03d
Skipped completed PASS work; did not retry the identical PDF fetch.

## 2. Newly resolved period-basis ambiguity
- Official NBT external-sector archive page shows year 2026 and visible link label “FOR THE 2 QUARTER”.
- Exact resolved target:
  https://nbt.tj/upload/iblock/ae9/9465qfirvabk79vi27r11sykrgn37xen/%D0%9F%D0%91-%D0%BD%D0%B8%D0%BC%D1%81%D0%BE%D0%BB%D0%B0%D0%B8%201%20%D1%81.2026.pdf
- URL-decoded filename: ПБ-нимсолаи 1 с.2026.pdf.
- The filename phrase “нимсолаи 1” denotes first half-year / half-year 1. This conflicts with the archive UI label.
- Official archive page lines 117–122 display year 2026 and “FOR THE 2 QUARTER”; lines 125–129 show the 2025 annual issue. The PDF's internal title, tables and cumulative/standalone basis remain uninspectable because fetching the exact PDF returned timeout.
- Official BOP page separately exposes “Standard representation” (link 94); opened page contains only heading/navigation and no extracted data table, so it does not independently resolve period basis or supply portfolio legs.
- Therefore do not treat the PDF as Q2 standalone solely from its archive link label. Filename suggests H1, but definitive period basis remains AMBIGUOUS until document inspection.

## 3. Explicit rejection / no false derivation
- No H1 minus Q1 subtraction: no same-vintage verified Q1 asset/liability legs were established in this task.
- No IIP stocks or operations/revaluation/other changes substituted for BOP transactions.
- No annual IMF staff estimates or annual values treated as Q2.
- No net-to-leg inference.
- No fabricated raw bytes, PDF hash, page count, or publication vintage.

## 4. Gate matrix
- TJK fixed-cohort Q2-2026 both-leg membership: PASS (reused; immutable cohort).
- NBT official archive page / 2026 publication locator: PASS.
- Archive display label “FOR THE 2 QUARTER”: CAPTURED.
- URL filename “нимсолаи 1” (half-year 1) period clue: CAPTURED.
- Internal PDF cover/table period basis: NOT_CAPTURED.
- Standalone Q2 vs H1 cumulative: AMBIGUOUS / NOT_VERIFIED.
- Separate portfolio asset and liability transaction legs: NOT_CAPTURED.
- Unit/sign/revision vintage: NOT_ESTABLISHED.
- Same-vintage IMF comparison: NOT_DONE.
- TJK NOT_VALIDATED / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact action
1. Obtain PDF bytes through an actual browser or byte-preserving route and inspect cover, table titles, reporting period, units and footnotes.
2. If it is H1 cumulative only, locate an independently published Q1 vintage with separate portfolio asset/liability legs and matching methodology/vintage. Only then may a documented H1−Q1 calculation be considered; otherwise no Q2 derivation.
3. If no matching Q1 vintage or standalone Q2 exists, mark national Q2 legs NOT_AVAILABLE and advance to next cohort country.
4. No repeated identical PDF fetch through the same timeout channel.

## 6. Sources
- Official NBT external-sector archive: https://nbt.tj/en/statistics/tavozuni-pardokhti-jt/tavozuni-pardokhti-jumhurii-tojikiston/nashriyai_tavozuni_pardoht_mavkei.php (archive link label “FOR THE 2 QUARTER”).
- Exact resolved PDF locator (fetch timed out): https://nbt.tj/upload/iblock/ae9/9465qfirvabk79vi27r11sykrgn37xen/%D0%9F%D0%91-%D0%BD%D0%B8%D0%BC%D1%81%D0%BE%D0%BB%D0%B0%D0%B8%201%20%D1%81.2026.pdf
- NBT Standard representation page: https://nbt.tj/en/payments_balance/standard_representation.php (no data table extracted).

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration or H1-Q1 subtraction without same-vintage evidence, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
