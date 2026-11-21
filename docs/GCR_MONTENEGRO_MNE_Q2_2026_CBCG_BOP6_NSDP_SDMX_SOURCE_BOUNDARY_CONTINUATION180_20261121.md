# Montenegro (MNE) Q2-2026 — CBCG BPM6 / NSDP SDMX source-boundary audit (Continuation 180)
Date: 2026-11-21 (Asia/Kolkata)
Decision: FIXED-COHORT / REPOSITORY DUPLICATE CHECK PASS; OFFICIAL CBCG BPM6 QUARTERLY BOP PAGE AND Q2 RELEASE CALENDAR PASS; OFFICIAL NSDP SDMX XML LOCATOR IDENTIFIED; CBCG ZIP AND NSDP BROWSE ROUTE NOT RETRIEVED BY CURRENT WEB TRANSFER; SDMX XML CONTENT NOT PARSED; NO SEPARATE Q2-2026 PORTFOLIO ASSET/LIABILITY VALUES CAPTURED; MNE PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and selection
- Re-fetched current Master Continuity Ledger (blob SHA `76fe53d83bd3b526df752d8aa955ac75f08830a5`), GCR Priority Queue (`2fa85104ae3a7b1b7d4d4b84481e3ce7e08b8e97`), Historical Task Registry (`781044abfc3805c4131dca2534f7d7a38d8b79e4`) and MNG C179 report (`bd6ef39ac77e4e82b28053a3651d618777eb7e3e`).
- MNG PxWeb API task remains PARTIAL and its same inaccessible API endpoint is not retried. MNG table source and period metadata retained.
- Searched repository for MNE/Montenegro Q2-2026 portfolio assets/liabilities and dedicated dual-leg reports; no prior dedicated MNE report found.
- Selected MNE from fixed cohort for a new official route. Fixed 63-country cohort CSV remains SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; MNE exact cohort row was not separately extracted in this bounded pass, so membership confirmation is recorded as pending recheck before any numeric comparison. No cohort rebuild or IMF re-query.

## 2. Official CBCG BOP source and release timing
- Official Central Bank of Montenegro (CBCG) Balance of Payments page: https://www.cbcg.me/en/statistics/statistical-data/international-economic-relations/balance-of-payments
- CBCG defines BOP as transactions between residents and non-residents, reports in EUR quarterly, and states BPM6 applies to data from 2010 onward. Its financial account is presented using net acquisition of financial assets and net incurrence of liabilities.
- Page reports Updated: 19 November 2026 and links “Balance of Payments of Montenegro in accordance with BPM6 (2010-2026)”.
- Clicking the linked archive resolved to official ZIP `https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip`; retrieval returned HTTP 400 unsupported content-type application/zip. No ZIP bytes, contents, workbook sheets, hashes or Q2 observations captured.
- Official CBCG 2026 statistical dissemination calendar reports Q2-2026 BOP release date 19-Aug-2026. MONSTAT 2026 annual official statistics plan independently lists the same Q2-2026 release date and CBCG as producer.

## 3. Official NSDP alternate locator and transfer boundary
- Official MONSTAT National Summary Data Page says its linked data correspond to IMF DSBB and lists Balance of Payments with Browse Data and Download in SDMX.
- Browse Data resolves to CBCG legacy URL `https://www.cb-cg.org/eng/index.php?mn1=statistics&mn2=international_economic_relations&mn3=balance_of_payments`; request timed out.
- Download in SDMX resolves to exact official DSBB XML locator `https://dsbb.imf.org/xml/MNE/BOP6_Montenegro.xml`; retrieval returned HTTP 400 unsupported content-type text/xml. This is a distinct locator, not a parsed or validated dataset.
- MONSTAT BOP metadata describes BOP as covering portfolio investment, BPM6, quarterly from 2005 onward, with unit EUR thousands and data available publicly in aggregate form. Metadata last updated 21-Nov-2025; it is descriptive metadata, not proof of Q2-2026 release vintage.
- CBCG Bulletin 1/2026 methodology says BOP data are quarterly in EUR; original-currency recalculation can use transaction-day CBCG middle rates, monthly/annual middle averages, and period-end daily rates for monitored valuation differences. It also says direct and portfolio investments are monitored from ITRS data and surveys. This methodological context does not by itself validate Q2-2026 national dual-leg values or their revision vintage.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Current Master Ledger / Queue / Registry / C179 preflight | PASS |
| No dedicated prior MNE Q2-2026 national dual-leg report found | PASS |
| Official CBCG BPM6 quarterly BOP source identified | PASS |
| CBCG quarterly EUR reporting and net asset/liability presentation confirmed | PASS |
| Official Q2-2026 release calendar date 19-Aug-2026 | PASS |
| CBCG BPM6 archive locator found | PASS; ZIP bytes NOT_CAPTURED |
| Official MONSTAT NSDP BOP row identified | PASS |
| Distinct official SDMX XML locator identified | PASS; XML bytes NOT_CAPTURED |
| NSDP Browse Data legacy CBCG endpoint retrieval | BLOCKED / timeout |
| Separate Q2-2026 portfolio asset observation | NOT_CAPTURED |
| Separate Q2-2026 portfolio liability observation | NOT_CAPTURED |
| Raw national export bytes / headers / SHA-256 | NOT_CAPTURED |
| MNE fixed cohort exact-row membership | NOT_RECHECKED in this bounded pass |
| Sign/scale/vintage bridge and IMF comparison | NOT_DONE |
| Full MNE national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Rejected substitutes and next action
- Rejected IIP assets/liabilities and external-debt series as BOP transaction flows.
- Rejected annual/forecast portfolio values and net-only financial-account summaries as dual-leg evidence.
- No net-to-leg back-solving, no fabricated SDMX/XML payload, no unverified sign or FX transformation.
- Next: if a supported file transfer becomes available, retrieve the official CBCG ZIP and DSBB XML, preserve original bytes, headers, retrieval UTC and SHA-256; parse only after verifying table/series metadata and Q2-2026 rows. Before numeric comparison, verify MNE's exact fixed-cohort row and reuse archived IMF raw values only. If transfer remains unsupported, do not repeat identical ZIP/XML clicks; move to next fixed-cohort member after preflight.

## 6. Protected invariants
₹0; official/free sources only. No synthetic values/timestamps, no IMF re-query/cohort rebuild, no net-to-leg back-solving, no IIP stocks as BOP flows, no unsupported sign/scale/FX conversion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
