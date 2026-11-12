# PRECISION-WIRES V11.3 — MASTER GAP MATRIX

**Snapshot date:** 2026-11-02  
**Repository:** `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`  
**Branch:** `fix/factor-registry-same-snapshot-reconcile`  
**Snapshot commit:** `54b90e592d7b67588febc34651c63862d154d1f2`  
**Purpose:** Preserve prior work, separate proven PASS from PARTIAL/BLOCKED/UNKNOWN, prevent duplicate work, and define the next evidence-backed action.

## 1. Non-negotiable controls

- Legal use only; no bypassing access controls, licence terms, or publisher restrictions.
- Research spend must remain **₹0**. No paid API/SFTP, subscription, licence, or paid dataset.
- No external contact, registration, account creation, API-key request, data sharing, or production change without the user's explicit prior approval.
- Production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE`, and the 672 diagnostics (56 × 12) remain unchanged.
- `UNKNOWN` is neither PASS nor FAIL. No synthetic rows, invented timestamps, or unsupported source promotion.
- Hard Gate stays `BLOCKED` until all required P0 coverage, data-quality, and matured event-study acceptance criteria are met.
- PR #13 remains Draft; do not merge as part of this audit.

## 2. Status definitions

| Status | Meaning |
|---|---|
| **PASS** | The exact acceptance test and its artifact were inspected and support the claim. |
| **PARTIAL** | Some implementation/data exists, but a material coverage, provenance, permission, or acceptance gap remains. |
| **BLOCKED** | A known dependency or failed acceptance check prevents progression. |
| **UNKNOWN** | Evidence is not available in this snapshot; do not infer success or failure. |
| **ARTIFACT_UNVERIFIED** | A workflow may have run, but the artifact has not been inspected against the acceptance criteria. |

A workflow conclusion of SUCCESS alone is not sufficient to promote a data source or close a research gate.

## 3. Master workstream matrix

| ID | Workstream / prior work | Evidence currently established | Status | Remaining gap / next acceptance condition |
|---|---|---|---|---|
| M01 | V11.3 architecture and 672 diagnostics | Architecture and 56 × 12 design are established in project history and repository. | **PASS — frozen design** | Regression proof must continue to show no changes to selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or diagnostic count. |
| M02 | RBI DBIE monthly G-Sec yield adapter | Adapter QA Run `41314656919` PASS; 365 monthly observations, Apr-1996–Aug-2026, 30 tenors, 9,477 observations, no duplicate date/tenor keys; normalized CSV SHA-256 `772aca6e440ca1adba603b8c8d10f6da049111181035262d501813e181bd2e07`. | **PASS — monthly adapter QA** | Not a daily FBIL/FBIL-like series. Do not relabel as daily 10Y par yield. Factor use still subject to factor-registry source/frequency fit. |
| M03 | RBI DBIE same-snapshot Factor Registry audit | Run `41314900549` PASS; artifact ID `13085804606`; 35 factor groups, 31 partial, 4 disconnected; F14 remains partial and India bond-yield factor has data-quality warning. | **PARTIAL** | 4 disconnected groups and partial coverage remain. Re-run only after source repair; preserve same-snapshot rule. |
| M04 | FBIL official endpoint discovery | Official first-party routes identified: `/wasdm/gsec/fetch`, `/wasdm/gsec/fetchfiltered`, `/wasdm/gsec/downloadPublished`; read-only probing; no authentication bypass. | **PASS — endpoint discovery** | The live fetch endpoint returns archive metadata, not per-observation publication clock time. |
| M05 | FBIL historical archive backfill | Run #14 `41325197755` PASS. Inspected artifact ID `13089969056`: 236 XLSX archives downloaded, 236 parsed rows, 236 unique observation dates, 0 download errors, 0 parser errors, 0 quarantined files; date range 2025-11-03–2026-10-23. Normalized CSV SHA-256 `7dcd2b698cf2e92aa7f2ad515da5b4411a640509759ebdf554a34dc21e85908b`. | **PASS — archive collection & date/row parse only** | This is 236 archive observations, not proof that every date is a trading session. Publication timestamp coverage is 0%; do not infer 18:30 or another time. |
| M06 | FBIL release timestamp and permitted use | Parser deliberately leaves `PUBLISHED_AT_IST` and `RELEASED_AT_UTC` blank. FBIL written permission not obtained. | **BLOCKED — production eligibility** | Keep out of Production Factor Registry until publication-time provenance and lawful free internal-use rights are evidenced. Do not contact FBIL without fresh user approval. |
| M07 | FBIL latest workflow integrity gate | Run #13 `41324215737` failed due to an incorrect quarantine-count assertion. Corrected in commit `54b90e592d7b67588febc34651c63862d154d1f2`; Run #14 `41325197755` SUCCESS. Inspected artifact ID `13089969056`: 236 files, 236 rows, 236 unique dates, zero download errors, zero parser errors, zero quarantined files; timestamp coverage 0%; normalized CSV SHA-256 `7dcd2b698cf2e92aa7f2ad515da5b4411a640509759ebdf554a34dc21e85908b`. Legacy homepage HTML parser still has no historical Date+Time rows. | **PASS — archive integrity gate; still BLOCKED for production eligibility** | Verifier corrected in commit `54b90e592d7b67588febc34651c63862d154d1f2` to require zero mismatches and zero errors. A fresh workflow run and artifact review are still required. |
| M08 | NSE 200-session cache / manifest | NSE Benchmark Run #162 `41325197764` SUCCESS; artifact ID `13090719723`; 200/200 sessions, 200 valid cache hits, 0 misses, 0 network requests in warm-cache benchmark; elapsed 12.768868 sec (15.663 sessions/sec); manifest SHA-256 `d23b294d8b9a4b93f3aeab06778a01be4646f7071b549155953ea073383d7422`; snapshot ID `f90c01c1d7e228ab7282a96fef4dfb3ceca7f67675938926dac009f9cb92d72c`; dates 2026-01-07–2026-10-30. | **PARTIAL — 200-session count, manifest generation and warm-cache benchmark PASS; legacy provenance remains unresolved** | Manifest states legacy cached files lack original network URL and authoritative retrieval timestamp; mtime is only a local proxy. Need source-provenance classification and full dataset/manifest reconciliation before calling the 200-session dataset fully accepted. Warm-cache speed is not an acquisition-speed benchmark. |
| M09 | NSE acquisition provenance | Benchmark artifact contains diagnostics showing legacy cached rows without original source URL; a small number of misses were freshly fetched from NSE archives during benchmark. | **PARTIAL** | Verify source URLs, response hashes and retrieval times for every newly acquired file; do not invent provenance for legacy files. |
| M10 | NSE snapshot manifest QA | Manifest test output records 200 sessions and a manifest hash in Run #161 artifact. | **PASS — generated manifest check** | Full row-level reconciliation against canonical data and all required layers remains to be proven. |
| M11 | Step 1 — NSE Quarterly Results endpoint/schema repair | Run `41330698503` SUCCESS; integrated filing endpoint HTTP 200; 1,767 rows, four pages 500+500+500+267, unique rows 1,767, pagination complete; Step 1 endpoint/schema PASS. | **PASS — full pagination and endpoint/schema acceptance** | Preserve missing original-broadcast timestamps; never substitute `creation_Date`. |
| M12 | Step 2 — five-field quarterly disclosure metadata acceptance | Run `41334950000` SUCCESS; artifact `13094767719`, ZIP SHA-256 `90bf3546cd044782fba522940e5fe4180b9e39f072bf1f6c94e7f79dad9232e3`. Inspected: 1,767 raw = reported total = normalized rows; four pages 500+500+500+267; 1,767 unique source hashes; SYMBOL, ISIN, SOURCE_URL, PUBLICATION_TIMESTAMP, REPORTING_PERIOD each 1,767/1,767 valid; missing 0; ambiguous 0; duplicate hashes 0; all six acceptance tests true. Independent of XBRL/PDF extraction. | **PASS — metadata acceptance verified** | Does not imply full XBRL metric extraction, Step 3 news/catalyst coverage, or final hard-gate readiness. |
| M13 | Step 3 — News & Catalyst Join | Historical Run `39977796193`, artifact `12513903105` inspected: 10 unique cutoff-symbol pairs; 10 coverage rows; unknown coverage 0; verified news 1; unverified news 0; no-match GDELT query windows 9; timestamp-window failures 0; invalid article/query URLs 0; duplicate pairs 0. Verification report PASS (1/1 checked row). Research status `READY_FOR_PAIRED_ABLATION`; 9 no-match queries do not prove absence of news. New Run `41335754845` is a separate TESTCO transport smoke (0 RSS items; full acceptance NOT_EVALUATED); it does not invalidate the historical result. | **PASS WITH COVERAGE LIMITATION — historical snapshot; refreshed snapshot NOT_EVALUATED** | Preserve historical Step 3 PASS. For a new snapshot only, recover/build the frozen candidate cutoff-symbol universe and run full join coverage, publisher verification, 24h timestamp/no-look-ahead, quarterly catalyst linkage and row-level reconciliation. Do not repeat the historical 10-pair audit. |
| M14 | Step 4 — Macro-Geo P0 source groups | Run `41283471559` on `audit/run145-factor-registry-gap-audit`, artifact `13074955372`, SHA-256 `82352f62a22647ff6d6c4c2a448b73285e092808893f34768b8362e3e1f1dde4`, inspected. Repair report: crude_oil 211 rows (`AVAILABLE_SECONDARY`, official EIA XLS); usd_inr 203 rows (`AVAILABLE_SECONDARY`, community mirror, not direct RBI); corporate_events 1,689 rows (NSE official); fpi_dii_flows 208 rows (NSDL official; FPI 105 dates/151 days, DII 103 dates/150 days). Source coverage 8/8 `P0_COMPLETE`. Four-group validator: benchmark 10, sector 90, volatility 228, geopolitical 15 rows; all `AVAILABLE_VALIDATED`. | **PASS WITH SOURCE QUALIFICATIONS — Step 4 coverage acceptance** | Do not recollect without a new snapshot or freshness failure. Keep crude and USD/INR labelled secondary; geopolitical rows are media mentions, not verified event occurrence. Artifact is on PR #11 audit branch and has null `source_snapshot_id`/`snapshot_id`; do not equate it with PR #13 snapshot. Broader Factor Registry and regime gates remain blocked. |
| M15 | Step 5 — missing/stale hard-gate rejection | New isolated QA Run `41340059447` SUCCESS on the active PR #13 branch; artifact `13097241013`, SHA-256 `24f553d2983f5369904f6b545986d5b5d7b35955bae634341efd6c8043531099`. Inspected `hard_gate_negative_regression.log`: 3 tests PASS — aligned complete fixture permits PASS; missing required coverage input fails closed and preserves `UNKNOWN/BLOCKED`; stale/misaligned market panel (>3 calendar days vs equity panel) fails closed. Test run 0.017 sec. All tests assert selector, `RANKING_SCORE` and `+1 PRESSURE_FADE` unchanged. | **PASS — missing-input and stale/misalignment negative-test scope** | Preserve this bounded QA artifact. This proves missing-file and panel/equity date-misalignment rejection; it does not test absolute wall-clock staleness when both panels are equally old. Do not claim broader stale-source freshness coverage without a separate test. No production selector, score, pressure-fade or gate changes. |
| M16 | Step 6 — cross-artifact consistency audit | Run `41283471559` artifact `13074955372` has `same_snapshot_reconciliation.json` status `SAME_WORKFLOW_SNAPSHOT_WITH_RECONCILIATION_GAPS`; `source_coverage_csv_json_statuses_match=false`. Root cause found: `collect_india_macro_series.py` wrote `AVAILABLE` to CSV but `DATA_QUALITY_WARN` to JSON for `macro_indicators` and `inflation_components`. Repair branch `fix/source-coverage-status-reconcile` now uses one status mapping; Run `41340560881` SUCCESS, artifact `13097271838` inspected, 6/6 tests PASS. | **BLOCKED — code repair and unit regression PASS; end-to-end same-snapshot regeneration still required** | Re-run only the bounded same-snapshot reconciliation after regenerated outputs exist; require CSV/JSON status parity TRUE, all other checks TRUE, immutable snapshot identifier present, and Hard Gate blockers resolved independently. |
| M17 | Historical event study / matured labels | Event-study and historical-regime modules/workflows exist. | **BLOCKED / ARTIFACT_UNVERIFIED** | Need matured H+1/H+3/H+5 outcomes, reproducible event windows and source-timestamp alignment. Do not score immature labels. |
| M18 | Rolling backtest (1 Dec–26 Oct; ~2,700 shares) | User-defined methodology exists in project history: next-day Open entry, 1–5 day exit, 0.22% cost, base universe price >₹50 and average volume >200k. | **ARTIFACT_UNVERIFIED** | Verify input dataset, daily universe, fills, survivorship handling, costs, output ledger and comparison vs base. Do not report performance without artifact. |
| M19 | IPO-PLX V2.0 | Separate IPO discovery/post-listing overlay architecture exists in project design. | **UNKNOWN** | Do not include in V11.3 hard gates. Inspect cohort and W5/W10/W20 artifacts only if required for final paper scope. |
| M20 | Final research paper and evidence appendix | Deliverable structure is defined; cross-report audit and evidence appendix not complete. | **BLOCKED** | Requires accepted P0, provenance, data integrity, matured event study, backtest and regression evidence. |

## 4. Latest verified workflow ledger (2026-11-01)

| Workflow | Run ID | Conclusion | Artifact / evidence | Interpretation |
|---|---:|---|---|---|
| FBIL Provenance #9 | `41320496728` | SUCCESS | Artifact `13089092719` | Earlier backfill/parser attempt; later corrected. |
| FBIL Provenance #10 | `41320718563` | SUCCESS | Artifact `13088957286` | Corrected filename/date parsing run. |
| FBIL Provenance #11 | `41320723105` | SUCCESS | Artifact `13089432150` | Strict workflow at that revision; inspect only for its exact code revision. |
| FBIL Provenance #12 | `41324200203` | SUCCESS | Artifact available in run | Retry-enabled backfill; 236 files and parse success confirmed by latest artifact data. |
| FBIL Provenance #13 | `41324215737` | FAILURE | Artifact `13090164109` | Incorrect quarantine assertion; superseded by #14. |
| FBIL Provenance #14 | `41325197755` | SUCCESS | Artifact `13089969056`; ZIP digest `5ab17515fc6078fdd9f51b83e555a83e6afcbc44c8148b021dfe7320962560d4` | 236 rows, 236 unique dates, zero errors/quarantine; timestamp 0%. |
| NSE Benchmark #162 | `41325197764` | SUCCESS | Artifact `13090719723`; ZIP digest `8e442a108c7cf197b07f0c2be890e9db4492546e207c2d8b5d35f05d2b1142ed` | 200/200 warm-cache hits; 12.768868 sec; manifest/snapshot verified. |
| NSE Benchmark #161 | `41324215748` | SUCCESS | Artifact `13090408760`; ZIP digest `596f5f3d61b524612ec99ef5504dc422a279186a83aa8c26096bfd0a82aacaa1` | 200 sessions / warm-cache validation; provenance caveats remain. |

Earlier workflow outcomes from previous project sessions are retained as historical user-reported evidence only unless their exact artifacts are re-opened and rechecked. A past PASS is not automatically current acceptance.

## 5. Six-step audit gate — current position

| Step | Required work | Current status | Gate |
|---:|---|---|---|
| 1 | NSE Quarterly Results endpoint/schema repair | Run `41330698503`; artifact `13093865217` inspected; 1,767/1,767 rows across 4 pages, unique and complete; endpoint/schema status PASS | **PASS — CLOSED** |
| 2 | Results source URL, publication time, period, symbol/ISIN validation | Run `41334950000`; artifact `13094767719` inspected. All 1,767 raw/normalized rows reconciled; each of five fields 1,767/1,767 valid; missing 0, ambiguous 0, duplicate hashes 0; pagination complete; six acceptance tests true. | **PASS — CLOSED (metadata acceptance only)** |
| 3 | News/catalyst join coverage and timestamp alignment | Historical Run `39977796193` artifact `12513903105`: 10/10 pairs covered, unknown 0, verified 1, unverified 0, timestamp failures 0; 9 GDELT no-match query windows are a coverage limitation. New `41335754845` is a separate 0-item transport smoke. | **PASS WITH COVERAGE LIMITATION (historical); refreshed snapshot NOT_EVALUATED** |
| 4 | Four Macro-Geo P0 source groups | Run `41283471559` artifact `13074955372` proves 8/8 required P0 groups available and four-group validator PASS. Secondary-source and event-occurrence qualifications remain; artifact belongs to PR #11 audit branch, not PR #13. | **PASS WITH SOURCE QUALIFICATIONS (artifact snapshot)** |
| 5 | Missing/stale hard-gate rejection test | Run `41340059447`, artifact `13097241013` inspected; missing required input and stale/misaligned market/equity panel tests both reject; aligned complete fixture passes; frozen invariants unchanged. | **PASS — defined negative-test scope** |
| 6 | New audit artifacts and cross-report consistency review | Depends on Steps 1–5 | **BLOCKED** |

## 6. Exact next-action queue (no duplicate work)

1. FBIL archive integrity gate is now closed at Run #14; do not repeat this work. Keep FBIL out of Production because timestamp provenance and written use permission remain unresolved.
2. Quarterly Results Step 1 and Step 2 metadata acceptance are closed: Step 1 Run `41330698503`; Step 2 Run `41334950000`, artifact `13094767719` inspected. Do not repeat the five-field metadata audit unless source snapshot changes. XBRL financial-metric extraction remains a separate downstream workstream and must not be conflated with Step 2 metadata PASS.
3. Preserve historical Step 3 Run `39977796193` PASS WITH COVERAGE LIMITATION (10 pairs, 1 verified story, 9 no-match query windows). Do not rerun that historical snapshot. For a genuinely new snapshot, first recover/build its frozen candidate cutoff-symbol universe; then run full join acceptance. Run `41335754845` is transport-only and does not supersede the historical PASS.
4. Preserve Step 4 P0 coverage evidence from Run `41283471559`: 8/8 required groups available; four-group validation PASS; crude/USDINR explicitly secondary. Do not rerun collection absent a new snapshot, freshness failure or provenance correction. Keep overall hard gate blocked for Factor Registry and historical-regime gaps.
5. Step 5 missing-file and stale/misaligned-panel rejection tests are now PASS in isolated Run `41340059447`; preserve artifact `13097241013`. Absolute wall-clock staleness when both panels are equally old remains outside this test scope.
6. Only after all dependencies pass, run the final consistency audit and matured event study/backtest.

## 7. Current phase verdict

**The project is not starting from zero.** Existing work is preserved. The current state is a mixed **PARTIAL + BLOCKED** state:

- Proven passes: RBI DBIE monthly adapter QA; FBIL archive download/row parsing at the latest inspected artifact; NSE 200-session count and warm-cache check; NSE manifest generation check.
- Partial: Factor Registry coverage, NSE legacy-cache provenance, FBIL timestamp provenance and usage permission, Macro-Geo four-group coverage.
- Proven passes: Quarterly Results Step 1 full pagination/schema acceptance (1,767/1,767 rows) at Run `41330698503`; Step 2 five-field metadata acceptance (1,767/1,767 for each field) at Run `41334950000`.
- Historical Step 3 has PASS WITH COVERAGE LIMITATION (Run `39977796193`); current refreshed-snapshot join is NOT_EVALUATED, not a historical regression. Step 4 P0 coverage has PASS WITH SOURCE QUALIFICATIONS (Run `41283471559`), while the wider Factor Registry and historical-regime anchors remain incomplete. Step 5 negative-test coverage remains PARTIAL. XBRL metric extraction, matured event-study interpretation, final cross-artifact consistency and final paper remain incomplete.
- Unknown/artifact-unverified: historical runs whose artifacts have not been reopened in this snapshot.

**No claim of 100% completion is made. Hard Gate remains BLOCKED.**

## 8. Historical PASS evidence reconciliation — 2026-11-02

This section preserves earlier PASS claims with their exact acceptance scope. A newer bounded smoke is not treated as a replacement for an older full-scope artifact. Branch and snapshot boundaries remain explicit.

| Step | Historical evidence recovered | Reconciled decision |
|---:|---|---|
| 1 | Run `41330698503`, artifact `13093865217`: 1,767 records, four pages, complete pagination and endpoint/schema acceptance. | **PASS — CLOSED** for endpoint/schema and pagination. |
| 2 | Run `41334950000`, artifact `13094767719`: five metadata fields each 1,767/1,767; missing, ambiguous and duplicate hashes 0. | **PASS — CLOSED** for metadata only; XBRL metric extraction is separate. |
| 3 | Run `39977796193`, artifact `12513903105`, SHA-256 `5dbf03176d7d655a533c04f97f27c56209948b3b8318515a6b4af98bce6e3b59`: 10 cutoff-symbol pairs, unknown coverage 0, 1 verified story, 9 no-match query windows, 0 timestamp failures, 0 invalid URLs, 0 duplicate pairs. | **PASS WITH COVERAGE LIMITATION** for historical paired-ablation readiness. Run `41335754845` is only a separate 0-item TESTCO smoke and does not invalidate the historical result. |
| 4 | Run `41283471559`, artifact `13074955372`, SHA-256 `82352f62a22647ff6d6c4c2a448b73285e092808893f34768b8362e3e1f1dde4`: P0 8/8; crude, USD/INR, corporate events and FPI/DII available; four-group validator PASS. | **PASS WITH SOURCE QUALIFICATIONS** for P0 coverage on that artifact snapshot. EIA crude and community USD/INR are secondary; geopolitical media mentions do not independently prove occurrence. |
| 5 | Run `41283471559` hard-gate report is BLOCKED and fail-closed. Follow-up isolated Run `41340059447`, artifact `13097241013`, proves missing required input and >3-day market/equity date misalignment reject; aligned fixture passes; invariants unchanged. | **PASS — defined negative-test scope**; absolute wall-clock staleness is not covered. |
| 6 | Run `41283471559` manifest reconciliation says RECONCILED, but hard gate remains BLOCKED and snapshot IDs are null. | **BLOCKED** for final release and final paper sign-off. |

### Branch and snapshot boundary

- Step 1/2 current acceptance and Step 3 historical evidence are preserved by their own Run IDs and artifacts.
- Step 4 Run `41283471559` was executed on `audit/run145-factor-registry-gap-audit` (PR #11 branch), not PR #13. Its result is preserved as historical evidence, not represented as a PR #13 artifact.
- PR #13 remains Draft and unmerged.
- The Step 4 manifest has `final_manifest_reconciliation.status=RECONCILED`, but `source_snapshot_id` and `snapshot_id` are null; it is not an immutable snapshot identifier for final cross-report sign-off.

### Next action after reconciliation

Do not rerun Steps 1–4. Close the remaining Step 5 QA evidence gap with isolated deterministic tests for (a) missing required input and (b) stale/misaligned market panel. Run only a bounded regression suite, inspect its test report, and verify frozen production invariants. Then proceed to Step 6 using one immutable snapshot identifier.


### Step 5 bounded regression evidence — 2026-11-02

- Workflow [Run `41340059447`](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/41340059447) SUCCESS on `fix/factor-registry-same-snapshot-reconcile`.
- Artifact `13097241013`, ZIP SHA-256 `24f553d2983f5369904f6b545986d5b5d7b35955bae634341efd6c8043531099`; inspected log contains 3/3 passing tests in 0.017 sec.
- Missing required coverage input → BLOCKED; `candidate_release_allowed=false`; semantics remain `UNKNOWN/BLOCKED`.
- Market panel/equity date gap >3 calendar days → `MARKET_PANEL_STALE_OR_DATE_MISALIGNED` and BLOCKED.
- Aligned complete fixture → PASS.
- All three invariants reported unchanged: production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`.
- Scope limitation: this validates missing input and cross-panel stale/misalignment rejection; it does not prove absolute wall-clock freshness when both panels are equally old.


