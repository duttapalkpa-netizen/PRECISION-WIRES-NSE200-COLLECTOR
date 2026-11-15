# IMF October 2025 BPM6 reporting document — retrieval and evidence-status audit

Audit date: 2026-11-15
Target document: "Economies Reporting on BPM6 Basis October 2025"
IMF publication date: 14 May 2026
Dataset association: Balance of Payments (BOP), International Investment Position (IIP)
Security classification: Public or Unrestricted
Content type: Manual
Format: PDF

## 1. What is verified

The official IMF Documents catalogue and the official IMF BOP dataset page both list the target document with the exact title, publication date, dataset association, public/unrestricted classification and PDF format.

Official catalogue:
`https://data.imf.org/en/Documents`

Official BOP dataset page:
`https://data.imf.org/Datasets/BOP`

Search-result metadata exposes the catalogue item identifier `1792656603400855000`.

## 2. What is not verified

The PDF binary and its complete country table were not retrievable through the available public page extraction in this audit. The catalogue landing page exposed the document metadata but not a direct PDF link or the document body. Therefore:
- no country row was read from the October 2025 table;
- no absence/presence conclusion is made for CAF, ERI, GNQ, SOM, TCD or TKM in this edition;
- no BPM6 BOP start date is assigned to any of the six;
- the April 2025 table result remains historical evidence only and is not silently carried forward.

This is an evidence-access limitation, not a failed country eligibility test.

## 3. Exact SDMX artefact limitation

The public IMF SDMX Central Structure Web Service page confirms the registry REST entry point:
`https://sdmxcentral.imf.org/sdmx/v2/`
and that the service can query Dataflows, Data Structures, Provision Agreements and related structural artefacts.

The public Reporting Constraints page lists `IMF:BOP6_CONSTRAINT` attached to `BOP6[1.0]` and `IMF:BOP_BP6_CONSTRAINT` attached to `BOP_BPM6[1.0]`. It does not establish that either applies to `IMF.STA:BOP(21.0.0)` / `IMF.STA:DSD_BOP(24.0.0)`.

A guessed REST path for the IMF.STA BOP dataflow returned inaccessible through the page retrieval interface; it is not treated as proof that the artefact is absent. No Provision Agreement or Data Provider identity was identified and no provider-level constraint was resolved.

## 4. Evidence table

| Question | Evidence status |
|---|---|
| October 2025 BPM6 document exists in official IMF catalogue | VERIFIED |
| Publication date is 14 May 2026 | VERIFIED |
| Document is public/unrestricted PDF | VERIFIED |
| PDF body retrieved and inspected | NOT_RETRIEVED |
| Six country rows checked in October 2025 table | NOT_DONE |
| Exact IMF.STA:BOP dataflow constraint identified | UNKNOWN |
| Applicable Provision Agreement identified | UNKNOWN |
| Applicable Data Provider identified | UNKNOWN |
| Provider-level constraint resolved | UNKNOWN |
| Six-country formal eligibility | UNKNOWN |

## 5. Next retrieval procedure

Use the official IMF catalogue item's identifier `1792656603400855000` to obtain the PDF's actual download/content URL from the IMF document metadata or browser download action; then preserve the downloaded PDF and SHA-256, inspect all pages including continuation pages, and transcribe only the BOP start-date column for the six exact country codes. In parallel, use the SDMX Central REST structure service UI to select Structure Type = Dataflow, Agency = IMF.STA (if present), Structure ID = BOP, Version = 21.0.0; retrieve its references, then follow only actual returned Provision Agreement and Data Provider references. Do not guess artefact IDs or reuse BOP6 constraints.

## 6. Gate decision

- Official catalogue metadata verification: PASS.
- October 2025 table content review: NOT_RETRIEVED.
- Exact dataflow / provision / provider constraint resolution: UNKNOWN.
- Six-country formal eligibility: UNKNOWN.
- Quarterly coverage acceptance: NOT PASS.
- EMDE aggregation: BLOCKED.

## 7. Protected invariants

₹0 spend; official public sources only; no credentials, paid API, external contact, synthetic data, aggregation, annual-to-quarterly conversion, PR merge or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.


## 8. Follow-up verification (2026-11-15)

A fresh inspection of the official IMF Documents catalogue and BOP dataset page reconfirmed the October 2025 document metadata and publication date (14 May 2026), but neither page extraction exposed the PDF download target or body. The official IMF SDMX Central REST Web Service page and its Web Services Guide confirm that structure queries can be generated through the UI and that the service supports Dataflow and Provision Agreement queries. The registry overview currently exposes only a paginated sample of dataflows; it does not establish the absence of an IMF.STA BOP dataflow. Direct retrieval of the guessed `IMF.STA/BOP/21.0.0` path remains inaccessible through this web retrieval channel. Consequently no negative inference is permitted.

Sources:
- IMF Documents catalogue: https://data.imf.org/en/Documents
- IMF BOP dataset: https://data.imf.org/Datasets/BOP
- IMF SDMX Central REST Web Service: https://sdmxcentral.imf.org/webservice/schema.html
- IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- SDMX Central Dataflow overview: https://sdmxcentral.imf.org/data/overview.html

Status remains unchanged: October 2025 PDF table NOT_RETRIEVED; exact IMF.STA Dataflow / Provision Agreement / Provider constraints UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 9. SDMX API contract validation and exact query specification (2026-11-15)

The official IMF SDMX Central Web Services Guide (last updated May 2025) was inspected. It confirms:
- REST entry point: `https://sdmxcentral.imf.org/sdmx/v2/`.
- Supported structure resources include `dataflow`, `provisionagreement`, `dataproviderscheme`, `contentconstraint`, `actualconstraint`, `allowedconstraint`, and `attachmentconstraint`.
- The query path has agencyID, structureID, version and optional itemID; the guide's references parameter supports `all`, `children`, `parents`, etc.
- A Dataflow or Provision Agreement can carry constraints; the registry's own landing page explains that constraints can restrict allowable content beyond the DSD.
- The SDMX Central Web Service UI allows the query URL to be generated from Structure Type, Agency, ID and Version selectors and downloaded. This is the preferred reproducible manual retrieval route if direct API retrieval is inaccessible.

Exact query template prepared from the documented contract (not evidence that the response exists):
`https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF.STA/BOP/21.0.0?references=all&format=sdmx-2.1`

Follow-up structure query templates, to be populated only from actual returned references:
`.../structure/provisionagreement/{agency}/{id}/{version}?references=all&format=sdmx-2.1`
`.../structure/contentconstraint/{agency}/{id}/{version}?format=sdmx-2.1`
`.../structure/actualconstraint/{agency}/{id}/{version}?format=sdmx-2.1`
`.../structure/attachmentconstraint/{agency}/{id}/{version}?format=sdmx-2.1`

Direct web retrieval attempts against the exact Dataflow URL, broad IMF Dataflow listing, ContentConstraint listing and ProvisionAgreement listing returned inaccessible through this web retrieval interface. These errors do not establish HTTP status at the origin and do not prove the structures are absent. No response body, artefact ID, provider, or constraint was fabricated.

The IMF SDMX Central registry currently visibly lists IMF:BOP6_CONSTRAINT attached to BOP6[1.0] and IMF:BOP_BP6_CONSTRAINT attached to BOP_BPM6[1.0]. These remain distinct from the target IMF.STA:BOP(21.0.0) flow unless an actual reference establishes a relationship.

Official sources:
- https://sdmxcentral.imf.org/webservice/schema.html
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (May 2025 guide; resources and references parameters)
- https://sdmxcentral.imf.org/ (registry description of Dataflow and Provision Agreement constraints)
- https://sdmxcentral.imf.org/data/constraints.html
- https://sdmxcentral.imf.org/data/overview.html

Status: API contract and reproducible query specification PASS; actual target Dataflow response NOT_RETRIEVED; target Provision Agreement/Provider/Constraint UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 10. Registry live-page cross-check and non-transferability finding (2026-11-15)

Fresh inspection of the live IMF SDMX Central pages established:

