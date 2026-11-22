# Macro-Geo Run #317 Completion and NSDL Gap Audit — C268

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity and evidence
Re-fetched the Master Continuity Ledger, C267 stall diagnostic, C266 cancellation diagnostic and C261 NSDL official-source triage report before acting. PASS work was not repeated. Run #317 (Actions run ID `45001040455`) completed with conclusion FAILURE on corrected collector SHA `885528a076e98996455358ee236f1a2960a276ea`. Job ID: `137143161030`.

Artifact `macro-geo-p0-event-study`, ID `14746542146`, size 4,909,367 bytes. Downloaded and independently SHA-256 verified: `a7cd5f508d11d0cc2e84e63f509a31dde7245417af0d42536efb0a26c3fb460f`, matching the GitHub artifact digest.

## Run outcome
Steps 1–15 succeeded, including 200-session official NSE acquisition, canonical panel build, P0 collection, bounded source repair, NSDL historical FPI/DII collection, source coverage audit, factor audit and event-study execution. Step 16 strict Macro-Geo hard gate returned FAILURE by design because its report status was BLOCKED; this is fail-closed acceptance, not an unhandled collector crash. Step 17 historical regime study ran but returned BLOCKED_NO_MATCHING_REGIMES; sector rotation feature step 18 was skipped; artifact upload step 19 succeeded.

## NSDL artifact audit
Artifact contents independently inspected:
- `fpi_dii_flows.csv`: 205 rows; FPI 103 unique dates and DII 102 unique dates over 2026-06-23..2026-11-20.
- Official NSDL collection report: 102 DII day queries succeeded; coverage vs 103 FPI archive dates = 99.03%.
- DII errors explicitly recorded for 2026-07-17 and 2026-08-26: no Equity/Stock Exchange net-investment table / schema not recognized. These are unresolved source-response gaps, not zero flows.
- 2026-07-17 has an FPI row (-3135.17) but no DII row. 2026-08-26 has no row in the combined output. Neither date is silently imputed.
- Five CM trading holidays are explicitly recorded and skipped with official circular provenance: 2026-06-26, 2026-09-14, 2026-10-02, 2026-10-20, 2026-11-10.
- This artifact does not prove the missing DII date responses or historical units across all NSDL pages. Keep both missing DII observations UNKNOWN.

## Strict gate and remaining blockers
Hard gate JSON: `status=BLOCKED`; P0 coverage 7/8; only missing required P0 group is `usd_inr`; `candidate_release_allowed=false`; production selector, ranking score and pressure fade all unchanged.
- USD/INR: 0 rows; FRED DEXINUS timed out; no verified direct official RBI/FBIL machine-readable endpoint configured.
- Event study: 21 publisher mentions, 1 eligible, 20 pending, 0 event windows. Report reason: no event had both a valid pre/post publication-close window. Publication time is not event occurrence time.
- Historical regime study: 11 provisional anchors, 0 regimes with windows; research remains BLOCKED.
- Source inventory: 8 of 34 sources available, 26 not connected. Generic source inventory does not prove live connectivity, point-in-time validity, units or causal validity.

## Rejected
- Rejected treating run FAILURE as collector crash; logs show explicit strict-gate BLOCKED result and successful artifact upload.
- Rejected declaring NSDL DII 2026-07-17 or 2026-08-26 as zero-flow, holiday or PASS.
- Rejected treating NSDL collection status AVAILABLE as complete coverage; actual coverage remains AVAILABLE_WITH_GAPS.
- Rejected claiming event-study or historical-regime research PASS from operational step success.
- No paid APIs, synthetic data, fabricated timestamps, speculative parser changes, duplicate dispatch or production changes.

## Exact next actions
1. Investigate official NSDL date-submitted response/page structure for 2026-07-17 and 2026-08-26; change parser only if direct source evidence establishes a distinct valid schema/table.
2. Continue official free RBI/FBIL USD/INR endpoint investigation; if no machine-readable historical contract is proven, retain BLOCKED.
3. For event study, build only from timestamped source events with valid pre/post closes and matured windows; keep publication and occurrence timestamps separate.
4. Re-run strict gate only after evidence changes; do not dispatch duplicate workflows while concurrency cancellation could interfere.
5. Keep Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged. Unknown remains UNKNOWN.