### Step 6 defect root cause and bounded repair — 2026-11-02

- Existing Run `41283471559` reported `source_coverage_csv_json_statuses_match=false`.
- Exact substantive mismatches: `macro_indicators` and `inflation_components` were `AVAILABLE` in CSV but `DATA_QUALITY_WARN` in JSON. The JSON status is correct because both histories are partial; nonzero row count alone must not promote them.
- Fix is isolated on branch `fix/source-coverage-status-reconcile`: one shared status override updates both JSON and CSV. Also corrected selectolax import to maintained Lexbor backend after Run `41340507789` exposed the deprecated Modest import.
- Run `41340560881` SUCCESS; artifact `13097271838` inspected; 6/6 tests pass in 0.006 sec, including CSV/JSON parity.
- Step 6 remains BLOCKED until a full same-workflow artifact is regenerated and inspected with `source_coverage_csv_json_statuses_match=true`, all other reconciliation checks true, and a non-null immutable snapshot ID. This bounded unit test is not represented as a full Step 6 PASS.


## 9. Quarterly Results XBRL metric extraction — artifact recovery and verification (2026-11-12)

This addendum updates the earlier `ARTIFACT_UNVERIFIED / UNKNOWN` state for the **separate XBRL financial-metric extraction workstream**. It does not alter the earlier Step 1 endpoint/schema PASS (1,767 disclosures) or Step 2 five-field metadata PASS (1,767 disclosures); those are separate acceptance scopes.

