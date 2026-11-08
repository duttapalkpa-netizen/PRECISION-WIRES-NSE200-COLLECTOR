# April 2026 IIP: superseding Output-PPI series and current-data extraction audit

Audit date: 2026-11-08
Scope: establish the authoritative current-series lineage for the April 2026 NIC-2025 manufacturing index values; preserve the original first-release record without treating it as current.

## 1. Authoritative release lineage

- 01 June 2026: MoSPI first press release of the 2022-23 IIP series, including Statement II-A, NIC-2025. The release uses WPI as deflator for value-reported items. Official PDF:
  https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- 29 June 2026: MoSPI May 2026 release, Release ID `IIPMFY26006MAY`, adopts Output PPI instead of WPI and explicitly states that the PPI-based series supersedes the WPI-based 2022-23 series released on 01 June. It also states that updated source-agency data from April 2022 onward were incorporated.
  Official PIB release:
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&reg=48&lang=2
- The May release's Statement II-A (NIC-2025, base 2022-23=100) supplies May 2026 index and Apr-May cumulative index values for NIC 10-32. Its separate "INDEX OF INDUSTRIAL PRODUCTION - MONTHWISE" table explicitly declares base 2011-12=100. The 2011-12 table must not be used as the revised PPI-based 2022-23 monthly series.

## 2. Consequence for the existing 23-row ledger

The 23 values sourced from the 01 June first-release PDF remain valid historical evidence of what that first WPI-based release published. They are not the current PPI-based April 2026 series values after the 29 June supersession.

The ledger now explicitly records, for every NIC 10-32 row:
- `first_release_deflator=WPI`
- `first_release_series_status=SUPERSEDED_BY_OUTPUT_PPI_SERIES`
- `superseded_by_release_id=IIPMFY26006MAY`
- `superseding_release_date=2026-06-29`
- `superseding_deflator=Output PPI`
- `current_series_apr2026_index_status=NOT_YET_EXTRACTED_FROM_COMPARABLE_CURRENT_SERIES_SOURCE`

The previously quarantined 2011-12 monthwise values remain raw observations only. Revision fields remain blank / UNKNOWN, and no cross-base-year arithmetic is performed.

## 3. Current data access findings

- MoSPI e-Sankhyiki's official portal identifies current IIP base year 2022-23 and says its Macro Indicators module supports filtered CSV downloads without registration.
  Portal: https://esankhyiki.mospi.gov.in/macroindicators?product=iip
- The e-Sankhyiki Data Catalogue exposes monthly NIC-2 and sectoral IIP table records; for example the August 2026 catalogue record is `IIPMFY26018AUG`. This confirms a public catalogue route for current-series detailed tables.
  Catalogue: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
- The official e-Sankhyiki IIP API documentation currently published in the NSO India `esankhyiki-mcp` repository declares a Bearer Authorization requirement and lists only base_year values `2011-12`, `2004-05`, and `1993-94`. It does not document 2022-23 in the API enum. Do not guess new parameters, call the API with undocumented values, or bypass authentication.
  API specification: https://github.com/nso-india/esankhyiki-mcp/blob/main/swagger/swagger_user_iip.yaml
  API server: https://api.mospi.gov.in/api/iip/getIipData
- No login, token, or private credentials were used. No API call was attempted using unsupported parameters.
- The May release's Statement II-A gives May monthly and Apr-May cumulative values; it does not provide the standalone April 2026 PPI-based NIC-2 values in that statement. The separate monthwise table is 2011-12 base. Do not derive April by subtracting or averaging cumulative values unless MoSPI's exact aggregation methodology and inputs are independently evidenced.

## 4. Next exact action

Use the public e-Sankhyiki Macro Indicators / Data Catalogue interface to select IIP, current 2022-23 Output-PPI series, monthly NIC-2 digit and sectoral indices, and reference period April 2026. Download the official filtered CSV or catalogue Excel table. Preserve its download URL, table ID, release/vintage date, metadata, file bytes, and SHA-256. Then independently validate all 23 NIC codes and values against the current series.

If the portal does not expose a standalone April current-series table, retain the status as ACCESS_NOT_YET_ESTABLISHED and request the downloaded official export from the account holder; do not infer it from cumulative figures.

## 5. Acceptance and safety status

