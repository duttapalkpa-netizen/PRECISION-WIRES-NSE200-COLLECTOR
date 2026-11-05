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
