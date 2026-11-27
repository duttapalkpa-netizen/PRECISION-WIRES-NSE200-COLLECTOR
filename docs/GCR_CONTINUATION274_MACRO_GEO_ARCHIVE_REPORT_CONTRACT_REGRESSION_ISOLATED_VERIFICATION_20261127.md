# GCR Continuation 274 — Macro-Geo archive report contract regression isolation
Date: 2026-11-27 (Asia/Kolkata)

## 1. Preflight and task selection
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, C273 handover, Library Mother File and Data Export Recovery Audit Phase 1.
- Skipped completed C273 MEX evidence-reference and 63-row/30-column matrix QA. Skipped the GEO publication trigger because the NBG Q3-2026 BOP release is scheduled for 30-Nov-2026 and is not yet due on 27-Nov.
- Selected the still-open PW-LSN-20261122-002 regression-execution gap. The underlying code fix and AST test already existed; no duplicate code patch was made.

## 2. Verified original failure
- Run #45038111510, job #137256604023, checked out source commit 135801ecea21460f565dd22d19439878bb0b49b3.
- Steps 1–8 succeeded; Step 9 (Collect P0 macro market panel and timestamped news) failed; Steps 10–13 were skipped.
- Exact exception at pipeline/macro_geo_collect_p0.py line 530: KeyError 'weekday_requests'.
- Producer nse_index_history() returned report keys observed_session_requests, rows, failures; consumer used weekday_requests. This is a verified producer/consumer contract mismatch, not an external-source failure.
- Existing artifact #14759889454 SHA-256 618fde324b34fef465a1a9190b07825594c39e2d9ab2dc9f84917c9668cac6cb retains canonical NSE panel SHA-256 d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db. All seven P0 external CSV groups and downstream repair/coverage/event-study/hard-gate reports were absent. Do not infer P0 success from this artifact.

## 3. Existing fix/test reused
- Collector fix commit: afa063959b39846c6722370afa655cb77335d4df; blob 78fe030e5964b8728963a4a0e0604f3cbe184c3f. Consumer now reads observed_session_requests.
- Regression test commit: 491cf1ff7b94ce40129f00c9e8baea499d6087c8; file qa/test_macro_geo_archive_report_contract.py; blob 56d62af1f318414b7db0eb51d25a122e8a4ae03a. AST-based, network-free producer/consumer contract.
- Existing recovery workflow test step commit: 1c9ecb82c29433f91b14e7bc9173652aa6ead67f; workflow .github/workflows/macro_geo_p0_recovery.yml; blob 546234eb9415a916038120d810946089b13c9012.

## 4. New bounded verification workflow
- Added .github/workflows/macro_geo_archive_contract_regression.yml to isolated branch audit/prospective-selector-tracking.
- Commit: 12cce4a15fdf9defa099fc17fa1675e2972505ee.
- Scope: run only the existing pytest contract test, generate archive_report_contract_validation.json with producer/consumer key sets and source/test SHA-256, upload a dedicated evidence artifact.
- Job timeout: 5 minutes. No NSE panel rebuild, market-source request, IMF request, cohort rebuild, Macro-Geo full collection, selector or production action.
- The commit was created on the branch and the workflow trigger is configured for push on this workflow path. At the time of this report, the GitHub combined commit-status endpoint returned an empty status list; therefore the actual workflow execution/result and artifact ID are NOT_VERIFIED. Do not mark the regression PASS from workflow-file creation alone.

## 5. Current acceptance boundary
| Item | Status |
|---|---|
| Original KeyError root cause | VERIFIED |
| Consumer code correction | COMMITTED |
| AST regression test | COMMITTED |
| Dedicated <=5-minute workflow | COMMITTED |
| Regression workflow execution | NOT_VERIFIED / PENDING |
| Macro-Geo P0 collection | BLOCKED |
| P0 repair / source coverage / event study | NOT_RUN in failed recovery attempt |
| Strict hard gate | BLOCKED / NOT_AUTHORIZED |
| candidate_release_allowed | false |
| Overall GCR | NOT_COMPUTABLE / NOT_CERTIFIED |

## 6. Next actions / reopen conditions
1. Verify the dedicated workflow run for commit 12cce4a15fdf9defa099fc17fa1675e2972505ee. Require a successful test step and read-back of archive_report_contract_validation.json; record run ID, job ID, artifact ID and ZIP SHA-256.
2. Only after regression PASS, separately authorize/re-run the audit-only Macro-Geo recovery workflow using Run #398 handoff artifact #14757294944; keep the runtime bounded and inspect Step 9 onward. Do not rerun NSE raw acquisition.
3. If collection succeeds, independently inspect all four P0 source groups (Brent, USD/INR, FPI/DII, corporate events), provenance, source coverage, event maturity, and hard-gate report. A source proxy does not close an official source gate.
4. GEO Q3-2026 release trigger remains 30-Nov-2026; inspect only after actual publication and only for Q2 separate portfolio A/L revisions, BPM5/BPM6 bridge and observation-specific vintage.

## 7. Protected constraints
₹0; official/free sources only; no paid APIs or credential/token bypass; no IMF re-query; no cohort rebuild; no synthetic values, guessed IDs or timestamps; UNKNOWN never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No PR merge or production integration.
