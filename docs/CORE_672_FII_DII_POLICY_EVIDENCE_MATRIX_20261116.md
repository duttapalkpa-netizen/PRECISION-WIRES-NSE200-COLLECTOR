# CORE-672 FII/DII Policy Evidence & Decision Matrix

Date: 2026-11-16  
Status: **SOURCE EVIDENCE RECONCILED; POLICY DECISIONS STILL BLOCKED**  
Scope: research-only evidence review; no aggregation implementation, no trading state, no production change.

## 1. Official NSE source findings

Official NSE report page: https://www.nseindia.in/reports/fii-dii

The page exposes two distinct Capital Market datasets:
1. FII/FPI & DII trading activity **on NSE**.
2. FII/FPI & DII trading activity **on NSE, BSE and MSEI combined**.

The page labels Buy Value, Sell Value and Net Value in **₹ Crores**. Its explanatory note says:
- FII/FPI data is based on same-day activity compiled from PANs provided by NSDL and is provisional, subject to custodial confirmation and modifications.
- DII data is based on trading codes entered by Trading Members and client-category classification supplied through unique-client-code details.
- The combined dataset is collated from trades executed by FIIs/FPIs and DIIs across NSE, BSE and MSEI.
- For final FII/FPI data, NSE points users to NSDL or CDSL.

Source page observed in web research: NSE FII/DII report, https://www.nseindia.in/reports/fii-dii (retrieved 2026-11-16). This is official source evidence, not an API schema contract.

## 2. Run #161 value reconciliation — material scope ambiguity

Archived Run #161 payload (artifact ID 14154408713; context member SHA-256 `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`) contains date 13-Nov-2026:
- FII/FPI: buy 18,339.57; sell 12,603.02; net +5,736.55.
- DII: buy 11,745.95; sell 13,999.53; net -2,253.58.

The official NSE page's **combined NSE+BSE+MSEI** table reports exactly these same values for 13-Nov-2026. The separate **NSE-only** table reports different values:
- DII buy 10,561.32; sell 12,532.05; net -1,970.73.
- FII/FPI buy 17,376.50; sell 12,122.52; net +5,253.98.

Therefore the Run #161 payload's values match the combined dataset, not the separately displayed NSE-only dataset, for this date. This is a one-date exact value reconciliation, not proof of the endpoint's behavior on all dates. The collector labels the source as `NSE /api/fiidiiTradeReact (category-normalized)`; it does not encode an explicit `market_scope` field. The endpoint-to-table scope mapping must be confirmed from a captured raw API response or official endpoint documentation before the dataset is labelled definitively.

Arithmetic checks:
- 18,339.57 − 12,603.02 = +5,736.55.
- 11,745.95 − 13,999.53 = −2,253.58.
Thus, for these archived rows, positive net means buy value exceeds sell value; negative net means sell value exceeds buy value. This is arithmetic/column-label interpretation, not a complete CORE-672 signal policy.

## 3. Evidence-backed policy matrix

| Policy dimension | What official/source evidence supports | What remains undecided | Safe interim status |
|---|---|---|---|
| Market scope | NSE publishes separate NSE-only and NSE+BSE+MSEI combined tables; Run #161 numbers match combined table for 13-Nov-2026 | Which scope CORE-672 is intended to represent; exact API-to-table mapping | BLOCKED; expose scope as unresolved, do not call it NSE-only |
| Units | Official table labels values ₹ Crores | Confirm API numeric values retain same unit across endpoint versions | VERIFIED FOR RUN #161 BY EXACT TABLE MATCH; ongoing schema contract not established |
| Sign | Net Value = Buy Value − Sell Value for archived rows; positive is net buying, negative net selling | Whether CORE-672 uses raw net, normalized net, threshold, or relative measure | Arithmetic convention supported; signal transform BLOCKED |
| Observation period | NSE describes same-day activity; row has a date | Latest common date vs N-day sum/mean, trading-session alignment, holidays, partial dates | BLOCKED; no window selected |
| FII provisional status | NSE explicitly says FII/FPI values are provisional and may change after custodial confirmation/modifications | Whether/how to retain revised vintages and which version is eligible at each historical cutoff | BLOCKED; preserve source vintage/provisional label |
| DII classification | NSE says based on trading codes and client-category classification supplied by trading members | Whether to combine with FII in a single directional signal or keep independent | BLOCKED; retain separate category |
| Freshness | Date-only observation and generated_at are distinct; NSE describes same-day activity | Max age, publication/availability timestamp, cutoff-time eligibility | BLOCKED; generated_at must not substitute for observation availability |
| Missing side | Collector exposes row counts/date counts; missing row is not equivalent to zero | Whether one-sided input is UNKNOWN, partial evidence, or other explicit state | Fail closed: UNKNOWN; no zero-fill |
| Duplicate rows | Actual fixture has one row per group/date | Canonical deduplication/revision selection rule | Reject/flag duplicates until explicit policy exists |

## 4. Safe decisions now established

1. Preserve the actual source row's date, group, buy, sell, net, source and generation timestamp.
2. Store/record market scope explicitly when it can be verified; do not infer scope from the word NSE in the URL or source label.
3. Interpret units as ₹ Crores only for the Run #161 values reconciled against the official page; confirm future payload continuity.
4. Retain FII/FPI and DII as separate observations.
5. Treat FII/FPI values as provisional unless a final NSDL/CDSL value and its vintage are separately captured.
6. Do not turn absent rows into zero.
7. Do not derive a market direction or CORE-672 state in this evidence-only stage.

## 5. Decisions still required before any state-producing adapter

- Intended market scope: NSE-only or combined NSE+BSE+MSEI.
- Aggregation period and trading-session alignment.
- Whether to use provisional NSE FII/FPI or final NSDL/CDSL vintage, and revision handling.
- Freshness/cutoff rule using a real observation/publication availability timestamp.
- Missing-side and duplicate/revision handling.
- Whether raw ₹ Crore net values are used directly or normalized before any thresholds.

No policy was selected by this report. No threshold, rolling window, freshness age, or missing-value substitution was invented.

## 6. Progress and scope

- Official NSE report source inspection: 100%.
- Unit/sign/segment-label evidence extraction: 100%.
- Run #161 one-date official table reconciliation: 100%.
- Endpoint-to-table scope proof: BLOCKED pending raw response/official endpoint mapping.
- Aggregation/freshness/missing-side policy approval: BLOCKED.
- State-producing adapter: 0% / NOT_AUTHORIZED.
- CORE-672 FII/DII acceptance: BLOCKED.

No production files, collector, workflow, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 definitions, engines A–E, dataset, default branch or PR state changed. No CI dispatched, no PR merged, no paid API/spend.
