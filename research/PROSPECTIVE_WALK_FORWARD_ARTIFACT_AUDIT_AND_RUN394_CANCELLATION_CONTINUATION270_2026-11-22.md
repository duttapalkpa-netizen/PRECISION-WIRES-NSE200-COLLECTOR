# Prospective Walk-Forward Artifact Audit and Run #394 Cancellation — C270

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Continuity check
Re-fetched `research/GITHUB_MASTER_CONTINUITY_LEDGER.md`, C269 and C268 before acting. PASS work was skipped. Current active dependency Run #318 was re-polled and remains IN_PROGRESS; no edits were made to its collector or workflow.

## Run #394 outcome
- Actions run ID: `45014759398`, run #394, head SHA `399b0a61535f84bfbee8347321e51c590ff9ff55`.
- Final status: `cancelled`, updated at `2026-11-22T11:05:48Z`.
- Steps 1–14 succeeded, including corrected-label walk-forward audit.
- Step 15 P0 market panel/timestamped geopolitical news was cancelled.
- Steps 16 onward (Macro-Geo repair, source coverage, event study, frozen selector diagnostics, historical cutoff comparisons, target-first experiment, strict gate, prospective picks and ledger persistence) were skipped.
- Artifact upload succeeded. Artifact ID `14751329364`, name `prospective-watchlist-audit`, size 31,123,774 bytes.
- Downloaded artifact SHA-256 independently computed as `d8086fd085dcd59317354a2d00bc79fd17efe45a0d4503f3f9d85979ff2d5bb4`, matching GitHub's artifact digest.

## Artifact QA and acquisition
- `data/qa/qa_report.json`: PASS; 200 raw files, 200 sessions, 2,999 symbols, 100% delivery quantity and delivery percentage coverage, no issues.
- `outputs/prospective/acquisition_manifest_validation.json`: PASS; 200 manifest entries, all 200 retained files verified and fully provenanced, no errors.
- These are scoped acquisition/QA passes only; they do not imply a complete prospective selector or Macro-Geo acceptance.

## Walk-forward metrics extracted from artifact
File: `outputs/backtest/walk_forward_metrics.json`.
- Engine label: V11.4 Historical Winner Separation Engine.
- Requested/tested: 100/100 sessions; 3,000 candidate rows; Top-N=30.
- Top-30 precision: T5_H1 32.43%, T10_H3 22.03%, T15_H5 14.10%, T20_H5 6.96%.
- Base rates: 9.17%, 6.83%, 4.87%, 2.20%; reported lift: 3.54x, 3.23x, 2.89x, 3.17x respectively.
- Recall: 4.08%, 3.62%, 3.19%, 3.49% respectively.
- Full-universe probability calibration sample sizes: T5_H1 n=251,843; T10_H3 n=251,478; T20_H5 n=251,097. Reported Brier scores: 0.08013, 0.06153, 0.02059; ECE: 0.01501, 0.00369, 0.00022.
- Critical diagnostic: reported winner/nonwinner mean probability separation is near zero or negative for the Top-30 aggregate (winner mean 0.086886 vs nonwinner 0.087184). Winner-specific interaction means are also close (63.941 vs 63.788), and latent-winner evidence means are virtually identical (93.938 vs 93.935). This cautions against interpreting the high Top-30 lift as strong calibrated probability separation. The metric artifact needs independent methodology/label audit before any selector adoption.
- These are historical target-hit classification metrics, not profitable trade returns. No transaction costs, slippage-adjusted P&L, drawdown or execution-return acceptance is evidenced by this file. Do not call them profits or production performance.
- The 50 matured observations per State rule remains in force for H+3 Behavioral DNA calibration; this artifact's aggregate rows do not establish that state-specific threshold.

## Run #318 live state at C270 inspection
Run ID `45014759390`, run #318, head SHA `399b0a61535f84bfbee8347321e51c590ff9ff55`: still `in_progress`; job `137184585110`. Steps 1–7 SUCCESS; step 8 “Collect P0 market series and timestamped media evidence” IN_PROGRESS; NSDL step 11 not reached. No artifact/conclusion available. Do not modify its active workflow/collector or dispatch duplicates.

## Exact next actions
1. Continue polling Run #318; inspect steps 8–19 and artifact only after completion. Verify NSDL attempt log and final status `AVAILABLE_WITH_GAPS` where appropriate; verify artifact SHA-256.
2. Inspect walk-forward metric generation/label methodology for the weak winner/nonwinner probability separation and reconcile the reported Top-30 lift against exact matured labels. Keep exploratory metrics separate from trade returns.
3. After Run #318 no longer active, wire `qa.test_macro_geo_nsdl_flows` into the workflow's existing regression command and run targeted CI; do not create a duplicate concurrent Macro-Geo run.
4. Continue official NSDL date-response and FBIL daily USD/INR archive verification; do not infer missing flow values or use monthly averages as daily observations.
5. Keep event windows pending until actual post-publication NSE closes exist; re-run strict hard gate only after source evidence changes.

## Rejected / guardrails
- Run #394 cancellation is not a walk-forward failure: the walk-forward step itself completed SUCCESS; the following P0 collection was cancelled.
- Skipped downstream steps are not PASS and no prospective picks were released.
- No adoption of V11.4 ranking or production selector changes from this artifact.
- No synthetic observations, paid sources, third-party mirrors, inferred event returns or gate relaxation.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E remain unchanged.
