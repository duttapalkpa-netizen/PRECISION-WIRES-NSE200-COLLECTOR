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


## Bounded repair batch (in progress; not a release PASS)

The first implementation batch adds real collectors for these source groups:
- `us_yields`: FRED observations with an official US Treasury daily-yield CSV fallback; the observed source and URL are retained.
- `dxy`: the ICE US Dollar Index ticker via the Yahoo Finance chart API, explicitly labelled as a third-party mirror and held for domain QA.
- `global_commodity_prices`: public FRED commodity observations. If a requested series fails, the report preserves the failure; a partial set is not treated as clean coverage.
- `global_policy_events`: official Federal Reserve and ECB feed items with publisher URL and publication timestamp. The publication date is explicitly marked as a proxy, not silently treated as the true policy-decision date.

QA controls:
- Mocked tests cover schema rejection, missing observations, source URLs, timestamps, DXY session-date alignment, RSS link parsing, UNKNOWN semantics, and warning-state handling.
- A source-inventory contract test checks that all 18 Run #145 missing groups have explicit path and required-column definitions.
- A separate short live test checks the official Treasury yield feed over a 21-calendar-day window.
- The full Macro-Geo workflow invokes the bounded collector before source coverage; collector failures are visible and do not relax the hard gate.
- The factor audit counts only non-empty `AVAILABLE` source rows as connected. `DATA_QUALITY_WARN` is not counted as connected.
- Collector output stays at `DATA_QUALITY_WARN` until a separate domain/source QA pass explicitly clears it.

This batch does **not** repair the remaining 15 of 18 disconnected groups, and does not by itself establish point-in-time validity, complete historical coverage, causal effect, or permission to release candidates. The full workflow and hard gate must remain blocked until all required groups have genuine source evidence and their domain-specific QA passes.


### First bounded smoke run evidence

