# IIP official-release gap crosswalk — 2026-11-03

## Scope and evidence snapshot
- Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
- PR: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/17
- Source audit workflow: Run #41640521553 (GitHub Actions conclusion: success).
- Source audit artifact: 13232127900, `iip-41-vintage-ingestion-revision-audit`.
- Independently recomputed ZIP SHA-256: `e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c`.
- 41 qualifying catalogue rows; 40 unique vintage IDs / 40 unique catalogue reference periods; 39 downloaded and parsed; one HTTP 404; 125,220 observations; 1,124 within-series differences.
- Source audit status: `BLOCKED_WITH_GAPS`; Hard Gate: `BLOCKED`.

## January 2026
- No independent monthly catalogue workbook row with `ref_period=Jan 2026`; this is a catalogue-vintage gap, not proof of missing observation values.
- Official Quick release: 2 Mar 2026, PIB PRID 2234512: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2234512&lang=1&reg=3
- The 30 Mar 2026 release PRID 2246871 identifies January 2026 as Final: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2246871&lang=1&reg=3
- January 2026 observations exist in six later parsed vintages. Keep catalogue gap explicit; do not manufacture a workbook or mark raw-workbook coverage satisfied.

## April 2026
- Catalogue record `IIPMFY26002APR` (catalogue code 158504) returned HTTP 404. Preserve the failed request and its provenance; do not substitute a May workbook.
- Official first new-series Quick release: 1 Jun 2026, 16:35 IST, PIB PRID 2267531: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- MoSPI PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- May 2026's Output-PPI Quick release, PIB PRID 2278961 (29 Jun 2026): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
- PRID 2278961 states the Output-PPI series supersedes the WPI-based series released on 1 Jun 2026. The downloaded May-2026 workbook is a later Output-PPI methodology vintage and does not prove that the missing April XLSX was downloaded.
- Preserve the 1 Jun WPI Quick PDF and 29 Jun Output-PPI workbook as distinct vintages.

## Revision policy
1. Legacy policy: PIB PRID 1931708 (12 Jun 2023) explicitly identifies current month Quick, previous month First Revision, and third previous month Final.
2. New policy: PIB PRID 2122427 (17 Apr 2025) changes release timing to 28 days and removes the second revision; from April 2025 the series is Quick followed by one Final estimate in the next release.
   - https://www.pib.gov.in/PressReleasePage.aspx?PRID=2122427&lang=2&reg=3

## Controls and unresolved work
- The 1,124 rows are observed value differences, not certified revisions.
- 684 policy-stage-aligned candidate transitions remain uncertified; Batch 001 has certified 9 exact April-2023 cell pairs against PIB statements and both source workbook hashes.
- 431 historical-panel/out-of-window transitions remain unresolved.
- Official PIB release page evidence is verified for 40 of 40 unique catalogue vintages. July 2024 and May 2025 were verified in the 3 Nov gap-closure addendum; see `IIP_OFFICIAL_RELEASE_GAP_CLOSURE_ADDENDUM_2026-11-03.md`.
- The April 2026 catalogue XLSX remains HTTP 404 even though the official Quick PDF exists.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 changes. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.

## 3 Nov 2026 official release-page gap closure
- July 2024: PIB PRID 2054214, 12 Sep 2024 17:30 IST, Quick Estimate.
- May 2025: PIB PRID 2140774, 30 Jun 2025 16:00 IST, Quick Estimate.
- Official page coverage: 40/40; UNKNOWN official release-page rows: 0.
- This closes only the PIB page lookup gap. April 2026 catalogue XLSX remains HTTP 404; certified cell-level revisions total 9 (Batch 001 only); Hard Gate remains BLOCKED.

## 5 Nov 2026 artifact re-verification — append-only
- Re-verified workflow Run #41646170762, job `validate`: conclusion `success`.
- Artifact ID: `13235815514`; artifact name: `iip-41-vintage-ingestion-revision-audit`.
- GitHub artifact digest and independently recomputed ZIP SHA-256 both equal: `5f9a2fa87b749607a750b4a1753be65f59483f004ad29c64a5a308329c7e4b90`.
- Current snapshot: 41 qualifying catalogue rows; 40 unique vintage IDs; 39 XLSX payloads downloaded and parsed; 1 HTTP 404; 125,220 observations; 1,124 observed within-series differences.
- Exact failed row: `IIPMFY26002APR`, April 2026, catalogue code 158504, HTTP 404, `HTTP_404`; retain as a failed raw-workbook acquisition, not a successful vintage.
- January 2026 remains a dedicated catalogue-row gap but its observations are present in six later vintages; do not label it a missing observation.
- Run success confirms the audit job and artifact upload only. The embedded audit status remains `BLOCKED_WITH_GAPS`; Hard Gate remains `BLOCKED`.
- The two release-page lookups were independently rechecked against PIB: July 2024 PRID 2054214 (12 Sep 2024 17:30 IST) and May 2025 PRID 2140774 (30 Jun 2025 16:00 IST). Official PIB page coverage remains 40/40.
- Remaining work: 684 policy-stage-aligned candidates are not cell-certified; 431 historical-panel/out-of-window transitions remain unresolved; April 2026 raw catalogue XLSX remains HTTP 404. Do not promote the 1,124 observed differences to certified revisions.
- This appendix changes documentation only; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 logic changed.
