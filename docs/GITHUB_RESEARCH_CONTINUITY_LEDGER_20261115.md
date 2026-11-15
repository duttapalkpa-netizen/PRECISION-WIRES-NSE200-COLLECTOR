# PRECISION-WIRES V11.3 — GitHub Research Continuity Ledger
**Snapshot:** 2026-11-15  
**Purpose:** Durable hand-off ledger. Research/QA only. This document records known evidence and blockers; it does not authorize production changes or PR merges.

## 1. Immutable project constraints
- CORE-672 remains 56 Steps × 12 Filters = 672 diagnostic signals.
- Five engines A/B/C/D/E and IPO-PLX V2.0 remain in scope.
- Do not change Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, Hard Gate, or engine logic without explicit authorization.
- UNKNOWN is never PASS. No synthetic data, fabricated timestamps, inferred source provenance, or forward-fill.
- Free official sources only; research spend ₹0; no paid APIs/subscriptions.
- All PRs #34, #35, #36, #37 remain Draft/Open/Unmerged unless the user explicitly authorizes otherwise. PR #20 remains Open/Unmerged.
- Prefer short, bounded CI runs (ideally 20–60 seconds; maximum target 10 minutes). Do not repeat already-passing tests without a code change or new evidence.

## 2. Repository and continuity
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- User's research continuation pages: “গবেষণা যাচাই অব্যাহত” 1–28, latest page 28 on 2026-11-15.
- Maintain a cumulative ledger of exact statuses, run IDs, job IDs, artifact IDs, commit/blob SHAs, SHA-256 digests, source URLs, and decisions. This snapshot consolidates the currently available verified context; it is not a claim that every historical page's raw transcript is stored in this file.

## 3. PR register
### PR #20 — Global Capital Rotation overlay
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/20
- Open/Unmerged. Overlay progress previously assessed at 62.5% (5/8 milestones); production integration 0% and unauthorized.
- USD H.10 broad index is not ICE DXY. DTWEXBGS must not be aliased to DXY. Broad EM flows are not India FPI.

### PR #34 — IMF BOP DSD workflow
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/34
- Branch: `research/register-imf-bop-dsd-workflow`
- Sync commit: `86c132676f467cda788f9e7acbbfb9cd6db6f790`; workflow blob: `9d7ba026b42a50108e4f9fec06e39f687ad26a5e`.
- Draft/Open/Unmerged. Workflow is workflow_dispatch-only, read-only, 5-minute timeout. SDMX 2.1 BOP Dataflow `IMF:BOP_BPM6:1.0`; Constraint `IMF:BOP_BP6_CONSTRAINT:1.0`; exact structure ref `IMF:BOP:2.6.0`.
- Parser/fixture QA passed locally; no live IMF XML acquired and no live workflow dispatch. Live IMF acquisition/runtime/country/frequency coverage remains 0%.

### PR #35 — NSE Full Delivery date-integrity guard
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/35
- Branch: `research/nse-date-integrity-guard-20261115`
- Latest commit: `07af523e5c12b75ee60a38844c8d09ca77673a61`
- Run #2 ID `43726244428`, Job `132848686824`: SUCCESS, 7/7 tests PASS.
- Draft/Open/Unmerged.

### PR #36 — Full Delivery + UDiFF + cached/legacy date-integrity hardening
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/36
- Branch: `research/nse-date-integrity-all-paths-20261115`
- Head: `7e4a30c971e65bef78343f91264595a694abb998`; UDiFF hardening commit `deb1539c506b8cb7ca27568da418a29b69abbf5d`.
- Original date tests Run #7 ID `43727475251`, Job `132852454675`: 11/11 PASS.
- Hardened regression Run #12 ID `43728332581`, Job `132855053289`: 17/17 PASS.
- Live probe Run #2 ID `43728332551`, Job `132855053336`: SUCCESS.
- Live NSE sources for 2026-11-13: Full Delivery URL `https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_13112026.csv`, UDiFF URL `https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20261113_F_0000.csv.zip`, legacy URL `https://archives.nseindia.com/products/content/sec_bhavdata_full_13112026.csv`. Each returned HTTP 200, 2,744 EQ rows, zero invalid/mismatched dates. Artifact ID `14166914556`; SHA-256 `5beab6b56e9f10196e92efd395800e00f95b3e9a0227a8eb0c4335bb64b62778`.
- Draft/Open/Unmerged.

