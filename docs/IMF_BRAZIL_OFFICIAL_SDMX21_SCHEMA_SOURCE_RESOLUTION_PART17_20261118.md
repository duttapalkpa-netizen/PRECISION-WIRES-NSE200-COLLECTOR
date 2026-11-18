# IMF Brazil SDMX 2.1 Official Schema Source Resolution — Part 17
Date: 2026-11-18
Scope: provenance/source resolution only; no production changes.

## Finding
The official SDMX Technical Standards Working Group repository provides an authoritative, version-pinned SDMX-ML 2.1 schema release:
- Repository: https://github.com/sdmx-twg/sdmx-ml
- Release/tag: `v2.1`
- Tag target commit: `bc28a2255966a3b8d33ec8f61e19f42e6e193284`
- Release: “SDMX-ML v2.1 Schemas and Samples, 2020” (published 2021-03-25); release page identifies it as the current SDMX-ML 2.1 Technical Specification and links the previous versioned repository.
- The SDMX TWG GitHub organization identifies itself as the standards working group and is domain-verified for sdmx.org.
- Official schema catalogue: https://xml.sdmx.org/ lists the SDMX 2.1 schema family and its registry files.

The repository's `schemas/` directory at tag `v2.1` was successfully enumerated through the GitHub repository API: **58 .xsd files**. The official release's schema directory is therefore a concrete, immutable source path, resolving the prior uncertainty about whether the third-party `airosa/sdmx-ml-v2_1` mirror was the only accessible version-pinned source.

## Direct file evidence
The following files were fetched from the official repository's raw URLs at tag `v2.1` and inspected:
- `SDMXMessage.xsd` — Git blob SHA `9bbb26d204c9a36b50f491a6d540519069abf9f7`, 76,322 bytes.
- `SDMXRegistry.xsd` — Git blob SHA `e70fbb8024310761833134989e2217b40f0ad5d7`, 1,083 bytes.
- `SDMXRegistryBase.xsd` — Git blob SHA `70d2a5e7991d57e36f23b16a29e7664c6ace42cc`, 12,512 bytes.
- `SDMXRegistryRegistration.xsd` — Git blob SHA `e851b312e2b2b9b2aabb5db9521e4a83e6446319`, 14,052 bytes.
- `SDMXRegistryStructure.xsd` — Git blob SHA `9ca2b346d2821c5e4b15da3fc9ed9f235e524cde`, 7,588 bytes.
- `SDMXRegistrySubscription.xsd` — Git blob SHA `38346e1712ae7daa5a2ffb8092f1a89e9fcd63b5`, 45,027 bytes.
- `SDMXCommon.xsd` — Git blob SHA `6243e16e62dfc20cb359723b2ae9908bd7f831e9`, 98,823 bytes.
- `SDMXCommonReferences.xsd` — Git blob SHA `e546f78cda521b41c1a5fe30bada84e2934858e8`, 240,042 bytes.
- `SDMXStructure.xsd` — Git blob SHA `41d6cd341415461cbd6cfbf40b0727fd9b7e471a`, 38,794 bytes.
- `SDMXStructureBase.xsd` — Git blob SHA `dd3f9632f333083bae52d8e3265b8828feb6a9cf`, 34,435 bytes.
- `xml.xsd` — Git blob SHA `9294f94721e6ac9ddbd3d92ce1459aa9fae10d9f`, 2,700 bytes.

All listed Git blob SHAs are Git object identifiers, **not SHA-256 file digests**. No SHA-256 values are asserted in this report.

## Schema-path confirmation
The fetched official `SDMXMessage.xsd` imports `SDMXRegistry.xsd`; `SDMXRegistry.xsd` includes `SDMXRegistryBase.xsd`, `SDMXRegistryRegistration.xsd`, `SDMXRegistryStructure.xsd`, and `SDMXRegistrySubscription.xsd`. The registration schema includes the base registry schema and imports common and structure schemas. This independently confirms the relevant official schema dependency path and supports the Part-16 parser's use of the SDMX 2.1 RegistryInterface/registration message family.

## Limits / acceptance
- Official SDMX TWG v2.1 tag and commit identified: **PASS**.
- Official schema directory enumerated (58 XSDs): **PASS**.
- Key registry/message XSD files retrieved and inspected: **PASS**.
- Complete 58-file bundle archived into this project: **NOT_DONE**.
- SHA-256 computed for each official XSD: **NOT_DONE**. Git blob SHA is not a substitute.
- Complete transitive dependency closure and offline formal XSD validation: **NOT_DONE**.
- Official xml.sdmx.org raw-host direct URL fetch via the web cache still returned cache miss in this session; the official SDMX TWG GitHub release/tag is the independently verified source used here.
- Real Brazil registration transaction fixture, PA revision chronology and BOP6/BOP_BPM6 mismatch: unchanged from prior parts. Mismatch remains **CONFIRMED / UNRESOLVED**; Brazil/EM remains **BLOCKED**.

## Next exact actions
1. Materialize all 58 XSD files from the pinned official tag into a versioned project schema bundle, preserving raw bytes and source URLs.
2. Compute SHA-256 from the actual downloaded bytes (not Git blob IDs); write a manifest with tag, commit, path, byte count, SHA-256, retrieval time and URL.
3. Resolve every include/import locally; reject any unpinned network dependency.
4. Run offline XSD validation against the existing parser fixtures; preserve fixture-only status and do not call it real Brazil event evidence.
5. Keep PR #39 draft and unmerged pending formal validation and genuine owner-exported Brazil transaction data.

No paid service, synthetic market data, production selector change, macro weight, trading admission, merge or deployment was performed. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E remain unchanged. UNKNOWN is not PASS.
