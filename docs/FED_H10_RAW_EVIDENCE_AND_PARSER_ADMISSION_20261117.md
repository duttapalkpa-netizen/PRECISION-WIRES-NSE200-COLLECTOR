# Fed H.10 Raw Evidence Capture and Parser Admission — 2026-11-17

## Status
- Official raw H.10 ZIP acquisition: PASS
- ZIP integrity: PASS
- Transport metadata and SHA-256: PASS
- Broad Dollar Index XML extraction: PASS
- Evidence Manifest V1: PASS (for the broad-dollar series)
- Existing overlay parser trusted-row validation: PASS
- Parser-admitted observations: 5,445
- Production / classifier integration: NOT_DONE / NOT_AUTHORIZED

## Exact acquisition
- Official endpoint: https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10
- GitHub workflow run: #6, ID 44035209336
- Workflow commit: 7faddf575e5f772f3823912dc2ad06b37842118f
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44035209336
- HTTP status: 200
- Content-Type: application/x-zip-compressed
- Retrieved UTC: 2026-11-17T06:59:11.059096+00:00
- Source package Prepared timestamp: 2026-11-16T16:47:01 (source publication vintage)
- Raw response byte length: 2,088,268
- Raw response SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77
- ZIP members integrity test: PASS
- Artifact ID: 14306184279
- Artifact name: fed-h10-official-evidence-44035209336
- Artifact ZIP byte length: 2,049,328
- Artifact ZIP SHA-256: 5fb36967f83329693a72e78ac6e9472469dd9ea1c29940b79a1efed9c39d2e74
- Artifact URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44035209336/artifacts/14306184279
- Artifact expiry: 2027-02-15T06:59:04Z. GitHub Actions artifact is retained for 90 days; it is not a permanent repository archive. Preserve/download it before expiry if long-term raw-byte retention is required.

## Exact qualified series and parser admission
- Series ID: JRXWTFB_N.B
- Indicator: fed_h10_nominal_broad_dollar_index
- Unit: Index:_1997_Jan_100
- Unit multiplier: 1
- Manifest ID: fed-h10-jrxwtfb_n-b
- Observation count in XML: 5,445
- Parser-admitted count: 5,445
- First observation: 2006-01-02 = 101.4155
- Latest observation: 2026-11-13 = 122.6503
- Parser admission result file: fed_h10_parser_admission.json (status PASS)
- Validation was executed by calling the existing `pipeline.global_capital_rotation_overlay.load_observations` from the capture job, not by a parallel imitation parser. This confirms exact source tuple, manifest fields, timestamps, content type, byte length, raw path containment and independently recomputed SHA-256 for all 5,445 rows.

## Other series found in the same official ZIP — NOT admitted
- JRXWTFN_N.B, nominal advanced-economy dollar index: 5,445 observations.
- JRXWTFO_N.B, nominal emerging-market dollar index: 5,445 observations.
- RXI_N.B.IN, H.10 INR bilateral series: 14,054 observations.
- These were extracted and documented for discovery only. They are not in the source registry and were not submitted to the parser as trusted observations. Do not treat the RXI unit string "Currency" as a complete unit definition without verifying the series description/convention. Do not conflate any of these with ICE DXY.

## Failed attempts and correction trail
- Capture run #3 (ID 44034776365) failed on a Python syntax error in manifest JSON construction; corrected.
- Capture run #5 (ID 44035148072) failed because the script directory, not repository root, was on Python import path; corrected by adding the repository root before importing the existing parser.
- Capture run #6 (ID 44035209336) completed SUCCESS and the parser admission summary reported PASS for 5,445 broad-dollar observations.
- The earlier #1 and #2 capture runs confirmed raw ZIP transport capture and XML extraction but did not exercise parser admission. Do not count them as parser PASS.

## Acceptance boundary
- Fed H.10 broad-dollar source identity and exact tuple: VERIFIED.
- Raw payload + transport evidence: VERIFIED for run #6 artifact.
- Broad-dollar observation parser admission: PASS, 5,445 observations.
- Long-term immutable raw archive in Git repository: NOT_DONE; current artifact retention expires 2027-02-15.
- Historical point-in-time validation across vintages: NOT_DONE; this is one H.10 publication vintage, not a full vintage archive.
- 20-session derived return/change: NOT_DONE; no calculation or forward-fill was authorized here.
- Mapping to existing `dxy_change_pct_20d`: NOT_AUTHORIZED; this is Fed nominal broad dollar index, not ICE DXY.
- Overlay classifier integration and production use: NOT_AUTHORIZED.

## Next permitted task
Build a small, explicit derived-series specification and QA test for a clearly named Fed H.10 broad-dollar 20-session change, using only valid observation dates and preserving gaps/ND. Before calculating, decide and document session calendar semantics (H.10 daily observation days vs Indian trading sessions), require 20 valid prior observations, no forward fill, and PIT cutoff by the source Prepared vintage. Keep the result separate from `dxy_change_pct_20d`. Do not add the other three series to registry until their exact descriptions/units are separately qualified.


## Correction addendum — 2026-11-17 (supersedes initial count above)
- The original collector skipped literal value strings `ND` but the H.10 XML encodes not-available observations with numeric sentinel `-9999.0` and `OBS_STATUS=ND`. The original 5,445 parser-admitted count therefore incorrectly included 214 ND records. Treat the original 5,445 admission count above as SUPERSEDED, not valid.
- XML source records: 5,445; `OBS_STATUS=A`: 5,231; `OBS_STATUS=ND`: 214. The corrected collector admits only `OBS_STATUS=A` with ISO date and finite numeric value.
- Corrected capture workflow #8 / ID 44036104490 SUCCESS; commit 4e3da948ff04e1d8efe50ee3782a16c4814e8965; artifact 14306134441; artifact SHA-256 2d9a4808cd9e48ac21175b8a79ccf42173f57f2370086e24832e4d460afbe4ba. Parser admission PASS for 5,231; 214 excluded.
- Corrected 20-valid-observation result: 2026-10-15 121.5693 to 2026-11-13 122.6503 = +0.8892047581% (rounded +0.8892%), using 20 prior valid H.10 observations plus current. 2026-11-11 ND is excluded; no fill.
- Full correction/result: docs/FED_H10_20OBS_DERIVED_SERIES_RESULT_20261117.md. Regression workflow #232 / ID 44036012995 SUCCESS, 72 tests in 0.056s.
