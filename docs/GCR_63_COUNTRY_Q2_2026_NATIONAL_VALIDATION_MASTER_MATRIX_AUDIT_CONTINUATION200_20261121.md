# GCR 63-country Q2-2026 National Validation Master Matrix — Continuation 200
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The existing country matrix was discovered and upgraded in place rather than creating a duplicate. It is aligned one-to-one with the immutable 63-country cohort; no cohort rebuild and no IMF re-query. The matrix now exposes the requested explicit state vocabulary for source, data capture, asset, liability, vintage and overall status.

## Mandatory preflight
- Master Continuity Ledger pre-task blob: e706975f96ea785e9e8370e8945a51c0d5b46c4b
- GCR Master Priority Queue pre-task blob: 7b69499a81f4c80b5cacb0bbbedf886c727ec241
- Historical Task Registry pre-task blob: 0d3dc8c03a5e4cf80a749dc8cc4fe02f28731f66
- Immutable cohort CSV blob: 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8
- Existing master matrix blob: 45e466c72c034d460dfccf57474b07bfb6d12ea9
- Exact cohort membership: 63 rows; matrix: 63 unique country codes; mismatches: 0.
- Every cohort row has both A_NFA_T and L_NIL_T marked PRESENT in the cohort file. This confirms IMF panel membership, not national-source validation.

## Matrix state counts
- SOURCE_FOUND: 20
- DATA_CAPTURED: 23
- BLOCKED: 19
- NOT_STARTED: 1
- Total: 63 countries.
- FULL_PASS: 0; VINTAGE_PASS is independently required.
- No aggregate admission is changed; every row retains NOT_AUTHORIZED pending the full acceptance gates.

## Status semantics
- NOT_STARTED: no official source identified in the current matrix.
- SOURCE_FOUND: official source/route identified, but no accepted Q2 national dual-leg capture.
- DATA_CAPTURED: data rows/values are captured or partially captured; this does not mean both legs passed.
- ASSET_PASS / LIABILITY_PASS: respective national leg independently passed its source-specific comparison/acceptance gate.
- VINTAGE_PASS: source vintage/revision alignment independently established.
- FULL_PASS: both legs and vintage gates pass together, with required source scope/units/sign/period checks.
- BLOCKED: current route/execution gate is blocked; this does not mean the national data do not exist.
- REVIEW is represented as DATA_CAPTURED rather than PASS; original detailed gate fields are retained unchanged.
- Legacy fields (current_stage, source_gate, data_capture_gate, asset_gate, liability_gate, vintage_gate, full_pass, aggregate_admission and evidence notes) are retained alongside normalized status fields.

## Interpretation / limitations
- This is a reconciled inventory baseline based on the previously committed 63-row matrix plus exact cohort membership. It does not independently re-open every one of the 63 national reports in this bounded task.
- Where the previous matrix did not contain a dedicated report reference, evidence_ref explicitly says NO_DEDICATED_REPORT_REF_IN_BASELINE. Those rows require report-level preflight before status promotion.
- Existing BLOCKED statuses are route/execution blockers and are not counted as completed countries.
- DATA_CAPTURED can still have sign, scope, FX, rounding or revision-vintage issues.
- Do not convert REVIEW/PENDING/UNKNOWN into PASS. Do not infer missing values as zero, use IIP stocks as flows, net-to-leg backsolve, or promote net-only sources to dual-leg validation.

## Protected constraints
₹0; official/free sources only; no synthetic values or fabricated timestamps; no IMF re-query/cohort rebuild; no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 or production integration. UNKNOWN is never PASS. Aggregate remains NOT_AUTHORIZED.