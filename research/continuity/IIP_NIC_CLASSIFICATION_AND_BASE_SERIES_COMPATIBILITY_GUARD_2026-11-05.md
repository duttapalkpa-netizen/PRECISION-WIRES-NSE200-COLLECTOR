# IIP NIC Classification and Base-Series Compatibility Guard — Batch 014
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Critical correction / scope clarification
The March 2024 Batch 014 crosswalk is explicitly the legacy IIP series with base 2011-12=100 and NIC-2008 classification. Its 19 NIC codes and values must not be silently relabelled as 2022-23 base or NIC-2025 data.

MoSPI's first press release for the new IIP series (1 June 2026) states that the new series has base 2022-23 and disseminates manufacturing two-digit data using NIC-2025. It also states that detailed new-series tables are available from April 2023 onward through e-Sankhyiki. Therefore the period April 2023 onward can have a new-series historical back-series that overlaps calendar periods already covered by legacy 2011-12/NIC-2008 releases. Reference month alone is not a sufficient series identifier.

Official sources:
- New-series first release (PIB PRID 2267531, 1 June 2026): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- MoSPI IIP FAQ, NIC-2025 classification for new series: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf
- Official e-Sankhyiki IIP catalogue/API landing page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip
- PIB release 29 June 2026 confirms Output-PPI based 2022-23 series supersedes the earlier WPI-based 2022-23 series: https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616

## Required independent series keys
Every IIP row must be keyed at minimum by:
- reference_period (YYYY-MM)
- base_year (2011-12 or 2022-23)
- classification_system (NIC-2008 or NIC-2025)
- deflator_vintage (legacy / WPI / Output-PPI / UNKNOWN)
- release_id or catalogue_table_id
- estimate_stage (QUICK / FIRST_REVISION / FINAL / source-defined)
- release_date, source_url, retrieval timestamp, raw payload SHA-256
- NIC code and official NIC description for that classification vintage

## Non-negotiable joins and mapping rules
- Never join or compare same-number NIC codes across NIC-2008 and NIC-2025 as if they identify the same industry. Require an official classification concordance and retain one-to-many/many-to-one mappings explicitly.
- Never compare 2011-12 and 2022-23 index levels directly. Any cross-series comparison requires an official documented bridge and must remain at the level for which the bridge is supported.
- Treat legacy 2011-12/NIC-2008 March 2024 Quick and First Revision observations as their own immutable release vintages.
- Treat the 2022-23/NIC-2025 historical back-series as a separate series vintage even for reference periods from April 2023 onward.
- For 2022-23 series, preserve WPI and Output-PPI vintages separately; the 29 June 2026 Output-PPI series supersedes the 1 June 2026 WPI series for current-series use, but the superseded WPI release remains immutable historical evidence.
- If base year, classification, or deflator cannot be identified from source metadata, mark UNKNOWN and block certified cross-series joins. UNKNOWN is neither PASS nor FAIL.

## Batch 014 impact
- Existing 19/19 March 2024 PIB cell crosswalk remains valid for the legacy 2011-12/NIC-2008 source pair only.
- This crosswalk does not validate the 2022-23/NIC-2025 historical back-series values for March 2024.
- Do not overwrite, relabel, or delete the existing ledger rows. Add the new-series vintage as a separate dataset when exact official catalogue metadata and source bytes are acquired.
- The existing candidate ledger is a 19-code subset, not a complete NIC universe.

## Status
LEGACY_MAR2024_SERIES_IDENTITY: VERIFIED (base 2011-12; NIC-2008; PIB two-sided cell crosswalk 19/19)
NEW_SERIES_IDENTITY: VERIFIED AT RELEASE/METHODOLOGY LEVEL (base 2022-23; NIC-2025; detailed back-series from Apr-2023)
NEW_SERIES_MAR2024_CELL_RECONCILIATION: NOT YET PERFORMED
OFFICIAL_NIC2008_TO_NIC2025_CONCORDANCE: NOT YET ACQUIRED
RAW_SOURCE_BINARY_SHA256: PENDING
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or V11.3(A/B/C/D/E) logic changed. No synthetic rows, fabricated timestamps, silent reclassification, unsupported source promotion, or hard-gate relaxation. Historical PASS evidence remains preserved.