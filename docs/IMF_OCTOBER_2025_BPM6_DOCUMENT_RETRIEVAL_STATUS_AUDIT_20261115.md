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

## 31. Dated BOPSY 2024 publication snapshot suitability audit (2026-11-15)

### Official dated publication located
Located the official IMF PDF, *Balance of Payments Statistics: Introductory Notes, as of November 2024*:
https://data.imf.org/-/media/iData/External-Storage/Documents/D7E2CE23AF2340EFA7932CF6CD7DD11A/en/BOP-Introductory-Notes-as-of-November-2024.pdf

The document states that the BOPSY electronic release contains individual country data for all available periods and world/regional aggregates for 2005–2023; individual country tables and BOP/IIP metadata are published through the online database. It states the BOPSY data are BPM6-based. The country tables are distinct from the world/regional aggregates, where IMF staff estimates may fill missing country data. India is listed with reporting currency XDC (domestic currency) in Annex IV.

The IMF Committee on BOP Statistics 2024 Annual Report independently states that annual BOP/IIP statistics through 2023 were published in BOPSY 2024, and that 195 economies reported BOP data in that release. This corroborates the existence and period of the dated annual publication, not the contents of India's exact raw series.

### Series mapping context
The November 2024 Introductory Notes standard presentation identifies portfolio investment assets and liabilities separately, and distinguishes equity/investment fund shares and debt securities. The 2024 release documentation therefore confirms the conceptual availability of portfolio assets/liabilities in country tables. It does not expose an archived raw SDMX response, exact `P_F` indicator mapping, exact `A_NFA_T`/`L_NIL_T` keys, or the four India series values in a machine-readable dated snapshot.

### Vintage suitability decision
- Dated BOPSY 2024 official publication/document lineage: PASS.
- India country-table publication availability and reporting currency metadata: PASS at documentation level.
- Raw India country table file or export for BOPSY 2024: NOT_RETRIEVED.
- Exact equivalence to `IMF.STA:BOP(21.0.0)` / `DSD_BOP(24.0.0)` and the four India series keys: NOT_ESTABLISHED.
- A second comparable raw snapshot for the 2015–2025 India series: NOT_ESTABLISHED.
- BOPSY 2024 is NOT accepted as a second vintage for the existing 110-row panel. Do not substitute BOPSY country-table documentation or aggregate values for exact raw series observations.
- Revision/vintage readiness remains UNKNOWN / NOT_READY; revision-aware backtest remains blocked.

### Next action
Use only an officially exposed country-table export/download from the dated BOPSY 2024 release, if the portal exposes it without authentication. Require raw bytes, dated release evidence, exact country and period keys, and a defensible mapping to the existing four series. If the portal only exposes the current live table or aggregate report, stop and preserve NOT_ESTABLISHED. No hidden endpoint guesses or login bypass.

No existing CSV, manifest, sidecar, raw response, or accepted gate changed.

## 32. IMF November 2024 BOP release-calendar evidence and archive-link test (2026-11-15)

### New dated release evidence
The official IMF Data news page "Services Trade Expands at a Faster Pace Than Goods Trade" identifies the Balance of Payments (BOP) dataset and states:
- BOPSY 2024 was published on 20 November 2024.
- Country tables on a BPM6 basis cover 2011–2023; 2005–2010 are available in an archive.
- A separate release titled "Balance of Payments and International Investment Position, Second Quarter 2024" was released on 20 November 2024, and the IMF tracks quarterly BOP/IIP across 190 countries with data starting from 1945.
Official page: https://data.imf.org/en/news/november%2013-

### Link test and limitation
The "Second Quarter 2024" release link on the official page points to an IMF redirect URL on `t.imfconnect.imf.org`. Following that link in this audit timed out before exposing a public document or file target. The page itself supplies release title/date/coverage, but not a downloadable country-level raw file, the India series keys, or a raw response hash.
The official page also confirms the BOPSY 2024 country coverage window but does not provide a dated export file in the page content.

### Decision
- Dated quarterly BOP release event (20 Nov 2024, reference 2024 Q2): PASS as release-calendar evidence.
- BOPSY 2024 country-table coverage statement (BPM6, 2011–2023): PASS as publication-scope evidence.
- Direct quarterly release document/file retrieval: NOT_RETRIEVED (redirect timeout).
- India country raw values / exact four-series mapping in this release: NOT_ESTABLISHED.
- Comparable second snapshot / revision comparison: NOT_ESTABLISHED.
- No vintage promotion: a release-calendar item is not itself a raw snapshot; release date alone does not establish the contents or vintage of the existing 110-row series.
- Revision/vintage readiness remains UNKNOWN / NOT_READY.

### Next action
Do not retry the same timed-out redirect or repeat BOPSY notes discovery. Search for an independently indexed official IMF document or archived public file for the 20 Nov 2024 Q2 release; accept only if raw content, release date, India country series, exact key mapping and overlapping periods can be verified. If none exists, close this public-link avenue as NOT_RETRIEVED and move to a different official archive source, without hidden endpoint guessing.

No CSV, manifest, sidecar, raw response, or accepted gate changed.

## 33. IMF CPIS/PIP adjacent-dataset non-equivalence audit (2026-11-15)

### Candidate identified and tested
IMF search results surface a dedicated dataset, "Portfolio Investment Positions by Counterpart Economy (formerly CPIS)", dataset identifier `IMF.STA:PIP`, with a "Foreign Portfolio Investments Breakdown" dashboard. The dataset description says participating economies report holdings of portfolio investment securities, separately for equity/investment fund shares, long-term debt instruments and short-term debt instruments; frequencies are annual and half-yearly/semester.
Official dataset page: https://data.imf.org/en/Datasets/PIP
Official dashboard catalogue: https://data.imf.org/en/Dashboards

### Why it is not a valid substitute
The existing India panel's four series are BOP financial-account transactions: net acquisition of financial assets (A_NFA_T) and net incurrence of liabilities (L_NIL_T), total portfolio investment (P_F), USD, annual/quarterly. These are flow measures.
The PIP/CPIS dataset is portfolio investment positions/holdings (stocks), organized by counterpart economy and instrument. It is not the same measurement concept, frequency, or series key. A position stock cannot be substituted for a transaction flow or treated as a vintage of the BOP flow panel.
The IMF BOP Introductory Notes explain that the financial account records net acquisition of financial assets and net incurrence of liabilities as transactions, while IIP records external financial assets/liabilities at a point in time; changes in IIP reflect transactions plus revaluations and other volume changes. This distinction prevents stock-flow conflation.

