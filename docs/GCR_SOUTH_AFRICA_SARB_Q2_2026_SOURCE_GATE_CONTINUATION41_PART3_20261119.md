# GCR South Africa — SARB Q2-2026 official source gate
Date: 2026-11-19
Continuation: 41, Part-3
Scope: official national-source availability and definition check for ZAF in the already archived 2026-Q2 dual-leg cohort. Metadata/source-family validation only; no numeric crosswalk or aggregate admission.

## Progress log
- Reused the existing candidate roster: ZAF is in the 63-country 2026-Q2 cohort with both IMF panel entries A_NFA_T and L_NIL_T present.
- Located SARB Quarterly Bulletin September 2026, published 29 September 2026, covering Q2-2026 and containing external-economic-accounts statistical tables.
- SARB bulletin narrative states Q2-2026 net financial-account capital flow switched to an inflow of R1.9 billion from an outflow of R23.1 billion in Q1; on a net basis direct investment, other investment and reserve assets were inflows, while portfolio investment and financial derivatives were outflows.
- SARB official September 2026 quarterly-bulletin XLSX download index identifies the Q2 release archive as 04Kbp5-Balance-of-Payments-September-2026-updated.zip. K1 is quarterly frequency.
- SARB June 2026 IIP publication is a separate end-June position source and must not be used as a BOP transaction-flow substitute.

## Official evidence
1. SARB September 2026 Quarterly Bulletin (published 2026-09-29): https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/quarterly-bulletin-publications/2026/september
2. SARB September 2026 XLSX data archive index (published 2026-09-29): https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/download-information-from-xlsx-data-files/2026/-download-information-from-xlsx-data-files
3. SARB June 2026 IIP publication: https://www.resbank.co.za/en/home/publications/publication-detail-pages/international-investment-position/2026/SouthAfricasquarterlyinternationalinvestmentpositionIIP
4. IMF BOP dataset overview: https://data.imf.org/en/datasets/IMF.STA%3ABOP
5. IMF operational guidance on BOP/IIP methodology: https://www.elibrary.imf.org/abstract/journals/007/2026/001/article-A001-en.xml

## Gate assessment
- ZAF in candidate cohort, both panel entries present: PASS (panel availability only).
- SARB official Q2-2026 BOP source family located: PASS.
- Official narrative confirms net portfolio investment outflow in Q2: PASS as a high-level directional cross-check only.
- Exact A_NFA_T and L_NIL_T national line-item mapping, units, sign convention, asset/liability split and observation values: NOT_YET_VALIDATED. Narrative net flow cannot validate the two gross legs.
- Exact release vintage / revision bridge for matching series: NOT_YET_VALIDATED.
- National-source validation for ZAF: PARTIAL / NOT PASS.
- 63-country GCR aggregate admission: NOT_AUTHORIZED.

## Exact next action
Download and inspect the official SARB archive 04Kbp5-Balance-of-Payments-September-2026-updated.zip; identify exact quarterly series/table codes for portfolio investment net acquisition of financial assets and net incurrence of liabilities (or exact national equivalents). Record unit, sign convention, Q2-2026 values, revision notes, source table IDs and vintage. Compare only like-for-like concepts; do not convert ZAR to USD or reverse signs without documented definitions and matching IMF metadata. If the archive is not directly retrievable, record the limitation and retain PARTIAL.

## Invariants
₹0; official/free sources only. No synthetic data, inferred unit conversion/sign flip, flow-stock substitution, or aggregation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
