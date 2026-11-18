# IMF BOP DSD V2.6.0 Endpoint Verification — Chapter 34 Part-1 (2026-11-18)

## Objective
Resolve the IMF BOP DSD metadata retrieval blocker using only the two previously documented official IMF SDMX Central routes. This is metadata qualification only; no BOP observations or aggregates are produced.

## Runtime evidence
- First execution Run `44249890707`: SUCCESS; exposed a parser bug in the initial probe (the DSD identifier was searched only in the first 200 KB of XML).
- Parser correction commit `930638c30c937d73e2c7d84bcf939d34acb652f5`: identify the exact XML `DataStructure` node by agencyID=IMF, id=BOP, version=2.6.0.
- Descriptor-scope correction commit `017265feb5fd99c54ce752033d10a3fceb3e209c`: count only direct members of DimensionList and AttributeList, avoiding false counts from nested codelists.
- Decision-state correction commit `42606d3687fe8dc0b6d2b64a740795cde4c883f9`: derive METADATA_ROUTE_VERIFIED from the parsed DSD evidence rather than a hard-coded UNKNOWN string.
- Final bounded validation Run `44250316163`: SUCCESS; probe step and artifact upload completed. Run head SHA `42606d3687fe8dc0b6d2b64a740795cde4c883f9`.
- Job/check ID `134619103234`; final artifact ID `14403372899`; artifact size 191,791 bytes; ZIP SHA-256 `1321f32274b48eca7a66dc1220c656be1a54faf2270fa76edc020f60cdf95def`; retained by GitHub until 2027-02-16.
- Workflow time limit: 5 minutes. Run completed successfully within the limit.

## Verified official endpoint evidence
Both exact candidate paths returned HTTP 200, Content-Type `application/xml;charset=UTF-8`, valid SDMX 2.1 Structure XML, and the exact IMF:BOP DSD identity at version 2.6.0.

| Route | Retrieval UTC | Bytes | SHA-256 | DSD identity |
|---|---|---:|---|---|
| Current `/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/` | 2026-11-18T06:18:14.598091Z | 895,438 | `f4df050115748bc0d20f07c47b33bd9bd7157cf6132e9c36a70a6f868bedd075` | PASS |
| Legacy `/ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/` | 2026-11-18T06:18:25.216081Z | 895,438 | `145fb6eeceb259564384b7e927ddae39d991a144713c5b57af82d7d66b4973cb` | PASS |

The parser confirms DSD version 2.6.0, **18 dimensions (including TIME_PERIOD)** and **15 attributes**. Current and legacy responses have separate response hashes because their response headers/prepared IDs differ; both identify the same requested DSD. The dimension and attribute IDs and positions/assignment statuses are recorded in the run's `probe_summary.json` and raw XML artifact.

## Important scope limits
- **Metadata endpoint qualification: PASS.** The current documented route is now the preferred verified route; legacy route also returned the same DSD identity.
- **Full codelist semantic audit: NOT_DONE.** The downloaded XML includes referenced structures, but a complete codelist inventory, code-value validation, unit/sign/frequency semantics and crosswalk to extraction fields still require a separate audit.
- **BOP observations: NOT_DOWNLOADED.** No observation endpoint or country-period series was queried.
- **Emerging-market aggregation: NOT_DONE.** No EM membership, aggregate, or portfolio-flow total was created.
- BOP remains annual/quarterly context and must not be treated as a daily market trigger.
- Original historical BOP observation coverage and any EM panel remain UNKNOWN until independently retrieved and validated.

## Invariants
₹0 spend; official/free sources only; no synthetic values, guessed dimensions, inferred signs/units, or fabricated timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and production workflows unchanged. No production integration authorized.


## Chapter 34 — Part-2: IMF BOP DSD Semantic & Codelist Audit (2026-11-18)

### Evidence inspected
- Reused the exact raw XML from final verified artifact `14403372899`; no endpoint probe repeated.
- Current-route raw XML: 895,438 bytes; SHA-256 `f4df050115748bc0d20f07c47b33bd9bd7157cf6132e9c36a70a6f868bedd075`; HTTP 200; SDMX-ML 2.1; DSD IMF:BOP(2.6.0).
- Parsed the actual DimensionList, AttributeList and MeasureList and followed every embedded codelist reference. Confirmed 18 dimensions, 15 attributes, one measure, 22 embedded codelists and 4,097 embedded codes.
- Machine-readable inventory committed at `data/global_capital_rotation/IMF_BOP_DSD_2_6_0_SEMANTIC_INVENTORY_V1.json`; commit `52658916787c1f31ea6d5a58f6541261a5a18e83`.

