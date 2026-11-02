# Macro-Geo P0 source separation and collector validation audit — 2026-11-02

## Scope
Research-only. Window: 2025-10-01 through 2025-10-10. No production selector, scoring, pressure-fade, or 672-diagnostic changes.

## Official endpoint findings

| Group | Official endpoint / route | Established | Not established |
|---|---|---|---|
| Benchmark index | https://www.nseindia.com/reports-indices-historical-index-data | Dedicated NSE Historical Index Data page, index selector, date controls and CSV control. | No selected-window raw CSV or direct download URL retrieved. |
| Sector indices | https://www.niftyindices.com/reports/historical-data | NSE Indices historical-data interface and sectoral index catalogue, including AUTO, BANK, IT, METAL. | No selected index/date-range CSV bytes retrieved. Do not reuse broad NSE CSV as independent sector evidence. |
| India VIX | https://www.nseindia.com/reports-indices-historical-vix | Separate NSE India VIX historical page; Date/Open/High/Low/Close/Prev Close/Change/% Change fields and CSV control. | Current scrape returned No Records; direct October 2025 CSV URL and bytes not established. |
| Geopolitical events | https://www.pib.gov.in/AllRel.aspx?lang=1&reg=3 ; https://www.mea.gov.in/advanced-search-list.htm | PIB PRID 2175552 shows 06 Oct 2025 7:50 PM publication time. | Raw HTML/PDF bytes not archived here. MEA advanced search is discovery, not a dated release record. |

## Cross-group contamination
The previous config assigned the same NSE all-indices URL to benchmark_index, sector_indices and volatility. This is not independent evidence. Collector v1.1 rejects cross-group URL reuse with CROSS_GROUP_URL_REUSE_REJECTED.

## Collector v1.1 safeguards
- Requires expected_date for market series.
- Requires CSV parsing, non-empty rows, date column and expected date.
- Supports optional index_name_column, expected_index_names and required_columns.
- Rejects cross-group URL reuse.
- Preserves raw bytes, response metadata and SHA-256; performs repeated-download comparison.
- Requires publication_vintage_verified=true before producing a vintage revision ledger.
- Retrieval/schema PASS is not factor coverage PASS; Hard Gate remains BLOCKED.

## Execution and evidence status
Collector v1.1 committed to research branch. No verified Actions run ID or downloadable artifact was exposed by the available GitHub integration during this operation. Therefore no raw-response SHA-256, drift outcome, or vintage revision conclusion is claimed. PIB/MEA raw HTML/PDF capture remains pending. No archived vintage pair verified; no revision ledger created.

## Official references
- https://www.nseindia.com/reports-indices-historical-index-data
- https://www.nseindia.com/reports-indices-historical-vix
- https://www.nseindia.com/all-reports
- https://www.niftyindices.com/reports/historical-data
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552

## Decision
SOURCE_ROUTE_IDENTIFIED_BUT_RAW_ACQUISITION_INCOMPLETE. All four P0 groups remain PARTIAL/UNKNOWN as applicable. No source promotion. Hard Gate BLOCKED.


## Actions run audit (verified 2026-11-02)
Workflow: `.github/workflows/macro_geo_p0_raw_acquisition.yml`

| Run | Commit | Conclusion | Evidence |
|---|---|---|---|
| #1 — 41423497196 | 475303fc54f2d7c398e4f319bfc492e813fb2050 | failure | Initial push-trigger workflow failed. |
| #2 — 41423553534 | e5bd88c50b24bdb5c606f14c56d061a2d2e744fa | failure | Self-contained push trigger revision failed. |
| #3 — 41431166713 | a7d52a70c3d122285d3b83ed2697234143661acd | failure | Strict CSV date/index validation revision failed. |
| #4 — 41431703627 | 5ab0742b906cb2f401729901280c327dd8468ee9 | failure | QA assertion/workflow revision failed. |
| #5 — 41432079313 | cdb112ba3747a71914d108c7bbe7892bd2209dea | failure | HTML rejection assertion fix run failed. |
| #6 — 41432087344 | 66438f2c1b6f7a1883075a797c81475457cbf109 | success | QA-only: 5 tests passed in 0.04s; collect job skipped. |