### PR #37 — Raw NSE manifest retention and date-integrity carry-forward
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/37
- Branch: `research/nse-raw-manifest-retention-20261115`
- Current head at snapshot: `16ae92b21ca6c956ddd2764a69f930131a5bbe92`; PR Open, Draft, Unmerged.
- Commit chain (chronological):
  - `434d906a66b27bea60cca59242027a89d99b0d5a` initial manifest script
  - `4a5fc03a70527f5d27e11cb8aab61c41a41f3f8b` workflow/raw artifact inclusion
  - `f4dd4791256f4f77bd253b75098c5ead9d3e2fad` parse errors fail-closed
  - `801f1fc798ad66e6f0b4c596ece9364ef11030a9` invalid filename/duplicate session hardening
  - `e438184436d0aa3c03daca99bf45b69531e3571c` initial tests
  - `34b4d2b7d1e7ea7733417856c6577dd4f16e75c0` tests workflow
  - `c3de86c5a7731d59777eed0a7a100306fc49f582` official live probe workflow
  - `2a6103c2f25ab621621c83d2d8eebf1f4dbfdb08` unittest argparse compatibility fix
  - `d3b8b0200beb4416d187bcd20dad32e2161388b3` strict date-integrity implementation carried from PR #36
  - `85bd8df576dd020e8067fcdc6bb12f90b7f4c94c` 17 date-integrity tests carried forward
  - `16ae92b21ca6c956ddd2764a69f930131a5bbe92` date-integrity workflow
- Manifest script: `scripts/research/build_raw_archive_manifest.py`. It hashes each raw CSV, compares filename date with every EQ-row embedded date, validates sessions list, fails closed on malformed/missing dates, duplicate dates/files, parse errors, and can enforce `--expected-sessions 200`.
- Main collector workflow calls the manifest after Strict QA and uploads `data/raw/` plus processed/QA outputs.
- Latest head workflow runs:
  - Run `43731507465` — NSE Raw Manifest Official-Source Probe — SUCCESS.
  - Run `43731507548` — NSE Raw Archive Manifest Tests — SUCCESS (7/7).
  - Run `43731507487` — NSE Date Integrity Tests — SUCCESS (17/17).
  - Thus 24/24 targeted tests and one-session official source probe are verified on the current head.
- Earlier argparse regression: Run `43731245541` failed with SystemExit 2; fixed by `parse_known_args`; subsequent Run `43731311911` Job `132864132941` passed 7/7.
- Latest live probe artifact ID `14169025516`; digest `f5f9931eb7c0c291a6087b31cde7a1aabd2f85a7a3e9eafa4e0c90da1142a8b1`.
- A one-session official NSE raw file was independently probed: 2026-11-13, 2,744 EQ rows, zero date mismatch; earlier artifact ID `14168103318`.
- A prior artifact from collector Run `43687120198`, artifact ID `14151241008`, ZIP SHA-256 `5e4596f93454cca24d4a276e26bad99e6bc01adb574510506eae26a67c74a238`, contains processed files but no `data/raw/`; therefore it cannot prove retention of 200 original session CSVs.
- The processed aggregate audit for that artifact: 502,150 rows; 2,994 symbols; 200 dates (2026-02-09 to 2026-11-13); no missing/invalid dates, duplicate symbol-date keys, nonpositive OHLC, invalid OHLC relationships, negative volume/delivery, or delivery percent outside 0–100. SERIES has whitespace (`' EQ'`) but trims to EQ. Audit status PARTIAL_PASS, not full raw archive PASS.
- Full 200-session raw archive manifest/artifact acceptance remains 0% / NOT_DONE / BLOCKED. QA report claims raw_files=200, but the artifact omitted the raw CSVs; this is not independent proof.
- Collector currently exposes `--sessions`, `--lookback-days`, `--out`, but no explicit start/end date batch controls. It loops backwards from today and tries Full Delivery, UDiFF, then legacy source. Main workflow timeout is 60 minutes.
- Current GitHub tool integration has no workflow-dispatch action. Do not claim a 200-session collector was dispatched. A practical next design is bounded date-range shards (ideally ≤10 minutes each), with a final merge/manifest artifact proving exactly 200 unique sessions. The shards must retain original raw bytes; do not synthesize dates. A workflow can be triggered by PR changes if configured for pull_request, but actual completion must be verified from runs/artifacts.
- Do not repeat 24/24 tests or one-session probe absent code changes/new evidence.

