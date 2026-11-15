# V11.3 Cutoff-Safe Historical Signal Adapter — Research Specification
Date: 2026-11-15
Status: DRAFT / NOT IMPLEMENTED / NOT APPROVED FOR REPLAY
Scope: research-only construction of historical V11.3-compatible `CUT_OFF,SYMBOL` signals for the isolated cost-aware replay.

## 1. Purpose and hard boundary
The cost-aware replay requires a historical signal ledger with `CUT_OFF,SYMBOL`. The current V11.3 candidate script emits only the latest row per symbol; the V11.4 walk-forward predictions are not an approved substitute. This specification defines a separately isolated adapter that may evaluate the existing V11.3 candidate rules repeatedly at historical cutoffs without changing production logic.

This is a specification only. It does not implement an adapter, create signals, run a replay, or authorize changes to production. Protected invariants remain unchanged: Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), and engines A–E.

## 2. Verified source facts (do not reinterpret)
- `pipeline/v11_3_abcd_e.py` currently sorts the processed dataset by symbol/date, calculates features, then uses `g.iloc[-1]` once per symbol. It writes latest candidates and top-30 outputs, not a historical cutoff ledger.
- The V11.3 candidate script optionally loads `outputs/backtest/behavioral_dna_library.json`; its `hit10_h3` rates contribute to the calibration component of the candidate score.
- The inspected library is produced by the V11.4 walk-forward workflow from future outcome fields (including FUT1/FUT3/FUT5 highs). A full-sample library must never be reused at earlier cutoffs.
- The V11.4 workflow's final state assignment (`_state_transition_v4`) is not the same function as V11.3's `classify_state`; therefore V11.4 DNA state rates cannot be joined to V11.3 states by label or assumed equivalence.
- The current V11.4 DNA library is aggregated from the Top-30 `pred` rows per cutoff, not the full eligible universe. Its `samples` field is therefore not a general per-state population count and cannot establish the approved 50-observation threshold for V11.3 state calibration.
- The inspected `future_outcomes` implementation uses `shift(-1).rolling(h, min_periods=1).max()`. Its rolling-window alignment and partial-window behavior must be tested against a deterministic hand-calculated fixture before treating `FUT3_HIGH_PCT` as the exact next-three-session high outcome. Do not silently assume it represents T+1 through T+3.
- The isolated cost-aware replay consumes OHLC rows with `SYMBOL,DATE,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,TTL_TRD_QNTY` and signals with `CUT_OFF,SYMBOL`.
- A 200-session raw archive and its raw-file manifest have already passed scoped acceptance. Do not reacquire or re-merge this archive for this task.

## 3. Proposed adapter behavior
For each eligible historical cutoff date C, and each symbol with valid observations through C:
1. Build the symbol's feature frame using only rows with `DATE <= C`. No row after C may enter feature calculation, normalization, ranking, calibration, or eligibility.
2. Reproduce the existing V11.3 feature and candidate calculations from the inspected source, preserving formulas and thresholds verbatim. Do not refactor or import the V11.4 top-30 ranking as a substitute.
3. Compute any behavioral-DNA calibration using only outcome observations whose complete H+3 maturity window ended on or before C. The H+3 outcome definition, state assignment, denominator, treatment of missing/non-traded sessions, and target-price convention must be copied exactly from the authoritative source implementation after code review; no approximate reconstruction is permitted.
4. Never use outcomes from C or later to calibrate signals at C. Enforce this with an explicit maximum source-outcome date assertion and a leakage regression test.
5. Emit a cutoff/symbol record only when the exact V11.3 rule inputs required for the signal are available and valid. Preserve explicit status and provenance fields in the adapter's audit output; the replay-facing file must contain only the required `CUT_OFF,SYMBOL` columns.
6. Sort deterministically by cutoff then symbol; reject duplicate `CUT_OFF,SYMBOL` keys. Do not fabricate rows for missing symbols, sessions, features, or outcomes.

## 4. Calibration gate — unresolved policy, no silent fallback
The production candidate formula uses a numeric calibration term. A cutoff-safe historical equivalent therefore requires a declared minimum number of matured observations per state and a declared behavior below that minimum.

