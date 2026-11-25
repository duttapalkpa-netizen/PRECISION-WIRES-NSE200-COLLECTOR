# Missed-Winner Discovery & Research Integration — 25-Nov-2026

## User requirement
Every morning and nightly PRECISION-WIRES alert must do more than list prospective candidates. It must systematically discover stocks in the same eligible NSE universe that later achieved +2%, +5%, +10%, +15% or +20%, explain why they were not selected, and carry verified lessons into subsequent research alerts.

## Current evidence-backed explanation for the missed names
1. **No full-universe missed-winner denominator:** the available decision/outcome records do not currently provide a reconciled point-in-time eligible-universe ledger linked to every selector decision. Therefore we cannot yet enumerate all eligible stocks that later moved, or prove which exact stock was missed by which filter.
2. **Pre-market source failure:** the 25-Nov morning report recorded live 1-minute source HTTP 403, zero rows and zero symbols; qualified candidates were 0/5. This is a confirmed source-readiness failure in the retrieval path, not evidence that the market had no candidates or that the exchange had no data.
3. **Outcome maturity/session defect:** the 23-Nov shadow cohort had 7 unique symbols / 10 signal rows. The tracker used the next sorted date row and did not enforce the official exchange session spine; 24-Nov was a holiday. The 23-Nov H+1 outcome was due after 25-Nov close but remains PENDING until official EOD rows and exact horizon-end dates are independently reconciled.
4. **Historical label/archive integrity:** prior diagnostics are NOT_VALIDATED because 200 date labels represented only 187 unique content sessions, forward-label construction and maturity semantics were defective, and denominator/CI reconciliation was incomplete.
5. **Filter-level root cause remains UNKNOWN:** without timestamped point-in-time selector decision traces for the full eligible universe, it would be speculation to blame momentum, volume, sector, catalyst, liquidity, a CORE-672 filter or a ranking threshold. Do not retrofit hindsight explanations as predictive signals.

## Mandatory protocol for every alert
- Scan the full eligible NSE equity universe for matured H+1/H+3/H+5 outcomes at +2/+5/+10/+15/+20, using official session calendar, verified symbol/ISIN, exact cutoff, source vintage and raw price/high/close evidence.
- Separate unique symbols from signal rows; separate intraday high-touch, close-to-close hit and executable trade outcome.
- For each missed winner, reconstruct only information available at the original cutoff: price structure/trend, relative strength, volume/delivery, sector breadth, official catalyst/publication time, liquidity, circuit/surveillance and event risk.
- Trace the symbol through the existing selector/diagnostic decision record and record the exact filter/gate/rank only when the point-in-time trace proves it. Otherwise UNKNOWN.
- Classify root cause VERIFIED / SUPPORTED / HYPOTHESIS / UNKNOWN. Distinguish predictable pre-cutoff signals from unforeseeable post-cutoff catalysts, data defects, universe exclusions and non-tradeable spikes.
- Append evidence to an existing immutable lesson ID when duplicate; create a new ID only for a genuinely new failure mode. Add a leakage-safe, bounded observation-only test with sample/maturity threshold, acceptance criteria, expected artifact and blocker.
- Carry open lessons and acceptance tests into the next morning and nightly alert. Never use immature outcomes or future information as features.
- No single missed winner can justify a production filter/threshold change. Require repeated evidence and out-of-sample validation plus explicit user approval.
- If full-universe decision logs or outcome source are unavailable, state the exact missing universe/date/horizon coverage as UNKNOWN/BLOCKED; never imply no missed winners.

## Acceptance tests / next actions
1. **Point-in-time decision ledger audit:** prove one row per eligible symbol/cutoff with universe inclusion/exclusion, selector rank, per-filter PASS/FAIL/UNKNOWN, source timestamp and code/config hash. Expected: `point_in_time_decision_ledger_audit.json`.
2. **Calendar-aware outcome spine:** exact official next 1/3/5 sessions, reject holidays, duplicate/missing sessions, wrong symbol mapping and incomplete horizon. Require OUTCOME_LAST_DATE for every matured horizon. Expected: `calendar_aware_tracker_regression.json`.
3. **Universe-wide missed-winner reconciliation:** join accepted decision ledger to independently verified official EOD outcomes and produce target/horizon-wise false-negative/missed-winner rows. Expected: `universe_missed_winner_reconciliation.json`.
4. **Root-cause and learning loop:** cutoff-only feature/catalyst reconstruction, repeated-pattern counts, evidence classification and lesson-register linkage. Expected: `missed_winner_root_cause_audit.json`.

## Status
- Root cause of current inability to identify individual missed winners: PARTIALLY EXPLAINED (missing full-universe point-in-time decision ledger, live-source 403, unresolved calendar-aware outcomes and historical label integrity).
- Individual missed stock names and exact filter failures: UNKNOWN pending reconciled evidence.
- Research integration: specification documented; implementation and tests OPEN.
- Production logic: unchanged. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.
- Constraints: ₹0; free official sources only; no paid APIs; no synthetic data, guessed mappings, fabricated timestamps, forward-fill or look-ahead leakage; observation-only.

This report records a research requirement and evidence-backed diagnosis. It does not claim that automation prompts, tracker code or production logic have been updated.