### Decision
- Official adjacent dataset discovered: PASS.
- Exact subject: portfolio investment positions/holdings, not BOP financial-account flows.
- Equivalence to `IND.A_NFA_T.P_F.USD.A/Q` and `IND.L_NIL_T.P_F.USD.A/Q`: REJECTED / NOT_EQUIVALENT.
- Use as cross-check only if a separately defined stock/position research task is approved; never use as second BOP vintage, flow backfill, or revision comparator.
- No change to existing data, series mapping, acceptance gates, or revision/vintage status. BOP revision readiness remains UNKNOWN / NOT_READY.

### Next action
Continue only with an official archived BOP flow country-table/raw response that matches the exact four flow keys. Keep CPIS/PIP out of the current flow pipeline. No hidden endpoint guesses or login bypass.

## 34. RBI official BPM6 quarterly BOP parallel-source contract audit (2026-11-15)

### New primary-source route
The RBI's April 2026 *Comprehensive Guide for Current Statistics of the RBI Monthly Bulletin* (published page 8 Oct 2026) identifies:
- Table 42: Standard Presentation of BoP in India as per BPM6 (US$ million), quarterly, primary source RBI, revision policy "Data are subject to revision".
- Table 43: same standard BPM6 presentation in ₹ crore.
- DBIE mapping: Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector; and Statistics > External Sector > International Trade.
- Table 42 includes financial account functional classification, including Portfolio Investment, and presents credit, debit and net separately. It explicitly distinguishes its BPM6 classification structure from legacy Table 40.
- RBI guide says extended historical time-series underlying Bulletin tables are available through DBIE in reusable formats, and latest periods may be provisional and revised as source updates arrive.
Official guide: https://rbi.org.in/scripts/PublicationsView.aspx?Id=24094
Official DBIE portal: https://data.rbi.org.in

### Relevance and limits
This is a strong independent official India BOP flow source for a parallel-source validation of the IMF India panel. It is BPM6, quarterly, USD, and explicitly revision-prone. It may provide a route to historical release snapshots through dated RBI Bulletins/DBIE time series.
However, the handbook description alone does NOT establish that RBI Table 42 splits portfolio transactions into the exact IMF P_F aggregate with separate A_NFA_T and L_NIL_T observations in the same direction/sign convention, nor does it provide a raw export or release-vintage pair. RBI's Table 40 is a different overall BoP presentation; do not map it as equivalent. Table 44 is IIP positions (stocks), not BOP transaction flows.
No RBI DBIE export was downloaded in this audit.

### Decision
- Official RBI BPM6 quarterly USD BOP source contract: PASS at metadata/documentation level.
- Portfolio investment category in Table 42: PASS at category level.
- Exact IMF four-key equivalence, component direction/sign and period mapping: UNKNOWN / NOT_ESTABLISHED.
- Historical raw export and two dated overlapping snapshots: NOT_DONE.
- RBI source is approved for a bounded parallel-source reconciliation experiment, NOT as an automatic replacement for IMF or a second IMF vintage.
- No values should be merged until the exact series mapping, units, signs, frequency and release/vintage metadata are validated.

### Next action
Inspect RBI DBIE Table 42's actual downloadable time series and at least two dated RBI Bulletin releases for an overlapping quarter. First perform a small schema-only/table-header inspection. Compare exact portfolio assets and liabilities only if both sides are independently represented and signs/credit-debit conventions can be mapped. Keep source-native series and release snapshots separate.

No IMF CSV, manifest, sidecar, raw response, or accepted gate changed.


## 2026-11-15 — RBI Table 42 live publication snapshots and DBIE export-boundary audit

### Official table and observed structure
- Re-opened the official RBI Table 42 publication (not the earlier handbook-only audit): Table 42 is titled "Standard Presentation of BoP in India as per BPM6 (US $ Million)" and displays quarterly periods, USD million, Credit/Debit/Net columns.
- The RBI publication's Financial Account explicitly separates: 3.2 Portfolio Investment; 3.2.A Portfolio Investment in India; 3.2.1 Equity and investment fund shares; 3.2.2 Debt securities; and 3.2.B Portfolio Investment by India. This confirms portfolio flow components are present in the actual published table, not only in the guide metadata.
- The DBIE table URL surfaced by public search resolves to a dataset titled "Standard presentation of India's balance of payments as per BPM6 - US dollars" but its displayed metadata says Annual, period 31-03-2012–31-03-2026, 91 rows. This is not accepted as Table 42's quarterly export: frequency conflicts with the RBI guide's Table 42 quarterly contract. The public page's CSV/JSON affordance was identified, but no raw export bytes/schema were downloaded in this bounded audit.

### Two dated bulletin snapshot comparison
- 22 Jul 2026 RBI Bulletin (Table 42) shows Jan–Mar 2025 and Jan–Mar 2026 (P); 25 Sep 2026 and 23 Oct 2026 bulletins show Apr–Jun 2025 and Apr–Jun 2026 (P).
- For the overlapping Apr–Jun 2025 quarter, 25 Sep and 23 Oct 2026 publications report identical values at the displayed US$ million precision:
  - Portfolio Investment total: Credit 146,339; Debit 144,731; Net 1,608.
  - Portfolio Investment in India: Credit 145,201; Debit 142,720; Net 2,481.
  - Portfolio Investment by India: Credit 1,138; Debit 2,011; Net −872 (published rounded components do not necessarily add exactly due to rounding).
  - Equity and investment fund shares: Credit 123,636; Debit 118,245; Net 5,391.
  - Debt securities: Credit 21,565; Debit 24,475; Net −2,910.
- Result: two dated public bulletin snapshots for the same reference quarter are available and agree at displayed precision. This is a repeat-publication consistency check, NOT evidence of a revision event or of unchanged source data between releases; no difference was observed in this pair. The two pages are not raw API response snapshots and their full publication payload hashes were not captured.
- July 22 2026 provides another dated table and an earlier reference quarter (Jan–Mar 2025), but it is not the same quarter as the September/October pair and is not used to infer revision.

### Mapping and gate decision
- Actual RBI Table 42 schema-level view: PASS (quarter, USD million, Credit/Debit/Net, portfolio categories and subcategories visibly present).
- Two dated overlapping RBI bulletin pages: PASS (25 Sep and 23 Oct 2026, Apr–Jun 2025); displayed values match for the rows above.
- DBIE downloadable raw export/schema for quarterly Table 42: NOT_RETRIEVED; surfaced DBIE page is annual and therefore not accepted as the quarterly export.
- Exact mapping to IMF P_F / A_NFA_T / L_NIL_T remains UNKNOWN / NOT_ESTABLISHED. In particular, do not equate RBI "Portfolio Investment in India/by India" or Credit/Debit directly with IMF net acquisition of financial assets/liabilities without an official sign/direction crosswalk. Credit/debit/net columns are not themselves proof of the IMF assets/liabilities direction.
- No IMF vintage evidence is added; RBI releases are an independent source lineage, not an IMF second vintage. No source merge, sign conversion, CSV creation, or production integration.

### Next action
Retrieve the actual quarterly DBIE Table 42 series through an officially exposed quarterly publication/time-series route, inspect raw CSV/JSON headers and notes, then locate a documented RBI-to-BPM6 financial-account assets/liabilities sign crosswalk. Only after that, capture two dated raw exports for the same quarter and hash exact bytes. Do not use the annual DBIE dataset or infer mapping from labels.

Sources inspected:
- RBI Table 42, 25 Sep 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495
- RBI Table 42, 23 Oct 2026: https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566
- RBI Table 42, 22 Jul 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352
- DBIE surfaced dataset: https://dbie.rbihub.in/tables?table=external_sector.r814_standard_presentation_of_india_s_balance_of_payments_as_pe

Bounded audit progress: 100% of this defined inspection complete. RBI parallel-source raw export/mapping readiness: NOT_READY. IMF BOP workstream remains 5/7 = 71.4%; October 2025 IMF PDF package remains 25%; full V11.3 project progress remains NOT_CALCULABLE.

No paid services, credentials, external contact, synthetic data, CSV/manifest/sidecar mutation, PR merge, or production change.

## 2026-11-15 — RBI Table 42 to IMF BPM6 financial-account direction/sign crosswalk audit

### Official evidence newly checked
- Re-inspected RBI's April 2026 Comprehensive Guide for Current Statistics and its Table 42 contract: quarterly, US$ million, BPM6 classification, financial account by functional classification, credit/debit/net presentation, residence principle, subject to revision.
- Inspected actual RBI Bulletin Table 42 values for Apr–Jun 2025: Portfolio Investment total (Credit 146339, Debit 144731, Net 1608); Portfolio Investment in India (145201, 142720, 2481); Portfolio Investment by India (1138, 2011, −872); equity/fund shares and debt securities are separately shown beneath Portfolio Investment in India.
- RBI's official Balance of Payments Manual for India explains that portfolio investment "in India" includes nonresident investment into India and separately identifies India's portfolio investment abroad. This supports a directional interpretation: "in India" relates to nonresident claims on Indian residents (liability-side economic direction); "by India" relates to resident holdings/claims abroad (asset-side economic direction). This is a conceptual direction clue, not an approved numerical crosswalk to IMF A_NFA_T/L_NIL_T observations.
- IMF BPM6 Compilation Guide and IMF BOPCOM sign-convention note state financial-account flows are recorded net separately for assets and liabilities: positive means net increase, negative means net decrease; financial-account balance is assets minus liabilities. This is not the same as treating a published Credit-minus-Debit net column as either an asset or liability series without a bridge.

### Critical mismatch / mapping decision
- RBI Table 42 publishes Credit, Debit and Net (= credit less debit) for the relevant functional categories. IMF A_NFA_T and L_NIL_T represent net acquisition of financial assets and net incurrence of liabilities, each signed by increase/decrease.
- RBI labels provide a plausible direction partition ("by India" ↔ asset direction; "in India" ↔ liability direction), but available official Table 42 guide/manual material does not provide an explicit equation mapping its Credit/Debit/Net columns to the IMF net-acquisition/net-incurrence series. The two net conventions must not be equated by assumption.
- RBI Table 42 total portfolio category and its India/by-India split are present. However the observed sub-breakdown (equity/debt) is shown under Portfolio Investment in India; the inspected page does not establish a matching equity/debt split under Portfolio Investment by India. Scope symmetry with IMF P_F aggregate is therefore not established.
- The old RBI manual's portfolio investment definitions are useful for residency/direction interpretation, but do not substitute for a current machine-readable sign-conversion rule or exact mapping of IMF indicator P_F.

### Status
- RBI Table 42 portfolio functional-category and directional-label inspection: PASS.
- Conceptual India-vs-abroad direction interpretation: PARTIAL (not a series-level mapping).
- Exact RBI Credit/Debit/Net → IMF A_NFA_T/L_NIL_T signed-flow crosswalk: NOT_ESTABLISHED / UNKNOWN.
- Matching P_F scope and symmetrical instrument coverage: NOT_ESTABLISHED.
- DBIE quarterly raw export and schema: NOT_RETRIEVED (previous annual dataset rejected as wrong frequency).
- Decision: DO NOT map, sign-flip, merge or use RBI Table 42 values as IMF A_NFA_T/L_NIL_T. Keep RBI as separate parallel source. No new acceptance-gate promotion.

### Next safe action
Obtain an official RBI technical note or raw quarterly DBIE schema that explicitly defines the financial-account Credit/Debit columns and the assets/liabilities mapping. In parallel, inspect the RBI Table 42 quarterly time-series publication route for raw headers and any direction flags. If no explicit bridge is exposed, record the crosswalk as NOT_ESTABLISHED and keep sources separate.

