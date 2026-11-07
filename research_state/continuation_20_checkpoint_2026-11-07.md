# PRECISION-WIRES V11.3 — Continuation 20 checkpoint
Date: 2026-11-07
Page: গবেষণা যাচাই অব্যাহত 20
Branch: fix/iip-41-vintage-audit-clean

## Immutable architecture and constraints
- Production selector unchanged.
- RANKING_SCORE unchanged.
- +1 PRESSURE_FADE unchanged.
- CORE-672 unchanged: 56 steps × 12 filters = 672 diagnostic signals.
- UNKNOWN is neither PASS nor FAIL.
- No synthetic rows, fabricated timestamps, inferred missing source vintages, unsupported source promotion, or hard-gate relaxation.
- Research spend ₹0; free official sources only; no paid APIs/licences/subscriptions or external contact without explicit approval.
- Preserve previous PASS artifacts, run IDs, commit SHAs, artifact IDs, and SHA-256 values. Do not repeat completed work.
- Hard Gate remains BLOCKED until all evidence and matured validation criteria are complete.

## Previous IIP 41-vintage state — retained
- Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
- IIP branch: fix/iip-41-vintage-audit-clean
- Run 41640521553, workflow job success only; embedded audit status BLOCKED_WITH_GAPS.
- Artifact ID 13232127900; SHA-256 e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c.
- Catalogue 456 records / 46 pages; 41 qualifying rows; 40 unique qualifying vintage records; 40 manifest rows; 39 parsed workbooks; 1 failed download; 0 parse failures; 125,220 observations; 1,124 revision differences.
- 39/41 monthly periods parsed = 95.1% ingestion count only, not audit completion.
- 693 candidate transitions: 431 unresolved; source-cell certification not established.
- Step 6 same-snapshot reconciliation remains pending.
- Initial 2026-06-01 PIB crosswalk remains separate supplemental evidence only; it represents the superseded WPI-based release.

## Continuation 19/20: official API recovery — completed evidence
1. Official e-Sankhyiki OpenAPI YAML was successfully fetched by GitHub Actions despite application/octet-stream content type. SHA-256: bed83ff75c1b361368019a55473ed29c9fcd7242651706cffea04debb65211e0.
2. Contract confirms production server https://api.mospi.gov.in/, GET /api/iip/getIIPData, and parameters frequency, base_year, year, month_code, type, category_code, subcategory_code, limit, page, viz_req. base_year description explicitly lists 2022-23.
3. Fixed audit false-negative: it previously looked for 2022-23 only in enum/default and missed the official parameter description. New contract audit run 42367367533 succeeded.
4. Official API request for April 2026:
   - GET https://api.mospi.gov.in/api/iip/getIIPData?frequency=Monthly&base_year=2022-23&year=2026&month_code=4&type=All&viz_req=true
   - HTTP 200; content type application/json; 43 records returned; 1 General + 36 Sectoral + 6 Use-based.
   - Retrieved 2026-11-07T11:19:49.576191Z.
   - Raw response SHA-256 ba0ee42f7fb7809483a86dcbfe53057d401c51af67e28638c6603fcedcdca71a.
5. Direct April validation against latest official IIP PIB release PRID 2329475 (2026-10-28): 43/43 rows match, 0 missing, 0 mismatches, 0 unexpected, 0 duplicates. Benchmarks: Statement I April column, Statement III April row, Statement IV April-2026 NIC-2025/sub-sector rows.
6. Independent May cross-check against the same latest release: 43/43 rows match. Raw May response SHA-256 0ca8a461028c2794da4683930805a6a2cfd95ba77a6eb0ae7519b9cb32c741db.
7. PPI identity: PIB PRID 2278961 (2026-06-29) explicitly states the entire 2022-23 IIP series was revised with Output PPI, superseding the earlier WPI-based 2022-23 series, with updated source-agency data from April 2022. Direct April 43/43 and May 43/43 matches to latest official release corroborate that the current API endpoint returns the current revised series. API rows themselves do not carry a deflator field; provenance relies on the official series-level notice plus exact row matches.
8. Important distinction: official JSON API source is recovered and validated; native catalogue XLSX is NOT recovered. Do not claim XLSX recovery. API evidence is separate and does not silently replace the native XLSX acceptance requirement.

## Durable outputs and identifiers
- CSV: data/macro/iip_apr2026_mospi_api_records.csv
  - 43 rows, 8 columns.
  - SHA-256 192267b76af8cc0bc524d33a86461d0d70906a96a34eadfdccea12b2245a82ee
  - Commit 198ad7bccf5d6f634e0f0af6a5868119369f1921
- Validation JSON: data/macro/iip_apr2026_mospi_api_validation.json
  - Commit 6b0bd934152fb83fb258fc6a3ffce29f4dce4f86
  - Contains API request provenance, response hash, 43/43 official release cross-check, PPI series evidence, and hard-gate caveat.
- Successful workflow run 42367705456 (run #10), job PASS; artifact ID 13572745125; artifact zip SHA-256 01c5b8d28fff2049cc3e706b01cb841da550bbdbc40acf58a3f461eae58c6ecc; artifact retention 90 days.
- API contract audit run 42367367533 succeeded; artifact ID 13571339650; artifact zip SHA-256 2efadcee518fc2deff6db37361491b08e3c29d26683c7f361958fb90ba3cf9f1.
- Failed intermediate attempts were diagnosed and retained in Actions history:
  - Run 42367288017 failed because contract script did not read base-year parameter descriptions.
  - Run 42367332782 failed due malformed escaped newline syntax in patch.
  - Run 42367414826 failed because runner TLS required legacy renegotiation compatibility.
  - After scoped TLS compatibility (certificate verification remained enabled), April API query succeeded in run 42367451621.
  - Run 42367573000 and 42367604833 were failed May cross-check attempts: first key normalization, then missing normalized-map initialization; no source data mismatch was implied.
  - Run 42367705456 succeeded with May 43/43 match and artifact capture.
- Do not rerun these successful API queries unless a specific validation requires it.

## Remaining blockers and next priorities
- Native April 2026 MoSPI catalogue XLSX provenance still unresolved; API JSON is not the native workbook.
- IIP 41-vintage audit remains BLOCKED_WITH_GAPS.
- 693 candidate transitions source-cell certification remains incomplete (431 unresolved).
- Step 6 same-snapshot reconciliation remains pending.
- Macro evidence snapshot, factor registry and event-study matured validation must be reconciled before final Hard Gate.
- Do not repeat completed API extraction or the 43-row validation.

## Progress reporting policy
- Do not invent an overall percentage. Last remembered overall baseline was 36%; no complete denominator/reconciliation has yet re-certified it.
- Report scoped ratios: April API extraction 43/43 rows; April latest-PIB validation 43/43; May latest-PIB validation 43/43; IIP monthly workbook ingestion 39/41 = 95.1% only.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 remain untouched.
