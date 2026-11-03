# IIP official release evidence — gap closure addendum (2026-11-03)

Two previously unresolved catalogue vintages now have exact official PIB release-page matches:

| Catalogue table ID | Reference period | Official PIB PRID | Publication timestamp (IST) | Stage | Verification |
|---|---|---:|---|---|---|
| IIPMFY24014JUL | July 2024 | 2054214 | 2024-09-12 17:30 | Quick Estimate | Verified |
| IIPMFY25006MAY | May 2025 | 2140774 | 2025-06-30 16:00 | Quick Estimate | Verified |

Official primary sources:
- July 2024: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2054214&lang=2&reg=48
- May 2025: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2140774&lang=2&reg=48

The July 2024 PIB release explicitly labels July 2024 as Quick Estimate and contains Statements I–IV. The May 2025 release explicitly labels May 2025 as Quick Estimate and records publication at 4:00 PM on 30 June 2025.

Updated ledger accounting: 40/40 unique catalogue vintages have verified official PIB release pages; UNKNOWN official release-page rows are now zero. This does not repair the separate April 2026 catalogue workbook HTTP 404: its official Quick Estimate PDF remains evidence of the release, not a substitute XLSX payload.

The source audit still contains 1,124 within-series value differences and 431 historical-panel/out-of-window transitions. Subsequent Batch 001 certified 9 exact April-2023 cell-level source matches; 684 policy-aligned candidates remain uncertified. See `IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.md`. Official release-page identification and policy stage are not sufficient to certify individual value revisions.

Hard Gate remains BLOCKED. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 logic was changed. No synthetic rows or fabricated timestamps were introduced.
