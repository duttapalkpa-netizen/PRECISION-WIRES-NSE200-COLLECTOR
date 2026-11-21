# South Africa (ZAF) Q2-2026 — SARB B03/B31 reporting-currency and FX-methodology boundary
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 219 / Research Verification 52
Status: NEW OFFICIAL SARB REPORTING GUIDES VERIFIED; REPORTING UNIT AND TRANSACTION-VALUATION PRINCIPLES DOCUMENTED; EXACT SARB BOP COMPILER FX CONVERSION RATE/ALGORITHM NOT PUBLISHED IN THE GUIDES REVIEWED. ZAF ASSET REMAINS REVIEW.

## 1. Mandatory continuity preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and Historical Task Registry before task selection.
- Re-opened C216 daily FX route boundary, C217 KBP export-family boundary, C218 monthly USD/ZAR series audit, C127 FX methodology boundary, and the original ZAF numeric reconciliation.
- Excluded repeat IMF extraction, SARB PDF extraction, subcomponent arithmetic, C215/C216 endpoint retries, C217 KBP workflow rediscovery and C218 monthly-value transcription.
- The C127 handoff already said not to retry ZAF absent new official methodology evidence; this continuation uses newly inspected SARB B03/B31 guides as a new official source family. It does not claim that those guides resolve the compiler FX rate.

## 2. New official SARB source family: B03 and B31 form-completion guides
### B03 — Foreign Transactions Liabilities and Assets (May 2021)
Official URL: https://www.resbank.co.za/content/dam/sarb/what-we-do/statistics/guides/Guide%20for%20the%20completion%20of%20the%20B03%20form%20.pdf
- Purpose: collect foreign transactions for compilation of South Africa's BOP and IIP.
- Accounting: accrual basis; purchases/sales, issues/redemptions recorded at transaction time, not settlement date.
- Valuation: equity/debt securities traded on exchanges are valued at market prices; proxies may be used if observable market prices are unavailable.
- Currency of completion: all monetary values in thousands of rand, except Table 2 which is full rand.
- B03 includes foreign-liability and foreign-asset tables, and separates transactions, revaluations (including exchange-rate changes), price changes and other-volume changes.
### B31 — Foreign Assets of Institutional Investors (June 2021)
Official URL: https://www.resbank.co.za/content/dam/sarb/what-we-do/statistics/guides/Guide%20for%20the%20completion%20of%20the%20B31%20form.pdf
- Purpose: collect quarterly cross-border transactions of South African institutional investors holding assets issued by unrelated non-residents; includes acquisitions, disposals, repatriations and investment income.
- Accounting: accrual basis; transactions recorded at the time of the transaction, not settlement date.
- Valuation: transaction value / market price at which purchases or sales were conducted; fair-value estimates only if market price is unavailable.
- Currency of completion: South African rand, amounts in thousands of rand.
- The guide does not specify which exchange-rate observation (actual transaction midpoint, daily average, 10:30 bank-weighted rate, monthly average or quarterly average) is applied when an underlying transaction is originally denominated in foreign currency.

## 3. General international standard and what it does/does not establish
- SARB public materials state that its BOP compilation follows IMF BPM6. SARB's 2014 BPM6 transition note and subsequent Quarterly Bulletin methodological notes support the framework reference.
- IMF BPM6 paragraphs 3.104–3.105: foreign-currency flows should be converted at the rate prevailing when flows take place; midpoint rate is preferred; actual transaction rate is preferred, with daily average as a practical approximation for daily transactions; if daily rates cannot be applied, use the shortest available period. Period averages are appropriate for continuous flows.
- IMF BPM6 paragraph 3.106: derived flow measures should in principle be built after converting the underlying flows, rather than directly converting a derived aggregate from one currency into another.
- This is the governing international benchmark, not proof of the exact operational conversion used by SARB's compiler for the published 2026-Q2 portfolio asset and liability aggregates.
- The B03/B31 guides report amounts in ZAR thousands and transaction timing/valuation rules, but they do not disclose the compiler-side FX rate source, midpoint convention, aggregation frequency, treatment of non-USD denominations, or the exact bridge from reporting forms to published USD-denominated IMF data.

