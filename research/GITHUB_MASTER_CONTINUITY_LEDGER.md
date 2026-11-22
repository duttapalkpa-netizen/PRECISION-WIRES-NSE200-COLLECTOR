# PRECISION-WIRES — GitHub Master Continuity Ledger

Last updated: 2026-11-22
Canonical audit branch: `audit/prospective-selector-tracking`
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Purpose and operating contract
This file is the continuity index for subsequent audit work. Before every task:
1. Read this ledger and the linked latest report(s).
2. Verify current GitHub Actions state and artifact evidence.
3. Skip work already marked PASS; select only an evidenced incomplete item.
4. Record exact commit/run/artifact IDs and distinguish PASS, IN_PROGRESS, BLOCKED, UNKNOWN.
5. Never promote UNKNOWN/BLOCKED to PASS.

Constraints: audit branch only; ₹0 spend; free official sources only; no synthetic data, fabricated timestamps, third-party mirrors, or access-control bypass. Preserve Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), and Engines A–E. This ledger is a verified continuity index, not a claim that every historical conversation has been exhaustively imported. Earlier numbered research reports remain the detailed source of record.

## Current priority
**IN_PROGRESS — Run #383**, workflow run ID `44992957027`, head `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`.
C249: corrected-label walk-forward step SUCCESS; P0 market/news collection IN_PROGRESS at last check.
C250: source-policy audit found Yahoo secondary fallback and GDELT/RSS media discovery in `pipeline/macro_geo_collect_p0.py`; the required-series predicate accepts `AVAILABLE_SECONDARY`. `pipeline/macro_geo_repair_p0.py` also has a community GitHub USD/INR mirror fallback. These cannot satisfy official-only acceptance. No code changed while Run #383 is executing. C250 report: `research/MACRO_GEO_P0_OFFICIAL_SOURCE_POLICY_AUDIT_CONTINUATION250_2026-11-22.md`, commit `e7b4e4fd4098f1df9720eb239a71335367203c9b`.
Next: after Run #383 ends, make secondary sources ineligible for official P0 gate; remove community mirror fallback; preserve GDELT/RSS only as clearly labelled media-publication discovery.
URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44992957027

## C251 — Run #383 cancellation and Macro-Geo source-policy repair
Run #383 ID `44992957027` concluded `cancelled`, not failed. Job log shows explicit operation cancellation at `pipeline/macro_geo_collect_p0.py` on 2026-11-22 06:26:25 UTC. No failed step was recorded. Partial artifact ID `14743330788`, SHA-256 `6c3fd376e7a1473e3ddc1f5ea58c18abcf92a46d8016e9a4bbd2105dd6953acb`. Artifact confirms 200 NSE sessions, 2,999 symbols, 100% delivery coverage and QA PASS; no completed P0 manifest/repair report, so Macro-Geo remains UNKNOWN/BLOCKED.
C251 commits: tests `a88d001a03a88dae21015fbd11f7abe8ccb00b84`; collector official-row gate `c38266fca0566d1244498625db43ad2b88456512`; repair mirror removal `0fa47564fbe532f66ed7d69ddff80faaefbe9517`; FRED provenance/status correction `e81aeb913f426917f27f602da926c1f56201478a`. Yahoo-only observations cannot satisfy official P0 readiness; community USD/INR mirror removed; USD/INR remains BLOCKED if FRED fails and no direct official RBI/FBIL source is verified; EIA RBRTE retained as official Brent fallback; FRED explicitly identified as Federal Reserve Bank of St. Louis. Five regression tests added at `qa/test_macro_geo_official_source_policy.py`.
Report: `research/MACRO_GEO_SOURCE_POLICY_REPAIR_CONTINUATION251_2026-11-22.md`. CI: Run #386 ID `44994006387` triggered by C251 code, initially PENDING; inspect latest run after subsequent commit before any PASS claim. C251 code COMMITTED, CI VERIFICATION PENDING.
Next: inspect latest run/artifact; targeted and full QA; verify official source gate from artifacts; retain UNKNOWN/BLOCKED where official coverage absent. Invariants unchanged.
 
## Recent verified continuity

