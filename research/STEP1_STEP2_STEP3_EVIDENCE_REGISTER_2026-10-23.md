# Step 1–3 Evidence Register — 2026-10-23

Branch: `audit/prospective-selector-tracking`  
Purpose: artifact-backed audit trail before proceeding to Macro–Geo Step 4. This register does not change the production selector or ranking logic.

## Evidence ledger

| Step | Run ID / link | Commit SHA | Artifact ID / name | Artifact report and observed status | Blockers / qualifications | Verdict |
|---|---|---|---|---|---|---|
| Step 1 — NSE quarterly-results endpoint/schema | [Run 39977796193](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39977796193) | `868735622906047dba8433d19a5ba233d70df942` | `12513903105` / `step3-news-catalyst-join-audit` | `outputs/quarterly_results/quarterly_results_research_report.json`: `endpoint_schema_step_1.status=PASS`; all six endpoint/schema checks true. | `source_mode=ANNOUNCEMENT_FALLBACK`, `fallback_used=true`. This proves endpoint/schema readiness for the observed run, not uninterrupted primary-endpoint availability. | PASS WITH QUALIFICATION |
| Step 2 — quarterly source validation and financial-metric coverage | [Run 39946907057](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39946907057) | `fa493035fb8d822e4ca177f3d77a6b8dec942792` | `12498149846` / `step3-news-catalyst-join-audit` | Artifact reports `step_2_status=PASS`, source validation PASS; 500 disclosure rows, 457 verified metric rows, 43 superseded rows with later verified replacement, 0 blocked rows, 0 unknown-status rows. | Superseded rows are reconciled through later verified replacements; they are not 43 independently verified current metric rows. Metric coverage does not itself prove Macro–Geo P0 coverage. | PASS |
| Step 3 — news/catalyst join | [Run 39977796193](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39977796193) | `868735622906047dba8433d19a5ba233d70df942` | `12513903105` / `step3-news-catalyst-join-audit` | `outputs/news_24h/stock_news_24h_readiness.json`: `research_status=READY_FOR_PAIRED_ABLATION`; 10 unique cutoff-symbol pairs, unknown coverage 0, verified news 1, unverified news 0, timestamp failures 0, invalid article/query URLs 0, duplicate pairs 0. `stock_news_verification_report.json`: PASS. | Only 1 verified news row and 9 no-match GDELT query-window rows. No-match is not proof that no material news exists. Readiness is audit/paired-ablation readiness, not Macro–Geo hard-gate PASS or profitability evidence. | PASS WITH COVERAGE LIMITATION |

## Step 4 — four P0 groups to verify from the current repair design

The current `pipeline/macro_geo_repair_p0.py` explicitly targets these four groups. These are the exact repair targets; their current coverage status must be established from a fresh `outputs/macro_geo/p0_repair_report.json` and `outputs/macro_geo/source_coverage.json`, not inferred from the script.

| P0 source group | Expected file | Required evidence / fields | Current status in this register |
|---|---|---|---|
| `crude_oil` | `data/external/brent_crude.csv` | FRED DCOILBRENTEU, explicitly labelled USD/barrel; DATE, CLOSE, source series/URL and observation provenance | BLOCKED — latest artifact shows NOT_CONNECTED (0 rows) |
| `usd_inr` | `data/external/usd_inr.csv` | FRED DEXINUS, explicitly labelled INR per USD; DATE, CLOSE, source series/URL and observation provenance | BLOCKED — latest artifact shows NOT_CONNECTED (0 rows) |
| `corporate_events` | `data/external/corporate_events.csv` | NSE filing-derived event rows with DATE, SYMBOL, EVENT_TYPE, PUBLISHED_AT, SOURCE_URL | BLOCKED — latest artifact shows NOT_CONNECTED (0 rows) |
| `fpi_dii_flows` | `data/external/fpi_dii_flows.csv` | Successful official NSE response with correctly mapped DATE, GROUP, NET_VALUE; otherwise remain BLOCKED | BLOCKED — latest artifact shows NOT_CONNECTED (0 rows) |

## Hard-gate boundary

- The four groups above are repair targets, not assumed PASS states.
- Also check the full Macro–Geo P0 requirements in `pipeline/macro_geo_source_coverage.py`: `benchmark_index`, `sector_indices`, `volatility`, `crude_oil`, `usd_inr`, `fpi_dii_flows`, `corporate_events`, and `geopolitical_events`.
- The canonical event-study inputs `data/external/market_panel.csv` and `data/external/events.csv` must exist, pass schema/date/close validation, and yield an allowed event-study status with mature windows.
- Missing or stale evidence remains UNKNOWN/BLOCKED, never negative.
- Do not start Step 5/6 or release candidates until fresh coverage, event-study, panel-freshness and hard-gate artifacts prove the prerequisites.
- Invariants unchanged: production selector unchanged; `RANKING_SCORE` unchanged; frozen `+1 PRESSURE_FADE` unchanged; Run #58 frozen; no fabricated data; only matured H+1/H+3/H+5 outcomes may be scored.