## 4. Historical Step 4 / Macro-Geo P0 blockers
- Step 4 Macro-Geo P0 Event Study remains BLOCKED; Step 5 Final Research Paper remains BLOCKED until Step 4 acceptance.
- Known blockers: Factor Registry incomplete (13 factor IDs / 18 unique source groups in recent tracking); FRED Brent collection; historical news backfill; insufficient matured event windows.
- Acceptance criteria: `hard_gate_report.json` status PASS; blockers empty; `candidate_release_allowed=true`; historical event source URL and publication timestamp; sufficient matured windows.
- Earlier Run #88: collector/QA PASS but hard gate BLOCKED, P0 6/8; `corporate_events` 0 valid rows; `fpi_dii_flows` 2 rows / 1 date (requires ≥60 dates and ≥90-day span); 0 matured event windows; blocker `EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS`.
- Earlier Run #111: run ID `38781833983`, commit `dd5f6aa`, prospective-audit job SUCCESS, artifact 84,026 bytes; core QA/reproducibility PASS, quarterly feed/news join/Macro-Geo gate BLOCKED; candidate release false.
- Earlier related commits: `e9e3bdee0136`, `44d48359d481`, `6e4eb595f2fc`.
- Six-step audit sequence: (1) NSE quarterly endpoint/schema repair; (2) verify source URL/publication time/reporting period/symbol-ISIN; (3) news/catalyst coverage and timestamp alignment; (4) connect missing Macro-Geo P0 groups; (5) missing/stale input rejection test; (6) inspect new audit artifacts. Do not skip or claim Step 4 PASS.

## 5. Other evidence tracks
### NSE archive
- User previously reported 317 sessions collected on 2026-11-12; separate verified collector artifact above contains 200 processed sessions. Do not conflate 317 claimed sessions with 200-session artifact.
- Preserve manifest and SHA-256 evidence. Raw originals are required for full audit.

### H.10 macro data — completed, do not repeat
- Run `43276577238` SUCCESS; artifact `13970661965`; ZIP SHA-256 `a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691`.
- 26/26 raw H.10 files; 304,510 dated rows, 291,831 numeric, 12,679 missing markers retained; date union 1971-01-04–2026-11-06, 14,570 dates.
- Exact NSE 200-session join PASS (2026-01-21–2026-11-12), 200/200 NSE files and 26/26 H.10 series hashes verified. Each series 190/200 numeric (95%); missing source markers retained, no forward-fill.
- Broad USD derived seed row 2026-11-06. DTWEXBGS is broad nominal trade-weighted USD, not DXY.

### IIP / NIC — do not repeat completed audits
- PR #21 and #23 open/unmerged.
- Run #251 ID `42501079840` SUCCESS; 41-vintage audit, 1,058 snapshot differences across 116,740 observations, 36 raw workbooks parsed, one legacy workbook HTTP404.
- Run #254 ID `42507902637` SUCCESS; 69-row PIB supplementary snapshot, 23 NIC codes × 3 periods; artifact `13628033276`, ZIP SHA `a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b`; 69/69 values matched MoSPI PDF Statement IV.
- Old 2011-12/NIC-2008 IIP series ends March 2026; old series April 2026 HTTP404 is NOT_APPLICABLE unless catalogue says otherwise.
- New IIP base 2022-23; MoSPI sources conflict NIC-2008 vs NIC-2025; mapping remains CONFLICTED/UNKNOWN. Do not promote NIC-2025 or apply generic 4-digit concordance without item-level evidence.

### Cost-aware V11.3 backtest — research only
- User-approved rules: next-session OPEN entry; intraday HIGH target touch; stop −3%; if neither, horizon final-session CLOSE; same-bar ambiguity stop-first; 0.22 percentage-point cost once per completed trade.
- Module `pipeline/v11_3_cost_aware_backtest.py`, source blob SHA `32b556717dab70d0b37de69a6e3d98105edd1702`; 8 unit tests plus hardening; Run #5 `43692427702` and Run #7 `43696699661` SUCCESS.
- Representative artifact `14151241008` / Run `43687120198`: 3,000 signals, 100 cutoffs, 200 sessions. 9,000 simulations. H+1 2,991 executed, 422 targets, mean net −0.6981%; H+3 2,975 executed, 255 targets, mean net −0.6998%; H+5 2,966 executed, 84 targets, mean net −0.7244%.
- Reconciliation ZIP SHA-256 `775efb09c5b6bb0f3c8da486f47143356f3f414d9fc65bbec43315b0767ecdff`.
- Holdout readiness ZIP SHA-256 `2300f91814d1dcb383ce0c0c59294026af3d419e9de5eedd3712dcf3548874f0`; prereg readiness 100%, holdout execution 0%, acceptance BLOCKED. Do not reuse the historical window as untouched holdout.
- Cost-aware acceptance remains BLOCKED: slippage, market impact, circuit/price-band feasibility and portfolio concurrency not modeled.

### CORE-672 implementation audit
- Existing diagnostics script creates 672 columns but only 3 unique full-column state vectors across 672 columns (540 one vector, 120 another, 12 third; 132 constant UNKNOWN) in audited artifact. This does not prove 672 independent implemented diagnostics. Do not change matrix; record as implementation/evidence gap.

