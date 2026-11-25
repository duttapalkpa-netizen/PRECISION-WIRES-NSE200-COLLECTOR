# GCR — Albania ALB Q2-2026 official flow FX rule and revision boundary
Date: 2026-11-25 (Asia/Kolkata)
Continuation: 238
Decision: **The official BoA BPM6 transition commentary confirms that BOP statistics are published in EUR and users may convert flow values using the published average exchange rate (stocks use end-period rates). This establishes the broad official flow-vs-stock conversion convention, but does not specify the exact Q2-2026 portfolio transaction-rate aggregation or a matched revision vintage for the C237 PDF and archived IMF rows. ALB remains DATA_CAPTURED / PARTIAL / NOT PASS; both numeric comparison gates REVIEW; vintage UNKNOWN; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-read current default-branch Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, 63-country matrix, Library Mother File (pages 1–53/addenda through C57), and C237 ALB report.
- Existing C237 Q2 national portfolio legs and C139 archived IMF observations were reused. No repeat of the C237 PDF text extraction, C140/C141/C192 legacy Main-data routes, IMF query, cohort rebuild, or previous route tests.
- Selected only the still-open ALB FX-convention/revision boundary.

## 2. New official Bank of Albania conversion evidence
- BoA official “Commentary for changes in the publication of external sector statistics according to BPM6, June 2014”:
  https://www.bankofalbania.org/rc/doc/01_commentary_for_changes_in_the_publication_of_external_sector_statistics_according_to_bpm6_june_2014_6689_1_10539.pdf
- The note states that BoA external-sector tables are published on a BPM6 basis from June 2014 and BOP is presented in EUR.
- It explicitly says users may convert BOP values to ALL, USD or other currencies using the **average exchange rate for flows** and the **end-of-period exchange rate for stocks**, published by BoA.
- This is direct national-source evidence of the broad conversion convention, not an inferred cross-rate.
- BoA official monthly-average exchange-rate table states its monthly average foreign-currency rates to ALL are the simple average of daily official rates, under BoA Regulation No.66 dated 30-Aug-2006:
  https://www.bankofalbania.org/Statistics/External_sector_statistics/Balance_of_Payments/Main_data_for_Balance_of_Payments.html?cregtab_id=645&evb=agregate&evn=agregate_detaje&periudha_id=1
- BoA official external-sector page confirms BOP compilation is based on IMF BPM6 and distinguishes transaction flows over a period from IIP positions at a reference date:
  https://www.bankofalbania.org/Statistics/External_sector_statistics/
- IMF BPM6 paragraphs 3.105–3.106 say actual transaction rates are preferred; daily average is usually a good approximation for daily transactions; if daily rates cannot be applied, use the shortest-period average; for continuous flows use the period average. Derived net flows must be calculated only after converting the underlying flows:
  https://www.bankofalbania.org/rc/doc/bpm6_9303_10534.pdf

## 3. What is and is not established
| Gate | Status | Evidence / boundary |
|---|---|---|
| BoA BPM6 compilation basis | PASS | Official BoA external-sector page |
| BoA BOP presentation currency EUR | PASS | BoA June-2014 BPM6 commentary |
| BoA general flow conversion convention | PASS | Published average FX rate for flows |
| Stock conversion convention | PASS | End-of-period FX rate for stocks; not used for BOP flow legs |
| Monthly average BoA rate definition | PASS | Simple average of daily official rates to ALL |
| Exact Q2-2026 portfolio-specific applied USD conversion | NOT_ESTABLISHED | No Q2-specific compilation record or transaction-level FX observations linked to these legs |
| Exact quarterly aggregation for the Q2 portfolio legs | NOT_ESTABLISHED | Monthly simple averages alone do not establish flow-weighted quarterly conversion for quarterly aggregate portfolio legs |
| Same-vintage link between C237 August-2026 PDF and archived IMF Q2 rows | UNKNOWN | No observation-specific revision timestamp / vintage identifier matched |
| Revision cutoff for Q2-2026 portfolio legs | UNKNOWN | No explicit Q2-2026 revision calendar/cutoff found in the inspected official evidence |
| Asset / liability numeric reconciliation | REVIEW / NOT_PASS | Do not apply an assumed quarterly average or inferred EUR/USD cross-rate |
| ALB full national validation | DATA_CAPTURED / PARTIAL / NOT PASS | Preserve current matrix gates |
| Aggregate admission | NOT_AUTHORIZED | No full-pass evidence |

## 4. Why no conversion was calculated
- BoA's published monthly average rates are quoted against ALL. A cross-rate derived from ALL/USD and ALL/EUR is not itself evidence that BoA used that exact aggregation for the Q2 portfolio flow legs.
- A simple mean of three monthly averages, or an unweighted quarterly mean, would not establish a transaction-weighted/shortest-period conversion for an aggregate quarterly portfolio flow.
- No transaction-level dates/amounts or official Q2 conversion workbook was captured. The diagnostic ratios recorded in C237 remain diagnostic only.
- No net-to-leg back-solving, IIP stock substitution, unsupported rate selection, or IMF re-query was performed.

## 5. Revision/vintage boundary
- BoA's 2014 commentary establishes the transition to BPM6 and EUR presentation and notes historical conversion of 2013 quarters for comparability. It does not provide a Q2-2026 observation-specific revision date.
- The BoA monthly report 08/2026 identifies the publication issue but is not itself a vintage ID for the Q2 row.
- The inspected official pages and PDF do not expose a dated Q2-2026 revision log or an exact vintage identifier that can be matched to the archived IMF row.
- Therefore the vintage and revision cutoff remain UNKNOWN / NOT_ESTABLISHED.

## 6. Next action and duplicate prevention
- Keep ALB numeric asset/liability gates REVIEW and vintage UNKNOWN.
- Reopen only if BoA publishes a distinct dated Q2-2026 revision record, a detailed Q2 FX-conversion/compilation note, or a transaction-level official flow-rate dataset sufficient to compute the applicable conversion without an unsupported proxy.
- Do not repeat the 2014 commentary PDF retrieval, C237 monthly report PDF text retrieval, legacy Main-data route, or archived IMF query.
- If no genuinely new official evidence appears, advance to the next eligible fixed-cohort item after exact route-history preflight.

## 7. Protected invariants
₹0; free official sources only; no synthetic values, fabricated timestamps, IIP stock substitution, net-to-leg back-solving, unsupported FX conversion, paid source, or external contact. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No production integration or merge.