1. The Dataflow overview is a paginated registry list (216 entries; visible first page shows CBSL and ESTAT entries including ESTAT BPM6_BOP_M and BPM6_BOP_Q). This is not a complete list of IMF entries and does not establish absence of an IMF.STA:BOP flow.
2. The Reporting Constraints page visibly lists:
   - `IMF:BOP6_CONSTRAINT` → `BOP6[1.0]`
   - `IMF:BOP_BP6_CONSTRAINT` → `BOP_BPM6[1.0]`
   Both are Dataflow cube-region constraints. Neither visible row names `IMF.STA:BOP(21.0.0)` or `IMF.STA:DSD_BOP(24.0.0)`; no equivalence or applicability is assumed.
3. The Provision Agreements page is also paginated (1,001 entries). Its visible first page includes country-specific agreements such as `IMF:AT_BOP` and `IMF:BE_BOP`, but no exact target reference for the IMF.STA BOP dataset is established. A text find on the opened rendered page returned no BOP match because the detail table is dynamically populated; this is not evidence of absence.
4. The Registrations page is a separate registry view with Dataflow, Data Provider and registered URL columns. A search-result extract lists provider registrations for `IMF:BOP6(1.0)`, `IMF:BOP_BPM6(1.0)` and `IMF:BOP_GBPM6` flows. Those are not automatically the target `IMF.STA:BOP(21.0.0)`; provider identity cannot be transferred between them.
5. The REST Web Service UI explicitly offers Structure Type, Agency, Structure ID, Version, References and Download controls. This confirms the exact reproducible UI route: select Structure Type=Dataflow; Agency=IMF.STA only if the selector actually offers it; Structure ID=BOP; Version=21.0.0; References=All; select SDMX-ML v2.1 (or retain supported default only if documented); inspect generated Query URL; use Download; preserve untouched response and SHA-256. If Agency/ID/version are not offered or query returns a formal SDMX error, preserve the response and do not substitute IMF:BOP6 or IMF:BOP_BPM6.
6. Official registry overview explains constraints can attach to DSD, Dataflow, Provision Agreement or Data Provider and cascade. The exact target chain must be followed only from returned references.

Sources:
- Dataflow overview: https://sdmxcentral.imf.org/data/overview.html
- Reporting constraints: https://sdmxcentral.imf.org/data/constraints.html
- Provision Agreements: https://sdmxcentral.imf.org/data/provisionAgreements.html
- Registrations: https://sdmxcentral.imf.org/data/registrations.html
- REST Web Service UI: https://sdmxcentral.imf.org/webservice/structure.html
- Registry constraint semantics: https://sdmxcentral.imf.org/overview.html

Gate: live registry page cross-check PASS; exact target Dataflow and its references NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 11. Critical namespace and endpoint correction — IMF SDMX Central vs IMF Data Portal (2026-11-15)

A fresh check of the live REST UI and the public SDMX service catalogue found an important namespace distinction that corrects the earlier query plan:

### A. IMF SDMX Central registry
- The live SDMX Central Structure UI's Agency selector lists `IMF` (International Monetary Fund) and does not list `IMF.STA` among the visible agency choices.
- The live Data Structure Definitions page lists agency `IMF`, ID `BOP`, latest version `2.6.0`, name "Balance of Payments and International Investment Position".
- The live UI offers Structure Type, Agency, Structure ID, Version, References, Query URL and Download controls.
- Therefore the previously prepared SDMX Central query `IMF.STA/BOP/21.0.0` is NOT a valid registry UI selection based on the currently visible agency/DSD catalogue. It must not be submitted as if confirmed. The registry-side query to test next is the DSD `IMF:BOP(2.6.0)` with References=All, then inspect actual returned Dataflow references. This DSD is not automatically equivalent to the IMF Data Portal dataset `IMF.STA:BOP(21.0.0)`.

### B. Separate IMF Data Portal service
- The public SDMX service catalogue lists a distinct IMF Data Portal service at `https://api.imf.org/external/sdmx/2.1` and `https://api.imf.org/external/sdmx/3.0`, separate from IMF SDMX Central at `https://sdmxcentral.imf.org/sdmx/v2/`.
- Thus IMF.STA dataset references, if valid in the IMF Data Portal, must be resolved against that separate service and not assumed to be SDMX Central registry identifiers.
- Opening the two API base paths without a resource returned 404 through the web retrieval interface. This is not a test of a specific structure resource and does not establish endpoint failure. No exact structure response has been retrieved from either service.

### C. Correct next retrieval sequence
1. In SDMX Central UI select Structure Type = Data Structure; Agency = IMF; Structure ID = BOP; Version = 2.6.0; References = All; inspect generated query URL and download the structure message. Record raw bytes/hash and extract actual Dataflow/constraint references.
2. Separately, for the original IMF Data Portal target, consult the IMF Data Portal's own SDMX 2.1/3.0 service catalogue and construct the target resource path only from its documented resource patterns and an actual returned agency/ID/version. Do not transplant registry IDs across services.
3. Follow Provision Agreement and Data Provider only from actual references returned by the relevant service.

### D. Gate
- Live UI namespace/catalogue cross-check: PASS.
- Prior IMF.STA/BOP/21.0.0 query as a SDMX Central UI selection: SUPERSEDED / INVALID FOR THAT UI (not evidence that the dataset itself is invalid).
- IMF:BOP(2.6.0) DSD response: NOT_RETRIEVED.
- Separate IMF Data Portal target structure response: NOT_RETRIEVED.
- Exact constraints / provision agreement / provider: UNKNOWN.
- October 2025 PDF country table: NOT_RETRIEVED.
- Six-country formal eligibility: UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.

Sources:
- SDMX Central Structure UI: https://sdmxcentral.imf.org/webservice/structure.html
- SDMX Central DSD catalogue: https://sdmxcentral.imf.org/data/datastructure.html
- IMF SDMX public service catalogue: https://browser.sdmx.io/agencies/IMF
- IMF SDMX Central registry overview: https://sdmxcentral.imf.org/


## 12. SDMx Global Registry canonical BOP DSD endpoint discovery (2026-11-15)

A new official source check found the SDMx Global Registry as the canonical public download location for the IMF-maintained BOP DSD:
- SDMx official BOP DSD page says structures and related dataflows/constraints are hosted in the SDMx Global Registry and are accessible without authentication.
- It identifies BOP DSD version 2.6.0, maintenance agency IMF, and provides SDMX-ML 2.1 and SDMX 3.0 download links.
- The exact SDMX-ML 2.1 endpoint exposed by the official link is:
  `https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1`
- A second request with `references=all` was constructed from the documented SDMX Central/SDMX REST query contract:
  `https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=all`

Retrieval status must be precise: the web retrieval interface attempted the exact official SDMX-ML endpoint but could not render its XML response (reported unsupported content-type application/xml). The references=all URL was reported inaccessible by the same web interface. This is a client/rendering limitation, not proof of origin HTTP failure, not proof the artefact is absent, and not a successful inspection of XML. No DSD dimensions, code lists, dataflows or constraints have been extracted from this response yet.

This is a different source path from the IMF SDMX Central catalogue UI and the IMF Data Portal APIs. The IMF-maintained BOP DSD v2.6.0 is a structural reference, not automatically the same artefact/version as the earlier IMF.STA BOP dataset reference. No cross-service equivalence is asserted.

Additional verified context: SDMx states that DSD versions are maintained annually and previous versions may remain valid where backward compatibility is preserved; the BOP 2.6.0 package was published December 2025. This does not prove compatibility with the target dataset's earlier version.

Official sources:
- https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
- https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1
- https://sdmxcentral.imf.org/webservice/schema.html
- https://data.imf.org/en/Resource-Pages/IMF-API

Gate: canonical BOP DSD endpoint discovery PASS; XML body and references NOT_RETRIEVED; IMF Data Portal dataset structure NOT_RETRIEVED; exact target constraints/provision/provider UNKNOWN; October 2025 PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 13. Official service-catalogue and retrieval-channel audit (2026-11-15)