## 6. Current next action and acceptance
1. Design/implement a bounded, reproducible date-sharded raw acquisition path, each shard with explicit start/end dates and a ≤10-minute timeout.
2. Ensure shards retain original NSE raw CSV bytes and source-date validation; no date inference/backfill.
3. Combine shards into one exact 200-session archive and generate `sessions.txt`, per-file SHA-256 manifest, duplicate/missing checks, and embedded EQ-date reconciliation.
4. Upload one final artifact containing all `data/raw/` files and manifest. Verify artifact contents and digest independently.
5. Only then mark full 200-session Raw Archive PASS. Until then: BLOCKED.
6. Keep PR #37 Draft/Open/Unmerged; no production integration or selector changes.

## 7. Status vocabulary
- PASS = independently evidenced and meets acceptance criteria.
- PARTIAL_PASS = some checks passed but required evidence is missing.
- BLOCKED = known dependency/tooling/data blocker prevents acceptance.
- UNKNOWN = insufficient evidence; never promote to PASS.
- NOT_DONE = not executed.


## 8. Update — bounded NSE date-shard support (2026-11-15)
- Added inclusive `--start-date YYYY-MM-DD --end-date YYYY-MM-DD` mode to `collector/nse_download.py`; default `--sessions 200 --lookback-days 500` behaviour remains when bounds are omitted.
- Added deterministic `iter_candidate_dates`: newest-first, inclusive, weekdays only; rejects one-sided and reversed ranges. Bounded mode scans the full date window; weekends are skipped, exchange holidays/missing source dates remain explicit misses.
- Bounded mode records start/end and per-date diagnostics, writes its own `sessions.txt`, does not enforce the default 200-session count, and fails if no valid sessions were acquired. Use a separate output directory per shard to prevent overwrites.
- Added five tests for inclusive range, newest-first order, single-day range, weekend-only range, reversed bounds, and one-sided bounds.
- Latest verified branch head: `cd7bc12946003f1ba7455363c42471199ca73b93`.
- GitHub Actions run #21 ID `43732684314`, job `132868428188`: SUCCESS; 22/22 date-integrity tests PASS (including 5 new shard iterator tests).
- On the same PR head, raw manifest test run #13 ID `43732684344`: SUCCESS; official-source probe run #12 ID `43732684305`: SUCCESS. These do not prove a 200-session archive.
- PR #37 remains Draft/Open/Unmerged. No full shard matrix, shard merge, or final 200-session raw artifact has been executed. Full raw archive acceptance remains BLOCKED / 0%.
- Next: add short per-shard Actions workflow with isolated output/artifacts, deterministic merge validator requiring exactly 200 unique session dates and no filename/content collisions, then independently inspect the final raw artifact. Final count must come from verified files, not inferred holidays.


## 2026-11-15 continuation — bounded NSE raw-acquisition shards

- Added inclusive ISO date-range options `--start-date YYYY-MM-DD --end-date YYYY-MM-DD` to `collector/nse_download.py`; existing default `--sessions/--lookback-days` mode remains in place. Bounded mode scans only the supplied date interval (weekends skipped), retains the existing Full Delivery → UDiFF → legacy source order and strict embedded-date checks, and writes `sessions.txt` plus acquisition diagnostics for that shard.
- Code update commit reported by GitHub contents API: `7c87a2c83eb64d492d3a5124c83878d080717b9d`; subsequent fetch reports the current collector file blob `084c475e05468c4fe962cdd93e7951cd8c93b019`. The contents API commit SHA and fetched blob SHA are distinct identifiers; do not confuse them.
- Added `tests/test_nse_bounded_shards.py` with four fail-fast CLI argument tests (missing bound, non-ISO date, reversed interval), commit `7b409fa01f0d5ea9aa7fd24b1eafa7114a6edfeb`.
- Updated `.github/workflows/nse_date_integrity_tests.yml` to run both existing date-integrity tests and the new bounded-shard tests, commit `5e11a11c9fcc85918a5958a0c9e6f36064568371`, workflow blob `a1ae13aebd32dd8879940456015cd39fcd319593`.
- CI status for these new tests: NOT_YET_VERIFIED. `fetch_commit_workflow_runs` for the workflow update commit returned no PR-triggered runs at check time. Do not claim tests passed until a run is observed.
- Scope still incomplete: no shard matrix workflow, no artifact merge/200-session exact-coverage manifest, and no final raw archive artifact. Bounded-shard implementation progress is partial; 200-session raw archive acceptance remains BLOCKED / 0% until the merged raw artifact contains exactly 200 unique sessions, source-date reconciliation, and per-file SHA-256 manifest.
- PR #37 remains Draft/Open/Unmerged; no production merge authorized. Existing production invariants remain unchanged.


### Follow-up verification on PR #37 head `0b15b8c6ad3224eb1487db41ae27a4c89732c18f`

- The earlier NOT_YET_VERIFIED status was superseded after the pull-request workflows completed.
- NSE Date Integrity Tests Run #26: run ID `43733064590`, job ID `132869599418`, SUCCESS; focused regression step completed successfully. This workflow now runs both `test_nse_date_integrity.py` and `test_nse_bounded_shards.py`.
- NSE Raw Archive Manifest Tests Run #17: run ID `43733064634`, job ID `132869582576`, SUCCESS.
- NSE Raw Manifest Official-Source Probe Run #16: run ID `43733064668`, job ID `132869582695`, SUCCESS; downloaded one real NSE Full Delivery file, verified source date and SHA-256 manifest, uploaded artifact ID `14168829295`, digest `sha256:8cf1f2819218895942d077128255b82580f199c59e8479dff9bc7e361a714c1c`.
- All three workflows completed SUCCESS on PR head `0b15b8c6ad3224eb1487db41ae27a4c89732c18f`. This verifies tests and a one-session live source probe only; it does not verify bounded shard collection over a multi-week range or the complete 200-session raw archive.
- PR #37 is still Draft/Open/Unmerged. Next engineering milestone remains: shard workflow with isolated output/artifacts, deterministic merge validator requiring exactly 200 unique session dates and no filename/content collisions, then independently inspect the final raw artifact. Final count must come from verified files, not inferred holidays.


## 2026-11-15 continuation — 20-shard archive acquisition and merge gate

- Added `scripts/research/merge_raw_archive_shards.py` (contents commit `14db63e619102c936765346e472441f46b45b9e6`, corrected implementation commit `a6f89844319705a6d7e8825d3cd6401562c6c88a`; current blob `a8702379a3b39136c4a72f9ae50f716bda223899`). It discovers isolated shard folders, validates exact ISO session list ↔ `sec_bhavdata_full_DDMMYYYY.csv` mapping, rejects duplicate dates/files, rejects unexpected/unlisted CSVs and wrong total count, copies original raw bytes without rewriting, writes combined sessions.txt, then invokes the existing SHA-256 + embedded-date manifest with `--expected-sessions`.
- Added `tests/test_merge_raw_archive_shards.py` with four tests: exact byte-preserving merge, duplicate date rejection, missing expected session rejection, and unlisted raw file rejection. File commit `b8ffd249f69d11e102b0bf25ac8bc5f50559aa7d`.
- Updated `.github/workflows/nse_date_integrity_tests.yml` to run merge tests and include the new tests/scripts in PR path filters. Commits `54412c02cca3c200a79f1160652e7d15354d2c66` and `a251ff052a76499a5673c89824aee9dd213e1492` added tests to CI; final PR trigger path fix commit `3837eb03189a13d400f40c23ae11823b80b24599`. Current workflow blob `55819aa750d8ce7e056b36d61f53a6eaa636b18c`.
- Added `.github/workflows/nse_200_session_raw_shards.yml`, commit `7960c9dab9608df1a1a52db7eae2fc75ca007487`, current blob `03a9064c94b3c7d2e7ba70bd0874e850bbc5ffa1`. It defines 20 non-overlapping calendar shards spanning 2026-02-09 through 2026-11-13, runs at most four collectors concurrently, sets each acquisition job timeout to 10 minutes, uploads isolated shard artifacts, and has a dependent merge job requiring exactly 200 unique sessions before final raw archive + manifest upload. The known processed archive date bounds are used as shard boundaries; final acceptance is based on actually acquired files, never inferred weekdays/holidays.
- PR #37 current head at this checkpoint: `3837eb03189a13d400f40c23ae11823b80b24599`; Draft=true, state=open, merged=false. The new PR-triggered shard workflow and focused tests have not yet been observed running at this checkpoint. Do not claim the 20 shards ran or that the final archive exists until Actions evidence/artifact is fetched.
- Important caution for follow-up: verify all 20 matrix shard jobs complete and upload artifacts; then merge job must report exactly 200 sessions and upload final artifact. If some shard fails due upstream NSE throttling/404 or the 10-minute limit, diagnose only failed shard windows and rerun those, not already successful tests or source probes. Current 200-session raw artifact acceptance remains BLOCKED pending real run and independent artifact inspection.


## 2026-11-15 continuation — first full shard execution result and corrective extension

