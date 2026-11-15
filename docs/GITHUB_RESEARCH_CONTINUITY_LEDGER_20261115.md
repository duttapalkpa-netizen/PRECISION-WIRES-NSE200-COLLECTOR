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