### Findings
1. The SDMX Global Registry's own Web Service UI confirms REST entry URL `https://registry.sdmx.org/sdmx/v2/`, selectable structure types including Dataflow, Data Structure and Provision Agreement, SDMX-ML 2.1/3.0 output, References=All, and a Download control. This is the correct unauthenticated registry route to retrieve the IMF BOP DSD package and references.
2. SDMx official BOP page confirms BOP DSD v2.6.0 is maintained by IMF, stored in the Global Registry, and has direct SDMX-ML 2.1 / SDMX 3.0 links. Older DSD versions may remain valid when backward-compatible; no compatibility conclusion is made for the earlier IMF.STA dataset.
3. IMF's public SDMX service catalogue explicitly separates:
   - IMF Data Portal 2.1: `https://api.imf.org/external/sdmx/2.1`
   - IMF Data Portal 3.0: `https://api.imf.org/external/sdmx/3.0`
   - IMF SDMX Central 2.1/3.0 services.
   These are distinct services, not interchangeable identifiers.
4. IMF's own API information page says the APIs are SDMX 2.1/3.0 and that the Swagger explorer requires signing in with a beta portal account. No such credentials were used or requested; this route was not tested with authenticated access.
5. The direct Global Registry XML endpoint was attempted in this environment; the web retrieval layer could not render the XML media type, and the container download attempt failed. Therefore the XML bytes, SHA-256, DSD dimensions and referenced codelists remain NOT_RETRIEVED. The official BOP package link's CIRCABC target returned 404 in the retrieval layer; no claim is made about the origin server's actual status.
6. IMF Documents catalogue continues to expose the October 2025 BPM6 PDF metadata (item `1792656603400855000`, published 14 May 2026) but the PDF binary/body remains NOT_RETRIEVED. No inference is made about the six countries from the October 2025 edition.

### Correct next action
Use the unauthenticated Global Registry Web Service UI to select Data Structure → Agency IMF → ID BOP → version 2.6.0 → SDMX-ML v2.1 → References All → Download. If the browser download succeeds, preserve the raw XML and SHA-256, parse the actual returned DSD and reference list, then follow only the returned Dataflow / Provision Agreement / Provider / Constraint identifiers. If not, record the exact UI error and stop; do not use credentials, paid APIs, external contact, or guessed identifiers. Separately, do not access the IMF Data Portal Swagger unless an authorized beta portal account is already available and explicitly approved.

Official sources:
- https://registry.sdmx.org/webservice/structure.html
- https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
- https://browser.sdmx.io/agencies/IMF
- https://data.imf.org/en/Resource-Pages/IMF-API
- https://data.imf.org/en/Documents
- https://data.imf.org/Datasets/BOP

Gate: service-catalogue separation and unauthenticated registry route PASS; XML binary/body NOT_RETRIEVED; IMF Data Portal Swagger requires beta portal sign-in (not accessed); exact target constraints/provision/provider UNKNOWN; October 2025 PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 14. IMF BOP concept-scheme and candidate codelist inventory (2026-11-15)

### Verified registry catalogue facts
The SDMx Global Registry's Concept Scheme catalogue lists:
- Agency: IMF
- ID: `CS_BOP`
- Name: Balance of Payments Concept Scheme
- Latest version: `1.20.0`

The same registry's Codelist catalogue visibly lists these IMF codelists:
- `CL_ACCOUNT_ENTRY` — Accounting entry code list — 1.5.0
- `CL_ACCOUNTS_ITEM` — Item classification code list — 1.8.0
- `CL_ADJUSTMENT` — Adjustment indicator — 1.4
- `CL_AREA` — Area code list — 2.0.0
- `CL_COMP_METHOD` — Compilation methodology code list — 1.2
- `CL_CURRENCY` — Currency of issuance or invoicing code list — 1.6.1
- `CL_FSENTRY` — Flow or stock entry code list — 1.1
- `CL_FUNCTIONAL_CAT` — Functional category code list — 1.10.1
- `CL_GFSM_STO` — Stocks, Transactions, Other Flows — 1.0
- `CL_ORGANISATION` — Compiling organisation code list — 2.1.0
- `CL_TIME_COLLECT` — Time period collection code list — 1.0
- `CL_UNIT` — Unit of measure code list — 1.19.0

These are candidate structural dependencies by subject matter only. The DSD XML body has not been retrieved, so no claim is made that any particular listed codelist is referenced by BOP DSD 2.6.0 or by the earlier IMF.STA BOP dataset. Version compatibility is not assumed.

### Extraction limitation
The concept-scheme page is a dynamic detail view; the catalogue exposes the CS_BOP identity/version but not its complete concept items in the retrieved page. A direct URN query was inaccessible through the web retrieval interface. No concept IDs, descriptions or representations were copied from inference.

### Correct next step
Use the Global Registry UI to select Concept Scheme → Agency IMF → ID CS_BOP → version 1.20.0 → View/Export SDMX-ML 3.0 (or supported export), then retrieve and hash the actual response. In parallel select each candidate codelist only when the BOP DSD XML or concept scheme's actual references identify it. Record each exact returned URN/version and compare with the target dataset's own service; do not treat a catalogue listing as proof of DSD attachment.

Official sources:
- https://registry.sdmx.org/items/conceptscheme.html
- https://registry.sdmx.org/items/codelist.html
- https://registry.sdmx.org/data/datastructure.html
- https://registry.sdmx.org/webservice/structure.html

Gate: CS_BOP catalogue identity/version PASS; candidate IMF codelist inventory PASS; actual concept contents NOT_RETRIEVED; BOP DSD-to-codelist linkage UNKNOWN; exact target constraints/provision/provider UNKNOWN; October 2025 PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 15. Registry-native cross-reference route and provenance boundary (2026-11-15)

A higher-value route than guessing REST references was confirmed in the live SDMx Global Registry UI:

1. **Structure References** page explicitly supports selecting Structure Type, Agency and a structure, then generating a report. Its description says the report identifies cross-referenced maintainable structures and cross-referenced identifiable components. It also offers an all-structures cross-reference workbook with three worksheets (maintainables and their reference counts; maintainable-to-maintainable references; identifiable-to-identifiable references).
2. **Export Reports** page explicitly offers:
   - Concept Usage for All Agencies: which Concept Schemes are referenced by which Data Structures.
   - Codelist Usage for All Agencies: which Codelists are referenced by which Data Structures.
   - Data Structures Report for All Agencies.
   - Codelist Report for All Agencies.
   These are Excel 2007 XLSX exports.
3. **Concept Scheme detail** UI offers References, Export SDMX-ML 3.0, Export Excel and View Concept Scheme; its detail grid has Id, Name, Representation and Description. This is the proper source for exact CS_BOP concept inventory once a row is selected.
4. **REST Structure UI** supports Structure Type, Agency, Structure ID, Version, format, Detail and References selectors, and displays a generated Query URL plus Download. The previous failure to retrieve XML via text/web interface should not be treated as registry failure; the UI provides a browser-native download route.

### Precise next execution sequence
A. Open Structure References; choose Structure Type = Concept Scheme; Agency = IMF; select `CS_BOP(1.20.0)`; Generate Report. Save the result and record exact structures that reference it.
B. Choose Structure Type = Data Structure; Agency = IMF; select `BOP(2.6.0)`; Generate Report. Save all exact outgoing and incoming references.
C. Run the Concept Usage and Codelist Usage XLSX exports; filter locally for `IMF:CS_BOP` and `IMF:BOP` only after download. This establishes exact DSD-to-concept/codelist links, not just candidate lists.
D. In Concept Scheme details, select `CS_BOP(1.20.0)`, export Excel, and preserve actual concept IDs, names, representations and descriptions.
E. Follow only exact returned references to Dataflow, Provision Agreement, Data Provider and Constraints. Keep the SDMx Global Registry service namespace separate from IMF Data Portal identifiers.

### Evidence and gate
- Registry-native cross-reference and export capabilities: VERIFIED.
- Actual generated reference report/XLSX files and hashes: NOT_YET_DOWNLOADED.
- Exact CS_BOP-to-BOP DSD link: UNKNOWN.
- Exact BOP DSD-to-codelist links: UNKNOWN.
- Exact target dataset constraints/provision/provider: UNKNOWN.
- October 2025 PDF body: NOT_RETRIEVED; six-country eligibility UNKNOWN.
- Quarterly coverage NOT PASS; EMDE aggregation BLOCKED.

Official sources:
- https://registry.sdmx.org/structurereferences/structureReferences.html
- https://registry.sdmx.org/export-reports.html
- https://registry.sdmx.org/items/conceptscheme.html
- https://registry.sdmx.org/webservice/structure.html

