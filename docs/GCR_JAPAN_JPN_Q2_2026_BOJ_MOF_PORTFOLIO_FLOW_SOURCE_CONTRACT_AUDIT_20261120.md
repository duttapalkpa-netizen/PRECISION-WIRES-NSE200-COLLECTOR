# Japan (JPN) Q2-2026 — BOJ/MOF Portfolio Flow Source Contract Audit
Date: 2026-11-20 (Asia/Kolkata)
Scope: bounded official-source contract audit for Japan's portfolio-investment flow and partner-economy dissemination as a major India market-transmission country. This is a research-only source gate; no data values are admitted in this report.

## Continuity preflight
- Re-fetched the current PRECISION-WIRES V11.3 Continuity & Acceptance Ledger (blob SHA `35de61d6439bf8280131980a6394cb2e6d5774b8`), GCR Master Priority Queue (blob SHA `8ba796fdf16176b28e3e8d2b1bc69a8c2ef0198b`) and Continuation 78 report (blob SHA `69597e2fbe40d859bfbccb4af165b6c10959c4a8`).
- Did not repeat CDSL archive, CDSL arithmetic, NSDL form inspection, BSE/NSE TRI rights, or any previously completed fixed-cohort country extraction.
- This Japan task is an independent India-transmission source-family gate; it does not alter or rebuild the fixed 63-country Q2-2026 IMF EMDE cohort.

## Official sources and verified contract
1. Bank of Japan (BOJ), “Balance of Payments Related Statistics (Data Based on the BPM6, January 2014 onward)”:
   https://www.boj.or.jp/en/statistics/br/bop_06/index.htm
   - BOJ states BOP is monthly flow data, including financial-account assets and liabilities and portfolio investment.
   - Portfolio Investment Assets/Liabilities include gross acquisitions/disposals and net transactions, with breakdowns by security type and other dimensions.
   - BOJ separately identifies Regional BOP as quarterly partner-economy data.
   - The BOJ description says portfolio-investment flows are available by counterparty economy for 45 economies; this is a distinct breakdown from the general 33-major-economy partner list.
   - Financial-account sign semantics: assets are net acquisition of financial assets; liabilities are net incurrence of liabilities. Gross asset/liability figures are also provided for portfolio investment. Preserve the two legs separately; do not net them or substitute portfolio balance.
   - Monthly preliminary BOP is released two months after the reference month; second preliminary data are released in Jan/Apr/Jul/Oct for the preceding quarter; annual revisions are released in April in subsequent years. Regional BOP is quarterly and released five months after quarter-end; annual revisions follow in May. Vintage must be stored per release, not silently overwritten.

2. Ministry of Finance Japan (MOF), Balance of Payments release schedule:
   https://www.mof.go.jp/english/policy/international_policy/reference/balance_of_payments/release_date.htm
   - The official CY2026 release schedule lists “Regional: 2nd quarter of CY2026” on 10-Nov-2026.
   - The same schedule lists the October 2026 monthly preliminary BOP release on 8-Dec-2026; do not confuse that future monthly release with the already scheduled Q2 regional release.
   - MOF's historical-data page links detailed portfolio investment assets/liabilities to BOJ Time-Series Data Search.

3. BOJ Time-Series Data Search:
   https://www.stat-search.boj.or.jp/ssi/docs/index_en.html
   - Official portal lists Balance of Payments [BP01] and a flat-file download facility.
   - BOJ API quick guidance (18-Feb-2026) states the API is public and can return JSON/CSV; monthly date labels are YYYY/MM and quarterly labels are YYYY/03, YYYY/06, YYYY/09, YYYY/12.
   - API user manual documents the `getDataLayer` route and CSV output for BP01 monthly data; its example is a different series/time window and is not treated as the Japan portfolio-series identifier.
   - BOJ main time-series page was current to 20-Nov-2026 and shows monthly BOP coverage through 2026/09. The visible main-table examples are current-account and financial-account net balance only, not portfolio asset/liability values.

## Important boundary
- The source family is official and has both the monthly portfolio asset/liability flow concept and quarterly partner-economy dissemination.
- The 10-Nov-2026 Q2 regional release date is verified, but the exact Q2 portfolio-by-partner rows, India row availability, series identifiers, values, units, and release-vintage bytes were not retrieved in this bounded task.
- Do not infer India-specific portfolio flow values from Japan's total BOP or total portfolio balance. Do not treat monthly total portfolio legs as India bilateral values.
- No API request was issued; no undocumented endpoint or series code was guessed. No raw payload, response headers, retrieval timestamp, or SHA-256 is claimed.
- This work does not establish a causal Japan→India market effect or any trading signal.

## Acceptance matrix
| Gate | Status |
|---|---|
| Official BOJ BPM6 BOP source identified | PASS |
| Monthly portfolio assets and liabilities concept identified | PASS |
| Asset/liability sign semantics recorded | PASS |
| Quarterly partner-economy BOP concept identified | PASS |
| Portfolio-flow partner coverage described by BOJ (45 economies) | PASS |
| Official Q2-2026 regional release date (10-Nov-2026) verified | PASS |
| BOJ public API / CSV capability documented | PASS |
| Exact Q2-2026 Japan portfolio-by-partner rows and India availability | NOT_DONE |
| Exact series IDs, units, values, raw bytes and SHA-256 | NOT_DONE |
| Same-vintage / revision bridge | NOT_ESTABLISHED |
| Japan→India causal transmission / event study | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next exact action
Open the official 10-Nov-2026 Q2 Regional BOP release and its linked BOJ/ MOF workbook or data table; inspect whether portfolio investment assets/liabilities are separately available for India as partner economy. Capture original bytes, HTTP metadata, retrieval UTC and SHA-256 before parsing. Record period, unit, sign, publication vintage and any revision notice. If the Q2 regional table does not contain the portfolio legs for India, retain NOT_AVAILABLE_IN_THIS_TABLE and use only the official 45-economy portfolio-by-counterparty series if its metadata explicitly identifies India. No guessed series code, no monthly-to-quarter aggregation until the monthly definitions and revisions are confirmed.

## Protected invariants
₹0 spend; official/free sources only; no synthetic observations, fabricated timestamps, unsupported FX conversion, forward-fill, net-only substitution, stock/flow mixing, or unverified country attribution. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, and fixed 63-country Q2-2026 IMF cohort unchanged. UNKNOWN is never PASS.
