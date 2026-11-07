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


- Final bounded dual-month API reconciliation: workflow Run 42381121341 (#12), commit `5f079524dfa7e1210005e46020fd9b6e109401e2`, all steps PASS. Artifact ID `13577128037`, SHA-256 `2337b9ed18d0057cac3a4c503a6d0657f0750df720f5a50878f14b3fc67d5059`.
- Run #12 validated April API 43/43 and May API 43/43 against PIB PRID=2329475 (28-Oct-2026), i.e. all 86 month-record comparisons PASS; each month has 0 missing, 0 mismatch, 0 unexpected, 0 duplicate. April raw API response SHA-256 remains `ba0ee42f7fb7809483a86dcbfe53057d401c51af67e28638c6603fcedcdca71a`. The same 8,129-byte official JSON response contained 43 April records, HTTP 200.
- Latest official PIB reference: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475 (28-Oct-2026). It explicitly states base 2022-23 and revision policy (lines 70-79); Statement I April values line 109, Statement III April values line 197, and Statement IV April-26 manufacturing/sector/sub-sector/general values lines 220-260. API index values were compared at one decimal; no growth rates were recomputed.
- Run #11 (42381063918) also completed PASS for the API contract + April retrieval + May reconciliation after comment/provenance cleanup. It was an automated push-triggered duplicate check; Run #12 is the final expanded audit including April-vs-latest-PIB comparison.
- Conclusion: API April and May data identity for base 2022-23 are now independently matched to the latest official PIB revised values. This resolves the April catalogue dead-link as a data-access path via official API, but does NOT recover the native catalogue XLSX or certify its file provenance. Keep the original missing XLSX issue visible; keep 41-vintage audit status BLOCKED_WITH_GAPS and Hard Gate BLOCKED.

## Other known unresolved work
- 693 IIP-related candidate transitions: 431 unresolved; source-cell certification was not established; certified revisions previously reported as 0.
- Step 6 same-snapshot reconciliation was pending: CSV/JSON source coverage parity, Factor Registry/Macro-Series/Event Study/Hard-Gate hashes, immutable snapshot ID, and source_coverage_csv_json_statuses_match=true still require evidence.
- April 2026 XLSX provenance remains unresolved even though official PIB detailed tables are now crosswalked as separate evidence.
- Macro Evidence Snapshot v2 Run 41598327067 was reported PASS; artifact SHA-256 2712e15b423be987f0e2b59b13ec46544ce7774ee09a6c3b267e83433ff3a18c.
- IIP Run 41640521553 was reported PASS at workflow/job level, but its embedded audit remains BLOCKED_WITH_GAPS as detailed above.
- Run 41340507789 must not be described as a timestamp-parser PASS; the observed GitHub job failed at “Run India macro source contract tests”. Its artifact is source-coverage-status-regression, SHA-256 c7f1fd351e52bd2dacf975d963910c5aef83d7caa69169d8c3e3d3004f5bcd79.


## Continuation 18 — official e-Sankhyiki API recovery and validation (2026-11-07)
- Official API OpenAPI contract was fetched and inspected from the e-Sankhyiki API. The `getIIPData` operation explicitly documents `base_year` choices including 2022-23, `frequency` Monthly, `year`, `month_code` and `viz_req` (full filtered dataset). Optional bearer token is documented; guest access was accepted by the live API request.
- Audit script correction: the first check incorrectly searched only enum/default and missed the documented 2022-23 description. It was corrected to inspect the parameter description. Successful contract audit: Run 42367367533 (workflow run #3).
- API TLS issue: initial query failed with `UNSAFE_LEGACY_RENEGOTIATION_DISABLED`. A narrowly scoped TLS compatibility context was added using system trust/certificate verification (verification remains ON); legacy renegotiation is permitted only for this endpoint compatibility. Do not disable certificate verification.
- Successful April 2026 API query: workflow Run 42367451621 (#5), job PASS. Endpoint:
  `https://api.mospi.gov.in/api/iip/getIIPData?frequency=Monthly&base_year=2022-23&year=2026&month_code=4&type=All&viz_req=true`
  HTTP 200; `application/json`; 8,129 bytes; 43 records; 0 invalid filter rows; 0 missing expected fields; 11 categories across General, Sectoral, Use-based. Retrieved 2026-11-07T11:16:14Z. Raw response SHA-256 `ba0ee42f7fb7809483a86dcbfe53057d401c51af67e28638c6603fcedcdca71a`. This is separate API evidence; it does not establish the missing native XLSX.
- April API audit remains `PASS_FILTERED_OFFICIAL_API_ROWS_RETURNED_SOURCE_VINTAGE_RECONCILIATION_PENDING`. Its response record schema does not itself name the deflator/release vintage. Do not assert native XLSX recovered or April source-vintage fully certified.
- May 2026 API cross-check: successful Run 42367705456 (workflow run #10), commit `167cc621c1587aaf9aba4fdc4c3df9ca7c937383`, job PASS. It fetched all 43 May-2026 API rows (base 2022-23) and matched all 43 against the latest official PIB release PRID=2329475 posted 2026-10-28 (not the superseded 2026-06-29 quick-estimate values). Results: 43/43 matched; missing 0; mismatches 0; unexpected 0; duplicates 0. Official release lines 70-79 explain base 2022-23 and revision policy; lines 96-103 identify NIC-2025 tables and e-Sankhyiki; Statements II-A to II-D and III/IV contain the detailed values.
- Run #10 artifact ID `13572745125`, SHA-256 `01c5b8d28fff2049cc3e706b01cb841da550bbdbc40acf58a3f461eae58c6ecc`. It includes official API contract, April API raw response/audit, and May-vs-PIB cross-check raw response/audit.
- API query evidence is now a validated supplemental path for April/May 2026; it is not a substitute for catalogue-native XLSX or for full vintage revision audit. Preserve old 41-vintage artifact and its BLOCKED_WITH_GAPS status.
- Workflow runs #7-#9 exposed script defects (case normalization / variable insertion), fixed in the subsequent run. Do not cite those failed runs as PASS. Run #10 is the verified end-to-end PASS.
- Latest outstanding tasks remain: native April 2026 XLSX/catalogue provenance; 693 candidate transitions (431 unresolved); source-cell certification; Step 6 same-snapshot reconciliation. Hard Gate remains BLOCKED.

## Progress reporting policy
- Do not present a guessed overall percentage. The last remembered overall baseline was 36%, but no complete current workstream denominator/reconciliation was available on 2026-11-07.
- Report workstream-specific ratios with their denominator and scope. For IIP ingestion, 39/41 = 95.1% of expected monthly periods parsed; the vintage audit remains BLOCKED.
- Next priority: repair the April 2026 MoSPI catalogue/XLSX provenance mismatch using the correct official 2022-23/NIC-2025 source, and preserve the PIB crosswalk only as supplemental evidence. Do not rerun the full 41-vintage workflow unless a targeted validation requires it.


## IIP cell-level revision certification — Batch 001 completed (2026-11-07)
- Used existing Run 41640521553 artifact ID 13232127900 (SHA-256 e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c); no recollection/re-download/re-run of the original 41-vintage collection was performed.
- Extracted the two exact source workbooks from that immutable artifact and independently recomputed their SHA-256:
  - IIPMFY23049APR QUICK workbook: 7cff38f066509e007c980a4267fd1753aa1fcae560438ad3df424d78d49ec30e
  - IIPMFY23054MAY FIRST_REVISION workbook: 6530370f75fa24997f98b760f336b70533a058e1a0a0f464bf1c26a10985425a
- Ran the existing bounded pipeline/audit_iip_cell_level_revision_batch_001.py logic against those exact files; all nine pre-specified April-2023 NIC-2008 rows matched both official PIB statements and both source XLSX cell values. 18/18 workbook cell matches; 18/18 official statement value matches; 9/9 transitions certified; zero mismatches.
- Verified source cells on sheet NIC 2d, sectoral monthly: previous/current cell pairs EF7, EF8, EF10, EF11, EF12, EF13, EF14, EF16, EF17. Values respectively: 135.2->136.1; 106.8->106.7; 106.9->106.8; 91.8->91.7; 99.5->97.8; 89.3->89.6; 79.4->80.6; 128.9->128.8; 126.9->126.2.
- PIB sources: PRID 1931708 (2023-06-12, Quick Estimates, Statement II) and PRID 1938974 (2023-07-12, April-2023 first revision in Statement IV). Official search results confirmed the release stages and values.
- Committed evidence:
  - data/macro/IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv, commit d22d36a534a57c465598a44f600730492a884d6c, GitHub blob SHA f93044e17d65b9d762ed7adf8b5673760189ff2c, SHA-256 40644baabc0273b0011cedf9eeaab765af48fac91340e5f07da810d4af25024b.
  - data/macro/IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json, commit 6cedbab197dd9ed15aadc8fd1c45596d7b3ce5c2, GitHub blob SHA 0be4a0f4c1fc2825b4900621f2acfe91dba23097, SHA-256 7e2d8a468e1946bae9bf7986bf123313f2b3f24a76e1785ad108136d749a4d7e.
- Candidate accounting after this batch: 9 certified; 684 policy-aligned candidates still NOT certified; 431 historical-panel/out-of-window transitions unresolved; 1,124 total observed differences. The remaining 1,115 are untouched by this batch. No extrapolation.
- Batch task progress: 100% (source artifact verification, 9 row source matching, CSV/JSON output, repository read-back). Overall research progress remains last defensible baseline 36%; no new whole-project denominator/reconciliation, so do not invent an updated percentage.
- IIP 41-vintage audit remains BLOCKED_WITH_GAPS; overall Hard Gate remains BLOCKED. Native April-2026 PPI XLSX provenance remains unresolved. The 86 April/May 2026 API-vs-PIB matches from Run #12 are supplemental and distinct.
- No production logic, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 components changed.


## Continuation 18 — Next-Day Performance Radar integration hardening (2026-11-07)
- The Radar is an integral supplemental V11.3 output, not a separate project. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, risk modifier and Hard Gate are unchanged.
- Exact official NSE CM UDiFF Bhavcopy for 2026-11-06 was recovered from Library path `/PRECISION-WIRES V11.3/NSE Data/2026-11-06/BhavCopy_NSE_CM_0_0_0_20261106_F_0000.csv.zip`; ZIP 208,064 bytes, SHA-256 `339e3f07bb00acb27d0200ea5bfa748de71d9b3f779b956d1069f2168c8c9904`. It contains 3,715 rows overall and 2,746 unique EQ symbols. UDiFF file has no delivery quantity/percentage; delivery is excluded, never carried forward or synthesized.
- The 6-Nov Radar output is a separate reproducible artifact; CSV SHA-256 `54a6ca0d5e0e682a5898a80c9a9bb20d92fbd1f589189a8c748b85d188b735ab`, summary JSON SHA-256 `fe74f9654c7ca40edf01c294c8a750f7a86519b9f85917c2c10885fe146a657a`, ZIP SHA-256 `b126cd6310afea4eb197300d8709f0353d8334e9ed40e2b56318396c9f23ee0e`. Forecast cutoff 2026-11-06; next session target 2026-11-09. 2,746 official EQ symbols total; 2,690 with >=20 sessions; 56 remain UNKNOWN_INSUFFICIENT_HISTORY. 805 positive setup, 233 negative setup, 1,652 neutral/unclear. Probabilities are intrahorizon HIGH-touch estimates, not guaranteed close-to-close returns.
- Independent chronological holdout had 71,259 symbol-session rows (test begins 2026-09-24); Brier/ECE: P5_H1 0.0844485/0.0125657; P10_H3 0.0575061/0.0011155; P20_H5 0.0181407/0.0032928. This validation is separate from current candidate ranking.
- Added `pipeline/next_day_performance_radar.py` and inserted it after final selection in `.github/workflows/nse_collector.yml`; intended scheduled execution 19:00 IST weekdays. Note: GitHub scheduled workflows execute only from the default branch. This schedule is NOT active until the integration PR is merged to main; do not claim daily automation is live yet.
- Important correction from code review: previous runner only read `data/processed/nse_eq_200_sessions.csv`, so a partial latest session could under-cover the official universe. Hardened it to require the latest normalized official daily file `data/raw/sec_bhavdata_full_DDMMYYYY.csv`, verify one matching source date, EQ-only rows >=1000, unique nonblank symbols, positive OHLC, valid high/low/close bounds, nonnegative quantity, replace any same-date partial processed panel, verify eligible >=20-session coverage, and record normalized raw-file SHA-256. If delivery fields absent, retain NaN and exclude delivery from probability features.
- Static QA workflow strengthened to assert raw-source completeness/fail-closed checks and immutable architecture flags. Latest static QA Run `42384225804` was observed with all test steps completed successfully; post-job cleanup was still running at last poll. Prior static QA Run `42384198549` conclusion SUCCESS, but it preceded the last eligible-history denominator correction; Run `42384225804` covers that correction plus strengthened assertions.
- Latest commits: Radar source hardening `291804be0e21c65f7689063aa8e3ae3314e1b22c`; eligible-history denominator correction `e41634f7c2f77d1fa3fc453743f0908fec1da44b`; strengthened static QA `5fdf9e16d324e08ad7673917ba90f34e6c424a56`.
- Full scheduled end-to-end run has NOT yet been performed. It requires collector + build + 200 sessions and exceeds the user's preference for very short runs; use a bounded separate manual QA harness before the first scheduled production-style run. The static QA does not prove runtime artifact generation.
- Do not re-run the 6-Nov one-off Radar or repeat source recovery. Next priority: validate the hardened runner against a preserved full 6-Nov daily file + 200-session history in a bounded workflow (<=10 min), upload artifact, compare raw count/hash and output symbol count, then prepare a small isolated PR or update the existing draft integration PR. Keep the schedule inactive until main branch integration is approved.
- Overall project percentage remains at last authoritative baseline 36%; do not recalculate without a reconciled denominator. Radar component status: standalone 6-Nov forecast 100%; code integration 100%; raw-feed fail-closed static checks pending final workflow completion; automated daily end-to-end validation 0%; Hard Gate unchanged BLOCKED.

- Final strengthened static QA Run `42384225804` completed SUCCESS on commit `5fdf9e16d324e08ad7673917ba90f34e6c424a56`; Python compile, immutable architecture checks, latest official raw daily file checks, duplicate/date/OHLC checks, fail-closed floor and eligible-history coverage assertions all passed. This remains static/code QA only, not a runtime end-to-end artifact PASS.
- Checkpoint update commit containing this addendum: pending read-back verification.
