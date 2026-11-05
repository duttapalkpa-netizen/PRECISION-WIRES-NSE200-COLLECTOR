# Portfolio Two-Stock Rolling Swing Audit

Recorded: 2026-11-05
Status: IMPLEMENTED; INITIAL NSE 200-SESSION EXECUTION IN PROGRESS

## User-requested research scope
Include only these two user-designated holdings in an isolated rolling research track:
- HINDCOPPER — Hindustan Copper Limited — ISIN INE531E01026
- EPACKPEB — EPack Prefab Technologies Limited — ISIN INE0MLS01022

The symbols and ISINs are checked against the NSE Security Master at runtime. EPack identity is also supported by NSE Integrated Filing:
https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_188610_20082026143715_iXBRL_WEB.html

## Implementation
- Script: pipeline/portfolio_rolling_audit.py
- Workflow: .github/workflows/portfolio_two_stock_rolling_audit.yml
- Uses existing official NSE Full Bhavcopy + Security Deliverable collector and 200-session normalizer.
- Enforces at least 200 valid sessions independently for each symbol.
- Uses OHLCV, relative volume, delivery percentage, EMA20/EMA50, 5/20-session returns and distance from 20-session high.
- Research-only setup cohort is explicitly defined and does not alter the production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or engines.
- Outcomes: 2%, 3%, 5% future high-touch and close-confirmation over T+1, T+3 and T+5; adverse excursion also reported.
- Future windows explicitly use T+1 through T+H. Incomplete forward tails are excluded from matured outcome denominators.
- Missing delivery/history evidence remains UNKNOWN and is excluded from the setup cohort, not treated as a negative signal.
- Outputs: outputs/portfolio/portfolio_daily_status.csv, portfolio_rolling_metrics.csv and portfolio_rolling_report.json.
- Workflow scheduled for 17:00 IST weekdays; GitHub scheduled workflows only execute from the repository default branch. Until merged to default, push/manual workflow runs are the available validation path.
- Rolling NSE source cache added so subsequent daily runs can reuse historical sessions and fetch only newly required sessions.

## Execution state at record time
- Initial portfolio audit run: 41979992934, started 2026-11-05 06:22:39 UTC.
- Last observed state: in_progress; job 127087641749 was acquiring the 200 official NSE cash-market sessions.
- Follow-up run 41980154510 was cancelled while a newer workflow revision was pushed; do not treat it as a failure or success.
- No daily portfolio status or rolling hit-rate results are certified until the full job completes and its artifact is inspected.
- The 200-session download has not yet been proven to complete within the 10-minute job limit.

## Research interpretation
This is a portfolio-specific diagnostic overlay, not a trade recommendation and not a selector change. The latest signal row is label-free; it cannot be assigned a future hit/miss until its H+1/H+3/H+5 windows mature. Report both high-touch and close-confirmation rates, with sample counts and adverse excursion. Do not infer that daily price appreciation alone proves improvement in the research system.

## Non-changes
No use of portfolio quantity, average purchase price or P&L to bias the model. No guessed NIC-2 mapping. No synthetic data, fabricated timestamps, look-ahead, hard-gate relaxation, paid APIs or external services.

## First execution and schema correction
- Run 41979992934 successfully acquired 200 NSE sessions and built 499,798 normalized rows across 2,991 symbols. The run took approximately three minutes for the 200-session acquisition and dataset build.
- The portfolio audit step then correctly blocked because the daily Full Bhavcopy schema did not include an ISIN column. This was an audit-code schema assumption, not a failure of the NSE data acquisition.
- Corrective commit 9fa5985cacec177420ff0870bc04a10a83f30cd2 changed the audit to resolve symbol identity from the independently validated NSE Security Master; if source ISIN is present it is cross-checked, not trusted blindly.
- Script also retains UNKNOWN when delivery evidence is missing and uses exact forward windows T+1..T+H.
- Follow-up workflow 41980329391 was queued at record time; preceding cache-enabled workflow 41980203487 was still acquiring historical sessions. No final rolling metrics are claimed until a successful run artifact contains all three portfolio outputs.
- Rolling cache is configured with per-run keys and a shared restore prefix to make later daily runs incremental.


## 317-session master reuse and portfolio audit result (2026-11-05)

### Correction to prior workflow design
The user's research already had a validated 317-session master. The earlier portfolio workflow independently reacquired 200 sessions because its initial implementation hard-coded a 200-session minimum and used a separate 200-session collector. Calling that a 200-session completion without distinguishing it from the existing 317-session research master was misleading. Do not repeat historical acquisition when the validated master is available.

