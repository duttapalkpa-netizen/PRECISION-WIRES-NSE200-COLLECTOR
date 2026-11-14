# IMF BOP Metadata-First Acquisition — Evidence Result
Date: 2026-11-14 (Asia/Kolkata)
Scope: research-only metadata acquisition and extraction-contract validation; no observation payload acquired; no EM aggregate calculated.

## 1. Exact IMF Data Portal dataset identity
The official IMF BOP dataset page was retrieved over HTTPS (HTTP 200, text/html, 286,487 bytes). The page's embedded dataset metadata identifies:
- Title: Balance of Payments (BOP)
- Dataset URN: IMF.STA:BOP(21.0.0)
- Agency ID: IMF.STA:BOP
- Dataset version: 21.0.0
- Publication/last-updated timestamp displayed in embedded catalogue metadata: 2026-11-03T15:12:50Z
- Dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Raw page SHA-256: 55c6a08f032f70d368a2c51670782013b57f9da552424904529a594a27e11987

This IMF Data Portal dataset URN/version is not silently equated with an IMF SDMX Central Dataflow ID/version.

## 2. IMF SDMX Central Dataflow catalogue discovery
Official IMF SDMX Central Dataflow structure response:
- Request: https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF/all/latest/?format=sdmx-2.1&references=children&detail=full
- HTTP 200; XML parsed; 448,310 bytes.
- Raw SHA-256: 6848863bd8a8f2e4b3120d03a3b1ae6a7530695329819d4bcff22cd0df26dd7d
- 101 IMF dataflow objects returned.
- BOP-related registry entries found:
  - BOP6 1.1 -> ECOFIN_DSD 1.0
  - BOP_BPM6 1.0 -> ECOFIN_DSD 1.0
  - BOP_GBPM6 2.0 -> BOP DSD 2.0
  - BPM6_BOP_Q 1.5 -> BOP DSD 1.5
  - BOP5_COLLECTION 1.0 -> ECOFIN_DSD 1.0
- These are registry dataflows with their own DSD references. No evidence in this audit proves that any of these registry dataflows is the API dataflow behind the separate IMF Data Portal dataset URN IMF.STA:BOP(21.0.0). Therefore the portal API dataflow-to-registry-dataflow crosswalk remains UNKNOWN; do not use a candidate as the production observation route.

## 3. Pinned BOP DSD V2.6.0 — raw retrieval and parse
Official IMF SDMX Central DSD request:
https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true

- HTTP 200; Content-Type application/xml;charset=UTF-8.
- Raw bytes: 1,041,211.
- Raw SHA-256: 42948c26081a214a5816cf9748a2ac7a19c9fb8d2b88bc3c3eacc02863910fdc
- DSD identity: IMF:BOP, version 2.6.0.
- Exact direct component counts, parsed from the pinned DataStructure's own DataStructureComponents (not recursive descendant counts):
  - 18 dimensions (17 coded dimensions + TIME_PERIOD)
  - 15 attributes
  - 1 primary measure: OBS_VALUE
- The 18 dimension order:
  1 FREQ
  2 ADJUSTMENT
  3 REF_AREA
  4 COUNTERPART_AREA
  5 REF_SECTOR
  6 COUNTERPART_SECTOR
  7 FLOW_STOCK_ENTRY
  8 ACCOUNTING_ENTRY
  9 INT_ACC_ITEM
  10 FUNCTIONAL_CAT
  11 INSTR_ASSET
  12 MATURITY
  13 UNIT_MEASURE
  14 CURRENCY_DENOM
  15 VALUATION
  16 COMP_METHOD
  17 TYPE_ENTITY
  18 TIME_PERIOD
- 15 attributes: TIME_FORMAT, OBS_STATUS, CONF_STATUS, PRE_BREAK_VALUE, COMMENT_OBS, COMMENT_TS, TITLE, UNIT_MULT, DECIMALS, TIME_PER_COLLECT, REF_PERIOD_DETAIL, COMPILING_ORG, DATA_COMP, DISS_ORG, TITLE_COMPL.
- Primary measure: OBS_VALUE (Double).

## 4. Referenced codelist acquisition and verified critical codes
- 22 unique codelist references in the DSD were retrieved from official SDMX Central.
- All 22 responses: HTTP 200 and XML parse PASS.
- Raw XMLs and inventory archived in the run artifact below.
- Critical code checks:
  - FREQ: SDMX:CL_FREQ 2.0 -> A Annual; Q Quarterly.
  - REF_AREA: IMF:CL_AREA 2.0.0 -> IN India.
  - FLOW_STOCK_ENTRY: IMF:CL_FSENTRY 1.1 -> T Transactions; K Changes in positions other than transactions.
  - ACCOUNTING_ENTRY: IMF:CL_ACCOUNT_ENTRY 1.5.0 -> A Assets (Net Acquisition of); L Liabilities (Net Incurrence of).
  - INT_ACC_ITEM: IMF:CL_ACCOUNTS_ITEM 1.8.0 -> FA Financial account.
  - FUNCTIONAL_CAT: IMF:CL_FUNCTIONAL_CAT 1.10.1 -> P Portfolio Investment.
  - INSTR_ASSET: ESTAT:CL_INSTR_ASSET 1.15.0 -> F3 Debt securities; F5 Equity and investment fund shares/units; F51 Equity; F52 Investment fund shares/units.
  - UNIT_MEASURE and CURRENCY_DENOM both reference IMF:CL_UNIT 1.19.0; preserve as separate dimensions.
  - OBS_STATUS references ESTAT:CL_OBS_STATUS 2.3; CONF_STATUS references SDMX:CL_CONF_STATUS 1.3.
