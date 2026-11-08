# IIP Series Transition Crosswalk — Old 2011-12 to Current 2022-23

Status: EVIDENCE-BACKED RESEARCH DATA CONTRACT
Recorded: 2026-11-08
Scope: IIP series lineage, classification, deflator and revision-vintage controls only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE or CORE-672 changes.

## Executive determination

The old IIP series is `BASE_2011_12 / NIC_2008` and its final official monthly release is March 2026 (released 28 April 2026). The replacement series begins with reference month April 2026 at base `2022_23`, but the first 1 June 2026 release was a WPI-deflated provisional version and was superseded on 29 June 2026 by the Output-PPI-deflated 2022-23 series. The current new-series classification is `NIC_2025`, not NIC-2008.

Therefore, the valid boundary is:
- Old series: 2011-12 base, NIC-2008, through 2026-03.
- New series: 2022-23 base, NIC-2025, from 2026-04 onward; use the Output-PPI version, not the superseded 1 June WPI vintage.
- Keep base-year, classification and deflator transitions explicit. Do not concatenate index levels, manufacture conversion factors, or map NIC-2008 to NIC-2025 without an official concordance and a separately validated mapping.

## Official evidence register

### A. Last old-base release
- Publisher: MoSPI / NSO.
- Reference month: 2026-03.
- Release date: 2026-04-28.
- Base/classification: 2011-12=100 / NIC-2008 (manufacturing two-digit statement).
- MoSPI PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1777370981972_ac151bbf-29ab-4f2c-a10e-bd727a4d3564_IIP_Press_release_March_2026.pdf
- PIB release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2256241&lang=2&reg=3
- Evidence: monthly NIC-2008 manufacturing indices through March 2026, including Statement IV.

### B. First new-base release — superseded vintage
- Reference month: 2026-04; release date: 2026-06-01.
- Base: 2022-23=100.
- Deflator at release: WPI.
- PIB: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- MoSPI PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- Treat as an archived first-release vintage only; do not use as the current 2022-23 series after supersession.

### C. Current 2022-23 series — Output PPI deflator
- PIB release: 2026-06-29, May 2026 IIP quick estimates.
- PIB archive page: https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616
- Official determination: MoSPI replaced WPI with Output PPI for value-reported item groups and explicitly said the revised Output-PPI series supersedes the earlier WPI-based 2022-23 series released 1 June 2026.
- Scope: 234 of 463 item groups, representing 36.02% of total index weight, use value-based production data affected by the deflator change. MoSPI also incorporated updated source-agency data from April 2022 and revised electricity sub-sector weights.
- The 29 June release publishes the comparative annual growth rates for 2022-23 Output-PPI series versus 2011-12 series.

### D. Current classification and latest verified monthly vintage
- The current 2022-23 series uses NIC-2025 two-digit industry groups. MoSPI's September 2026 release explicitly labels Statements II and related manufacturing detail by NIC-2025.
- Latest verified release as at this record: September 2026 quick estimate, published 2026-10-28.
- PIB: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48
- Current-series quick estimate IIP growth: 6.7% y/y; manufacturing 7.6%; mining -6.2%; electricity & gas 11.2%; water/sewerage/waste management 5.8%.
- The same release says September 2026 quick estimates and August 2026 final revision have weighted response rates of 86.5% and 92.0% respectively. Quick estimates are subject to subsequent revision.
- These figures are a current monthly vintage snapshot, not a historical series bridge.

## Official comparative growth-rate bridge

The following values are copied from MoSPI/PIB's 29 June 2026 comparative annual growth-rate statement. They are not calculated from index levels. The official release warns that the two series' growth rates are not strictly comparable due to coverage, methodology, basket, sector composition and weights.

| Sector | Series | FY2023-24 | FY2024-25 | FY2025-26 |
|---|---|---:|---:|---:|
| General | 2022-23 Output PPI | 6.8% | 5.7% | 4.3% |
| General | 2011-12 legacy | 5.9% | 4.0% | 4.1% |
| Mining & Quarrying | 2022-23 Output PPI | 2.2% | 2.8% | 3.7% |
| Mining & Quarrying | 2011-12 legacy | 7.5% | 3.0% | 1.4% |
| Manufacturing | 2022-23 Output PPI | 7.1% | 6.0% | 4.8% |
| Manufacturing | 2011-12 legacy | 5.5% | 4.1% | 5.0% |
| Electricity & Gas Supply | 2022-23 Output PPI | 7.4% | 5.2% | 0.8% |
| Electricity (legacy sector definition) | 2011-12 legacy | 7.1% | 5.2% | 1.0% |

Source for all bridge values: official PIB archive page above, 29 June 2026. Keep the official sector labels as published; do not infer a one-to-one sector equivalence where scope differs.

## Mandatory data contract

Each stored observation/vintage must retain, at minimum:
- `series_id`
- `base_year`
- `classification`
- `deflator`
- `reference_period`
- `release_id` / PIB PRID where available
- `release_date`
- `vintage_type` (quick_estimate, revised_estimate, final_revision, later_snapshot, etc.)
- `source_url`
- `source_sha256` (only when raw bytes were actually captured and hashed)
- `response_rate` (when stated by source)
- `supersedes_release_id` (when officially stated)

## No-splice / no-fabrication rules

1. Never join old and new index levels as if they form one continuous numeric series.
2. Never infer a rebasing multiplier or convert index levels from growth-rate tables.
3. Never treat the 1 June WPI-based 2022-23 release as current after the official 29 June supersession.
4. Never label the new series NIC-2008: current 2022-23 industry-group tables are NIC-2025.
5. Never join NIC-2008 and NIC-2025 industry groups without an official concordance, explicit many-to-many mapping where applicable, and validation. If absent, status is UNKNOWN.
6. Use only the official MoSPI/PIB comparative growth-rate bridge for high-level comparison; preserve its warning that growth rates are not strictly comparable.
7. Keep every monthly quick estimate and subsequent revision as separate vintages. Never overwrite the first release or fabricate a first-release value from a later snapshot.
8. Missing, stale, unmapped or unsupported inputs remain UNKNOWN; UNKNOWN is neither PASS nor FAIL.
9. No synthetic data, inferred timestamps, unsupported source promotion, paid APIs or spend.

## Prior errors prevented by this crosswalk

- Do not keep requesting an old-base April 2026 workbook: the old series ends March 2026. The previously logged HTTP 404 is consistent with NOT_APPLICABLE for an old-base April observation; retain the 404 hash in the audit trail.
- Do not accidentally treat the 1 June WPI-based new series as current: it was officially superseded on 29 June.
- Do not incorrectly tag the new series as NIC-2008: the current manufacturing groups are NIC-2025.
- Do not mistake monthly quick estimates for immutable final values: subsequent revisions are part of the official release process.

## Completion boundary

This document completes the research crosswalk specification and evidence reconciliation for the old/new series transition. It does not complete source-byte archival/hashes for every cited release, a machine-readable NIC concordance, the full monthly revision-vintage acquisition, the IIP 41-vintage gate, or the project-wide Hard Gate. No production integration or PR merge is authorized or performed.
