# IMF Brazil SDMX 2.1 schema and timestamp semantics audit — Part 15
Date: 2026-11-18 (Asia/Kolkata)
Workstream: PRECISION-WIRES V11.3 / গবেষণা যাচাই অব্যাহত 36

## Purpose
Improve the Brazil registration-event verification path by checking the parser's assumptions against the published SDMX 2.1 registry specification and IMF's own operational guide. This is a specification audit, not a real Brazil transaction validation.

## Source hierarchy and retrieval boundary
1. Official SDMX schema catalogue: https://xml.sdmx.org/
   - The catalogue describes itself as publishing official SDMX-ML XSD schemas and lists a dedicated 2.1 schema set including SDMXMessage.xsd, SDMXRegistry.xsd, SDMXRegistryBase.xsd and SDMXRegistryRegistration.xsd.
   - Direct retrieval of the official XSD files was attempted in this session but failed at the web/container retrieval layer. Therefore no claim is made that the official raw XSD bytes were locally archived or validated.
2. SDMX 2.1 schema mirror, pinned commit:
   - Repository: https://github.com/airosa/sdmx-ml-v2_1
   - Commit: d66144444d27c5b66361fb508d795a87072821ac
   - Files and blob SHAs:
     - schemas/SDMXRegistry.xsd — 8529b280653cced66e6f5923b19bdbeeebf1d52e
     - schemas/SDMXRegistryBase.xsd — 763c6b0930eef9a7812b539f659b4ed53cd7e477
     - schemas/SDMXRegistryRegistration.xsd — 84c44f5bc7c0c90ab8dd0429e5b23d3f65112963
     - schemas/SDMXRegistryStructure.xsd — b3ed7b27509d8a28c69a9f2cd0e78c37663ccb61
     - schemas/SDMXRegistrySubscription.xsd — 235a41c0365a17764a146690e22f830c35a33cf7
     - schemas/SDMXMessage.xsd — 7df02f90ea9b8fe940166410e707ebf6c992d384
     - schemas/SDMXCommon.xsd — 46bf6b8b7f171c8245b38688fb57d82b1471244d
   - These are a pinned third-party mirror, not the official xml.sdmx.org raw downloads. Their content was inspected to derive validation requirements, but equivalence to the official published XSD bytes has NOT been hash-verified. Treat the XSD-specific details below as mirror-derived specification evidence pending official raw-byte confirmation.
3. IMF SDMX Central Web Services Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
   - Its registration example uses RegistryInterface / SubmitRegistrationsRequest / RegistrationRequest action="Replace".
   - It says a registration links a Dataflow and Data Provider to a URL pointing to an SDMX-ML data file.
   - It says re-registering an existing registration updates the Last Updated timestamp.
4. IMF SDMX Central User Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
   - RSS transactions include structure additions/modifications/deletions and data registrations/deletions. Each RSS item links to the underlying SDMX 2.1 RegistryInterface document.

## Material schema observations (pinned mirror; not yet official-byte verified)
- RegistryInterface's registration request envelope is plural SubmitRegistrationsRequest; its request children are RegistrationRequest elements.
- Each RegistrationRequest contains a Registration element and a required action attribute.
- Registration contains a ProvisionAgreement reference and a Datasource.
- Datasource may contain SimpleDataSource and/or QueryableDataSource.
- The shared ActionType enumeration in the inspected mirror is Append, Replace, Delete, Information. The parser's current action allow-list (register, reregister, re-register, delete, replace) is not aligned with this enumeration: it omits Append/Information and accepts register/reregister strings not in that enum.
- Registration's lastUpdated attribute is typed as xs:dateTime in the inspected mirror, with documentation describing it as the timestamp for the last time the data source was updated. It is not, by itself, the registry transaction time.
- A PA reference in a registration event is a PA reference; the provider and Dataflow must be resolved through the PA's authoritative structure reference, not guessed from the PA ID suffix.

## Consequences for current parser
Current file: scripts/research/imf_brazil_event_parser.py
Current parser blob at last verified Part-10 state: a51dc69b28d244642736eca47e945bdd5b3d3459.

1. The parser currently scans arbitrary descendants and values rather than requiring the schema-shaped path RegistrationRequest -> Registration -> ProvisionAgreement + Datasource. This can overstate candidate evidence if a Brazil string occurs in an unrelated descendant.
2. The parser's action candidates currently include register/reregister/re-register and omit Append/Information. This must be corrected only after the official XSD bytes and actual IMF event fixtures are available; do not infer that Append maps one-to-one to "initial create" or Replace maps one-to-one to "re-register".
3. The parser currently treats BOP6-like strings found anywhere as Dataflow candidates. For a registration payload, the event may carry a PA reference; resolve that PA against the PA registry evidence and keep PA URN, Dataflow URN and provider URN as separate fields.
4. Do not use Registration/@lastUpdated as the event transaction timestamp. Preserve it as source_last_updated. Transaction timestamp must come from the event/transaction envelope or an official transaction log field, with timezone and raw lexical value preserved.
5. Existing 9 unit tests are parser-fixture tests only; they do not establish XSD validity or real IMF Brazil event behavior.

## Safe next parser contract (proposal; not implemented in this part)
- Parse only the exact RegistryInterface 2.1 namespace.
- Distinguish plural SubmitRegistrationsRequest from singular legacy/documentation wording; retain singular only as compatibility mode and mark schema_conformance UNKNOWN until proven against official schema.
- Require each registration candidate to be inside RegistrationRequest/Registration and collect only direct schema-relevant fields.
- Capture action lexical value exactly; classify against the official ActionType enum only after official XSD bytes are archived. Never translate action names to create/re-register without IMF transaction semantics.
- Capture PA URN, datasource URL, Registration ID, source_last_updated, and transaction timestamp as distinct fields.
- Resolve PA URN -> Dataflow and Provider via a separately hashed PA registry snapshot; do not infer from the PA identifier.
- Keep schema validation, semantic attribution, and historical chronology as separate acceptance gates. No candidate can auto-PASS.

## Acceptance
- Official schema catalogue discovery: PASS.
- IMF guide registration example / re-registration timestamp semantics: PASS.
- Pinned third-party 2.1 XSD mirror inspection: PASS as mirror-only evidence.
- Official raw XSD retrieval and SHA-256 archive: NOT_DONE.
- Local XSD validation of parser fixtures: NOT_DONE.
- Parser code correction: NOT_DONE (deliberately deferred pending official raw schema and event fixture).
- Real Brazil transaction fixture: NOT_DONE.
- Brazil historical registration chronology: UNKNOWN.
- BOP6 vs BOP_BPM6 payload mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission and market use: BLOCKED / NOT_AUTHORIZED.

## No-change statement
No parser or tests changed, no workflow run, no RSS/BCB repeat download, no full NSE collector, no production integration, no PR merge, no macro weights, no Brazil/EM admission, and no spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), and Engines A-E remain unchanged. UNKNOWN is not PASS.

## Sources
- Official SDMX XML schema catalogue: https://xml.sdmx.org/
- Pinned 2.1 XSD mirror commit: https://github.com/airosa/sdmx-ml-v2_1/tree/d66144444d27c5b66361fb508d795a87072821ac/schemas
- IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- IMF SDMX Central User Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
