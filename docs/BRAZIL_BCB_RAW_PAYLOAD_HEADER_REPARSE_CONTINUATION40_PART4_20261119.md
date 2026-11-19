# Brazil BCB Raw Payload Independent Header Reparse — Continuation 40, Part-4
Date: 2026-11-19 (Asia/Kolkata)
Scope: Reuse the already captured official BCB XML from IMF RSS + Brazil Registration Audit run 44301482210; independently reparse the actual XML bytes. No new network retrieval, no duplicate capture, no authenticated action, no production changes.

## Progress / provenance
- Existing GitHub Actions run: 44301482210, SUCCESS; artifact 14426565546; artifact digest 0a35ddb0f83ae2c14f5ce2a60dc365f5324e56de55a3442227b8a74e786a132f.
- Artifact ZIP downloaded again from GitHub and extracted locally. Existing BCB file: bcb_bop_bpm6.xml.
- Official source URL recorded in original manifest: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
- Original retrieval metadata: HTTP 200; Content-Type text/xml; retrieved_at_utc 2026-11-18T12:11:07.589328+00:00; 4,840,062 bytes.
- Independent local SHA-256 of the exact extracted BCB bytes: 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c. Matches the original manifest.
- XML parse: PASS; root {http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message}StructureSpecificData.

## Corrected exact header parse
The earlier scanner recorded header_reference_elements=[] because it looked for literal DataflowRef/ProviderRef elements. That empty result was a parser coverage failure, not evidence that the Dataflow was absent.

Independent parse of the root xsi:schemaLocation yields the exact SDMX Dataflow URN:
urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD
Therefore exact payload Dataflow = IMF:BOP_BPM6(1.0), observation dimension = TIME_PERIOD.

The Header/Structure element independently carries:
- structureID = IMF_BOP_BPM6_1_0
- namespace = urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD
- dimensionAtObservation = TIME_PERIOD

The DataSet independently carries structureRef = IMF_BOP_BPM6_1_0.

## Dataset structure and bounded coverage
- DataSet contains 237 Series.
- Total observations: 89,097.
- Series dimensions: DATA_DOMAIN=BOP6; REF_AREA=BR; COUNTERPART_AREA=W1; FREQ=M; UNIT_MULT=6; TIME_FORMAT=P1M.
- INDICATOR cardinality = 237 (all series distinct on the indicator dimension).
- Observation TIME_PERIOD coverage: 1995-01 through 2026-09; 381 unique monthly periods.
- These are properties of this single captured BCB payload, not proof of registry admission or a historical revision chronology.

## Reconciliation against current public PA structure (prior Part-3)
Current PA IMF:BR_BOP_BP6(1.0) has StructureUsage -> IMF:BOP6(1.0), Provider -> IMF:BR1. The BCB payload's exact Dataflow remains IMF:BOP_BPM6(1.0). The DataSet DATA_DOMAIN=BOP6 does not override or rename the root Dataflow identity; they are distinct SDMX concepts. Do not infer equivalence from matching BOP6 text or shared ECOFIN_DSD.

Result:
- BCB payload Dataflow extraction: PASS (independently re-parsed from root schemaLocation and Structure namespace).
- BCB payload DataSet structureRef extraction: PASS.
- Dataset series/observation and monthly coverage parse: PASS.
- PA Dataflow vs payload Dataflow mismatch: CONFIRMED / UNRESOLVED.
- Brazil-specific official crosswalk or correction: NOT_PROVEN.
- Brazil Reconstruction admission: BLOCKED.

## Limitations and rejected actions
- No new BCB GET was performed; this was an independent reparse of the already archived HTTP-200 raw response. Avoid needless duplicate downloads.
- No PA Changelog/Revision/Compare export is present; historical PA chronology remains UNKNOWN.
- No BCB payload edit, IMF registration write, credential use, authenticated UI interaction, or inferred alias.
- Do not retry the known transaction-ID-2 fusion-json/sdmx-json HTTP 500 endpoints.
- This report does not resolve the mismatch; it closes the parser blind spot and supplies stronger reproducible payload-side evidence.

## Exact next actions
1. Keep the technical mismatch gate BLOCKED until an authoritative IMF-side correction or documented Brazil-specific crosswalk is captured.
2. Obtain the exact PA IMF:BR_BOP_BP6(1.0) Changelog/Revisions/Compare and IMF:BR1 registration detail through authorized owner-side export; no credentials should be shared in chat.
3. Continue GCR Chile current-vintage Q1/Q2 revision matrix and India Q1-2026 liability review separately; do not publish a full 154-member aggregate before missingness, vintage, BPM basis and scale gates pass.

## Invariants
₹0, free official sources only. No synthetic data, guessed IDs, fabricated timestamps/hashes, inferred aliases, or unauthorized access. UNKNOWN is never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged.