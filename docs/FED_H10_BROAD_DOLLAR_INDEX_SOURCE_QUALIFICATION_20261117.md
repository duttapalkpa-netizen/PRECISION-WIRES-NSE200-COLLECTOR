# Federal Reserve H.10 Nominal Broad Dollar Index — Source Qualification

Audit date: 2026-11-17
Scope: metadata qualification only; research overlay; no production approval.

## Qualified exact source tuple

- Source: Federal Reserve Board H.10 Data Download Program
- Official single-series preview URL: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10
- Exact series ID: H10/H10/JRXWTFB_N.B
- Series description: Nominal Broad Dollar Index
- Indicator key: fed_h10_nominal_broad_dollar_index
- Unit: Index:_1997_Jan_100
- Multiplier: 1
- Quality class: VERIFIED_OFFICIAL (source identity/definition only)
- Official content type expected from preview route: text/html
- Registry entry: config/global_capital_rotation_source_registry.json

## Distinctions that must not be collapsed

1. JRXWTFB_N.B is the Fed Nominal Broad Dollar Index. It is not ICE U.S. Dollar Index (DXY); do not label it DXY.
2. RXI_N.B.IN is a separate H.10 bilateral series, India Rupee per U.S. Dollar. It is not the broad dollar index and is not an RBI reference rate.
3. The user's Library file FRB_H10(1).csv contains three daily index series, including JRXWTFB_N.B, with dates 2026-10-26 through 2026-11-06. Its computed SHA-256 is c47d0f4b10e2cc5f541f91113d9c4d34bd9dfc72845b2313a99e68437ea7dad1 (813 bytes). This is a user-Library comparison fixture, not an independently acquired official raw-payload artifact and must not be used as the manifest raw payload.
4. The user's Library file FRB_H10 (1)(1).csv is a separate H.10 bilateral exchange-rate table including RXI_N.B.IN. Its computed SHA-256 is cafe63d09de50d3e051f0733f5c6ded7382ebf2194447d128b9f5d28fd5012d9 (3,672 bytes). It is also a comparison fixture, not a new official acquisition.

## Official checks observed

- Federal Reserve H.10 release page states daily bilateral exchange rates and U.S. dollar indexes are released on Mondays at 4:15 p.m. for the previous business week (following business day when Monday is a Federal holiday).
- Official H.10 preview for JRXWTFB_N.B reports unit Index:_1997_Jan_100, multiplier 1.
- The official preview surfaced these observations: 2026-11-13 = 122.6503; 2026-11-12 = 122.5433; 2026-11-11 = ND; 2026-11-10 = 122.1143; 2026-11-09 = 121.6623; 2026-11-06 = 121.8803; 2026-11-05 = 121.5061; 2026-11-04 = 121.3983; 2026-11-03 = 121.8084; 2026-11-02 = 121.3702.
- User-Library daily index fixture's 2026-10-26 through 2026-11-06 values match the official Fed DownloadTable rendering for the three daily index series on the overlapping dates. This is a cross-check of displayed values, not proof of raw-byte identity.
- The official H.10 bilateral rate preview identifies RXI_N.B.IN as India Rupee, with units expressed as INR per USD. H.10 historical notes describe the bilateral rates as noon buying rates in New York, based on a sample of market participants; do not substitute for RBI reference rate or DBIE interbank close.

## Acceptance boundary

- Source identity, series ID, description, unit, multiplier, official URL: VERIFIED.
- Registry tuple admission: ADDED as one exact metadata-qualified source tuple.
- Official raw HTML payload acquisition, retrieval timestamp, HTTP headers/status, byte length, SHA-256 and immutable evidence manifest: NOT_ACQUIRED.
- Trusted observation admission using the manifest gate: BLOCKED until official raw payload bytes are acquired and manifest is created.
- 20-trading-day derived change: NOT_DONE. The 10-date user fixture is insufficient for a full 20-session calculation; the official preview includes an ND on 2026-11-11. Never forward-fill ND or infer missing observations.
- Overlay classifier integration: NOT_DONE. Do not map this raw index directly to dxy_change_pct_20d. A separate tested derivation and explicitly named derived indicator are required.
- Production use: NOT_AUTHORIZED.

## Official references

- H.10 daily release and schedule: https://www.federalreserve.gov/releases/H10/
- H.10 broad-dollar series preview: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10
- H.10 Indian rupee bilateral series: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FRXI_N.B.IN&rel=H10
- H.10 DDP source package chooser: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10

## Next permitted step

Acquire the official H.10 preview payload directly from the exact URL above through an allowed HTTP client, capture final URL, UTC retrieval time, HTTP status, content type, byte length and SHA-256, store bytes under the manifest-controlled raw payload path, and create an append-only evidence manifest. If raw bytes cannot be obtained, stop and keep trusted observations BLOCKED. Do not use a search snippet, browser-rendered text, or user-library CSV as a substitute for the official raw payload.


