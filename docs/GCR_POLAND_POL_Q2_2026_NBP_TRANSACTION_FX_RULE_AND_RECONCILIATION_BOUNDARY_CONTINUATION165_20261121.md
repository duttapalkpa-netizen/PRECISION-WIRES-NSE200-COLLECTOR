# Poland POL Q2-2026 — NBP transaction FX rule and reconciliation boundary
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 13
Continuation sequence: 165
Decision: OFFICIAL TRANSACTION-DATE FX RULE NOW DOCUMENTED FOR PORTFOLIO SECURITY REPORTING; AGGREGATE Q2 PLN-TO-USD CONVERSION STILL NOT COMPUTABLE WITHOUT TRANSACTION-LEVEL DISTRIBUTION; IMF-NBP SAME-VINTAGE BRIDGE NOT_ESTABLISHED; POL PARTIAL / NOT PASS.

## 1. Continuity preflight
- Re-fetched current Master Continuity Ledger, GCR Priority Queue and POL Part-12 methodology/vintage report.
- Reused NBP Q2 release dual legs from Part 11 and IMF raw receipt. No duplicate Q2 value extraction, no IMF re-query, no cohort rebuild.
- Part 12 had stated exact transaction FX convention NOT_ESTABLISHED. This Part found a newer/more specific official NBP explanatory-notes document and updates that one gate only.

## 2. Official NBP reporting instructions — new decisive evidence
Official NBP Department of Statistics, “Explanatory notes to reporting questionnaires”, Version 1.8, July 2023:
https://nbp.pl/wp-content/uploads/2025/08/EN-objasnienia-do-rozporzadzenia-v1.8.pdf

### 2.1 General FX conversion rule
- General explanatory note §6 (PDF page 6; lines 86–89 in extracted source): reporting data are in PLN, full zloty, no decimals. Foreign-currency end-period balances use NBP average rates on the last business day of the reporting period. “Other data” use the actual exchange rate used on that date, arising from the nature of the operation, or the NBP average rate for the currency on the preceding day.
- Therefore quarter-end average rate is a rule for end-period balances, not a blanket conversion for transaction flows.

### 2.2 Portfolio asset reporting form PW-AIN
- Questionnaire PW-AIN is explicitly for financial instruments with an ISIN issued by non-residents and held by the reporting unit; it reports in PLN without decimal places (PDF page 206; extracted lines 11513–11543).
- Its transaction columns are separate from beginning/end positions and from other-price/exchange-rate changes.
- NBP's worked example for purchase of 10,000 Microsoft shares at USD 15 explicitly applies USD/PLN 3.15 at trade date, yielding PLN 472,500. End-period position uses the distinct end-period rate USD/PLN 3.20 (PDF page 210; extracted lines 11717–11816).
- This is direct, form-specific evidence that the foreign portfolio asset transaction amount is translated using the trade-date FX rate in the worked example, not quarter-end FX.

### 2.3 Portfolio liability-side reporting form PW-RIN
- Questionnaire PW-RIN is for resident-issued securities purchased outside the domestic market and held by the reporting unit (PDF page 199 onward; extracted lines 11125–11144).
- Its worked example also distinguishes trade-date USD/PLN 3.15 from end-period USD/PLN 3.20 and uses the trade-date rate for the purchase transaction (PDF page 203; extracted lines 11322–11334; 11415–11424).
- The explanatory notes show asset and liability-side security transactions have distinct questionnaires and separate transaction columns. This supports a consistent trade-date conversion principle for the relevant portfolio security reporting flows.

### 2.4 Important scope limitation
- The official instructions establish the reporting-unit conversion rule and an explicit trade-date example. They do NOT provide the actual underlying transaction-level portfolio purchases/sales for all Polish reporting units in Q2 2026, nor the daily transaction distribution/rates behind the national Q2 aggregates.
- NBP's national quarterly values (assets PLN 24,144m; liabilities PLN 70,910m) are therefore not convertible into USD by multiplying/dividing by one quarter-average, quarter-end or aggregate-implied rate. Such a conversion would be unsupported.
- The separate FX-change column also must not be conflated with the transaction columns.

## 3. What this resolves and what remains open
Resolved:
- Official NBP source methodology does specify the FX principle relevant to portfolio security transactions: actual exchange rate used on transaction date, or general §6 fallback actual rate / NBP average rate on preceding day where applicable.
- Quarter-end NBP average rate is for end-period balances, not the transaction flow totals.
- Part-12's blanket “exact transaction FX convention NOT_ESTABLISHED” is superseded by this form-specific official evidence.

Still unresolved:
- Q2 national totals in PLN cannot be independently translated to USD without transaction-level date/currency amounts and rates or an official NBP matched USD Q2 dual-leg publication.
- The official Q2 PDF raw bytes and SHA-256 remain NOT_CAPTURED.
- NBP Q2 publication vintage 30-Sep-2026 vs existing IMF raw archive 19-Nov-2026 equivalence remains NOT_ESTABLISHED.
- No numeric cross-currency comparison or residual is computed.

## 4. Acceptance matrix
| Gate | Result |
|---|---|
| NBP Q2 national portfolio asset value | PASS — 24,144 mn PLN (Part 11) |
| NBP Q2 national portfolio liability value | PASS — 70,910 mn PLN (Part 11) |
| Official portfolio reporting forms identified | PASS — PW-AIN / PW-RIN |
| Transaction-date FX principle | PASS — official form-specific examples |
| Quarter-end FX correctly restricted to end-period balances | PASS |
| Underlying Q2 transaction-level FX distribution | NOT_AVAILABLE / NOT_CAPTURED |
| Matched official USD Q2 dual-leg aggregate | NOT_CAPTURED |
| NBP PDF raw bytes/SHA-256 | NOT_CAPTURED |
| NBP Sep-30 vs IMF Nov-19 same-vintage bridge | NOT_ESTABLISHED |
| Cross-currency numeric comparison | NOT_DONE |
| POL national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 5. Next bounded action and decision
- Search only for an official NBP Q2-2026 USD-denominated dual-leg table or a downloadable national transaction series with matching USD and vintage metadata. If no such public aggregate exists, stop trying to convert the PLN totals: retain the national PLN legs as independently validated source observations and advance to the next eligible country.
- Do not infer aggregate USD values from daily FX rates without the underlying daily transaction weights. Do not use quarter-end balance rates or aggregate ratios.
- No repeat NBP PDF download attempts in this Part; raw PDF hash remains a separate integrity task if a supported retrieval path becomes available.
- ₹0; official/free sources only. No synthetic data, fabricated timestamps, net-to-leg inference, ad-hoc FX conversion, stock-as-flow, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
