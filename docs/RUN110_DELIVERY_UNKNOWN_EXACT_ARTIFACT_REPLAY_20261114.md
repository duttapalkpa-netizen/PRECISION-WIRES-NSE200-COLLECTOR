# Run 110 Exact Artifact Replay — Missing Delivery Evidence
Date: 2026-11-14
Scope: retrieve and inspect the exact GitHub Actions artifact referenced by issue #27; recompute delivery rolling fields from the archived input dataset; reconcile to the archived walk-forward output. No model rerun and no source/production code change.

## Artifact identity and integrity
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Workflow run ID: `42622884559` (Run #110)
- Job: `collect-and-test`; conclusion: `success`
- Artifact ID: `13678590181`
- Artifact name: `precision-wires-adaptive-110`
- ZIP size: 61,442,608 bytes
- ZIP SHA-256: `02422a83c781e28dde568574e6f65a71d311a871b88c7095ed1169bd7c8dc8c7`
- This matches the SHA-256 already recorded in issue #27.
- Archived input: `data/processed/nse_eq_200_sessions.csv`; 500,808 rows × 21 columns; SHA-256 `51bb6875fe1ec4474c73feefd99e49c37c9eaacec7735f18b34f72f639040a4c`.
- Archived walk-forward universe probabilities: 249,473 rows; 100 distinct cutoff dates.
- ZIP contains the original dataset, walk-forward outputs, QA report and calibration/backtest outputs.

## Exact replay of delivery rolling fields
Recomputed from the archived dataset after sorting by SYMBOL, DATE, using the source-code formula:
`DELIV20 = rolling(20, min_periods=5).mean(DELIV_PER)`
and
`DELIV_GAP = DELIV_PER - DELIV20`.

Across the 100 walk-forward cutoff dates:
- Universe observations: 255,082.
- Raw `DELIV_PER` missing observations: exactly 2.
- Both are `GSEC10ABSL`: 2026-09-11 and 2026-09-14.
- For these rows, DELIV20 was available (93.7042105263 and 93.4205555556 respectively), but current DELIV_PER was missing, so DELIV_GAP was UNKNOWN/NaN.
- Additional rows with non-missing current DELIV_PER but unavailable 20-row rolling baseline (`DELIV20` NaN due to the five-valid-observation minimum): 1,269.
- Total cutoff rows with DELIV_GAP NaN: 1,271 (2 raw current-delivery missing + 1,269 rolling-baseline unavailable). These two causes must not be conflated.

## Downstream behavior confirmed for the two issue-reported rows
For both GSEC10ABSL cutoff rows:
- ABSORPTION delivery component: `25 * (NaN >= 0).astype(int)` = 0 points. This is the same numeric result as a negative gap, so evidence-state is lost at this component.
- REPRICING_PRESSURE delivery subcomponent: `clip(50 + fillna(0)*3, 0, 100)` = 50 (neutral midpoint); its 20% weighted term contributes 10 points to the composite before the outer sum/clip.
- WINNER_INTERACTION_SCORE: archived value is NaN for both dates because the delivery interaction has no missing-value handling.
- Archived RANKING_SCORE remains finite: 7.0868191099 on 2026-09-11 and 8.3152488958 on 2026-09-14. This matches inspected source: current RANKING_SCORE formula excludes WINNER_INTERACTION_SCORE.
- Archived outcomes: H+3 high return +0.212333% on 2026-09-11 and 0.000000% on 2026-09-14; neither is a +10% H+3 winner. These are observed archived outcomes, not counterfactual estimates.

## Impact boundary
- Proven exactly: two raw missing delivery observations in the 100 cutoff-date universe; 1,269 further rolling-baseline unavailable rows; 1,271 total DELIV_GAP UNKNOWN rows.
- Proven exactly: the two GSEC10ABSL rows have zero ABSORPTION delivery points, neutral 50 repricing subcomponent, NaN interaction score and finite current RANKING_SCORE.
- Not claimed: a counterfactual score/hit-rate change from imputing delivery. No imputation or alternate policy was run.
- Not claimed: all 1,271 NaN interactions arise solely from raw missing DELIV_PER; most are rolling-baseline unavailable. Other interaction inputs may also independently affect NaN propagation.
- The archive's feature_ablation_effects.csv is historical run output; its metrics are not re-labelled as a missing-delivery counterfactual.

## Acceptance matrix
| Criterion | Result |
|---|---|
| Exact Run 110 artifact retrieved | PASS |
| ZIP SHA-256 matches issue #27 evidence | PASS |
| Archived input dataset digest captured | PASS |
| Two raw missing delivery rows independently reproduced | PASS |
| Rolling-baseline missingness separated | PASS |
| Archived downstream values reconciled for both rows | PASS |
| Counterfactual performance impact | NOT_RUN / UNKNOWN |
| UNKNOWN delivery policy | UNRESOLVED; approval required |

## Next admissible step
Owner decision is still required on how UNKNOWN delivery evidence is represented in feature construction and ablation. After policy approval, run a separate, clearly labelled counterfactual replay against this exact frozen input and compare affected feature rows and target metrics. Until then, do not impute, change formulas or promote this audit to a policy PASS.

## Safety
No code change, workflow rerun, data imputation, PR, merge, production integration, paid source, or external contact. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, Engines A–E and Hard Gate remain untouched.
