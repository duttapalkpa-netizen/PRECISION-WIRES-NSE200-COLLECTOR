# Run #407 — Source Denominator and H+5 Serialization Reconciliation
Date: 2026-11-20

## Scope and provenance
- Existing artifact only; no new NSE collection, workflow dispatch, backtest rerun, or production change.
- Workflow run #407 / ID 44542948987; source commit d013577157bc1f24322cd100aaf60c40a20c4d17.
- Artifact ID 14539426731; ZIP SHA-256 b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7 (matches GitHub digest).
- Re-read pipeline/walk_forward_backtest.py at the exact source commit and inspected the processed dataset and exported prediction/universe CSVs in the ZIP.

## Exact row-membership reconciliation
The source builds each cutoff candidate frame as:
1. rows at the cutoff date;
2. non-null TOMORROW_EXPANSION_SCORE;
3. HISTORY_DEPTH_AT_T >= 20.

The exported walk_forward_universe_probabilities.csv has 251,724 rows. Reconstructing the 100 cutoff dates from the raw 200-session dataset gives:
- all_by_date rows used by metrics: 257,696;
- rows with HISTORY_DEPTH_AT_T >= 20: 251,724;
- excluded short-history rows: 5,972;
- export key comparison on (CUT_OFF, SYMBOL): 0 missing keys, 0 extra keys, 0 duplicates.
Thus the 5,972-row membership difference is fully explained by the >=20 history eligibility filter. The metrics source denominator uses all raw cutoff-date rows, whereas the exported probability table is eligibility-filtered.

## Reconstructed raw-source outcome denominators
Using the source's future_outcomes definition (future HIGH_PRICE, shift(-1), rolling max over horizons 1/3/5) on the archived processed dataset:
- all_by_date rows = 257,696.
- T5_H1: 23,616 winners; 193 null labels.
- T10_H3: 10,418 winners; 0 null labels.
- T20_H5: 2,096 winners; 0 null labels.
Eligible exported-universe winner counts are respectively 22,519; 9,735; 1,964.

## Top-30 metrics reconciliation
Prediction CSV counts:
- T5_H1: 648 hits; JSON precision 21.60%; agrees.
- T10_H3: 1,198 hits; JSON precision 39.9333%; agrees.
- T20_H5: 612 hits; CSV precision 20.40%; JSON precision is 20.30%, implying 609 hits. This 3-hit discrepancy remains unresolved.

The JSON recall/base-rate values align with its stated all_by_date scope for T5_H1 and T10_H3. For T20_H5, JSON base rate 0.813361% implies 2,096/257,696 winners, but JSON recall 29.05534% does not equal either 609/2,096 or 612/2,096. Recomputed source-scope recall from prediction CSV hits is 612/2,096 = 29.19847%. Therefore the T20_H5 JSON precision/recall pair is internally inconsistent with the archived prediction CSV and denominator count.

## Paired cutoff-cluster bootstrap
20,000 resamples; 100 cutoff clusters resampled as paired units; seed 20261120; percentile 95% intervals. These are reconstructed from the archived prediction CSV and raw dataset:
- T5_H1: precision 21.6000%, 95% CI [19.3333%, 24.0667%]; recall 2.74390%, CI [2.4950%, 3.0246%]; lift 2.35698x, CI [2.14014x, 2.60041x].
- T10_H3: precision 39.9333%, CI [36.8000%, 43.1667%]; recall 11.49933%, CI [10.8224%, 12.2239%]; lift 9.87777x, CI [9.33142x, 10.46156x].
- T20_H5: precision 20.4000%, CI [18.3000%, 22.6333%]; recall 29.19847%, CI [26.5144%, 32.1632%]; lift 25.08110x, CI [22.80528x, 27.56944x].
The T20_H5 figures are provisional because of the unresolved 3-hit mismatch in JSON. T5/T10 precision and source-scope recall arithmetic reconcile.

## Decision
- Row membership reconciliation: PASS for the 5,972-row scope difference.
- T5_H1 and T10_H3 source-scope metric reconciliation: PASS at aggregate arithmetic level.
- T20_H5 metric serialization consistency: BLOCKED (3-hit difference; JSON recall does not reconcile).
- Full artifact reproducibility: PARTIAL; source dataset manifest is absent from ZIP.
- No production selector/ranking/pressure-fade/CORE-672/engine changes. No shadow challenger started until the T20_H5 discrepancy and manifest limitation are resolved.
- No new data collection or workflow dispatch. ₹0; UNKNOWN is never PASS.

## Next action
Trace why the archived metrics JSON records 609 T20_H5 hits while the prediction CSV records 612, using exact workflow job logs, artifact timestamps, and source/output provenance. If the retained evidence cannot identify the cause, preserve T20_H5 as BLOCKED and request an approved bounded audit-only export from the existing processed dataset; do not recollect NSE data.
