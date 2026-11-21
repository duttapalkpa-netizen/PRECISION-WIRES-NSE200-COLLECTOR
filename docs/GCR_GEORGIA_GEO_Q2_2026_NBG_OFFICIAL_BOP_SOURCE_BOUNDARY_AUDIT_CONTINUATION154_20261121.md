# Georgia (GEO) Q2-2026 — NBG official BOP source-boundary audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 154
Status: FIXED-COHORT MEMBERSHIP PASS; OFFICIAL Q2 BOP RELEASE / PERIOD / BPM5 STATEMENT PASS; SEPARATE Q2 PORTFOLIO TRANSACTION LEGS NOT_CAPTURED; VINTAGE / BPM BRIDGE NOT_ESTABLISHED; GEO PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity & Acceptance Ledger, blob SHA `c6a953ff88dcae619023bfd11235a1e7936ad12a`.
- Re-fetched current GCR Master Priority Queue, blob SHA `0e5fb9304e5af696042aa1919f2f1fa49f651850`.
- Reused immutable 63-country Q2-2026 cohort CSV, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; GEO is a member and has both A_NFA_T and L_NIL_T entries present in the existing IMF panel.
- Scoped repository searches for GEO / Georgia Q2-2026 national portfolio dual-leg validation returned no dedicated prior GEO report. No cohort rebuild, no IMF re-query, no duplicate completed-country extraction.

## 2. Official National Bank of Georgia Q2-2026 BOP release
- Official release: “Balance of Payments of Georgia (II Quarter 2026)”.
- Official URL: https://nbg.gov.ge/en/media/news/balance-of-payments-of-georgia-ii-quarter-2026
- Publication date shown: 30 September 2026.
- The release explicitly states it is prepared in accordance with IMF Balance of Payments Manual, Fifth Edition (BPM5).
- It confirms the target reference period is Q2 2026 and publishes current-account, goods, services, income, transfers and net FDI headline values. It does not expose separate portfolio-investment asset and liability transaction amounts in the accessible release text.
- Do not infer portfolio legs from the financial-account balance or from the net international investment position. Do not substitute portfolio position stocks for BOP flows.

## 3. Official NBG data and revision boundary
- Official NBG “National Summary Data Page” is linked from the bank's website: https://nbg.gov.ge/en/statistics/national-data
- The rendered page lists separate BOP components “Portfolio investment: Assets” and “Portfolio investment: Liabilities”, each in USD millions. However, the visible observation period shown in the page extraction is Q3/21, so the displayed series snapshot is stale relative to target Q2-2026 and cannot supply current-quarter values.
- Official NBG BOP publications page: https://nbg.gov.ge/en/publications/balance-of-payments
  - States BOP and IIP are compiled quarterly and annually.
  - States BOP/IIP/external debt are regularly revised and revisions may apply to any period.
  - The page's visible annual document links run through 2024; it does not expose a Q2-2026 portfolio-legs dataset in the captured rendering.
- Official NBG IIP Q2-2026 release (30-Sep-2026): https://nbg.gov.ge/en/media/news/international-investment-position-of-geor-67
  - Reports June-end IIP assets and liabilities / quarter-on-quarter changes in aggregate position. These are stock-position measures and are explicitly excluded from transaction-flow comparison.
- No downloadable Q2-2026 BOP table, API response, workbook bytes, separate portfolio-legs values, raw national receipt, SHA-256, or observation-specific revision snapshot was captured in this bounded audit.

## 4. Existing archived IMF Q2 rows reused — no new query
From the existing raw IMF panel CSVs:
- Asset file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - Exact row: COUNTRY=GEO; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=325871168.2; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - Exact row: COUNTRY=GEO; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=416264206.49; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Raw OBS_VALUE and SCALE are preserved exactly. No scale conversion, sign adjustment, or national comparison is admitted. Git blob identifiers are not represented as newly computed SHA-256 digests.

## 5. BPM and vintage comparability
- NBG's Q2-2026 release explicitly states BPM5.
- The archived IMF rows are drawn from the existing IMF.STA:BOP(21.0.0) panel with P_F indicator and raw SCALE=6. This archive alone does not establish that the NBG BPM5 series is definitionally identical to the IMF panel observation, nor does it expose the underlying source-submission/revision timestamp for GEO Q2.
- NBG says revisions may apply to any period. The release date (30-Sep-2026) and IMF archive acquisition date (19-Nov-2026) do not prove synchronized source vintages.
- Therefore item-level mapping, sign equivalence, scale equivalence and same-vintage alignment remain NOT_ESTABLISHED.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| GEO membership in immutable 63-country Q2-2026 cohort | PASS |
| Archived IMF A_NFA_T / L_NIL_T rows present | PASS |
| Official NBG Q2-2026 BOP release located | PASS |
| NBG Q2 release publication date and BPM5 statement | PASS |
| National separate portfolio transaction legs for Q2-2026 | NOT_CAPTURED |
| NBG NSDP separate asset/liability labels | PASS (taxonomy only; visible period stale at Q3/21) |
| Current Q2 national unit/sign/concept mapping | NOT_ESTABLISHED |
| BPM5-to-IMF panel item equivalence | NOT_ESTABLISHED |
| Observation-specific revision vintage match | NOT_ESTABLISHED |
| National raw bytes / receipt / SHA-256 | NOT_CAPTURED |
| Separate-leg numeric comparison | NOT_DONE |
| GEO full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 7. Next bounded action
- Do not repeat the same NBG press-release page or use the visible stale Q3/21 NSDP values.
- Seek a genuinely different NBG statistics-data export/API route that returns current quarterly BOP component series, specifically portfolio asset and liability transaction flows for 2026-Q2. Preserve the raw response/workbook and its timestamp/hash.
- Resolve the NBG BPM5 release basis against the IMF panel's exact item definitions before comparing values. Capture NBG's observation-level revision status and any available revision snapshot.
- If the current official export route is unavailable, retain GEO PARTIAL / NOT PASS and advance to the next eligible fixed-cohort member. No IIP stock substitution, net-to-leg back-solving or estimated allocation.

## 8. Protected invariants
₹0; free official sources only. No synthetic values, no fabricated timestamps, no IMF re-query, no cohort rebuild, no inferred sign/scale, no stock-as-flow, no net-to-leg back-solving, no aggregate admission and no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