- Historical WPI first-release ledger: preserved and explicitly marked superseded.
- Current PPI-based April 2026 NIC-2025 values: not yet extracted.
- Same-series April revision check: pending.
- Raw first-release PDF SHA-256: pending.
- IIP acceptance: BLOCKED; project-wide hard gate remains BLOCKED.
- No synthetic values, re-basing, cross-series arithmetic, or unsupported API calls.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and all 672 diagnostics unchanged.
- Spend: ₹0; official sources only.

This audit note supplements the prior cross-base-year contamination audit and supersedes any interpretation that the June 01 WPI first-release values remain the current Output-PPI series.

## 6. Additional official Output-PPI source located on 2026-11-08

- The Office of the Economic Adviser (OEA), DPIIT, official page `https://eaindustry.nic.in/download_data_2223.asp` is titled "Index Files For WPI & PPI Series (Base Year = 2022-23)" and lists monthly/quarterly Output Producer Price Index (OPPI) index files from April 2023 onwards.
- OEA's 15 June 2026 Output PPI release states that SUT category-wise Output PPI indices from April 2023 to May 2026 are available from that download page: `https://eaindustry.nic.in/press_release/press_release_202606.pdf`.
- This is a useful official source for the **deflator input series**, but it is not itself the MoSPI IIP NIC-2025 manufacturing output index table. Do not substitute OEA OPPI values for the 23 IIP NIC-2 index values.
- The OEA download page could not be fetched in this runtime (timeout), and no OPPI file bytes, file name, download URL, or SHA-256 were captured in this audit. Treat OEA file extraction as not yet complete.
- The e-Sankhyiki catalogue search result confirms the August 2026 monthly NIC-2/sectoral IIP table ID `IIPMFY26018AUG`; a separate April 2026 catalogue record/table ID was not independently exposed by the public search/index used here. Do not infer an April table ID from the August sequence.
- The e-Sankhyiki Macro Indicators page is JavaScript-rendered and returned no readable table content in this runtime. The official portal FAQ says filtered CSV downloads are available without registration, but this audit has not captured the April 2026 export bytes.

Updated status on 2026-11-08:
- Official route for Output PPI deflator files: IDENTIFIED (page-level only; file not downloaded).
- April 2026 current PPI-based IIP NIC-2 catalogue table ID: NOT_VERIFIED.
- April 2026 current PPI-based IIP NIC-2 values 10-32: NOT_EXTRACTED.
- Raw June 01 WPI first-release PDF SHA-256: PENDING; the exact MoSPI PDF URL returned 403 in the web fetcher and DNS resolution failure in the container download runtime. No substitute hash is acceptable.

## 7. May 2026 Output-PPI IIP Statement II-A transcription (2026-11-08)

- Official source: MoSPI/PIB May 2026 IIP release, Release ID `IIPMFY26006MAY`, posted 29 June 2026:
  https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616
- The release explicitly says the entire 2022-23 IIP series was revised with Output PPI and supersedes the WPI-based 01 June series; users are advised to use the PPI-based series (release paragraphs 8-10, 27-28).
- Statement II-A contains NIC-2025 codes 10-32 and publishes May 2026 monthly index, May 2025 comparison index, Apr-May cumulative index, and growth rates. It does **not** publish a standalone April 2026 monthly index column in that statement.
- A source-faithful 23-row transcription was added:
  `audit_inputs/iip_may2026_output_ppi_nic2025_statement_IIA_transcription.csv`
  Commit: `963cf6b9e86ed7bff8da57af9240183b1f4f8149`
  Blob SHA: `efbc8940fb1bac66dddb927444ebada5394401a4`
- Verification performed after write: 23 data rows; NIC codes exactly 10 through 32 in contiguous order; all rows identify base year 2022-23, NIC-2025, release ID/date and Statement II-A; every row explicitly marks standalone April 2026 index as `NOT_PRESENT_IN_STATEMENT`.
- This is a separate evidence artifact for the May release. It is not substituted into the April 2026 ledger and does not claim to complete the 23 April values.
- The April and May cumulative values must not be used to infer April values unless an official, documented aggregation formula and required inputs are available. No inferred April values are created.
- Current April 2026 NIC-2 PPI-IIP catalogue table ID remains NOT_VERIFIED from the accessible catalogue index. Catalogue search confirms current monthly NIC-2 table `IIPMFY26018AUG` for August 2026 only.
- Raw first-release PDF SHA-256 remains PENDING: the official PDF URL is confirmed, but the runtime download attempt failed with DNS resolution error; no bytes or hash were produced.