### Verified source batches

| Batch | Run ID | Artifact ID | Source disclosures | Artifact SHA-256 |
|---|---:|---:|---:|---|
| Batch 1 | `41585837753` | `13207184371` | 1,000 | `0b8b07e6bbc59bcc87016ed3b96cf54ad01d5b2dfeb3a7fa8f5f748489b25829` |
| Batch 2 | `41587465930` | `13209235865` | 988 | `7bee96713ea6d1f85fd9ea7b79316cca1a18747d2c176b5ad25121b1434bc415` |

Both source workflow runs have GitHub conclusion SUCCESS. Their exact run/artifact IDs and digests were rechecked against the GitHub Actions API.

### Global reconciliation

- Workflow: `Quarterly Metric Batches Global Reconciliation`
- Run ID: `41588275108`; conclusion SUCCESS; commit `e60d749b5df5df9e7230c4a92545a5ac55f519d0`.
- Artifact: `quarterly-metric-batches-global-reconciliation`; ID `13209151475`; 24,098,158 bytes.
- GitHub artifact ZIP SHA-256: `f0f53e610f8e0ae53f93a9c46f2246e82324538dca252556df0a70f60a230997`.
- Artifact was downloaded again and its ZIP SHA-256 independently recomputed; it matches GitHub's digest.
- ZIP contains 1,920 files, including 1,911 XBRL evidence files; no PDF evidence files were present in this artifact.
- Source disclosure rows: 1,988; merged ledger rows: 1,988; unique source URLs: 1,988; evidence-file SHA-256 checks verified: 1,988.
- Final global status counts: `SOURCE_LINKED_XBRL_FACTS=1864`, `SUPERSEDED_BY_LATER_DISCLOSURE=118`, `BLOCKED_NO_VERIFIED_XBRL_METRICS=6`.
- Computed feature rows: 1,864; symbols: 1,021; exact duplicate feature rows removed: 0; consensus rows: 0.
- No ambiguous latest-period-basis blocker was accepted by the workflow assertion.
- Production invariants all false for change: selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and diagnostics 672.

