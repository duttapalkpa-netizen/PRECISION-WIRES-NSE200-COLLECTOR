# IIP monthly catalogue coverage reconciliation — 2026-11-07

## Immutable input and method
- Source: preserved GitHub Actions Run 41640521553, Artifact ID 13232127900.
- Original artifact ZIP SHA-256: `e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c`.
- Re-downloaded artifact and independently rechecked the ZIP SHA-256 against the retained digest before inspection.
- Reconciled every row of `vintage_ingestion_manifest.csv` against a complete calendar-month sequence from 2023-04 through 2026-08.
- No new data acquisition, inferred table ID, or synthetic observation was used.

## Reconciled counts
- Calendar span: 2023-04 to 2026-08 inclusive = 41 months.
- Unique catalogue manifest records: 40.
- Successfully downloaded and parsed XLSX vintages: 39.
- Catalogued April 2026 table: 1, HTTP 404, not parsed.
- Month absent from the catalogue manifest: January 2026 (no table ID inferred).
- Therefore, the manifest has 40/41 months represented; 39/41 parsed source vintages. These are period-coverage counts only, not observation-level or cell-certification rates.

## Series boundary
- 35 parsed vintages from April 2023 through March 2026: base year 2011-12, NIC-2008.
- April 2026: unresolved 404 catalogue record; no base year/classification assigned from the failed workbook.
- Four parsed vintages from May through August 2026: base year 2022-23, NIC-2025.
- The June 29, 2026 official Output-PPI series supersedes the earlier WPI-based new series. Preserve methodology vintage labels; do not concatenate series levels or infer April PPI values from neighbouring months.
- Official release context for the Output-PPI supersession: PIB PRID 2278961, 2026-06-29: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3

## Month-by-month coverage
The companion CSV contains all 41 months, explicit status, exact catalogue table ID where present, base-year/classification where parsed, HTTP and parse statuses, and scope notes.

## QA conclusions
- Manifest row count and unique ID count: 40/40.
- Calendar-month reconciliation: 41 expected, 40 represented.
- Missing catalogue month: 2026-01.
- Failed catalogue download: 2026-04 (404).
- Parsed vintages: 39.
- No duplicate month in this exact manifest; do not conflate this with earlier catalogue page scrape count of 41 qualifying rows including a duplicate.
- Two distinct gap types remain separate: absent catalogue record (January 2026) and present-but-unavailable catalogue record (April 2026).
- No new candidate transition certified; 693 policy-stage candidates remain uncertified, 431 historical/out-of-window transitions unresolved.
- IIP full audit remains BLOCKED_WITH_GAPS; master Hard Gate remains BLOCKED.

## Research implications / next action
1. Target official catalogue/API metadata for January 2026 and the April 2026 Output-PPI vintage separately.
2. For April 2026, do not reuse the June 1 WPI-based PIB crosswalk as PPI-based evidence.
3. After obtaining official records, acquire raw payload first, record retrieval timestamp, content type, byte count and SHA-256, then parse and run source-cell QA.
4. Until both missing periods are resolved, do not label the April 2023–August 2026 monthly panel complete.

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or V11.3(A/B/C/D/E) production logic changed. UNKNOWN remains neither PASS nor FAIL. No synthetic data, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation. Research spend ₹0.