Run #6 job IDs: QA 125232874120 (success); collect 125232996100 (skipped).
Run #6 artifact inventory: 0 artifacts. Consequently there is no workflow artifact ZIP to download and no raw-file SHA-256 or drift result to independently recompute from this run. The successful result is limited to collector unit tests; it is not a successful acquisition.

## Dated official response records found (not raw-byte archived)
- PIB PRID 2175552: official rendered release page identifies Ministry of Finance, title “Fourth Kautilya Economic Conclave (KEC 2025)...”, Posted On 06 Oct 2025 7:50 PM by PIB Delhi. URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552 . The page was inspected in rendered form; the original HTTP response bytes/headers were not captured to a file, so no SHA-256 is claimed.
- MEA official PDF located: https://www.mea.gov.in/Portal/CountryNews/25076_Press_release_for_Diwali_reception_on_19th_Oct_2025.pdf . Search-indexed PDF identifies Embassy of India, Ashgabat, press release about the 19 Oct 2025 Diwali reception. The PDF bytes were not downloaded into the workflow artifact; no SHA-256 is claimed.
- PIB archive documentation confirms PIB archive records are searchable by year/month, ministry and keyword: https://www.pib.gov.in/Aboutarchive.aspx?lang=1&reg=1 .

## Hash and validation disposition
- Unit validation: PASS, 5/5 tests (Run #6 logs).
- Production raw CSV date/index validation on downloaded market data: NOT RUN; no market raw CSV acquired.
- Independent SHA-256 recomputation: NOT POSSIBLE; no acquisition artifact/raw response file exists in Run #6.
- Download drift/repeat-fetch comparison: NOT RUN.
- PIB/MEA response archival: SOURCE LOCATED, ORIGINAL RESPONSE BYTES NOT ARCHIVED.
- Archived vintage pair: NOT FOUND/NOT VERIFIED. No revision ledger created, by design.

## Updated decision
COLLECTOR_QA_PASS_RAW_ACQUISITION_BLOCKED. Route discovery and tests are useful progress, but no market raw acquisition or official-response byte archive has been completed. All P0 coverage remains partial/unknown; no source promotion; Hard Gate BLOCKED.


## PIB/MEA raw-response archive — verified success
- Workflow: `.github/workflows/pib_mea_official_response_archive.yml`
- Successful run #3 / ID: `41469790857`
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/41469790857
- Commit: `30cf4e25a8ce2ef0a54b8feb7fe83ee9e1ce3a14`
- Job: `archive` — success; both source validation and artifact upload steps completed.
- Artifact: `pib-mea-official-response-archive`, ID `13153344725`, 2,450,096 bytes, expires 2027-01-31.
- Artifact SHA-256 from GitHub: `d340c12e14e0be71679cf62a13087d3c96eeb15793c2641d02c9648ae7a91164`.
- Artifact independently downloaded; ZIP integrity test PASS; locally recomputed ZIP SHA-256 matches GitHub digest exactly.

### Raw response byte verification
| Source | Attempts | HTTP/content validation | Raw bytes | SHA-256 | Repeat |
|---|---:|---|---:|---|---|
| PIB PRID 2175552 HTML | 2 | 200 / HTML / PRID+Kautilya markers PASS | 137,059 each | attempt 1 `512e0bd506b8284aac1c08e14b8c3801b50fe48eabebeef379e036f41de45b11`; attempt 2 `6a2c517c1da061f226e9b48890ac716928b9be4aba74c256ec5c8ced6b49cb32` | Different raw bytes; dynamic response drift observed, not interpreted as historical content revision. |
| MEA Ashgabat Diwali 19 Oct 2025 PDF | 2 | 200 / application/pdf / %PDF signature PASS | 1,182,251 each | `47362d5c6efb4da1a0c7022eb62198109abc56b66092bfe9ca99261d7272f77f` both attempts | Identical bytes. |

MEA download was captured from the Embassy of India, Ashgabat official website PDF route, which serves the same press-release title as the MEA domain PDF. MEA-hosted URL itself returned HTTP 403 from the GitHub runner; the Embassy-hosted official mirror returned HTTP 200 and valid PDF bytes.

### Remaining limits
- PIB/MEA original response bytes now archived with independently recomputed hashes.
- PIB raw HTML differs between repeat requests. This is a response-level drift signal only; no vintage/revision inference.
- Market index/sector/India VIX raw CSV acquisition remains NOT RUN; therefore actual date/index-name validation on market observations remains NOT RUN.
- No archived vintage pair verified. Revision ledger intentionally NOT created.
- Hard Gate remains BLOCKED; no factor promotion.


## Verified original-response archive — workflow run #4
- Run ID: 41469877717; conclusion SUCCESS; archive job 125360328270 SUCCESS.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/41469877717
- Artifact ID: 13155345145; name `pib-mea-official-response-archive`; size 2,450,101 bytes.
- GitHub artifact digest: `sha256:3eeac0c74fc39203a3a39664e46a5b47a20782167f440b5ed21550f46c727cc3`.
- Artifact downloaded independently; ZIP integrity/listing passed. Independently recalculated ZIP SHA-256: `3eeac0c74fc39203a3a39664e46a5b47a20782167f440b5ed21550f46c727cc3` (matches GitHub digest).
- Artifact contains both attempts for PIB and MEA plus manifest.json.

### Original response hashes independently recalculated from downloaded artifact
| Source | Attempt | HTTP | Bytes | SHA-256 | Validation |
|---|---:|---:|---:|---|---|
| PIB PRID 2175552 HTML | 1 | 200 | 137,060 | `74966f7cbca3b65cd24b49e5b2b37af2a87086c4f6ec7fbc291b74bbdb87aeee` | Source content PASS |
| PIB PRID 2175552 HTML | 2 | 200 | 137,060 | `35e226513644c0e96c91f9000700f67776988705b54433168e97554be4abaffb` | Source content PASS |
| MEA Ashgabat Diwali PDF | 1 | 200 | 1,182,251 | `47362d5c6efb4da1a0c7022eb62198109abc56b66092bfe9ca99261d7272f77f` | PDF signature PASS |
| MEA Ashgabat Diwali PDF | 2 | 200 | 1,182,251 | `47362d5c6efb4da1a0c7022eb62198109abc56b66092bfe9ca99261d7272f77f` | PDF signature PASS |

- Every per-file SHA-256 recomputation matched the archived manifest.
- MEA repeated download: byte-identical (no drift observed).
- PIB repeated download: same byte count but different SHA-256; dynamic response drift observed. Both versions are preserved; this is not treated as a publication-vintage pair or revision evidence.
- The initial run #1/#2 had failed because MEA returned HTTP 403 and the upload was skipped. Run #4 is the first verified complete artifact capture.

### Scope boundary
This artifact archives two official response bodies and records request-time response headers; it does not provide October 2025 immutable historical response captures. No revision ledger is justified or created. Market index raw CSVs were not acquired, so market date/index validation, market-file SHA-256 and index-source drift remain NOT RUN. Hard Gate remains BLOCKED.


## NSE/Nifty Indices historical endpoint probe — 2026-11-02
- Workflow run #1: 41472861029, commit 779896c7c042b97ac522a167928c1c364f7d65c2; job failed at the first metadata API response. Artifact 13156405645 (15,738 bytes), ZIP SHA-256 `48fe330fa883a00a94bb61663b1f789d205fdc7164e3b0218dbd09fae31100ad`.
- Workflow run #2: 41473019128, commit 9b5a6e6bc6ba75a5f7728b2215bb9099cabb9fc8; job failed at the first metadata API response after warming the official historical page. Artifact 13155593115 (34,850 bytes), GitHub digest `sha256:dbca4dbafee17f56417968e84199e77a25081bfc3f9fc453b5460b2d70bf26b3`.
- Artifact #2 downloaded and independently hashed: `dbca4dbafee17f56417968e84199e77a25081bfc3f9fc453b5460b2d70bf26b3` (matches GitHub digest); ZIP listing/integrity passed.
- Captured response was HTTP 200 but HTML redirect to `https://www.niftyindices.com/?ReturnUrl=...`, not JSON. The official site's POST metadata endpoint was therefore not accessed; no benchmark/sector/VIX data rows were returned.
- No market CSV raw files exist in this probe artifact. Date/index validation, market raw SHA-256 and drift remain NOT RUN.
- Source route references in external reverse-engineering documentation are leads only, not proof of a functioning official API. No source promotion.

## Current decision
NSE HISTORICAL API ACCESS BLOCKED BY OFFICIAL SITE REDIRECT/AUTH FLOW. Preserve diagnostic artifact and investigate page JavaScript, session/cookie/anti-bot requirements or official NSE alternative. Hard Gate remains BLOCKED; no vintage pair found and no revision ledger created.


## Nifty Indices API probe — verified attempts
Official historical-data page: https://www.niftyindices.com/reports/historical-data . Independent technical reference documents the ASP.NET POST routes and response schemas for historical index OHLC and India VIX; it is implementation guidance, not an official source. The first workflow probe used an invalid endpoint path casing and received HTML instead of JSON. A subsequent probe corrected the path to `/BackPage.aspx/`, added X-Requested-With/AJAX headers, and warmed the official landing page.

- Run #3: 41476680585, failed before API calls because DNS resolution for `iislliveblob.niftyindices.com` failed. Artifact 13156239702 captured only the landing HTML and metadata; artifact digest `adb88378ce4880dd84934a6735f06c4e94e5181190f9e602f05086f8ae823c74`.
- Run #4: 41476792069, created after removing the static-asset DNS dependency. At the latest audit observation it remained queued; no conclusion or artifact is claimed.
- The earlier run #1 (41472861029) failed on non-JSON HTML response from the metadata endpoint; artifact 13156405645 was preserved for diagnostics.

No NIFTY 50, sector-index or India VIX raw historical data response has yet been acquired. Date/index validation and independent raw-data hash/drift checks are therefore NOT RUN. The technical route reference is not promoted as source evidence. No revision ledger created. Hard Gate remains BLOCKED.


## Official NSE historical endpoint probe — verified
- Workflow: `.github/workflows/nse_historical_index_vix_probe.yml`
- Run ID: 41480560725; job ID: 125397423289; conclusion SUCCESS.
- Artifact ID: 13160321349; artifact name `nse-historical-index-vix-probe`; size 2,297 bytes.
- Artifact digest: `sha256:e2f8f838620ed3f248d6d2c27d3183110dcb455920a9e4c18084553db26ec874`.
- Artifact downloaded and ZIP SHA-256 independently recomputed; exact digest match.
- Raw benchmark response SHA-256 independently recomputed: `92697f9cba40a712bcf130a36d92ff65c6cc07b919914c73be8afdff4b4b799a`, 1,917 bytes, HTTP 200.
- Raw India VIX response SHA-256 independently recomputed: `0ff77ae23978f10e3f01617906fcdb3f87a0b9dc123288499f9faa9d1a4f511c`, 1,992 bytes, HTTP 200.
- Benchmark: NIFTY 50, 7 records, 1/3/6/7/8/9/10 Oct 2025; all identities exactly `NIFTY 50`.
- Volatility: INDIA VIX, 7 records, same trading dates; all identities exactly `INDIA VIX`.
- Date and index identity checks PASS. Raw bytes and manifest archived.
- This proves source endpoint connectivity and schema only, not 200-session coverage or factor-group promotion.

### 200-session acquisition attempt
- Workflow `.github/workflows/nse_p0_200_session_coverage.yml` first attempt Run ID 41480717765 failed closed because NSE endpoint returned only 70 NIFTY 50 records for the requested one-year window; artifact ID 13159797039 preserved the partial response.
- Collector changed to bounded 45-day chunks to test whether the endpoint's response cap can be safely handled without dropping records.
- Second attempt Run ID 41480824206 was observed IN_PROGRESS at audit time; no result/artifact is claimed yet.
- Separate sector series requested are NIFTY BANK and NIFTY IT; no sector coverage claim until run completion and raw artifact audit.
