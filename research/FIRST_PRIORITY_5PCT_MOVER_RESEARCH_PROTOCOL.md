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
