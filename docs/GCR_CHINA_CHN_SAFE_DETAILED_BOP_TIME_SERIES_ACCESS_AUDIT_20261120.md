# China SAFE detailed BOP time-series access audit — 2026-11-20
Status: PARTIAL / BLOCKED at file-content inspection. Official source locator found; workbook bytes could not be retrieved in this execution environment. No sign-convention resolution claimed.

## Progress log
- Preflighted current Master Continuity Ledger, GCR priority queue, CHN comparison, ZAF comparison, cross-country validation report and 63-country Q2 cohort.
- Excluded completed PASS items: IMF DSD/registry capture, 154-member WEO roster, 9,299-row panel QA, 12-country exact-key sample, CHN exact IMF receipts, SAFE Q2 abridged table arithmetic, and prior country validations. No duplicate IMF queries or panel rebuild.
- Continued the explicitly open CHN task: official SAFE detailed time-series BOP workbook and metadata/version inspection.

## Official navigation chain and file identity
1. SAFE Data and Statistics index: https://www.safe.gov.cn/en/DataandStatistics/index.html
2. Balance of Payments category: https://www.safe.gov.cn/en/BalanceofPayments/index.html
3. The category lists “The time-series data of Balance of Payments of China” with date 2026-09-29.
4. The linked detail page is https://www.safe.gov.cn/en/2019/0329/1496.html, index 000014453-2019-0016, dispatch date 2026-09-29.
5. The detail page's file link resolves to:
   https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx
   Expected content type from the web fetch response: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.
6. Browser text extraction cannot inspect this XLSX (unsupported content type); direct byte download through the available container fetch also failed. Therefore workbook sheet names, exact Q2 values, data definitions, revision/vintage metadata and row sign semantics have NOT been inspected or hashed. Do not invent a workbook hash or claim its contents.

## Independent SAFE release confirmation
SAFE's 2026-09-29 Q2 release page (index 000014453-2026-0068) states:
- Q2 table lines 30–32: portfolio investment -USD5.5bn, assets -USD48.8bn, liabilities +USD43.3bn.
- Note 2: credit positive, debit negative, and net is the sum of credit and debit.
- Note 6: rounded numbers; note 8: BOP data is regularly revised.
- Note 7 explicitly directs readers to SAFE Data and Statistics for detailed data.
Official page: https://www.safe.gov.cn/en/2026/0929/2458.html
This abridged statement confirms the sign shown in the summary table but does not supply the detailed workbook's row-level definitions needed to map SAFE assets to IMF A_NFA_T.

## Decision
- Official detailed workbook locator: PASS.
- Workbook retrieval/content inspection/hash: BLOCKED / NOT_DONE.
- CHN liability rounded comparison: remains PASS at published precision.
- CHN asset magnitude corroboration: remains within published rounding, but sign mapping remains REVIEW / NOT_RESOLVED.
- CHN full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Retrieve the exact XLSX bytes through a supported file-transfer route (for example, owner-side browser download or a workflow runner that can access the public official URL), then:
1. Record retrieval timestamp, HTTP status, content length, response headers and SHA-256.
2. Inspect workbook sheets, dimensions, labels, units, BPM6 codes, footnotes, Q2-2026 observations and revision date.
3. Compare exact quarterly portfolio asset/liability rows to the already archived IMF exact-key values; preserve source signs before any mapping.
4. Only accept a sign transformation when SAFE workbook metadata or official methodology explicitly supports it. Otherwise keep REVIEW.
Do not substitute IIP stocks, external debt stocks, or Q3 cumulative totals for Q2 BOP transactions.

## Protected invariants
No production changes, aggregation, netting, imputation, synthetic data, silent sign flip, or repeated IMF/SARB work. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
