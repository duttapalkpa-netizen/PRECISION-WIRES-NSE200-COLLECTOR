# IIP Classification Scope Correction and Official API Contract Priority — 2026-11-05

## Why this correction is necessary
Earlier work over-prioritized full NIC-2025 ↔ NIC-2008 4-digit concordance extraction as if it were a direct prerequisite for the new IIP series. Official series-specific documentation shows that this is not the right critical path.

## Authoritative series-specific findings
1. MoSPI's FAQ for the new IIP series (base 2022-23), posted 26 May 2026, Q28 states that NIC-2025 is used to disseminate the new IIP at NIC 2-digit level. Official PIB FAQ: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2265637&lang=2&reg=3 ; official MoSPI FAQ PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf
2. PIB's TAC-IIP report release (25 May 2026) states that the new series will provide manufacturing indices at NIC-2-digit level and detailed data from April 2023 onwards: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2264966&lang=2&reg=48
3. The first new-series IIP release (1 June 2026) and its detailed data publication route are documented at: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3 ; e-Sankhyiki table/API landing page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip
4. MoSPI microdata catalogue metadata for IIP 2022-23 (DDI-IND-NSO-IIP-2022-23; metadata production date 29 June 2026) says manufacturing coverage is NIC divisions 10–32, item selection references NIC-2008 3-digit industry groups, and the new series uses Output PPI where applicable. It also states that geometric-mean linking factors are calculated at General Index and sectoral levels only. Source: https://microdata.gov.in/nada/index.php/catalog/299/study-description
5. The general MoSPI FAQ currently contains a statement that the current IIP classification is NIC-2008. This conflicts with the newer, series-specific new-IIP FAQ (Q28) and the TAC-IIP release. Treat the generic FAQ statement as stale for the 2022-23 series; do not apply it to the new series without further official reconciliation.

## Research interpretation / corrected scope
- Old IIP 2011-12 series and the new IIP 2022-23 series have different classification contexts. New-series NIC-2 dissemination uses NIC-2025; manufacturing item selection metadata references NIC-2008 3-digit groups.
- The official 4-digit NIC-2025 ↔ NIC-2008 concordance remains useful as a classification lineage/reference artifact, but it is NOT a prerequisite for ingesting the new IIP NIC-2 tables.
- The concordance explicitly uses `(p)` for partial and `+` for aggregation. Therefore, do not derive a NIC-2 crosswalk by truncating codes, flattening expressions, or assuming one-to-one mapping.
- No NIC-2 linking factor may be inferred from 4-digit concordance. Official series linking factors are only General Index and sectoral level.
- Priority is now direct acquisition of the official new-series IIP tables/API data from April 2023 onward, with NIC-2025 division codes, month, index, growth, use-based/sectoral category, revision status, release date, source URL, and raw-byte hash where a downloadable file exists.

## New implementation committed
- `pipeline/audit_official_iip_api_contract.py` fetches only the official e-Sankhyiki Swagger contract at https://esankhyiki.mospi.gov.in/layout/swagger_user_iip.yaml, hashes the raw YAML, parses exact endpoints/parameters/security/base-year enum, and explicitly does NOT call the data API.
- `.github/workflows/official_iip_api_contract_audit.yml` runs the contract audit manually with a 5-minute timeout and uploads the official spec plus JSON report.
- Workflow dispatch was not performed in this session; no run ID, API response, or raw source hash is claimed.

## Concordance parser safety correction
- The previous parser's use of `\s` across a whole PDF text stream could cross line boundaries and incorrectly merge adjacent table rows. This is a material parsing risk.
- The extractor has been changed to parse one visual text line at a time, require explicit `+` between NIC-2008 class tokens, preserve `(p)`, and fail closed when row layout is not machine-readable.
- Runtime regression assertions cover direct mapping, partial/aggregate mapping, multi-token plus expressions, and refusal to parse two rows joined by a newline.
- This parser update is code-level only and has not yet been exercised against the downloaded official PDF binary.

## Current priority / status
NEW_SERIES_IIP_NIC2025_NIC2_DISSEMINATION: OFFICIAL_SERIES_SPECIFICALLY_VERIFIED
OLD_VS_NEW_CLASSIFICATION_CONTEXT: DOCUMENTED
NEW_SERIES_ITEM_SELECTION_NIC2008_3DIGIT_REFERENCE: DOCUMENTED_FROM_METADATA
OFFICIAL_IIP_API_CONTRACT_RAW_BYTES_AND_SHA256: PENDING_WORKFLOW_RUN
API_PARAMETER_SCHEMA_AND_AUTHENTICATION: PENDING_OFFICIAL_SPEC_PARSE
NEW_SERIES_IIP_MONTHLY_DATA_INGESTION: PENDING
4DIGIT_CONCORDANCE_EXTRACTION: OPTIONAL_REFERENCE_NOT_CRITICAL_PATH
NIC2_CROSSWALK_FROM_4DIGIT_TABLE: NOT_CERTIFIED_AND_NOT_TO_BE_INFERRED
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED

## Protected invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or V11.3(A/B/C/D/E) logic changed. No historical PASS artifacts were deleted or rewritten. No synthetic rows, fabricated timestamps, unsupported source promotion, or Hard Gate relaxation.