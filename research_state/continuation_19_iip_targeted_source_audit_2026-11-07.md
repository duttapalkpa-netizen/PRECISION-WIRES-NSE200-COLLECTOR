# PRECISION-WIRES V11.3 — Continuation 19 targeted IIP source audit
Date: 2026-11-07
Page: গবেষণা যাচাই অব্যাহত 19

## Scope and no-repeat control
This is a targeted continuation of the unresolved April 2026 IIP native-source recovery. The continuation-18 PIB crosswalk, crosswalk QA, and source-discovery note were not recreated or modified.

## New verified official evidence
1. The official e-Sankhyiki IIP API page exposes the endpoint label GET /api/iip/getIIPData and links the OpenAPI document at ../../layout/swagger_user_iip.yaml. Browser retrieval of the YAML fails with HTTP/tool content-type limitation (application/octet-stream). Therefore the parameter schema, response fields, and valid monthly filters remain UNVERIFIED. Official API page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
2. The official e-Sankhyiki catalogue currently indexes 4,784 entries and its latest IIP catalogue page shows August 2026 tables:
   - IIPMFY26020AUG: monthly use-based classification
   - IIPMFY26017AUG: annual NIC-2 digit/sectoral indices
   - IIPMFY26019AUG: annual use-based indices
   - IIPMFY26018AUG: monthly NIC-2 digit and sectoral indices
   Source: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
3. Exact official catalogue search for April 2026 table IDs did not return an indexed matching result. The existing legacy record IIPMFY26002APR remains HTTP 404 according to the previously committed audit. Do not infer a replacement ID from the August naming pattern.
4. Official MoSPI portal FAQ states that the IIP dissemination contains monthly indices and growth rates at sectoral, NIC 2-digit and use-based levels; item-group production and indices are provided through the micro-data catalogue to registered users. This distinction matters: the public catalogue workbook and restricted microdata should not be conflated. Source: https://mospi.gov.in/faq
5. Official PIB release 2278961 (29 June 2026) supersedes the 1 June WPI-based 2022-23 series with the Output-PPI-based series and says updated source-agency data from April 2022 onward were incorporated. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
6. Official e-Sankhyiki home page describes the current IIP base year as 2022-23 and says portal Macro Indicators datasets can be downloaded as CSV, while Catalogue datasets are downloadable as Excel. Source: https://esankhyiki.mospi.gov.in/

## Outcome
- Native April 2026 PPI-based MoSPI workbook: NOT RECOVERED.
- API schema/filters: NOT VERIFIED.
- Catalogue confirms a current monthly/annual table family, but does not identify the April 2026 PPI-based table ID or download URL from available indexed content.
- No guessed API parameters, URLs, table IDs, or data values were used.
- No data was downloaded, parsed, or promoted into the research dataset.
- IIP audit remains BLOCKED_WITH_GAPS; Hard Gate remains BLOCKED.

## Next bounded action
Continue through official e-Sankhyiki's user-facing metadata/table workflow to identify the April 2026 row and its current PPI-based table metadata. If the portal exposes only API data/CSV, record that as a distinct official source format; do not assert an XLSX exists unless the catalogue itself exposes it. Use exact filter values only after official metadata/API schema is readable. Capture the raw response, retrieval timestamp, URL, response headers/content type, row count, and SHA-256 before parsing.

## Progress accounting
- Official API route discovery: complete (endpoint path only).
- API schema and monthly filter verification: 0%.
- April 2026 current PPI native workbook/source recovery: 0%.
- IIP monthly ingestion count remains 39/41 = 95.1%; this is period ingestion coverage only, not audit completion.
- No defensible new overall research percentage calculated. Last recorded overall baseline remains 36%, not re-certified.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, and CORE-672 remain untouched.


