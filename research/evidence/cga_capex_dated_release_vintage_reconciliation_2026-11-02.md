# CGA Capex — dated release/vintage reconciliation (FY 2025-26, Apr–Sep)

Status: `PASS_DATED_RELEASE_CROSSCHECK_NO_REVISION_DETECTED_WITH_INTERMEDIATE_VINTAGES_UNKNOWN`. Research-only.

## Method
For each reference month, the official PIB Ministry of Finance monthly accounts release published the following month supplies a dated publication timestamp, Release ID and cumulative capital-account expenditure (₹ crore). Standalone monthly Capex is derived as the difference between consecutive cumulative releases. Both cumulative and derived monthly values were checked against the current CGA month-specific report snapshots and the previously reconciled dashboard dataset. PIB cumulative capital-account expenditure is cross-walked to CGA's Capital Expenditure line; this is a metric mapping, not proof of independent source lineage.

## Month-by-month evidence

| Reference month | PIB publication (IST) | Release ID | PIB cumulative capital account (₹ cr) | Derived monthly (₹ cr) | Current CGA cumulative / monthly (₹ cr) | Delta |
|---|---|---:|---:|---:|---:|---:|
| April 2025 | 30 May 2025 18:22 | 2132828 | 159,790 | 159,790 | 159,790 / 159,790 | 0 / 0 |
| May 2025 | 30 Jun 2025 16:22 | 2140807 | 221,354 | 61,564 | 221,354 / 61,564 | 0 / 0 |
| June 2025 | 31 Jul 2025 18:24 | 2150924 | 275,132 | 53,778 | 275,132 / 53,778 | 0 / 0 |
| July 2025 | 29 Aug 2025 16:39 | 2161869 | 346,926 | 71,794 | 346,926 / 71,794 | 0 / 0 |
| August 2025 | 30 Sep 2025 16:40 | 2173166 | 431,579 | 84,653 | 431,579 / 84,653 | 0 / 0 |
| September 2025 | 31 Oct 2025 16:32 | 2184648 | 580,746 | 149,167 | 580,746 / 149,167 | 0 / 0 |

All six dated PIB releases match current CGA cumulative snapshots exactly. The derived standalone monthly values also match exactly. No numerical revision is detectable across these six observed release points.

## Limits
- Dated PIB pages prove that the cumulative capital-account values were publicly stated on the recorded dates.
- Standalone monthly values are derived by differencing cumulative release values; they are not separately quoted in PIB.
- CGA HTML reports were retrieved on 2 Nov 2026. These are current copies of month-specific report URLs, not independently preserved HTTP captures from their original release days.
- No mismatch was found. This does not prove no intermediate correction occurred and was later reverted, nor establish independent lineage between PIB and CGA. Intermediate revision history remains UNKNOWN.
- CGA states monthly accounts are provisional and subject to change. Retain that caveat.

## Decision
`PASS_DATED_RELEASE_CROSSCHECK_NO_REVISION_DETECTED_WITH_INTERMEDIATE_VINTAGES_UNKNOWN`.

Six of six monthly release points have dated official PIB evidence; six of six cumulative values match; six of six derived monthly values match; all deltas are zero. No factor promotion is authorized. Do not synthesize observation-level release timestamps from the reporting month. Hard Gate remains BLOCKED. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and all 672 diagnostics remain unchanged.

## Official source links
- April: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2132828&lang=2&reg=48
- May: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2140807&lang=2&reg=48
- June: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150924&lang=2&reg=48
- July: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2161869&lang=2&reg=48
- August: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2173166&lang=2&reg=48
- September: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2184648&lang=2&reg=48
- CGA July 2025 At-a-Glance: https://cga.nic.in/writereaddata/MonthAccount/72025/DATA2526.htm
- CGA archive index: https://cga.nic.in/MonthlyReport/Published/11/2025-2026.aspx
- CGA monthly-account disclaimer: https://cga.gov.in/Page/Monthly-Accounts-Review.aspx
