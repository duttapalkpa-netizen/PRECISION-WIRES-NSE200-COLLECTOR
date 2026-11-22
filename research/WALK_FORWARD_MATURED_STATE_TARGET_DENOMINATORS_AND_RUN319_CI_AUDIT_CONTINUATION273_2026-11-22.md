# Walk-Forward Matured State Target Denominators and Run #319 CI Audit — C273

Date: 2026-11-22
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
Branch: `audit/prospective-selector-tracking`

## Continuity and scope
Re-fetched the Master Continuity Ledger and C272/C271 reports before selecting work. PASS work was not repeated. Run #319 was polled to completion; the existing 200-session archive, NSDL gap evidence and strict Macro-Geo gate were not reworked. Changes are confined to the audit-only walk-forward report path; no production selector or scoring logic was changed.

## Run #319 — final evidence
- Run #319 ID: `45017190489`; head `9d3535d62e54a4ad2edc3f7d6d7975f7ace37c6b`.
- Conclusion: FAILURE.
- Regression step executed the exact command `python -m unittest qa.test_macro_geo_engine qa.test_macro_geo_repair_p0 qa.test_macro_geo_nsdl_flows -v`.
- All 19 tests passed, including NSDL gap tests; log reports `Ran 19 tests in 0.045s` and `OK`.
- Workflow failure occurred later at step 6, official NSE 200-session acquisition; subsequent dependent steps were skipped. Therefore the NSDL regression wiring is CI-verified PASS, but the overall Macro-Geo workflow remains FAILURE/BLOCKED.
- Artifact `macro-geo-p0-event-study`, ID `14752487664`, 8,139 bytes, GitHub digest `sha256:7817fd88b0b1b9df7fd6832c601b675323ac07b1b4f1382267d33feea1fbd604`. This is a small partial diagnostic artifact, not a full source/event-study acceptance artifact.

## C273 — per-State, per-target matured denominator repair
### Proven defect
The previous walk-forward State metrics used `rows=len(g)` alongside `_hit_rate`, which drops null outcomes internally. Thus row counts were not valid matured denominators, and the >=50 H+3 Behavioral DNA eligibility rule was not represented per State.

### Implemented audit-only repair
- Added `_matured_state_target_metrics(frame)` to `pipeline/walk_forward_backtest.py`.
- For each State, it now reports distinct matured numerator, denominator, observation count and hit rate for:
  - +5% H+1 (`FUT1`)
  - +10% H+3 (`FUT3`)
  - +15% H+5 (`FUT5`)
  - +20% H+5 (`FUT5`)
- A row is counted only when both its target outcome and matching horizon end-date are present. Each target uses its own denominator.
- H+3/+10 is `CALIBRATED` only at >=50 matured observations; below 50 is explicitly `UNKNOWN`. Other target eligibility is `NOT_APPLICABLE`.
- The metrics are attached to each State's `state_performance` record. Existing selector ranking, ranking weights, state adjustments, pressure-fade adjustment, CORE-672 diagnostics and Engines A–E are unchanged.

### Regression tests added
`qa/test_walk_forward_matured_state_denominators.py` adds four cases:
1. 49 matured H+3 observations (from 55 rows with 6 incomplete) remains UNKNOWN.
2. Exactly 50 matured H+3 observations is eligible.
3. State-specific denominators remain independent (55 vs 45).
4. Missing horizon end dates are excluded independently for H+5 targets.

### CI state
- Code commit: `2861b308248413d9657cdfba19931385a0fc7870`.
- Test commit: `73b865cc830280ef89012b1cc1e25c63ee5b50d1`.
- The first push triggered prospective run #395 ID `45018120031` on the code-only commit; the second push triggered run #396 ID `45018125140` on the code+test commit. At report creation, #395 was IN_PROGRESS and #396 PENDING. No CI PASS is claimed for the new walk-forward code/tests yet. Both runs must be inspected; run #396 is the authoritative combined revision.
- Because two commits were pushed separately, two runs were queued. No further duplicate dispatch or edits should be made while these runs are active.

## Status matrix
- Run #319 NSDL regression suite: PASS (19/19 tests); overall workflow: FAILURE due official NSE acquisition step 6.
- NSDL archive failed dates 2026-07-17 and 2026-08-26: UNKNOWN / unresolved; no inferred holiday or zero flow.
- USD/INR official complete daily history: BLOCKED.
- Event study / historical regime windows: BLOCKED pending genuine matured market windows and complete P0 inputs.
- Walk-forward matured denominator implementation: CODED; CI verification IN_PROGRESS.
- H+3 per-State calibration status: UNKNOWN until the new artifact reports each State's actual matured denominator; no sample is presumed >=50.

## Rejected / guardrails
- Rejected using total State rows as matured sample count.
- Rejected pooling State denominators or using one target's denominator for another horizon.
- Rejected calibrating H+3 with fewer than 50 matured observations.
- Rejected treating null/incomplete forward horizons as non-winners.
- Rejected calling Run #319 an overall PASS because its regression substep passed.
- No synthetic observations, invented timestamps, paid APIs, third-party mirrors, or gate relaxation.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.

## Exact next actions
1. Poll Runs #395 and #396; inspect test-step logs and walk-forward artifact. Require the combined #396 test suite to pass before marking implementation CI PASS.
2. If #396 fails, repair only the demonstrated defect; do not repeat unrelated archive/quarterly PASS audits.
3. Inspect generated `walk_forward_metrics.json` and `behavioral_dna_library.json`; confirm every State has target-specific numerator/denominator and that H+3 eligibility follows >=50.
4. Keep USD/INR, NSDL failed dates, event windows and Macro-Geo strict hard gate BLOCKED/UNKNOWN until official evidence changes.
5. Append subsequent verified results to this ledger and report. Preserve all production invariants.
