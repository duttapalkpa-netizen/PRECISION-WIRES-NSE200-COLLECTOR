# April 2026 IIP — Output-PPI superseding-release evidence audit
Date: 2026-11-08
Status: OFFICIAL_RELEASE_EVIDENCE_VERIFIED; NATIVE_CATALOGUE_SOURCE_NOT_RECOVERED

## Objective
Resolve whether April 2026 has any official Output-PPI-based IIP evidence, without confusing the 1 June WPI-based first release with the 29 June superseding PPI-based series, and without inventing a catalogue table ID.

## Primary official source
- PIB / MoSPI PRID 2278961, posted 29 June 2026 at 16:00 IST.
- URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
- The release explicitly states that the entire 2022-23 IIP series was revised with Output PPI, superseding the 1 June 2026 WPI-based series; it also incorporates updated source-agency data from April 2022 onward. The notice says users should use the PPI-based series for analytical, research and policy purposes.
- It explicitly identifies May 2026 Quick Estimates as base 2022-23=100, deflator Output PPI.
- The release states that Statement IV provides month-wise indices for the last 13 months, by NIC-2008 industry groups, sectors and sub-sectors. The HTML rendering includes a month-wise manufacturing table spanning May 2025 through May 2026, including an April 2026 column. Thus April 2026 is represented within the official superseding-release publication, even though the old standalone April catalogue ID in the retained manifest is HTTP 404.
- The source page's Statement IV begins at lines 157–159 in the opened official PIB rendering. The April 2026 month column is visible in the month-wise manufacturing series (e.g., food products 100.5; beverages 155.2; tobacco products 113.8; textiles 135.7; wearing apparel 91.0). These are source-page transcriptions, not native MoSPI catalogue workbook rows.

## Critical source distinction
1. 1 June PRID 2267531 is the initial April 2026 new-series release and is explicitly WPI-based. It is NOT the final PPI-based source.
2. 29 June PRID 2278961 is the superseding Output-PPI-based full-series release. It is the valid official source for April 2026 PPI-series backfill evidence.
3. Existing catalogue ID `IIPMFY26002APR` remains HTTP 404 in the earlier immutable manifest. No replacement table ID or April standalone XLSX was located in this task.
4. Therefore the April gap is narrowed from “no identified Output-PPI official release evidence” to “official superseding PIB release contains April month-wise data; native catalogue table/XLSX and full cell-level extraction still outstanding.” Do not claim native MoSPI workbook recovery or complete monthly-vintage ingestion.

## QA and limits
- Release identity, publication timestamp, deflator, supersession statement, and April historical-panel inclusion: VERIFIED against the official PIB page.
- Exact April cell transcription beyond the few illustrative rows above: NOT EXTRACTED / NOT QA-CERTIFIED in this task.
- Native April catalogue table ID / XLSX: NOT RECOVERED.
- API schema and exact monthly API filters: NOT VERIFIED.
- No synthetic data, inferred IDs, or guessed API parameters used.
- Do not splice this April month-wise panel with May monthly quick estimates without preserving source statement, classification, base, deflator, and release-vintage metadata.

## Recommended next bounded step
Extract the full April 2026 column from Statement IV of PRID 2278961 into a separately typed PIB-release transcription ledger, preserve row labels and exact statement context, validate all rows and arithmetic where possible, and only then reconcile against the native e-Sankhyiki/API output if official schema/metadata becomes available.

## Invariants
Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and V11.3(A/B/C/D/E) remain unchanged. UNKNOWN is neither PASS nor FAIL. Hard Gate remains BLOCKED. Research spend ₹0.