Official sources:
- RBI current statistics guide: https://www.rbi.org.in/scripts/PublicationsView.aspx?Id=24094
- RBI Table 42 bulletin, 25 Sep 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495
- RBI Balance of Payments Manual for India: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013
- IMF BPM6 Compilation Guide: https://data.imf.org/-/media/iData/External-Storage/Documents/FB1F86C7158646DDB554D0882F1F2A3B/en/3-BPM6-com-guide.pdf
- IMF BOPCOM sign convention note: https://www.imf.org/external/pubs/ft/bop/2013/13-13.pdf

Bounded crosswalk audit: 100% complete. Mapping gate remains NOT_ESTABLISHED; RBI raw quarterly export remains NOT_RETRIEVED; IMF BOP workstream 5/7=71.4%; October 2025 IMF PDF package 25%; overall V11.3 progress NOT_CALCULABLE.

No paid sources, credentials, synthetic data, fabricated mapping, data-file mutation, PR merge or production change.

## 2026-11-15 — CORRECTION: official RBI BPM6 sign-convention crosswalk recovered

This section supersedes the immediately preceding crosswalk audit's statement that no official RBI sign-conversion rule was located. A targeted search of RBI's official *Balance of Payments Manual for India* and the official Working Group report located the missing convention.

### Exact official rule
- RBI Manual, paragraphs 1.16 and 1.19 (official 2010 manual): for assets, a positive credit figure represents a decrease in assets and a negative debit figure represents an increase in assets; for liabilities, a positive credit figure represents an increase in liabilities and a negative debit figure represents a decrease in liabilities. Financial-account components are recorded net, separately for each asset or liability category; positive change means decrease in assets or increase in liabilities, and negative change means increase in assets or decrease in liabilities.
- RBI Working Group report further states that netting is done within the same asset or liability type; changes in financial assets are not netted against changes in liabilities (except possible financial-derivative treatment).
- Current RBI April 2026 guide confirms Table 42 is quarterly, USD million, BPM6, financial account by functional classification, with Credit/Debit/Net columns and residence principle. It does not restate the detailed sign equation, so the sign equation is sourced from the official RBI Manual, not inferred from Table 42 labels.
  
### Conditional mathematical crosswalk (same portfolio functional category, same period, same USD unit)
Let RBI Net = Credit − Debit, using the RBI Manual's financial-account sign convention:
- IMF-style net acquisition of financial assets = − (RBI net change on the asset side).
- IMF-style net incurrence of liabilities = + (RBI net change on the liability side).
Thus, if RBI Table 42 exposes separate net portfolio asset and liability observations at the same aggregation level, the candidate mapping is:
  - Assets: IMF A_NFA_T candidate = Debit − Credit = −Net.
  - Liabilities: IMF L_NIL_T candidate = Credit − Debit = +Net.
This is a sign-convention bridge, not yet an approved data-series crosswalk. It must be applied only to separate asset-side/liability-side net observations, never to a combined portfolio net balance. The direction must be assigned from the RBI table's explicit asset/liability row labels or an official definition; do not assign it from "in India/by India" labels alone without confirming the table's row definitions.

### Remaining validation before numeric use
- Exact RBI Table 42 portfolio row split into asset-side and liability-side values at the same total P_F scope: NOT_YET_VERIFIED from raw export.
- Raw quarterly DBIE Table 42 export, column headers, row labels and metadata: NOT_RETRIEVED.
- Exact matching coverage/instrument aggregation to IMF P_F: NOT_ESTABLISHED.
- Two dated raw RBI export snapshots and release/vintage metadata: NOT_RETRIEVED. Previously inspected bulletin pages are human-readable publication snapshots, not raw data-file vintage evidence.
- Therefore the sign-convention formula is now documented, but no numeric RBI-to-IMF series has been created, merged or promoted. The IMF vintage gate remains unaffected.

### Revised status
- Official RBI sign-convention rule located: PASS.
- Conditional assets/liabilities sign bridge: PASS (methodology-level only).
- Exact Table 42 row mapping and P_F scope equivalence: NOT_ESTABLISHED.
- Quarterly raw export and dated raw snapshots: NOT_RETRIEVED.
- RBI parallel-source readiness: NOT_READY pending data-level mapping and raw snapshot validation.

Sources:
- RBI Balance of Payments Manual for India, especially paragraphs 1.16 and 1.19: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013
- RBI Working Group report, sign convention and netting within same asset/liability type: https://www.rbi.org.in/scripts/PublicationReportDetails.aspx?ID=596
- RBI April 2026 Current Statistics Guide, Table 42: https://www.rbi.org.in/scripts/PublicationsView.aspx?Id=24094

Bounded sign-convention recovery task: 100% complete. IMF BOP workstream remains 5/7=71.4%; October 2025 IMF PDF package 25%; overall V11.3 project progress NOT_CALCULABLE. No data mutation, synthetic values, paid source, credentials, PR merge or production change.

## 2026-11-15 — RBI Table 42 vs archived IMF India P_F single-quarter numerical reconciliation (2025-Q2)

### Method and exact source keys
- Used official RBI Table 42 for Apr–Jun 2025 (quarter 2025-Q2), USD million, Credit/Debit/Net; compared with the already archived IMF India quarterly observations in the existing committed CSV. No new IMF API pull and no data-file modification.
- IMF exact keys: IND / A_NFA_T / P_F / USD / Q / 2025-Q2 and IND / L_NIL_T / P_F / USD / Q / 2025-Q2. Existing CSV values are in USD units with SCALE=6; converted only for display/comparison by dividing raw OBS_VALUE by 10^6 (metadata scale interpretation already present in the extraction contract).
- RBI Table 42 rows for same quarter:
  - 3.2.A Portfolio Investment in India: Credit 145201, Debit 142720, Net +2481 (USD million) → RBI manual says liability-side credit increases liabilities and debit reduces liabilities; net incurrence candidate +2481.
  - 3.2.B Portfolio Investment by India: Credit 1138, Debit 2011, Net −872 (USD million) → RBI manual says asset-side credit reduces assets and debit increases assets; net acquisition candidate −(Net) = +872.
- RBI total row 3.2 Portfolio Investment Net +1608 is not used as either asset or liability; it is the combined net balance and must not be mapped to one IMF side.

