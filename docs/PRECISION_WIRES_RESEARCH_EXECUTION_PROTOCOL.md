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


## 8. Trigger deduplication (2026-11-18)
- After any branch ref update or contents-API write that can trigger a workflow, immediately inspect the latest Actions runs for the intended workflow and commit SHA.
- If a matching run exists (queued, pending, in progress, or completed), do not make another workflow-path write merely to trigger it.
- Do not combine a Git Data API ref update with a second contents-API update to the same workflow path as a trigger; both can dispatch separate runs for the same research batch.
- One research batch must have one deliberate workflow trigger. Treat any duplicate run on the same code/input as duplicate verification only, not independent evidence.
- If a ref update does not trigger a run, verify that no matching run exists before issuing one contents-API trigger commit.


## 9. Reconcile source headers before accepting registration rows (2026-11-18)
- A successful registration lookup and an exact ProvisionAgreement link are not sufficient to accept a country payload. Parse the original SDMX Header `Structure/@namespace` and root `xsi:schemaLocation` and compare both against the registered Dataflow ID.
- Compare Dataflow identities, names, referenced DSDs and attached constraints separately. A shared DSD is not proof that two Dataflow IDs are aliases or that their constraints are interchangeable.
- Measure observed series membership against each attached allowed constraint; report allowed/total, excluded codes and exact hashes. Do not select the constraint with the higher coverage as a substitute for an authoritative contract.
- If registration and payload disagree, classify the contract as UNKNOWN/BLOCKED, preserve the raw payload, and keep all downstream admissions NOT_AUTHORIZED. Resolve only through authoritative BCB/IMF metadata or a formal registry/source correction; no guessed remapping.
- Prefer reusing prior workflow artifacts for re-analysis. Do not reacquire BOP observations to investigate a metadata-only mismatch.


## 10. Dataflow identity reconciliation acceptance (2026-11-18)
- For country SDMX payloads, compare all three identities: registration Dataflow, SDMX Header `Structure/@namespace` and root `xsi:schemaLocation` Dataflow. Preserve exact source bytes and hashes.
- A shared DSD is not a Dataflow alias. Compare maintainable IDs, labels, version, structure reference, and attached constraints separately.
- Calculate indicator membership for the exact payload against each candidate Allowed constraint. Report counts and excluded codes; do not pick the highest-coverage constraint as an automatic correction.
- If registration and payload Dataflow disagree, classify the selected Dataflow as UNKNOWN and block downstream use until an authoritative source/registry correction. Preserve the original payload; do not rewrite headers, change registration rows, or silently remap.
- Prefer re-analysis of a verified prior artifact. Record both source archive digest and per-file SHA-256. No observation reacquisition for a metadata-only contract issue.


## 11. Public registration documentation is not a country-specific contract correction (2026-11-18)
- The IMF Web Services Guide describes registration as a Dataflow + Data Provider + URL association; the IMF User Guide says SDMX Central queries the URL to validate the data file. These documents do not, by themselves, establish the exact validation algorithm or resolve an individual provider's header-vs-registration mismatch.
- The IMF SDMX Central overview distinguishes Dataflow-level and Provision Agreement-level constraints. Keep their attachment points separate; do not infer that shared DSDs or similar labels make Dataflow IDs interchangeable.
- A public registration row and generic validation description are evidence of the registry association, not evidence that a contradictory source Header is acceptable. For a mismatch, preserve UNKNOWN/BLOCKED until a country-specific authoritative registration/source correction is visible.
- Documentation-only reviews must be recorded as such; do not invent a workflow run, artifact, source capture timestamp or SHA-256. Do not trigger a full acquisition workflow for a metadata-only documentation update.

## 12. Registration history evidence hierarchy (2026-11-18)
- For a country-specific registration-history question, prefer the official Data Registrations activity page, filtered by Provision Agreement, Dataflow, or Data Provider. Capture detail fields (Data URL, Provision URN, Dataflow URN, Data Provider URN, User) and every event row with its action/time if actually returned.
- The public Registrations table's Last Updated field is an event-time indicator for the current registration; it is not a full event history. The User Guide documents that Re-Register updates Last Updated for the same URL.
- The IMF SDMX Central RSS feed is documented to emit transactions including data registrations/deletions and to link each event to a RegistryInterface SubmitRegistrationRequest/SubmitStructureRequest. Preserve the raw event document and SHA-256 if retrievable. Do not infer event history from the current registration table alone.
- An empty/unpopulated client-side history extraction is NOT evidence of zero events. Classify Brazil-specific history as NOT_RETRIEVED/UNKNOWN until a filtered event or a complete bounded feed capture is inspected.
- The generic SDMX Transactions page may show structure submissions; do not treat it as the dedicated Data Registrations history.
