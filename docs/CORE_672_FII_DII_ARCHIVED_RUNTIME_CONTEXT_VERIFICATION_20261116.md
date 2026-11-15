# CORE-672 FII/DII Archived Runtime Context Verification

Date: 2026-11-16  
Scope: read-only inspection of an existing successful collector artifact  
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Executive result

**PASS — a real archived `market_context.json` has now been located and verified.** This closes the previous artifact-discovery gap for one specific collector run and provides actual collector-shaped runtime evidence. It does NOT approve an aggregation formula, freshness threshold, or CORE-672 signal outcome.

## Run and artifact provenance

- Workflow: `.github/workflows/nse_collector.yml`
- Workflow ID: `373721663`
- Run #161; run ID: `43696699698`
- Event: `push`; branch: `main`
- Head commit: `cc4d397f25e735e9f7b63d2da74b40baff1aaab9`
- Run status/conclusion: `completed / success`
- Run started: `2026-11-15T08:54:51Z`
- Run updated/completed: `2026-11-15T09:01:03Z`
- Artifact ID: `14154408713`
- Artifact name: `precision-wires-adaptive-161`
- Artifact size: 61,626,954 bytes
- Artifact created: `2026-11-15T09:00:59Z`; not expired at inspection.
- Downloaded archive: `collector-run161.zip`
- Archive SHA-256 (independently recomputed): `b4623c28d30d04a73d21eb67662caeeab56123b2eba637d9eb652225df0305e8`
- ZIP entries: 25
- Context member: `data/context/market_context.json`, 5,973 bytes
- Context member SHA-256 (independently recomputed): `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`
- Exact `collector/context_data.py` at the run's head commit was fetched; blob SHA `f38e17979774d1439eea79e4dc7728ba92a790d1`, matching the previously inspected collector source.

## Actual context payload findings

- JSON parsed successfully.
- Top-level keys include `generated_at`, `sources`, `fii_dii`, `fii_dii_coverage`, market status, indices and geo-news.
- `generated_at`: `2026-11-15T08:59:46.921319+00:00`.
- `sources.fii_dii`: `NSE /api/fiidiiTradeReact (category-normalized)`.
- `fii_dii` row count: 2.
- Coverage metadata: rows=2, fii_rows=1, dii_rows=1, fii_dates=1, dii_dates=1.
- Both rows carry date-only observation `13-Nov-2026`; no intraday observation timestamp is present.
- DII row: buy 11745.95, sell 13999.53, net -2253.58.
- FII/FPI row: buy 18339.57, sell 12603.02, net 5736.55.
- Observed row keys are `category`, `group`, `date`, `buy_value`, `sell_value`, `net_value`; groups are `DII` and `FII_FPI`.
- No collector error keys were present.
- Structural checks: exactly one row per group/date in this payload; group keys recognized; net values parse as finite numeric values; both categories share one common observation date; no duplicate group/date pair detected.

## What this proves — and what it does not

**Proven for this run/artifact only:**
1. The successful collector workflow uploaded a real context JSON file.
2. The runtime payload matches the category-normalized schema expected from the collector source.
3. FII/FPI and DII rows are both present for 13-Nov-2026, with numeric net values.
4. `generated_at` is a file-generation timestamp and distinct from the date-only market observation.

**Not proven / still blocked:**
1. This single-date payload does not support a rolling-window test or a history-depth claim.
2. It does not establish the correct CORE-672 aggregation window, sign convention, units interpretation, missing-side rule, or maximum freshness age.
3. It does not justify changing the diagnostic's current `fii_net` / `dii_net` lookups.
4. No POSITIVE/NEGATIVE CORE-672 result is calculated or asserted.
5. No adapter, regression suite, or production change was made.
6. This artifact's presence does not prove every historical collector run retained context.

## Progress

- Successful collector run discovery: 100%.
- Artifact inventory and retrieval: 100%.
- ZIP SHA-256 verification: 100%.
- Context JSON extraction and SHA-256 verification: 100%.
- JSON/provenance/schema/row-level structural validation: 100% for this artifact.
- Runtime schema evidence: advanced from NOT_VERIFIED to VERIFIED_FOR_RUN_161_ONLY.
- Aggregation/freshness policy: BLOCKED.
- Research-only adapter implementation: 0% / NOT_STARTED.
- Focused regression execution: 0% / NOT_STARTED.
- CORE-672 semantic acceptance: BLOCKED.

## Scope protection

No production code, collector workflow, dataset, selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 definitions, engines A–E, default branch or PR state changed. No CI run dispatched, no PR merged, no paid API/spend.

## Next action

Prepare a small, research-only adapter contract test using this real archived payload as a provenance-pinned regression fixture (not synthetic market data), while retaining the unresolved aggregation/freshness decisions as explicit blockers. Implementation that emits any trading state must wait for approved aggregation policy.
