# GCR — Armenia (ARM) Q2-2026 CBA BOP XLS source and stock/flow boundary
Date: 2026-11-21 (Asia/Kolkata)
Status: PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Progress log / selection
- Reopened Master Priority Queue, Master Continuity Ledger and fixed immutable 63-country Q2 dual-leg cohort before selecting ARM. ARM is a cohort member; repository inventory had no dedicated ARM Q2-2026 national portfolio flow dual-leg report. No IMF re-query and no cohort rebuild.
- Selected because CBA's official external-sector page exposes a direct BPM6 Balance of Payments XLS time-series file.

## Official national source and exact retrieval boundary
- CBA legacy official External Sector Statistics page states CBA compiles Armenia's BOP, IIP and external debt and lists separate BPM6 datasets.
- Exact official BOP workbook link: https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls
- Browser retrieval failed with 400 Unsupported content-type: application/vnd.ms-excel. Direct container download also failed. Workbook bytes, sheets, cells and SHA-256 were not captured.
- CBA BOP metadata: USD millions, quarterly/annual, BPM6; transactions between residents and non-residents over a period; residency, accrual and double-entry principles; annual revisions generally at end-June, mainly current year.
- CBA methodology notes record 2026 revisions to BOP years 2022–2025 for goods/imports, insurance/freight services and telecommunications/computer/information services, and 2024–2025 compensation/personal transfers. This is not evidence that portfolio lines were unchanged.

## Q2-2026 observations — strict stock/flow separation
- Armstat NSDP (last update 20-Nov-2026) shows Q2-2026 BOP flow aggregates in USDm: current account -749.7; capital account +13.2; financial account -421.4; direct investment -287.5; financial derivatives +2.6; other investment -235.0; reserve assets +357.0. The visible NSDP summary does not expose a portfolio investment flow line. This is not evidence of zero portfolio transactions.
- The same NSDP separately shows Q2-2026 IIP END-OF-PERIOD stocks: portfolio investment assets USD2,131.2m and liabilities USD2,526.7m. These are positions/stocks, not BOP transaction flows; excluded from portfolio-flow reconciliation.
- CBA metadata distinguishes BOP transactions over a period from IIP point-in-time positions. CBA calendar says BOP is quarterly/annual and released by last working day of third month after period; Armstat calendar lists Q2/26 BOP release 30-Sep-2026.
- IMF DSBB metadata says Armenia disseminates BOP in analytical or standard-component format; Financial Account includes direct, portfolio, derivatives, other investment and reserve assets. This establishes classification, not Q2 values.

## Existing archived IMF rows — reused only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- ARM Q2-2026 A_NFA_T: OBS_VALUE=-206248729.725102; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- ARM Q2-2026 L_NIL_T: OBS_VALUE=52279059.5905749; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Raw values/attributes retained. No conversion, sign transform, or IMF re-query.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / IMF Q2 both-leg availability | PASS (roster only) |
| Official CBA BPM6 BOP dataset link | PASS |
| Exact official BOP XLS bytes / SHA-256 | NOT_CAPTURED |
| Q2 national portfolio asset/liability flows | NOT_CAPTURED |
| Q2 IIP portfolio stocks | CAPTURED but EXCLUDED from flow test |
| National sign/scale and detailed portfolio taxonomy | NOT_ESTABLISHED |
| Same-vintage bridge | NOT_ESTABLISHED |
| Separate-leg numerical comparison | NOT_DONE |
| ARM full validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Recover the exact official CBA XLS via supported spreadsheet/browser download or owner-side save; preserve original bytes, retrieval UTC, URL, response metadata and SHA-256.
2. Inspect workbook sheets and extract Q2-2026 portfolio assets and liabilities separately; do not use IIP stocks.
3. Verify workbook vintage/revision annotations and national sign convention; compare separate legs against existing archived IMF raw rows without unapproved transformation.
4. If XLS remains inaccessible, retain ARM PARTIAL and advance to next eligible cohort member. Do not repeat the same unsupported XLS fetch.

## Protected invariants
₹0; official/free sources only; no synthetic data; no IIP stock as BOP flow; no account aggregate as portfolio proxy; no unsupported zero assumption; no unapproved sign/scale transform; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- CBA official external sector page: https://old.cba.am/en/sitepages/statexternalsector.aspx
- Exact CBA BOP XLS: https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls
- CBA BOP metadata: https://www.cba.am/en/statistics/metadata/206
- CBA methodological notes: https://www.cba.am/en/statistics/meth-notes/205/
- CBA release calendar: https://www.cba.am/en/statistics/advance-release-calendar/197
- Armstat NSDP: https://www.armstat.am/nsdp/
- Armstat release calendar: https://www.armstat.am/nsdp/arc/
- IMF DSBB Armenia BOP metadata: https://dsbb.imf.org/sdds/dqaf-base/country/ARM/category/BOP00