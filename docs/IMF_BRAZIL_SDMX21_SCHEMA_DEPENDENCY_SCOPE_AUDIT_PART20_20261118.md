# IMF Brazil SDMX 2.1 Schema Dependency Scope Audit — Part 20
Date: 2026-11-18
Scope: pinned-source schema inventory and dependency-path audit; QA/research only.

## Source pin and inventory
- Official SDMX Technical Standards Working Group repository: https://github.com/sdmx-twg/sdmx-ml
- Tag: v2.1
- Tag target commit: bc28a2255966a3b8d33ec8f61e19f42e6e193284
- Recursive Git tree query at the pinned commit returned `truncated=false` and exactly 58 paths under `schemas/*.xsd`.
- This establishes the pinned schema inventory, not a local archived bundle and not raw-byte SHA-256 values.

## Root schema dependency findings
Inspection of the official pinned `SDMXMessage.xsd` showed its direct imports:
- SDMXMessageFooter.xsd
- SDMXCommon.xsd
- SDMXStructure.xsd
- SDMXQuery.xsd
- SDMXRegistry.xsd
- SDMXDataGeneric.xsd
- SDMXDataStructureSpecific.xsd
- SDMXMetadataGeneric.xsd
- SDMXMetadataStructureSpecific.xsd
- xml.xsd

Thus the standard RegistryInterface root is part of the general SDMX message schema, whose root file directly imports multiple data, metadata, query, structure and registry modules. A registry-only subset must not be represented as the complete dependency closure for validating against SDMXMessage.xsd.

## Registry path confirmed from pinned XSDs
- SDMXRegistry.xsd includes SDMXRegistryBase.xsd, SDMXRegistryRegistration.xsd, SDMXRegistryStructure.xsd, SDMXRegistrySubscription.xsd.
- SDMXRegistryRegistration.xsd includes SDMXRegistryBase.xsd and imports SDMXCommon.xsd and SDMXStructure.xsd.
- SDMXRegistryBase.xsd imports SDMXCommon.xsd.
- SDMXCommon.xsd imports SDMXCommonReferences.xsd and xml.xsd.
- SDMXStructure.xsd includes SDMXStructureBase.xsd and its structure module schemas; SDMXStructureBase.xsd imports SDMXCommon.xsd.
- SDMXMessageFooter.xsd imports SDMXCommon.xsd and xml.xsd.
- The inspected `SDMXRegistryRegistration.xsd` confirms RegistrationRequest/@action is required and typed as common:ActionType.
- The pinned `SDMXCommon.xsd` ActionType enumeration is exactly Append, Replace, Delete, Information. The parser's four-value allow-list matches the XSD lexical enumeration.
- The inspected `SDMXRegistryBase.xsd` defines Datasource as a choice including SimpleDataSource of type xs:anyURI. The PA reference type is in SDMXCommonReferences.xsd and permits a URN element; parser subtree text/attribute extraction can retain exact URN values.

## Completeness boundary
For this Part-20 audit, 12 key schema files were fetched and their import/include references inspected. The complete 58-file raw-byte bundle was not archived in the repo, and the full transitive dependency closure has NOT been mechanically verified. No local XML Schema processor was run. No raw-byte SHA-256 manifest is claimed. Therefore:
- Pinned inventory: PASS
- Root direct-import list: PASS
- Registry branch dependency relationships inspected: PASS
- Full 58-file bundle archived: NOT_DONE
- Full transitive closure resolved against local files: NOT_DONE
- Per-file raw-byte SHA-256 manifest: NOT_DONE
- Offline formal XSD validation: NOT_DONE

## Exact pinned inventory
- `schemas/SDMXCommon.xsd`
- `schemas/SDMXCommonReferences.xsd`
- `schemas/SDMXDataGeneric.xsd`
- `schemas/SDMXDataGenericBase.xsd`
- `schemas/SDMXDataGenericTimeSeries.xsd`
- `schemas/SDMXDataStructureSpecific.xsd`
- `schemas/SDMXDataStructureSpecificBase.xsd`
- `schemas/SDMXDataStructureSpecificTimeSeries.xsd`
- `schemas/SDMXMessage.xsd`
- `schemas/SDMXMessageFooter.xsd`
- `schemas/SDMXMetadataGeneric.xsd`
- `schemas/SDMXMetadataStructureSpecific.xsd`
- `schemas/SDMXQuery.xsd`
- `schemas/SDMXQueryBase.xsd`
- `schemas/SDMXQueryCategorisation.xsd`
- `schemas/SDMXQueryCategory.xsd`
- `schemas/SDMXQueryCodelist.xsd`
- `schemas/SDMXQueryConcept.xsd`
- `schemas/SDMXQueryConstraint.xsd`
- `schemas/SDMXQueryData.xsd`
- `schemas/SDMXQueryDataStructure.xsd`
- `schemas/SDMXQueryDataflow.xsd`
- `schemas/SDMXQueryHierarchicalCodelist.xsd`
- `schemas/SDMXQueryMetadata.xsd`
- `schemas/SDMXQueryMetadataStructure.xsd`
- `schemas/SDMXQueryMetadataflow.xsd`
- `schemas/SDMXQueryOrganisation.xsd`
- `schemas/SDMXQueryProcess.xsd`
- `schemas/SDMXQueryProvisionAgreement.xsd`
- `schemas/SDMXQueryReportingTaxonomy.xsd`
- `schemas/SDMXQuerySchema.xsd`
- `schemas/SDMXQueryStructureSet.xsd`
- `schemas/SDMXQueryStructures.xsd`
- `schemas/SDMXQueryTransformation.xsd`
- `schemas/SDMXRegistry.xsd`
- `schemas/SDMXRegistryBase.xsd`
- `schemas/SDMXRegistryRegistration.xsd`
- `schemas/SDMXRegistryStructure.xsd`
- `schemas/SDMXRegistrySubscription.xsd`
- `schemas/SDMXStructure.xsd`
- `schemas/SDMXStructureBase.xsd`
- `schemas/SDMXStructureCategorisation.xsd`
- `schemas/SDMXStructureCategory.xsd`
- `schemas/SDMXStructureCodelist.xsd`
- `schemas/SDMXStructureConcept.xsd`
- `schemas/SDMXStructureConstraint.xsd`
- `schemas/SDMXStructureDataStructure.xsd`
- `schemas/SDMXStructureDataflow.xsd`
- `schemas/SDMXStructureHierarchicalCodelist.xsd`
- `schemas/SDMXStructureMetadataStructure.xsd`
- `schemas/SDMXStructureMetadataflow.xsd`
- `schemas/SDMXStructureOrganisation.xsd`
- `schemas/SDMXStructureProcess.xsd`
- `schemas/SDMXStructureProvisionAgreement.xsd`
- `schemas/SDMXStructureReportingTaxonomy.xsd`
- `schemas/SDMXStructureStructureSet.xsd`
- `schemas/SDMXStructureTransformation.xsd`
- `schemas/xml.xsd`

## Decisions / safety
No parser logic change in this part; Part-19 namespace correction remains as recorded. No merge, production integration, workflow dispatch, paid API, market-data modification, macro weights or trading admission. PR #39 remains research-only. Brazil transaction evidence and chronology remain NOT_DONE/UNKNOWN; BOP6 vs BOP_BPM6 mismatch remains CONFIRMED/UNRESOLVED; Brazil/EM admission BLOCKED. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
