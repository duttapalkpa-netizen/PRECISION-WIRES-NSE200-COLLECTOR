# Poland (POL) Q2-2026 — NBP official USD dual-leg publication search closure (Continuation 181)
Date: 2026-11-21 (Asia/Kolkata)
Decision: CONTINUITY PREFLIGHT PASS; PRIOR POL PLN LEGS / TRANSACTION-DATE FX RULE REUSED; DISTINCT OFFICIAL PUBLICATION SEARCH PERFORMED; NO OFFICIAL CURRENT Q2-2026 USD-DENOMINATED PORTFOLIO ASSET/LIABILITY FLOW TABLE FOUND IN THE SEARCHED PUBLIC NBP SURFACES; POL REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight
- Re-fetched current Master Ledger (blob `3db69bed5715e72a160c84df97b93eae7f2703af`), Priority Queue (`8e6724d5a846f9c9e1fac47e26c73526cc6d84a9`), Historical Registry (`9199e036d6a778863bfed0ad5081f5cbba807868`) and POL Continuation 165 report (blob `8ad43db8378856aba7ace4cb5e75a802c4633a51`).
- Prior POL national values and transaction-date FX rule retained: portfolio assets 24,144 mn PLN; liabilities 70,910 mn PLN; NBP forms PW-AIN/PW-RIN establish transaction-date valuation principle. Quarter-end FX is not accepted for flows.
- Excluded repeat work: no re-download of already blocked NBP Q2 PDF/XLSX routes, no recalculation using daily FX averages, no new IMF query, no cohort rebuild.
- Prior report's unresolved gates remain: official USD-matched Q2 dual-leg aggregate NOT_CAPTURED; transaction-level date/currency amounts NOT_CAPTURED; same-vintage bridge NOT_ESTABLISHED.

## 2. New bounded official-source search
- Searched current NBP public English statistical pages and current Balance of Payments table surfaces for a separate USD-denominated Q2-2026 portfolio assets/liabilities transaction table.
- Official current NBP English BOP PDF locator: https://static.nbp.pl/dane/bilans-platniczy/bopa_en.pdf . Search-indexed table labels the unit as million PLN and its latest columns are quarterly 2026 values; it is not a USD dual-leg table.
- Official NBP reporting/publication list: https://sprawozdawczosc.nbp.pl/pages/information/publication/common-publication-list.jsf . The visible public list contains BOP reporting instructions and notices, but no matching Q2-2026 USD portfolio-flow publication was identified in this bounded search.
- NBP public Table A exchange-rate page/API offers exchange rates; it does not provide the underlying transaction date/currency weights needed to convert aggregate PLN flow totals into USD. NBP Web API documentation covers currency exchange rates and historic quotations, not portfolio transaction amounts.
- Historical NBP statistical annexes surfaced in search contain older cash-basis USD tables; they are not current Q2-2026 BPM6 matched dual-leg publications and are rejected as substitutes.
- This is a bounded search result, not proof that no such table exists anywhere in NBP systems. No exact USD Q2 national observation was located, no raw bytes/hash captured, and no numeric conversion performed.

## 3. Acceptance matrix
| Gate | Status |
|---|---|
| Master Ledger / Queue / Registry / POL C165 preflight | PASS |
| Prior national Q2 portfolio asset row | PASS (reused; 24,144 mn PLN) |
| Prior national Q2 portfolio liability row | PASS (reused; 70,910 mn PLN) |
| Transaction-date FX principle | PASS (reused; official form examples) |
| New current official NBP USD dual-leg search | COMPLETED; no qualifying USD Q2 table located |
| Current NBP BOP table unit | PLN million; not USD |
| Transaction-level currency/date weights | NOT_CAPTURED |
| Matched official USD Q2 portfolio asset/liability values | NOT_CAPTURED |
| Q2 PDF raw bytes/SHA-256 | NOT_CAPTURED |
| NBP–IMF same-vintage bridge | NOT_ESTABLISHED |
| Cross-currency numeric comparison | NOT_DONE |
| POL national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 4. Rejected substitutes / next action
- Do not multiply or divide quarterly PLN totals by daily, monthly, quarterly-average, or quarter-end FX without official transaction-date/currency weights or an official matched USD publication.
- Do not use IIP stocks, current FX quotations, old cash-basis USD annexes, or net-only summaries as Q2-2026 BOP portfolio dual legs.
- POL's USD conversion route is now bounded for the searched public pages. Reopen only if a distinct official USD Q2-2026 dual-leg release or transaction-level source with currency/date values and matching vintage appears.
- Next priority: move to the next fixed-cohort country with an unexhausted official national route after exact repository/registry preflight. No cohort rebuild or IMF re-query.

## 5. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, unsupported FX conversion, net-to-leg back-solving, stock-as-flow, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