- Workflow Run #2 ID `43733753079` on PR #37 executed all 20 configured shards. All 20 shard acquisition jobs completed SUCCESS and uploaded artifacts; dependent merge job failed closed. Merge log: `BLOCKER: expected exactly 200 unique sessions, found 188`.
- Downloaded and independently inspected all 20 shard artifacts. Their `sessions.txt` files contained exactly 188 unique dates; all 188 were included in the previous 200-date processed archive. The 12 missing processed dates were: `2026-03-03`, `2026-03-26`, `2026-03-31`, `2026-04-03`, `2026-04-14`, `2026-05-01`, `2026-05-28`, `2026-06-26`, `2026-09-14`, `2026-10-02`, `2026-10-20`, `2026-11-10`. Each date is recorded as `MISS` in its shard's `acquisition_diagnostics.json`; no official raw file was accepted by the strict Full Delivery → UDiFF → legacy validation chain for those dates. There were zero extra dates and no duplicates among the 188 acquired sessions.
- Artifact-by-artifact date counts: shard 01=10, 02=9, 03=10, 04=7, 05=9, 06=9, 07=10, 08=9, 09=10, 10=9, 11=10, 12=10, 13=10, 14=10, 15=10, 16=9, 17=9, 18=10, 19=9, 20=9; total 188. Shard 04's seven-session artifact was also downloaded and inspected separately.
- The 12 misses are not raw sessions; the processed aggregate's inclusion of these dates is not proof of official NSE raw trading files. Do not fabricate or backfill these dates. To obtain 200 genuine sessions, extend the raw acquisition range backwards and collect 12 earlier verified sessions.
- Corrective workflow change: added shard `00`, inclusive range `2026-01-21` through `2026-02-08`, intended to collect 12 earlier trading sessions; existing 20 shards retained. Merge workflow label updated to 21 artifacts. Commit `255b8d3c7f3d2d722afc6179fb4b8f63f7f91bb7`, workflow blob `d02c508bbf31f332774af31fa70d25ebf4d392a2`.
- New 21-shard rerun has not yet been observed at the time of this ledger update. Do not claim shard 00 or final 200-session merge passed. If shard 00 returns other than 12 valid files, use its actual sessions list and determine exact remaining gap; do not assume holidays or infer missing dates.
- Run #2 `43733753079` remains FAILED at the merge gate, despite 20/20 shard jobs SUCCESS. No final 200-session artifact was uploaded. Raw archive acceptance remains BLOCKED.


## 2026-11-15 — 200-session raw NSE archive independently verified PASS

- First 20-shard run #2 (`43733753079`) correctly failed closed at 188 sessions. Comparing the 188 raw session lists with the old processed 200-date aggregate exposed 12 dates with no official raw source accepted by strict validation. Rather than fabricate/forward-fill those dates, extended acquisition backwards.
- Added shard `00` for `2026-01-21`–`2026-02-08`; its official-source artifact contains exactly 12 valid dates: 2026-01-21, 01-22, 01-23, 01-27, 01-28, 01-29, 01-30, 02-02, 02-03, 02-04, 02-05, 02-06. 2026-01-26 correctly remains MISS. No holiday or missing date was fabricated.
- Corrected 21-shard workflow commit `ae97d497b7356bb0ee6bb7c593fb4adac9eb850c`; workflow blob `f144a28878556402a90f2372209f0a507ac62646`.
- Successful 21-shard run #4: run ID `43734398604`, final status SUCCESS. All 21 acquisition jobs SUCCESS; all 21 shard artifacts downloaded; merge gate SUCCESS; final raw archive and manifest uploaded. Run URL: `https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43734398604`.
- Companion validations on same corrected branch: NSE Date Integrity Tests run `43734398612` SUCCESS; Raw Archive Manifest Tests run `43734398613` SUCCESS; Official-Source Probe run `43734398609` SUCCESS.
- Final artifact: ID `14170166475`, name `nse-200-session-raw-archive-5`, size 26,279,303 bytes, GitHub digest `sha256:3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`. Download URL: `https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43734398604/artifacts/14170166475`.
- Downloaded final artifact and independently audited its ZIP contents locally: exactly 200 raw CSV files; `sessions.txt` has 200 unique dates; exact equality between session list and filename-derived dates; first session 2026-01-21, last 2026-11-13; manifest status PASS, 200 file records, 0 blockers; all 200 per-file SHA-256 values recomputed and matched the manifest; every EQ row in every CSV has a valid embedded date equal to the filename date; 500,733 EQ rows; 74,968,063 bytes of uncompressed raw CSV data; independent errors=0. GitHub artifact digest matches independently computed ZIP SHA-256.
- Local downloaded ZIP: `/mnt/data/nse-200-session-raw-archive-5.zip`; SHA-256 `3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`.
- Status: 200-session official raw archive + manifest acceptance = PASS / 100%. This closes the raw archive evidence gap only. It does not resolve Macro-Geo Step 4 / Factor Registry blockers or authorize production selector integration. PR #37 remains Draft/Open/Unmerged; do not merge without explicit authorization.


