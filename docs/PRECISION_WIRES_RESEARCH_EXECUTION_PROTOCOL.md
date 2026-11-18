# PRECISION-WIRES Research Execution Protocol

**Effective:** 2026-11-18  
**Scope:** Global Capital Rotation Overlay / IMF–BCB BOP source research and subsequent PRECISION-WIRES evidence workflows.

## Objective
Reduce elapsed time, repeated acquisition, fragmented commits, and research error risk without weakening evidence standards. This protocol changes execution discipline only; it does not change production selectors, scoring, diagnostics, or trading rules.

## 1. Single-batch change discipline
- Group all changes for one coherent research question into one reviewed patch: parser, tests, workflow wiring, report, and continuity-ledger update.
- Create one atomic Git commit for that batch. Do not create one commit per file or per tiny edit.
- Do not start a new workflow after each intermediate commit.
- Expensive IMF/BCB acquisition workflow is deliberately gated. A normal push is not sufficient. Run only on manual `workflow_dispatch` or a consolidated commit whose message explicitly contains `[run-bop-audit]`.
- Concurrency is serialized per branch; a new run must not race an earlier run.

## 2. Reuse evidence; refresh only on a justified trigger
- Before downloading anything, inspect the latest accepted artifact manifest and SHA-256 values.
- Reuse an immutable captured source when its exact source bytes/hash are already available and the research question does not require a newer vintage.
- Refresh only when the source's expected update cadence, a documented source change, or a specific missing evidence requirement justifies it.
- Never overwrite an earlier source vintage. Keep each capture, request URL, HTTP metadata, capture timestamp, source-reported publication/vintage metadata, and SHA-256 distinct.
- Never rerun a completed audit whose code, inputs, and acceptance criteria are unchanged.

## 3. Pre-run validation and one-run acceptance
- Before the expensive run, inspect changed files, verify source-code labels/IDs against the actual official source, run syntax and focused unit tests, and verify the workflow paths and command-line arguments.
- Execute one consolidated run with a hard job timeout of 8 minutes. Split only genuinely independent long work into separately bounded jobs; do not split merely to create more runs.
- On failure, inspect the failed step and its logs first. Fix the root cause and rerun only the failed job when safe; do not repeat successful source acquisitions unnecessarily.
- A successful GitHub Actions job means the audit executed. It does not mean the underlying data passed reconciliation. Runtime status and research acceptance status must always be reported separately.

## 4. Evidence and decision states
- **PASS:** exact acceptance criteria satisfied by inspectable raw evidence and reproducible output.
- **FAIL:** a measured condition violates an explicit criterion; preserve mismatch samples and counts.
- **PARTIAL:** only a subset of required scope passed.
- **UNKNOWN:** evidence or semantics insufficient. UNKNOWN is never promoted to PASS.
- **NOT_RUN:** no execution evidence exists for the current code/input version.
- Every reported result must identify the run ID, commit SHA, artifact ID, artifact SHA-256, relevant report SHA-256, source period, unit, and comparison tolerance where applicable.
- No synthetic observations, inferred timestamps, unverified mappings, silent rescaling, source substitution, or data splicing.
- A parser test with fabricated fixtures is a regression check only; it does not establish the real source result. Real-source claims require the exact source artifact.

## 5. Research safety invariants
- Keep the Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), and engines A–E unchanged.
- Keep Brazil portfolio flow panel, Global EM aggregate, and trading-signal admission NOT_AUTHORIZED until the source-lineage, quality, sign, unit, and registration/constraint gates are explicitly resolved.
- No paid API, paid subscription, or external contact; research spend remains ₹0.

## 6. User-facing progress discipline
- Report one concise progress log per meaningful batch, not after every small command or file write.
- Separate completed evidence, unresolved blockers, rejected/unsupported claims, and the single next action.
- Never claim a task is complete while its required runtime artifact is missing or its source-level acceptance gate is FAIL/UNKNOWN.

## 7. Initial enforcement change (2026-11-18)
The workflow `.github/workflows/imf_bop_dsd_acquisition.yml` now ignores workflow-file-only pushes and requires either manual dispatch or the explicit `[run-bop-audit]` commit marker. It also serializes runs by branch. This prevents each intermediate code/documentation commit from triggering a full IMF/BCB download.