## 4. Consequence for the prior ZAF reconciliation
- The earlier comparison converted SARB's quarterly ZAR net-flow aggregates using one OECD quarterly-average ZAR/USD rate. This produced liability residual +0.007354619 USDm (previously within the strict rounding bound) and asset residual -0.056053395 USDm (outside the bound).
- Those numeric results are historical calculations, not recalculated here.
- Because the exact SARB compiler conversion method is still not established, neither the earlier liability PASS nor asset REVIEW proves conversion-method equivalence to IMF USD data. Preserve the previous arithmetic result but annotate its conversion-method limitation.
- The SARB KBP5339M monthly middle-rate observations verified in C218 are a distinct published monthly series; the 10:30 weighted-average footnote is not evidence that the BOP compiler uses that rate for every portfolio transaction.
- No Q2 daily EXCX135D rows, transaction-level foreign-currency records, SARB compiler conversion receipt, or raw response SHA-256 were captured in this task.

## 5. Acceptance disposition
| Gate | Status |
|---|---|
| Current continuity preflight | PASS |
| Official B03 guide retrieved/read | PASS |
| Official B31 guide retrieved/read | PASS |
| Reporting unit and transaction-time/valuation rules extracted | PASS |
| SARB compiler FX conversion method for 2026-Q2 portfolio flows | NOT_ESTABLISHED |
| BPM6 benchmark identified | PASS — international standard only |
| Daily EXCX135D Q2 capture | NOT_CAPTURED |
| Exact SARB compiler USD bridge / same-vintage conversion receipt | NOT_CAPTURED |
| ZAF asset numeric reconciliation | REVIEW / NOT PASS (prior result preserved) |
| ZAF liability numeric reconciliation | Prior arithmetic PASS retained; method equivalence NOT_ESTABLISHED |
| ZAF full dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 6. Next action selection
- ZAF public methodology search has reached a bounded stop: the newly inspected official B03/B31 guides still do not publish the compiler-side FX conversion rule. Do not repeat these guide searches absent a new official revision or source endpoint.
- Resume the existing 63-country rank-1 cohort task at China (CHN), already named in C127 as the next high-priority unresolved country. Inspect the existing SAFE detailed BOP XLSX access audit; do not rebuild the cohort or re-query IMF. Reopen SAFE only if a new official byte-transfer route or source revision is evidenced.
- Keep ZAF open and reopen only on new SARB daily-history payload, a USD-equivalent official national table, transaction-level FX methodology, or direct official compiler confirmation.

## 7. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, synthetic data, fabricated timestamps, guessed FX code, quarterly-rate substitution, tolerance widening, net-to-leg back-solving or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 8. Sources
- SARB B03 form guide (May 2021): https://www.resbank.co.za/content/dam/sarb/what-we-do/statistics/guides/Guide%20for%20the%20completion%20of%20the%20B03%20form%20.pdf
- SARB B31 form guide (June 2021): https://www.resbank.co.za/content/dam/sarb/what-we-do/statistics/guides/Guide%20for%20the%20completion%20of%20the%20B31%20form.pdf
- SARB BPM6 transition note: https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/articles-and-notes/2014/6533
- IMF BPM6 Chapter 3, paragraphs 3.104–3.106: https://data.imf.org/-/media/iData/External-Storage/Documents/73FBCD5B6CDE4D289C60B9B0CAA40622/en/2-bpm6.pdf
- Controlling C127 methodology boundary: docs/GCR_ZAF_Q2_2026_FX_CONVERSION_METHODOLOGY_BOUNDARY_CONTINUATION127_20261121.md
- Controlling ZAF reconciliation: docs/GCR_ZAF_Q2_2026_IMF_SARB_OECD_FX_RECONCILIATION_20261120.md