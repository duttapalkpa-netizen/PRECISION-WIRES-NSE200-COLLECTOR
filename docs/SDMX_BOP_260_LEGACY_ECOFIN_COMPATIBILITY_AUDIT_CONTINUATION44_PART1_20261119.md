# SDMx-BOP 2.6.0 Official DSD Capture and Legacy Compatibility Boundary
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 44, Part-1
Decision: **Official SDMx-BOP DSD V2.6.0 captured in both SDMX-ML 2.1 and 3.0; both parse successfully. Structural comparison against the archived IMF ECOFIN_DSD(1.0) shows a material model change (6 to 18 dimensions; 5 to 15 attributes). V2.6.0 is NOT an automatic replacement/crosswalk for legacy BOP6/BOP_BPM6.**

## Progress Log
### Reused evidence
- Reused immutable IMF structure archive from run `44533595369`, artifact `14534769007`, ZIP SHA-256 `4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e`.
- The archived legacy DSD is `IMF:ECOFIN_DSD(1.0)`, used by both legacy Dataflows `IMF:BOP6(1.0)` and `IMF:BOP_BPM6(1.0)`. Its direct component lists were parsed offline; no legacy source endpoint was re-fetched.
- Official SDMx maintenance policy: annual cycle; new DSD versions do not automatically invalidate prior versions; old versions are discontinued only rarely when backward compatibility cannot be assured. BOP V2.6.0 published December 2025; registry downloads are public without authentication.

## Official new DSD capture
- Source: `https://registry.sdmx.org/`, IMF-maintained DataStructure `IMF:BOP(2.6.0)`.
- Workflow run `44541286036`, SUCCESS; URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44541286036
- Artifact `14537633127`, `sdmx-bop-260-44541286036`, 5,062 bytes.
- ZIP SHA-256 (independently recomputed; matches GitHub digest): `b3475f7271324bf4577b5e99337c710e5defffe4f0244f1c8401e7b42b35e682`.
- SDMX-ML 2.1 response: HTTP 200, 30,286 bytes, XML parse PASS, SHA-256 `2b467382bc5a8dfaab3df9bccb18ac8326f52fb4111c197a54f94783a742c644`.
- SDMX-ML 3.0 response: HTTP 200, 25,602 bytes, XML parse PASS, SHA-256 `f54c4ca1beea49674481e75c009c9ebec24373091cdb1906faeb03973f626940`.
- Both identify exact maintainable `IMF:BOP(2.6.0)`; 2.1 and 3.0 are separate serialization representations of the same versioned DSD. Both raw bytes retained in the Actions artifact with retrieval UTC and hashes in manifest.

## Structural comparison: legacy ECOFIN_DSD(1.0) vs SDMx-BOP(2.6.0)
| Component | Legacy IMF:ECOFIN_DSD(1.0) | New IMF:BOP(2.6.0) |
|---|---:|---:|
| Dimensions including time | 6 | 18 |
| Non-time dimensions | 5 | 17 |
| Attributes | 5 | 15 |
| Primary measure | OBS_VALUE | OBS_VALUE |

Legacy dimensions (ordered): `DATA_DOMAIN, REF_AREA, INDICATOR, COUNTERPART_AREA, FREQ, TIME_PERIOD`.

New BOP 2.6.0 dimensions (ordered): `FREQ, ADJUSTMENT, REF_AREA, COUNTERPART_AREA, REF_SECTOR, COUNTERPART_SECTOR, FLOW_STOCK_ENTRY, ACCOUNTING_ENTRY, INT_ACC_ITEM, FUNCTIONAL_CAT, INSTR_ASSET, MATURITY, UNIT_MEASURE, CURRENCY_DENOM, VALUATION, COMP_METHOD, TYPE_ENTITY, TIME_PERIOD`.

Legacy attributes: `COMMENT, BASE_PER, UNIT_MULT, OBS_STATUS, TIME_FORMAT`.
New BOP attributes: `TIME_FORMAT, OBS_STATUS, CONF_STATUS, PRE_BREAK_VALUE, COMMENT_OBS, COMMENT_TS, TITLE, UNIT_MULT, DECIMALS, TIME_PER_COLLECT, REF_PERIOD_DETAIL, COMPILING_ORG, DATA_COMP, DISS_ORG, TITLE_COMPL`.

## Interpretation
- The new BOP DSD exposes a much richer dimensional model, including separate reference/counterpart sectors, flow/stock entry, accounting entry, functional category, instrument/asset, maturity, currency and valuation.
- The legacy IMF Dataflows `BOP6` and `BOP_BPM6` both still reference `ECOFIN_DSD(1.0)`; their separate Dataflow IDs and constraints remain distinct.
- Similar concepts such as `REF_AREA`, `COUNTERPART_AREA`, `FREQ`, `TIME_PERIOD`, and `OBS_VALUE` do not prove a complete dimension-level crosswalk. The new DSD's 18 dimensions cannot be mapped to the legacy 6-dimension structure by name matching alone.
- The public SDMx page explicitly states that prior DSD versions can remain valid and that changes do not automatically invalidate earlier versions. Thus BOP 2.6.0 is a new standard artefact, not evidence that IMF:BOP6(1.0) aliases IMF:BOP_BPM6(1.0), nor proof that the BCB XML payload should be relabelled.
- No country-specific Brazil PA migration, provider registration, BOP 2.6.0 crosswalk or migration notice was found in this capture.

## Acceptance matrix
| Gate | Status |
|---|---|
| Official BOP 2.6.0 SDMX-ML 2.1 capture | PASS |
| Official BOP 2.6.0 SDMX-ML 3.0 capture | PASS |
| Both XML parses | PASS |
| ZIP and raw hashes verified | PASS |
| Legacy DSD component baseline reused from archive | PASS |
| Legacy/new DSD structural difference quantified | PASS |
| BOP 2.6.0 adoption by Brazil PA/BR1 proven | NOT_FOUND / UNKNOWN |
| BOP6 vs BOP_BPM6 identity resolved | BLOCKED |
| Brazil Reconstruction 100% | NO — BLOCKED |
| GCR country coverage/vintage/BPM admission | BLOCKED / PARTIAL |

## Exact next action
1. Preserve the legacy Dataflow/PA identities and constraints as separate; do not alias or mutate payload.
2. If an authorized official BOP 2.6.0 Brazil migration record or BR1 PA is exposed in SDMx Global Registry, capture its exact PA/Dataflow/provider/constraint references and versioned mapping. No inferred bridge.
3. Keep the current IMF BR1 GUI Changelog/Compare route as the remaining authoritative PA revision evidence; its controls are visible in the public page, but static page retrieval does not expose selected record history.
4. GCR remains blocked pending country-vintage alignment, 154-member coverage policy and BPM basis reconciliation.

## Invariants
₹0; public official sources only; no synthetic mappings, aliases, guessed chronology or invented timestamps. No production integration, macro weights or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. UNKNOWN is not PASS.
