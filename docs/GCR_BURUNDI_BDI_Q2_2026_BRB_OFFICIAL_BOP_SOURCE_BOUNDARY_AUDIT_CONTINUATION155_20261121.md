# GCR Q2-2026 — Burundi (BDI) official BRB source-boundary audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 155
Status: FIXED-COHORT / IMF ROW PRESENCE PASS; OFFICIAL BRB HISTORICAL DUAL-LEG TABLE LOCATED; Q2-2026 NATIONAL DUAL LEGS NOT_CAPTURED; BDI PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and immutable 63-country Q2-2026 cohort. Reused the existing cohort and raw IMF panels; no IMF re-query and no cohort rebuild.
- BDI is a member of the fixed cohort: `BDI,Burundi,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`.
- Repository search found no dedicated prior BDI Q2-2026 national portfolio dual-leg validation report.
- Rejected repeat work: no re-download/rebuild of IMF panels, no conversion, no use of annual or projected IMF Article IV estimates as quarterly national evidence.

## 2. Official BRB source route and latest captured quarterly table
- Official source: Banque de la République du Burundi (BRB), “Rapport de Politique Monétaire du 4ème Trimestre 2025”, published 26-Feb-2026.
- Official document URL: https://www.brb.bi/sites/default/files/2026-03/Rapport%20de%20Politique%20Mon%C3%A9taire%20du%20quatri%C3%A8me%20trimestre%202025.pdf
- Official publication listing: https://www.brb.bi/autres_documents ; the currently indexed listing exposes the Q4-2025 report and Q3-2025 report, but no Q2-2026 BOP report in the captured page.
- Q4-2025 Table 9 (“Balance des paiements”, MBIF) publishes separate portfolio investment lines:
  - Portfolio investment net: -14,143.6 MBIF
  - Net acquisition of financial assets: 0.0 MBIF
  - Net incurrence of liabilities: 14,143.6 MBIF
  - The table also gives Q4-2024 and Q3-2025 comparators, not Q2-2026.
- The separate dual-leg presentation and MBIF unit are evidenced for the historical Q4-2025 table only. It does not establish Q2-2026 values, same-vintage metadata, BPM equivalence, or exact IMF mapping.
- A prior official BRB Q3-2025 report likewise published the two separate portfolio legs, but is also outside the target quarter. Do not splice adjacent quarters or derive Q2-2026 from cumulative/annual totals.
- The BRB site’s “Autres Documents” index and the currently indexed homepage show the Q4-2025 monetary-policy report as the latest BOP-containing monetary-policy report found in this bounded search. This is a search boundary, not proof that no unpublished or differently indexed dataset exists.

## 3. Existing archived IMF Q2-2026 rows reused — no query
From the existing raw IMF panel CSVs:
- Asset file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - Exact row: COUNTRY=BDI; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=130723.2699945969; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - Exact row: COUNTRY=BDI; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=0; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Raw OBS_VALUE and SCALE preserved exactly. Git blob identifiers are not SHA-256 digests. No scale conversion, sign adjustment or national comparison admitted.

## 4. Other non-substitutable evidence and rejection
- IMF 2026 Article IV report contains annual estimates/projections and is not a national quarterly Q2-2026 portfolio dual-leg source. Excluded.
- BRB Q4-2025 and Q3-2025 monetary-policy reports establish historical table format only; wrong reference period. Excluded from Q2 comparison.
- BRB monthly monetary/banking situation tables are not BOP portfolio transaction flows. Excluded.
- No national Q2-2026 separate portfolio asset/liability transaction values, raw source bytes, receipt timestamp, SHA-256, current unit/sign mapping or observation-specific revision vintage captured.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| BDI membership in immutable 63-country Q2-2026 cohort | PASS |
| Archived IMF A_NFA_T / L_NIL_T rows present | PASS |
| Official BRB Q4-2025 BOP dual-leg table located | PASS (historical format only) |
| BRB Q2-2026 national separate portfolio transaction legs | NOT_CAPTURED |
| National Q2-2026 raw bytes / receipt / SHA-256 | NOT_CAPTURED |
| National unit/sign/concept mapping for Q2-2026 | NOT_ESTABLISHED |
| BPM and item equivalence to IMF panel | NOT_ESTABLISHED |
| Observation-specific revision-vintage match | NOT_ESTABLISHED |
| Separate-leg numeric comparison | NOT_DONE |
| BDI full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. GEO route-discovery addendum from the preceding bounded audit
- NBG's official NSDP page has a Balance of Payments row with “Browse Data” and “Download in SDMX”; its “Browse Data” route points to the general NBG Statistics Data portal. The page's separately rendered National Summary Data Page still exposes stale Q3/2021 BOP observations. No exact SDMX download URL, current Q2-2026 response, raw bytes or observation-specific vintage was captured, so this is a route lead only, not a data capture.
- Official NBG Q2-2026 BOP release (30-Sep-2026) says BPM5. However, NBG's own official 2014 methodology notice says that from Q1-2014 BOP/IIP are compiled under BPM6 and since 2015 data are presented only in BPM6. This is a material methodology conflict requiring resolution; do not assume either version without a Q2-specific correction/metadata explanation.
- Official NBG BOP publications page says BOP/IIP are regularly revised and may be revised for any period. GEO remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Relevant official URLs:
  - NSDP: https://nbg.gov.ge/en/page/nsdp
  - Statistics Data portal: https://nbg.gov.ge/en/statistics/statistics-data
  - Q2-2026 release: https://nbg.gov.ge/en/media/news/balance-of-payments-of-georgia-ii-quarter-2026
  - NBG 2014 methodology notice: https://nbg.gov.ge/en/media/news/national-bank-of-georgia-started-compiling-balance-of-payments-statistics-according-to-new
  - BOP publications/revision note: https://nbg.gov.ge/en/publications/balance-of-payments

## 7. Next bounded action
- Keep BDI PARTIAL. Do not use Q4-2025 or Q3-2025 values as Q2-2026; do not derive quarterly values from annual estimates.
- Next eligible cohort member should be selected from the immutable cohort after a fresh duplicate-report search and source-feasibility preflight. Prefer an official free Q2-2026 BOP source with separate portfolio asset/liability transaction legs.
- Revisit BDI only if BRB publishes a Q2-2026 table or a genuinely different official data export with current dual-leg values and dated revision metadata.
- For GEO, pursue the exact NBG SDMX download target and resolve the BPM5/BPM6 contradiction before any comparison.

## 8. Protected invariants
₹0; free official sources only. No synthetic values, fabricated timestamps, IMF re-query, cohort rebuild, inferred sign/scale, stock-as-flow, net-to-leg back-solving, annual-to-quarter allocation, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
