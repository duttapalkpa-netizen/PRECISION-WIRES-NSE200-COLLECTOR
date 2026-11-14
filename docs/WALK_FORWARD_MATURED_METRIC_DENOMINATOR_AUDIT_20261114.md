# Walk-forward matured-outcome metric denominator audit — 2026-11-14

## Scope
Distinct downstream evaluation audit of `pipeline/walk_forward_backtest.py`, source blob `d085f7a2d35a88b4c4eaba65144a429a06961b09`, branch `research/corporate-events-rss-collector-v1-20261114`. This audit follows Appendix 56 but is not a repeat: it inspects validation/calibration metric populations after outcomes are exported.

## Confirmed findings
1. Top-N precision at lines 697–705 uses `hits / len(pred)`. `pred` can contain rows whose H+3/H+5 outcome is unavailable; comparisons of NaN with thresholds are false, while `len(pred)` still counts those rows. Precision can therefore be diluted by immature observations.
2. Universe winner counts use `(all_by_date[FUT... ] >= threshold).sum()`, which omits NaN comparisons from the numerator, but base-rate denominator is `len(all_by_date)`, which includes immature rows. Base rate is therefore computed on a different population than the mature-outcome numerator.
3. Recall uses Top-N hits divided by universe winners. Even if numerator and universe-winner count are mature-only, Top-N precision and base-rate denominators are not aligned to that mature population; reported precision/recall/lift can be internally inconsistent.
4. State performance at lines 710–712 and transition-signature performance at line 724 compute Boolean means over all rows in each group. NaN outcomes compare False, so immature outcomes are counted as non-winners in hit-rate denominators.
5. Winner/non-winner separation at lines 716–719, 725–727 and diagnostic separation at lines 746–750 use threshold comparisons that treat missing outcomes as False for the non-winner group. Immature outcomes can contaminate non-winner means and diagnostic lift.
6. Full-universe calibration at lines 730–734 casts threshold comparisons to integer labels. Missing outcomes are converted to class 0, reproducing the missing-to-negative issue from Appendix 56 in the calibration/evaluation path as well.
7. Missed-winner attribution at lines 635–637 only creates rows for positive comparisons; missing outcomes are not explicit UNKNOWN and can disappear from the missed-winner audit without a separate maturity accounting.

## Impact boundary
- These are denominator/label-population integrity defects in the inspected script. The direction and magnitude of metric distortion cannot be quantified without running the actual source dataset.
- H+1/H+3/H+5 each need an independent maturity mask; do not assume a global date cutoff proves per-symbol maturity.
- The existing forward-window alignment defect (Appendix 55) and missing-label conversion defect (Appendix 56) remain separate blockers. This audit does not correct either.
- No dataset was loaded, no metrics were recomputed, and no code/data/workflow/selector/ranking/diagnostics/production behavior was changed.

## Safe remediation design (not applied)
- For each horizon, create an explicit `mature_h` mask requiring a finite, complete future window for that symbol.
- Compute precision only over mature Top-N rows; compute universe base rate over mature universe rows; compute recall with mature winners from the same cutoff/universe definition.
- Apply the same per-horizon maturity mask to state, transition, diagnostic, calibration, winner/non-winner separation, ablation, and missed-winner reporting.
- Preserve immature outcomes as UNKNOWN/NaN and report mature and immature counts separately; never coerce missing target labels to 0.
- Add tests where a Top-N cohort contains mature winners, mature non-winners and immature rows; verify denominator arithmetic exactly for each horizon and all group metrics.
- After Appendix 55 and 56 corrections plus this denominator correction pass tests, rerun all dependent metrics from source data and retain superseded outputs separately.

## Status
- Scoped source/logic audit: 100% complete.
- Dataset-level affected-row/metric quantification: NOT RUN.
- Corrective code and regression tests: 0% / NOT RUN.
- Full backtest and calibration rerun: 0% / BLOCKED.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No PR/merge.
