# April 2026 current-series NIC-2025 IIP workbook verification

Audit date: 2026-11-08  
Scope: inspect the user-provided Library workbook selected from the official e-Sankhyiki August 2026 monthly NIC-2 catalogue record and independently reconcile April 2026 NIC 10-32 monthly indices.

## Source workbook inspection

- Original filename: `IndicesIIP2011-12Monthly_annual_sept26_NIC 2d_sectoralmonthly(3).xlsx`
- File size: 32,179 bytes
- SHA-256: `ce4c0bba17d2135474c6abd10aabe03758248e1423d434817c90a2d497ee16ce`
- Sheet: `NIC 2d, sectoral monthly`
- Workbook title: `INDEX OF INDUSTRIAL PRODUCTION`
- Workbook base-year heading: `(Base 2022-23)`
- Monthly index table classification heading: `NIC 2025`
- Monthly date columns: April 2023 through September 2026 (42 monthly observations)
- April 2026 is the 40th worksheet column; 23 manufacturing NIC rows 10-32 are present in the monthly-index table.
- Important filename warning: the filename contains `2011-12`, but the workbook's internal heading explicitly says `Base 2022-23`. The filename must not override the internal source metadata.

## Independent official cross-check

The official PIB release for August 2026 states:
- Title: Quick Estimates of Index of Industrial Production and Use-Based Index for August 2026.
- Posted: 28 September 2026.
- Release ID: `2315957`.
- Statement IV explicitly states `Base: 2022-23=100` and `NIC 2025`, with month columns including `Apr-26`.
- Source URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2315957&lang=1&reg=3
- Statement IV locator: lines 157-182 in the web-rendered official PIB release (NIC 10-32 rows).

Comparison result: all 23 workbook April-2026 values for NIC 10-32 match the official August-2026 PIB Statement IV April-2026 column exactly at the displayed one-decimal precision (23/23; 0 mismatches). The row codes are contiguous 10 through 32 and the displayed weights match the official NIC-2025 weights.

## Reconciliation of the apparent cross-base-year value collision

A previous audit noted that the same 23 April values appear in the May 2026 PIB monthwise table, whose separate monthwise section is explicitly labelled `Base: 2011-12=100`. This created a legitimate provenance warning.

The August 2026 PIB release independently publishes the same April-2026 values in Statement IV explicitly labelled `Base: 2022-23=100` and `NIC 2025`. Therefore:
- The user-provided workbook's internal metadata and its 23 April values are independently corroborated by the later official current-series 2022-23 Statement IV.
- The identical displayed values in the May 2011-12-labelled monthwise table do not justify merging the two base-year series or calculating cross-base revision deltas.
- Keep each source's base-year/classification metadata attached to its own observations. Do not use the May 2011-12-labelled table as the source for the current 2022-23 ledger.
- The current workbook is accepted as a 2022-23/NIC-2025 monthly historical panel for April 2026, supported by the August 2026 official current-series statement.

## Data artifact

CSV extracted from the workbook, preserving one row per NIC code:
`audit_inputs/iip_apr2026_current_output_ppi_nic2025_monthly_values.csv`

The CSV carries period, NIC code, description, weight, April 2026 index, base year, classification, deflator, source workbook name and SHA-256, sheet, month column, catalogue table ID, official PIB release ID/date, statement locator, and verification status.

- Catalogue record selected: `IIPMFY26018AUG`, Monthly NIC-2 digit and sectoral indices and growth rates upto August 2026.
- Official catalogue: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
- Official May 2026 release establishes Output PPI adoption and supersession of the earlier WPI-based 2022-23 series: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
- Official August 2026 release independently validates the April values in the current 2022-23 series.

## QA result and guardrails

- Workbook structure and base/classification metadata: PASS.
- NIC 10-32 coverage: PASS (23/23).
- April 2026 extraction: PASS (23/23).
- Official August current-series Statement IV cross-check: PASS (23/23; 0 mismatches).
- Cross-base-year arithmetic: NOT PERFORMED.
- Original workbook hash: captured from raw file bytes.
- No synthetic values, inferred table IDs, cumulative-to-monthly derivation, or fabricated timestamps.
- The workbook is a monthly historical panel through September 2026; no claim is made here that this alone completes every IIP vintage/revision requirement.
- Project-wide Hard Gate remains BLOCKED pending all other independent P0/factor, vintage, and event-study requirements.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and CORE-672 are unchanged.
- Spend: ₹0; official public sources only.

This note supersedes the earlier provisional status that the August workbook contents and April values were not yet inspected. It does not merge or rewrite prior audit evidence.