### Recovered source master
- Library source: `NSE_317_SESSION_MASTER_MERGE_2026-11-05.zip`
- Source ZIP SHA-256: `5875be86d9b4753582b24363243ffad9fa18c197e4e7f9eecd7e1d0936ce7880`
- Dataset: `nse_eq_317_sessions.csv`
- Dataset SHA-256: `a6e8c4c703365dfa320df448740690b0b445be4aac6383e0765a488867e85dff`
- 317 dates: 2025-08-06 through 2026-11-03; 765,887 EQ rows; 3,040 symbols; zero duplicate SYMBOL+SERIES+DATE rows.
- HINDCOPPER: 317 sessions (2025-08-06 through 2026-11-03).
- EPACKPEB: 279 sessions (2025-10-01 through 2026-11-03), reflecting its shorter listing history; no missing history was synthesized.
- Source master embeds OHLCV and delivery quantity/percentage fields. The package manifest lists the 200-session baseline plus 57- and 60-session verified backfills; the 317-session merge was verified separately from the fresh portfolio workflow.

### Portfolio historical audit output (research-only; local execution against recovered 317-session master)
- Package: `PRECISION_WIRES_PORTFOLIO_317_SESSION_ROLLING_AUDIT_2026-11-05.zip`
- Package SHA-256: `fe561c593b25c0ac2de5beb1e5874e967d1342bb32d0c61b5120b58e3104661c`
- Saved to Library root at `/PRECISION_WIRES_PORTFOLIO_317_SESSION_ROLLING_AUDIT_2026-11-05.zip`.
- Identity reference uses the two official NSE Integrated Filing URLs and ISINs, not a fabricated copy of the full NSE EQUITY_L security master.
- Latest historical session in this 317-master audit: 2026-11-03. Latest session has no matured forward outcome and is excluded from outcome denominators.
- All-cutoff baseline metrics (high-touch / maximum-close-confirmation rates):
  - HINDCOPPER: T+1 2% = 40.190% / 22.152%; T+3 = 60.510% / 39.490%; T+5 = 69.551% / 49.679%.
  - HINDCOPPER: T+1 3% = 28.165% / 14.873%; T+3 = 49.682% / 32.166%; T+5 = 58.974% / 42.308%.
  - HINDCOPPER: T+1 5% = 12.658% / 5.380%; T+3 = 30.892% / 19.427%; T+5 = 41.346% / 31.731%.
  - EPACKPEB: T+1 2% = 54.317% / 23.022%; T+3 = 72.101% / 43.841%; T+5 = 76.642% / 52.920%.
  - EPACKPEB: T+1 3% = 40.288% / 17.626%; T+3 = 59.783% / 35.507%; T+5 = 67.153% / 45.620%.
  - EPACKPEB: T+1 5% = 15.827% / 8.993%; T+3 = 38.406% / 26.087%; T+5 = 48.540% / 36.496%.
- Setup-qualified sample sizes were very small: HINDCOPPER 2 cutoffs, EPACKPEB 3 cutoffs. These rates are descriptive only and are not adequate evidence of predictive edge. Do not relax setup gates to inflate sample size.
- Latest 2026-11-03 daily setup state was false for both stocks; latest forward labels remain NOT_MATURED.
- This 317-session audit is a local research computation and is not a GitHub Actions run. The saved ZIP contains daily status, rolling metrics, JSON report, identity reference and manifest.

### GitHub workflow failure diagnosis and fix
- Run `41981518300` failed in the outcome aggregation step because pandas DataFrame.max() does not accept `min_count`. NSE security master acquisition, 200-session acquisition and normalized dataset build all succeeded.
- Fixed complete-window aggregation using explicit per-row completeness masks in commit `71b52c5f87bb94ee63cf6fcd24a3c8585a4c11cc`; blob SHA `0285a29104edb925fd9342cd62db6b894fd9d208`.
- Run `41982221358` succeeded, artifact ID `13395020000`, artifact SHA-256 `41c9ebafbd7d45080b4d0a6e6f87dfed9e2483d397b3fc975e80993b40c140a7`. It used a separate 200-session dataset with 200 sessions per stock and latest session 2026-11-04. This success does NOT replace or supersede the 317-session master audit above.
- The workflow still needs a controlled integration path to consume the existing 317-session master/backfill components for ongoing GitHub-based portfolio refreshes; do not describe the current 200-session workflow as a 317-session run.

### Non-changes
No change to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A/B/C/D/E, hard gates or UNKNOWN semantics. No synthetic rows, fabricated timestamps, paid sources or portfolio quantity/cost-basis use.



