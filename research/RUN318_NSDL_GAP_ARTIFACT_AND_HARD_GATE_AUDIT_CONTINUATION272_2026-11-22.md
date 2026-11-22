# Run #318 NSDL Gap Artifact and Strict Hard-Gate Audit — C272

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Continuity check
Re-fetched the current Master Ledger and C271/C270/C269 reports before work. PASS archive QA and manifest work were not repeated. Run #318 was completed and its artifact inspected. No change to production selector invariants.

## Run #318 final status
- Run ID `45014759390`, run #318, head `399b0a61535f84bfbee8347321e51c590ff9ff55`.
- Conclusion: FAILURE, updated `2026-11-22T11:20:23Z`.
- Steps 1–15 SUCCESS, including NSDL collection, source coverage, factor audit and event-study operation.
- Step 16 strict Macro-Geo hard gate FAILURE (fail-closed).
- Step 17 historical regime study operationally SUCCESS but research BLOCKED.
- Step 18 sector rotation features SKIPPED.
- Step 19 artifact upload SUCCESS.
- Artifact `macro-geo-p0-event-study`, ID `14752530805`, size 4,909,190 bytes.
- Downloaded ZIP independently SHA-256: `a8fc05c8cb0a4782dc6e0546a3587a22bcae8ca4e742d761865e7316edf118c8`, exactly matching GitHub artifact digest.

## NSDL evidence — scoped operational PASS, research remains gapped
Artifact `outputs/macro_geo/nsdl_fpi_dii_collection.json`:
- Status: `AVAILABLE_WITH_GAPS`.
- Window 2026-06-23 through 2026-11-20.
- FPI: 103 rows / 103 unique dates / 150-day span.
- DII: 102 rows / 102 unique dates / 150-day span.
- Exact DII attempts: 104; successes 102; failures 2.
- Failed dates: 2026-07-17 and 2026-08-26; both return “no Equity/Stock Exchange net-investment table / schema not recognized”.
- FPI-date alignment: 99.03%; this is not the total DII query-success rate and does not resolve Aug 26 because FPI has no row for that date.
- Five NSE holidays separately recorded with official circular URL; not counted as missing flow dates.
- This is a scoped operational collection PASS with explicit gaps, not complete NSDL coverage. The two failed dates remain UNKNOWN; do not treat as zero flow or holiday.

## Strict gate and event study
Artifact `outputs/macro_geo/hard_gate_report.json`:
- `status=BLOCKED`; P0 available groups 7/8.
- Missing P0 group: `usd_inr`.
- Event study BLOCKED; one eligible event, zero windows; market/equity panels end 2026-11-20.
- Blockers: `EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS`, `P0_SOURCE_COVERAGE_INCOMPLETE`.
- `candidate_release_allowed=false`.
- Production selector, ranking score and pressure fade unchanged.

Artifact `event_study_report.json`: 16 event mentions, 1 eligible, 15 pending, 0 windows; no valid pre/post publication close window. Operational status PASS_WITH_RESEARCH_BLOCKED. No synthetic returns.
Historical regime study: 11 provisional date anchors, 0 matched windows; status BLOCKED_NO_MATCHING_REGIMES. Operational execution success is not research acceptance.
Four-group validation reports PASS for benchmark indices (207 rows), sector indices (1,863), volatility (426) and geopolitical publisher mentions (16); event occurrence remains independently unverified.

## NSDL CI regression wiring
After Run #318 completed, updated `.github/workflows/macro_geo_p0_event_study.yml` to explicitly include `qa.test_macro_geo_nsdl_flows` in the existing unittest command.
- Workflow commit: `9d3535d62e54a4ad2edc3f7d6d7975f7ace37c6b`.
- Re-fetched workflow blob: `b7a2b950a750e42b7ed9897688effbb2ac7fb380`.
- Exact command now: `python -m unittest qa.test_macro_geo_engine qa.test_macro_geo_repair_p0 qa.test_macro_geo_nsdl_flows -v`.
- Push triggered Macro-Geo run #319 / ID `45017190489`, head equals workflow commit. At latest poll it is IN_PROGRESS, updated `2026-11-22T11:24:48Z`; initial regression step (event-study timestamp and data-quality tests) SUCCESS, NSE 200-session acquisition step IN_PROGRESS. The new NSDL test suite has not yet been reported by a completed test step; do not claim CI PASS until run #319 completes and logs/steps show it.
- No duplicate run dispatched. Run #319 is now the active workflow.

## Rejected / guardrails
- Rejected marking NSDL fully AVAILABLE; exact failed query log remains explicit.
- Rejected treating 99.03% FPI alignment as 100% DII query success.
- Rejected inferring 2026-07-17 / 2026-08-26 flows or relabeling them holidays.
- Rejected treating four-group PASS as overall Macro-Geo PASS.
- Rejected treating event/regime operational execution as research acceptance.
- USD/INR remains BLOCKED; monthly FBIL averages are not daily values.
- No paid APIs, synthetic data, third-party flow mirrors, invented event windows or gate relaxation.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.

## Exact next actions
1. Poll run #319; confirm the updated regression command executes `qa.test_macro_geo_nsdl_flows` and all tests pass; verify the final workflow result and artifact digest.
2. Investigate the two official NSDL failed-date responses using documented official page evidence only; do not guess POST fields or switch hosts without proof.
3. Continue free official FBIL daily USD/INR historical endpoint investigation; retain BLOCKED absent a verified complete daily schema.
4. Wait for genuine post-publication NSE closes before event study; re-run strict gate only after USD/INR and event-window evidence changes.
5. In the audit-only walk-forward output, add per-state/per-target matured denominators and >=50 eligibility labels; do not infer state calibration from total rows.
