# April 2026 NIC-2025 IIP portal export verification

Audit date: 2026-11-08

## Captured user-provided portal export

- Library filename: `iip_62.xlsx`
- Size: 90,294 bytes
- SHA-256: `31ab1a00ea14b90a21086d3c618cd65456e45b3a02b4ae85251ee1dac9fb189e`
- Sheet: `Sheet1`
- Header: `base_year, year, month, type, category, sub_category, index, growth_rate`
- Workbook contains 216 data rows: 9 months (January–September 2026) × 24 rows per month.
- All rows identify base year `2022-23`, type `Sectoral`, category `Manufacturing`.
- April 2026 contains 24 rows: 23 named manufacturing NIC-2 categories and one aggregate Manufacturing row with blank sub_category.
- The 23 named April category index values match the existing NIC 10–32 ledger exactly (23/23; zero mismatches).
- The separate aggregate row is index 118.7, growth 6.1%; it is excluded from the 23 NIC-2 observations.

## Provenance boundaries

- The user supplied this workbook from the e-Sankhyiki portal and shared portal screenshots showing base year 2022-23, monthly frequency, year 2026, month April, Sectoral, Manufacturing, and selected manufacturing subcategories.
- The exported workbook itself does not include the catalogue table ID, download URL, download timestamp, or explicit NIC code column. These remain `NOT_VERIFIED` / `NOT_CAPTURED`; do not infer an April catalogue ID from the August ID.
- NIC 10–32 mapping follows the ordered 23 manufacturing subcategory rows and the independently checked Statement IV code/value list; the workbook names are retained as source labels.
- This confirms the portal-exported April values and the matching panel context, but it does not establish a distinct April catalogue record ID or a standalone per-month file.

## QA and guardrails

- Export bytes SHA-256 captured from the original Library file.
- April category row count: 23; aggregate rows: 1; missing category/index rows: 0; duplicate category names: 0.
- April NIC 10–32 values: 23/23 exact match with the existing current Output-PPI ledger and the two official PIB Statement IV cross-checks already recorded there.
- The ledger source workbook filename and SHA-256 are updated to this actual portal export; validator pins both filename and hash.
- No synthetic rows, fabricated timestamps, guessed catalogue IDs, cumulative-to-monthly derivations, or cross-base-year arithmetic.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, collector and production engines unchanged.
- Project-wide Hard Gate remains BLOCKED pending other independent acceptance requirements.
- Spend: ₹0.