### Numerical comparison
- IMF A_NFA_T / P_F / 2025-Q2 raw OBS_VALUE 872453921.9430683; SCALE=6 → USD million 872.4539219430683.
- RBI asset-side candidate (Portfolio Investment by India) = +872 USD million from displayed Net −872.
- Absolute difference = 0.4539219431 USD million, within ±0.5 USD million display-rounding interval.
- IMF L_NIL_T / P_F / 2025-Q2 raw OBS_VALUE 2480700911.919279; SCALE=6 → USD million 2480.700911919279.
- RBI liability-side candidate (Portfolio Investment in India) = +2481 USD million.
- Absolute difference = 0.2990880807 USD million, within ±0.5 USD million display-rounding interval.
- Both independent side comparisons fall within the rounding interval of RBI's whole-million published values. This is a strong single-quarter numerical consistency result, not proof of complete series equivalence or revision/vintage status.

### Validation boundary
- Official RBI sign rule, directional labels, exact quarter and currency, archived IMF exact series keys, and both rounded numeric comparisons align in this one test.
- RBI Table 42 published page itself is the source for values, not a raw quarterly DBIE CSV export. DBIE raw export/schema remains NOT_RETRIEVED.
- One quarter only; multi-quarter independent replication NOT_DONE.
- IMF raw series capture still lacks a verified release vintage; RBI bulletin date pair does not create an IMF vintage. Revision-aware gate remains NOT_READY.
- Decision: single-quarter parallel-source numerical check PASS_WITH_ROUNDING for both sides. Conditional sign/direction mapping validated for this quarter only. Do not merge RBI values into IMF panel, do not overwrite IMF data, do not promote revision/vintage gate, and do not generalize across the entire 2015–2025 panel.

### Next action
Repeat the same two-sided check for three additional non-adjacent quarters already in the archived IMF quarterly series and find corresponding dated RBI Table 42 bulletins. Use the same exact rule and tolerance ±0.5 USD million only when RBI displays whole USD millions. If any quarter fails, investigate period definition, revision status and coverage; do not widen tolerance.

Sources:
- RBI Table 42, 25 Sep 2026, 2025-Q2: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495
- RBI Table 42, 23 Oct 2026, 2025-Q2: https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566
- RBI Manual, paragraphs 1.15–1.16 and 5.20, portfolio investment 5.63–5.68: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013
- IMF archived data CSV (existing repo path): data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv

Bounded 2025-Q2 two-sided reconciliation: 100% complete. Result PASS_WITH_ROUNDING (2/2). DBIE quarterly raw export NOT_RETRIEVED; multi-quarter replication NOT_DONE; IMF revision/vintage readiness NOT_READY; IMF BOP workstream 5/7=71.4%; October 2025 IMF PDF package 25%; full V11.3 progress NOT_CALCULABLE.

No new data acquisition, data/manifest/sidecar mutation, synthetic values, paid source, credentials, PR merge or production change.

## 2026-11-15 — Three additional RBI Table 42 vs archived IMF P_F quarterly reconciliations

### Test design
- Extended the prior single-quarter 2025-Q2 comparison to three additional, non-adjacent quarter periods: 2024-Q3, 2024-Q4 and 2025-Q1.
- RBI official Table 42 sources: 20 Feb 2026 (Jul-Sep 2024), 23 Apr 2026 (Oct-Dec 2024), and 22 Jul 2026 (Jan-Mar 2025). All are Table 42, BPM6, USD million, Credit/Debit/Net.
- IMF values were read from the already committed 110-row CSV data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv, exact keys IND/A_NFA_T/P_F/USD/Q and IND/L_NIL_T/P_F/USD/Q. No new IMF API call and no source data modification.
- Applied the official RBI Manual sign bridge: asset-side candidate = −(RBI Portfolio Investment by India Net); liability-side candidate = RBI Portfolio Investment in India Net. Comparison tolerance ±0.5 USD million because RBI Table 42 publishes whole USD millions.

### Results (USD million)
| Quarter | RBI asset candidate | IMF A_NFA_T | abs diff | RBI liability candidate | IMF L_NIL_T | abs diff |
|---|---:|---:|---:|---:|---:|---:|
| 2024-Q3 | −35 | −34.990038547 | 0.009961453 | 19,815 | 19,815.071031982 | 0.071031982 |
| 2024-Q4 | −63 | −62.610017414 | 0.389982586 | −11,435 | −11,434.646504149 | 0.353495851 |
| 2025-Q1 | −136 | −135.999310934 | 0.000689065 | −5,995 | −5,994.630947245 | 0.369052755 |

- All six side-by-quarter comparisons fall within ±0.5 USD million. Result: 6/6 PASS_WITH_ROUNDING.
- Together with the earlier 2025-Q2 test, cumulative cross-check is 4 quarters × 2 sides = 8/8 PASS_WITH_ROUNDING.
- 2025-Q2 prior test remains: assets diff 0.453921943; liabilities diff 0.299088081 USD million.

### Interpretation and strict boundary
- This is now repeated numerical support across four quarter periods, with correct direction/sign and rounded public values.
- The compared IMF series are A_NFA_T and L_NIL_T, indicator P_F; RBI rows are Portfolio Investment by India and Portfolio Investment in India. Numerical agreement is strong evidence of a consistent aggregate mapping for the tested quarters.
- Still not a full 2015–2025 equivalence proof: only four quarters tested; RBI raw quarterly DBIE export/schema not retrieved; RBI public bulletin tables are whole-million displayed values; no independent raw RBI export bytes or hashes; IMF response vintage remains unverified. Do not merge RBI values into the IMF panel or claim revision-ready/vintage-complete.
- No tolerance widening; all tests used the predeclared ±0.5 USD million display-rounding interval.

### Next action
Run a full-period 2015–2025 quarterly spot-check matrix (prefer one quarter per year, with exact RBI Bulletin pages and archived IMF values) before considering a research-only source mapping note. Keep raw-source capture and vintage checks separate. If any quarter fails, stop and investigate; do not widen tolerance.