## Completed bounded task — September 2026 IIP metrics and full NIC-2 CI QA (2026-11-07)
- Workflow previously manual-only was safely extended to trigger on pushes touching only the two September 2026 source CSVs, their validators, or the workflow file. Branch-scoped to `fix/iip-41-vintage-audit-clean`; timeout remains 5 minutes; artifacts uploaded even on failure. No main branch automation.
- Run `42400271361` SUCCESS, commit `fe9f87a37bb110a5202729c721a8713a671b6392`: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/42400271361.
- Artifact ID `13584194796`, ZIP SHA-256 `6a97828061391dece1825a1b26c1daea65ad1705c6edef92468e5510cf54956b`; downloaded ZIP hash independently matches GitHub digest.
- Release metrics QA: `PASS_TRANSCRIPTION_AND_STRUCTURE_QA`, 19 rows, 19 unique keys, 0 errors; CSV SHA-256 `79ff77d60d6ad3e776a5aa68fedec3a4891269c5b196a2c4f50b558b30d39540`; JSON SHA-256 `33a55d1e6eccd10dd361c02783a901ca0e3e90729c2f5f8b6a5cd849024d1bd1`.
- NIC-2 Statement II-A QA: `PASS_TRANSCRIPTION_STRUCTURE_AND_ARITHMETIC_QA`, 23/23 codes 10–32, 0 errors; positive/negative/zero groups 17/6/0; weight sum 76.065 vs official 76.062, +0.003 rounding within ±0.005; source CSV SHA-256 `102bef6c87b95c1478686935d9a6f5fcacda90dce07ea48f36d09e340fc29b7f`; JSON SHA-256 `5e22145ecd4e96f7881a427a1cd556b2ca9f689350dad83e31fbef23573493c0`.
- Report: `research/continuity/IIP_SEPTEMBER_2026_RELEASE_QA_CI_RESULT_2026-11-07.md`, commit `4630e2a56c4bf55e2e1dbd64f25a3dedc50d9d38`.
- Scope boundary: transcription/schema/arithmetic QA only. Raw PIB PDF binary hash still NOT_ACQUIRED; not a full April-2023 onward monthly panel, not full vintage revision audit. IIP full audit/Hard Gate remain BLOCKED. Overall research remains last defensible 36% baseline. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 unchanged; ₹0.


## Completed next priority — IIP 41-month catalogue coverage reconciliation (2026-11-07)
- Re-downloaded immutable Run `41640521553`, Artifact ID `13232127900`; verified its ZIP SHA-256 against retained digest `e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c`.
- Reconciled all 40 unique rows in `vintage_ingestion_manifest.csv` against 41 calendar months from 2023-04 through 2026-08.
- Exact result: 39 parsed XLSX vintages; April 2026 catalogue ID `IIPMFY26002APR` returned HTTP 404; January 2026 has no record in the manifest. Distinguish absent catalogue record from present-but-404 record; no table ID inferred.
- Parsed legacy segment: 35 vintages Apr-2023–Mar-2026, base 2011-12/NIC-2008. Parsed new segment: 4 vintages May–Aug 2026, base 2022-23/NIC-2025. April 2026 is unassigned/UNKNOWN because workbook unavailable. Never concatenate across base-year/deflator breaks.
- Created `research/continuity/IIP_MONTHLY_CATALOGUE_COVERAGE_RECONCILIATION_2026-11-07.md` commit `f58c76a22d0db436534fbc71b2447d75a45a1430`; companion 41-month ledger `research/data/iip_monthly_catalogue_coverage_2023-04_to_2026-08.csv` commit `afbaa057279df6b30466655e6c7ba281b3ea4a12`.
- Period coverage: 40/41 months represented; 39/41 successfully parsed. These are period counts, not observation/cell certification rates.
- Remaining: resolve official January 2026 catalogue record and April 2026 Output-PPI vintage independently; 693 candidate transitions remain uncertified; 431 historical/out-of-window unresolved. IIP full audit/Hard Gate BLOCKED. Overall research stays at last defensible 36% baseline. Invariants unchanged; ₹0.


## Completed bounded task — January 2026 official PIB release gap reconciliation (2026-11-07)
- Independently verified official MoSPI/PIB PRID 2234512, published 2026-03-02 16:00 IST: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2234512&lang=1&reg=3
- The official release confirms January 2026 IIP Quick Estimate, base 2011-12=100, NIC-2008 2-digit and use-based statements. General index 169.4 and YoY growth 4.8%; sector indices/growth: Mining 157.2/+4.3%, Manufacturing 167.2/+4.8%, Electricity 212.1/+5.1%.
- This resolves the ambiguity: January is absent from the prior XLSX catalogue manifest, but an official PIB monthly release exists. Keep the two source channels distinct. Do not infer a catalogue table ID or claim native XLSX recovery.
- New report: `research/continuity/IIP_JANUARY_2026_OFFICIAL_RELEASE_GAP_RECONCILIATION_2026-11-07.md`, commit `3a86a7a71683fc20bf61c7ed484b67021c80860b`.
- January official release identification/classification: 100% complete. Native catalogue table/XLSX recovery: still open; observation-level transcription and independent cell QA: not performed. April 2026 Output-PPI source recovery and API schema verification remain open.
- IIP full audit remains BLOCKED_WITH_GAPS; master Hard Gate BLOCKED. Overall research stays at last defensible 36% baseline. Production invariants unchanged; ₹0.
