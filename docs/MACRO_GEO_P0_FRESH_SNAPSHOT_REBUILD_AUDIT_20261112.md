# Macro-Geo P0 fresh snapshot rebuild — audit record
**Date:** 2026-11-12  
**Workflow:** Macro Geo P0 fresh same-snapshot rebuild from verified NSE 200-session evidence  
**Branch:** \`audit/run145-factor-registry-gap-audit\`  
**Run:** \`43259234768\` — SUCCESS  
**Artifact:** \`13963926359\` — \`macro-geo-p0-fresh-snapshot-20261112\`  
**Artifact size:** 163,037,121 bytes  
**Artifact ZIP SHA-256:** \`bcc2cfafd25488160bfca68300de07ef06da9a94291083ec70e50445b48b1e02\`  
**Workflow duration:** 108 seconds; within the 10-minute operating limit.

## 1. Objective and provenance

The expired original Macro-Geo P0 cache key could not be restored. A newer/different NSE panel was not substituted into the old P0 snapshot. Instead, a fresh, explicitly versioned P0 rebuild was performed from a separately verified official NSE 200-session artifact.

Pinned upstream source:
- NSE source workflow run: \`43245527846\` — SUCCESS.
- NSE source artifact: \`13955899352\`, \`nse-200-session-cache-verification-331\`.
- GitHub artifact digest: \`sha256:1833c75c09c89e7610ad3fbdff62bbdf9a67737e2b39c1e4bf223bddc3a1e070\`.
- NSE snapshot ID: \`ee037b46aa2e8e7bce7df51919aada51418fd03787a1ed740a103f4b47804305\`.
- NSE source manifest SHA-256: \`ab37d0e14458aceaa13b7684e5739d9486c27e4b3f04d2667e1911abd568a17a\`.
- The workflow rechecked all 200 raw session files against the manifest: bytes, SHA-256, source URL, successful HTTP 200 response and retrieval timestamp. No raw source row was synthesized.

The canonical panel was rebuilt with the repository's existing \`collector/build_200_sessions.py\` implementation:
- Rows: 500,400.
- Symbols: 2,996.
- Unique sessions: 200.
- Window: 2026-01-21 through 2026-11-12.
- Panel SHA-256: \`91b320094baff93be9982564e5dc175203bc45cb7b03d59afc470bc049900122\`.
- Snapshot import status: \`PASS_EXACT_PINNED_OFFICIAL_NSE_EVIDENCE\`.
- Panel rebuild status: \`PASS_CANONICAL_PANEL_REBUILT_FROM_PINNED_RAW\`.

A deterministic composite snapshot fingerprint was independently calculated from the upstream NSE snapshot ID plus the exact downstream file-hash map:
\`2e57a4f1eae955c8d12793f024b1f2f076dfef68096889d7adb5911ba9371db6\`.
This is an audit fingerprint for this rebuild, not a replacement for the original NSE snapshot ID.

## 2. P0 rebuild outcome

P0 window: 2025-12-22 through 2026-11-12.

| Metric | Result |
|---|---:|
| Canonical NSE rows | 500,400 |
| Symbols | 2,996 |
| NSE sessions | 200 |
| Market-panel rows | 340 |
| Market-panel series | 12 |
| Accepted trusted-publisher event rows after deduplication | 22 |
| Source groups in inventory | 35 |
| Generic-available groups | 6 |
| Not connected groups | 29 |
| Factor groups | 35 |
| Fully available factor groups | 0 |
| Partial factor groups | 7 |
| Not-connected factor groups | 28 |
| Unmapped factor groups | 0 |

P0 group status:
- Available: benchmark index, sector indices, volatility, geopolitical publisher events (4/8).
- Crude oil: NOT_CONNECTED.
- USD/INR: NOT_CONNECTED.
- FPI/DII: insufficient historical coverage; 2 rows on one date only, one row per investor group.
- Corporate events: official NSE endpoint timed out; NOT_CONNECTED.

The index data is limited: each of the 11 Indian benchmark/sector/India-VIX series has 10 observations (2026-10-29 to 2026-11-12); GLOBAL VIX has 230 observations (2025-12-22 to 2026-11-11). The 340-row panel is therefore not a 200-session, fully populated market panel.

Event collection:
- 22 unique accepted rows came from three public publisher feeds: BBC 11, Al Jazeera 9, Bloomberg 3 accepted before deduplication.
- GDELT: 4/4 requests timed out.
- Reuters RSS: HTTP 404.
- AP RSS: HTTP 403.
- These are publisher publication timestamps, not independently verified event-occurrence timestamps. They are candidate/media evidence only and do not prove causality.

P0 collector status: \`PASS_WITH_CRITICAL_DATA_GAPS\`.  
Research status: \`READY_FOR_EXPLORATORY_EVENT_STUDY\`.  
Source coverage: \`INVENTORY_COMPLETE_WITH_GAPS\`; P0 coverage \`P0_INCOMPLETE\` (4/8).  
Factor Registry: \`FACTOR_COVERAGE_AUDITED_WITH_GAPS\`.  
Hard Gate: NOT CLEARED. Candidate release remains disallowed.

## 3. Output hashes

| File | SHA-256 |
|---|---|
| \`data/processed/nse_eq_200_sessions.csv\` | \`91b320094baff93be9982564e5dc175203bc45cb7b03d59afc470bc049900122\` |
| \`data/external/market_panel.csv\` | \`9314f22d35e655638fbe32cd0b8220386bde5b6a56a73e1118ae3524ade4b61c\` |
| \`data/external/events.csv\` | \`3dd5b8ff65450c562ad897e53e82b5e4c58017931d6ab47a8b0959e01d0b3635\` |
| \`outputs/macro_geo/p0_collection_manifest.json\` | \`8dcb33809a5e9f1f335a6bdd2048f55fa1ccb901b553c1bd76e7755266df69d8\` |
| \`outputs/macro_geo/source_coverage.json\` | \`be6790dbb0370088f98630e6b40b0d026a7c2bb5eb987e1624f77330ff8af166\` |
| \`outputs/macro_geo/source_coverage.csv\` | \`c2e640f267d6cafe237d4d27462ff674fb43be793324932ef5b4896a186254b7\` |
| \`outputs/macro_geo/factor_coverage_audit.json\` | \`e0be00a2b1d996c04d6a565d0cc085f9be7bb174a985cbbfea724e69f87212ed\` |
| \`outputs/macro_geo/p0_fresh_snapshot_rebuild_manifest.json\` | \`8c9606dda969563aa298d04d09b018c6da77ef20780008920d179877cd1b9de2\` |

## 4. Regression test and correction history

Final successful run executed 27 existing regression tests: **27/27 PASS**.

Failed diagnostic attempts are retained and are not counted as successful evidence:
- \`43258574046\`: escaped \`github.sha\` expression produced an invalid checkout refspec.
- \`43258838250\`: test command referenced a nonexistent test module; corrected to the existing Macro-Geo regression suites.
- \`43258942061\`: direct Python artifact download forwarded GitHub authorization through the storage redirect and received HTTP 401; replaced with \`gh run download\`.
- \`43259070374\`: escaped token/repository expressions caused bad credentials; corrected YAML expressions.
- \`43259089218\`: manifest assertion used \`successful_response.sha256\`; actual schema field is \`successful_response.response_sha256\`. Assertion corrected to the actual manifest contract.
- \`43259234768\`: final run SUCCESS; all workflow steps and artifact upload succeeded.

## 5. Acceptance boundary and next work

This task successfully restores a reproducible canonical NSE panel and creates a new P0 snapshot artifact. It does **not** complete the Macro-Geo P0 gate.

Next high-value remediation:
1. Connect crude oil using official FRED DCOILBRENTEU or EIA RBRTE Brent spot, with exact units, timestamps, window and freshness checks.
2. Connect USD/INR using a verified official source (the existing Federal Reserve H.10/BIS dual-source evidence is available for a separately audited integration; retain each source separately and preserve missing statuses).
3. Recover >=60 distinct FPI/DII dates spanning >=90 calendar days for each investor group from official NSE/NSDL sources.
4. Repair corporate-event ingestion from official NSE disclosures and preserve publication timestamps/attachment URLs.
5. Extend official Indian benchmark/sector index history beyond the 10-day subset; do not treat GLOBAL VIX as a substitute for India VIX or sector indices.
6. Re-run source coverage, 35-factor coverage, event-level H+1/H+3/H+5 maturity, historical-regime coverage and Hard Gate against this exact fresh snapshot.

## 6. Invariants

- Production selector unchanged.
- \`RANKING_SCORE\` unchanged.
- \`+1 PRESSURE_FADE\` unchanged.
- 672 diagnostics unchanged.
- No synthetic rows or timestamps; no source promotion from a proxy or media mention.
- ₹0 spend; free sources only.
- No PR merge; no production integration.
- UNKNOWN remains neither PASS nor FAIL.
