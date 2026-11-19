# Run #407 — T20_H5 JSON/CSV Forensic Trace (Part 1)
Date: 2026-11-20

## Scope
Read-only forensic continuation using only the already archived GitHub Actions artifact and the exact source commit. No workflow dispatch, no new NSE collection, no backtest rerun, no production code change.

## Exact provenance
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Run #407 / run ID: `44542948987`
- Job: `collect-and-test`, job ID `135625864171`, conclusion SUCCESS
- Source commit: `d013577157bc1f24322cd100aaf60c40a20c4d17`
- Artifact ID: `14539426731`, name `precision-wires-adaptive-407`
- Artifact created: `2026-11-19T14:28:44Z`; expires `2027-02-17T14:22:02Z`
- GitHub artifact SHA-256 and independently rechecked ZIP SHA-256: `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`
- Prediction CSV SHA-256: `06dc89983aa748bae5e03eee8e3ad4be5bd2add008e5b00dc350e5e65399d843`
- Metrics JSON SHA-256: `9a79719ec8482953044cae38b6ab9329c20849fef64b69dfd85e81c3d3b99061`

## Workflow-log and archive trace
- Job log shows `pipeline/walk_forward_backtest.py` started at `2026-11-19T14:24:44.027Z` with `WF_SESSIONS=100`.
- The metrics JSON printed by that process at `2026-11-19T14:27:20.180Z` records `T20_H5 precision = 0.203` (609/3,000 implied).
- Artifact ZIP lists both `walk_forward_predictions.csv` and `walk_forward_metrics.json` with the same ZIP timestamp `2026-11-19 14:27:18` (ZIP timestamp precision is one second; it cannot establish sub-second write order).
- The same job subsequently uploaded artifact `precision-wires-adaptive-407`; the upload log reports the same SHA-256 as GitHub's artifact metadata.
- The successful job's steps show one walk-forward invocation followed by later pipeline stages and artifact upload. No second walk-forward invocation is recorded in the job steps/log segment reviewed.

## Independent archived-file recomputation
- Prediction CSV: 3,000 rows, 100 cutoffs × 30; 3,000 unique (CUT_OFF, SYMBOL) keys; zero duplicate keys.
- Recomputed `FUT5_HIGH_PCT >= 20` from the archived CSV: **612 hits / 3,000 = 20.40%**.
- Recomputed per-cutoff ledger: 100 cutoffs, exactly 30 rows per cutoff, total 612 hits. The cutoff-level sum reconciles to the row-level CSV count.
- H+1 and H+3 controls reconcile: 648/3,000 = 21.60%; 1,198/3,000 = 39.9333%, matching JSON.

## Exact source-code trace
At source commit `d013577157bc1f24322cd100aaf60c40a20c4d17`, `pipeline/walk_forward_backtest.py`:
- Lines 687–689 write `universe_pred`, then `pred` to the prediction CSV.
- Lines 697–705 calculate target hits from the same `pred` DataFrame using `(pred[FUT{h}_HIGH_PCT] >= t).sum()`, with precision divided by `len(pred)`.
- Lines 766–769 write and print `walk_forward_metrics.json`.
- Therefore, for an unchanged `pred` object, the JSON T20_H5 precision should equal the CSV recomputation. The archived evidence instead shows 609 implied by JSON versus 612 in CSV.

## Forensic conclusion
**T20_H5 serialization discrepancy remains BLOCKED / ROOT CAUSE NOT ESTABLISHED.**
The archived CSV independently and reproducibly supports 612/3,000 (20.40%). The run log and metrics JSON support 0.203 (609/3,000). The source-code path reviewed should calculate from the same `pred` object that was exported, so the discrepancy cannot be explained by the documented 5,972 short-history-row exclusion, the all_by_date recall denominator, or a simple CSV duplicate-key issue. ZIP timestamps are too coarse to prove whether one output was stale or overwritten. Do not choose 609 or 612 as the definitive serialized metric until an independent bounded audit resolves the provenance break.

## Next bounded research action
Prepare an audit-only, existing-artifact replay/export that emits a 100-row cutoff ledger with:
1. per-cutoff Top-30 row count and T20_H5 hit count;
2. the exact ordered `(CUT_OFF, SYMBOL, FUT5_HIGH_PCT)` membership fingerprint;
3. raw-source and eligible-universe winner counts per cutoff;
4. output SHA-256 values and an explicit assertion that JSON precision equals CSV-derived hits / Top-30 rows.
Use only the already archived processed dataset and exact source commit. No new NSE download, no workflow dispatch, no production selector/ranking/pressure-fade/CORE-672/engine change. If the replay cannot reproduce the archived output pair, retain BLOCKED and report the divergence; do not silently rewrite the historical artifact.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. No new data collection or workflow dispatch. UNKNOWN is never PASS.