No credentials, paid services, external contact, synthetic data or production changes used.


## 16. Registry Dataflow inventory cross-check and UI execution boundary (2026-11-15)

### New public catalogue observations
- The SDMx Global Registry Data Structure Definitions catalogue lists agency IMF, ID `BOP`, name "Balance of Payments and International Investment Position", latest version `2.6.0`.
- The Registry Concept Scheme catalogue lists agency IMF, ID `CS_BOP`, name "Balance of Payments Concept Scheme", latest version `1.20.0`.
- The Registry Dataflows overview extraction visibly lists `ESTAT:BPM6_BOP_M(2.6.0)` and `ESTAT:BPM6_BOP_Q(2.6.0)` among the first visible rows. These are ESTAT agency dataflows; they must not be relabelled as IMF dataflows or assumed to be the target IMF Data Portal dataset.
- The public Data Providers catalogue shows `ESTAT:IMF` = IMF as a provider under the ESTAT agency, distinct from agency `IMF`. This is a provider-catalogue fact only; it does not establish a BOP Provision Agreement, registration or constraint for the target dataflow.
- Registry home documentation says constraints may attach to DSD, Dataflow, Data Provider or Provision Agreement and cascade. This confirms why a DSD-only check is insufficient.

### Browser/UI execution audit
- The public Structure References page explicitly provides a selector for report generation, a structure-type/agency/structure selector and Generate Report action. The text extraction exposes controls but not the live populated selector options or generated report bytes.
- The public Export Reports page documents four XLSX reports (Concept Usage, Codelist Usage, Data Structures, Codelist). The web retrieval exposes the Download controls as labels, not downloadable target URLs or file bytes.
- Attempts to retrieve the Registry REST SDMX-ML URLs via the text retrieval interface returned inaccessible/internal errors. This is a retrieval-layer limitation only, not proof the Registry origin is unavailable.
- Therefore no XLSX, generated cross-reference workbook, SDMX-ML payload, or SHA-256 was acquired in this pass.

### Evidence classification
- IMF:BOP DSD 2.6.0 catalogue presence: VERIFIED.
- IMF:CS_BOP 1.20.0 catalogue presence: VERIFIED.
- ESTAT:BPM6_BOP_M and ESTAT:BPM6_BOP_Q catalogue presence: VERIFIED as ESTAT dataflows only.
- IMF BOP target Dataflow / Provision Agreement / provider registration / constraint chain: UNKNOWN.
- CS_BOP-to-BOP exact reference and BOP-to-codelist exact references: UNKNOWN.
- October 2025 PDF body: NOT_RETRIEVED; six-country eligibility UNKNOWN.
- Quarterly coverage NOT PASS; EMDE aggregation BLOCKED.

No credentials, paid services, external contact, synthetic data or production changes used.


## 17. IMF BOP dataset-page and October 2025 document metadata verification (2026-11-15)

### Official BOP dataset page
The IMF Data Portal's public BOP dataset page identifies:
- Dataset title: Balance of Payments (BOP).
- Publisher: International Monetary Fund; Department: Statistics Department (STA).
- Frequencies: Annual and Quarterly (catalogue metadata).
- The page exposes API, View Data, Download and Documents navigation.
- The October 2025 BPM6 reporting document is listed under this dataset and under IIP.

### October 2025 document metadata (catalogue only)
The IMF Documents catalogue entry is:
- Item ID: `1792656603400855000`
- Title: `Economies Reporting on BPM6 Basis October 2025`
- Publication date: 14 May 2026
- Dataset association: Balance of Payments (BOP) and International Investment Position (IIP)
- Security classification: Public or Unrestricted
- Content type: Manual
- Format: PDF

The catalogue confirms that a public October 2025 document exists and is associated with BOP/IIP. It does not expose the PDF body, direct file URL or bytes in the retrieved page content. Therefore the document's country table has not been inspected in this pass and no country-level conclusion is drawn.

### Acceptance boundary
- BOP dataset catalogue metadata (publisher/department/frequency): VERIFIED.
- October 2025 document metadata and BOP/IIP association: VERIFIED.
- October 2025 PDF bytes/body/table: NOT_RETRIEVED.
- Six-country October 2025 inclusion/exclusion: UNKNOWN.
- Quarterly reporting eligibility remains UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.

No credentials, paid services, external contact, synthetic data or production changes used.


## 18. Official BOP/IIP aggregate methodology and nonreporting-economy estimate risk (2026-11-15)

### Official IMF statement
The IMF Data Portal page for "Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates" (historically BOPSY) states:
- It is an annual publication based on BPM6.
- Country-level information is based on actual data reported directly to the IMF or obtained from a country's National Summary Data Page, except accounts between individual countries and the IMF, which may be replaced with Fund Accounts data.
- World and country-group aggregates (other than Euro Area) combine reported country data with estimates for nonreporting economies.
- Those estimates are derived from additional sources including WEO and External Wealth of Nations databases.
- Euro Area aggregates are reported by the ECB and represent transactions/positions vis-à-vis the rest of the world.

### Research implication
1. An IMF-published country-group aggregate is not proof that every member country has directly reported data for the same period.
2. A published EMDE/world aggregate may include estimates for nonreporting economies; it must not be used as direct evidence of quarterly country-level reporting eligibility or as a substitute for missing reporter observations.
3. The research must distinguish (a) reporter-level observations, (b) source-reported aggregate values, and (c) IMF estimated contributions for nonreporting economies. If the public source does not expose the decomposition, the aggregate's reporter/nonreporter split is UNKNOWN.
4. This supports retaining the current hard gate: no EMDE aggregate promotion until reporter-level coverage and provenance are independently proven. No estimate backfill or synthetic row creation is authorized.

### Acceptance boundary
- Official BOPSY aggregate methodology statement: VERIFIED from IMF Data Portal.
- October 2025 BPM6 PDF bytes/body/table: NOT_RETRIEVED.
- Six-country October 2025 inclusion/exclusion: UNKNOWN.
- Quarterly country eligibility: UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.

No data rows created, no estimates substituted, no credentials/paid services/external contact, and no production changes.

## 19. Progress accounting and no-repeat control (2026-11-15)

### Fixed definitions
Percentages below are completion ratios for explicitly enumerated work packages or already approved acceptance gates. They are not confidence, production readiness, or an estimate of total project effort.

**October 2025 BPM6 PDF retrieval-and-country-table work package: 25% (1/4 milestones).**
1. Official catalogue identity, publication date, BOP/IIP association, public classification and PDF format verified — PASS.
2. Direct public PDF download target resolved — NOT_DONE.
3. PDF bytes acquired, preserved and SHA-256 recorded — NOT_DONE.
4. Country table extracted and compared with April 2025 inventory for CAF, ERI, GNQ, SOM, TCD, TKM — NOT_DONE.

The 25% reflects only milestone 1 of 4. It does not imply any country eligibility conclusion.

**IMF BOP workstream acceptance: 5/7 = 71.4%**, using the pre-existing seven-gate rubric and last reconciled ledger decision. Do not add a gate for catalogue metadata already included in the existing evidence. The unfinished reporter coverage / full India panel / EM aggregation items remain partial, NOT_DONE or BLOCKED as already recorded. The recent October PDF catalogue re-verification and aggregate methodology safeguard do not promote any gate.

**Full PRECISION-WIRES V11.3 project progress: NOT_CALCULABLE.** The master ledger does not contain a complete current set of all workstream gate denominators and approved weights; prior P0, Factor Registry, historical regime and event-study statuses require revalidation. Do not substitute the IMF 71.4% for the project-wide percentage.

### No-repeat decision
- Do not repeat catalogue metadata searches for item 1792656603400855000; identity/date/public-PDF metadata is already verified.
- Do not repeat the April 2025 six-country inventory review or the 39-country annual frequency/continuity audits absent new source evidence.
- Do not re-run the successful 110-row India annual/quarterly acquisition and arithmetic reconciliation absent code/source changes.
- Next work should target the unresolved direct PDF file target via the official IMF document item/download action. If the interface cannot expose a download target, record a precise retrieval limitation and move to a distinct unresolved gate; do not re-label the catalogue as the PDF.
- Continue preserving all prior run failures, fixes, artifacts, commits, hashes and superseding decisions; do not replace historical entries.