Acceptance status remains:
- May 2026 PPI-based NIC-2025 evidence transcription: PASS (23/23 rows and codes verified).
- April 2026 standalone PPI-based NIC-2 IIP values: NOT_EXTRACTED.
- April 2026 exact catalogue table ID: NOT_VERIFIED.
- Original WPI PDF raw SHA-256: PENDING.
- IIP sub-audit and project hard gate: BLOCKED; no production logic changed.

## 8. First-release PDF byte-provenance follow-up (2026-11-08)

### Official HTML copy independently accessible

- PIB official release page for the 01 June 2026 first release is accessible:
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- The page identifies the Ministry of Statistics & Programme Implementation, title "FIRST PRESS RELEASE OF ALL INDIA INDEX OF INDUSTRIAL PRODUCTION OF NEW SERIES WITH BASE YEAR 2022-23", and posting date 01 June 2026.
- The page's Statement II-A is explicitly headed "INDEX OF INDUSTRIAL PRODUCTION - (Manufacturing at NIC 2 digit)" and "(Base: 2022-23=100)", with NIC 2025 codes and April 2026 quick-estimate index column. The table is available in the accessible HTML at lines 79-109 of the rendered page.
- The 23 first-release April 2026 index values in the existing ledger match the official PIB HTML Statement II-A at displayed precision. The HTML is a second accessible official representation of the release content, not the original PDF byte stream.
- The PIB page does not expose a direct raw-PDF byte response in the accessible rendering.

### Raw PDF checksum status

- Exact official MoSPI PDF URL remains:
  https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- A fresh web fetch on 2026-11-08 returned HTTP 403 Forbidden.
- A fresh runtime HTTP request failed DNS resolution for www.mospi.gov.in before any response bytes were received.
- Therefore no raw PDF bytes were acquired and no SHA-256 can be computed. The earlier status remains PENDING; do not substitute the HTML page hash, CSV hash, browser-rendered page hash, or a guessed value.
- This does not invalidate official content verification of the 23 table values, but raw-file byte provenance remains incomplete.

### Updated evidence interpretation

- First-release table values: independently supported by the official PIB HTML Statement II-A and earlier PDF visual/text review.
- Original PDF byte checksum: NOT AVAILABLE / PENDING.
- First-release ledger remains provisional specifically for raw PDF byte provenance.
- First-release values remain historical WPI-based observations and are superseded by the 29 June 2026 Output-PPI series. They must not be presented as current PPI values.
- No synthetic data, inferred hash, cross-base-year arithmetic, or production logic changes.

## 9. Two-source independent current-series cross-check and duplicate-count correction (2026-11-08)

- The 28 September 2026 PIB/MoSPI IIP release (Release ID `2315957`) and the 28 October 2026 release (Release ID `2329475`) are the two distinct official releases used for the April 2026 NIC-2025 Statement IV cross-check.
- Official September release: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2315957&lang=1&reg=3
- Official October release: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2329475&lang=2&reg=48
- All 23 April 2026 values (NIC 10-32) match across the workbook-derived ledger and both separately published official Statement IV releases.
- A schema review on 2026-11-08 found that Release ID `2329475` had been represented twice in the CSV and validator under both `second_official` and `third_official` field groups. These were not two independent sources. The duplicate third-source columns and checks have now been removed; the validator explicitly rejects reintroduction of `third_official_*` duplicate-source fields.
- The evidence count is therefore **two distinct official releases**, not three. No claim of a third independent release is made.
- The duplicate-source correction does not change any of the 23 April index values, workbook hash, base year, classification, or the two actual release IDs. The current-series validator continues to pin both official release metadata sets and all 23 index values.
- The exact April 2026 e-Sankhyiki catalogue table ID remains NOT_VERIFIED. The August catalogue ID `IIPMFY26018AUG` must not be re-labelled as an April ID.
- Raw first-release WPI PDF SHA-256 remains PENDING; this separate byte-provenance gap is unaffected.

## 10. Official e-Sankhyiki catalogue/API capability re-check (2026-11-08)

