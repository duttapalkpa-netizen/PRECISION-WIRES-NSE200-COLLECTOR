# GCR Continuation 298 — South Africa (ZAF) Q2-2026 SARB BOP transaction timing, currency and FX-conversion methodology boundary
Date: 28-Nov-2026 (Asia/Kolkata)
Scope: fixed 63-country Q2-2026 cohort; ZAF next after WSM in the cohort's recorded continuation order.

## 1. Mandatory continuity preflight and PASS work skipped
- Re-read the current GitHub Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country matrix and controlling C297 / C255 reports.
- Rechecked Library Mother File and prior ZAF reports (C127, C215, C255) through Library search / GitHub source. No duplicate SARB quarterly-table extraction, IMF query, old 24-row no-date API request, date-format guessing, OECD quarterly FX arithmetic or cohort rebuild.
- C297 WSM raw-file follow-up was attempted using the exact first-party SBS BOP XML, CBS B1 XLSX and CBS B11 XLSX locators. The current retrieval channel rejected XML/XLSX MIME; direct byte download also failed. No raw bytes, file size, schema, rows or SHA-256 captured. WSM remains REVIEW/REVIEW/UNKNOWN, FULL_PASS=NO; aggregate NOT_AUTHORIZED.
- Following C297's explicit fallback rule and the fixed cohort continuation order, WSM is left pending and ZAF is the next eligible unresolved country. This is a task transition, not a WSM pass.

## 2. New official SARB B03 methodology evidence
Official source: SARB, *Guide for the Completion of the B03 Form: Foreign Transactions Liabilities and Assets*, May 2021.
URL: https://www.resbank.co.za/content/dam/sarb/what-we-do/statistics/guides/Guide%20for%20the%20completion%20of%20the%20B03%20form%20.pdf

Verified source statements:
- The B03 form is used by SARB to collect foreign transactions for compilation of official BOP and IIP statements.
- Accounting conventions: accrual basis; assets and liabilities reported gross, not netted; balances and transactions recorded at the time of transaction, not settlement date.
- Currency of completion: all monetary values reported in thousands of rand (except Table 2).
- Reporting period: transactions in all tables total all transactions during the quarter; balances are as at quarter-end.
- Liabilities: increase in liabilities is inflow (+); decrease in liabilities is outflow (-).
- Assets: decrease in assets is inflow (-); increase in assets is outflow (+).
- Revaluations due to exchange-rate and price movements are distinct from transactions and are separately identified in the B03 tables.

Important scope limitation:
- B03 is a reporting form for foreign transactions/assets/liabilities submitted by institutions; it is a primary SARB compilation-method source, but it does not explicitly state the actual exchange-rate source, rate fixing time, midpoint/bid/ask convention, or exact conversion frequency used for the published aggregate Q2 portfolio-investment flows. It must not be represented as an explicit SARB portfolio-flow FX conversion rule.

## 3. Cross-check with SARB's public BOP framework
- SARB September 2025 Quarterly Bulletin describes South Africa's BOP compilation as broadly aligned with IMF BPM6. This is a broad framework statement, not a ZAF Q2-2026 FX conversion-rate specification.
- The IMF BPM6 Compilation Guide (2014), section 4.18–4.21, recommends daily average midpoint rates for transactions aggregated for a day; if transaction values are aggregated over a longer period such as a week or month, use the average midpoint rate for that period. It separately says positions use the midpoint market rate applicable on the measurement date.
- The same IMF Guide states it is practical guidance rather than a prescriptive definitive national method, and that national compilers adapt methods to national circumstances. Therefore BPM6 general guidance cannot by itself prove which specific series SARB applied to the Q2 portfolio-flow table.
- Sources:
  - SARB B03 guide above.
  - SARB September 2025 Quarterly Bulletin: https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/quarterly-bulletin-publications/2025/september/01Full%20Quarterly%20Bulletin.pdf
  - IMF BPM6 Compilation Guide: https://data.imf.org/-/media/iData/External-Storage/Documents/FB1F86C7158646DDB554D0882F1F2A3B/en/3-BPM6-com-guide.pdf

## 4. Reassessment of EXCX135D admissibility
- C255 already established official SARB series EXCX135D is Rand per US Dollar (ZAR/USD), described as a weighted average of banks' daily rates at approximately 10:30 am, weighted by banks' FX transactions.
- That description does not prove that EXCX135D is the actual rate used to translate Q2 portfolio transactions into rand for the published BOP flow table. Nor does B03 guide identify EXCX135D.
- C255's date-bounded Q2 daily API response remained inaccessible through the current retrieval surface. Do not repeat the already exhausted no-date sample or path-format guesses.
- Thus EXCX135D remains a candidate comparator only, not an admitted BOP conversion series. No Q2 daily average or new asset residual was calculated.

## 5. ZAF acceptance decision
| Gate | Result |
|---|---|
| B03 official methodology source | PASS |
| Accrual / economic-ownership timing | PASS |
| Gross separate asset/liability reporting | PASS |
| Transaction vs revaluation separation | PASS |
| B03 monetary unit (thousand ZAR) | PASS |
| B03 transaction-period / quarter-end stock distinction | PASS |
| Official SARB Q2 portfolio flow FX source / fixing rule | NOT_ESTABLISHED |
| EXCX135D identity and unit | PASS (carried forward from C255) |
| EXCX135D as actual SARB BOP conversion rate | NOT_ESTABLISHED |
| Complete Q2 daily FX raw series | NOT_CAPTURED |
| ZAF asset numeric comparison | REVIEW (carried forward; no recalculation) |
| ZAF liability numeric comparison | PASS (carried forward; no recalculation) |
| ZAF same-vintage / full validation | PENDING / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Exact next action
1. Do not calculate a Q2 conversion from EXCX135D until an official SARB publication or methodology explicitly connects that series/rate convention to BOP portfolio transaction compilation.
2. If a distinct official SARB metadata/technical note later documents the flow-conversion rate and frequency, capture it with date/version and then obtain complete Q2 source observations through a supported API route; do not retry the already exhausted endpoint surface.
3. If no explicit FX rule or supported full Q2 series is available, preserve asset REVIEW and proceed to the next unfinished country in the fixed cohort. Keep liability PASS only as previously accepted.
4. Revisit WSM only if supported raw-file capture becomes available for the exact CBS/SBS first-party XML/XLSX locators and the DSBB BOP methodology body can be captured.

## 7. Invariants
₹0; official/free sources only; no token or credential acquisition, no paid API, no external contact, no synthetic observations, no fabricated timestamps, no unsupported FX/sign/scale conversion, no tolerance widening, no netting, no stock/flow substitution, no IMF re-query or cohort rebuild. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge, workflow dispatch or production integration.

**Task result:** C298 adds a first-party SARB B03 methodology boundary and clarifies that EXCX135D cannot yet be treated as the BOP portfolio-flow conversion rate. ZAF remains PARTIAL / NOT PASS; WSM remains pending; aggregate remains NOT_AUTHORIZED.
