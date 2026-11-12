# IIP Series-Break and Vintage Guard — Research Control Note
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Why this control is required
The IIP evidence pipeline must not silently concatenate observations from different base-year or deflator vintages. A series break or methodological revision can create apparent level/growth changes that are not market-cycle signals. This is a research-data comparability control only; it does not alter the production selector or any scoring logic.

## Officially established series facts
1. The 2011-12 base IIP series and the 2022-23 base IIP series are distinct statistical series. MoSPI/PIB states that detailed new-series tables, including manufacturing NIC-2 digit tables, are available from April 2023 onward through e-Sankhyiki.
2. MoSPI released the 2022-23 base IIP series using WPI as deflator on 1 June 2026.
3. MoSPI subsequently stated that it adopted Output PPI instead of WPI for item groups whose output is collected in value terms, affecting 234 of 463 item groups (36.02% of total index weight). The revised 2022-23 series released on 29 June 2026 supersedes the earlier WPI-based 2022-23 series released on 1 June 2026.
4. The e-Sankhyiki catalogue is the official public catalogue and advertises downloadable Excel statements; the IIP API is separately documented on the portal. API access/schema must be validated before any automated ingestion.

## Mandatory vintage dimensions
Every IIP observation ingested into the research layer must carry, where available:
- series_base_year (2011-12 or 2022-23)
- deflator_vintage (not applicable/legacy, WPI, Output-PPI, or explicitly UNKNOWN)
- reference_period (YYYY-MM)
- estimate_stage (QUICK, FIRST_REVISION, FINAL, or source-defined)
- release_date and exact release identifier / catalogue table ID
- source_url, retrieval timestamp, and raw payload SHA-256
- NIC code / sector code and statement/table identity
- source_revision_vintage and supersession relationship

## Hard comparability rules
- Never join 2011-12 and 2022-23 base index levels as if they were one continuous level series.
- Never join the June 2026 WPI-based 2022-23 vintage and the June 29 2026 Output-PPI-based vintage without explicit version labels and a documented overlap/bridge study.
- Preserve each released vintage as immutable evidence; revisions are additional vintages, not overwrites.
- YoY growth must be calculated within the same base-year and deflator vintage unless an official, documented bridge explicitly permits comparison.
- Where the vintage cannot be resolved from the source record, mark it UNKNOWN and exclude it from certified comparisons; UNKNOWN is neither PASS nor FAIL.
- No backfilled synthetic values, inferred release dates, or silent source promotion.

## Research impact and priority
Priority: HIGH (macro data integrity / comparability control).
This guard is a research QA layer only. It does not change the production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or V11.3(A/B/C/D/E) logic.

## Current scope limitation
This note does not claim that historical e-Sankhyiki table IDs, original workbook binaries, or raw payload hashes for March 2024 have been acquired. Batch 014 remains subject to its separate binary-provenance and full NIC-2 cohort blockers. Catalogue discovery or a current downloadable table is not proof of an exact historical release workbook.

## Status
IIP_SERIES_BREAK_CONTROL: DOCUMENTED
VINTAGE_TAGGING_REQUIRED: YES
HISTORICAL_RAW_BINARY_SHA256: PENDING
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED