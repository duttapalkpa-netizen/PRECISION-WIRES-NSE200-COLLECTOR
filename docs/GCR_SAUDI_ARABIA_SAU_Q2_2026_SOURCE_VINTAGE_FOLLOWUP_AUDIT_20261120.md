# Saudi Arabia SAU Q2-2026 source-vintage follow-up audit — 2026-11-20

Status: **PARTIAL / NOT PASS**. The existing SAMA-vs-IMF two-leg numeric comparisons remain PASS at published rounding, but exact same-vintage identity remains NOT_ESTABLISHED. No new IMF query or panel rebuild was performed.

## Progress log and preflight
- Re-fetched the current Master Continuity Ledger, GCR priority queue, SAU reconciliation report and CHN access audit before work.
- Excluded completed SAU national table extraction, IMF exact-key retrieval, arithmetic and report correction.
- Investigated only the open dependency: whether a later official SAMA Q2-2026 portfolio observation/revision or dated revision record is publicly evidenced.

## Official source evidence
1. SAMA Monthly Bulletin Statistics landing page: https://sama.gov.sa/en-US/Statistics/Pages/MonthlyStatistics.aspx
   - Search/index evidence identifies the September 2026 bulletin as published 29 October 2026.
2. SAMA Advanced Release Calendar: https://sama.gov.sa/en-US/Statistics/pages/advancedreleasecalendar.aspx
   - The monthly bulletin calendar lists 29 October for October 2026 data and 29 November for November 2026 data. As of 2026-11-20, the November-dated release is still in the future.
3. September 2026 Monthly Statistical Bulletin, official PDF:
   https://www.sama.gov.sa/en-US/Statistics/MonthlyStatistics/Monthly_Statistical_Bulletin_For_Sep_2026.pdf
   - Table 1, Balance of Payments, Contd.6, Q2 2026 portfolio asset/liability rows remain explicitly marked e = Estimate.
   - The existing reconciled values remain: assets +9,664 USDm; liabilities +6,381 USDm; portfolio balance +3,283 USDm.
4. IMF Dissemination Standards Bulletin Board metadata for Saudi Arabia:
   https://dsbb.imf.org/sdds/dqaf-base/country/SAU/category/EXD00
   - Metadata describes the general BOP revision practice as usually three months after the reference quarter and published on SAMA website / Monthly Statistical Bulletin.
   - It also states no public revision studies/analyses are made. This general schedule is not proof that the specific Q2-2026 portfolio legs have been revised.

## Decision
- Existing SAMA↔IMF numerical asset comparison: PASS at ±0.5 USDm whole-million display rounding (prior report).
- Existing SAMA↔IMF numerical liability comparison: PASS at ±0.5 USDm whole-million display rounding (prior report).
- SAMA Q2-2026 source vintage: explicitly Estimated (e).
- Later public Q2-2026 revised portfolio legs / dated revision snapshot: NOT_FOUND in the official public material inspected in this audit; this is a bounded search result, not proof that no internal or future revision exists.
- Exact SAMA↔IMF same-vintage identity: NOT_ESTABLISHED.
- SAU full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next action
Preserve SAU as PARTIAL and advance to the next eligible country in the already fixed 63-country Q2 both-leg cohort using the existing IMF exact-key sample. Do not rebuild the cohort, issue duplicate IMF queries, or treat the general three-month revision schedule as evidence of a particular revised value.

## Protected invariants
No aggregation, netting, imputation, forward-fill, synthetic observations, silent sign transform, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
