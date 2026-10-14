# Macro–Geo & Sector Engine — Data-gap register and Run 29 audit

**Scope:** audit branch only. **As of:** 2026-10-14 (IST).  
**Verified workflow run:** [Run #29 — 38448989013](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/38448989013)  
**Audited commit:** `8ff1cf9844bf8c41aced7a39d4fd5833ffc26185`

## Verified run result

- GitHub Actions workflow conclusion: **SUCCESS**; all 22 main steps completed successfully.
- Unit tests: **PASS**, including the three Macro–Geo tests (missing inputs remain blocked, event-window arithmetic, duplicate panel rejection) and prospective-ledger tests.
- NSE acquisition: **200 valid sessions**.
- Normalized dataset: **494,805 rows; 2,946 symbols; 200 dates**.
- Strict dataset QA step: **completed successfully**.
- Retrospective reproducibility: **PASS_BYTE_FOR_BYTE_REPRODUCIBLE**.
- Macro–Geo source inventory: **INVENTORY_COMPLETE_WITH_GAPS** — 24 logical source groups total; 1 AVAILABLE and 23 NOT_CONNECTED; 0 schema failures, 0 generic-QA warnings, 0 read errors in this run.
- Event study: **BLOCKED_MISSING_OR_INVALID_INPUTS** because both `data/external/market_panel.csv` and `data/external/events.csv` were absent. No event returns were calculated.
- Prospective ledger at run end: 40 rows; unresolved outcomes T1=12, T3=32, T5=32. These are not 30 fully matured prospective cutoffs; do not describe the experiment as fully validated.

## How to interpret “1 AVAILABLE”

This means the expected file was present and passed the script's generic schema/missingness/duplicate/date checks. It does **not** certify source authenticity, units, historical revision handling, point-in-time availability, or macro/geo coverage. The available group is the normalized NSE daily-equity panel; the 23 external macro/geo/sector source groups are still disconnected.

## Priority order for closing gaps

1. **P0 — minimum viable event study:** benchmark and sector index history; India VIX/global volatility; FPI/DII flows; crude; USD/INR; corporate and geopolitical events; market microstructure; then construct the canonical `market_panel.csv` and `events.csv`.
2. **P1 — policy and repricing context:** RBI policy/liquidity, India and US yields, DXY, official macro releases, earnings revisions, global commodity prices, global policy events, IPO float/unlocks.
3. **P2 — broader transmission coverage:** sector fundamentals, FX carry/cross-currency, weather/agriculture, freight/shipping, research-house actions.

The detailed machine-readable inventory is `config/macro_geo_data_gap_register.csv`. Its 23 disconnected source groups plus the two missing canonical event-study inputs are tracked separately (25 rows), because the canonical files are derived inputs, not extra source groups.

## Required quality contract before scoring

Every source should carry source name/URL, observation date, publication timestamp and timezone, units/currency, revision/vintage if applicable, and a point-in-time availability rule. Add source-specific validation, calendar alignment, stale-data thresholds, duplicate handling and licensed-access checks. Missing data remains **UNKNOWN**, never automatically NEGATIVE.

## Guardrails

This is audit-only. No live-feed ingestion, Macro–Geo factor scoring, or ranking modification is operational yet. Do not change Run #58, the production selector, `RANKING_SCORE`, the collector/QA backbone, 672 diagnostics, or `+1 PRESSURE_FADE`. Do not promote a factor until point-in-time event studies, benchmark-adjusted returns, matched controls, overlap handling, confidence intervals and walk-forward/prospective tests demonstrate incremental value.