Sources:
- RBI Table 42, 20 Feb 2026, Jul-Sep 2024: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24025
- RBI Table 42, 23 Apr 2026, Oct-Dec 2024: https://www.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24156
- RBI Table 42, 22 Jul 2026, Jan-Mar 2025: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352
- Prior RBI Table 42, 25 Sep 2026, Apr-Jun 2025: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495
- RBI BOP Manual: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013
- Archived IMF CSV: data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv

Bounded three-quarter extension: 100% complete. Cumulative four-quarter numerical validation: 8/8 PASS_WITH_ROUNDING. Full-period mapping validation: NOT_DONE. RBI quarterly raw export/schema: NOT_RETRIEVED. IMF revision/vintage readiness: NOT_READY. IMF BOP workstream remains 5/7=71.4%; October 2025 IMF PDF package 25%; overall V11.3 project progress NOT_CALCULABLE.

No new IMF data pull, RBI raw-file creation, source-data mutation, manifest/sidecar mutation, synthetic data, paid service, credentials, PR merge or production change.


## Historical RBI BPM6 quarterly cross-check extension — 2016–2017 (2026-11-15)

Scope: two non-overlapping historical fiscal-year quarters identified from RBI's official bulletin archive. The 2016 and 2017 observations are calendar-quarter Q2 (Apr–Jun), matched to IMF CSV periods 2016-Q2 and 2017-Q2. This is the earlier historical Standard Presentation of BoP in India as per BPM6 (RBI Table 40 in the October 2017 bulletin), not mislabeled as current Table 42.

Source: RBI Bulletin dated 10 October 2017, official URL https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=17190 . It reports (US$ million):
- Apr–Jun 2016 (PR): Portfolio Investment in India net +1,241; Portfolio Investment by India net +863.
- Apr–Jun 2017 (P): Portfolio Investment in India net +11,921; Portfolio Investment by India net +530.

Mapping retained from the signed-convention audit:
- RBI Portfolio Investment by India Net -> IMF asset net acquisition = negative RBI net.
- RBI Portfolio Investment in India Net -> IMF liability net incurrence = positive RBI net.

Comparisons against the existing archived IMF quarterly CSV (USD million; raw OBS_VALUE divided by SCALE=10^6):
| Period | RBI asset comparator | IMF asset | abs diff | RBI liability comparator | IMF liability | abs diff | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2016-Q2 | -863 | -862.901610612507 | 0.098389387493 | 1241 | 1240.54 | 0.46 | PASS_WITH_ROUNDING |
| 2017-Q2 | -530 | -530.439269462386 | 0.439269462386 | 11921 | 11921.16 | 0.16 | PASS_WITH_ROUNDING |

Acceptance rule remains absolute difference <= 0.5 USD million; no tolerance widening. Result: 4/4 side-by-side comparisons PASS_WITH_ROUNDING. RBI bulletin is rounded to whole USD million, while IMF retains sub-million precision.

Evidence limitations:
- This is a two-year historical extension only, not a completed 2015–2025 matrix.
- RBI archive search surfaced this October 2017 USD-million BPM6 table; older or other-year pages with different units/table numbers are not silently converted or promoted.
- No raw RBI CSV/DBIE export, raw export hash, or vintage metadata was obtained.
- IMF CSV is unchanged; no rows were added or modified. No source promotion, no data merge, and no revision-vintage conclusion.
- The earlier four quarters (2024-Q3, 2024-Q4, 2025-Q1, 2025-Q2) remain 8/8 PASS_WITH_ROUNDING. Combined directly observed checks now cover six quarters and 12/12 side comparisons, but are not a statistically representative full-period validation.

Progress:
- This bounded historical extension (2016–2017): 100% complete.
- Requested 2015–2025 annual spot-check matrix: 2/11 years covered = 18.2%; 9/11 years remain NOT_DONE.
- RBI quarterly raw DBIE export: NOT_RETRIEVED.
- IMF revision/vintage: NOT_READY / NOT_VERIFIED.
- IMF BOP workstream remains 5/7 = 71.4%; this extension does not change that gate count.
- Overall PRECISION-WIRES V11.3 project progress remains NOT_CALCULABLE pending reconciled denominators and approved weights.

Integrity: no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, source CSV, manifests, or historical artifacts.


## RBI BPM6 annual spot-check expansion — 2018–2023 (2026-11-15)

Method: use one calendar Q2 observation per year (Apr–Jun), compare RBI's published whole USD-million Portfolio Investment Net figures with the existing archived IMF quarterly CSV. Mapping and acceptance rule unchanged: RBI "Portfolio Investment by India" net is negated for IMF asset net acquisition; RBI "Portfolio Investment in India" net is used as IMF liability net incurrence; absolute difference <=0.5 USD million.

Official RBI sources and values:
- 2018-Q2: RBI Table 198 in official publication dated 18 Sep 2020, https://www.rbi.org.in/scripts/PublicationsView.aspx?id=19931. Portfolio Investment in India net -9,106; by India net +961.
- 2019-Q2 and 2020-Q2: RBI Bulletin dated 12 Oct 2020, Table 40, https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=19879. In India net +5,156 / +1,098; by India net -314 / -456.
- 2022-Q2 and 2023-Q2: RBI Bulletin dated 19 Oct 2023, Table 40, https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=22169. In India net -14,659 / +16,089; by India net +29 / -358.
- 2021-Q2: no exact official USD-million BPM6 row located in this bounded search; NOT_RETRIEVED, not inferred.

IMF CSV comparisons (USD million; raw OBS_VALUE / 10^6):
| Period | RBI asset comparator | IMF asset | abs diff | RBI liability comparator | IMF liability | abs diff | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2018-Q2 | -961 | -960.621114404864 | 0.378885595136 | -9106 | -9105.960000000043 | 0.039999999957 | PASS_WITH_ROUNDING |
| 2019-Q2 | +314 | +313.590331450881 | 0.409668549119 | +5156 | +5156.281990468391 | 0.281990468391 | PASS_WITH_ROUNDING |
| 2020-Q2 | +456 | +455.928583274424 | 0.071416725576 | +1098 | +1097.593483845092 | 0.406516154908 | PASS_WITH_ROUNDING |
| 2022-Q2 | -29 | -28.778465336278 | 0.221534663722 | -14659 | -14658.870488236891 | 0.129511763109 | PASS_WITH_ROUNDING |
| 2023-Q2 | +358 | +358.405859195828 | 0.405859195828 | +16089 | +16089.227782268420 | 0.227782268420 | PASS_WITH_ROUNDING |

