# May 2026 Output-PPI IIP Statement II-A transcription validation

Audit date: 2026-11-08  
Branch: `qa/iip-apr2026-crosscheck-validation`  
Source release: MoSPI/PIB Release ID `IIPMFY26006MAY`, 29 June 2026  
Official source: https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616

## Scope

Independently validate the committed 23-row transcription:
`audit_inputs/iip_may2026_output_ppi_nic2025_statement_IIA_transcription.csv`

CSV Git blob SHA: `efbc8940fb1bac66dddb927444ebada5394401a4`.

## Source-to-ledger reconciliation

The official release identifies the current series as base 2022-23, deflator Output PPI, and Statement II-A as NIC-2025 two-digit manufacturing. The published table occupies official page text lines 56-84. The transcription contains the exact 23 NIC codes 10-32 in order.

Independent field-by-field comparison against the official Statement II-A rows 10-32:
- NIC codes: 23/23 exact.
- Descriptions: 23/23 exact.
- Weights: 23/23 exact at published precision.
- May 2025 index: 23/23 exact.
- May 2026 index: 23/23 exact.
- Apr-May 2025-26 cumulative index: 23/23 exact.
- Apr-May 2026-27 cumulative index: 23/23 exact.
- May 2026 year-on-year growth: 23/23 exact.
- Apr-May cumulative growth: 23/23 exact.
- Total numeric/source-cell comparisons: 161/161 exact (7 numeric fields per row: weight, two monthly indices, two cumulative indices, and two growth rates).

## Independent arithmetic QA

For each row, recomputed:
1. `(May-2026 index / May-2025 index - 1) * 100`
2. `(Apr-May 2026-27 cumulative / Apr-May 2025-26 cumulative - 1) * 100`

Both results rounded to one decimal place using decimal arithmetic. Result: 46/46 calculations match the published growth cells; 0 mismatches.

Schema/provenance checks:
- 23 data rows; unique NIC codes exactly 10 through 32.
- All rows identify reference period 2026-05, base year 2022-23, classification NIC-2025, release ID `IIPMFY26006MAY`, release date 2026-06-29, Statement II-A, and the same official PIB source URL.
- All 23 rows explicitly retain `standalone_apr_2026_index_status=NOT_PRESENT_IN_STATEMENT`.
- The 23 rounded weights sum to 76.065, while the published aggregate manufacturing weight is 76.062; this 0.003 difference is a rounding-level sum of displayed three-decimal component weights and is not used to alter any source value.

## Interpretation and guardrails

- May 2026 transcription QA: PASS.
- This artifact does not provide the standalone April 2026 PPI-based NIC-2 IIP values.
- Do not derive April from the Apr-May cumulative index; no such inference was made.
- Do not mix with the separate monthwise table explicitly labelled base 2011-12.
- The WPI-based 01 June first release remains superseded by the Output-PPI series as stated in the 29 June release.
- April 2026 catalogue table ID and current-series standalone April values remain NOT_VERIFIED / NOT_EXTRACTED.
- Original 01 June WPI PDF raw SHA-256 remains PENDING.
- IIP sub-audit and project-wide Hard Gate remain BLOCKED.
- No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or CORE-672 diagnostic changed.
- No paid source, API credential, fabricated data, or synthetic timestamp used; spend ₹0.

## Acceptance

This validation closes only the May 2026 Statement II-A transcription QA subtask. It does not close the April 2026 current-series extraction or overall IIP acceptance.