## 2026-11-15 — first 20-shard live run: 188/200 and targeted recovery

- Live run `43733753079` on PR #37 head `6fbff62e9e91c43ef0afd8fc6aa1945c823e544b`: all 20/20 acquisition jobs SUCCESS; all 20 shard artifacts downloaded successfully. Merge job `132872547023` FAILED closed with exact message `expected exactly 200 unique sessions, found 188`. No final archive artifact was uploaded.
- Independent inspection of downloaded shard ZIPs confirms 20/20 artifacts contain internally consistent `sessions.txt` and filename-date sets, no duplicate dates between shards, and 188 distinct dates total. The 20 windows start 2026-02-09, but the required 200-session archive begins 2026-01-21. This omitted earliest window contains 12 sessions, 2026-01-21 through 2026-02-06 (trading dates as listed by official source files). This is a matrix-boundary omission, not a reason to fabricate/backfill dates or relax the exact-200 gate.
- Artifact IDs/digests are preserved in the GitHub run. The shard artifacts are named `nse-raw-shard-01` through `nse-raw-shard-20`; run id `43733753079`. All were fetched and locally inspected; combined raw CSV file count=188, unique dates=188, per-shard `sessions.txt` exactly matches raw filename dates.
- Added targeted recovery workflow `.github/workflows/nse_raw_archive_recovery.yml`, commit `5dc3de5bc5e7a5d60478008bc2a56251ea76bd08`. It fetches only the missing 2026-01-21–2026-02-08 window in a <=10-minute job, uploads `nse-raw-shard-00-recovery`, downloads the 20 existing successful artifacts from run `43733753079` (not re-acquired), adds the recovery shard, then invokes the same byte-preserving merge and exact-200 SHA-256/embedded-date manifest gate. It uploads the final raw archive only on successful audit.
- Recovery workflow has been committed but its PR-triggered run and final artifact are NOT YET VERIFIED. Current raw archive acceptance remains BLOCKED. Next: inspect the recovery workflow run; verify recovered shard count=12 and all 200 raw files; confirm merge + manifest PASS; independently download final artifact, compare raw file count, session set, embedded dates, manifest hashes, and artifact digest. Do not rerun the original 20 successful acquisition shards unless evidence shows a defect.


## 2026-11-15 — Page 29 authoritative reconciliation and next-gate checkpoint

