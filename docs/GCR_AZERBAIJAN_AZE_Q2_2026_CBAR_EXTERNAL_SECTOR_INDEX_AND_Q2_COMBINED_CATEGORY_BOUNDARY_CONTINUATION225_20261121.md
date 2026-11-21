# Azerbaijan (AZE) Q2-2026 — CBAR external-sector index and combined-category boundary
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 225
Status: DISTINCT OFFICIAL EXTERNAL-SECTOR INDEX ROUTE VERIFIED; Q2-2026 CBAR BULLETIN CONFIRMS ASSET/LIABILITY SPLIT ONLY AT “PORTFOLIO AND OTHER INVESTMENTS” COMBINED LEVEL; PORTFOLIO-ONLY LEGS NOT_CAPTURED; AZE PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate prevention
Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, fixed 63-country cohort, national validation matrix and AZE C146 report. ALB C139/C140/C141/C192 routes were excluded as closed; GIN C170/C224 and GEO C154/C223 routes were excluded as bounded. AZE C146 is the controlling country report. Reused the fixed cohort and existing archived IMF rows; no IMF re-query or cohort rebuild.

## 2. New official route inspected
- CBAR official External Sector Statistics index: https://www.cbar.az/page-43/external-sector-statistics?language=en
- The official page organizes downloadable external-sector publications by year and exposes a 2026 section with eight file entries. The same page links an Interactive Statistic Database at navigation.e-cbar.az; the linked database shell returns no text content in the current retrieval channel.
- CBAR official Macroeconomic Indicators page: https://www.cbar.az/page-41/macroeconomic-indicators?language=en lists a 27-Oct-2026 Balance of Payments item, file size 63.66 KB, separately from the 09/2026 Statistical Bulletin.
- The index is a distinct official discovery surface, but the 2026 attachment controls resolve to same-page asset anchors in the accessible rendering; no distinct raw Q2 file locator or data response was returned from those anchors. Do not guess attachment IDs/URLs.

## 3. Q2 2026 official bulletin category check
- Re-opened CBAR Statistical Bulletin 09/2026: https://uploads.cbar.az/assets/34f2e92e50d556d098dd5b36f.pdf
- Table 1.4, “Balance of payments of the Republic of Azerbaijan”, unit USD million, has explicit QII 2026 column. It reports net acquisition of financial assets 3,116 and net incurrence of liabilities 2,255 at the top level.
- Under each leg, the bulletin groups “portfolio and other investments” together: asset-side -302; liability-side +2,466 (USDm). These are combined portfolio-plus-other values, not portfolio-only observations. They must not be admitted as AZE national portfolio legs or compared to the IMF portfolio-only rows.
- The table note states BOP is classified from 2013 according to assets/liabilities and based on IMF BPM6. This supports broad framework context only; it does not make the combined category portfolio-only.
- No national portfolio-only Q2 asset/liability values, raw Q2 dataset bytes, API payload, retrieval receipt, or new SHA-256 were captured. The 2026 index/H1 materials do not authorize a quarterly split or differencing.

## 4. Existing IMF rows and gate preservation
C146 remains the source of record for archived IMF Q2 raw rows: A_NFA_T OBS_VALUE=-333337000 and L_NIL_T OBS_VALUE=-8044000.0000001, both retained with original USD/SCALE=6 attributes. No transformations or recalculation performed in this continuation.

| Gate | Status |
|---|---|
| Fixed 63-country cohort / IMF rows reused | PASS |
| Distinct official CBAR external-sector index inspected | PASS |
| Q2 2026 BOP bulletin category and unit confirmed | PASS |
| Q2 national portfolio-only asset leg | NOT_CAPTURED |
| Q2 national portfolio-only liability leg | NOT_CAPTURED |
| Combined portfolio-and-other asset/liability rows | FOUND; NOT_ADMISSIBLE as portfolio-only |
| Raw export/API payload and national SHA-256 | NOT_CAPTURED |
| Sign/scale/vintage crosswalk for portfolio-only rows | NOT_ESTABLISHED |
| AZE full national validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Next exact action
Only reopen AZE if a distinct official detailed Q2 BOP annex/export/API exposes portfolio investment separately from other investment for both assets and liabilities, with raw bytes and revision metadata. The 2026 external-sector index and Q2 bulletin category boundary have now been documented; do not repeat them. Do not subtract H1 and Q1 unless both are standalone portfolio-only observations from a matched vintage. No net-to-leg back-solving, combined-category substitution, IIP stock substitution, IMF re-query or cohort rebuild.

## 6. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, unsupported sign/scale/FX conversion, no tolerance widening, no production code/configuration change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
