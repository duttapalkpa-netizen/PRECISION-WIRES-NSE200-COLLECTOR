# IIP official-release gap crosswalk — 2026-11-03

## Scope and evidence snapshot

- Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
- PR: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/17
- Source audit workflow: Run #41640521553 (GitHub Actions conclusion: success).
- Source audit artifact: 13232127900, `iip-41-vintage-ingestion-revision-audit`.
- GitHub artifact digest / independently recomputed ZIP SHA-256: `e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c`.
- Source commit: `16f382aabf984eca403e85fb0c701e36a5a35370`.
- Audit payload: 41 qualifying catalogue rows; 40 unique vintage IDs / 40 unique catalogue reference periods; 39 downloaded and parsed; one HTTP 404; 125,220 parsed observations; 1,124 within-series value differences (1,056 in 2011-12/NIC-2008 and 68 in 2022-23/NIC-2025).
- Audit status in artifact: `BLOCKED_WITH_GAPS`; Hard Gate: `BLOCKED`.

## Officially reconciled apparent period gaps

### January 2026

- The catalogue manifest has no independent monthly catalogue workbook row with `ref_period=Jan 2026`. This is a catalogue-vintage gap, not proof that January 2026 observations are absent.
- Official MoSPI/PIB Quick Estimate release: 2 March 2026, PIB Release ID 2234512, `QUICK ESTIMATE OF INDEX OF INDUSTRIAL PRODUCTION AND USE-BASED INDEX FOR THE MONTH OF JANUARY 2026`, base 2011-12, NIC-2008.
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2234512&lang=1&reg=3
  - MoSPI-hosted PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1772446993082_bafbeab1-d887-4088-ad79-34bca753b231_IIP_Press_release_January_2026.pdf
- The official 30 March 2026 February release states that January 2026 underwent final revision. PIB Release ID 2246871:
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2246871&lang=1&reg=3
- Independent inspection of `all_vintage_observations.csv` confirms January 2026 observations are present in six later parsed catalogue vintages. Thus `missing_reference_periods=["2026-01"]` describes the absence of a dedicated catalogue release row, not missing January observation values.
- Treatment: retain the catalogue gap as an explicit provenance limitation; add the official March 2 Quick and March 30 Final release documents as separate release-stage evidence. Do not manufacture a missing catalogue workbook or mark the raw-workbook requirement satisfied.

### April 2026

- The catalogue entry `IIPMFY26002APR` (catalogue code 158504) returned HTTP 404 for the referenced XLSX. Preserve that failed request and its SHA-256 in the raw manifest; do not substitute a May workbook for the missing April catalogue file.
- The first official new-series release was published 1 June 2026 at 4:35 PM IST: PIB Release ID 2267531, `FIRST PRESS RELEASE OF ALL INDIA INDEX OF INDUSTRIAL PRODUCTION OF NEW SERIES WITH BASE YEAR 2022-23`. It explicitly identifies April 2026 as Quick Estimates, base 2022-23, NIC-2025, and provides Statements I, II(A-D), and III.
  - URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
  - MoSPI-hosted PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- The 29 June 2026 MoSPI/PIB release for May 2026 explicitly states that the entire 2022-23 IIP series was revised using Output PPI instead of WPI and that this PPI-based series supersedes the earlier WPI-based series released on 1 June 2026. It instructs users to use the PPI-based series for analytical, research, and policy purposes.
  - PIB archive URL: https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616
- The downloaded May-2026 vintage workbook `IIPMFY26006MAY` (release date 29 Jun 2026) contains April-2026 NIC-2025 observations. These are the later PPI-based revised vintage, not the missing 1 June WPI-based Quick release.
- Treatment: preserve both release vintages distinctly. The 1 June PDF is the official initial Quick release; the 29 June PPI-based series is the superseding analytical series. Do not collapse their values or treat the June 29 workbook as proof that the missing April catalogue XLSX was downloaded.

## Revision-policy chronology that must govern stage tagging

1. Before the revised release schedule took effect, the official policy used Quick, first-revised, and final estimates. MoSPI's 17 April 2025 announcement changed the schedule from 42 to 28 days and removed the second revision; thereafter each reference month has a Quick estimate followed by one Final estimate in the next release.
   - PIB Release ID 2122427: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2122427&lang=2&reg=48
2. The 30 March 2026 release explicitly identifies February 2026 as Quick and January 2026 as Final.
3. The 1 June 2026 release identifies April 2026 as Quick in the new base-year / NIC classification.
4. The 29 June 2026 release is a methodology vintage break: Output PPI replaces WPI and the whole new-base series is superseded. Record this separately from ordinary Quick-to-Final revision.

## Interpretation controls

- The 1,124 rows in `revision_differences.csv` are observed value differences between parsed source vintages, not yet a fully certified revision-stage ledger.
- Counts: 1,056 differences in 2011-12/NIC-2008; 68 differences in 2022-23/NIC-2025. No cross-base-year or cross-classification comparisons are included.
- Do not label a difference Quick-to-Final until the source release date, reference period, estimate stage, series definition, and methodology vintage are joined to an official release.
- The artifact's `missing_reference_periods` field is based on catalogue release-row continuity. It must not be presented as a missing observation-period test.
- The audit remains BLOCKED because one raw catalogue workbook fetch failed (HTTP 404), a separate catalogue reference-period row is absent, and the initial/final release-stage and methodology-vintage joins still need machine-readable evidence and validation.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, or 672-diagnostic changes are permitted. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.
