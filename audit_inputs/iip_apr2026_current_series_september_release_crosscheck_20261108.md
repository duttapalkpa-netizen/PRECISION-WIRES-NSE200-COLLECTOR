# April 2026 NIC-2025 IIP independent September-release cross-check

Audit date: 2026-11-08  
Scope: independently compare the already extracted April 2026 NIC 10-32 current-series values against the later official September 2026 IIP release. This is an additional-source check, not a rerun of workbook extraction.

## Official source

- PIB release: Quick Estimates of Index of Industrial Production and Use-Based Index for September 2026
- Release ID: `2329475`
- Posted: 28 October 2026
- Source URL: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475&lang=1&reg=3
- Statement IV: Monthly Index of Industrial Production
- Statement IV header explicitly states `Base: 2022-23=100` and `NIC 2025`.
- April 2026 column and NIC 10-32 rows: web-rendered official source lines 221-244.
- The release explains that Statement IV gives month-wise indices for the last 13 months, by NIC-2025 industry groups (release text lines 98-99).

## Comparison

Compared the April-2026 column for each NIC code 10 through 32 in the September release with the already independently checked current-series ledger and August-2026 Statement IV cross-check.

- NIC rows: 23/23 present, contiguous 10-32.
- April values: 23/23 exact matches at published precision.
- Mismatches: 0.
- April 2026 values, in NIC order 10-32:
  `100.5, 155.2, 113.8, 135.7, 91.0, 99.8, 84.3, 115.0, 103.8, 104.6, 104.9, 110.7, 125.8, 115.8, 128.9, 125.9, 137.9, 151.5, 109.9, 130.4, 153.4, 109.8, 112.1`.

## Interpretation and guardrails

- This provides a second, later official publication cross-check for the April-2026 current-series values, independent of the user's August 2026 workbook extraction.
- No April-2026 value change is observed between the August 2026 release (PIB Release ID `2315957`) and September 2026 release (PIB Release ID `2329475`).
- This is only an observation across these two published releases; it does not establish that April 2026 is permanently final or unrevisable.
- The September release notes that August 2026 indices incorporate updated production data; do not infer that this statement means April values were revised.
- Keep base-year and classification metadata attached to each source. No 2011-12 data is used, and no cross-base-year arithmetic is performed.
- No cumulative-to-monthly derivation, synthetic values, inferred identifiers, or fabricated timestamps.
- This audit does not change the April current-series ledger, first-release WPI ledger, revision arithmetic, production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or CORE-672.
- Project-wide Hard Gate remains BLOCKED pending the other independent P0/factor, vintage, and event-study requirements.
- Spend: ₹0; official public sources only.
