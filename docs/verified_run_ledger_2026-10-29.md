# Verified Run Ledger — 2026-10-29

Purpose: reuse passed evidence and prevent repeated fixes. A GitHub workflow PASS does **not** imply research hard-gate PASS.

| Workflow | Run | Commit | Result | Reuse rule |
|---|---|---|---|---|
| Macro Geo Fast QA | [#47](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40898402939) | `1d1fa66d7d331a07b72df79a844e5dcb80c14ed4` | SUCCESS | Do not rerun without relevant code/contract changes |
| Brent Live Smoke | [#16](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40899280574) | `31ac5ad524b0cddf224236121e74010387c22663` | SUCCESS | Collector-reported path/freshness tested; no unchanged rerun |
| Macro Geo P0 Event Study | [#210](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40898379422) | `57c6b4aec7545aace7c3f11aeee92fc200cc7207` | Workflow SUCCESS; research BLOCKED | Reuse artifact 12908992135; do not conflate workflow and gate |
| Brent Live Smoke | [#15](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40898379576) | `57c6b4aec7545aace7c3f11aeee92fc200cc7207` | FAILURE, resolved in #16 | Hardcoded canonical filename mismatched Yahoo BZ=F proxy output |

## Verified outstanding research blockers
- Macro-Geo P0: 7/8; `corporate_events` remains unavailable; no usable validated official NSE rows.
- Factor Registry: 35 groups, zero fully available; 21 disconnected.
- Historical regime windows: 9/11 anchors.
- Event study incomplete. Candidate release **BLOCKED**.
- Preserve selector, `RANKING_SCORE`, `+1 PRESSURE_FADE` and strict UNKNOWN semantics.

## Next target
Inspect `pipeline/quarterly_results_research.py` and its actual NSE endpoint diagnostics, then repair **only** corporate-events source/schema/provenance with focused mocked and bounded live tests. Do not rerun the full P0 workflow until a changed targeted test and real evidence justify it.

## Run discipline
1. Before any rerun, compare changed paths, head SHA, test contract and prior passing evidence.
2. Reuse artifacts for unchanged components; run the narrowest relevant test.
3. Never relax the hard gate or fabricate source rows.
4. Log new failures by exact step, root cause, fix commit and verification run.