No new country-level evidence acquired in this progress reconciliation. No credentials, paid services, synthetic data, external contact or production changes.

## 20. IMF India 110-row vintage/revision readiness audit (2026-11-15)

### Scope and reproducibility
Read the committed research CSV and its JSON manifest directly from the research branch; no new API acquisition or data mutation was performed.
- CSV: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv`
- Manifest: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.manifest.json`
- Manifest declares 110 rows and combined CSV SHA-256 `260ccc247ec564737bb3afe0a820c2435e37a58f588603241274537eca99f1b9`.
- Re-read CSV contains 110 data rows, four exact series with counts 11/11/44/44, and zero duplicate series-period keys. The manifest's four raw response hashes and row counts align with the four series declarations.

### Actual CSV metadata findings
- CSV header has 20 columns; none is a vintage, revision, release-date, retrieval-timestamp or publication-timestamp field.
- `SOURCE`, `STATUS`, `ACCESS_SHARING_NOTES`, `OVERLAP` are null in all 110 rows.
- `IFS_FLAG` is true on 55 asset rows and null on 55 liability rows; null is preserved as UNKNOWN, not false.
- `SCALE=6`, `PRECISION=6`, `DERIVATION_TYPE=O`, `ACCESS_SHARING_LEVEL=PUBLIC_OPEN`, `SECURITY_CLASSIFICATION=PUB` each appear on all 110 rows.
- The source response SHA is carried per series, not per vintage. It identifies the archived response body but does not establish historical revisions or a vintage timeline.

### Decision
- Committed CSV/manifest structural and key-integrity re-audit: PASS (110/110 rows; four series counts match; no duplicate series-period keys).
- Revision/vintage readiness: NOT_READY / NOT_ESTABLISHED from this dataset. The acquired 110 observations are one archived response vintage per series; no revision history or source timestamp is represented in the CSV.
- Do not infer that the values were never revised. Do not use current archived values as original first-release observations. No revision-aware backtest or vintage-sensitive research acceptance can be promoted from this file alone.
- Next distinct action: identify an official IMF revision/vintage endpoint or a reproducible public release archive; if none is public, explicitly keep revision/vintage acceptance UNKNOWN and scope the India panel to current archived observations only.

### Progress accounting
- This bounded 110-row vintage-readiness audit: 100% of defined checks completed (header/row count/series counts/duplicate key check/manifest alignment/attribute distributions). Evidence outcome is NOT_READY for revision history; completion of the audit is not acceptance of the revision gate.
- IMF BOP workstream accepted gates remain 5/7 (71.4%) on the pre-existing rubric.
- October 2025 PDF retrieval package remains 25% (1/4 milestones); official catalogue metadata PASS, direct file target/PDF bytes/table NOT_DONE.
- Full PRECISION-WIRES V11.3 project progress remains NOT_CALCULABLE pending reconciled workstream denominators and approved weights.

No new observation values were created or changed. No credentials, paid services, synthetic data, external contact, PR merge or production changes.

## 21. Extraction-contract compliance matrix against committed India 110-row panel (2026-11-15)

### Basis and method
Compared the exact required-field contract in `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md` (Section 3 and Section 5) against the committed 110-row CSV and its JSON manifest. This is a schema/provenance readiness review, not a new observation acquisition. No source values or files were changed.

### Compliance matrix
| Required contract element | Evidence in CSV / manifest | Status |
|---|---|---|
| Reporting economy code | CSV COUNTRY=IND | PRESENT |
| Frequency and reference period | CSV FREQUENCY and TIME_PERIOD | PRESENT |
| BPM standard/version | CSV METHODOLOGY=BPM6; manifest | PRESENT |
| Dataflow/version | Manifest identifies IMF.STA:BOP(21.0.0) | PRESENT |
| Official dimension key/values | CSV dimension columns; manifest dimension order | PRESENT |
| Portfolio instrument classification | INDICATOR=P_F; total portfolio aggregate only | PARTIAL_SCOPE |
| Asset/liability direction | BOP_ACCOUNTING_ENTRY A_NFA_T / L_NIL_T | PRESENT |
| Measure/transaction basis | P_F and accounting-entry codes; manifest descriptions | PRESENT |
| Unit/currency and scale | UNIT=USD, SCALE=6 | PRESENT_AS_SOURCE_METADATA |
| Numeric value as published | OBS_VALUE | PRESENT |
| Observation status/confidentiality/estimation flags | DERIVATION_TYPE=O, ACCESS_SHARING_LEVEL=PUBLIC_OPEN, SECURITY_CLASSIFICATION=PUB; STATUS null; no OBS_STATUS/CONF_STATUS columns | PARTIAL |
| Source URL and dataset identifier | Dataset URN in manifest; per-response hash; exact request URLs documented in companion audit, not row-level | PARTIAL |
| Retrieval timestamp UTC | Not present in CSV or manifest series records | MISSING |
| Publication/release vintage | Not present | MISSING |
| Raw file checksum | Combined CSV hash and four response hashes in manifest | PRESENT |
| Exact series key uniqueness including vintage | Unique series-period keys checked; vintage dimension absent | PARTIAL |

### Interpretation
- The panel is structurally reproducible as a single archived response snapshot and has valid period-key uniqueness within the captured four series.
- It does not satisfy the full extraction contract for revision-aware/vintage-sensitive research because per-response retrieval timestamp and publication/release vintage are absent, and observation status/confidentiality detail is incomplete.
- `DERIVATION_TYPE=O` is retained as source-reported status evidence, but it does not replace the missing `OBS_STATUS`/`CONF_STATUS` fields specified by the contract.
- `P_F` is the total portfolio investment indicator. The panel does not split equity/investment-fund shares and debt securities. Do not claim instrument-level coverage beyond the total portfolio aggregate.
- Existing source URL and dataset identifiers in the companion audit/manifest do not create a per-row retrieval timestamp or release vintage.
- Preserve the 110-row data as the current archived snapshot; do not fabricate timestamps or backfill release vintage from the audit date.

### Gate outcome and progress
- This bounded extraction-contract comparison: 100% of the defined 16 contract elements reviewed.
- Contract compliance for a revision-aware panel: PARTIAL / NOT_READY (not PASS).
- Vintage/revision readiness remains NOT_READY; no new source vintage or revision series obtained.
- IMF BOP workstream acceptance remains 5/7 (71.4%) on the pre-existing rubric; this audit does not promote a gate.
- October 2025 PDF retrieval package remains 25% (1/4).
- Full PRECISION-WIRES V11.3 project progress remains NOT_CALCULABLE pending full workstream denominator/weight reconciliation.

### Next distinct action
Implement a separate research-only provenance sidecar schema for future source pulls that records actual retrieval timestamp (UTC), actual final URL, HTTP status, Content-Type, byte count, response SHA-256 and actual publication/release vintage where the source supplies it. If the source does not supply a release vintage, store null/UNKNOWN rather than the retrieval date. Do not alter the existing 110-row CSV or production pipeline; require a newly acquired source response before creating a new vintage record.

No credentials, paid services, synthetic timestamps, fabricated vintage, external contact, PR merge or production changes.

## 22. Research-only IMF BOP response provenance sidecar schema V1 (2026-11-15)

Created a versioned JSON Schema and capture contract on the research branch:
- `schemas/imf_bop_response_provenance.schema.json`
- `docs/IMF_BOP_RESPONSE_PROVENANCE_SIDECAR_V1.md`

The schema requires exact requested/final URL, GET method, exact series key, HTTP 200, Content-Type, actual UTC retrieval timestamp, positive response byte count, SHA-256 over exact raw response-body bytes, explicit vintage status, and research controls. It distinguishes `SOURCE_PROVIDED`, `NOT_EXPOSED_BY_SOURCE`, and `NOT_VERIFIED`. If source vintage is not exposed/not verified, release date and release ID must be null; retrieval time is never substituted for publication vintage.

The documentation defines capture order, rejection conditions, and the rule that every independently retrieved raw response gets its own sidecar. The existing India 110-row CSV and manifest remain untouched and are explicitly not retroactively compliant. No fabricated timestamp, release date, HTTP response, or checksum was added.