### C235 — Security Master fail-closed provenance
Report: `research/NSE_SECURITY_MASTER_FAIL_CLOSED_PROVENANCE_GATE_CONTINUATION235_2026-11-22.md`
Commit: `96050af2685b8520a3933b55da47aeaf8deb7b89`
Legacy NSE equity master is explicitly classified as `LEGACY_EQUITY_L_CSV`; daily CM-MII equivalence is `NOT_ESTABLISHED`. Validator enforces source provenance, freshness, hashes, columns, unique symbols and row counts. Six offline tests added. Do not claim daily CM-MII equivalence.

### C236 — stale-file protection
Report: `research/NSE_SECURITY_MASTER_FRESH_ACQUISITION_STALE_ARTIFACT_GUARD_CONTINUATION236_2026-11-22.md`
Code/test commits: `6f8a655826f829bcf8acd8df2ef3bd498a806721`, `dcab18abbc5e8a8d1a70487cb372fe5341d8c9b7`; report commit `e55665b3f4db8f59b11802e5bd124cdff4559951`.
Old CSV/manifest pair removed before fresh acquisition. Regression test covers failed network acquisition after stale-file seeding. No CI verification was recorded at C236.

### C237 — manifest integrity
Report: `research/NSE_SECURITY_MASTER_MANIFEST_INTEGRITY_GATE_CONTINUATION237_2026-11-22.md`
Validator/test/fixture commits: `9ab2ef454c598d430d79051366641012086d26f1`, `f0181b6478d8508f77d97e4fb8daacb3e8b48d53`, `220e5cc716d2036d733954b7d5e9f0bf35a3a20b`; report commit `8351e4d66554ad60d97cd297c7fac072cf800d1c`.
Schema version, HTTP 200, SHA-256 shape, positive source byte count and regression cases enforced.

### C238–C240 — CI and workflow control
C238 report `research/NSE_SECURITY_MASTER_REGRESSION_SUITE_CI_VERIFICATION_CONTINUATION238_2026-11-22.md`, commit `cb66a6851c5296f3ac6d112ada32680159ec2a5f`. Run #372 (ID `44991296424`) QA suite step passed; later C240 inspection confirmed XBRL extraction passed, but corrected-label walk-forward was still running at that observation.
C239 report `research/AUDIT_WORKFLOW_TRIGGER_COST_CONTROL_CONTINUATION239_2026-11-22.md`, commit `915108afa4f4091c81cee105368aa2658a09f470`. Removed `research/**` from push path filters to avoid report-only audit runs.
C240 report `research/SECURITY_MASTER_CI_ACCEPTANCE_UPDATE_CONTINUATION240_2026-11-22.md`, commit `a2b241faf19b8d9c289ee620d225240c436ec368`. Step-level PASS only; do not infer full-workflow PASS from it.

### C241–C242 — quarterly/XBRL inspection
C241 found test coverage for SEBI taxonomy facts, dimensions/basis, units, period/date parsing, insurance facts, inline iXBRL scale/sign, malformed HTML, official attachment discovery, bounded discovery and PDF evidence; no proven source defect or commit.
C242 evidence was summarized in C243/C245 reports. Do not use isolated counts without the corresponding artifact scope.

### C243–C244 — preserve 403 diagnostics and repair regression
C243 report `research/NSE_ATTACHMENT_403_DIAGNOSTIC_PRESERVATION_CONTINUATION243_2026-11-22.md`, report commit `c23000b8bf890e901746cafb5d0fed8d8dec1748`; code/test commits `8da955850e07763d9f40148124716c7db26b2f48`, `66e1a030d2633ca86c3a16df359c4873f0b61a87`. CI exposed an indentation defect.
C244 fixed indentation (commit `ac3f93da1f6546b820620d5567ff8196f277339d`) and corrected HTTPError test mocks (commit `fe5f9dff9d1ab0affcda8a93cc58db4da6a5044c`). Run #133 (ID `44992195724`) completed SUCCESS and uploaded artifact `14741638800`. Report `research/QUARTERLY_XBRL_403_REGRESSION_REPAIR_CONTINUATION244_2026-11-22.md`, commit `f368bc995cee320b1c6ad98d51b89f15a0e78b6a`. Run #381 was cancelled; not a PASS.

