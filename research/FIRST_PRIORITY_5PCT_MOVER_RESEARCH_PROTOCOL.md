# First-Priority Research: H+1 +5% Movers

**Branch:** `audit/prospective-selector-tracking`  
**Status:** audit-only research protocol; no production-selector change.

## Research question

Can the existing V11.3 candidate universe identify stocks whose **next eligible session's high is at least 5% above the decision reference price**? This is the first-priority outcome. H+3 +10% and H+5 +20% remain secondary outcomes and must not dilute the primary objective.

## News window and evidence rules

For the catalyst/news feature, use only articles and filings published during the **24 hours before the frozen decision cutoff**. Store the canonical source URL, publication timestamp with timezone, publisher, headline, source type, and verification state. Use exchange/company primary disclosures where available, then Reuters, AP, BBC, Al Jazeera, Bloomberg and reputable Indian business sources. Deduplicate syndicated headlines.

The GDELT collector is a **discovery source only**. Every symbol-query match remains unverified until independently checked. A successful empty GDELT query means only “no match in the observed source/query window”; it is not proof of no material news across all sources. Blocked feeds, failed queries, missing timestamps, and unverified stories must remain `UNKNOWN` or explicitly unverified, never negative evidence.

Do not confuse the news lookback with the technical lookback. Historical price/volume remains necessary for relative strength, volatility, EMA, base/volume behaviour and out-of-sample validation.

## Frozen label

- **Primary:** `FUT1_HIGH_PCT >= 5.0` from the pre-declared decision reference price, using the next eligible trading session only.
- **Secondary:** next-session close return of at least +5%, when close-based label is separately available.
- Record the exact cutoff and reference price before observing the outcome. Use official NSE data where possible; apply corporate-action adjustments and mark unresolved cases `UNKNOWN`.
- Do not claim a target was tradable if entry timestamp, intraday path, liquidity, or circuit state is unknown. Daily OHLC cannot establish first-hour confirmation.

## Selection experiment

Run the audit-only target-first experiment using the frozen candidate universe and frozen `RANKING_SCORE`. Compare the pre-declared selectors (current winner probability, P10/P20 mean, P5/H1-only, and exhaustion-guarded P5/H1) on the same eligible cutoffs. The experiment may analyze candidates outside the existing Top-30 to expose missed winners, but must not edit production ranks, scores, or `+1 PRESSURE_FADE`.

## Metrics required

For each mature cutoff and the aggregate walk-forward sample, report selected count, true +5% movers, precision, recall/capture, false positives, missed winners, Top-10/Top-30 capture, unresolved labels, and sector/liquidity/circuit breakdown. Compare a price/volume-only baseline against the same baseline plus last-24-hour **independently verified, stock-specific** news; use identical dates, universe and labels. Include uncertainty and transaction-feasibility notes. Do not promote a selector based on retrospective results alone.

## Quarterly results / earnings layer — first-class research input

Quarterly results are a high-priority stock-specific catalyst and must be tracked each audit run, not added as a casual news tag. The workflow runs `pipeline/quarterly_results_research.py` after normalized NSE history QA and uploads the source ledger, upcoming board-meeting calendar, financial feature table, event-study output and a machine-readable report.

### Source and event rules
- NSE corporate financial-results filings are the primary discovery source; board-meeting notices are collected separately as forward calendar events. A scheduled meeting is never treated as an already-declared result.
- Preserve symbol, company, filing subject, broadcast timestamp, quarter/period, attachment/source URL, observation timestamp and raw-record SHA-256. If NSE blocks the request, changes its schema, or returns no recognizable records, mark source coverage `UNKNOWN/BLOCKED`; do not infer no results.
- Numeric actuals must enter through `data/raw/quarterly_financial_metrics.csv` with a primary-source filing URL, disclosure timestamp, period end and explicit `STANDALONE` or `CONSOLIDATED` basis. Headline text is not parsed into financial numbers. Duplicate symbol-period-basis rows block feature computation.
- Compare revenue, PAT and EPS year-on-year and quarter-on-quarter where valid history exists; track EBITDA margin, PAT margin, debt, interest expense and operating cash flow when disclosed. Calculate revenue/PAT/EPS surprise only when a timestamped, point-in-time analyst consensus value is actually available. Missing consensus is unknown, not a zero surprise.
- Event-study returns are descriptive and start from the first trading session strictly after the disclosure date to avoid assuming an intraday release time that the feed does not establish. This is not causal proof or a tradability claim.

### How results may affect selection research
- Treat results as a separate **earnings-quality / repricing catalyst layer** alongside technical lead-time, volume, sector/RS and verified news—not as an automatic buy signal.
- Distinguish positive revenue growth from earnings quality: PAT/EPS acceleration, margins, cash conversion, leverage/interest burden, guidance, and actual-versus-consensus surprise can diverge. Bank/NBFC metrics require sector-specific interpretation and should not be directly ranked against industrial-company margins.
- Test any earnings-aware +5% H+1 selector only with point-in-time disclosures available by each frozen cutoff. Use same-cutoff paired comparisons against the frozen baseline, with identical universe and mature labels; report coverage, missingness, precision, recall/capture, false positives and confidence intervals.
- Until source-linked historical financial metrics and as-of consensus coverage exist, the pipeline is **collection/feature-readiness research only**; it must not claim that quarterly results improved +5% H+1 performance.
- Audit branch only. Do not change production `RANKING_SCORE`, live selector, or frozen `+1 PRESSURE_FADE` until a leakage-safe paired ablation demonstrates repeatable out-of-sample lift.

## Macro-Geo hard gate — audit candidate release

The user has explicitly directed that Macro-Geo be a **hard gate**. On this audit branch, prospective/live candidate release is blocked unless all of the following pass:

1. Macro-Geo P0 coverage report says `P0_COMPLETE` and every required P0 group has a non-empty, QA-valid source.
2. The publication-time event study reports `COMPUTED_EXPLORATORY` or `COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS`, with at least one eligible event and at least one computed window.
3. Market-panel and NSE equity-panel dates are valid and aligned within the gate's declared tolerance.
4. Any missing, stale, invalid, blocked or incomplete critical evidence fails closed as `BLOCKED`; it must never be interpreted as a benign macro regime.

The gate is applied before the audit workflow generates its live prospective picks. Historical research and diagnostic artifacts may still be produced before the gate. This strict gate can intentionally withhold all candidate picks until source coverage is complete. It does **not** modify the production selector on the default branch and does not imply a causal relationship between geopolitics and returns.

## Freeze constraints

- Audit branch only.
- No production-selector changes and no `RANKING_SCORE` edits.
- No change to frozen `+1 PRESSURE_FADE`.
- The Macro-Geo hard gate applies to candidate release in this audit workflow; do not silently propagate it to the production branch.
- No future labels in ranking or prospective picks.
- No claim of intraday tradability from daily OHLC alone.
- News ablation is not complete until source-specific coverage is known, stories are independently verified, and a same-cutoff paired result artifact exists.
