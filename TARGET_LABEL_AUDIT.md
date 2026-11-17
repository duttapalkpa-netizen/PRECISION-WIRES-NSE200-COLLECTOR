# Corrected Forward Target Labels — Audit Only

## Safety boundary
This branch starts from frozen baseline `4188644b59e3aa335d23911a8bd250865afda871`.
It is isolated from `main`. No production ranking weights, the `PRESSURE_FADE` +1 adjustment, candidate-selection rules, collector, or 672-diagnostic definitions are intentionally changed.

## Defects addressed for validation
1. The former `shift(-1).rolling(h)` target calculation applied a trailing rolling window to shifted data; for horizons greater than one it did not reliably compute the maximum over exactly T+1..T+h.
2. Incomplete future horizons were compared to thresholds and cast to integer, silently becoming negative labels.
3. Historical metrics and probability calibration could count missing outcomes as non-winners.
4. A training row's forward label could mature after the current walk-forward cutoff, leaking outcomes from the future into the model fit. Training now requires the label's final outcome date to be strictly before the cutoff.
5. Evaluation now reports +5% H+1, +10% H+3, +15% H+5, and +20% H+5 with complete-case denominators. +15% is an evaluation target only; it is not a new ranking feature or weight.

## Validation
Run the manual GitHub Actions workflow **Audit-only Corrected Target Label Walk-Forward**. It runs synthetic regression tests, rebuilds/validates the NSE dataset, then runs the same expanding-window walk-forward engine with corrected targets and unchanged ranking formula.

## Promotion gate
Do not merge to `main` or use these outputs as production performance claims until:
- synthetic forward-window tests pass;
- strict data QA passes;
- 100-session walk-forward completes;
- precision, recall, base rate, lift, calibration, and missed-winner analysis are reviewed against the previous frozen run;
- the corrected-label results demonstrate out-of-sample improvement without unacceptable false-positive growth.

No model can guarantee detection of every future 5–20% winner. The goal is measured recall improvement with controlled precision and risk.
