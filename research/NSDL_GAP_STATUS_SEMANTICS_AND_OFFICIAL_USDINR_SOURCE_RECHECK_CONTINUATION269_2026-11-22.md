# NSDL Gap Status Semantics and Official USD/INR Source Recheck — C269

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity check
Re-fetched the current Master Continuity Ledger (C268 present), C268 artifact audit, C261 NSDL source triage, C253 FBIL endpoint audit, and the current NSDL collector, source-coverage logic and workflow YAML. PASS work was not repeated. Runs #316/#390 were confirmed cancelled; #317 completed as recorded in C268; no older active Macro-Geo run remained before this bounded audit change.

## New direct artifact findings
Re-opened Run #317 artifact `14746542146` and parsed `outputs/macro_geo/nsdl_fpi_dii_collection.json`:
- Collector summary status was `AVAILABLE` despite two explicit DII query errors.
- DII successes: 102. DII errors: 2 (2026-07-17 and 2026-08-26).
- The `coverage_audit` compared DII dates only against FPI archive dates. That correctly identifies July 17 as a missing DII date, but it cannot expose August 26 because the FPI archive itself has no row for that date.
- Thus the 99.03% figure is specifically DII/FPI archive-date alignment, not complete DII query coverage and not an all-trading-session rate.

## Bounded audit-code correction
Code commit: `399b0a61535f84bfbee8347321e51c590ff9ff55`.
Changed only `pipeline/macro_geo_nsdl_flows.py` and added `qa/test_macro_geo_nsdl_flows.py`:
1. Record every exact DII date-query result as SUCCESS or FAILED with date, row count/error and source URL.
2. Report total attempted, successful and failed DII requests plus exact failed dates separately from FPI-date alignment.
3. Return `AVAILABLE_WITH_GAPS` rather than `AVAILABLE` whenever collection meets the minimum history threshold but any source query or date-alignment gap remains. Insufficient history remains `BLOCKED_INSUFFICIENT_HISTORICAL_COVERAGE`.
4. Do not infer an authoritative trading calendar from the collector's weekday request schedule; the audit explicitly labels query attempts separately.

Test fixture scope: unit fixtures only; no fixture rows enter research data. Equivalent helper assertions were executed successfully in the local Python validation. The newly added unittest file is not yet wired into the existing workflow test command, so CI execution of that specific test remains PENDING.

## Live CI state on corrected audit commit
- Run #318 / ID `45014759390`, head `399b0a61535f84bfbee8347321e51c590ff9ff55`: IN_PROGRESS. Setup, dependencies and existing event-study/repair regression step 5 SUCCESS; official NSE 200-session acquisition step 6 IN_PROGRESS; NSDL step 11 not reached. No conclusion or artifact yet.
- Run #394 / ID `45014759398`, same head: IN_PROGRESS. Setup, dependencies and corrected-forward-label/prospective-ledger regression step 5 SUCCESS; normalized NSE history acquisition step 6 IN_PROGRESS; later walk-forward and research steps pending.
- Job-log retrieval for #318 returned Azure BlobNotFound; this is a log retrieval limitation, not run failure.
- No duplicate dispatch or edits were made while these runs were active.

## Official NSDL source recheck
The official NSDL date-driven form `https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A` is publicly readable as a form with a date input and “View Report”, but the accessible page has no submitted-date response, form field contract or returned table for 2026-07-17 / 2026-08-26. The collector currently posts to the legacy host/path `https://www.fpi.nsdl.co.in/web/Users/DIIGenerateReport.aspx?Rep=A`; the two host/path forms are not proven equivalent by the available evidence. A public fetch of the legacy URL returned 502/timeout in this inspection. Do not guess a new POST contract or silently switch hosts. Both exact dates remain UNKNOWN pending direct date-submitted official response evidence.

## Official USD/INR source recheck
- RBI's official July 4, 2018 release says FBIL would take over daily reference-rate computation from July 10, 2018 and RBI's daily reference-rate release would stop after July 9, 2018.
- RBI's current Reference Rate Archive page provides date-range and Excel controls, but RBI's own notice directs users to FBIL for post-2018 rates. It does not establish post-2018 daily USD/INR coverage.
- Newly inspected official FBIL November 2026 newsletter reports monthly-average USD/INR reference-rate values and monthly trade/volume aggregates; these are not daily observations. FBIL homepage search indexing also exposes a small number of dated daily spot-rate rows, but no verified public full-history machine-readable endpoint, schema, pagination or date-range contract.
- Therefore no daily USD/INR series was fabricated or substituted. USD/INR remains BLOCKED. The FBIL newsletter may be retained as a monthly cross-check only if its methodology and exact monthly averaging semantics are documented; it cannot satisfy daily P0 coverage.

## Event-study maturity diagnosis
Run #317's market panel ends 2026-11-20. The only event inside panel date bounds was published at 2026-11-20T15:14:01Z (20:44:01 IST), after the 15:30 IST NSE close. There was no post-publication close in the panel, so zero windows is expected under the current publication-time rule. The other 20 publisher mentions are dated 2026-11-21/22 and remain pending until subsequent observed market closes are collected. No code defect or missing price should be inferred; no return may be computed before the panel is extended with genuine closes.

## Validation and status
- The changed helper logic passed equivalent local fixture assertions for two explicit failed query dates, separate FPI-date alignment, and fail-closed status derivation.
- Full corrected workflow and artifact validation are PENDING on Run #318.
- New unittest CI integration is PENDING.
- NSDL date-response proof remains UNKNOWN.
- USD/INR daily official historical coverage remains BLOCKED.
- Event windows remain BLOCKED pending new post-publication closes.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E remain unchanged.

## Rejected
- Rejected presenting 99.03% FPI/DII date alignment as complete DII query coverage.
- Rejected marking an artifact AVAILABLE when explicit source queries failed.
- Rejected treating Aug 26 as covered merely because it is absent from the FPI archive.
- Rejected using FBIL monthly averages as daily USD/INR values.
- Rejected treating RBI's pre-July-10-2018 daily archive as post-2018 coverage.
- Rejected switching the NSDL host or inventing a POST body without a proven official form contract.
- Rejected manufacturing event returns for after-close or future publications.
- No paid APIs, third-party flow mirrors, synthetic market observations or production-selector changes.

## Exact next actions
1. Poll #318 until completion; inspect step 11, the updated NSDL report, exact failure dates and artifact. If it completes, verify `AVAILABLE_WITH_GAPS`, 102 successes, 2 failed dates and SHA-256 before recording any scoped PASS.
2. Once #318/#394 no longer occupy their queues, wire `qa.test_macro_geo_nsdl_flows` into the workflow regression command and run the targeted test without cancelling an active Macro-Geo job.
3. Obtain direct official NSDL date-submitted evidence for July 17 and Aug 26; compare legacy and pilot form contracts only through documented, ordinary public form behavior.
4. Continue FBIL official frontend/archive investigation; retain BLOCKED unless a free daily historical endpoint and complete schema/date coverage are proven.
5. After the next NSE session's genuine market close is present in the panel, re-run event study; do not force early returns.
6. Re-run the strict hard gate only after evidence changes. Preserve all production invariants and UNKNOWN/BLOCKED semantics.