### C245 — quarterly coverage baseline
Report: `research/QUARTERLY_METRIC_COVERAGE_ROOT_CAUSE_TRIAGE_CONTINUATION245_2026-11-22.md`
Commit: `2e71f70b3437615c8f7905a30301530ed9ec4ca8`
Run #133 artifact baseline: 500 disclosures, 926 attachment attempts, 500 ledger rows, 67 verified metric rows / 44 symbols, 426 blocked, 7 superseded. 99 of 100 surfaced errors were official attachment retrieval failures, one facts/basis incomplete. Coverage remained BLOCKED. Do not attribute all blocked rows to those 99 errors without row-level join.

### C246 — official NSE host fallback
Report: `research/NSE_INTEGRATED_FILING_ARCHIVE_HOST_FALLBACK_CONTINUATION246_2026-11-22.md`
Code commit `b8a9f541ec98fbf427caec27905cc4e4f4fba5da`; test commit `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`; report update commit `ca58ccdf1be661f0fa6a8ffea12b3fce57824819`.
Adds official `.in` host allowlisting and bounded same-path fallback between `nsearchives.nseindia.in` and `archives.nseindia.com`, with regression coverage. No unofficial mirror or bypass.

### C247 — measured archive fallback outcome
Report: `research/QUARTERLY_NSE_ARCHIVE_FALLBACK_EVIDENCE_OUTCOME_CONTINUATION247_2026-11-22.md`
Commit: `37684fbf445d4be50deb42e56a6edaa9e7cb9585`
Run #135 ID `44992957011` completed SUCCESS on head `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`. Artifact `quarterly-endpoint-schema-audit`, ID `14742483865`, 9,411,646 bytes, SHA-256 `109f64d618567e99f65e559c7e3aad5d9e794bf94834dfa29773ee9c5e2cbad5`.
Artifact measured 476 verified source-linked metric rows / 275 symbols, 1 blocked, 23 superseded; 500/500 result source-validation records valid; 500 disclosures, 501 attachment attempts. Two residual errors: one official NSE XBRL URL HTTP 404 (AGL), one iXBRL attachment with zero parseable facts/incomplete basis (AGL). 37/500 disclosures lack broadcast_Date. Coverage still reports BLOCKED_INCOMPLETE_OR_UNVERIFIED_COVERAGE. Event study still BLOCKED_MISSING_EVENT_OR_PRICE_PANEL because processed 200-session price panel was absent from this targeted artifact. Do not claim host fallback alone caused every recovered row without per-attempt host attribution.

## Known unresolved issues / exclusions
- Do not re-run PASS quarterly extraction or regression suite without new evidence of regression.
- Run #383 walk-forward is the current active dependency; wait for and inspect its result before starting overlapping downstream work.
- Four Macro-Geo P0 groups and historical event study remain unverified until Run #383 steps complete with evidence.
- Do not treat absent broadcast timestamps as creation timestamps.
- Do not treat 1 blocked + 23 superseded as all metrics verified; preserve coverage gate.
- Event study requires the processed price panel; no result may be inferred from targeted quarterly artifact.
- Legacy NSE equity master is not proven equivalent to daily CM-MII security master.

## Exact next actions
1. Re-fetch Run #383 jobs and artifacts. If complete, inspect every step and artifact before changing status.
2. If corrected-label walk-forward fails, inspect its failed step logs and repair only the proven defect on the audit branch.
3. If it passes, proceed to the next pending P0 collection step and validate source timestamps/provenance; do not skip gates.
4. Keep Macro-Geo groups, selector diagnostics, historical targets and prospective picks BLOCKED/UNKNOWN until their explicit acceptance evidence passes.
5. Append new continuation reports and update this ledger after each material verified outcome.

## Permanent guardrails
- PASS work is skipped unless regression evidence appears.
- Every claim is scoped to its exact run, artifact and data coverage.
- Matured observations only; minimum 50 fully matured observations per State for H+3 Behavioral DNA calibration. Below 50 remains UNKNOWN/uncalibrated.
- Historical target-hit rates are not profitable trade returns.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E remain unchanged.