### Key extraction semantics established from the embedded codelists
- `INT_ACC_ITEM=FA`: Financial account (IMF:CL_ACCOUNTS_ITEM 1.8.0).
- `FUNCTIONAL_CAT=P`: Portfolio Investment (IMF:CL_FUNCTIONAL_CAT 1.10.1).
- `FLOW_STOCK_ENTRY=T`: Transactions (IMF:CL_FSENTRY 1.1), distinct from positions/stocks and other changes.
- `ACCOUNTING_ENTRY=A`: Assets (Net Acquisition of); `L`: Liabilities (Net Incurrence of) (IMF:CL_ACCOUNT_ENTRY 1.5.0). Keep separate; do not collapse or sign-flip.
- `INSTR_ASSET=F3`: Debt securities; `F5`: Equity and investment fund shares/units (ESTAT:CL_INSTR_ASSET 1.15.0 referenced by this DSD). Preserve agency and version; do not assume all referenced codelists are IMF-maintained.
- `UNIT_MEASURE` and `CURRENCY_DENOM` both reference IMF:CL_UNIT 1.19.0; unit and currency-denomination dimensions remain distinct. `UNIT_MULT` and `DECIMALS` are mandatory attributes in the DSD and must be retained.
- `OBS_STATUS` and `CONF_STATUS` are mandatory attributes; missing/suppressed observations must not be coerced to zero.

### Acceptance matrix
| Gate | Status |
|---|---|
| Exact DSD identity and raw hash | PASS |
| Dimension-to-codelist reference inventory | PASS |
| Embedded codelist inventory (22 / 4,097 codes) | PASS |
| Critical FA / P / T / A / L / F3 / F5 code labels | PASS |
| Unit, multiplier, decimals and observation-status fields identified | PASS |
| Exact IMF dissemination dataflow linkage and permitted series key | UNKNOWN / BLOCKED |
| IMF BOP observation payload and country-period rows | NOT_DONE |
| Versioned EM membership and aggregate | NOT_DONE |

### Important limitation
This is a metadata-semantic mapping, not proof that an IMF-owned public dissemination dataflow exposes these exact dimensions/codes or that a particular series is available. The earlier extraction specification explicitly reports the IMF BOP6 registration as a 2023 sample compact URL and no verified current public observation endpoint. Do not query the sample registration as if it were a complete panel, do not substitute ESTAT dataflows, and do not infer a valid data key from the DSD alone.

### Decision and next action
Part-2 metadata semantic audit: PASS for the captured DSD and embedded codelists. Observation access remains UNKNOWN/BLOCKED; no country rows or EM aggregates created. Next bounded task: qualify the official IMF BOP dataflow-to-DSD linkage and its permitted query dimensions from an official, directly accessible catalogue/constraint response. Stop if authentication is required; no bypass or guessed key. All production invariants remain unchanged.


## Chapter 34 — Part-3: Official IMF BOP6 Dataflow / Constraint Catalogue Cross-check (2026-11-18)

### Scope and method
- Reused the already archived IMF:BOP DSD 2.6.0 XML and Part-2 semantic inventory; no repeated DSD download, no observation request, and no guessed series key.
- Checked the live official IMF SDMX Central Dataflows overview, Reporting Constraints catalogue, and Registrations catalogue, plus the official IMF Data API page.

### Directly evidenced catalogue facts
- The official Reporting Constraints catalogue lists `IMF:BOP6_CONSTRAINT` as a Cube Region Constraint targeting `BOP6[1.0]`; it separately lists `IMF:BOP_BP6_CONSTRAINT` targeting `BOP_BPM6[1.0]`. The BPM5 legacy flow is separately listed as `BOP5_COLLECTION[1.0]` and remains excluded.
- The current Dataflows overview (216 entries in the rendered catalogue) shows ESTAT-owned `BPM6_BOP_M(2.6.0)` and `BPM6_BOP_Q(2.6.0)`; it does not show an IMF-owned BOP6 dataflow in the visible listing. These ESTAT flows are not substituted for IMF BOP6.
- The Registrations catalogue lists multiple provider registrations for `IMF:BOP6(1.0)`, including Brazil (`IMF:BR1`), Chile (`IMF:CL2`), Romania, Sweden and the IMF's own sample compact registration. These are provider-specific SDDS registrations, not proof of a unified IMF country panel. The IMF-owned registration still points to a 2023 sample compact URL; Brazil's current provider URL is a national-provider file and cannot be treated as IMF-wide dissemination.
- The official IMF Data API page confirms SDMX 2.1/3.0 availability but states that the Swagger explorer requires beta-portal sign-in.

