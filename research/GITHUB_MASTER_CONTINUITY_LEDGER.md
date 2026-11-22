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

## C252 — Run #386 hard-gate failure analysis
Run #386 ID `44994024718`, head `e81aeb913f426917f27f602da926c1f56201478a`, job `137121090511`, artifact `14743653729`, SHA-256 `20e83e668e7d089bf915b74bfc31cd47853ec77171c9d34cda52fb65aa5c690a`. Workflow FAILURE is solely strict hard-gate step 16; collection, repair, audit, four-group validation, event study script and upload steps succeeded. Hard gate: 7/8 P0 groups, missing usd_inr; 0 matured event windows; blockers EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS and P0_SOURCE_COVERAGE_INCOMPLETE; candidate_release_allowed=false. Production selector, ranking score, pressure fade unchanged.
Artifact verified: EIA official Brent repair 212 rows (2026-01-19..2026-11-17); USD/INR FRED timed out and direct FBIL historical endpoint not yet verified; NSE FPI/DII snapshot only 1 date and fails >=60 dates/90-day gate; separate NSDL official archive reports FPI 119 dates/172 days and DII 102 dates/150 days with 7 DII schema misses. Event study 21 publisher-feed mentions; 20 pending events dated 2026-11-21/22 after panel latest close 2026-11-20; one eligible event had no valid pre/post close window; zero windows. Publication-time proxies are not event-occurrence times. Do not loosen gates or fabricate event windows.
Official-source discovery: RBI release confirms FBIL assumed reference-rate dissemination from 2018-07-10; FBIL official site publishes INR/1 USD rates; RBI Table 223 page currently surfaced only through 2026-04-21 and is not accepted as complete Nov-2026 coverage. Links and full evidence in `research/MACRO_GEO_HARD_GATE_FAILURE_ANALYSIS_CONTINUATION252_2026-11-22.md`.
Next: inspect official FBIL frontend/download/API contract; only implement a fully evidenced official historical collector with provenance and tests; otherwise keep USD/INR BLOCKED. Backfill source-linked historical media publications, retain publication-time semantics, wait for post-publication market closes before event windows. C252 report commit: `65afc86cc5873d94f08c73c4f2565192712c90ac`.

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


### C253 — FBIL official USD/INR endpoint verification
Report: `research/FBIL_OFFICIAL_USDINR_ENDPOINT_VERIFICATION_CONTINUATION253_2026-11-22.md`
Report commit: `5a5adad6cf75fe2eebb129907406f3ced1d12039`.
Re-read C252 and verified latest audit-branch Actions: Run #387 / ID `44994024678` cancelled; same-head hard-gate run ID `44994024718` failed as documented in C252. No new PASS supersedes it.
Official RBI source confirms FBIL took over USD/INR reference-rate computation/dissemination from 2018-07-10; FBIL methodology confirms transaction-based rate construction. FBIL homepage is not text-readable through the available inspection path; public search snippets show daily rates but no verified public historical API/download contract, schema, date-range parameters, or complete machine-readable coverage through 2026-11-20.
Decision: USD/INR remains BLOCKED; no code change, guessed endpoint, community mirror, paid API, or gate relaxation. FBIL ownership/methodology VERIFIED; machine-readable archive UNKNOWN/NOT VERIFIED.
Excluded: RBI pre-2018 archive, partial RBI Table 223 coverage, search snippets as endpoint proof, third-party mirrors and paid/keyed APIs.
Next: (1) inspect official FBIL user-facing navigation/assets for a real downloadable archive and validate host/schema/coverage; (2) if unavailable, retain BLOCKED; (3) separately inspect existing official NSDL FPI/DII archive evidence from Run #386 without conflating it with the one-date NSE snapshot; (4) continue timestamp-grounded event publication backfill and matured-window gating.
Invariants unchanged. PASS work skipped.

