# CPI 2024 Back-Series — Screenshot Provenance Reconciliation
Audit date: 2026-11-11 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1
Scope: evidence-only reconciliation; no observation changes and no registry promotion.

## Evidence recovered from the user's Library
The following original Chrome screenshots were found in the Library, materialized without modification, and SHA-256 hashed:

| Screenshot | Library created_at (UTC) | SHA-256 | What it establishes |
|---|---|---|---|
| Screenshot_20261111_000523_Chrome.jpg | 2026-11-10T18:36:01Z | d39975309d635b3a86348c910ee0bb8a3e648aa044d456b0a85c96dd4d91191b | e-Sankhyiki Macro Indicators landing page; CPI product is available |
| Screenshot_20261111_000723_Chrome.jpg | 2026-11-10T18:37:38Z | cbcd09f8923e71325f2145649314fe44bc725075183d1702243d7fab1710a9b1 | CPI table default Current series, base year 2024; 1,445,316 records before narrowing |
| Screenshot_20261111_001333_Chrome.jpg | 2026-11-10T18:43:45Z | 017f1f72c4f81dc64f7a7fb70b7f5b0717c329a5ff8748df5e7177ff31742ec9 | Base Year 2024; Series dropdown shows Current and Back choices; Rural/Urban/Combined sector and CPI (General) division visible |
| Screenshot_20261111_002059_Chrome.jpg | 2026-11-10T18:51:15Z | 18e94e74cf84f23ca545a93443218cba6ce312202c2313316d9ffdf8aa44c127 | Selected Base Year 2024, Series Back, State All India, Sector Rural/Urban/Combined, Division CPI (General); table shows 20 of 432 records and monthly rows across the three sectors |

Important timestamp distinction: Library created_at is the screenshot upload/Library-ingestion time, not proof of the original browser download time. The screenshot filenames encode local capture clock values, but those filenames are not treated as authoritative timestamps without device metadata. No browser download history, network log, or exact request URL was recovered.

## Reconciliation against the immutable workbook
- Workbook: cpi_2479.xlsx
- Raw SHA-256: 1779d670323982833f3f0668fee9b5f959dbe93f481571c17ab7a1b44a2ddbc0
- Workbook scope already QA-verified: Base Year 2024, Back series, All India, CPI (General), Rural/Urban/Combined; 432 monthly index records for 2013-01..2024-12 and 396 inflation records for 2014-01..2024-12.
- Screenshot filter configuration is now independently evidenced by the original UI screenshots and is consistent with the workbook scope.

## What is and is not closed
- Selected product and filter configuration: VERIFIED from screenshots.
- 432-row visible table count: VERIFIED from screenshot.
- Exact download URL: UNKNOWN (not visible in screenshots; no browser history/network log).
- Formal table/dataset ID: NOT_APPLICABLE_TO_THE_VISIBLE_MACRO-INDICATOR_TABLE_VIEW / UNKNOWN_FOR_ANY_UNDERLYING_API_RESOURCE. Do not invent a catalogue table ID; catalogue table IDs belong to separate released-statement records.
- Original workbook retrieval timestamp: UNKNOWN. Library upload timestamps and screenshot filename clock values must not be substituted.
- Raw workbook hash and prior structural QA: unchanged and PASS.
- Normalized panel: unchanged, 828 rows, all quality_status UNKNOWN pending provenance; no rows rewritten.
- Factor Registry admission: remains BLOCKED / UNKNOWN_PENDING_PROVENANCE.
- Active overlay ingestion: NOT DONE.

## Official source context
The official CPI Macro Indicators page documents a public paginated GET /api/cpi/getCPIData endpoint, guest access without a bearer token, and rate limits. The portal's FAQ states filtered Macro Indicators datasets can be downloaded as CSV. These pages prove an official public data route exists; they do not prove that this particular XLSX was downloaded from that API or provide its request parameters/response timestamp. Do not retrospectively relabel the XLSX as an API response.

## Next bounded acceptance action
If the original Chrome download history or download details are available on the user's device, capture the entry for cpi_2479.xlsx showing full source URL and download time/timezone. Otherwise retain UNKNOWN and, if useful, create a separate new reproducible API acquisition with its own request log, raw response, UTC retrieval timestamp, and SHA-256. Never retrofit new API evidence onto the old workbook.

## Safety invariants
Research-only. No synthetic observations, no fabricated timestamps, no guessed IDs, no forward-fill, no paid APIs/services, no production selector/RANKING_SCORE/+1 PRESSURE_FADE/CORE-672/Engines A-E/Hard Gate changes, no PR merge, and no production integration. UNKNOWN is neither PASS nor FAIL.