- Do not treat code-name matches as sufficient to construct a full series key. The remaining dimensions and dataset-specific constraints must be checked against the IMF Data Portal's actual observation API contract.

## 5. Methodological correction / prior audit defect
The first metadata run counted all descendant XML elements named Dimension/Attribute/PrimaryMeasure, including nested referenced structures and attribute relationships. Those recursive counts (182, 15, 5) were not valid direct DSD component counts. They are explicitly superseded for component interpretation by the second workflow's parser, which selects the single pinned DataStructure and reads only its direct DimensionList, AttributeList and MeasureList. The corrected parser asserts exactly 18/15/1. Preserve the first run artifact as historical evidence; do not rewrite or delete it.

## 6. Observation access boundary
- IMF official API page states SDMX 2.1 and SDMX 3.0 APIs are available and the Swagger explorer requires a beta-portal account sign-in.
- No authenticated account/session was used.
- No BOP observation request was made, no observation rows were acquired, and no observation endpoint/key has been promoted to verified.
- Dataset page contains client-side VIEW DATA and DOWNLOAD controls; the captured HTML does not expose a direct downloadable file URL.
- Observation acquisition status: BLOCKED pending a documented public download/API route or an explicitly authorized beta-portal session. No sign-in bypass, scraping of restricted endpoints, or access-control circumvention.

## 7. EM aggregation gate
Candidate classification authority for a research EMDE panel: IMF World Economic Outlook, April 2026 Database Appendix. It defines Emerging and Developing Economies as a 154-economy group, while explicitly noting that the classification is analytical and not based on strict criteria. This is EMDE, not a claim to represent every investible-market definition of “EM”.
- Official source: https://data.imf.org/-/media/iData/External%20Storage/Documents/4AA1F4D0624C46E98F95988F1F83E770/en/April%202026%20WEO%20Database%20Appendix
- The appendix's external-sector composite convention converts BOP data to USD using average market exchange rates; it should not be copied without checking the exact portfolio-flow measure and period-specific data conventions.
- A versioned economy-name-to-IMF-CL_AREA-code crosswalk has not yet been generated and reconciled.
- No portfolio observations, reporter coverage denominator, weights, USD conversion, or EM aggregate were produced.
- EM aggregation remains BLOCKED. No partial convenience sample or currency summation.

## 8. GitHub Actions evidence
### Run 43590032021 — IMF BOP metadata-first access audit
- Result: SUCCESS.
- Commit: 47c2037de3fe4ff06094803a24e96a5aa5ff24fe
- Artifact ID: 14112042284
- Artifact ZIP SHA-256: 95aa8c3a730704cd1778ae12b7e5321b6e1c373b0d4eea81b0acfd6448fe1822
- Includes official DSD raw response, dataflow catalogue response, IMF dataset page capture and metadata summary.
- Important: recursive XML element counts from this run are not the accepted direct DSD component counts; see Section 5.

### Run 43590132930 — IMF BOP DSD component and codelist audit
- Result: SUCCESS.
- Commit: 8df4589a1171bc74914b577313bd9c65ebc69f02
- Artifact ID: 14111193621
- Artifact ZIP SHA-256: 60c5485f6dd9538255a1ca364e719a2bc843b68be12d13a7521c5febae84d840
- Artifact contains 24 files: pinned DSD XML, 22 referenced codelist XMLs, and dsd_component_inventory.json.
- Corrected component assertions: 18 dimensions / 15 attributes / 1 measure PASS; 22/22 codelists HTTP 200 + XML parse PASS.

## 9. Gate matrix and next steps
| Gate | Status |
|---|---|
| IMF BOP dataset identity/version from official portal page | PASS |
| IMF SDMX Central DSD 2.6.0 raw retrieval + SHA-256 | PASS |
| Direct DSD component inventory 18/15/1 | PASS |
| All 22 referenced codelists retrieved and parsed | PASS |
| Critical portfolio-transaction code meanings | PASS (metadata-level) |
| Exact Portal dataset-to-SDMX registry dataflow crosswalk | UNKNOWN |
| Official observation API/download route + access authorization | BLOCKED |
| Actual India observations and row-level provenance | NOT DONE |
| Versioned WEO April 2026 EMDE membership mapped to IMF area codes | NOT DONE |
| EM panel coverage, FX/unit harmonization and aggregation | BLOCKED |
| Overall IMF BOP-to-EM aggregate acceptance | BLOCKED |

Next highest-value work:
1. Resolve the IMF Data Portal dataset's own API dataflow/endpoint and access model without bypassing beta sign-in.
2. Build a versioned WEO April 2026 EMDE membership file and exact crosswalk to IMF CL_AREA 2.0.0, preserving unmapped names as UNKNOWN.
3. Only after an authorized public observation route is verified, request a narrow India-only quarterly/annual portfolio-investment sample using metadata-confirmed dimensions; archive raw bytes, response headers, key, period, and SHA-256.
4. Validate observation flags, unit/multiplier, revisions, and assets/liabilities separately.
5. Do not calculate EM aggregation until all country, period, instrument, unit, FX, coverage, and vintage gates pass.

## 10. Invariants
Research-only; ₹0 spend; official free sources; no paid APIs, no synthetic values/timestamps, no external contact, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 remain unchanged. UNKNOWN is neither PASS nor FAIL.
