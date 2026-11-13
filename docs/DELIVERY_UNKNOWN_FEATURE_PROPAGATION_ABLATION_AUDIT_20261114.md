# Missing Delivery Evidence — Downstream Feature and Ablation Impact Audit
Date: 2026-11-14
Scope: static source audit of the default-branch `pipeline/walk_forward_backtest.py`, with a bounded numerical semantics check. No source or production code changed.

## Inspected source
- File: `pipeline/walk_forward_backtest.py`
- Blob SHA: `d085f7a2d35a88b4c4eaba65144a429a06961b09`
- Relevant lines (1-based): 57–58, 72–79, 155–161, 352–359, 470–493, 523–540, 560 onward.
- Existing open issue: #27, "Audit inconsistent handling of missing delivery evidence in historical features". Its evidence bundle SHA-256: `8796442a8b1ab6adc8647aed5b1116c89d9a0442b9c56feee4c2d61dd9aca2eb`.

## Confirmed missingness pathways
1. `DELIV20` is a 20-row rolling mean with `min_periods=5`; `DELIV_GAP = DELIV_PER - DELIV20`. Missing current delivery or insufficient valid history can produce NaN.
2. `ABSORPTION` awards 25 points for `(DELIV_GAP >= 0).astype(int)`. In pandas/NumPy semantics, NaN comparison is False, so missing delivery evidence contributes 0 points (indistinguishable from a negative delivery gap at this component).
3. `REPRICING_PRESSURE` computes its delivery component using `DELIV_GAP.fillna(0)`; missing evidence is converted to the neutral midpoint 50 before the 20% weighting. Thus the same missing observation is penalized in ABSORPTION but neutralized in REPRICING_PRESSURE.
4. `_winner_interaction_score` computes `delivery = clip(50 + DELIV_GAP*3)` without a missing-value branch. A NaN delivery gap therefore makes the delivery interaction NaN; the mean of the six interactions becomes NaN.
5. The current walk-forward `RANKING_SCORE` formula is explicitly the three-component combination of SEPARATION_SCORE (0.4375), RARE20_SPECIALIST_SCORE (0.3750), WINNER_PROBABILITY_PCTL (0.1875), plus state adjustment. It does not include WINNER_INTERACTION_SCORE.
6. The counterfactual `_feature_ablation_scores` still includes WINNER_INTERACTION_SCORE (10%) and LATENT_WINNER_EVIDENCE (10%) in the ablation variants, including DROP_STATE_ADJUSTMENT. The current variant is `RANKING_SCORE`; non-current ablation variants can therefore be affected by NaN interaction scores when delivery evidence is missing. This can distort diagnostic ablation comparisons even though the current ranking formula excludes the interaction component.

## Bounded semantics check
- `NaN >= 0` evaluates False in the feature's comparison pathway.
- `fillna(0)` maps missing delivery gap to a 0 gap, yielding the neutral midpoint 50 in the repricing delivery subcomponent.
- `clip(50 + NaN*3)` remains NaN; arithmetic mean including NaN remains NaN.
- These are language/library semantics, not an estimate of affected stock count or performance impact.

## Impact boundary
- Confirmed: missing delivery evidence is represented inconsistently across ABSORPTION, REPRICING_PRESSURE and WINNER_INTERACTION_SCORE.
- Confirmed: current walk-forward RANKING_SCORE excludes WINNER_INTERACTION_SCORE in the inspected source revision.
- Confirmed: counterfactual ablation variants include WINNER_INTERACTION_SCORE and can become NaN-affected.
- Not established: number of cutoff-symbol rows affected in Run 110 or any other historical run; this requires exact historical input/artifact replay.
- Not established: effect on Top-30 precision/recall or target hit rates; no replay was run.
- Existing issue #27 reports two missing observations for GSEC10ABSL on 2026-09-11 and 2026-09-14 in Run 110. This audit does not independently re-download or recompute that artifact.

## Acceptance matrix
| Check | Result |
|---|---|
| Missingness propagation in DELIV_GAP | PASS — semantics mapped |
| ABSORPTION missing-value behavior | CONFIRMED — 0 points |
| REPRICING_PRESSURE missing-value behavior | CONFIRMED — neutral 50 subcomponent |
| Winner interaction missing-value behavior | CONFIRMED — NaN score |
| Current RANKING_SCORE dependency on interaction | NO — excluded in inspected revision |
| Counterfactual ablation sensitivity | CONFIRMED — interaction component retained |
| Historical affected-row count / metric delta | UNKNOWN — no run artifact replay |
| Policy for UNKNOWN delivery evidence | UNRESOLVED — requires explicit approval |

## Recommended next action (not applied)
Define one explicit missing-evidence contract for delivery:
- preserve raw missingness and an explicit evidence-state flag;
- do not map UNKNOWN to negative, neutral or positive;
- decide whether affected rows are excluded from a feature, marked UNKNOWN, or make the relevant feature unavailable;
- apply the same approved contract to all dependent features and counterfactual ablations;
- only then replay the exact Run 110 input and compare pre/post feature values and metrics.
No code change is recommended before policy approval.

## Safety
No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 diagnostics, Engines A–E or Hard Gate changed. No data was imputed, no workflow run started, no PR opened/merged, no external contact or paid source used.
