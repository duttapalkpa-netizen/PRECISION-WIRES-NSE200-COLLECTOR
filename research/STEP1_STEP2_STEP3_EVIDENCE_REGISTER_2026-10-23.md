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
| `crude_oil` | `data/external/brent_crude.csv` | FRED DCOILBRENTEU, explicitly labelled USD/barrel; DATE, CLOSE, source series/URL and observation provenance | NOT YET VERIFIED FROM LATEST COVERAGE ARTIFACT |
| `usd_inr` | `data/external/usd_inr.csv` | FRED DEXINUS, explicitly labelled INR per USD; DATE, CLOSE, source series/URL and observation provenance | NOT YET VERIFIED FROM LATEST COVERAGE ARTIFACT |
| `corporate_events` | `data/external/corporate_events.csv` | NSE filing-derived event rows with DATE, SYMBOL, EVENT_TYPE, PUBLISHED_AT, SOURCE_URL | NOT YET VERIFIED FROM LATEST COVERAGE ARTIFACT |
| `fpi_dii_flows` | `data/external/fpi_dii_flows.csv` | Successful official NSE response with correctly mapped DATE, GROUP, NET_VALUE; otherwise remain BLOCKED | NOT YET VERIFIED FROM LATEST COVERAGE ARTIFACT |

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