### Recomputed artifact file hashes

| File | SHA-256 |
|---|---|
| `data/raw/quarterly_financial_metrics.csv` | `8687356bd833ac78d2dd01e7eb356d32043cc4045f75baba8a02d6174a74d561` |
| `outputs/quarterly_results/quarterly_financial_features.csv` | `7dd5766e5879165fbce6790a43895f737feab2cc9e23f901ce55e14d2be3142d` |
| `outputs/quarterly_results/quarterly_metric_batches_reconciliation.json` | `aedd23722e74df233ece11299f318368a24ab78bf4305cf07faa2bf5a844a0af` |
| `outputs/quarterly_results/quarterly_metric_batch_manifest.json` | `3c004b77076285a7b66248686c28630ed9fc025fb3661bf732667df630864963` |
| Batch 1 source disclosures CSV | `1f95e41758e397191294d4843601588eeb0b73c8ce7b4ef79913817fd0b7a7d7` |

### Reconciled status and remaining limits

**Status: ARTIFACT VERIFIED — PASS WITH EXPLICIT BLOCKERS.** The previous UNKNOWN/ARTIFACT_UNVERIFIED label is superseded for this exact 1,988-disclosure extraction and global-reconciliation artifact. Do not rerun the two extraction batches or the successful global reconciliation workflow merely to refresh the status.