## 317-source component verification and integration status (2026-11-05)
- Re-opened the Library source ZIP and independently streamed the merged CSV: ZIP SHA-256 remains `5875be86d9b4753582b24363243ffad9fa18c197e4e7f9eecd7e1d0936ce7880`; merged CSV SHA-256 remains `a6e8c4c703365dfa320df448740690b0b445be4aac6383e0765a488867e85dff`.
- Independently counted the actual CSV: 765,887 rows, 317 distinct dates (2025-08-06 to 2026-11-03), 3,040 symbols, all series EQ, zero duplicate SYMBOL+SERIES+DATE keys; HINDCOPPER 317 rows and EPACKPEB 279 rows. Manifest and CSV counts agree.
- The three source Actions artifacts were re-read from GitHub: baseline Run 41633211838 / Artifact 13229637442 / archive SHA `369e5c1dcb8ab60584861564549de07c2d3bce4fb33abcff93724ae3ec99fa52`; 57-session Run 41846486071 / Artifact 13330413906 / archive SHA `f7234520994cf6ab6d878b693e5d9cfba2abc4f7394a0d3f080ca64a919b2ecb`; 60-session Run 41887855100 / Artifact 13352257383 / archive SHA `f3be8d977ecc6905569693b09ac10004e73775db1a54f7aee67eb30feb7c2d3a`.
- The 57-session dates are 2025-11-04 through 2026-01-27; the 60-session dates are 2025-08-06 through 2025-11-03. Together with the baseline 200, these are disjoint components of the verified 317-session calendar.
- Added planning record `research/continuity/PORTFOLIO_317_WORKFLOW_INTEGRATION_PLAN_2026-11-05.md` in commit `34f2f9a12dd14faf74cdd5e229316f1c627d36f0`.
- Integration is NOT yet complete: no new 317-session GitHub workflow run or artifact exists. The attempt to create the assembler source file was blocked by the GitHub write safety layer; do not claim code was committed or the new workflow executed. Keep the already successful 200-session run distinct from the verified local 317-session audit. Next safe action is to add and validate the assembler + separate workflow in a controlled commit, then inspect its run artifact before calling it operational.


## GitHub 317-session reconstruction and portfolio audit — SUCCESS (2026-11-05)
- Added `pipeline/verify_317_artifact_inputs.py`: downloads are reconciled against the expected baseline CSV SHA, each raw backfill file SHA, both manifest calendars, 317 distinct dates, 765,887 rows, 3,040 symbols, EQ-only series and unique SYMBOL+SERIES+DATE keys. It writes the 317-session normalized CSV and manifest; it does not fetch historical data from NSE.
- Added separate workflow `.github/workflows/portfolio_two_stock_rolling_audit_317.yml`. It downloads the three already existing immutable Actions artifacts, reconstructs the 317-session source, obtains the current NSE Security Master, and runs the isolated portfolio audit against that source. Job timeout is 10 minutes.
- Modified `pipeline/portfolio_rolling_audit.py` to accept `PORTFOLIO_SOURCE`; its default remains the original 200-session file. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines, or hard-gate behavior was changed.
- Successful GitHub Actions run: **41985471618**, commit `49459c62600001ea76edc7da3a1c0d9003c88d5d`, completed SUCCESS in about 40 seconds; job `127105070635`.
- All three source downloads were checksum-verified by actions/download-artifact: baseline artifact 13229637442 digest `369e5c1dcb8ab60584861564549de07c2d3bce4fb33abcff93724ae3ec99fa52`; 57-session artifact 13330413906 digest `f7234520994cf6ab6d878b693e5d9cfba2abc4f7394a0d3f080ca64a919b2ecb`; 60-session artifact 13352257383 digest `f3be8d977ecc6905569693b09ac10004e73775db1a54f7aee67eb30feb7c2d3a`.
- Assembler result: `PASS_SOURCE_RECONCILIATION`; 317 sessions 2025-08-06 to 2026-11-03; 765,887 rows; 3,040 symbols; zero duplicate keys; merged normalized CSV SHA-256 `c60afb406103be6c079cea7e3b18a50bd2f729d4424aa526b0bb51523bb17464`.
- NSE Security Master step succeeded: 2,393 EQ symbols; raw source SHA-256 `2b8620a8be23025c60185502f7782aff05461768d5c2df5fe7b764b53a3278df`.
- Portfolio step result: `PASS_RESEARCH_ONLY`; HINDCOPPER 317 sessions; EPACKPEB 279 sessions; latest source session 2026-11-03; 36 metric rows emitted. Latest daily close: HINDCOPPER ₹400.30 (daily -2.58%), EPACKPEB ₹201.51 (daily -7.64%). Both research setup flags false; latest forward outcomes remain NOT_MATURED and are excluded from matured hit-rate denominators.
- Uploaded reproducible GitHub artifact: ID `13395692955`, name `portfolio-two-stock-rolling-audit-317-1`, SHA-256 `af5d182747c9d6334bb395adec244fa0dccff9224427d69282a21c6220f5ec67`, 26,685,852 bytes. It contains the 317-session CSV, manifest, NSE security master evidence and portfolio reports.
- The separate legacy 200-session workflow also ran successfully as Run `41985457123` due the shared portfolio script path trigger; it remains a distinct 200-session run and must not be conflated with Run `41985471618`.
- Schedule caveat: the new workflow's weekday 17:00 IST cron is present but is not active until the workflow is merged into the default branch. No merge was performed or authorized. Until then, use manual dispatch or branch pushes.
- Scope caveat: this successful run reconstructs and audits the 317-session historical baseline; it does not yet append sessions newer than 2026-11-03. A subsequent controlled incremental NSE daily append is a separate next task.