Outcome: 10/10 additional side comparisons PASS_WITH_ROUNDING; no mismatch and no tolerance widening. The historical RBI source publication labels differ by year (Table 198/40); all rows above are explicitly identified as BPM6 standard presentation in USD million. 2021 remains an evidence gap.

Cumulative status:
- 2016–2017 extension: 4/4 PASS_WITH_ROUNDING.
- 2018, 2019, 2020, 2022, 2023 extension: 10/10 PASS_WITH_ROUNDING.
- Four 2024–2025 quarters from prior audit: 8/8 PASS_WITH_ROUNDING.
- Total directly checked: 11 quarters, 22/22 side comparisons PASS_WITH_ROUNDING.
- Annual coverage of 2015–2025 matrix: 7/11 years = 63.6% (2016, 2017, 2018, 2019, 2020, 2022, 2023); 2015, 2021, 2024, 2025 are not counted in this annual-Q2 matrix. Note: 2024–25 have separate quarter checks but do not replace the defined annual Q2 sampling design.
- 2021 Q2 source: NOT_RETRIEVED.
- RBI raw quarterly DBIE export: NOT_RETRIEVED; IMF vintage: NOT_READY / NOT_VERIFIED.
- IMF BOP workstream remains 5/7 = 71.4%; overall V11.3 project progress remains NOT_CALCULABLE.
- IMF CSV unchanged; no raw source export, manifest, sidecar or production artefact modified. No source promotion or full-period equivalence claim.


## Targeted RBI archive retrieval audit — unresolved Q2 gaps (2026-11-15)

Scope: targeted retrieval for the two unfilled annual-Q2 sample periods 2015-Q2 and 2021-Q2. This is a source-discovery audit only; no numerical comparison is claimed where the exact RBI observation was not retrieved.

Verified official archive evidence:
- RBI June 2021 bulletin archive page lists Table 40, "Standard Presentation of BoP in India as per BPM6 (US $ Million)", but the page is the June 2021 bulletin and its table is not the Apr-Jun 2021 reporting period: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?mon=6&yr=2021
- RBI Aug 17 2021 bulletin (Id=20483) Table 40 contains Jan-Mar 2020 and Jan-Mar 2021, not Apr-Jun 2021: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=20483
- RBI June 16 2022 bulletin (Id=21114) Table 40 contains Oct-Dec 2020 and Oct-Dec 2021, not Apr-Jun 2021: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=21114
- RBI March 17 2022 bulletin (Id=20916) contains Jul-Sep 2020 and Jul-Sep 2021, not Apr-Jun 2021: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=20916
- RBI search also surfaced 2021-22 and 2022-23 annual BPM6 USD-million publications, but annual observations are not substitutes for quarterly Q2 rows.
- Searches for exact Apr-Jun 2021 RBI Table 40 row and Apr-Jun 2015 USD-million BPM6 quarterly row did not surface a source page with the required Portfolio Investment in India and Portfolio Investment by India net values.

Decision:
- 2021-Q2 RBI quarterly comparator: NOT_RETRIEVED. Do not derive it from annual values, adjacent quarters, DBIE values of unknown frequency, or FPI flow datasets.
- 2015-Q2 RBI quarterly comparator: NOT_RETRIEVED. The surfaced Feb 2016 archive pages show Jul-Sep 2014 and Jul-Sep 2015, not Apr-Jun 2015; no quarterly comparator accepted.
- No numeric PASS/FAIL result added. Existing IMF CSV remains unchanged; no interpolation, synthetic data, or sign/tolerance changes.

Progress:
- Targeted retrieval audit for these two gaps: 100% complete as a bounded search; outcome is unresolved source availability, not validation PASS.
- Annual Q2 matrix remains 7/11 years = 63.6%; 2015 and 2021 remain NOT_RETRIEVED; 2024 and 2025 remain outside the annual-Q2 sampling design despite separate quarter checks.
- Existing directly checked comparisons remain 11 quarters, 22/22 PASS_WITH_ROUNDING.
- IMF BOP workstream remains 5/7 = 71.4%; IMF vintage NOT_READY / NOT_VERIFIED; RBI raw quarterly DBIE export NOT_RETRIEVED; whole V11.3 project NOT_CALCULABLE.

No production logic, CSV, manifest, sidecar, prior PASS artefact, or gate was changed.


## RBI DBIE source-contract and export-path verification (2026-11-15)

New primary documentation reviewed: RBI, Comprehensive Guide for Current Statistics of the RBI Monthly Bulletin, April 2026 edition, published on RBI site 08 Oct 2026:
https://www.rbi.org.in/scriptS/PublicationsView.aspx?id=24094

Verified from the guide:
- Table 42 is explicitly "Standard Presentation of BoP in India as per BPM6 (US$ million)".
- Reference period: Quarterly; unit: US$ million; source department DEPR; primary source RBI; revision policy: data subject to revision.
- Official DBIE mapping is DBIE > Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector, and DBIE > Statistics > External Sector > International Trade.
- Table 42 coverage includes financial account portfolio investment, separate assets/liabilities totals, and credit/debit/net presentation.
- Table 43 is the ₹ crore BPM6 counterpart; Table 40 is the older overall BoP classification and is not the Table 42 substitute.
- The guide says historical time series underlying Bulletin tables are available through DBIE, with quarterly BoP frequency. It also says Bulletin tables are generated from CIMS and aligned with underlying DBIE time-series data.
- RBI's public DBIE export guide says preformatted reports can be accessed under Statistics > Sector > Sub Sector > Required Report or Publication > Required publication > Required Report/Search Option; available report data can be exported as Excel, PDF, Text or CSV through "Export Document as".

