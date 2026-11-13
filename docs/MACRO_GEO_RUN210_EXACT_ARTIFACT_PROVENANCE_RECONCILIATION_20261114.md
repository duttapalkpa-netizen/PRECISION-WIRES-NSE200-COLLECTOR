# Macro-Geo P0 Run 210 — Exact Artifact Provenance Reconciliation
Date: 2026-11-14

## Retrieval identity and integrity
- Run ID: `40898379422` (Macro-Geo P0 Run #210)
- Job: `macro-geo-p0`; conclusion: SUCCESS
- Artifact ID: `12908992135`; name: `macro-geo-p0-event-study`
- ZIP size: 96,946 bytes
- Downloaded ZIP SHA-256: `8c2de588aaf79697578a1343f7c88c9fd9bd383cbd6e2866d51e97eb5fadcb48`
- Artifact contains 35 files; ZIP listing and payload were inspected locally.

## Brent canonical-vs-proxy reconciliation
The archived payload resolves the original same-path overwrite defect for this run's canonical data:
- `data/external/brent_crude.csv`: 213 rows, 2025-12-22 through 2026-10-26; source identity is US EIA RBRTE daily Brent spot (official XLS), source series RBRTE, units USD/barrel; SHA-256 `203b886a538a18c4631b4d21f4a91d44f0bdf41986ef026ea7e9d800cf3810b8`.
- `p0_repair_report.json` identifies the same canonical path, source, row count, date range and EIA URL `https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls`.
- `crude_oil_collection_report.json` independently identifies Yahoo `BZ=F` as a proxy and reports its intended path as `data/external/brent_crude_futures_proxy.csv`, 212 rows, 2025-12-22 through 2026-10-26, explicitly not equivalent to spot.
- The ZIP does not contain `data/external/brent_crude_futures_proxy.csv`. Therefore the canonical EIA spot was not overwritten in this artifact, but the separate proxy payload's inclusion/retention is NOT VERIFIED. Do not claim the proxy file was archived.
- The artifact's manifest still describes the crude front-month series as BLOCKED for the longer window because the primary FRED and Yahoo attempts failed earlier in the P0 manifest path; the later repair report's EIA secondary is explicitly AVAILABLE_SECONDARY. Preserve these distinct stage statuses rather than flattening them into a single PASS.

## Hard-gate and research status from the exact artifact
- Hard gate: BLOCKED; candidate release not allowed.
- P0: 7/8; corporate_events BLOCKED (0 valid official rows with symbol, subject, publication timestamp and source URL).
- Factor Registry: 35 groups audited; 0 fully available; 21 not connected.
- Event study: 48 event rows, 26 eligible, 22 pending; 81 window rows; 26 events mature H+1 and 23 mature H+5. Status exploratory with pending events, not a production acceptance.
- Historical regime coverage: 9 of 11 anchors have windows; coverage incomplete.
- FPI/DII: 101 FPI and 100 DII distinct dates over 147 calendar days; this is collection coverage, not a full registry or all-calendar validation.
- Market/equity panel both end 2026-10-26; 0 calendar-day difference; invalid market-close rows 0.
- Hard-gate report explicitly confirms Production Selector, RANKING_SCORE and +1 PRESSURE_FADE unchanged; missing-data semantics UNKNOWN/BLOCKED.

## Acceptance
| Check | Result |
|---|---|
| Run/artifact retrieval and ZIP SHA | PASS |
| Canonical EIA Brent file vs repair report identity/rows/date range/URL | PASS |
| Yahoo futures clearly separated from canonical spot path | PASS for report/path metadata |
| Separate Yahoo proxy CSV actually present in artifact | UNKNOWN / NOT INCLUDED |
| Corporate events P0 | BLOCKED |
| Factor Registry 35/35 | BLOCKED (0 fully available) |
| Historical regimes 11/11 | BLOCKED (9/11) |
| Event study maturity | PARTIAL / EXPLORATORY |
| Overall Hard Gate | BLOCKED |

## Safety and next work
No code changes, workflow reruns, imputation, paid APIs, external contact, PR, merge or production integration. Protected invariants remain untouched. The next highest-value source task is Corporate Events P0, since it is the explicit missing eighth P0 group and currently prevents P0 completeness. The Yahoo proxy archive omission should be logged as a separate packaging/retention question, not mistaken for a canonical spot overwrite.
