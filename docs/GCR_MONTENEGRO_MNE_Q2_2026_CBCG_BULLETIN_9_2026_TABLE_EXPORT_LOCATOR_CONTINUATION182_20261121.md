# Montenegro (MNE) Q2-2026 — CBCG Bulletin 9/2026 table-export locator audit (Continuation 182)
Date: 2026-11-21 (Asia/Kolkata)
Decision: FIXED COHORT ROW VERIFIED; DISTINCT OFFICIAL CBCG BULLETIN 9/2026 PDF RETRIEVED AND METHODOLOGY REVIEWED; TABLE 5.1–5.4 DOWNLOAD AFFORDANCE IDENTIFIED BUT PAYLOAD/EXACT PORTFOLIO LEGS NOT CAPTURED; MNE PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and duplicate prevention
- Re-fetched Master Ledger, Priority Queue, Historical Registry and MNE C180 source-boundary report before work. Existing CBCG BOP ZIP and MONSTAT NSDP SDMX XML/Browse routes were not retried; their HTTP 400 / timeout failures remain closed for the same transfer method.
- Reused fixed cohort file `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, SHA-256 `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- Exact row verified: `MNE,Montenegro,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`.
- No cohort rebuild, IMF re-query or panel modification.

## 2. New official CBCG publication route
- Official CBCG Bulletin archive page: https://cbcg.me/en/publications/regular-publications/cbcg-bulletin
- Bulletin 9/2026 official PDF: https://cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf
- PDF is 65 pages. Its balance-of-payments section begins on printed page 55 / PDF page 54 and explicitly advertises “Tables 5.1–5.4 — download tables”. The English methodology note states BOP data are quarterly and reported in euros; original-currency source data are converted using CBCG middle rates at transaction day, monthly and annual average rates, and period-end daily rates for valuation of transactions whose difference is monitored.
- The bulletin says its published data are preliminary and may be revised when final data become available.
- The methodological note states direct and portfolio investments are monitored using foreign payment operations statistics (ITRS) and surveys.
- This is a distinct publication route from the C180 archive ZIP and NSDP SDMX XML. However, the PDF text itself does not contain the separate Q2-2026 portfolio asset/liability numeric rows; the “download tables” text is only an affordance, not a downloaded workbook or evidence of the values.

## 3. What is and is not proven
| Gate | Status |
|---|---|
| Fixed cohort MNE Q2 both-leg presence | PASS (exact row verified; fixed cohort unchanged) |
| Official CBCG Bulletin 9/2026 PDF retrieved/read | PASS |
| Bulletin BOP table group locator 5.1–5.4 | PASS (locator only) |
| Quarterly frequency / EUR reporting | PASS (methodology) |
| Transaction-day FX principle | PASS (methodology) |
| Preliminary/revision warning | PASS |
| Exact Q2-2026 portfolio asset value | NOT_CAPTURED |
| Exact Q2-2026 portfolio liability value | NOT_CAPTURED |
| Downloadable Table 5.1–5.4 bytes / URL / MIME / SHA-256 | NOT_CAPTURED |
| Exact row labels / sign convention for separate portfolio legs | NOT_ESTABLISHED |
| IMF-national numeric comparison | NOT_DONE |
| Same-vintage bridge | NOT_ESTABLISHED |
| MNE national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Next bounded action
- Resolve the Bulletin 9/2026 PDF's linked “Tables 5.1–5.4 — download tables” annotation or locate the same four tables through a distinct official CBCG table-export interface. Capture exact workbook/CSV bytes, URL, MIME, timestamp, SHA-256, sheet/table metadata, Q2-2026 period, and separate portfolio asset/liability rows; then compare separately to the already archived IMF rows.
- Do not infer the table payload from the PDF text, do not use IIP positions or net-only totals, and do not retry the same C180 ZIP/XML/Browse transfer paths. If the official table-export affordance cannot be resolved with a supported browser/download method, preserve PARTIAL and move to the next eligible cohort country.

## 5. Protected invariants
₹0; free official sources only. No synthetic values, fabricated timestamps, FX conversion without source-supported method, net-to-leg back-solving, stock-as-flow, IMF re-query, cohort rebuild, aggregate authorization or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
