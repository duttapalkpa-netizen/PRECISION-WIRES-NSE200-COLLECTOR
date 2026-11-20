# Türkiye TUR Q2-2026 TCMB vs IMF portfolio BOP validation — 2026-11-20

Decision: **PARTIAL / NOT PASS**. The asset leg reconciles exactly at displayed USD-million precision; the liability leg has a USD 87m residual against the latest inspected TCMB monthly series. Do not aggregate.

## Continuity preflight
- Re-fetched the current Master Continuity Ledger, GCR Priority Queue, POL NBP source-gate report, SAU vintage report and CHN access audit.
- POL's NBP XLSX retrieval blocker is already documented; did not repeat the same failed retrieval.
- Selected Türkiye (TUR), next eligible member in the existing 12-country IMF exact-key receipt. No new IMF GET, cohort rebuild or panel rebuild.

## IMF exact-key receipt (reused)
Artifact run 44474458684 / artifact 14505009889; ZIP SHA-256:
588101c0deff3b431098e0f3205005d3d5913f3014137065b074890b353ecdf60

- TUR A_NFA_T: HTTP 200; retrieved 2026-11-19T06:45:23.329543Z; 4,864 bytes; SHA-256 380018babf368f4e66c49f2c1753e5adc496088f3d0d71e4e4676c8c252f529f.
- TUR L_NIL_T: HTTP 200; retrieved 2026-11-19T06:45:23.717012Z; 4,729 bytes; SHA-256 b8852a6b3e5ddbc7e84ecd47786cc71413b3daf74021791a438d6b0638a5df1d.
- Each exact series has 46/46 broad observation/attribute matches, 2015-Q1 through 2026-Q2; no missing keys or mismatches.
- IMF Q2-2026: A_NFA_T +5,749,000,000 USD; L_NIL_T +9,270,000,000 USD (SCALE=6; display USDm +5,749 and +9,270).

## Official national source
Central Bank of the Republic of Türkiye (CBRT/TCMB), “Balance of Payments Statistics”, September 2026 data:
- Official statistics landing page: https://tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Statistics/Balance%2Bof%2BPayments%2Band%2BRelated%2BStatistics/Balance%2Bof%2BPayments%2BStatisticss/
- Official monthly detailed presentation PDF: https://www.tcmb.gov.tr/wps/wcm/connect/2c897137-850e-4d15-9a2a-c0d4735d9986/bop.pdf?MOD=AJPERES
- Official data ZIP locator from landing page: https://tcmb.gov.tr/wps/wcm/connect/08454646-62d8-4188-bfbe-1c8c01d83fc4/bop.zip?MOD=AJPERES
- The September 2026 detailed presentation gives monthly observations in USD million for 2026 April, May and June.
- Table 2 rows:
  - 2.1 Net acquisition of financial assets: April 2,368; May 1,266; June 2,115 USDm.
  - 2.2 Net incurrence of liabilities: April 6,334; May -1,802; June 4,651 USDm.
- Q2 aggregation is the arithmetic sum of the three monthly flows; no FX conversion or sign transform is applied.

## Q2 reconciliation
| Leg | TCMB April | TCMB May | TCMB June | TCMB Q2 sum (USDm) | IMF Q2 (USDm) | IMF − TCMB (USDm) | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | 2,368 | 1,266 | 2,115 | 5,749 | 5,749 | 0 | PASS at displayed precision |
| Portfolio liabilities / L_NIL_T | 6,334 | -1,802 | 4,651 | 9,183 | 9,270 | +87 | REVIEW / NOT PASS |

The asset leg matches exactly at the national source's displayed USDm precision. Liability residual +87 USDm exceeds whole-million display rounding. No tolerance widening, fitted adjustment, netting or imputation is permitted.

