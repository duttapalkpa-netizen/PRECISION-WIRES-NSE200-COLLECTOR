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


## Continuation 80 — official Q2-2026 Regional BOP attachment inspection (2026-11-20)
- Reopened current Master Continuity Ledger, GCR Master Queue and Japan Continuation 79 report before execution. Completed PASS work was not repeated.
- Followed the MOF release-date page's exact CY2026 Regional / 2nd quarter link (link 37) to the official PDF: https://www.mof.go.jp/policy/international_policy/reference/balance_of_payments/regional/rbp20260406.pdf .
- PDF cover identifies “Regional Balance of Payments for the 2nd quarter of 2026”, release date 10-Nov-2026, jointly MOF/BOJ. It is a 14-page PDF; table unit is 100 million yen.
- Inspected page 8 “Financial account (Assets)” and page 9 “Financial account (Liabilities)” both visually and through extracted table text. Each has a distinct Portfolio investment column and a named India row.
- India Q2-2026 portfolio investment asset cell on page 8 is displayed as an em dash (—), not a numeric observation. Preserve as reported dash / unavailable-or-not-reported; do not convert to zero.
- India Q2-2026 portfolio investment liability cell on page 9 is 7,526 (100 million yen), i.e. the source's displayed unit. No conversion to INR/USD performed.
- Thus the exact official quarterly partner-economy release does expose separate portfolio asset/liability columns and an India row, but only the liability leg is numerically populated in the inspected table. It cannot validate a full dual-leg India portfolio flow for Q2 from this release alone.
- The PDF was readable via official web document retrieval and page images, but byte-preserving download failed in the current execution environment. No local raw bytes, HTTP headers, retrieval UTC, file length, or SHA-256 are claimed. Citation/page-level visual inspection is evidence, not a raw-file archive.
- Status: official Q2 partner table + India row PASS; liability display extraction PASS; asset leg NOT_REPORTED_IN_THIS_TABLE (dash, not zero); dual-leg national validation PARTIAL / NOT PASS; raw-byte archive/hash NOT_DONE; same-vintage reconciliation NOT_ESTABLISHED; Japan→India causal transmission NOT_DONE; production NOT_AUTHORIZED.
- Next exact action: inspect the official BOJ portfolio-investment country-breakdown series (45 economies) for Q2-2026, specifically Portfolio Investment Assets, Country Breakdown and Portfolio Investment Liabilities, Country Breakdown, with India as partner. Use exact BOJ metadata/series IDs only; capture original CSV/XLSX bytes and SHA-256 before parsing. If the asset series has no India observation, retain the asset leg UNKNOWN and do not synthesize from totals.
- Protected invariants unchanged: ₹0 spend; no inferred zero, no netting, no unsupported currency conversion, no synthetic data, no change to Production Selector/RANKING_SCORE/+1 PRESSURE_FADE/CORE-672/Engines A–E/IPO-PLX V2/fixed 63-country IMF cohort. UNKNOWN is never PASS.


## Continuation 81 — BOJ 45-economy monthly portfolio country-breakdown verification (2026-11-20)
- Re-fetched the current Master Continuity Ledger, GCR queue and updated Japan report. Reused the Q2 Regional BOP India-row result; did not repeat the PDF page inspection.
- BOJ BPM6 source page explicitly defines Portfolio Investment Assets, Country Breakdown as transactions by economy of issuer and Portfolio Investment Liabilities, Country Breakdown as transactions by economy of transactor; each is monthly and covers 45 economies. Official partner-economy list marks portfolio investment country breakdown as 45 economies.
- Followed MOF official release-date page to June 2026 Portfolio Investment Assets/Liabilities preliminary PDF: https://www.mof.go.jp/policy/international_policy/reference/balance_of_payments/preliminary/bppi202606.pdf . Document title says June 2026 (Preliminary); 6 pages; table unit 100 million yen.
- Page 4 / section VI Portfolio Investment Assets, Country Breakdown, India row:
  Total acquisition 1,379; disposition 2,056; net -677.
  Equity and investment fund shares: acquisition 1,169; disposition 1,860; net -691.
  Long-term debt securities: acquisition 210; disposition 196; net 14.
  Short-term debt securities: dash across the displayed fields (preserve as dash, not numeric zero).
- Page 5 / section VII Portfolio Investment Liabilities, Country Breakdown, India row:
  Total acquisition 1,187; disposition 2,773; net -1,586.
  Equity and investment fund shares: acquisition 0; disposition 0; net 0.
  Long-term debt securities: acquisition dash; disposition 920; net -920.
  Short-term debt securities: acquisition 1,187; disposition 1,852; net -665.
- Table arithmetic checks for populated categories: Assets 1,169+210=1,379 acquisitions; 1,860+196=2,056 dispositions; -691+14=-677 net. Liabilities: 0 + dash + 1,187 and 0 + 920 + 1,852 / net 0 + (-920) + (-665) = -1,585, while published total net is -1,586; retain published total and classify the 1 (100 million yen) difference as displayed rounding/rounding residual pending exact source methodology. Do not overwrite published total. Note liabilities long-term debt acquisition is dash, not zero; arithmetic using dash as zero is only a display reconciliation, not a semantic assertion that the underlying value equals zero.
- June monthly values demonstrate that the BOJ 45-economy country-breakdown publication has India rows for both assets and liabilities. They are monthly preliminary figures, not Q2 totals and not comparable directly to the Q2 Regional BOP table without period/vintage reconciliation.
- This PDF was inspected via official MOF PDF extraction; byte-preserving download failed in this execution environment. No raw bytes, HTTP headers, local file length, retrieval UTC or SHA-256 claimed.
- Status: official series definitions/45-economy scope PASS; June 2026 India monthly asset row PASS; June 2026 India monthly liability row PASS; within-source asset arithmetic PASS; liability published-total residual 1 (100 million yen) flagged for rounding/unknown dash semantics; Q2 Apr-Jun matched-vintage aggregation NOT_DONE; raw-byte archive/hash NOT_DONE; production NOT_AUTHORIZED.
- Next exact action: inspect official April and May 2026 monthly portfolio PDFs (same 45-economy sections), capture/hash original files if supported, and reconcile April/May/June values and revision vintages against the 10-Nov-2026 Q2 Regional BOP release. Do not add preliminary month values into a Q2 total unless vintage/period definitions support it; preserve each month's published totals and dashes.
- Protected invariants unchanged: ₹0; no inferred zeros, no FX conversion, no netting, no stock/flow mixing, no synthetic values, no changes to Production Selector/RANKING_SCORE/+1 PRESSURE_FADE/CORE-672/Engines A–E/IPO-PLX V2/fixed 63-country IMF cohort. UNKNOWN is never PASS.
