# PRECISION-WIRES V11.3 — Continuation 18 checkpoint
Date: 2026-11-07
Page: গবেষণা যাচাই অব্যাহত 18

## Immutable architecture and operating constraints
- Production selector unchanged.
- RANKING_SCORE unchanged.
- +1 PRESSURE_FADE unchanged.
- CORE-672 unchanged: 56 steps × 12 filters = 672 diagnostic signals.
- UNKNOWN is neither PASS nor FAIL.
- No synthetic rows, fabricated timestamps, inferred missing vintages, unsupported source promotion, or hard-gate relaxation.
- Research spend ₹0; use free official sources only; no paid APIs, licences, subscriptions, or external contact without explicit approval.
- Preserve prior PASS artifacts, run IDs, commit SHAs, artifact IDs, and SHA-256 values. Do not repeat completed work.
- Final Hard Gate remains BLOCKED until all required evidence and matured validation are complete.

## Confirmed IIP 41-vintage audit state
- GitHub repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
- IIP branch: fix/iip-41-vintage-audit-clean
- Commit: 16f382aabf984eca403e85fb0c701e36a5a35370
- Run: 41640521553 (GitHub Actions job conclusion SUCCESS; this is not an IIP audit PASS).
- Artifact ID: 13232127900
- Artifact SHA-256: e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c
- Artifact revision_audit.json says audit_status=BLOCKED_WITH_GAPS and hard_gate=BLOCKED.
- Catalogue total 456 records across 46 pages; 41 qualifying catalogue rows; 40 unique qualifying vintage records after excluding one duplicate catalogue row; 40 manifest rows; 39 raw workbooks downloaded/cache-verified and parsed; 1 failed download; 0 parse failures.
- 125,220 parsed observations; 1,124 revision differences; revision comparison is correctly scoped to same base year + classification + NIC code + reference period.
- Expected missing reference period: 2026-01.
- April 2026 catalogue record IIPMFY26002APR returned HTTP 404. Its catalogue metadata still points to a filename denoting the old 2011-12 series, while the official April 2026 release is the new 2022-23 base / NIC-2025 series. Do not mark the native MoSPI workbook vintage PASS.
- This gives 39 parsed of 41 expected monthly periods (95.1% ingestion count only); it is not overall research completion.

## Work completed in continuation 18: official April 2026 source crosswalk
- Official PIB release PRID=2267531, posted 2026-06-01, explicitly identifies April 2026 as the first new IIP series release, base 2022-23; it includes Statements II-A to II-D with NIC-2025 detailed tables.
- Extracted 36 source rows: II-A 24, II-B 4, II-C 5, II-D 3. All marked QUICK_ESTIMATE, with source URL and PIB line references. Official published growth rates are retained; they are not recomputed from rounded index values.
- Crosswalk CSV path: data/macro/iip_apr2026_pib_statement_crosswalk.csv
- Crosswalk CSV SHA-256: 37772b90e136376ec4ed993eeafdb030d9a59debca7e1cf8ee4d6ecea1416811
- Audit JSON path: data/macro/iip_apr2026_pib_crosswalk_audit.json
- The crosswalk explicitly says it does NOT replace the missing native MoSPI XLSX; IIP audit and Hard Gate remain BLOCKED.
- GitHub commit adding CSV: 58b5588c1fd8e82132ec15521a66296b16279bce
- GitHub commit adding audit JSON: c35a250d3c3d6c38898e0172471c0fffde57d3ce
- Read-back QA on committed CSV: 16 columns, 36 data rows, statement counts 24/4/5/3, 0 duplicate statement/code pairs, 0 contract violations. Commit combined status currently has no status checks (no CI PASS claimed).

## Other known unresolved work
- 693 IIP-related candidate transitions: 431 unresolved; source-cell certification was not established; certified revisions previously reported as 0.
- Step 6 same-snapshot reconciliation was pending: CSV/JSON source coverage parity, Factor Registry/Macro-Series/Event Study/Hard-Gate hashes, immutable snapshot ID, and source_coverage_csv_json_statuses_match=true still require evidence.
- April 2026 XLSX provenance remains unresolved even though official PIB detailed tables are now crosswalked as separate evidence.
- Macro Evidence Snapshot v2 Run 41598327067 was reported PASS; artifact SHA-256 2712e15b423be987f0e2b59b13ec46544ce7774ee09a6c3b267e83433ff3a18c.
- IIP Run 41640521553 was reported PASS at workflow/job level, but its embedded audit remains BLOCKED_WITH_GAPS as detailed above.
- Run 41340507789 must not be described as a timestamp-parser PASS; the observed GitHub job failed at “Run India macro source contract tests”. Its artifact is source-coverage-status-regression, SHA-256 c7f1fd351e52bd2dacf975d963910c5aef83d7caa69169d8c3e3d3004f5bcd79.

## Progress reporting policy
- Do not present a guessed overall percentage. The last remembered overall baseline was 36%, but no complete current workstream denominator/reconciliation was available on 2026-11-07.
- Report workstream-specific ratios with their denominator and scope. For IIP ingestion, 39/41 = 95.1% of expected monthly periods parsed; the vintage audit remains BLOCKED.
- Next priority: repair the April 2026 MoSPI catalogue/XLSX provenance mismatch using the correct official 2022-23/NIC-2025 source, and preserve the PIB crosswalk only as supplemental evidence. Do not rerun the full 41-vintage workflow unless a targeted validation requires it.
