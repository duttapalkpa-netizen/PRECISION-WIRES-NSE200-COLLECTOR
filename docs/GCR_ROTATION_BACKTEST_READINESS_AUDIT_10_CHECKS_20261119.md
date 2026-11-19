# Global Capital Rotation — 10-Check Backtest Readiness Audit
Date: 2026-11-19 (Asia/Kolkata)
Scope: Existing GCR evidence and V11.3 backtest implementation; read-only review. No production changes.

## Executive decision
**Actual GCR rolling performance backtests executed in this audit: 0/10.**
**Readiness/contract checks reviewed: 10/10.**
This is not a performance result and does not prove predictive value. A genuine GCR-to-India rolling backtest remains NOT_RUN / BLOCKED.

## Progress log
### Completed / reused (not repeated)
- Existing GCR IMF BOP 154-member raw panel and country-level archive are acknowledged; existing country coverage, scale, vintage and structural blockers remain in force.
- Existing RBI Table 197 benchmark: 12/12 PASS across six quarters.
- Existing RBI Table 42 current-vintage supplement: 10 PASS, 2 REVIEW; 2026-Q1 liability/net discrepancy remains REVIEW.
- Existing FRED/H.10 dollar-source audits and 72-test regression are reused, not rerun.
- Existing cost-aware replay script and research contract were inspected, not executed.

### 10 acceptance/readiness checks
| # | Check | Result | Evidence / reason |
|---|---|---|---|
| 1 | Time leakage: features at T use only <=T | PARTIAL | V11.4 walk-forward source documents strict cutoff and expanding prior-window training; no independent run-level leakage test artifact inspected here. |
| 2 | H+1/H+3/H+5 maturity | PARTIAL | V11.4 code excludes final five sessions for matured outcomes; actual matured sample counts not available in this audit. |
| 3 | Exact +5% H+1 / +10% H+3 / +20% H+5 labels | PARTIAL | Targets exist in V11.4 and cost-aware replay contract; no fresh output ledger verified. |
| 4 | 0.22% round-trip cost convention | PARTIAL | V11.3 replay code applies 0.22 percentage points once; slippage is explicitly unmodelled and user-approved execution assumptions remain unresolved in the research contract. |
| 5 | Stop/target same-bar ambiguity and stop-loss | PARTIAL | Replay code encodes -3% stop and stop-first; contract says execution conventions require user approval. Do not treat this as accepted strategy logic. |
| 6 | Gap-through-target / executable fill | PARTIAL | Code has conservative gap handling, but no circuit-lock/market-impact validation or executed ledger was inspected. |
| 7 | Missing/invalid OHLC, zero volume, missing symbol-session | PARTIAL | Code fails closed / emits non-executable statuses; no run-level exclusion reconciliation inspected. |
| 8 | Duplicate SYMBOL/DATE and invalid date guards | PARTIAL | Guards exist in code; no independent test-run output verified. |
| 9 | Gross/net arithmetic, denominators, precision/recall/lift | BLOCKED | Existing V11.3 cost-aware contract requires complete ledger/metrics; no verified GCR-linked cost-aware output artifact or reconciled denominators was inspected. |
| 10 | Reproducibility, hashes, protected production invariants | PARTIAL | Replay code hashes input/output files; this audit did not execute it or verify new output hashes. No production files were changed. |

## Why actual GCR backtesting is blocked
1. The GCR Observation work remains open; cross-country IMF panel coverage and scale/vintage semantics are not yet sufficient to authorize a common aggregate signal.
2. The repository evidence explicitly states GCR relative-attraction formula, sector transmission and rolling backtest are NOT_DONE.
3. GCR global factors are not yet synchronized and joined to India sector/stock total-return outcomes with defensible timestamp/vintage alignment.
4. The cost-aware V11.3 replay is an OHLC trade replay, not a validated GCR factor attribution / incremental-value test.
5. The V11.3 cost-aware research contract is a draft and states G0 user-approved entry/exit/stop/circuit conventions BLOCKED; G1–G4 NOT_STARTED.

## Rejected / not admitted
- No IMF 154-member aggregate; coverage gaps, scale semantics and revisions remain unresolved.
- No national-source gross-leg substitutions or annual estimates used to fill missing quarterly flows.
- No India Q1-2026 RBI Table 42 liability discrepancy adjustment.
- No synthetic rows, forward-fill, guessed crosswalks, fabricated timestamps or unverified trade fills.
- No production selector, ranking score, pressure-fade, CORE-672, Engines A–E or IPO-PLX V2 change.

## Decision
- Actual GCR performance backtest: **BLOCKED / NOT_RUN (0 of 10)**.
- Readiness checks: **10 reviewed; 0 full execution PASS; 9 PARTIAL; 1 BLOCKED**.
- GCR Observation: **OPEN**. Do not advance to Planning/Organizing or production admission.

## Next highest-value bounded action
Build a leakage-safe, synchronized timestamp/vintage join specification and source coverage gate for the already archived GCR factor panel versus official India sector TRI/market outcomes; first prove one small historical window end-to-end with raw source bytes, exact timestamps, matured outcomes and hashes. Do not launch the full rolling backtest until this pilot passes and G0 execution assumptions are explicitly approved.

## Source code and contract reviewed
- `pipeline/v11_3_cost_aware_backtest.py` — blob SHA: `32b556717dab70d0b37de69a6e3d98105edd1702`
- `docs/V11_3_COST_AWARE_ROLLING_BACKTEST_RESEARCH_CONTRACT_20261115.md` — blob SHA: `d06734cce715eacc609d663bead7e1853af5a79f`
- `pipeline/walk_forward_backtest.py` — blob SHA: `d085f7a2d35a88b4c4eaba65144a429a06961b09`

No workflow was dispatched; no new run ID, artifact ID or output SHA-256 is claimed. No production code or protected invariant was modified.