Access test:
- Opened the official DBIE root via RBI guide link (https://data.rbi.org.in/); public page extraction returned no readable lines. No login, credentials, bypass, hidden endpoint, or direct undocumented API used.
- The exact Table 42 historical quarterly series export, schema, and CSV bytes were not retrievable through the public page extraction in this run.
- The previously surfaced DBIE dataset page (dataset path external_sector.r814_standard_presentation_of_india_s_balance_of_payments_as_pe) described Annual frequency and therefore remains rejected as the quarterly Table 42 export; it must not be repurposed.
- Consequently 2015-Q2 and 2021-Q2 RBI comparators remain NOT_RETRIEVED. No numeric comparison or PASS/FAIL result is added.

Decision and next actionable route:
- Source contract and official navigation/export path are now VERIFIED; raw quarterly export remains NOT_RETRIEVED.
- Next retrieval should use the documented DBIE UI path and locate the quarterly USD Table 42 report/series, then export CSV and preserve the unmodified bytes, retrieval timestamp, displayed frequency/unit, and SHA-256. If DBIE requires login or blocks export, stop and retain NOT_RETRIEVED; do not use undocumented endpoints.
- Existing 11-quarter / 22-of-22 PASS_WITH_ROUNDING results remain unchanged.
- IMF BOP workstream remains 5/7 = 71.4%; IMF vintage NOT_READY / NOT_VERIFIED; overall V11.3 NOT_CALCULABLE.
- No CSV, manifest, sidecar, production code, or prior PASS artefact changed.


## DBIE public-access execution checkpoint (2026-11-15)

Objective: execute the documented RBI DBIE UI path for the quarterly Table 42 time-series export, without undocumented APIs or credentialed access.

Freshly revalidated RBI guide:
- Official April 2026 Comprehensive Guide (published 08 Oct 2026): https://rbi.org.in/scripts/PublicationsView.aspx?Id=24094
- Table 42 is explicitly quarterly, US$ million, DEPR/RBI, subject to revision; DBIE mapping is Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector, and Statistics > External Sector > International Trade.
- Guide states DBIE contains extended historical time series and tables align with the CIMS repository.
- RBI public DBIE export instructions: https://dbieold.rbi.org.in/DBIE/doc/Exporting_report_data_%26_related_options.pdf . Preformatted reports can be accessed through Statistics > Sector > Sub Sector > Required Report or Publication > Required publication > Required Report/Search Option; export supports Excel, PDF, Text and CSV.

Execution result:
- Opened official DBIE root https://data.rbi.org.in/ through available public page retrieval. The page returned no readable content or navigable report controls.
- The old DBIE root timed out in the public retrieval interface. The export-instructions PDF is readable, but it documents UI actions rather than providing a data file.
- No exact Table 42 quarterly report URL, report identifier, export bytes, or schema was exposed by the accessible public pages in this execution.
- Therefore no CSV was downloaded, no SHA-256 can be computed, and 2015-Q2 / 2021-Q2 RBI comparator values remain NOT_RETRIEVED.
- This is a tooling/access boundary, not evidence that RBI data do not exist. No credentials, login, undocumented endpoint, scraping workaround, or external contact used. RBI guide lists dbie@rbi.org.in for queries; no message sent, as external contact requires user approval.

Bounded task status:
- Public-path execution attempt: 100% complete; outcome BLOCKED at interactive DBIE report access.
- Raw quarterly CSV/export: 0% acquired / NOT_RETRIEVED.
- 2015-Q2 and 2021-Q2: NOT_RETRIEVED; no numeric comparisons claimed.
- Existing 11-quarter / 22/22 PASS_WITH_ROUNDING results unchanged.
- IMF BOP workstream remains 5/7 = 71.4%; IMF vintage NOT_READY / NOT_VERIFIED; overall PRECISION-WIRES V11.3 NOT_CALCULABLE.
- No source CSV, manifest, sidecar, prior PASS artifact, production code, selector, ranking score, pressure fade, diagnostic or gate changed.

Next dependency: user-authorized interactive access to the RBI DBIE report/export UI or explicit approval to contact the RBI-listed DBIE support address. Without one of these, repeated public-page fetches will not produce the missing raw export and must not be repeated.


## Targeted RBI bulletin-index cross-check — 2015-Q2 / 2021-Q2 (2026-11-15)

Purpose: use indexed official RBI bulletin pages to determine whether the prior NOT_RETRIEVED labels can be closed without DBIE interactive access. This is not a repeat of the earlier broad DBIE access attempt.

Official RBI results inspected:
- RBI June 16 2021 bulletin archive index lists Table 40, BPM6 USD-million, but the bulletin itself is June 2021 and its Table 40 is not a Q2 2021 observation: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?mon=6&yr=2021
- RBI June 16 2021 Table 40 (Id=20363) reports Oct-Dec 2019 and Oct-Dec 2020: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=20363
- RBI Aug 17 2021 Table 40 (Id=20483) reports Jan-Mar 2020 and Jan-Mar 2021(P): https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=20483
- RBI June 16 2022 Table 40 (Id=21114) reports Oct-Dec 2020 and Oct-Dec 2021(P): https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=21114
- Search for an RBI indexed Table 40 page explicitly containing Apr-Jun 2021 did not return a matching page. No exact Apr-Jun 2015 quarterly USD-million Table 40 page was located either.
- RBI Apr 11 2016 Bulletin result (Id=16211) is Table 41 in ₹ billion and contains Oct-Dec 2014 and Oct-Dec 2015, not Apr-Jun 2015: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=16211

Conclusion:
- 2015-Q2 and 2021-Q2 remain NOT_RETRIEVED; no annual, IIP stock, adjacent-quarter or INR table was substituted.
- No numeric comparison, PASS, FAIL, or data-source promotion is claimed.
- Public indexed-source search is exhausted for this bounded query; the remaining route is interactive DBIE access or user-approved contact with RBI DBIE support. Do not repeat identical searches absent new source evidence.
- No CSV, manifest, sidecar, prior PASS artifact, production code, or gate changed.

Progress:
- Bounded official-index cross-check: 100% complete; both target values remain NOT_RETRIEVED.
- Raw quarterly DBIE export: NOT_RETRIEVED.
- Existing direct validation: 11 quarters / 22 of 22 side comparisons PASS_WITH_ROUNDING.
- IMF BOP workstream remains 5/7 = 71.4%; vintage NOT_READY / NOT_VERIFIED; full V11.3 progress NOT_CALCULABLE.