Schema/document creation and remote re-fetch verification completed. No new IMF observation response was acquired and no schema-instance validation against a real response was claimed. Thus the sidecar contract implementation milestone is COMPLETE, while live capture validation remains NOT_DONE. Revision-aware panel gate remains NOT_READY.

## 23. Official IMF BOP Portal vintage affordance audit (2026-11-15)

### Direct dataset-page inspection
Inspected the exact official BOP dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP . The rendered page exposes API, VIEW DATA, DOWNLOAD, Metadata, and Documents. It does not expose a visible "See Vintages" action or a vintage-history section in the retrieved page content. The API link redirects to the IMF API developer portal sign-in page. The official IMF API documentation states data are available through SDMX 2.1/3.0 and the Swagger explorer requires a beta portal account to sign in.

This is a bounded page/UI finding only. It does not prove that no authenticated API, internal endpoint, or downloadable release archive supports vintages. No login, credential use, or bypass was attempted.

### Cross-dataset distinction
The IMF public catalogue does show "See Vintages" for some other datasets (e.g. WEO and selected MFS datasets). That proves the portal has a vintage affordance for some datasets, not that BOP supports it. Do not transfer another dataset's vintage capability to BOP.

### Methodological grounding
The IMF BPM7 manual defines a data vintage as a data value/dataset released for use at a particular release period; a new vintage exists when the same reference-period data are released again at a different release period. Retrieval timestamp alone is not a vintage. Therefore the sidecar's separation of retrieval timestamp from source-provided release vintage is required.

### Decision
- BOP public page vintage affordance: NOT EXPOSED on inspected page.
- Publicly documented BOP vintage endpoint / historical release selector: NOT ESTABLISHED.
- Revision history for the existing India 110 observations: UNKNOWN / NOT_READY.
- Do not create a vintage from the page's publication date, today's retrieval time, commit time, or latest data value.
- Sidecar schema V1 remains useful for recording future actual response provenance, but it cannot create missing historical vintages.
- Next distinct avenue: investigate official IMF BOP publication/download archive records (dated public releases or dated raw files) and check whether at least two dated snapshots overlap the same India series-period keys. If no official dated snapshots exist, preserve UNKNOWN and keep revision-aware gate closed.

### Evidence
- Official BOP dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Official IMF API page: https://data.imf.org/en/Resource-Pages/IMF-API
- BPM7 manual (March 2025, white-cover version), Chapter 20, vintage definitions around printed page 661 / PDF extracted lines near Box 20.2.
- Other-dataset "See Vintages" examples are not BOP evidence.

This audit did not change data, the schema, production, or any prior acceptance gate.

## 24. Official IMF BOPSY annual-release archive avenue audit (2026-11-15)

### Official archive route identified
The official IMF dataset page for `BOP_AGG` identifies the World and Country Group Aggregates as the annual publication historically called BOPSY, released each November. Its 2025 explanatory notes are an official dated November 2025 release document. The IMF's 2024 BOP Introductory Notes are separately dated November 2024. IMF BOPCOM annual reports independently identify annual country BOP data through 2023 in BOPSY 2024 and through 2024 in BOPSY 2025.

Official sources inspected:
- BOP_AGG dataset page: https://data.imf.org/Datasets/BOP_AGG
- BOPSY 2025 Explanatory Notes (November 2025): https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
- BOP Introductory Notes (November 2024): https://data.imf.org/-/media/iData/External-Storage/Documents/D7E2CE23AF2340EFA7932CF6CD7DD11A/en/BOP-Introductory-Notes-as-of-November-2024.pdf
- BOPCOM 2025 Annual Report: https://www.imf.org/-/media/files/publications/balance-of-payments-statistics/abpea2025001.pdf
- BOPCOM 2024 Annual Report: https://www.imf.org/-/media/files/publications/balance-of-payments-statistics/abpea2024001.pdf

### What is established
- BOPSY is an annual November publication.
- BOPSY 2024 contains annual BOP/IIP statistics through 2023; BOPSY 2025 contains annual BOP/IIP statistics through 2024.
- The 2025 notes list India last reported BOP period as 2024.
- The BOP_AGG page states country-level information is based on actual reported data or National Summary Data Page sources, but World/country-group aggregates can include estimates for nonreporting economies.
- The November 2024 and November 2025 notes are distinct dated official documents and therefore establish a dated publication-document lineage.

### What is NOT established
- The two notes PDFs are methodology/country-overview documents, not two archived raw observation snapshots for the four exact India series `IND.A_NFA_T.P_F.USD.A`, `IND.L_NIL_T.P_F.USD.A`, `IND.A_NFA_T.P_F.USD.Q`, and `IND.L_NIL_T.P_F.USD.Q`.
- The BOP_AGG page's country/group aggregate tables are not automatically equivalent to the Portal BOP dataflow `IMF.STA:BOP(21.0.0)` or its exact 110-row India panel. Group/world aggregates can contain IMF estimates; do not use them as reporter observations or vintage substitutes.
- No two dated raw BOP observation files with overlapping exact India series-period keys were retrieved in this audit.
- The legacy IMF SDMX pilot BOP dissemination page is explicitly last updated 9 January 2013; it is not a 2024/2025 revision archive.
- Therefore the official BOPSY publication-document archive avenue is DISCOVERED, but a usable exact-series vintage archive remains NOT_ESTABLISHED.

### Gate decision
- Official annual publication archive discovery: PASS (document lineage).
- Exact India BOP raw snapshot pair: NOT_DONE.
- Revision comparison: NOT_DONE.
- India revision/vintage readiness: UNKNOWN / NOT_READY.
- Do not infer that values changed or did not change from annual report coverage statements, country overview periods, or methodology PDFs.
- Next action: use the BOP_AGG dataset's official View Data/Download route only to determine whether individual country tables can be exported as raw country-level observations with an identifiable release vintage. Accept only if the exact series dimensions and country reporter status can be matched; otherwise reject as non-equivalent.

This is a source-route discovery audit, not a data extraction or revision-comparison PASS. No prior CSV/manifest or acceptance gate was changed.

## 25. BOPSY country-table export affordance audit (2026-11-15)

### Exact official-document finding
The official BOPSY November 2025 Explanatory Notes PDF was retrieved and inspected (31 pages). It explicitly states:
- Country-level information is based on actual data reported directly to IMF or obtained from the country's National Summary Data Page, with a stated exception for accounts between individual countries and IMF (PDF pp. 3; lines 21-27).
- Individual country tables can be found in the "Summary of International Transactions and Positions" table (PDF p. 4; lines 99-104).
- Users can customize how they view and download data from the database (PDF p. 3; lines 65-73).
- The country overview lists India BOP last reported period 2024 (PDF p. 8; line 217).
- The same notes explain estimates for nonreporting economies in world/country-group aggregates, including WEO-based gap filling (PDF pp. 3-4; lines 28-64). These are not to be treated as reporter-level observations.

Official source:
https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
Dataset page:
https://data.imf.org/en/datasets/IMF.STA:BOP_AGG

### What the page/UI inspection establishes
The BOP_AGG page exposes a VIEW DATA control and a DOWNLOAD control, and links the November 2025 notes. The notes specify that individual country tables are available within the "Summary of International Transactions and Positions" table. This is a concrete official route to investigate, more precise than treating the entire BOP_AGG aggregate as a single data series.

### Critical non-equivalence / unresolved checks
The retrieved public page text does not expose the underlying dashboard table's complete schema, data export payload, exact observation dimensions, series keys, or a versioned downloadable country-level raw file. Therefore this audit cannot certify that the country table contains the exact Portal series keys `IND.A_NFA_T.P_F.USD.A` / `IND.L_NIL_T.P_F.USD.A`, nor that its downloadable content is an archived 2025 vintage snapshot.
The November 2025 country overview's "last reported period 2024" is coverage metadata, not a revision history or proof of the exact P_F portfolio component series.
No export was downloaded and no vintage comparison performed.

### Decision
- Official country-table access route documented: PASS.
- Exact country table export/schema inspected: NOT_DONE.
- Exact India P_F assets/liabilities mapping: UNKNOWN.
- Dated 2025 raw country snapshot and second overlapping vintage: NOT_DONE.
- Revision/vintage readiness: UNKNOWN / NOT_READY.
- No use of world/group aggregates as substitutes; no synthetic data, inferred keys, or fabricated release timestamps.
- Next highest-value action: resolve the BOPSY "Summary of International Transactions and Positions" table's actual dashboard/export target from the public page's underlying links/metadata, then test a single India country table export and schema before any bulk retrieval.

