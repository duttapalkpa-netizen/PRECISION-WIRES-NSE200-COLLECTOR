# IIP cell-level revision audit — Batch 001 (2026-11-03)

## Scope
First bounded batch from the 693 policy-stage-aligned candidate transitions. This batch covers April 2023 NIC-2008 observations for industry codes 10, 11, 13, 14, 15, 16, 17, 19 and 20, comparing the April 2023 Quick vintage with the May 2023 First Revision vintage.

## Official primary release evidence
- Previous Quick vintage: PIB PRID 1931708, published 12 Jun 2023 17:30 IST. Statement II contains the April 2023 NIC-2008 index values. https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1931708&lang=2&reg=48
- Current First Revision vintage: PIB PRID 1938974, published 12 Jul 2023 17:30 IST. The release explicitly states April 2023 underwent first revision; Statement IV provides monthly NIC-2008 values including April 2023. https://www.pib.gov.in/PressReleasePage.aspx?PRID=1938974&lang=2&reg=3

## Source workbook integrity
- Previous workbook SHA-256: `7cff38f066509e007c980a4267fd1753aa1fcae560438ad3df424d78d49ec30e`
- Current workbook SHA-256: `6530370f75fa24997f98b760f336b70533a058e1a0a0f464bf1c26a10985425a`
- Both workbook payloads are from the original Run #41640521553 audit artifact. Each exact value was located in the `NIC 2d, sectoral monthly` worksheet at the coordinates recorded in the CSV.
- All nine previous values match PIB Statement II and their source workbook cells. All nine current values match PIB Statement IV and their source workbook cells.

## Result
- Candidate rows reviewed: 9
- Exact workbook cell matches: 18/18
- Official PIB statement value matches: 18/18
- Certified cell-level source matches: 9
- Mismatches: 0
- Revision differences retained as numeric source facts; no claim that direction or magnitude implies economic significance.

| NIC code | Previous Quick | First Revision | Delta |
|---:|---:|---:|---:|
| 10 | 135.2 | 136.1 | +0.9 |
| 11 | 106.8 | 106.7 | -0.1 |
| 13 | 106.9 | 106.8 | -0.1 |
| 14 | 91.8 | 91.7 | -0.1 |
| 15 | 99.5 | 97.8 | -1.7 |
| 16 | 89.3 | 89.6 | +0.3 |
| 17 | 79.4 | 80.6 | +1.2 |
| 19 | 128.9 | 128.8 | -0.1 |
| 20 | 126.9 | 126.2 | -0.7 |

## Remaining work and gate
- Policy-aligned candidate transitions not yet certified: 684
- Historical-panel/out-of-window transitions unresolved: 431
- Total observed within-series differences: 1,124
- Certified rows are now 9, not 1,124; no extrapolation to unreviewed cells.
- April 2026 catalogue XLSX HTTP 404 and the other previously documented source gaps remain unresolved.
- Hard Gate remains BLOCKED. This bounded evidence step does not alter the production selector, RANKING_SCORE, +1 PRESSURE_FADE or CORE-672 diagnostics.

## Reproducibility
The bounded verifier is `pipeline/audit_iip_cell_level_revision_batch_001.py`. It verifies both source workbook SHA-256 values, locates the NIC-2008 April 2023 cells by industry code, compares them to the fixed official PIB statement values and emits the CSV/JSON ledger. The script fails closed on a source hash or cell-value mismatch.
