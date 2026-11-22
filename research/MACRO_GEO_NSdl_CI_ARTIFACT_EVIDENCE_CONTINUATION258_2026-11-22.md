# Macro-Geo CI Artifact Evidence — Continuation 258

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## 1. Continuity and source checks
Re-fetched `research/GITHUB_MASTER_CONTINUITY_LEDGER.md` (blob `14da53d6588faa1315a768859c003e4c10000b1a`), C257 `research/PROSPECTIVE_AUDIT_ARTIFACT_REVIEW_CONTINUATION257_2026-11-22.md` (blob `ea63bb9a278ae30297b59b87f5691818587a0599`), C256 (blob `d30ee2b4d64e8d7d26209fd08442124f0f7439f3`) and C255 (blob `7c70f2cc215df850640b00baf31f207bbed59af9`). No previously PASS work repeated.

## 2. Run #315 completed; strict gate failed as designed
- Run ID `44998007758`, head `77ffe26afcc9afd3ede9fab0aea07816868abb6c`; conclusion FAILURE.
- Steps 5–15 succeeded, including official NSDL flow collection, source audit, four-group schema/provenance validation and publication-time event-study execution.
- Step 16 strict Macro-Geo hard gate FAILED (exit code 1); this is an intentional fail-closed acceptance result, not a runtime exception.
- Steps 17 historical regime/sector study completed with research status BLOCKED; step 18 sector rotation feature build skipped; step 19 artifact upload succeeded.
- Artifact `macro-geo-p0-event-study`, ID `14745631182`, 4,909,744 bytes; GitHub digest and independently computed ZIP SHA-256 both `d0f5dae577a6165b3721b0453efdc4af54b7ad5aeabc5a2128d242edf9cad029`.

## 3. C254 NSDL date-window repair — artifact verified
Artifact file `data/external/fpi_dii_flows.csv`:
- 205 rows: FPI 103 dates; DII 102 dates.
- Date range exactly 2026-06-23 through 2026-11-20; 103 distinct dates; zero rows outside declared window.
- Zero duplicate (DATE,GROUP) keys.
- 2026-07-17 has an FPI row but no DII row. Do not infer holiday or fill the missing DII row.
- `nsdl_fpi_dii_collection.json` independently reports 103 FPI dates, 102 DII dates, 150 calendar-day span, 99.03% DII coverage versus observed official FPI archive dates, and missing DII date 2026-07-17.
- Seven DII dates were not parsed because the collector found no Equity/Stock Exchange net-investment table: 2026-06-26, 2026-07-17, 2026-08-26, 2026-09-14, 2026-10-02, 2026-10-20, 2026-11-10. This is a schema/table availability diagnostic, not proof of market holidays.
- Thus C254 clipping has end-to-end artifact evidence: date clipping WORKING for this run. The 2026-07-17 gap and six other schema gaps remain unresolved. Row-level unit interpretation across these archive pages remains NOT VERIFIED; preserve source timing semantics.

## 4. Macro-Geo hard gate and evidence
`outputs/macro_geo/hard_gate_report.json`:
- status BLOCKED; P0 groups 7/8; only missing P0 group is `usd_inr`.
- Event study: 21 publisher mentions; 1 eligible; 20 pending; 0 event windows.
- Market/equity panel latest date 2026-11-20.
- blockers: `EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS`, `P0_SOURCE_COVERAGE_INCOMPLETE`.
- `candidate_release_allowed=false`; production_selector_changed=false; ranking_score_changed=false; pressure_fade_changed=false.
`p0_repair_report.json`:
- Brent: AVAILABLE, 212 rows, official EIA RBRTE XLS, 2026-01-19..2026-11-17.
- USD/INR: BLOCKED, FRED DEXINUS timeout; no verified direct official RBI/FBIL endpoint configured; community mirror disabled.
- Corporate events: AVAILABLE, 164,377 rows / 2,471 symbols from official NSE API.
- NSE FPI/DII snapshot: BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE (2 rows, one date); keep distinct from the separate official NSDL archive dataset above.
`four_group_validation.json` PASS covers schema/row/date/provenance checks only: benchmark 207 rows, sector indices 1,863, volatility 426, geopolitical publisher mentions 21. Geopolitical records are publisher/RSS/GDELT mentions; occurrence independently unverified.
`factor_coverage_audit.json`: 35 groups; 0 fully available schema groups; 19 partial; 16 not connected.
Event study has zero windows; `event_study_windows.csv` is empty. Twenty post-panel publisher mentions remain pending; the single eligible mention did not produce a valid pre/post close window.
Historical regime study: 11 provisional anchors, zero regimes with windows; no historical sector-relative inference or factor integration.

## 5. Status / exclusions
- C254 date clipping: CODED + END-TO-END OUTPUT VALIDATED for Run #315; do not repeat this repair.
- NSDL date alignment: 102/103 observed FPI archive dates have DII rows (99.03%); seven DII schema gaps remain; no inferred holiday or imputation.
- USD/INR: BLOCKED; no guessed endpoint/mirror/paid API.
- Macro-Geo P0 release gate: BLOCKED; no candidate release.
- Event study and historical regime research: BLOCKED for zero matured windows.
- Four-group validation PASS is scoped only to schema/provenance, not overall source coverage or causal event verification.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; production branch untouched.

## 6. Exact next actions
1. Investigate the seven official NSDL DII archive schema/table misses from raw official HTML and exact archive form behavior; only add parser support after inspecting actual HTML/headers and units. Do not label dates holidays without independent NSE calendar evidence.
2. Continue official FBIL/RBI USD/INR archive endpoint verification; if no public free machine-readable source contract is evidenced, keep BLOCKED.
3. For event study, acquire timestamp-grounded event-occurrence evidence or continue to label publisher publication timestamps as media mentions; wait for post-publication market closes. No synthetic windows.
4. Re-run the strict gate only after source evidence materially changes. Do not rerun completed PASS collection/test steps without regression evidence.
5. Keep probability-discrimination investigation from C257 separate from production scoring; no selector or ranking changes.

## Guardrails
₹0 spend; official/free sources only; no fabricated data/timestamps; UNKNOWN/BLOCKED never PASS. Historical target-hit rates are not net returns. No gate relaxation.