### Catalogue search result
- Official e-Sankhyiki catalogue page: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
- The currently indexed catalogue result identifies the monthly NIC-2 digit and sectoral IIP table for reference period Aug 2026 as `IIPMFY26018AUG`, release date 28 September 2026.
- Exact April 2026 NIC-2 current-series table ID was not returned by the official catalogue page rendering or targeted public search. The catalogue page is JavaScript-rendered and has no readable page lines in the current retrieval environment.
- The August ID is evidence only for August. No April ID is derived by changing the month suffix or decrementing any sequence.

### Official MoSPI MCP/API documentation check
- The NSO India / MoSPI e-Sankhyiki MCP repository publishes its source code and documents the sequential workflow `list_datasets -> get_indicators -> get_metadata -> get_data`.
- Repository: https://github.com/nso-india/esankhyiki-mcp
- Source file: https://github.com/nso-india/esankhyiki-mcp/blob/main/mospi_server.py
- In the published IIP metadata documentation, supported IIP base-year values are explicitly listed as `2011-12`, `2004-05`, and `1993-94`; the IIP metadata implementation also defaults to `2011-12`. The published documentation does not list the 2022-23 series.
- Source lines in the currently rendered GitHub page: 3056-3068 (base-year and IIP frequency parameter documentation) and 3147-3166 (IIP metadata implementation and stated coverage).
- This means the documented IIP MCP/API route is not currently an evidenced route for querying the 2022-23 NIC-2025 April 2026 current series. No unsupported base-year value was submitted; no API request was made using undocumented parameters; no authentication bypass or credentials were used.
- The same repository README describes the API workflow and says metadata-returned filter values must be used as-is. This reinforces the no-guessing rule; it does not establish April catalogue ID.

### Updated access conclusion
- April 2026 exact catalogue table ID: `NOT_VERIFIED`.
- April 2026 current-series standalone IIP export bytes and download URL: `NOT_CAPTURED`.
- Publicly indexed August 2026 monthly NIC-2 table ID: `IIPMFY26018AUG` (not reusable as April).
- Official API/MCP documented IIP base-year coverage for this route: legacy bases only; 2022-23 unsupported in published parameter documentation.
- Next valid path: capture the exact April export through the official portal UI or an official downloadable catalogue record whose metadata explicitly states reference period Apr 2026, base year 2022-23, NIC-2025, and table identifier. If no such record can be observed, retain `NOT_VERIFIED` and do not manufacture a locator.
- No values or table IDs were inferred, no old base-year data were promoted, no production code was changed, and project Hard Gate remains BLOCKED.


## 11. Official portal IIP API tab and authentication/parameter boundary (2026-11-08)

- The official e-Sankhyiki IIP Macro Indicators page exposes an `API` tab. The rendered portal documentation identifies the IIP endpoint as `GET /api/iip/getIIPData` and links its OpenAPI description as `swagger_user_iip.yaml`.
  Portal API tab: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
- The matching published NSO India / MoSPI OpenAPI specification is available at:
  https://github.com/nso-india/esankhyiki-mcp/blob/main/swagger/swagger_user_iip.yaml
- The specification declares the endpoint `/api/iip/getIipData`, requires a `base_year` query parameter, and enumerates only `2011-12`, `2004-05`, and `1993-94`. It also declares a Bearer Authorization header. The current published spec therefore does not document a 2022-23 parameter value for this IIP API endpoint.
- The official portal API tab was directly observed on 2026-11-08. The linked YAML itself could not be fetched from the portal host in this runtime because the response was served as `application/octet-stream`; the corresponding NSO India repository copy was inspected and its blob SHA is `d9acaccf1557825f2a093c7f826b15d659f2c646`.
- No bearer token, login, private credential, guessed parameter, or API request was used. No authentication was bypassed.
- This finding narrows the earlier API conclusion: the **published IIP API specification** is legacy-base-only and token-protected. It does not prove that the separate open-access catalogue or Macro Indicators UI lacks a 2022-23 downloadable table. The UI/CSV route remains distinct and must be tested through its visible filters and exported file.
- Decision: do not attempt this API for the 2022-23 April 2026 NIC-2025 cross-check unless MoSPI publishes a revised specification/metadata explicitly including that base year and lawful access is available. Continue with the public catalogue/UI route; retain exact table ID and export bytes as NOT_VERIFIED / NOT_CAPTURED until observed.
- No data values, catalogue IDs, or authentication material were inferred. All production invariants and project gate status remain unchanged.
