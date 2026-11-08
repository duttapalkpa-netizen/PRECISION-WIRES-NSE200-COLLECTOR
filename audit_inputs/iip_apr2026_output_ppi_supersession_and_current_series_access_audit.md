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
