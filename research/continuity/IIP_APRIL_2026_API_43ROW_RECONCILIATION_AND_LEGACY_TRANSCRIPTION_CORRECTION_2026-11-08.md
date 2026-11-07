# April 2026 IIP — 43-row official API reconciliation and legacy transcription correction
Date: 2026-11-08
Status: PASS_ALL_43_API_ROWS_MATCH_LATEST_PIB; LEGACY_37_ROW_METADATA_QUARANTINED

## Why this correction is required
A later repository audit found that the April 2026 official MoSPI JSON API evidence had already been acquired and validated, but the recent Continuation 21 discussion focused on a separate 37-row PIB Statement IV transcription. The two artifacts must not be conflated. The 37-row CSV also carries a conflicting base-year label (2011-12=100) compared with the latest revised 2022-23 official release and API series. It is preserved for audit history but quarantined from current-series ingestion.

## Primary official API contract and retrieval
- Official OpenAPI source: https://esankhyiki.mospi.gov.in/layout/swagger_user_iip.yaml
- HTTP 200; content type application/octet-stream; OpenAPI 3.0.1; 11,226 bytes.
- Raw spec SHA-256: bed83ff75c1b361368019a55473ed29c9fcd7242651706cffea04debb65211e0.
- Explicit operation: GET /api/iip/getIIPData, production server https://api.mospi.gov.in/.
- Parameters documented: frequency (required), base_year (optional; description explicitly lists 1993-94, 2004-05, 2011-12, 2022-23), year, month_code, type, category_code, subcategory_code, limit, page, viz_req.
- Official API request: https://api.mospi.gov.in/api/iip/getIIPData?frequency=Monthly&base_year=2022-23&year=2026&month_code=4&type=All&viz_req=true
- Retrieved 2026-11-07T11:19:49.576191Z; HTTP 200; application/json; 8,129 bytes; 43 records (1 General, 36 Sectoral, 6 Use-based); raw response SHA-256 ba0ee42f7fb7809483a86dcbfe53057d401c51af67e28638c6603fcedcdca71a.
- Current CSV: data/macro/iip_apr2026_mospi_api_records.csv; 43 rows, 8 columns; CSV SHA-256 192267b76af8cc0bc524d33a86461d0d70906a96a34eadfdccea12b2245a82ee; commit 198ad7bccf5d6f634e0f0af6a5868119369f1921.
- Validation JSON: data/macro/iip_apr2026_mospi_api_validation.json; commit 6b0bd934152fb83fb258fc6a3ffce29f4dce4f86.

## Latest official revised PIB benchmark
- PIB PRID 2329475, 2026-10-28, official URL: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475
- Page explicitly identifies the latest IIP release as base 2022-23=100 (lines 70–79, 104–105, 217–219).
- April 2026 benchmark locations: Statement I April column (line 109); Statement III April row (line 197); Statement IV April-2026 NIC-2025 column (lines 219–260).
- The official page contains 43 expected April values: 1 General, 36 Sectoral, 6 Use-based.
- A dedicated reproducible comparison script is present at pipeline/verify_iip_api_apr2026_against_pib.py. It compares normalized (type, category, sub_category) keys and one-decimal index values; it does not recompute published growth rates.
- Final bounded dual-month audit Run 42381121341 (#12), job conclusion SUCCESS; commit 5f079524dfa7e1210005e46020fd9b6e109401e2; artifact ID 13577128037; artifact ZIP SHA-256 2337b9ed18d0057cac3a4c503a6d0657f0750df720f5a50878f14b3fc67d5059. Artifact independently re-downloaded; ZIP SHA-256 matched GitHub digest.
- Inside Run #12 artifact, April comparison JSON reports expected=43, observed=43, matched=43, missing=0, mismatches=0, unexpected=0, duplicate keys=0; status PASS_ALL_43_MATCH. April raw API response SHA-256 matches the earlier retained digest above.
- The same run independently matched May 2026 43/43 to the latest PIB revision; April + May = 86/86 month-record comparisons. May raw response SHA-256 0ca8a461028c2794da4683930805a6a2cfd95ba77a6eb0ae7519b9cb32c741db.
- PPI identity is corroborated by PIB PRID 2278961 (2026-06-29), which says the full 2022-23 series was revised using Output PPI and supersedes the earlier WPI-based series. API rows do not themselves include a deflator field; preserve that provenance caveat.

## Correction to the 37-row PIB transcription created in Continuation 21
- File retained unchanged: research/data/iip_april_2026_statement_iv_output_ppi_pib_transcription.csv; 37 rows, commit 65b1ed4304a7decc26fc39327e3211b5c3fe217f.
- It is a 37-row Statement IV-only transcription and omits the six use-based categories, so it is not a complete 43-row April dataset.
- Its metadata says base_year=2011-12=100, while the latest official revised April series in PRID 2329475 and the API request are base_year=2022-23. This makes the old file unsuitable as the current-series master data table.
- Action: preserve the file and its original QA report for audit history, but quarantine it from current-series joins and production inputs. Do not overwrite or silently relabel it.
- Current authoritative April data for the 2022-23 series is the 43-row official API CSV, validated 43/43 against PRID 2329475.
- Native catalogue XLSX remains NOT RECOVERED. The API is an official data source but does not satisfy the separate native XLSX file-provenance criterion.

## Task progress (scoped)
- Official API contract discovery and parameter schema: 100%.
- April 2026 API acquisition: 100% (43/43 rows returned).
- April latest-PIB reconciliation: 100% (43/43, zero discrepancy).
- May latest-PIB reconciliation: 100% (43/43, zero discrepancy).
- PPI series identity corroboration: 100% at series level, with no per-row deflator field.
- Native April catalogue XLSX recovery: 0% / NOT RECOVERED.
- Full 41-vintage source audit: still BLOCKED_WITH_GAPS.
- 37-row transcription: legacy supplemental evidence only; excluded from current-series ingestion.

## Hard-gate and architecture
IIP full audit remains BLOCKED_WITH_GAPS; master Hard Gate remains BLOCKED. API evidence does not certify all vintage revisions or 693 candidate transitions. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or V11.3(A/B/C/D/E) production logic changed. UNKNOWN remains neither PASS nor FAIL. Research spend ₹0.