- GitHub Actions run: [#40362003941](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40362003941) — SUCCESS.
- Mocked unit tests: 10 passed, including a contract check for all 18 missing source-group definitions.
- Official US Treasury live source smoke: 42 observations across 2Y, 10Y, and 30Y maturities, 2026-10-05 through 2026-10-26.
- The live smoke validates feed reachability, schema, and source URL for the Treasury yield series only. It does not validate the full 18-group registry or release readiness.

- Expanded live smoke for DXY and central-bank feed connectivity: [Run #40362378233](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40362378233), pending at documentation update time.


### Source contract tightening

The source inventory now requires `SOURCE_URL` and `OBSERVED_AT_UTC` for each of the 18 disconnected groups, plus group-appropriate `PUBLISHED_AT` or `RELEASED_AT` fields where point-in-time event/indicator data needs them. A file with only the numerical value columns is insufficient for release readiness. Schema failures remain distinct from generic QA warnings and cannot be downgraded by collector-report reconciliation.


## Status checkpoint — 2026-10-26 (do not interpret as release PASS)

The latest bounded source smoke is [GitHub Actions #40362965982](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40362965982), SUCCESS. It validates the bounded unit suite and live Treasury feed test, not the full Factor Registry.

### Collector implementation status for the 18 Run #145 missing groups

| Source group | Implementation evidence | Release/coverage status |
|---|---|---|
| `us_yields` | Official US Treasury daily CSV collector; bounded live feed passed | Collected; domain QA / integration artifact still required |
| `dxy` | Yahoo Finance `DX-Y.NYB` collector; live smoke passed | Third-party mirror; domain/licensing/definition QA required |
| `global_commodity_prices` | FRED series collector for WTI and gold | Collector exists; full live series and unit/frequency QA pending |
| `global_policy_events` | Federal Reserve and ECB RSS/Atom parser | Feed connectivity passed; item relevance and actual event-date QA pending |
| `fed_policy_surprises` | No validated expected-rate consensus source | UNKNOWN / NOT REPAIRED |
| `macro_indicators` | No complete collector with release-time provenance | UNKNOWN / NOT REPAIRED |
| `sector_fundamentals` | No validated sector metric collector | UNKNOWN / NOT REPAIRED |
| `government_capex` | No collector with official release timestamp and actual/budget spend schema | UNKNOWN / NOT REPAIRED |
| `china_indicators` | No collector with verified official release-time provenance | UNKNOWN / NOT REPAIRED |
| `india_bond_yields` | No validated official-source collector in this repair batch | UNKNOWN / NOT REPAIRED |
| `inflation_components` | No collector with component-level release timestamps | UNKNOWN / NOT REPAIRED |
| `fx_carry_and_cross_currency` | No validated paired rate/tenor source collector | UNKNOWN / NOT REPAIRED |
| `weather_agriculture` | No validated IMD/agriculture collector | UNKNOWN / NOT REPAIRED |
| `global_freight_shipping` | No validated freight index/route collector | UNKNOWN / NOT REPAIRED |
| `ipo_float_unlocks` | No validated exchange filing/float-unlock collector | UNKNOWN / NOT REPAIRED |
| `market_microstructure` | No complete per-symbol circuit/surveillance collector | UNKNOWN / NOT REPAIRED |
| `research_house_actions` | No validated publisher action collector | UNKNOWN / NOT REPAIRED |
| `earnings_revisions` | No point-in-time estimates/revisions collector | UNKNOWN / NOT REPAIRED |

### Required next gate sequence

1. Implement and unit-test each remaining collector against its real source response and required schema.
2. Run small live checks per source group and preserve response URL, publication/release time, query window, retrieval time, and symbol/ISIN validation where relevant.
3. Run the full source coverage audit; inspect `source_coverage.json`, `factor_coverage_audit.json`, and all collector manifests. Any missing or unvalidated group remains UNKNOWN and blocks release.
4. Only after source coverage clears, rerun the event study and score only matured H+1/H+3/H+5 outcomes; inspect event-level rows, exclusions, and window counts.
5. Run the hard gate and require explicit blocker-free report plus `candidate_release_allowed: true` before making a release claim.
6. Complete the final research paper with methods, evidence, matured results, failed-run ledger, limitations, and the hard-gate decision.

No full historical validation or new hard-gate PASS is claimed in this checkpoint. The Run #145 blocker remains unresolved until a new full-workflow artifact proves otherwise.


## Append-only checkpoint — 2026-10-26 — bounded run #40373908643

- Run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/40373908643
- Conclusion: SUCCESS; job `bounded-smoke` completed.
- Artifact check: the run returned no uploaded artifacts. Its console log is test evidence, not a substitute for a new full-workflow artifact bundle.
- Mocked tests: 10 factor-source tests passed; the bounded historical/manifest regression suite ran 37 tests and passed.
- Live-source smoke: Treasury yields 42 rows for 2Y/10Y/30Y (2026-10-05..2026-10-26); DXY 16 rows (2026-10-05..2026-10-26); Federal Reserve feed 20 entries; ECB feed 15 entries. This confirms bounded connectivity/schema only. DXY remains a third-party mirror; policy feed publication date remains explicitly a proxy, not a verified event date.
- Crucial regression evidence printed by the hard-gate audit inside the unit suite: `event_study_status=COMPUTED_EXPLORATORY_WITH_PENDING_EVENTS`, `event_study_total_event_rows=3`, `event_study_eligible_event_rows=0`, `event_study_window_rows=0`; blocker `EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS`; `candidate_release_allowed=false`. The test suite passes because it tests the defined fail-closed behavior; this is not a research/hard-gate PASS.
- The suite's temporary fixture showed one factor group and one regime window, so those figures must not be presented as full-history validation.
- No source-group coverage completion is claimed: 14 groups remain UNKNOWN / NOT REPAIRED, and the 4 implemented groups are still short of complete domain QA and full-registry integration.
- Required next action: repair real collectors for all remaining 14 groups, run the full workflow against the observed production dataset, upload its artifact bundle, inspect matured H+1/H+3/H+5 event-level rows and exclusions, and only then evaluate the final hard gate. The production selector, `RANKING_SCORE`, and frozen `+1 PRESSURE_FADE` must remain unchanged.
- Research paper status: NOT READY; do not finalize conclusions until the full historical artifact and blocker-free hard-gate report exist.