This bounded affordance audit is complete; it does not promote a data or revision gate.

## 26. BOPSY dashboard target resolution and export-schema boundary audit (2026-11-15)

### Official dashboard target resolved
The BOP_AGG dataset page's "DASHBOARD RELEASE Power BI Dashboard" link resolves to the official IMF Data report page:
https://data.imf.org/en/dashboards/bopsy%20dashboard
The report page identifies the title "BOPSY Dashboard", publication date 19 November 2025, and dataset association with "Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates". The BOP_AGG page also exposes VIEW DATA and DOWNLOAD controls.

### Export/schema inspection result
The publicly retrievable report-page representation exposes report identity and dataset association only. It does not expose the embedded Power BI report payload, direct Power BI report/embed URL, table visual's query metadata, export action URL, downloadable raw file URL, or country table schema. The IMF Data page's Tables catalogue route also returned only its shell/navigation in the public representation. Thus no exact table/dashboard export endpoint could be verified from the public page response.

### Evidence boundary and decision
- Official BOPSY Dashboard identity, publication date, and dataset association: PASS.
- Direct dashboard/embed target and table visual identification: NOT_ESTABLISHED.
- Country table downloadable raw payload/schema: NOT_DONE.
- India exact P_F assets/liabilities key mapping: UNKNOWN.
- Dated raw 2025 India snapshot and a second overlapping snapshot: NOT_DONE.
- Revision/vintage readiness: UNKNOWN / NOT_READY.
- This is a bounded public-page inspection result, not evidence that no export exists in the interactive dashboard or an authenticated session. No login, credential, or bypass was attempted.
- Do not substitute World/Regional aggregates or country overview metadata for raw country observations.
- Next permissible action: inspect only public browser-visible dashboard interactions / officially exposed downloadable resource links if available; if no unauthenticated public export target is exposed, stop and record access limitation rather than infer endpoints or automate undocumented APIs.

No data files, CSVs, manifests, source captures, or prior acceptance gates were modified.

## 27. Separate IMF Balance of Payments (BOP) country dataset route identified (2026-11-15)

### Distinct official dataset route
A new official IMF dataset page was identified: https://data.imf.org/Datasets/BOP
Title: "Balance of Payments (BOP)".
The page exposes API, VIEW DATA, DOWNLOAD and Metadata controls, and describes the dataset as transactions between residents and nonresidents, covering goods/services, primary/secondary income, capital and financial accounts. Frequency is Annual and Quarterly. This is distinct in name and purpose from BOP_AGG (World and Country Group Aggregates / BOPSY).

Official page also states relevant metadata/highlights include BPM5, BPM6 Conversion Matrix, and IMF Committee on Balance of Payments Statistics materials.
The IMF API documentation states data are exposed through SDMX 2.1 and SDMX 3.0 APIs; Swagger exploration requires beta portal account sign-in. No sign-in or bypass was attempted.

### Why this is the correct next route to inspect
The BOP dataset is the official country-level Balance of Payments dataflow candidate, whereas BOP_AGG is annual World/Country Group Aggregates. The BOP page supports annual and quarterly frequency, matching the frequency class needed for India country series. This makes it a more direct source candidate than BOPSY aggregate dashboard for country-reporter data.
However, dataset page identity/frequency alone does not prove exact dimensions, exact series-key equivalence, revision/vintage history, or a dated archived download.

### Boundaries and next checks
- Official BOP dataset page and annual/quarterly frequency: DISCOVERED / PASS.
- Exact portal dataflow version and DSD mapping for this page: must be revalidated against the already known `IMF.STA:BOP(21.0.0)` and `DSD_BOP(24.0.0)`; do not assume version equivalence solely from page title.
- Exact India series mapping to `IND.A_NFA_T.P_F.USD.A/Q` and `IND.L_NIL_T.P_F.USD.A/Q`: NOT_REVALIDATED in this route audit.
- Raw dated country-level download and two overlapping release vintages: NOT_DONE.
- Vintage/revision readiness remains UNKNOWN / NOT_READY.
- No use of BOP_AGG world/group aggregates as substitute for BOP country series.
- Next action: inspect BOP page's official metadata and VIEW DATA/DOWNLOAD target to determine exact dataset version, dimensions and India series keys. If it matches the known Portal BOP dataflow, test one small India series retrieval only, with the provenance sidecar rules; no bulk download until key/schema match.

No CSV, manifest, prior India panel, or production logic was changed. No acceptance gate promoted.

## 28. IMF BOP page identifier and public API access boundary revalidation (2026-11-15)

### Identifier resolved from official page
The official IMF dataset route is:
`https://data.imf.org/en/datasets/IMF.STA:BOP`
The dataset page exposes the API link, VIEW DATA and DOWNLOAD controls, and identifies the dataset as "Balance of Payments (BOP)". The URL's dataset identifier is `IMF.STA:BOP`, matching the dataflow family used in the earlier successful India extraction. This corroborates the dataset identity at the portal-page level; it does not independently expose the full versioned dataflow/DSD contract.

### Public API access boundary
The dataset page's API link resolves to `https://portal.api.imf.org/signin?returnUrl=/apis`. The IMF API documentation says data are served through SDMX 2.1 and SDMX 3.0 APIs and Swagger exploration requires a beta portal account sign-in.
No sign-in, credential use, access-control bypass, or undocumented endpoint probing was attempted.

### Important source-version distinction
- Page-level dataset identifier `IMF.STA:BOP`: CONFIRMED.
- Previously used versioned dataflow `IMF.STA:BOP(21.0.0)` and DSD `IMF.STA:DSD_BOP(24.0.0)`: remain the exact prior extraction contract; the current page itself does not display these version strings in its public page text.
- Therefore this audit does not claim that the current page proves current DSD version or backward compatibility. Existing prior successful extraction artifacts remain the evidence for the earlier versioned contract.

### Gate decision
- Official BOP page-to-dataset identifier: PASS.
- Public API documentation and sign-in requirement: PASS.
- Anonymous direct API schema/metadata discovery: NOT_AVAILABLE via the documented Swagger route.
- Exact versioned DSD revalidation from this page: NOT_ESTABLISHED.
- No new observation retrieval; no revision/vintage evidence; revision readiness remains UNKNOWN / NOT_READY.
- No change to existing India CSV, manifest, or prior accepted extraction/reconciliation evidence.
- Next safe step: rely on the already archived successful raw responses and exact versioned manifest for the prior BOP contract; pursue a public non-authenticated metadata/export resource only if IMF officially exposes one. Do not infer hidden endpoints.

This audit distinguishes the page's unversioned identifier from the versioned dataflow/DSD already used in prior research, preventing an accidental version-mismatch promotion.

## 29. Existing India response provenance sidecar compatibility audit (2026-11-15)

### Audit scope and method
Re-fetched the committed V1 JSON Schema, V1 sidecar specification, India 110-row CSV and companion manifest from the research branch. Parsed the schema and manifest as JSON, checked required schema groups, the four exact series keys, response-hash syntax, positive byte counts, CSV row/column structure, per-series row counts, and availability of the fields required to instantiate a sidecar. No network request or new IMF data pull was made.

### Results
- Schema JSON valid; manifest JSON valid; all seven required top-level schema groups exist.
- Manifest contains four expected series keys; all four response SHA-256 strings are 64 lowercase hex characters; all four response byte counts are positive.
- CSV has 110 data rows and 20 columns; 11/11/44/44 rows by the four expected series; 110 unique series-period keys.
- CSV includes source-response SHA-256 per row; manifest contains raw response byte counts and hashes.
- The archived manifest/CSV do NOT contain actual UTC retrieval timestamps, requested URLs, final URLs, HTTP status, Content-Type, or per-response query parameter objects.
- The manifest contains response byte counts and SHA-256 values but does not contain the exact raw HTTP response body bytes as a sidecar-accessible file in the audited paths. A hash and byte count alone cannot reconstruct or independently validate the raw response body.
- The original CSV also has blank SOURCE, STATUS and ACCESS_SHARING_NOTES fields across the inspected records; these nulls remain preserved and are not retroactively filled.