## Artifact retrieval

Run 39977796193 → artifact `step3-news-catalyst-join-audit` (ID `12513903105`).  
Run 39946907057 → artifact `step3-news-catalyst-join-audit` (ID `12498149846`).

This ledger records evidence observed in those artifacts and explicitly marks Step 4 source coverage as pending fresh artifact inspection.


## Step 4 — latest real Macro–Geo artifact inspection (Run #61)

- Workflow: [Run #39808222731](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39808222731)
- Workflow conclusion: SUCCESS (job steps completed).
- Commit SHA: `83ea174ccf64f30ed42b45aadc65e93ca871c431`
- Artifact: `macro-geo-p0-event-study`, ID `12440940735`, ZIP size 653,590 bytes.
- Inspected reports: `outputs/macro_geo/source_coverage.json`, `outputs/macro_geo/p0_collection_manifest.json`, `outputs/macro_geo/event_study_report.json`, `outputs/macro_geo/factor_coverage_audit.json`, plus included CSVs.
- Overall inventory: `INVENTORY_COMPLETE_WITH_GAPS`; P0 coverage `P0_INCOMPLETE`, 4 of 8 required groups available.
- Event study: `COMPUTED_EXPLORATORY`; 4,114 panel rows, 11 series, 29 eligible event rows, 132 event-window rows. Exploratory status does not clear the P0 hard gate.

### Four requested repair targets — artifact evidence

| Source group | Actual status | Rows | Date range | Schema / provenance | Blocker |
|---|---|---:|---|---|---|
| `crude_oil` | `NOT_CONNECTED` | 0 | none | Expected `DATE,CLOSE`; no selected file or source URL. Manifest reports FRED `DCOILBRENTEU` timeout (2006-01-01..2010-12-30) and Yahoo Finance fallback HTTP 429. | No usable `data/external/brent_crude.csv`; source data absent. |
| `usd_inr` | `NOT_CONNECTED` | 0 | none | Expected `DATE,CLOSE`; no selected file or source URL. Manifest reports FRED `DEXINUS` timeout (2006-01-01..2010-12-30) and Yahoo Finance fallback HTTP 429. | No usable `data/external/usd_inr.csv`; source data absent. |
| `corporate_events` | `NOT_CONNECTED` | 0 | none | Expected `DATE,SYMBOL,EVENT_TYPE,PUBLISHED_AT,SOURCE_URL`; no selected file. | No usable normalized corporate-event file. Do not infer zero events. |
| `fpi_dii_flows` | `NOT_CONNECTED` | 0 | none | Expected `DATE,GROUP,NET_VALUE`; no selected file. | Official NSE response/schema mapping did not yield usable normalized data. Do not substitute estimates. |

### Other required P0 groups in the same artifact

| Source group | Status | Rows | Date range | Schema / provenance | Qualification |
|---|---|---:|---|---|---|
| `benchmark_index` | `AVAILABLE` | 374 | 2025-04-21 to 2026-10-22 | `DATE,SERIES,CLOSE,SOURCE,SOURCE_URL,OBSERVED_AT_UTC`; NSE daily index archive URLs retained. | Generic QA passed; point-in-time and calendar checks remain. |
| `sector_indices` | `AVAILABLE` | 3,366 | 2025-04-21 to 2026-10-22 | Same six columns; NSE archive URLs retained. | Generic QA passed; domain-level validation remains. |
| `volatility` | `AVAILABLE` | 374 | 2025-04-21 to 2026-10-22 | Same six columns; India VIX from NSE archive. | Global VIX separately BLOCKED (0 rows) in collection manifest. |
| `geopolitical_events` | `AVAILABLE` | 29 | 2026-10-21 to 2026-10-22 | `EVENT_DATE,PUBLISHED_AT,EVENT_TYPE,SOURCE,SOURCE_URL,CONFIDENCE`; RSS URLs and timestamps retained. | Generic QA only; manifest labels items `TRUSTED_PUBLISHER_RSS_MENTION_NOT_VERIFIED_EVENT`, so event occurrence is not independently confirmed. |

### Step 4 verdict

**BLOCKED — do not proceed to Step 5 or Step 6.** The four repair targets remain absent. `market_panel.csv` exists (4,114 rows, 11 series; 2025-04-21 to 2026-10-22) and `events.csv` exists (29 rows; event dates 2026-10-21 to 2026-10-22; publication timestamps 2026-10-21T03:58:16Z to 2026-10-22T15:56:36Z), permitting an exploratory event study only. The artifact's `event_study_report.json` says `COMPUTED_EXPLORATORY`; this does not override missing P0 sources. The strict `macro_geo_hard_gate.py` report must be separately inspected before any release decision.

Artifact: [Run #61 — Macro Geo P0 Collection and Event Study](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39808222731), artifact ID `12440940735`.

All missing values remain UNKNOWN/BLOCKED, never negative. Production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE`, and Run #58 remain unchanged.


## Step 4 — Run #62 fresh artifact verification (2026-10-23)

- Workflow: [Run #62 — Macro Geo P0 Collection and Event Study](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/39989970086)
- Run ID: `39989970086`; workflow run number: `62`; conclusion: `success`.
- Commit SHA: `4ca3fcb16e8f3424e44a232015e2bfbc1d5c16cb`.
- Artifact: `macro-geo-p0-event-study`, ID `12517254906`, size 654,061 bytes; SHA-256 `518447d63aa2cbda0589d2aa519b34886c0008db069ba80696fcb66f1833f283`.
- Artifact files inspected: `outputs/macro_geo/four_group_validation.json`, `source_coverage.json`, `p0_collection_manifest.json`, `event_study_report.json`, `factor_coverage_audit.json`, and the four target CSVs.

### Four requested groups — measured artifact results

| Group | Validation status | Rows | Date range | Schema | Provenance | Blocker / qualification |
|---|---|---:|---|---|---|---|
| `benchmark_index` | `AVAILABLE_VALIDATED` | 375 | 2025-04-21 to 2026-10-23 | `DATE,SERIES,CLOSE,SOURCE,SOURCE_URL,OBSERVED_AT_UTC` | 375/375 valid HTTP(S) source URLs; source value `NSE daily index close archive`; 375 valid observation timestamps | No blockers in strict four-group validator. Domain/calendar and point-in-time checks still needed. |
| `sector_indices` | `AVAILABLE_VALIDATED` | 3,375 | 2025-04-21 to 2026-10-23 | `DATE,SERIES,CLOSE,SOURCE,SOURCE_URL,OBSERVED_AT_UTC` | 3,375/3,375 valid HTTP(S) URLs; `NSE daily index close archive`; 3,375 valid observation timestamps | No blockers in strict validator. Domain/calendar and point-in-time checks still needed. |
| `volatility` | `AVAILABLE_VALIDATED` | 375 | 2025-04-21 to 2026-10-23 | `DATE,SERIES,CLOSE,SOURCE,SOURCE_URL,OBSERVED_AT_UTC` | 375/375 valid HTTP(S) URLs; `NSE daily index close archive`; 375 valid observation timestamps | India VIX is available; Global VIX remains separately BLOCKED (Yahoo 429 and FRED timeout). Do not treat India VIX as a replacement for Global VIX. |
| `geopolitical_events` | `AVAILABLE_VALIDATED` | 24 | 2026-10-22 to 2026-10-23 | `EVENT_DATE,PUBLISHED_AT,EVENT_TYPE,SOURCE,SOURCE_URL,CONFIDENCE` | 24/24 valid HTTP(S) URLs; sources Al Jazeera, BBC, Bloomberg; all publication timestamps valid | No schema/provenance blocker. These are publisher/RSS/GDELT media mentions with publication-date proxies, not independently verified event occurrences. GDELT had 429s; Reuters feed 404 and AP News 403. |

Strict validation artifact: `outputs/macro_geo/four_group_validation.json` → overall `PASS`, all four groups `AVAILABLE_VALIDATED`, blockers empty for each. Generic coverage artifact remains `INVENTORY_COMPLETE_WITH_GAPS`.

### Run #62 overall source/hard-gate decision

The four groups requested in this run are validated at schema/provenance level. **Step 4 as a whole remains BLOCKED** because other required P0 inputs are still missing:
- `crude_oil`: `NOT_CONNECTED`, 0 rows, no date range/file; FRED request failed and Yahoo returned HTTP 429.
- `usd_inr`: `NOT_CONNECTED`, 0 rows, no date range/file; FRED request failed and Yahoo returned HTTP 429.
- `corporate_events`: `NOT_CONNECTED`, 0 rows; NSE announcements endpoint returned HTTP 403.
- `fpi_dii_flows`: `NOT_CONNECTED`, 0 rows; NSE FPI/DII endpoint returned HTTP 403.
- Global VIX: blocked separately; Yahoo HTTP 429 and FRED timeout.
- Factor coverage audit: `FACTOR_COVERAGE_AUDITED_WITH_GAPS`, 35 factor groups, 0 fully available schema groups, 6 partial source coverage, 29 not connected.
- Event study: `COMPUTED_EXPLORATORY`, operational status PASS; 4,125 panel rows, 11 series, 24 event rows, 88 event-window rows. This is exploratory only, not a P0 hard-gate pass or causal evidence.
- Collection manifest: `PASS_WITH_CRITICAL_DATA_GAPS`; required-series availability is false because Brent crude and USD/INR are absent; corporate/FPI-DII remain UNKNOWN/BLOCKED.

**Decision:** four-group sub-validation PASS; Macro-Geo Step 4 overall BLOCKED. Do not proceed to Step 5/6 or release candidates until the remaining required sources are connected and a fresh artifact proves full coverage. Missing remains UNKNOWN, never negative.

Invariants remain unchanged: production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE`, and Run #58. No fabricated rows; only matured H+1/H+3/H+5 outcomes may be scored.
