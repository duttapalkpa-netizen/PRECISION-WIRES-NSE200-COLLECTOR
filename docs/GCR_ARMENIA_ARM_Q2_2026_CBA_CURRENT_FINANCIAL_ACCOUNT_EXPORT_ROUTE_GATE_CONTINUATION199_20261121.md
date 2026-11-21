# Armenia (ARM) Q2-2026 — CBA current Financial Account export-route gate (Continuation 199)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
NEW CURRENT-DOMAIN CBA EXPORT ROUTE LOCATED; EXPORT ENDPOINT TIMED OUT; NO Q2 NATIONAL PORTFOLIO DUAL-LEG VALUES OR BYTES CAPTURED. ARM remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. This is a distinct route-discovery result, not successful data retrieval. The older CBA legacy XLS route documented in C143 is not retried.

## 1. Mandatory continuity preflight and duplicate rejection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable cohort file and full ARM C143 report before selecting this bounded follow-up.
- Pre-task blob SHAs:
  - Ledger: e3a744f0f006f7cafa65c1ff858a2f603899ee63
  - Priority Queue: 02e9839d7a7251793b72285aede298f0c82ecf19
  - Historical Registry: b342a4c6770f7be277140f967c08a9a159415c4f
  - Fixed cohort CSV: 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8
  - ARM C143: b13a5dea3b53358c27b181e6591e7ecd55cbcb53
- The cohort file is the existing immutable 63-country Q2-2026 both-leg roster. ARM is present with A_NFA_T and L_NIL_T panel entries; no cohort rebuild and no IMF request.
- C143 already tested the legacy workbook URL https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls; browser returned 400 unsupported Excel MIME and direct container download failed. This exact legacy XLS route is closed and was not retried.
- C143 already captured Q2 IIP portfolio asset/liability positions; these are stocks and are explicitly excluded from BOP transaction-flow validation. No re-extraction or stock substitution was performed.

## 2. Distinct current CBA official portal route
- Current official CBA external-sector index: https://www.cba.am/en/statistics/statistics-of-the-external-sector/21
- It links a separate Financial Account dataset page: https://www.cba.am/en/statistics/financial-account/275
- The current Financial Account page visibly exposes three selector controls and date-range fields, Search, Export all data, Export filtered data, and XLSX, XML and JSON format choices.
- Exact Export all data target resolved by the official link: https://www.cba.am/en/statistics/financial-account/275/export-all/
- The exact export target was opened once through the supported page-link route; retrieval returned a timeout. No file/body, HTTP response headers, content type, byte count, series list, Q2 rows or SHA-256 were returned.
- This route is distinct from the legacy C143 XLS URL and represents a newer current-domain export interface. Page-level controls do not prove the target dataset contains the required portfolio asset/liability transaction series.
- Dynamic selector values and filtered export behavior were not executed. No unsupported UI action or URL guess was attempted.

## 3. Official metadata and period boundary
- CBA BOP metadata: https://www.cba.am/en/statistics/metadata/206
  - Table: Balance of Payment of RA; source: Central Bank of RA.
  - Currency: USD; unit: millions; periodicity: quarterly and annual.
  - Timeliness: last working day of the third month after the reference period.
  - Compilation: BPM6; transactions between residents and non-residents; residency, accrual and double-entry principles.
  - Revision: annual external-sector revisions generally at end-June, mainly current-year data; some items receive additional review.
- Official Armstat NSDP: https://www.armstat.am/nsdp/ . The page states its last update was 20-Nov-2026 and shows Q2-2026 BOP aggregates. The visible summary has current account, capital account, total financial account, direct investment, derivatives, other investment and reserve assets; it does not show a separate portfolio-investment BOP flow line. This is not evidence that portfolio transactions are zero or absent from the detailed CBA dataset.
- The same NSDP reports Q2-2026 end-of-period IIP portfolio asset/liability stocks. These remain excluded from BOP transaction-flow validation.

## 4. Existing IMF archive reuse — no new query
- Reuse the exact ARM Q2 rows already documented in C143 and the immutable raw panels; no IMF GET or re-extraction:
  - A_NFA_T: raw OBS_VALUE -206248729.725102, UNIT=USD, SCALE=6, quarterly, DERIVATION_TYPE=O.
  - L_NIL_T: raw OBS_VALUE 52279059.5905749, UNIT=USD, SCALE=6, quarterly, DERIVATION_TYPE=O.
- Raw values and SCALE are retained unchanged. No scale conversion, sign transform or numeric comparison admitted because national portfolio transaction legs are still NOT_CAPTURED.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / C143 preflight | PASS |
| ARM fixed-cohort membership / existing IMF two-leg panel rows | PASS (reused) |
| Prior legacy CBA XLS route fingerprint reviewed | PASS — no repeat |
| Distinct current CBA Financial Account page located | PASS — locator |
| XLSX/XML/JSON export controls visible | PASS — UI affordance only |
| Exact current-domain export-all target identified | PASS — locator |
| Current export-all target retrieval | TIMEOUT |
| Q2-2026 national portfolio asset transaction value | NOT_CAPTURED |
| Q2-2026 national portfolio liability transaction value | NOT_CAPTURED |
| Export bytes / headers / byte count / receipt timestamp / SHA-256 | NOT_CAPTURED |
| Exact financial-account series identity / period selector / vintage | NOT_ESTABLISHED |
| Separate-leg comparison to archived IMF rows | NOT_DONE |
| ARM national validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Next bounded action and no-repeat rule
- Do not retry the same current-domain export-all timeout through the same retrieval surface in this cycle; do not retry the legacy XLS URL from C143.
- Reopen only if an actually supported, distinct route becomes available (for example, a successful owner-side official export file or a different official machine-readable endpoint documented by CBA). If an official workbook/export is supplied, preserve untouched bytes, exact URL/source, retrieval UTC, headers, byte count and SHA-256 before parsing.
- A future export must explicitly identify Q2-2026 portfolio investment net acquisition of financial assets and net incurrence of liabilities, native USD-million unit, sign, preliminary/revision vintage and coverage. Do not treat the BOP summary's missing portfolio row as zero; do not use IIP stocks, financial-account aggregate or net-to-leg inference.
- After recording this distinct route boundary, advance to the next eligible unvalidated fixed-cohort member with a static official source that is retrievable in the current session. Apply the C198 Execution-Mode Gate before selection.

## 7. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, unsupported sign/scale conversion, stock-as-flow, net-to-leg back-solving, IMF re-query, cohort rebuild, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.