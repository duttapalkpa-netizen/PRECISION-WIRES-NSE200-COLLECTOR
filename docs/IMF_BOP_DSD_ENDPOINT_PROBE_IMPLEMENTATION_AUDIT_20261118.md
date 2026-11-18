# IMF BOP DSD V2.6.0 Endpoint Verification — Chapter 34 Part-1 (2026-11-18)

## Objective
Resolve the IMF BOP DSD metadata retrieval blocker using only the two previously documented official IMF SDMX Central routes. This is metadata qualification only; no BOP observations or aggregates are produced.

## Runtime evidence
- First execution Run `44249890707`: SUCCESS; exposed a parser bug in the initial probe (the DSD identifier was searched only in the first 200 KB of XML).
- Parser correction commit `930638c30c937d73e2c7d84bcf939d34acb652f5`: identify the exact XML `DataStructure` node by agencyID=IMF, id=BOP, version=2.6.0.
- Descriptor-scope correction commit `017265feb5fd99c54ce752033d10a3fceb3e209c`: count only direct members of DimensionList and AttributeList, avoiding false counts from nested codelists.
- Decision-state correction commit `42606d3687fe8dc0b6d2b64a740795cde4c883f9`: derive METADATA_ROUTE_VERIFIED from the parsed DSD evidence rather than a hard-coded UNKNOWN string.
- Final bounded validation Run `44250316163`: SUCCESS; probe step and artifact upload completed. Run head SHA `42606d3687fe8dc0b6d2b64a740795cde4c883f9`.
- Job/check ID `134619103234`; final artifact ID `14403372899`; artifact size 191,791 bytes; ZIP SHA-256 `1321f32274b48eca7a66dc1220c656be1a54faf2270fa76edc020f60cdf95def`; retained by GitHub until 2027-02-16.
- Workflow time limit: 5 minutes. Run completed successfully within the limit.

## Verified official endpoint evidence
Both exact candidate paths returned HTTP 200, Content-Type `application/xml;charset=UTF-8`, valid SDMX 2.1 Structure XML, and the exact IMF:BOP DSD identity at version 2.6.0.

| Route | Retrieval UTC | Bytes | SHA-256 | DSD identity |
|---|---|---:|---|---|
| Current `/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/` | 2026-11-18T06:18:14.598091Z | 895,438 | `f4df050115748bc0d20f07c47b33bd9bd7157cf6132e9c36a70a6f868bedd075` | PASS |
| Legacy `/ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/` | 2026-11-18T06:18:25.216081Z | 895,438 | `145fb6eeceb259564384b7e927ddae39d991a144713c5b57af82d7d66b4973cb` | PASS |

The parser confirms DSD version 2.6.0, **18 dimensions (including TIME_PERIOD)** and **15 attributes**. Current and legacy responses have separate response hashes because their response headers/prepared IDs differ; both identify the same requested DSD. The dimension and attribute IDs and positions/assignment statuses are recorded in the run's `probe_summary.json` and raw XML artifact.

## Important scope limits
- **Metadata endpoint qualification: PASS.** The current documented route is now the preferred verified route; legacy route also returned the same DSD identity.
- **Full codelist semantic audit: NOT_DONE.** The downloaded XML includes referenced structures, but a complete codelist inventory, code-value validation, unit/sign/frequency semantics and crosswalk to extraction fields still require a separate audit.
- **BOP observations: NOT_DOWNLOADED.** No observation endpoint or country-period series was queried.
- **Emerging-market aggregation: NOT_DONE.** No EM membership, aggregate, or portfolio-flow total was created.
- BOP remains annual/quarterly context and must not be treated as a daily market trigger.
- Original historical BOP observation coverage and any EM panel remain UNKNOWN until independently retrieved and validated.

## Invariants
₹0 spend; official/free sources only; no synthetic values, guessed dimensions, inferred signs/units, or fabricated timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and production workflows unchanged. No production integration authorized.