The 118 superseded revisions and 6 blocked disclosures remain explicit non-current/non-verified records; they are not promoted to valid feature rows. The artifact proves 1,864 computed feature rows from source-linked XBRL facts, not 1,988 fully verified metric rows. The ZIP's evidence inventory contains XBRL files only and no PDF files, so this artifact does not establish PDF-table metric extraction. Further PDF extraction or treatment of the six blocked records requires a separately scoped, source-backed task and must preserve their current blocked status until independently verified.

This closes the artifact-verification gap only. It does not close matured H+1/H+3/H+5 event study, rolling backtest, overall Factor Registry, Macro-Geo, Step 6 same-snapshot reconciliation, Hard Gate, or Final Research Paper acceptance.


## 10. NSE 200-session provenance refresh — independently inspected artifact (2026-11-12)

- Workflow Run `43245527846` — SUCCESS on the PR #13 head commit `a44434fda193c1d8246cc44e4e6c7527b40c2488`; job completed successfully. Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43245527846
- Artifact `nse-200-session-cache-verification-331`, ID `13955899352`; GitHub ZIP digest `sha256:1833c75c09c89e7610ad3fbdff62bbdf9a67737e2b39c1e4bf223bddc3a1e070`. Downloaded and independently recomputed ZIP SHA-256; exact match.
- Artifact contains 212 files. Snapshot manifest `raw/nse_snapshot_manifest_ee037b46aa2e8e7b.json`: 200 expected and actual sessions, 200 unique trade dates and files, 2026-01-21 through 2026-11-12.
- Snapshot ID: `ee037b46aa2e8e7bce7df51919aada51418fd03787a1ed740a103f4b47804305`; manifest file SHA-256: `ab37d0e14458aceaa13b7684e5739d9486c27e4b3f04d2667e1911abd568a17a`.
- Independently checked every one of the 200 manifest records: all have a source URL, retrieval timestamp, 64-character SHA-256, schema_validation=`validated`, cache_origin=`network`, acquisition_status=`OK_FULL_BHAVCOPY_DELIVERY`, successful HTTP 200 response, matching successful-response URL, present local file, and exact local-file SHA-256 match. Result: **200/200 record-level source/hash matches**.
- Acquisition diagnostics contain 213 calendar-date checks: 200 `OK_FULL_BHAVCOPY_DELIVERY` and 13 `MISS` (non-session/lookback dates); no failed session is silently counted as one of the 200 valid sessions.
- Warm-cache QA: 200/200 hits, 0 misses, 0 network requests, 16.770754 seconds, 11.926 sessions/sec. This is a local warm-cache benchmark, not an acquisition-speed benchmark.
- `qa/snapshot_manifest_result.json` reports 200 sessions and the same snapshot ID. Artifact ZIP digest and snapshot manifest SHA-256 independently recomputed and matched.
- **Bounded status update:** this exact 2026-11-12 snapshot demonstrates complete URL/retrieval-time/response-hash/local-file-hash provenance for all 200 manifest records, unlike the earlier legacy-cache snapshot. However, the manifest's static `provenance_limitations` array still claims pre-existing legacy cache records lack original URL/retrieval timestamps. This text is inconsistent with the 200 current records and must be reconciled in the manifest-generation/reporting logic before promoting the broader NSE provenance workstream to unconditional PASS. Preserve the warning; do not silently delete it or overstate historical provenance.
- No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or 672-diagnostic changes were made. No PR merge was performed.



