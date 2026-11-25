# GCR Continuation 251 — Albania (ALB) official USD archive route vintage / Q2-2026 eligibility adjudication
Date: 2026-11-26 (Asia/Kolkata)
Decision: A distinct official Bank of Albania archive navigation route exposes legacy USD quarterly BOP and financial-account datasets, including portfolio assets/liabilities taxonomy. However, the legacy USD BOP route ends at Q4-2013 and carries a 11-Sep-2017 revision/publication note; the New-format Financial Account USD quarterly page also carries the 11-Sep-2017 revision note. Neither is a Q2-2026 source or a valid conversion bridge for the C237 Q2 EUR legs. No Q2-2026 USD observations, current conversion method, revision/vintage link or raw export were captured. ALB remains DATA_CAPTURED / PARTIAL / NOT PASS; asset/liability REVIEW; vintage UNKNOWN; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity and selection
- Re-fetched current default-branch Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, fixed 63-country matrix, and C250 report before selection.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`; scope remains curated pages 1–53, not a verbatim archive.
- Searched and reopened ALB C139, C237 and C238. Reused C237 Q2-2026 EURm legs (+156.25 assets, +124.70 liabilities) and C238 methodology findings. No repeated C237 PDF extraction, C140/C141/C192 Main-data route, C238 2014 methodology PDF, IMF query or cohort rebuild.
- C238 allowed reopening only for distinct dated Q2 revision evidence, detailed Q2 FX compilation note or transaction-level flow-rate data. A newly discovered official archive page offered USD quarterly series, so its period/vintage suitability was tested as a new route fingerprint.

## 2. New official archive navigation and USD series
- Official Bank of Albania archive navigation page: https://www.bankofalbania.org/Statistics/Monetary_Financial_and_Banking_statistics/Monetary_Financial_and_Banking_statistics.html?CRegtab=679&Cgroups=46&evb=agregate&evn=expand&periudha_id=1
- The page explicitly lists `Balance of Payments USD [Bank of Albania] (Quarterly)` and `Financial Account USD [Bank of Albania] (Quarterly)`, plus a separate `Financial account USD (New format) [Bank of Albania] (Quarterly)` series.
- The legacy Balance of Payments USD quarterly child page: https://www.bankofalbania.org/Statistics/Monetary_Financial_and_Banking_statistics/Monetary_Financial_and_Banking_statistics.html?cregtab_id=539&evb=agregate&evn=agregate_detaje&periudha_id=3
- Its official description says all items are in USD millions and quarterly. The selectable period list runs Q1-1993 through Q4-2013 only. It states the 11-Sep-2017 publication represents revised BOP data for 2013 due to IIP/external-debt reconciliation and methodological changes.
- The distinct New-format Financial Account USD quarterly child page: https://www.bankofalbania.org/Statistics/Monetary_Financial_and_Banking_statistics/Monetary_Financial_and_Banking_statistics.html?cregtab_id=683&evb=agregate&evn=agregate_detaje&periudha_id=3
- Its methodology describes USD-million quarterly financial-account items and repeats the 11-Sep-2017 2013 revision note. Taxonomy exposes liabilities and assets, with portfolio investment and equity/debt children; this confirms taxonomy only, not a current Q2-2026 value.

## 3. Why the archive cannot close the open Q2 gate
- The legacy USD BOP child page period selector ends at Q4-2013; therefore Q2-2026 is outside its coverage. The 2017 note is a historical revision statement, not a 2026 observation vintage.
- The New-format USD Financial Account child page's visible metadata also identifies the 2017 publication/revision note and exposes no Q2-2026 observation cells in the current retrieval. It is not evidence of a current 2026 archive merely because the navigation remains visible.
- The archive pages do not establish that their USD series are the same Q2 compilation as the August-2026 Monthly Statistical Report EURm Table 2-1. No direct link, common release identifier, revision log, or matching observation vintage was found.
- No USD values were copied from the old page, no exchange-rate conversion was inferred, no diagnostic IMF/EUR ratio was used, and no USD/ALL/ EUR monthly rates were combined.

## 4. Reused ALB values and acceptance
| Gate | Status |
|---|---|
| C237 Q2-2026 national asset | +156.25 EURm (captured; reuse) |
| C237 Q2-2026 national liability | +124.70 EURm (captured; reuse) |
| C237 published net identity | +31.55 EURm (156.25 - 124.70; identity only) |
| C238 general BoA flow conversion rule | PASS (average rate for flows; general rule only) |
| New official USD archive navigation | PASS (route discovered) |
| Legacy USD BOP Q2-2026 coverage | FAIL / NOT_ELIGIBLE (series ends Q4-2013) |
| New-format USD financial account Q2-2026 value / vintage | NOT_CAPTURED / NOT_ESTABLISHED |
| Q2-specific EUR→USD conversion / aggregation | NOT_ESTABLISHED |
| Asset numeric comparison | REVIEW / NOT_PASS |
| Liability numeric comparison | REVIEW / NOT_PASS |
| Same-vintage / revision cutoff | UNKNOWN |
| Raw current USD export / SHA-256 | NOT_CAPTURED |
| ALB national validation | DATA_CAPTURED / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Decision / duplicate prevention / next action
- C251 closes the newly discovered legacy USD archive route as ineligible for Q2-2026; this prevents accidental use of a 2013-ending USD series as if it were a current Q2-2026 bridge.
- Do not repeat the archive page or its same child URLs absent a genuinely new official 2026 dataset version, dated revision record, or supported export containing Q2-2026 USD portfolio asset/liability observations.
- Keep ALB asset/liability gates REVIEW and vintage UNKNOWN. Do not calculate or publish a conversion from the diagnostic ratio or from an unweighted monthly/quarterly mean.
- Advance to the next eligible fixed-cohort member only after exact report-history/route-fingerprint preflight. No IMF re-query or cohort rebuild.

## 6. Protected invariants
₹0; official/free sources only; no external contact; no IMF re-query; no cohort rebuild; no synthetic values, fabricated timestamps or hashes; no IIP stock substitution; no net-to-leg back-solving; no unsupported FX/sign/scale conversion; UNKNOWN never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No merge, workflow dispatch or production integration.