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


## Chapter 34 — Part-2: IMF BOP DSD Semantic & Codelist Audit (2026-11-18)

### Evidence inspected
- Reused the exact raw XML from final verified artifact `14403372899`; no endpoint probe repeated.
- Current-route raw XML: 895,438 bytes; SHA-256 `f4df050115748bc0d20f07c47b33bd9bd7157cf6132e9c36a70a6f868bedd075`; HTTP 200; SDMX-ML 2.1; DSD IMF:BOP(2.6.0).
- Parsed the actual DimensionList, AttributeList and MeasureList and followed every embedded codelist reference. Confirmed 18 dimensions, 15 attributes, one measure, 22 embedded codelists and 4,097 embedded codes.
- Machine-readable inventory committed at `data/global_capital_rotation/IMF_BOP_DSD_2_6_0_SEMANTIC_INVENTORY_V1.json`; commit `52658916787c1f31ea6d5a58f6541261a5a18e83`.

### Key extraction semantics established from the embedded codelists
- `INT_ACC_ITEM=FA`: Financial account (IMF:CL_ACCOUNTS_ITEM 1.8.0).
- `FUNCTIONAL_CAT=P`: Portfolio Investment (IMF:CL_FUNCTIONAL_CAT 1.10.1).
- `FLOW_STOCK_ENTRY=T`: Transactions (IMF:CL_FSENTRY 1.1), distinct from positions/stocks and other changes.
- `ACCOUNTING_ENTRY=A`: Assets (Net Acquisition of); `L`: Liabilities (Net Incurrence of) (IMF:CL_ACCOUNT_ENTRY 1.5.0). Keep separate; do not collapse or sign-flip.
- `INSTR_ASSET=F3`: Debt securities; `F5`: Equity and investment fund shares/units (ESTAT:CL_INSTR_ASSET 1.15.0 referenced by this DSD). Preserve agency and version; do not assume all referenced codelists are IMF-maintained.
- `UNIT_MEASURE` and `CURRENCY_DENOM` both reference IMF:CL_UNIT 1.19.0; unit and currency-denomination dimensions remain distinct. `UNIT_MULT` and `DECIMALS` are mandatory attributes in the DSD and must be retained.
- `OBS_STATUS` and `CONF_STATUS` are mandatory attributes; missing/suppressed observations must not be coerced to zero.

### Acceptance matrix
| Gate | Status |
|---|---|
| Exact DSD identity and raw hash | PASS |
| Dimension-to-codelist reference inventory | PASS |
| Embedded codelist inventory (22 / 4,097 codes) | PASS |
| Critical FA / P / T / A / L / F3 / F5 code labels | PASS |
| Unit, multiplier, decimals and observation-status fields identified | PASS |
| Exact IMF dissemination dataflow linkage and permitted series key | UNKNOWN / BLOCKED |
| IMF BOP observation payload and country-period rows | NOT_DONE |
| Versioned EM membership and aggregate | NOT_DONE |

### Important limitation
This is a metadata-semantic mapping, not proof that an IMF-owned public dissemination dataflow exposes these exact dimensions/codes or that a particular series is available. The earlier extraction specification explicitly reports the IMF BOP6 registration as a 2023 sample compact URL and no verified current public observation endpoint. Do not query the sample registration as if it were a complete panel, do not substitute ESTAT dataflows, and do not infer a valid data key from the DSD alone.

### Decision and next action
Part-2 metadata semantic audit: PASS for the captured DSD and embedded codelists. Observation access remains UNKNOWN/BLOCKED; no country rows or EM aggregates created. Next bounded task: qualify the official IMF BOP dataflow-to-DSD linkage and its permitted query dimensions from an official, directly accessible catalogue/constraint response. Stop if authentication is required; no bypass or guessed key. All production invariants remain unchanged.