### Compatibility matrix
- Structural schema validity: PASS.
- Four series identity/key mapping: PASS.
- Existing snapshot's CSV/manifest integrity references: PRESENT (the previous independent integrity run is retained; this audit did not recalculate the SHA-256 of raw HTTP bodies).
- V1 sidecar instance readiness for all four historical responses: REJECTED / NOT_READY due to missing required transport provenance and absence of the exact raw response bytes in the audited archive.
- Vintage status: NOT_VERIFIED / UNKNOWN. Do not label historical responses NOT_EXPOSED_BY_SOURCE because no vintage evidence was inspected at original retrieval time; do not set release_date from audit_date or retrieval date.
- Revision-aware panel eligibility: NOT_READY.

### Corrective boundary
Do not backfill timestamps, URLs, HTTP metadata, query parameters, or raw response bodies from commit dates, run dates, artifact IDs, or memory. Do not create four incomplete/invalid sidecar files. Preserve the existing 110-row CSV, manifest and all original hashes unchanged. The next compliant sidecar can only be created during a new real public HTTP GET that captures the exact response body bytes and transport metadata at acquisition time; if public access is unavailable without sign-in, retain the gate as UNKNOWN/NOT_READY.

This audit is a completed compatibility check, not a revision-history PASS and not a new data acquisition.

## 30. Historical India raw response artifacts recovered; four V1 provenance sidecars created (2026-11-15)

### Recovery breakthrough
The previous bounded audit concluded that the CSV/manifest alone did not carry transport metadata or raw body bytes. Rather than fabricate fields, the original GitHub Actions artifacts were located and downloaded:
- Artifact 14125515371 (run 43623518481): three raw response bodies and per-response JSON capture metadata (annual liabilities, quarterly assets, quarterly liabilities), plus summary.
- Artifact 14122421554 (run 43616059985): annual assets exact `response.body` and `result.json` capture metadata.
These are the original acquisition artifacts, not new IMF pulls.

### Exact raw body verification
For all four series, extracted exact response body bytes from the original workflow ZIP and independently recalculated SHA-256 and byte count. Each matched the original manifest/capture metadata:
- Annual assets: 7,845 bytes; `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`; retrieval 2026-11-14T16:31:30.767933Z.
- Annual liabilities: 7,846 bytes; `6eba68f8779efa5636afea8d4a9de4ce26478c67150144c1e4f128e4f6d3a4e4`; retrieval 2026-11-14T17:53:17.958495Z.
- Quarterly assets: 10,201 bytes; `aff39180e21eec8f71308ac269f9191eb0138b5471808bfa710c6a582be1d24f`; retrieval 2026-11-14T17:53:18.399962Z.
- Quarterly liabilities: 10,185 bytes; `6ebe3c2eabd7f9019ffd80d51e01de359bc1f64aee66c8609877654ad4558ccc`; retrieval 2026-11-14T17:53:18.632136Z.
All four capture records show HTTP 200, SDMX JSON content type, exact requested/final IMF API URLs and series-specific query parameters. Hash scope is the exact response body before parsing/transformation.

### Sidecars created
Four independent V1 JSON sidecars have been committed:
- `data/research/provenance/india_portfolio_assets_usd_annual_2015_2025.provenance.v1.json`
- `data/research/provenance/india_portfolio_liabilities_usd_annual_2015_2025.provenance.v1.json`
- `data/research/provenance/india_portfolio_assets_usd_quarterly_2015_2025.provenance.v1.json`
- `data/research/provenance/india_portfolio_liabilities_usd_quarterly_2015_2025.provenance.v1.json`

Each sidecar preserves actual acquisition UTC time, requested/final URL, GET, exact series key, query parameters, HTTP 200, Content-Type, byte count and verified raw-body SHA-256. Sidecars deliberately use vintage status `NOT_VERIFIED` with null release date/ID: capture metadata does not establish that source vintage was inspected at acquisition. Retrieval time is not a release vintage.

### Acceptance boundary
- Historical raw body recovery: PASS (4/4).
- Exact bytes/hash/byte-count cross-check: PASS (4/4).
- Transport provenance completeness for V1 required fields: PASS (4/4).
- Sidecar creation: PASS (4/4).
- Vintage verification: UNKNOWN / NOT_VERIFIED (not promoted).
- Revision-aware eligibility: NOT_READY pending actual source vintage evidence and at least two independently dated releases overlapping the same series-period keys.
- Existing 110-row CSV and manifest unchanged. No new IMF pull, no synthetic data, no production change, no spend, no PR merge, no gate promotion.

This supersedes only the earlier statement that the audited repository paths did not contain raw bodies: the original workflow artifacts have now been recovered. It does not retroactively create source-vintage evidence.

## 30. Archived raw SDMX vintage-attribute inspection (2026-11-15)

### Scope
Inspected the exact archived raw SDMX-JSON response bodies recovered from the original GitHub Actions artifacts for all four India series:
- `IND.A_NFA_T.P_F.USD.A`
- `IND.L_NIL_T.P_F.USD.A`
- `IND.A_NFA_T.P_F.USD.Q`
- `IND.L_NIL_T.P_F.USD.Q`

The three response bodies in artifact 14125515371 and annual-assets body in artifact 14122421554 were parsed directly from the ZIPs. No new HTTP request or data pull was made. Previously verified response-body byte counts and SHA-256 values were retained.

### Findings
- All four raw SDMX bodies contain `meta: {}`; no release/vintage field is present in the response metadata object.
- The SDMX structure includes dataset-level attributes such as DOI, FULL_DESCRIPTION, PUBLISHER, DEPARTMENT, AUTHOR, CONTACT_POINT, TOPIC_DATASET, KEYWORDS_DATASET, LANGUAGE, PUBLICATION_DATE, UPDATE_DATE, METHODOLOGY_NOTES, source citation and license. It does not define a dedicated vintage/release identifier attribute in the inspected structure.
- Dataset-level attributes include UPDATE_DATE value `2026-11-07T14:56:50.476461500Z` and a second update timestamp `2026-11-07T14:56:50.532906Z` in the captured SDMX dataset attributes. These are dataset-level update metadata, not a per-response release ID or an explicitly documented publication vintage. They must not be promoted to vintage.
- Observation attributes retained in the data are PRECISION, DERIVATION_TYPE, STATUS, ACCESS_SHARING_LEVEL, ACCESS_SHARING_NOTES, SECURITY_CLASSIFICATION and SOURCE. No observation-level vintage/release identifier appears. STATUS, ACCESS_SHARING_NOTES and SOURCE are null in the observations.
- The dataset-level source-methodology text names multiple potential source types, including country authorities, National Summary Data Pages, ECB and IMF Staff Estimates. It does not identify the provenance of each India observation or establish whether an observation is direct-reported versus estimated.
- Dataset citation text refers to a BOP/IIP dataset page and says "Accessed on [current date]"; this is citation boilerplate, not a vintage field.

### Decision
- Raw SDMX vintage-field inspection: COMPLETE for all four archived responses.
- Explicit source-supplied vintage/release identifier: NOT EXPOSED in the inspected raw response structures.
- Dataset-level UPDATE_DATE: observed but NOT_ACCEPTED as a vintage.
- Historical observation release vintage: UNKNOWN; the original capture metadata did not establish a vintage at retrieval time.
- Sidecar vintage status remains `NOT_VERIFIED`, not `NOT_EXPOSED_BY_SOURCE`, because the sidecar status refers to whether vintage evidence was adequately inspected for the original acquisition event; this retrospective inspection does not create a source-supplied per-response vintage.
- Revision-aware panel eligibility remains NOT_READY. One response snapshot per exact series is still insufficient for revision comparison.

### Next action
Seek an independent dated IMF release/archive snapshot that contains the same four exact India series and overlapping reference periods. Compare only after proving both snapshots' exact dataflow/DSD, series keys, release dates/IDs and raw-body hashes. If no second dated snapshot is publicly available, preserve UNKNOWN and keep revision-aware research blocked.

No existing CSV, manifest, sidecar, raw response or accepted gate was modified.
