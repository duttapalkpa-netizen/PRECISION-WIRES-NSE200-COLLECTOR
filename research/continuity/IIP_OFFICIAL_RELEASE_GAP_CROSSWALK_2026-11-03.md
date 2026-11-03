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
- 693 policy-stage-aligned candidate transitions remain uncertified pending exact source statement cell matching and per-source payload provenance.
- 431 historical-panel/out-of-window transitions remain unresolved.
- Official PIB release page evidence is verified for 38 of 40 unique catalogue vintages. July 2024 and May 2025 remain UNKNOWN, not inferred from adjacent months. See `IIP_OFFICIAL_RELEASE_EVIDENCE_LEDGER_2026-11-03.md`.
- The April 2026 catalogue XLSX remains HTTP 404 even though the official Quick PDF exists.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 changes. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.
