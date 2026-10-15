# First-Priority Research: H+1 +5% Movers

**Branch:** `audit/prospective-selector-tracking`  
**Status:** audit-only research protocol; not a production-selector change.

## Research question

Can the existing V11.3 candidate universe identify stocks whose **next eligible session's high is at least 5% above the decision reference price**? This is the first-priority outcome. H+3 +10% and H+5 +20% remain secondary outcomes and must not dilute the primary objective.

## News window

For the catalyst/news feature, use only articles and filings published during the **24 hours before the frozen decision cutoff**. Store the canonical source URL, publication timestamp with timezone, publisher, headline, and verification state. Use exchange/company primary disclosures where available, then Reuters, AP, BBC, Al Jazeera, Bloomberg and reputable Indian business sources. Deduplicate syndicated headlines. No fresh verified story means `NO_MATERIAL_NEWS`; blocked feeds or missing timestamps mean `UNKNOWN`, not a negative catalyst.

Do not confuse the news lookback with the technical lookback. The stock's historical price/volume series is still needed for relative strength, volatility, EMA, base/volume behaviour and fair out-of-sample validation.

## Frozen label

- **Primary:** `FUT1_HIGH_PCT >= 5.0` from the pre-declared decision reference price, using the next eligible trading session only.
- **Secondary:** next-session close return of at least +5%, when close-based label is separately available.
- Record the exact cutoff and reference price before observing the outcome. Use official NSE data where possible; apply corporate-action adjustments and mark unresolved cases `UNKNOWN`.
- Do not claim a target was tradable if the entry timestamp, intraday path, liquidity, or circuit state is unknown. Daily OHLC cannot establish first-hour confirmation.

## Selection experiment

Run the existing audit-only target-first experiment using the frozen candidate universe and frozen `RANKING_SCORE`. Compare its pre-declared selectors (current winner probability, P10/P20 mean, P5/H1-only, and exhaustion-guarded P5/H1) on the same eligible cutoffs. The experiment may analyze candidates outside the existing Top-30 to expose missed winners, but it must not edit production ranks, scores, or `+1 PRESSURE_FADE`.

## Metrics required

For each mature cutoff and the aggregate walk-forward sample, report selected count, true +5% movers, precision, recall/capture, false positives, missed winners, Top-10/Top-30 capture, unresolved labels, and sector/liquidity/circuit breakdown. Compare a price/volume-only baseline against the same model plus last-24-hour news; use identical dates, universe and labels. Include uncertainty and transaction-feasibility notes. Do not promote a selector based on retrospective results alone.

## Macro/geopolitical study relationship

The Macro-Geo event study is secondary context research. It must not block the primary H+1 +5% experiment. Event records beyond the latest available market close are pending and excluded from computed returns until mature; pre-panel events are separately excluded. If no mature event window exists, the operational pipeline may pass while research remains blocked. Never manufacture prices or classify missing inputs as negative evidence.

## Freeze constraints

Audit branch only. No production-selector changes, no `RANKING_SCORE` edits, no change to the frozen `+1 PRESSURE_FADE`, and no Macro-Geo hard gates. Promotion requires mature prospective validation, missed-winner analysis, liquidity/circuit feasibility, and documented approval.