### Exact unresolved test
- Direct official Structure Web Service requests for `dataflow/IMF/BOP6/1.0` and `constraint/IMF/BOP6_CONSTRAINT/1.0` were attempted through the available retrieval route; both returned inaccessible/internal-error responses without an XML body, HTTP status, or checksum. This is `PROBE_BLOCKED`, not proof that the structures do not exist.
- Therefore the exact BOP6-to-DSD reference, BOP6 dimension order, constraint-cube permitted values, and a valid query key are still not established from a directly captured structure response. The DSD 2.6.0 dimension/codelist inventory alone cannot fill this gap.

### Acceptance matrix
| Gate | Status |
|---|---|
| Official catalogue confirms BOP6_CONSTRAINT targets BOP6[1.0] | PASS |
| Official catalogue distinguishes BOP_BPM6 and legacy BPM5 | PASS |
| Provider-specific BOP6 registrations identified | PASS |
| Exact IMF:BOP6 dataflow-to-DSD reference | UNKNOWN / PROBE_BLOCKED |
| BOP6 dimension order and permitted constraint values | UNKNOWN / PROBE_BLOCKED |
| Anonymous current IMF BOP observation endpoint and valid key | UNKNOWN / BLOCKED (Swagger sign-in required) |
| Observation payload / India rows / country panel | NOT_DONE |
| Versioned EM membership / aggregate | NOT_DONE |

### Decision
Part-3 closes the public catalogue cross-check, but **does not close the IMF BOP extraction gate**. Do not treat provider registrations as a consolidated panel, do not substitute ESTAT dataflows, do not query the 2023 sample as current data, and do not infer the BOP6 DSD/key from the BOP DSD 2.6.0 alone. Next legitimate action requires an IMF-authenticated Swagger/API specification or a current official IMF-distributed BOP6 dataflow structure response. If unavailable, keep this source UNKNOWN/BLOCKED. No observations or aggregates were created; no production integration or production logic changes.

Sources checked (official):
- https://sdmxcentral.imf.org/data/overview.html
- https://sdmxcentral.imf.org/data/constraints.html
- https://sdmxcentral.imf.org/data/registrations.html
- https://data.imf.org/en/Resource-Pages/IMF-API


## Chapter 34 — Part-4: IMF Official API Access Boundary & Historical BOP_BPM6 Submission Contract Audit (2026-11-18)

### New official documentation evidence
- Re-opened the IMF Data API page. It confirms SDMX 2.1 and 3.0 APIs, but explicitly directs users to the Swagger page using a beta-portal account sign-in. This confirms an access boundary; it does not prove that all API data require authentication.
- Re-opened the official IMF SDMX Central Web Services (API) Guide, last updated May 2025. It documents the public structure-service entry point `https://sdmxcentral.imf.org/sdmx/v2/` and says structures include Dataflows, Codelists, Concepts and Data Structures. The guide distinguishes public structure queries from private/credentialed registration actions; do not conflate registration authentication with read-only structure-query authentication.
- The same official guide contains a historical SDMX submission example explicitly naming `IMF:BOP_BPM6(1.0)` as Dataflow and `IMF:ECOFIN_DSD(1.0)` as DataStructure, with `DATA_DOMAIN=BOP6`, `REF_AREA`, `COUNTERPART_AREA`, `FREQ`, `UNIT_MULT`, `TIME_FORMAT`, `OBS_STATUS`, and `INDICATOR`. Its examples show annual and quarterly submissions and illustrative indicator codes. This is evidence of an IMF BOP6 reporting/submission contract in the guide, not proof of a current public dissemination dataset or observation API.
- The guide's May-2025 generic structure-query documentation plus its older illustrative BOP_BPM6 example must not be silently equated with the separate IMF:BOP DSD 2.6.0 already audited in Part-1/2, or with the IMF:BOP6(1.0) provider registrations and BOP6_CONSTRAINT catalogue entry from Part-3. These are distinct identifiers/structure roles until a direct current structure response proves their relationships.

### Bounded direct check
- Attempted the documented public Structure Web Service query for `IMF:BOP_BPM6(1.0)` requesting its DSD reference, and for `IMF:ECOFIN_DSD(1.0)` requesting referenced children. The retrieval route returned inaccessible/internal-error responses without XML body, HTTP status or checksum. Record `PROBE_BLOCKED`; do not infer that the structures do not exist.
- IMF Swagger access remains beta-portal sign-in gated. No credentials were supplied or used; no authentication bypass attempted.

