# IMF Brazil Reconstruction — SDMX-ML 2.1 tagged schema dependency roots (Part-32)
Date: 2026-11-18 (Asia/Kolkata)

## Exact version pin
The official SDMX-ML GitHub repository release page identifies the v2.1 release tag as `v2.1`, commit prefix `bc28a22`, and describes it as the current SDMX-ML 2.1 Technical Specification corrected in July 2020:
https://github.com/sdmx-twg/sdmx-ml/releases
The exact release commit used for inspection is `bc28a22`. This avoids accidentally reading the current v3.1 schemas from the repository default branch.

Official publication index: https://xml.sdmx.org/ (2.1 directory lists 52 XSD files).
Official source repository: https://github.com/sdmx-twg/sdmx-ml/tree/v2.1/schemas

## Verified dependency edges (tag v2.1)
All files below were fetched from repository `sdmx-twg/sdmx-ml`, ref `bc28a22`. The Git blob SHAs below identify Git objects; they are NOT raw-byte SHA-256 hashes.

- `SDMXMessage.xsd`, blob `9bbb26d204c9a36b50f491a6d540519069abf9f7`: imports `SDMXMessageFooter.xsd`, `SDMXCommon.xsd`, `SDMXStructure.xsd`, `SDMXQuery.xsd`, `SDMXRegistry.xsd`, `SDMXDataGeneric.xsd`, `SDMXDataStructureSpecific.xsd`, `SDMXMetadataGeneric.xsd`, `SDMXMetadataStructureSpecific.xsd`, and `xml.xsd`.
- `SDMXRegistry.xsd`, blob `e70fbb8024310761833134989e2217b40f0ad5d7`: includes `SDMXRegistryBase.xsd`, `SDMXRegistryRegistration.xsd`, `SDMXRegistryStructure.xsd`, `SDMXRegistrySubscription.xsd`.
- `SDMXRegistryBase.xsd`, blob `70d2a5e7991d57e36f23b16a29e7664c6ace42cc`: imports `SDMXCommon.xsd`.
- `SDMXRegistryRegistration.xsd`, blob `e851b312e2b2b9b2aabb5db9521e4a83e6446319`: includes `SDMXRegistryBase.xsd`; imports `SDMXCommon.xsd` and `SDMXStructure.xsd`.
- `SDMXRegistryStructure.xsd`, blob `9ca2b346d2821c5e4b15da3fc9ed9f235e524cde`: includes `SDMXRegistryBase.xsd`; imports `SDMXCommon.xsd` and `SDMXStructure.xsd`.
- `SDMXRegistrySubscription.xsd`, blob `38346e1712ae7daa5a2ffb8092f1a89e9fcd63b5`: includes `SDMXRegistryBase.xsd`; imports `SDMXCommon.xsd` and `SDMXStructure.xsd`.
- `SDMXCommon.xsd`, blob `6243e16e62dfc20cb359723b2ae9908bd7f831e9`: includes `SDMXCommonReferences.xsd`; imports `xml.xsd`.
- `SDMXMessageFooter.xsd`, blob `54d828119e7f16414fd0dcac577221317a1855b7`: imports `SDMXCommon.xsd` and `xml.xsd`.
- `SDMXStructure.xsd`, blob `41d6cd341415461cbd6cfbf40b0727fd9b7e471a`: includes 17 structure modules: Base, Categorisation, Category, Codelist, Concept, Constraint, DataStructure, Dataflow, HierarchicalCodelist, Metadataflow, MetadataStructure, Organisation, ProvisionAgreement, Process, ReportingTaxonomy, StructureSet, Transformation.
- `SDMXQuery.xsd`, blob `85f1f9127314baa427e11e101bfb78f5837c6333`: includes 21 query modules (Base, Categorisation, Category, Codelist, Concept, Constraint, Data, Dataflow, DataStructure, HierarchicalCodelist, Metadata, Metadataflow, MetadataStructure, Organisation, Process, ProvisionAgreement, ReportingTaxonomy, Schema, StructureSet, Structures, Transformation) and imports Common.

## Key parser-specific conclusion
The official v2.1 Message schema directly imports Registry and the other SDMX message families; Registry is not a standalone one-file schema. For a RegistryInterface document, the relevant structural validation closure must include the Message root and its imports, then recursively resolve all includes/imports for those schemas. The root imports nine SDMX namespace modules plus W3C xml.xsd. The Registry subtree adds four included Registry modules and further Common/Structure dependencies.

Do not count unique schema files by adding edge counts: imports/includes overlap. A graph traversal with URL/path normalization and cycle detection is required. Also distinguish the full Message schema closure from a minimal purpose-built validation schema set; do not prune imports unless a formally tested reduced schema is justified.

## Remaining work / status
- Official v2.1 tag and release commit pin: PASS.
- Direct dependency edges for 10 key schema files inspected: PASS.
- Full recursive transitive closure across every reachable schema: NOT_DONE.
- Exact schema bytes archive and HTTP retrieval metadata: NOT_DONE.
- Raw-byte SHA-256 manifest: NOT_DONE (Git blob SHAs above are not raw-byte SHA-256).
- Offline XSD validation of the captured Brazil XML: NOT_DONE.
- Existing offline parser unit tests: 16/16 PASS (Run #21 / 44329119370), but not XSD validation.
- Brazil registration chronology / PA history: UNKNOWN / NOT_DONE.
- IMF:BOP6(1.0) vs IMF:BOP_BPM6(1.0): CONFIRMED / UNRESOLVED.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next bounded implementation
Create a short, deterministic resolver/archiver pinned to tag `v2.1` (commit `bc28a22`). Traverse relative imports/includes from `SDMXMessage.xsd`, preserve exact resolved URLs and file bytes, reject missing/escaping locations and unexpected namespaces, emit a sorted manifest with raw SHA-256, then validate the Brazil XML offline. Keep download and validation in separate short CI jobs.

## Guardrails
No paid APIs, synthetic data, guessed timestamps, production integration, PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
