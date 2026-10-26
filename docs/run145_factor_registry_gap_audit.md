# Run #145 Factor Registry Gap Audit and Repair Plan

- Audit run: [GitHub Actions #145](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40308886446)
- Artifact: `macro-geo-p0-event-study` (artifact ID `12645866010`)
- Audited commit: `030d40e1903139a37062cf78c2e6bd39399d661a`
- Branch: `audit/run93-corrective-fixes`
- Audit date: 2026-10-26
- Decision: **BLOCKED**; do not release prospective candidates.

## Evidence read from the actual Run #145 artifact

Files inspected:
- `outputs/macro_geo/factor_coverage_audit.csv`
- `outputs/macro_geo/factor_coverage_audit.json`
- `outputs/macro_geo/source_coverage.csv`
- `outputs/macro_geo/source_coverage.json`
- `outputs/macro_geo/hard_gate_report.json`

Observed results:
- Factor Registry: 35 factor rows; 0 factors have all mapped source groups available; 13 factors are `NOT_CONNECTED`, 22 are `PARTIAL_SOURCE_COVERAGE`.
- Source inventory: 34 registered source groups; 9 available, 25 not connected.
- Hard-gate blocker: `FACTOR_REGISTRY_HAS_INCOMPLETE_SOURCE_COVERAGE`.
- `candidate_release_allowed=false`.
- P0 backbone is separately reported `P0_COMPLETE` (8/8 groups); this does **not** mean the wider Factor Registry is complete.
- Event study: 45 events, 20 eligible, 228 windows; event-level audit reports 19 mature H+1 and 15 mature H+5 events.
- Panel/equity latest date: 2026-10-23; no calendar-day mismatch.
- Missing data semantics: `UNKNOWN/BLOCKED`, never negative.
- Production selector, `RANKING_SCORE`, and `+1 PRESSURE_FADE` are unchanged.

## Exact 13 disconnected Factor Registry entries

Important naming correction: the 13 count is **factor IDs**, not 13 source-group names. These 13 factors collectively reference 18 distinct source groups that are not connected in the artifact's source inventory.

| Factor ID | Factor | Required mapped source groups | Artifact evidence |
|---|---|---|---|
| F05 | Federal Reserve surprise and guidance | us_yields; dxy; global_policy_events; fed_policy_surprises | all 4 NOT_CONNECTED |
| F07 | Domestic growth and public expenditure | macro_indicators; global_policy_events; sector_fundamentals; government_capex | all 4 NOT_CONNECTED |
| F09 | China and global industrial cycle | global_commodity_prices; macro_indicators; global_policy_events; china_indicators | all 4 NOT_CONNECTED |
| F14 | Global inflation and inflation expectations | macro_indicators; us_yields; india_bond_yields; inflation_components | all 4 NOT_CONNECTED |
| F15 | Global central banks beyond Fed | global_policy_events; fx_carry_and_cross_currency; us_yields | all 3 NOT_CONNECTED |
| F16 | China policy and commodity-specific supply shocks | global_commodity_prices; macro_indicators | all 2 NOT_CONNECTED |
| F17 | Monsoon weather and agricultural conditions | weather_agriculture; macro_indicators | all 2 NOT_CONNECTED |
| F18 | Domestic consumption and household demand | macro_indicators; sector_fundamentals | all 2 NOT_CONNECTED |
| F21 | Supply-chain disruption and critical inputs | global_freight_shipping; global_commodity_prices; sector_fundamentals | all 3 NOT_CONNECTED |
| F28 | Global growth and recession probability | macro_indicators; global_commodity_prices; global_freight_shipping | all 3 NOT_CONNECTED |
| F30 | Energy transition carbon and climate policy | global_policy_events; sector_fundamentals | both NOT_CONNECTED |
| F33 | IPO float listing age and post-listing supply | ipo_float_unlocks; market_microstructure | both NOT_CONNECTED |
| F34 | Research-house and analyst action | research_house_actions; earnings_revisions | both NOT_CONNECTED |

## Source-level evidence of the gap

For each of the following 18 source groups, Run #145's `outputs/macro_geo/source_coverage.csv` records `NOT_CONNECTED`, zero rows, no selected file path, and the note “No source file found; absence is UNKNOWN, not NEGATIVE”:

1. `us_yields`
2. `dxy`
3. `global_policy_events`
4. `fed_policy_surprises`
5. `macro_indicators`
6. `sector_fundamentals`
7. `government_capex`
8. `global_commodity_prices`
9. `china_indicators`
10. `india_bond_yields`
11. `inflation_components`
12. `fx_carry_and_cross_currency`
13. `weather_agriculture`
14. `global_freight_shipping`
15. `ipo_float_unlocks`
16. `market_microstructure`
17. `research_house_actions`
18. `earnings_revisions`

This is evidence of **missing repository inputs**, not evidence that the underlying real-world factor is negative or that the source publisher has no data.

## Required schema from the collector inventory

The expected required columns are defined in `pipeline/macro_geo_source_coverage.py`:

| Source group | Required fields |
|---|---|
| us_yields | DATE, SERIES, CLOSE |
| dxy | DATE, CLOSE |
| global_policy_events | EVENT_DATE, PUBLISHED_AT, COUNTRY, EVENT_TYPE, SOURCE_URL |
| fed_policy_surprises | DATE, ANNOUNCEMENT_AT, EXPECTED_RATE, ACTUAL_RATE, SURPRISE_BPS, SOURCE_URL |
| macro_indicators | DATE, INDICATOR, VALUE |
| sector_fundamentals | DATE, SECTOR, METRIC, VALUE |
| government_capex | DATE, DEPARTMENT, ACTUAL_SPEND, BUDGET_SPEND, RELEASED_AT, SOURCE_URL |
| global_commodity_prices | DATE, COMMODITY, CLOSE |
| china_indicators | DATE, INDICATOR, VALUE, RELEASED_AT, SOURCE_URL |
| india_bond_yields | DATE, YIELD_10Y |
| inflation_components | DATE, COUNTRY, COMPONENT, VALUE, RELEASED_AT, SOURCE_URL |
| fx_carry_and_cross_currency | DATE, PAIR, VALUE |
| weather_agriculture | DATE, REGION, INDICATOR, VALUE |
| global_freight_shipping | DATE, INDICATOR, VALUE |
| ipo_float_unlocks | DATE, SYMBOL, EFFECTIVE_FLOAT, EVENT_TYPE |
| market_microstructure | DATE, SYMBOL, CIRCUIT_STATUS, SURVEILLANCE_STATUS |
| research_house_actions | PUBLISHED_AT, SYMBOL, HOUSE, ACTION, SOURCE_URL |
| earnings_revisions | DATE, SYMBOL, REVISION, PUBLISHED_AT |

## Repair sequence (fail closed)

1. Implement collectors only against documented official/credible endpoints; record source name, exact URL, retrieval timestamp, units, publication/release timestamp, and whether the series is official or secondary.
2. Preserve raw responses immutably before normalization. Never write placeholder rows, fill missing values with zero, or infer a publication timestamp from retrieval time.
3. Add deterministic mocked tests for response schemas, empty responses, timeouts/rate limits, malformed dates, duplicates, and missing provenance.
4. Run a bounded live smoke test per source adapter; capture actual HTTP status, returned row count, date span, and source URL in an artifact.
5. Run domain-specific QA (units, dates, release timestamps, revisions, symbol mapping, and point-in-time availability) before promoting any group to AVAILABLE. Schema-only availability is insufficient evidence of research readiness.
6. Rebuild `source_coverage.json`, `factor_coverage_audit.csv/json`, and hard-gate report from observed files. Require zero disconnected required groups, no contradictory manifest status, and `candidate_release_allowed=true` before declaring PASS.
7. Keep the production selector, `RANKING_SCORE`, and frozen `+1 PRESSURE_FADE` unchanged. Do not score immature H+1/H+3/H+5 outcomes. Missing evidence remains UNKNOWN/BLOCKED.

## Status of this change

This file records a reproducible artifact audit and an actionable repair contract. It does **not** claim that the 18 datasets have already been collected. Run a new bounded collector workflow and inspect its artifacts before marking any source group repaired.
