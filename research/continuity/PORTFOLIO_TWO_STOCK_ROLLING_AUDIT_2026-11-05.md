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