These policy values are NOT established by the inspected source and must not be invented by implementation:
- Minimum matured H+3 observations per state: **50 — EXPLICITLY APPROVED BY USER ON 2026-11-15**.
- Counting unit: one unique, fully matured `CUT_OFF,SYMBOL` observation assigned to that exact state at that cutoff. Duplicate keys, repeated rows, immature outcomes, and synthetic observations do not count.
- Scope: counts are maintained independently for each state; do not pool observations across states to meet the threshold.
- Below-threshold behavior: that state remains **UNKNOWN / NOT CALIBRATED / NOT ELIGIBLE**. Do not substitute 0, 50, a pooled rate, a full-sample rate, or another synthetic value.
- Scope of exclusion: only the affected state’s signal/calibration is UNKNOWN; other states may proceed if they independently satisfy all gates. Any row in an under-threshold state must not receive a calibrated numeric score.
- Maturity: an H+3 observation counts only after all three subsequent valid exchange sessions and the complete outcome window are available under the approved outcome definition. Missing sessions or incomplete windows do not count.

The threshold policy is approved, but accepted scored signals and replay remain blocked until the authoritative H+3 outcome calculation, state assignment, and cutoff maturity logic are independently verified. Source inspection and date-isolation tests may proceed.

## 5. Required inputs and provenance
- Processed OHLC dataset derived from the accepted 200-session archive; record exact path, SHA-256, row count, date range, schema, and upstream archive artifact ID.
- Exact source-code commit/blob SHAs for every imported feature function and candidate formula.
- Any source inputs needed for state/outcome calibration, with source path, SHA-256, row count, date range, and the original outcome-generation definition.
- Adapter commit SHA, Python/pandas/numpy versions, run ID, cutoff calendar, and output SHA-256.
- Preserve raw source files unchanged. No synthetic data, fabricated timestamps, paid APIs, or external contacts.

## 6. Fail-closed validation gates
A0. State parity and population integrity: implement the exact V11.3 `classify_state` on cutoff-only features; prove state labels match V11.3 at each cutoff. Do not import V11.4 `_state_transition_v4` labels or its Top-30-only `samples` counts as V11.3 calibration evidence.
A00. H+3 outcome semantics: verify the existing `future_outcomes` window against a deterministic fixture for T+1, T+2, and T+3, including incomplete tails. Record any discrepancy as a source defect; do not silently change the production or reference workflow.
A. Cutoff isolation: mutate or append post-cutoff rows and prove the signal output at C is byte-identical.
B. Maturity isolation: outcomes whose H+3 window ends after C must not affect calibration at C.
C. Future-DNA exclusion: reject full-sample `behavioral_dna_library.json` inputs and any V11.4 future-outcome feature leakage.
D. Schema and uniqueness: strict dates; unique `SYMBOL,DATE` OHLC keys; unique `CUT_OFF,SYMBOL` output keys; valid symbols; no silent date repair.
E. Session completeness: use the verified global trading-session calendar; missing symbol sessions remain explicit UNKNOWN/exclusion, never forward-filled.
F. Formula parity: golden tests compare adapter feature/candidate values against the existing V11.3 implementation at the same cutoff, with only the calibration source replaced by cutoff-matured data.
G. Determinism: identical input bytes and code version produce identical output bytes and hashes.
H. Replay precondition: no replay until all policy decisions are approved, all gates pass, and an independent audit confirms the signal ledger lineage.

## 7. Required artifacts
- This specification and a decision record for unresolved calibration policy.
- Adapter source and isolated unit tests (only after approval).
- Cutoff-level leakage audit, per-cutoff coverage report, signal provenance manifest, and SHA-256 manifest.
- A separate PASS/BLOCKED report for signal-input acceptance.
- Only after signal-input acceptance: cost-aware trade ledger, metrics, exclusions, and independent reconciliation.

## 8. Current decision and progress
- Existing V11.3 historical signal ledger: NOT_FOUND.
- V11.4 predictions as substitute: REJECTED.
- Adapter specification: UPDATED with approved minimum 50 matured observations per state.
- Adapter implementation/tests: NOT_STARTED.
- Historical cost-aware replay: BLOCKED / NOT_STARTED; H+3 outcome/maturity semantics, state-taxonomy parity, and Top-30 sample bias require independent audit.
- Independent replay reconciliation: NOT_STARTED.

## 9. Safety
Research-only. Do not modify production selector, ranking, pressure-fade, CORE-672, engines A–E, or production workflows. Keep PR #37 Draft/Open/Unmerged. No merge authorization.