## Vintage and revision policy
- TCMB's official BOP revision policy states that, when disseminating the current month's data except December, the current year's data and previous year's monthly data (for items other than specified external-debt series) are subject to revision. December releases subject the previous five years to retrospective revision; large-scale revisions may also revise prior years with public notice.
- Thus TCMB Q2 monthly values in the September 2026 data vintage are potentially revised relative to earlier vintages. The current official data ZIP and PDF are linked from the same landing page, but the ZIP timed out through the available browser; its bytes, hash, and workbook/CSV revision metadata are NOT_INSPECTED.
- IMF exact observations were retrieved 2026-11-19, but no source-vintage identity bridge tying the IMF Q2 liability observation to the same TCMB September vintage was established. The 87m discrepancy cannot be attributed to revision without the exact source vintages and revision record.

## Acceptance matrix
- Existing IMF exact receipt: PASS.
- TCMB official source locator / September 2026 monthly detailed table: PASS.
- Q2 portfolio asset aggregation: PASS; matches IMF at displayed precision.
- Q2 portfolio liability aggregation: REVIEW / NOT PASS; USD 87m residual.
- Exact same-vintage identity: NOT_ESTABLISHED.
- TUR full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Retrieve and hash the exact TCMB September 2026 data ZIP through a supported transfer route; inspect its data files, revision/vintage metadata and Q2 asset/liability observations. Compare its exact liability observation with the existing IMF raw receipt and seek a dated revision bridge. If the residual remains unexplained, preserve TUR PARTIAL and advance to the next eligible cohort country. No new IMF query or cohort rebuild.

## Protected invariants
No aggregation across countries, no netting, imputation, forward-fill, synthetic data, silent sign transform, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.


## 2026-11-20 — August-to-September TCMB PDF vintage cross-check
- Follow-up preflight: re-fetched Master Continuity Ledger, GCR priority queue, TUR detailed report and adjacent POL/SAU/CHN blocker reports. Reused the prior exact IMF artifact; no duplicate IMF request or data panel rebuild.
- Inspected two distinct official TCMB monthly PDF snapshots: August 2026 PDF (official URL: https://www.tcmb.gov.tr/wps/wcm/connect/2c897137-850e-4d15-9a2a-c0d4735d9986/bop.pdf?CACHEID=ROOTWORKSPACE-2c897137-850e-4d15-9a2a-c0d4735d9986-mJkOjvD&MOD=AJPERES) and September 2026 PDF (official URL: https://www.tcmb.gov.tr/wps/wcm/connect/2c897137-850e-4d15-9a2a-c0d4735d9986/bop.pdf?CACHEID=ROOTWORKSPACE-2c897137-850e-4d15-9a2a-c0d4735d9986-mVuqob0&MOD=AJPERES).
- August snapshot Table 1 reports Q2 monthly portfolio assets 2,368 / 1,266 / 2,115 USDm and liabilities 6,334 / -1,802 / 4,651 USDm. September snapshot Table 1 reports the same monthly values. September Table 1 marks the table provisional. August PDF table lines 48–49 and September PDF lines 40–41 show the Q2 component rows; detailed table column headers explicitly identify April, May, June.
- Recomputed Q2 sums in both snapshots: assets 5,749 USDm; liabilities 9,183 USDm. Against existing IMF Q2 exact values assets 5,749 and liabilities 9,270 USDm, asset residual 0 and liability residual +87 USDm. The +87m discrepancy persists unchanged across the two TCMB PDF snapshots; no August-to-September revision of these Q2 rows is observed in these PDFs.
- This is a limited two-snapshot comparison, not proof of the complete revision history or exact source-vintage identity. The September data ZIP bytes/hash and row-level revision metadata remain NOT_INSPECTED because the official ZIP endpoint timed out. Do not infer the cause of the discrepancy or mark same-vintage PASS.
- Updated status: TUR asset leg PASS; liability leg REVIEW / NOT PASS; full national dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next exact action: obtain the September 2026 official ZIP through a supported transfer route, inspect raw data/vintage fields, and compare to IMF raw receipt. If unavailable, retain blocker and advance to another cohort member.