### Acceptance matrix
| Gate | Status |
|---|---|
| Official IMF API protocol (SDMX 2.1/3.0) confirmed | PASS |
| Swagger beta-portal sign-in requirement documented | PASS |
| Official May-2025 SDMX Central structure-service contract reviewed | PASS |
| Historical IMF:BOP_BPM6(1.0) / IMF:ECOFIN_DSD(1.0) submission example identified | PASS (historical documentation only) |
| Current live BOP_BPM6 → DSD structure response captured | UNKNOWN / PROBE_BLOCKED |
| Relationship among BOP_BPM6, BOP6, BOP DSD 2.6.0 and BOP6_CONSTRAINT established | UNKNOWN |
| Current public IMF BOP observation endpoint / valid query key | UNKNOWN / BLOCKED |
| Observation rows, India panel, EM aggregate | NOT_DONE |

### Decision and next action
Part-4 successfully qualifies an additional official historical submission-contract route and clarifies the API access boundary, but does **not** qualify current observation access. The exact historical example must not be used as a current dataflow/key. Next useful step, if the user has legitimate beta-portal access, is to export the current BOP dataset's Swagger/OpenAPI metadata or a current Data Portal API query definition (no password/token should be pasted into chat). Without that user-authorized metadata, retain UNKNOWN/BLOCKED and do not build a guessed query. No observations or aggregates created; no production integration or production logic changes.

Official references:
- https://data.imf.org/en/Resource-Pages/IMF-API
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (May 2025; especially lines 77-99, 116-120, and historical BOP_BPM6 example around printed page 9)
- https://sdmxcentral.imf.org/data/overview.html
- https://sdmxcentral.imf.org/data/constraints.html


## Chapter 34 — Part-5: Current IMF BOP6 Provider Registration Discovery & Safe Access Qualification (2026-11-18)

### New discovery from official IMF SDMX Central registration catalogue
- The indexed official Registrations catalogue exposes a newer national-provider registration: `IMF:BOP6(1.0)`, provider `IMF:BR1` (Brazil), registered URL `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`, last updated `2026-10-26T11:47:29Z`.
- This is a material improvement over the IMF-owned 2023 sample registration: it provides a current-ish, official, country-provider SDMX BOP6 registration candidate. It is still Brazil's provider file, not an IMF-hosted consolidated global panel and not an India observation source.
- The same catalogue also lists Chile `IMF:BOP6(1.0)` provider `IMF:CL2` updated 2026-10-07, and other country-specific `IMF:BOP_BPM6` registrations. Do not merge different dataflow IDs/versions or assume identical DSDs without structure-level verification.

### Access test and result
- Attempted to open the exact Brazil registered XML URL from the official catalogue. The available web retrieval layer rejected the response because its content type is `text/xml` (unsupported content type); it returned no XML body, HTTP status, byte count or checksum.
- Result: `REGISTERED_URL_DISCOVERED`; payload capture = `BLOCKED_BY_RETRIEVAL_CONTENT_TYPE`; no claim of URL failure, no parsed DSD, no observation extraction, and no SHA-256 fabricated.
- The official Registrations page describes SDMX Central as providing web services for querying structures and data, and identifies the SDMX Central Web Services Guide. Registration-page actions that create/modify registrations require re-authentication; no such action was attempted.

### Acceptance matrix
| Gate | Status |
|---|---|
| Official catalogue exposes current Brazil IMF:BOP6(1.0) provider registration | PASS (discovery) |
| Registered URL and last-updated timestamp captured | PASS (catalogue metadata) |
| Brazil XML payload fetched and parsed | UNKNOWN / BLOCKED (text/xml unsupported by retrieval layer) |
| BOP6(1.0) DSD identity / version / dimension order verified from payload | NOT_DONE |
| Brazil BOP6 observation values / latest period validated | NOT_DONE |
| India BOP6 source or consolidated IMF panel verified | UNKNOWN / NOT_DONE |
| EM membership and aggregate | NOT_DONE |

### Decision and next action
This is a valid new official-provider discovery and a bounded access test, not an extraction pass. Preserve the Brazil registration as a **schema/transport candidate only**. The next safe task is to use a raw HTTP client in an authorized execution environment that can accept `text/xml`, archive response headers and exact bytes, validate SDMX-ML, and calculate SHA-256; then compare its declared dataflow/DSD to the Part-2 IMF BOP DSD inventory. Until that is done, do not parse or query guessed keys. Even if Brazil payload validates, it cannot be used as India's data or as a full EM panel. No observation rows or aggregates created; no production integration or production logic changes.

Official catalogue source: https://sdmxcentral.imf.org/data/registrations.html
Registered provider URL (Brazil): https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
