# Walk-forward immature-horizon label propagation audit — 2026-11-14

## Scope
Read-only audit of `pipeline/walk_forward_backtest.py` on branch `research/corporate-events-rss-collector-v1-20261114`.
Source blob SHA: `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
This is a distinct downstream-label audit; it does not repeat or replace Appendix 55's forward-window alignment finding.

## Confirmed finding
In `main()`, the training labels are assigned as:
```python
for target,h in [("WIN5_H1",1),("WIN10_H3",3),("WIN20_H5",5)]:
    prior[target]=(prior[f"FUT{h}_HIGH_PCT"]>=threshold).astype(int)
train=prior.dropna(subset=prob_features+["WIN5_H1","WIN10_H3","WIN20_H5"])
```
A comparison of a missing/NaN future outcome against a numeric threshold evaluates False; converting that boolean to integer changes the unavailable outcome into label 0. The subsequent `dropna` on the integer label cannot recover the missingness. Thus, even after Appendix 55's proposed full-horizon NaN/UNKNOWN handling is implemented, immature symbol-specific H+1/H+3/H+5 rows can silently enter training as non-winners unless label construction is changed to preserve missingness.

## Downstream impact
- Training target populations and fitted/calibrated probabilities can be biased by false negative labels at immature per-symbol history boundaries.
- The issue is independent of the rolling-window alignment defect: correcting the forward window alone does not fix this label-casting behavior.
- A global cutoff based on the last five market dates does not guarantee every symbol has h subsequent observations where symbol histories are sparse, newly listed, or contain missing sessions.
- This audit does not quantify affected row counts because no source dataset was loaded or recomputed in this read-only review.

## Safe remediation design (not applied)
- Construct labels with a nullable/NaN-preserving operation: assign 1/0 only where the corresponding future outcome is finite and the full required horizon is mature; leave all other rows missing/UNKNOWN.
- Filter training rows separately for each target's mature label rather than requiring or manufacturing a common negative label. If a shared training population is deliberately required, document that choice and quantify the resulting sample loss.
- Add tests proving NaN outcomes remain missing after label construction; test symbol-specific terminal rows, sparse histories, all three horizons, and that no missing target is counted as a negative.
- Audit all metric denominators and calibration/separation paths to ensure immature outcomes are excluded from both winner and non-winner populations.
- Recompute affected training and validation artifacts only after both Appendix 55 alignment correction and this label-propagation correction pass tests.
- No code, data, selector, ranking, diagnostic, workflow, or production behavior was changed. No PR/merge.

## Status
- Scoped source/logic audit: 100% complete.
- Dataset-level impact count: NOT RUN (no data load).
- Corrective implementation and regression tests: 0% / NOT RUN.
- Refit and walk-forward rerun: 0% / BLOCKED pending approved research-only corrections.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED.
