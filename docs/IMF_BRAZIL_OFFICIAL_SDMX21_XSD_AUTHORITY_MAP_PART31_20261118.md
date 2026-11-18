# IMF Brazil Reconstruction — Official SDMX-ML 2.1 XSD authority map (Part-31)
Date: 2026-11-18 (Asia/Kolkata)

## Scope and source
The user supplied a mobile screenshot of the SDMX community homepage (sdmx.org). The screenshot establishes that the page is the SDMX community's official public site and describes SDMX's role in statistical data/metadata exchange. It does not itself establish a particular schema version, file inventory, or validation result.

Follow-up source verification located the SDMX-published XML schema index:
- Official index: https://xml.sdmx.org/
- The index states that it publishes official XSD schemas for SDMX-ML structural metadata, data, reference metadata and registry operations, with versions 2.0, 2.1, 3.0.0 and 3.1.0.
- The SDMX-ML schema location for 2.1 is https://xml.sdmx.org/2.1/SDMXMessage.xsd and its message namespace is http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message.
- The 2.1 index visibly lists 52 XSD files (index links 92–143 inclusive). Relevant registry files include SDMXRegistry.xsd, SDMXRegistryBase.xsd, SDMXRegistryRegistration.xsd, SDMXRegistryStructure.xsd and SDMXRegistrySubscription.xsd.
- Official SDMX technical standards page identifies Section 3B as SDMX-ML XML schemas/samples and Section 5 as the Registry Specification / logical interfaces: https://sdmx.org/standards-2/.
- Official Registry Specification PDF describes Submit Registration, Query Registration, Submit Structure and other registry interfaces: https://sdmx.org/wp-content/uploads/SDMX_2-1_SECTION_5_RegistrySpecification_2020-07.pdf.

## Parser implications
1. Keep the parser pinned to SDMX-ML 2.1 for the captured Brazil payload unless the payload itself establishes another version. Do not silently upgrade it to 3.x.
2. Validate the message envelope against the 2.1 message schema and the registry content against the imported 2.1 registry schemas. The previously corrected namespace split remains required: message envelope elements use the message namespace; RegistrationRequest, Registration, ProvisionAgreement and Datasource use the registry namespace.
3. Build the schema dependency closure from actual xs:include/xs:import references starting at the relevant 2.1 entry schemas. Do not assume that the 52 top-level index entries equal the transitive closure, nor use an arbitrary 58-file count without a generated manifest.
4. Archive each exact XSD byte stream, URL, retrieval timestamp, HTTP status/headers, byte count and raw-byte SHA-256. Then run offline XSD validation against the archived closure and fixtures. A successful parser unit test is not XSD validation.
5. Preserve the distinction between structural validity and chronology/provenance: XSD validation cannot prove when IMF registered the Brazil Provision Agreement, whether a registration was re-registered, or resolve the BOP6 vs BOP_BPM6 Dataflow ID mismatch.

## Evidence status
- SDMX official homepage identity/context from user screenshot: PASS (homepage context only).
- Official SDMX-ML XSD publication authority and 2.1 index discovery: PASS.
- 2.1 index count: 52 listed XSD entries, based on the opened official index lines 109–164.
- Exact 2.1 schema bytes downloaded/archived: NOT_DONE.
- Full transitive dependency closure and raw-byte SHA-256 manifest: NOT_DONE.
- Offline XSD validation of Brazil XML: NOT_DONE.
- Existing offline parser unit tests: 16/16 PASS in GitHub Actions Run #21 (44329119370), but this remains unit-test evidence only.
- Brazil registration chronology / PA history: UNKNOWN / NOT_DONE.
- Dataflow mismatch IMF:BOP6(1.0) vs IMF:BOP_BPM6(1.0): CONFIRMED / UNRESOLVED.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next bounded action
Acquire the official 2.1 schema files reachable from the relevant message and registry XSDs, recursively resolve imports/includes, and produce a deterministic manifest. Keep the job small and resumable (index/dependency resolver first; byte archive and offline validation in a separate short job). Fail closed on missing imports, namespace mismatch, unpinned schema versions or hash mismatch.

## Guardrails
No paid APIs, synthetic data, guessed timestamps, production integration, PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
