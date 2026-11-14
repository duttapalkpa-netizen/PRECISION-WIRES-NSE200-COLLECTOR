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
