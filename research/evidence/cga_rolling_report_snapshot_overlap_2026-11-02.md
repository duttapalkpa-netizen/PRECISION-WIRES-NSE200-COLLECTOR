# CGA rolling monthly-report snapshot comparison — 2026-11-02

Status: `PASS_OVERLAPPING_CGA_REPORT_SNAPSHOTS_NO_NUMERIC_REVISION_DETECTED`; publication-vintage timestamps for the individual HTML report files remain unverified.

## Newly recovered CGA report snapshots

Official month-specific details pages were inspected:
- June 2025: https://cga.gov.in/writereaddata/MonthAccount/62025/DTL12526.HTM
- August 2025: https://cga.gov.in/writereaddata/MonthAccount/82025/DTL12526.HTM
- September 2025: https://cga.gov.in/writereaddata/MonthAccount/92025/DTL12526.HTM
- October 2025: https://cga.gov.in/writereaddata/MonthAccount/102025/DTL12526.HTM

The month-specific page paths identify the reporting month. The currently served content is not, by itself, proof of the date on which that HTML was first published. The pages do, however, expose progressively longer month-to-date/YTD histories and can be compared as distinct report-period snapshots.

## Overlapping Capex values (₹ crore)

| Reference month | June report YTD | August report YTD | September report YTD | October report YTD | Cross-snapshot delta |
|---|---:|---:|---:|---:|---:|
| April 2025 | 159,790 | 159,790 | 159,790 | 159,790 | 0 |
| May 2025 | 221,354 | 221,354 | 221,354 | 221,354 | 0 |
| June 2025 | 275,132 | 275,132 | 275,132 | 275,132 | 0 |
| July 2025 | — | 346,926 | 346,926 | 346,926 | 0 |
| August 2025 | — | 431,579 | 431,579 | 431,579 | 0 |
| September 2025 | — | — | 580,746 | 580,746 | 0 |

All overlapping values are exact matches. The six month-specific report snapshots provide a progressively expanding set of overlapping observations: June (3 months), August (5), September (6), October (7). No numeric revision is detected in these overlaps.

## Interpretation and boundaries
- This is stronger than comparing only the present-day CGA dashboard with PIB: it shows the same cumulative values recur in multiple report-period-specific CGA pages.
- It is not a complete immutable historical archive proof: current fetch time is not original release time, and page path/report period does not prove first publication date.
- PIB dated releases separately provide publication timestamps for the six monthly points; standalone monthly flow remains derived from cumulative differences.
- No evidence of a revision in the observed overlap; intermediate corrections that were later reverted remain UNKNOWN.
- CGA's official disclaimer says monthly accounting data is provisional and subject to change: https://cga.gov.in/Page/Monthly-Accounts-Review.aspx

## Decision
Accept the rolling CGA report-period overlap as additional corroborating evidence. Status: `PASS_OVERLAPPING_CGA_REPORT_SNAPSHOTS_NO_NUMERIC_REVISION_DETECTED` with `ORIGINAL_CGA_HTML_PUBLICATION_TIMESTAMPS_UNKNOWN`. Keep Factor Registry group partial / provisional; do not promote; Hard Gate remains BLOCKED. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and 672 diagnostics unchanged.