## Append-only official NSE incremental refresh — SUCCESS (2026-11-05)
- Added `pipeline/append_official_nse_sessions.py` and separate workflow `.github/workflows/portfolio_two_stock_rolling_audit_incremental.yml`. This is an isolated research-only append track; no historical baseline re-download after a cache hit, and the seed path verifies the already reconstructed 317-session manifest before initializing the rolling cache.
- Workflow run **41987260655** completed **SUCCESS**; job **127110836521**; branch `fix/iip-41-vintage-audit-clean`; head commit `82e4d48ea50ca96449975da164dc600a13de1174`. Duration from 07:26:29Z to 07:28:23Z (~1m54s), within the 10-minute limit. All 15 job steps completed successfully.
- The initial rolling cache was not present, so the workflow correctly downloaded and reassembled the three immutable source artifacts, then seeded the append-only cache. This is a cache-miss bootstrap, not a historical re-collection from NSE.
- Official NSE acquisition requested the latest five published sessions. 2026-11-05 returned MISS (no valid official full bhavcopy available at acquisition time); 2026-11-04, 2026-11-03, 2026-11-02, 2026-10-30 and 2026-10-29 were successfully downloaded as Full Bhavcopy + Security Deliverable files. The append logic skipped all dates at/before the 317-session seed's 2026-11-03 cutoff and appended only **2026-11-04**.
- Newly appended official daily file: `sec_bhavdata_full_04112026.csv`; SHA-256 `eba68f9e211dcf5b2e349acdf58240dcb06e2fc92b30dc1aafdc15b1efc3df47`; 402,256 bytes; 2,739 EQ rows.
- Rolling dataset validation from downloaded artifact: **318 distinct sessions**, 2025-08-06 through 2026-11-04; **768,626 rows**, **3,043 symbols**, all EQ, zero duplicate SYMBOL+SERIES+DATE keys. HINDCOPPER 318 sessions; EPACKPEB 280 sessions. No fabricated rows or dates.
- Rolling manifest: `PASS_ROLLING_APPEND`; initial seed SHA-256 `c60afb406103be6c079cea7e3b18a50bd2f729d4424aa526b0bb51523bb17464`; appended date 2026-11-04; final dataset SHA-256 `61fa8dae1d6173221886b9be44af75dd19c4d4b28fa4d85591e7f99c6bae45ee`.
- Portfolio audit: `PASS_RESEARCH_ONLY`; source SHA matches the rolling manifest; latest session 2026-11-04. Latest HINDCOPPER close ₹423.25 (daily +5.733%), EPACKPEB close ₹205.01 (daily +1.737%). Both research setup flags remain false; latest forward labels are NOT_MATURED and excluded from matured denominators.
- Updated all-cutoff descriptive high-touch rates (not predictive edge claims): HINDCOPPER 2% T+1/T+3/T+5 = 40.256%/60.703%/69.649%; 3% = 28.435%/49.840%/59.105%; 5% = 12.780%/30.990%/41.214%. EPACKPEB 2% = 54.545%/72.364%/76.727%; 3% = 40.364%/60.000%/67.273%; 5% = 15.636%/38.545%/48.364%. Setup-qualified cutoff counts remain tiny (HINDCOPPER 2; EPACKPEB 3), so these conditional rates are not statistically adequate evidence of scanner precision or profitability.
- Uploaded artifact: ID **13396801561**, name `portfolio-two-stock-rolling-incremental-1`, 31,899,796 bytes; archive digest SHA-256 `5f186ac473778ffed92adfc6e3526252919a0c1b731ad92af514f1ae525e7fc1`. Downloaded and inspected the archive; dataset, manifest, raw official file, acquisition diagnostics and portfolio outputs reconcile.
- Schedule caveat remains: weekday 17:00 IST schedule is inactive until the workflow is merged to the default branch. No merge was performed. Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/41987260655
- This proves only the rolling portfolio-data append and two-stock research audit. It does not change or pass the V11.3 master Hard Gate, scanner precision/recall/lift calibration, 672 diagnostic winner separation, or Final Research Paper acceptance.