- Page label for the active continuation is **“গবেষণা যাচাই অব্যাহত 29”**. This is a continuation label only; it does not reset or replace prior pages or evidence.
- IMPORTANT CORRECTION: the first 20-shard run #2 / ID `43733753079` did fail closed at 188 sessions. That failure was already resolved by the subsequent 21-shard workflow run #4 / ID `43734398604`, commit `ae97d497b7356bb0ee6bb7c593fb4adac9eb850c`. Do not report the earlier 188-session failure as the current raw-archive status, and do not repeat the recovery.
- Verified run #4 jobs: all 21 acquisition shard jobs SUCCESS and merge job `132874642266` SUCCESS. The merge log confirms 21 artifacts downloaded, 21 artifact SHA-256 digests verified, `MERGED_SHARDS=21`, `UNIQUE_SESSIONS=200`, first session `2026-01-21`, last session `2026-11-13`. Independent manifest report in the merge log: `status=PASS`, `raw_file_count=200`, `sessions_listed=200`, `blockers=[]`.
- Final archive artifact: run `43734398604`, artifact ID `14170166475`, name `nse-200-session-raw-archive-5`, size 26,279,303 bytes, GitHub SHA-256 `3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`, expiry 2027-02-13T16:14:57Z. URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43734398604/artifacts/14170166475 .
- Companion tests: NSE Date Integrity run `43734398612` SUCCESS (job `132873685552`); Raw Archive Manifest Tests run `43734398613` SUCCESS (job `132873684932`); official-source probe run `43734398609` previously recorded SUCCESS. Prior local independent artifact audit is recorded above: 200 raw CSVs, 200 unique session dates, filename/session-list equality, embedded EQ date equality, 200 manifest hashes recomputed and matched, 500,733 EQ rows, zero independent errors. Do not repeat artifact download/audit unless a specific integrity concern arises.
- Clarification of the earlier 188/200 narrative: the 188-session run was an incomplete 20-shard window. The successful recovery added shard 00 for 2026-01-21–2026-02-08 and contributed the 12 earlier verified trading sessions. Do not mislabel all individual `MISS` log lines from weekday candidate scanning as 12 required missing trading dates; the actual accepted recovery sessions are the 12 dates listed in the preceding archive section. Strict embedded-date validation remains unchanged.
- Raw NSE 200-session archive acceptance: **PASS / 100% for this scoped work package**. This does not close Macro-Geo Step 4, Factor Registry, full V11.3 backtest, 672 semantic coverage, or final project acceptance.
- Cost-aware V11.3 research replay unit-test CI: Run #7 / ID `43696699661`, job `132758733905`, SUCCESS. Log confirms 10 tests run, all 10 passed, including cost-once, duplicate-key fail-closed, stop-gap, invalid cost/target/horizon, missing symbol session, horizon-close exit, same-bar stop-first, unmatured horizon and invalid/zero-volume OHLC. This is unit-test acceptance only; no historical replay has been run.
- Backtest module on main has blob SHA `32b556717dab70d0b37de69a6e3d98105edd1702`. Its required inputs are a verified OHLC CSV with columns `SYMBOL,DATE,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,TTL_TRD_QNTY` and a signal CSV with `CUT_OFF,SYMBOL`. The research replay consumes next global trading-session OPEN, intraday HIGH target touch, -3% stop, stop-first same-bar ambiguity and a one-time 0.22 percentage-point round-trip cost deduction. Slippage is not modelled. The input signal file lineage still needs approval/validation: do not assume V11.4 walk-forward top-30 signals are approved V11.3 production-selector signals. Do not claim replay metrics before an actual run and independent audit.
- Next highest-value task: perform a bounded input-lineage and schema audit for the exact OHLC and signal inputs, including session coverage, duplicate keys, cutoff leakage, signal-generation engine/version, and whether the approved V11.3 selector output can be sourced without modifying protected production logic. Then run the full research replay only when those inputs are proven compatible. No synthetic signals or guessed data paths.
- Scoped progress: raw archive acceptance 100% PASS; cost-aware replay unit-test gate 100% PASS; historical replay 0% NOT_STARTED; independent replay reconciliation 0% NOT_STARTED; project-wide percentage NOT_CALCULABLE.
- Preserve PR #37 Draft/Open/Unmerged and no merge authorization. No production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), engines A–E, or production workflow changes. No paid APIs/spend; no repeated collector acquisition.


## 2026-11-15 — Page 29: V11.3 historical signal input-lineage audit

- New audit document: `docs/V11_3_HISTORICAL_SIGNAL_INPUT_LINEAGE_AUDIT_20261115.md`, commit `0b0bbdcb925bcba845e9df2c710039857c98781c`. This is a research-only audit; no production changes.
- Inspected `pipeline/v11_3_abcd_e.py` (blob `34ad08f130254a0e8c5f09ae5a0e2d93590757df`): it reads the 200-session processed OHLC dataset, calculates current features, and emits only each symbol's latest row (`g.iloc[-1]`) to current candidates/top30. It does not create a historical per-cutoff `CUT_OFF,SYMBOL` signal ledger.
- Inspected `pipeline/walk_forward_backtest.py` (blob `d085f7a2d35a88b4c4eaba65144a429a06961b09`): explicitly V11.4. Its `add_tomorrow_features` function body uses same-row causal features, but its `behavioral_dna_library.json` is generated from future outcome fields FUT1/FUT3/FUT5. The V11.3 candidate script optionally consumes `hit10_h3` rates from that full-sample library in its calibration score. Reusing that full-sample library at earlier historical cutoffs would leak future outcomes.
- Therefore V11.4 `walk_forward_predictions.csv` is not accepted as a silent substitute for V11.3 selector signals. No compatible archived V11.3 historical `CUT_OFF,SYMBOL` signal ledger has been identified.
- Decision: full historical cost-aware replay remains BLOCKED / NOT_READY pending a genuine archived V11.3 signal ledger or a separately specified cutoff-safe research adapter. Any adapter must evaluate only information available at each cutoff and define an explicit minimum-sample/fail-closed calibration rule; do not invent a fallback or change production scoring. Protected selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and engines A–E remain unchanged.
- Scoped progress: V11.3 source/input lineage diagnosis 100%; compatible historical signal ledger 0% / NOT_FOUND; cutoff-safe signal adapter specification 0% / NOT_STARTED; historical replay 0% / NOT_STARTED; independent replay reconciliation 0% / NOT_STARTED. Raw archive remains 100% PASS; replay unit-test gate remains 100% PASS; overall project percentage NOT_CALCULABLE.