### C254 — NSDL FPI/DII date-window integrity repair
Report: `research/NSDL_FPI_DII_DATE_WINDOW_INTEGRITY_REPAIR_CONTINUATION254_2026-11-22.md`
Report commit: `02a62d56d31854b48c3bd2c37691b00a18781023`.
Re-read C253 and fetched Run #386 artifact `14743653729` (SHA-256 `20e83e668e7d089bf915b74bfc31cd47853ec77171c9d34cda52fb65aa5c690a`). Independent CSV audit found 119 FPI dates in the file, but 16 dates (2026-06-01..2026-06-22) were outside the collector's declared 2026-06-23..2026-11-20 window because month-end FPI queries returned the whole month. Within the declared window: FPI 103 dates, DII 102 dates, zero duplicate DATE/GROUP keys, one DII missing FPI archive date (2026-07-17), 99.03% date alignment. Seven DII schema failures were logged; six dates were not in the FPI archive date set. These six are not labelled holidays absent independent calendar evidence.
Code commit `77ffe26afcc9afd3ede9fab0aea07816868abb6c`: added date-window clipping and an explicit FPI-vs-DII archive-date coverage audit; no imputation and no change to 60-date/90-day threshold. Test commit `71e7102acd3e647263e29b5f806e596e048096b8`: added three regression tests for clipping, exact missing-date reporting, and complete alignment.
CI at report time: Run #388 ID `44998007760` IN_PROGRESS; Run #389 ID `44998017821` PENDING. Code and tests are COMMITTED, but CI verification is PENDING, not PASS. NSDL flow availability under the existing threshold is not complete date alignment. NET_VALUE units still require source-table confirmation. USD/INR and overall Macro-Geo hard gate remain BLOCKED.
Next: inspect both CI runs; verify new artifact's date range; investigate only the 2026-07-17 DII missing date using official NSDL evidence; confirm official NSDL units/field semantics before financial interpretation. Invariants unchanged.
### C255 — NSDL flow CI and unit semantics verification
Report: `research/NSDL_FLOW_CI_AND_UNIT_SEMANTICS_VERIFICATION_CONTINUATION255_2026-11-22.md`
Report commit: `3419cac341f3f82e0e12dddaa3164eaa371110c3`.
Re-read C254 and checked CI: Run #388 / ID `44998007760`, job `137133127591`, steps 1–14 completed successfully, corrected-label walk-forward step 15 still IN_PROGRESS, remaining steps pending. Run #389 / ID `44998017821` remained PENDING with no job available. No code changes were made while Run #388 was active.
Official NSDL DII report page (https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L) explicitly separates `Net Investment (Rs. Crore)` from `Net Investment US ($) million` and includes USD/INR conversion. The collector's `net investment` column matching with USD/million exclusions is consistent with INR crore on pages carrying those exact headers, but row-level mapping across all historical pages remains NOT VERIFIED. The page also distinguishes provisional T-day exchange data from confirmed custodian/depository reports for prior trading days; downstream interpretation must retain this distinction.
Exact 2026-07-17 DII page schema remains uninspected. No assumption that the missing date was a holiday; no synthetic data. C254 date-window repair remains CODED/CI PENDING; test run pending. USD/INR and overall Macro-Geo P0 gate remain BLOCKED.
Next: inspect Runs #388/#389 and resulting artifact; inspect official NSDL 2026-07-17 page; assert parser schema only from actual HTML evidence; verify output window and preserve missing dates; no gate relaxation. Invariants unchanged.

### C256 — NSDL archive date lookup and CI continuity
Report: `research/NSDL_ARCHIVE_DATE_LOOKUP_AND_CI_CONTINUITY_CONTINUATION256_2026-11-22.md`
Report commit: `16dae3e1781bb5b3c9b495fc76007639c26358eb`.
Re-fetched ledger and C255 report before work. C254 implementation was not repeated.
CI: Run #388 / ID `44998007760` cancelled after step 15; regression step 5 and corrected-label walk-forward step 15 SUCCESS, but collection step 16 cancelled and later steps skipped. Run #389 / ID `44998017821` remains IN_PROGRESS; step 5 SUCCESS, step 6 NSE history acquisition IN_PROGRESS. Run #315 / ID `44998007758` remains IN_PROGRESS; steps 5–7 SUCCESS, step 8 P0 market/media collection IN_PROGRESS. No code edits during active runs.
Official NSDL reports listing exposes “Archive DII”, which resolves to the official date-input form `https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A`. The form shows “Please Select Date” / “No Data Found” without a submitted date; public inspection did not reveal the POST contract or exact 2026-07-17 response. Therefore that row/schema remains NOT VERIFIED. No inferred holiday, guessed POST route, synthetic row, or parser change.
Official live DII page continues to show separate INR-crore and USD-million columns and provisional T-day versus confirmed previous-day semantics; this remains page-level, not row-level proof.
Statuses: C254 clipping CODED; regression step SUCCESS; fresh artifact window validation PENDING. 2026-07-17 row/parser mapping UNKNOWN. USD/INR and Macro-Geo P0 release gate BLOCKED. Production branch/invariants unchanged.
Next: (1) inspect #389/#315 completion and artifacts; (2) verify all FPI dates clipped to 2026-06-23..2026-11-20; (3) preserve exact 2026-07-17 DII gap unless official row is retrieved; (4) inspect official form HTML/JS for an evidenced date-submit contract before implementing anything; (5) keep all hard gates strict.