## 11. NSE cache provenance crosswalk — artifact lineage correction and exact-hash confirmation (2026-11-12)

### 11.1 Cache-only candidate semantics

The later cache benchmark artifact is not a fresh network retrieval. Its 200 manifest records have acquisition status \`CACHED\`, cache origin \`pre-existing-cache\`, and no direct source URL or successful-response hash. This is accurately represented as cache-only evidence; local file mtime is not promoted to an authoritative retrieval timestamp.

- Benchmark run: \`43252429755\` — SUCCESS.
- Artifact: \`nse-200-session-cache-verification-340\`, ID \`13961345601\`.
- Artifact ZIP SHA-256: \`1fbf6836b26f7cc823f816f26c5cb1f6ff8af48a998b0f5f1566d68400a7016c\`.
- Snapshot ID: \`250fb46b8d6d1696b9718ecafdf59cee7d80c6a6341e6e29c7d85432d5dd7b39\`.
- Manifest SHA-256: \`720e44b1bc3ef1df5f55f8a509d9b92bcae3236656fd2de4f02b9339dff55c65\`.
- 200 selected sessions; warm-cache benchmark 200/200 hits, zero misses, zero network requests, 12.752288 seconds. This is local cache validation only.

### 11.2 Exact-hash inherited provenance crosswalk

The crosswalk was rerun with matching candidate artifact pins and downloads after correcting two workflow defects: the candidate download had pointed to artifact 332 while the report pinned artifact 333, and an escaped GitHub Actions expression caused a bad-credentials failure.

- Workflow correction commit: \`1811620794380f967d0d748be3af6eec4eb1e97d\` (candidate download aligned to run 43249886595 / artifact 13957294024).
- Token-expression correction commit: \`60d43af7b3f62cd3d6a6f0f8ef287882d14102c8\`.
- Failed diagnostic run retained: \`43255640632\` — failure caused by literal backslashes in \`GH_TOKEN\` and \`GH_REPO\` expressions; no evidence was promoted from this run.
- Corrected crosswalk run: \`43255859354\` — SUCCESS.
- Crosswalk artifact: ID \`13960994076\`, ZIP SHA-256 \`5fb55edcbb06b80f4f612f146d63d9cf5188944ad36080b14e87e43824109733\`.
- Crosswalk report SHA-256: \`b7d01bb9cf72e3a3c721dc9af5b8a40293855044eeb08b35a2573a557ce1c5fc\`.
- Reference: run \`43245527846\`, artifact \`13955899352\`, 200 official NSE HTTP 200 records.
- Candidate: run \`43249886595\`, artifact \`13957294024\`, cache-only snapshot; direct retrieval is explicitly not claimed.
- Reconciliation: 200/200 trade dates, filenames, byte counts, content SHA-256 values, candidate schema validations, official source URLs, reference HTTP 200 records and reference retrieval timestamps; unmatched records = 0.
- Result: \`PASS_CONTENT_IDENTICAL_TO_PREVIOUSLY_SOURCE_VERIFIED_SNAPSHOT\`.

A further independent ZIP inspection compared the later artifact 340 with the crosswalk candidate artifact 333: both have the same snapshot ID and manifest SHA-256, and all 200 raw NSE session CSV files have identical SHA-256 values. Therefore artifact 340 has the same exact file content as the already-crosswalked candidate. This is inherited evidence only, not a new NSE retrieval.

### 11.3 Macro-Geo same-snapshot reconciliation — still blocked

- Macro-Geo reconciliation workflow run \`43254145873\` completed SUCCESS as an audit/artifact workflow, artifact ID \`13961036859\`, ZIP SHA-256 \`c8efd6a90c0ae2e571333ef3393e604e37f3f0df3872e21507009cfdbb679ac2\`.
- The contained \`same_snapshot_reconciliation.json\` is **not PASS**: status \`INCOMPLETE_REQUIRED_EVIDENCE_MISSING\`; missing file: \`data/processed/nse_eq_200_sessions.csv\`.
- The exact old P0 cache key \`macro-geo-nse200-audit/run145-factor-registry-gap-audit-41274367993\` is unavailable. The workflow correctly refuses to substitute a differently dated NSE panel.
- The original P0 artifact (run \`41283471559\`, artifact \`13074955372\`) does not contain the missing processed NSE equity panel. The later 200-session NSE archive is a distinct snapshot and must not be silently substituted as the old P0 panel.
- Source coverage JSON/CSV parity is PASS: 35 source keys each, zero duplicate keys, zero status mismatches. This does not establish full factor coverage.
- Factor Registry: 35 groups audited; 0 fully available, 22 partial, 13 not connected, 0 unmapped.
- P0: 8/8 required groups available in the retained audit.
- Event study: 43 events, 29 eligible, 14 pending; 26 events have matured H+1 and 25 matured H+5 windows.
- Historical regime study: 11 anchors, 9 with windows, 2 without windows; anchor coverage incomplete.
- Hard Gate remains \`BLOCKED\` for \`FACTOR_REGISTRY_HAS_INCOMPLETE_SOURCE_COVERAGE\` and \`HISTORICAL_REGIME_ANCHOR_COVERAGE_INCOMPLETE\`. Candidate release remains disallowed.

### 11.4 Next acceptance work

1. Recover or regenerate a fully evidenced NSE equity panel for the Macro-Geo P0 workflow, with its own immutable snapshot identity and explicit date alignment to the market panel; do not substitute the newer cache snapshot without recomputing dependent audits.
2. Re-run the same-snapshot reconciliation on one exact workflow snapshot and require the NSE panel file, hashes and all reconciliation checks.
3. Close Factor Registry source gaps and verify the 11 historical regime anchors from primary sources before reconsidering Hard Gate.
4. Keep matured H+1/H+3/H+5 event windows, rolling backtest and final paper gates separate from operational workflow success.

### 11.5 Production invariants

No production selector, \`RANKING_SCORE\`, \`+1 PRESSURE_FADE\`, or 672-diagnostic changes. No production integration and no PR merge. Research remains ₹0 spend and free official sources only. \`UNKNOWN\` remains neither PASS nor FAIL.