## CI validation after registry admission
- Registry commit 380918fc008ad96bccabbbab06b18b4ae6683df5 triggered workflow run #221 / ID 44030991201; conclusion SUCCESS. The tests job and Python unittest step both succeeded.
- Source Register commit d970737f9bb2cdc682ad5c8bd256c2b7fdf84d24 triggered workflow run #222 / ID 44031034467; conclusion SUCCESS. The tests job and Python unittest step both succeeded.
- These CI passes validate the current overlay test suite with the one-entry registry. They do not establish official raw-payload acquisition, manifest creation, any admitted observation, 20-session derivation, or production authorization.


- Follow-up documentation commit c1c252ad635bff9429c13f4e0d14ccb7918dde20 was also exercised by workflow run #223 / ID 44031095909; final run status COMPLETED / SUCCESS, test job and unittest step passed. This verifies the documentation-updated branch head used for that run; it still does not satisfy raw payload acquisition or observation manifest admission.


## Official transport capture addendum — 2026-11-17

### Acquisition method
- Collector: `tools/capture_fed_h10_official.py`
- Workflow: `.github/workflows/fed_h10_official_evidence_capture.yml`
- Workflow run #2: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44031614252
- Run ID: 44031614252; head `1fe925b6c8a52a33745a4e445461fdbe9aa12afd`
- Artifact ID: 14305441931; name `fed-h10-official-evidence-44031614252`
- Artifact SHA-256: `05928613d892fafd3ac904c3ae325794535fcc643613f39c8d3dd968d79620f2`
- Artifact retention: 90 days; not permanent archival.

### Captured official HTTP response
- Request/final URL: https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10
- Request started UTC: 2026-11-17T06:29:47.973930+00:00
- Retrieved UTC: 2026-11-17T06:29:48.056078+00:00
- HTTP status: 200
- Content-Type: application/x-zip-compressed
- Raw response length: 2,088,268 bytes
- Raw response SHA-256: `c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77`
- ZIP integrity: PASS.
- Hash independently recomputed after downloading the Actions artifact; matched manifest and checksum sidecar exactly.
- Response headers captured in the artifact include Date, Content-Type, Content-Disposition, Last-Modified and transport metadata.

### ZIP/XML verification
- `H10_data.xml`: 27,426,691 bytes; `H10_H10.xsd`: 34,088; `H10_struct.xml`: 131,344; `frb_common.xsd`: 139,952.
- XML well-formedness: PASS.
- XML Header Prepared: `2026-11-16T16:47:01`; this is source package preparation time, not HTTP retrieval time. Timezone is unspecified; do not convert it to UTC.
- `JRXWTFB_N.B` Broad Dollar Index: unit `Index:_1997_Jan_100`, multiplier 1, 5,445 observations, 2006-01-02 through 2026-11-13; latest 2026-11-13 = 122.6503, status A.
- `JRXWTFN_N.B` Advanced Foreign Economies Index: 5,445 observations; latest 2026-11-13 = 116.2360.
- `JRXWTFO_N.B` Emerging Market Economies Index: 5,445 observations; latest 2026-11-13 = 130.8877.
- `RXI_N.B.IN` bilateral INR series: unit Currency; 14,054 observations; latest 2026-11-13 = 94.2400. It is not the broad index or an RBI reference rate.
- This package extends beyond the earlier Library ZIP vintage; retain both vintages separately.

### Correction / controls
- Initial capture run #1 sidecars contained literal escaped newline suffixes; run #1 is superseded and not canonical.
- Collector was corrected. Run #2's JSON and checksum sidecars parse correctly; only run #2 / artifact 14305441931 is canonical for this capture.
- Registry now allows only the exact observed `application/x-zip-compressed` content type and exact H.10 package URL as an allowed final URL for this exact series tuple.

### Acceptance status
- Official HTTP transport evidence: PASS.
- Raw package bytes + independent SHA-256: PASS.
- ZIP integrity + XML well-formedness: PASS.
- Selected series identity/unit/observation extraction: PASS.
- XSD validation: NOT_DONE (SDMX dependency chain incomplete).
- Per-observation manifest bound to parser CSV: NOT_DONE.
- Durable GitHub archive beyond 90-day artifact retention: NOT_DONE.
- 20-session derived index change: NOT_DONE.
- Classifier integration: NOT_DONE.
- Production authorization: NOT_AUTHORIZED.

Next bounded step: create observation CSV + exact per-observation evidence manifest bound to this raw ZIP, execute parser validation at a point-in-time cutoff, and preserve the raw ZIP in durable GitHub evidence storage. Do not rename this series ICE DXY or map it directly to `dxy_change_pct_20d`.