### C257 — prospective audit artifact review
Report: `research/PROSPECTIVE_AUDIT_ARTIFACT_REVIEW_CONTINUATION257_2026-11-22.md`
Report commit: `b5609ccecbf5943514a8ea060e35658f703be469`.
Re-fetched ledger, C256 and C255 reports; no prior PASS work repeated.
Run #389 / ID `44998017821`, head `71e7102acd3e647263e29b5f806e596e048096b8`, conclusion CANCELLED. Steps 1–15 SUCCESS (including C254 tests step 5 and corrected-label walk-forward step 15); step 16 P0 collection cancelled; steps 17–33 skipped; artifact upload step 34 SUCCESS.
Artifact `prospective-watchlist-audit`, ID `14744698608`, 31,122,264 bytes; GitHub digest and independently computed ZIP SHA-256 both `5abaa9ca0110848f1181297db69b5774ced282b39f2cd045fa67993ceeb4ad6d`. Artifact confirms 200/200 provenanced NSE sessions (2026-02-16..2026-11-20), manifest validation PASS, dataset QA PASS, 2,999 symbols and 100% delivery coverage.
Walk-forward artifact: 100 sessions, 3,000 candidates, Top-30. Precision/lift: T5_H1 32.43%/3.54x; T10_H3 22.03%/3.23x; T15_H5 14.10%/2.89x; T20_H5 6.96%/3.17x. Recall 4.08%, 3.62%, 3.19%, 3.49%. Full-universe winner mean probability 0.086886 is slightly below nonwinner 0.087184; median separation is also weak. Investigate probability discrimination and target-label joins before interpreting calibration. No T2_H1 result and no cost-aware profitability evidence; no net-return claim.
Artifact contains no NSDL/FPI/DII/flow files, so it does not verify C254's FPI date clipping or 2026-07-17 DII gap. C254 stays CODED; test step SUCCESS; real NSDL output verification PENDING.
Run #315 / ID `44998007758` remains IN_PROGRESS; P0 market/media steps 8 and corporate disclosure step 9 SUCCESS; step 10 bounded repair IN_PROGRESS; no artifact yet. USD/INR and Macro-Geo hard gate remain BLOCKED/UNVERIFIED.
Next: investigate probability score vs winner separation without modifying production selector/ranking; secure an audit run with actual NSDL flow artifact; inspect #315 final source evidence and strict gate; no inferred +2% or profitability data. All protected invariants unchanged.