## V11.4 Top-30 walk-forward pilot — methodology hardening and run status (2026-11-05)
- The prior pipeline/walk_forward_backtest.py used partial future windows (rolling min_periods=1) and trained on earlier cutoff rows whose H+5 labels could overlap the test cutoff. This was identified as a material leakage/maturity risk before accepting any ranking metrics.
- Updated the research walk-forward code to accept WF_SOURCE, require complete T+1..T+H forward windows, and embargo the five sessions immediately preceding each test cutoff (training cutoff <= test cutoff - 6 trading sessions). This is research validation code only; production selector and its scoring remain unchanged.
- Added bounded workflow .github/workflows/v11_4_top30_walk_forward.yml, using the verified 318-session rolling artifact Run 41987260655 / Artifact 13396801561. Source manifest and SHA are checked before analysis. Initial pilot Run 41988728020 completed success; Artifact 13396254188, archive digest 74766213e0d023299e6e9789b925f36777aa79e46952c82da17dbf04b224f609, 30 cutoffs and 900 Top-30 rows.
- Independent artifact inspection found an inconsistency in the initial metrics JSON's H+5 precision denominator versus the actual prediction CSV; therefore the initial run's precision/recall/calibration output is NOT ACCEPTED as final evidence. It must remain a pilot artifact only, not a validated performance claim.
- Added pipeline/reconcile_walk_forward_maturity.py and made it a mandatory workflow step. It re-joins Top-30 predictions to the full scored universe by (CUT_OFF, SYMBOL), checks outcome alignment and duplicate keys, and recomputes target-specific precision, recall, base rate, lift, calibration and diagnostic winner separation using only fully matured outcome rows.
- Corrected rerun 41989086610 (head commit a471dc6c904a831d20e39104e4b9cc5d941e2aa8) was observed in progress at the time of this note. Do not call the Top-30 validation complete until this run finishes successfully and its walk_forward_maturity_reconciliation.json is inspected.
- The first pilot's exploratory metrics are not production claims. In particular, winner/non-winner probability separation was near zero in its unreconciled report; the small 30-cutoff pilot cannot establish robust scanner edge, profitability, or final Hard Gate acceptance.


## Independent audit exception and read-back guard (2026-11-05)
- Re-opened corrected Top-30 walk-forward artifact Run **41989086610**, Artifact **13396449602**, ZIP SHA-256 `f4e51ee4de4b171ea6a5399e6668c2c6cd67f7a152b2489b881d3d97f3263643`.
- Independent local count of the persisted CSVs found a material mismatch against `walk_forward_maturity_reconciliation.json`: Top-30 T20_H5 matured hits are 64 in `walk_forward_predictions.csv` versus 62 in the JSON; full-universe T20_H5 winners are 1,476 in `walk_forward_universe_probabilities.csv` versus 1,455 in the JSON. H+1 and H+3 counts agree. Selected prediction keys are unique and the selected/universe outcome values align.
- The JSON/CSV mismatch means H+5 precision/recall/lift from this artifact are not certified. Do not quote 7.52% precision or 4.08x lift as validated until the exact persisted artifact is reconciled.
- Diagnostic separation CSV has 784 diagnostic-state rows: 635 UNKNOWN, 130 POSITIVE, 19 NEGATIVE. Macro/geopolitical source slots remain UNKNOWN; some technical evidence slots are POSITIVE but have little/no meaningful separation. This is not evidence that all 672 diagnostics have been independently sourced or validated.
- Added a strict persisted-file read-back guard to `pipeline/reconcile_walk_forward_maturity.py`, commit `decd59469208207816f458b3a2f2454701219df6`, blob SHA `f89de61766862666cd42e5edfce923d7964e496d`. The guard recomputes matured hit/winner counts from the exact CSV files intended for upload and blocks if either JSON disagrees.
- Guarded rerun **41990750128** is in progress as of 2026-11-05 07:56:32 UTC; do not accept until all steps complete and its new artifact has been independently inspected.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines or hard-gate criteria were changed. No hard gate was relaxed.