### C258 — Macro-Geo CI artifact and NSDL date-window evidence
Report: `research/MACRO_GEO_NSdl_CI_ARTIFACT_EVIDENCE_CONTINUATION258_2026-11-22.md`
Report commit: `6a3d1b89aa285466f14e6ec46d698bd7b9a1f31e`.
Re-fetched Master Ledger, C257, C256 and C255 before work. Run #315 / ID `44998007758` completed FAILURE at strict hard-gate step 16; steps 5–15 and 17 succeeded; step 18 skipped; step 19 artifact upload succeeded. This is fail-closed acceptance, not runtime exception.
Artifact `macro-geo-p0-event-study`, ID `14745631182`, 4,909,744 bytes; ZIP SHA-256 `d0f5dae577a6165b3721b0453efdc4af54b7ad5aeabc5a2128d242edf9cad029`, matching GitHub digest.
C254 clipping end-to-end verified in artifact `data/external/fpi_dii_flows.csv`: 205 rows, FPI 103 dates, DII 102 dates, range 2026-06-23..2026-11-20, 103 distinct dates, zero out-of-window rows, zero duplicate DATE/GROUP keys. DII missing on 2026-07-17 while FPI exists. Collection JSON reports 99.03% DII coverage vs official FPI archive dates and 150-day span. Seven DII archive date queries lacked Equity/Stock Exchange net-investment table: 2026-06-26, 2026-07-17, 2026-08-26, 2026-09-14, 2026-10-02, 2026-10-20, 2026-11-10. These are schema/table misses, not proven holidays. Unit mapping across historical pages remains NOT VERIFIED.
Hard gate BLOCKED: P0 7/8, missing usd_inr; event study 21 publisher mentions, 1 eligible, 20 pending, 0 windows; panel latest 2026-11-20; blockers EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS and P0_SOURCE_COVERAGE_INCOMPLETE; candidate_release_allowed=false. Production selector/ranking/pressure fade unchanged.
EIA Brent official 212 rows AVAILABLE. USD/INR BLOCKED due FRED timeout and no verified direct official RBI/FBIL endpoint. Corporate events 164,377 rows / 2,471 symbols AVAILABLE. Separate NSE FPI/DII snapshot remains 2 rows/1 date and BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE; do not confuse with NSDL archive flows.
Four-group validation PASS is schema/provenance only: benchmark 207, sector 1,863, volatility 426, geopolitical publisher mentions 21; occurrence independently unverified. Factor registry: 35 groups, 0 fully available, 19 partial, 16 not connected. Event windows CSV empty. Historical regime: 11 provisional anchors, 0 regimes with windows.
Next: inspect seven DII official raw HTML/table variants and units; no parser change absent direct evidence. Continue FBIL/RBI official USDINR endpoint research; maintain BLOCKED if no free official machine-readable contract. Keep event publication timestamps distinct from event occurrence and wait for mature closes. Re-run hard gate only after evidence changes. C254 clipping PASS scoped to observed output, not complete DII coverage.
All protected invariants and production branch unchanged; no gate relaxation.


### C259 — NSDL DII holiday root-cause classification and bounded repair
Report: `research/NSDL_DII_HOLIDAY_ROOT_CAUSE_AND_REMAINING_GAP_CONTINUATION259_2026-11-22.md`
Report commit: `53c7135776ceef703f82a6e93b18c1a6539dbd11`.
Re-fetched the Master Continuity Ledger, C258 report, collector and tests. Re-inspected Run #315 artifact `14745631182`. Six of the seven prior DII “schema not recognized” dates are official 2026 NSE Capital Market holidays per NSE circular NSE/CMTR/71775 dated 2025-12-12: 2026-06-26 Muharram; 2026-08-26 Id-E-Milad; 2026-09-14 Ganesh Chaturthi; 2026-10-02 Mahatma Gandhi Jayanti; 2026-10-20 Dussehra; 2026-11-10 Diwali-Balipratipada. Official circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf. The seventh date, 2026-07-17, is not listed and remains unresolved; no holiday inference or row imputation.
Bounded repair committed: collector skips only those six official 2026 holidays, records date/name/source under non_trading_holidays, and leaves 2026-07-17 for actual retrieval/schema diagnosis. Regression test asserts the six names and asserts July 17 is not a holiday. Code commit `91caabc9b11e8cd22d592f50f1121a99b3859c3a`; test commit `82c0e6fe31ec9b19529f35e934b807880089f694`.
At report time CI pending/in progress: Run #390 ID `45000517346`, Run #391 ID `45000520528`, Macro-Geo Run #316 ID `45000517341`. CODED/TEST-COMMITTED, not yet CI PASS. Prior C258 archive remains 102 DII dates vs 103 FPI dates (99.03%); C254 clipping PASS remains unchanged. USD/INR and event windows remain BLOCKED; no production invariant changed.
Next: inspect all three runs and fresh artifact; verify holiday skip metadata and July 17 gap; only repair July 17 if official source evidence proves the schema; retain strict P0 gate. PASS work skipped.


### C260 — correction of NSE Capital Market vs Debt Segment holiday classification
C259 contained an overbroad holiday classification. Re-read the actual official circulars: Capital Market circular NSE/CMTR/71775 lists five of the seven DII error dates (2026-06-26, 2026-09-14, 2026-10-02, 2026-10-20, 2026-11-10). It does NOT list 2026-08-26. That date appears in separate Debt Segment circular NSE/DS/71968 and must not be used to skip an equity/Capital Market DII request. 2026-07-17 also remains absent from the Capital Market holiday list. Official links: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf and https://nsearchives.nseindia.com/content/circulars/DS71968.pdf.
Corrected collector removes 2026-08-26 from NSE_TRADING_HOLIDAYS_2026; corrected regression test asserts 2026-08-26 is not a Capital Market holiday. Code correction commit `885528a076e98996455358ee236f1a2960a276ea`; test correction commit `9fac7d42bd09f6b0a4d9a4c0742a36451816e0a4`. C259 report correction addendum commit `661f74b9b0b3a7734c1d8fac2e0e9874f5d0fc22`.
Runs #390 and #316 still execute on pre-correction C259 SHA and cannot validate this correction. A new corrected-SHA run is required. Five dates are confirmed Capital Market holidays; Aug 26 and Jul 17 remain NSDL query/evidence items, not assumed data/no-data. No production selector invariant changed. Next: verify corrected files, wait/inspect old runs as historical-only, launch/verify CI on corrected commit, then inspect new artifact for holiday metadata and actual NSDL outcomes. USDINR/event windows remain blocked.


### C261 — NSDL DII 2026-07-17 official-source triage and corrected CI queue
Report: `research/NSDL_DII_20260717_OFFICIAL_SOURCE_TRIAGE_AND_CI_QUEUE_CONTINUATION261_2026-11-22.md`; report commit `ee902a190fd50c247484a9d9cf9993dea4e18786`.
Re-fetched the Ledger, C259 report, collector and tests; did not repeat C254 clipping PASS. Official NSE CM trading circular NSE/CMTR/71775 does not list 2026-07-17 or 2026-08-26. Separate Capital Market SETTLEMENT holiday circular NCL/CMPT/71904 lists 2026-08-26, but that is not a trading holiday; Debt Segment circular NCL/DS/71918 is also not the CM trading calendar. Official links: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf ; https://nsearchives.nseindia.com/content/circulars/CMPT71904.pdf ; https://nsearchives.nseindia.com/content/circulars/DS71918.pdf.
NSDL official DII date form renders “Please Select Date” / “No Data Found” when no date is submitted; exact 2026-07-17 date-submitted response not available in public indexed evidence. Official latest DII report example explains provisional T-day exchange data versus confirmed custodian/depository data for previous trading day(s), and separate INR crore/USD million fields; this does not prove July 17 row existence. Links: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A and https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L. Thus July 17 remains UNKNOWN/BLOCKED; no zero-flow/holiday inference. Aug 26 remains a date to query; do not skip it on settlement-holiday evidence.
Corrected code/test commits remain `885528a076e98996455358ee236f1a2960a276ea` and `9fac7d42bd09f6b0a4d9a4c0742a36451816e0a4`. Runs #392 CANCELLED, #393 PENDING, #317 PENDING; #390/#316 are still on superseded SHA. No corrected CI PASS or artifact acceptance yet. No production invariants changed.
Next: inspect #393/#317 when jobs appear; launch/inspect corrected full Macro-Geo run after active jobs finish; validate Aug 26 and July 17 actual NSDL query outcomes; preserve UNKNOWN if source response unavailable; maintain USDINR/event-window blockers.


C261 report-path correction: the report was successfully created at `research/NSDL_DII_20260717_OFFICIAL_SOURCE_TRIAGE_AND_CI_QUEUE_CONTINUATION261_2026-11-22.md` with actual create commit `74a76fe5cfb0fee39c331e17549d87c943241720`. Use this actual commit, superseding the earlier provisional commit reference in the C261 entry.
