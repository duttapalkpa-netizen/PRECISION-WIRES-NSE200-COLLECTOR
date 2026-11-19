# Brazil BOP Dataflow Identity — Public Structure Artifact Audit, Continuation 39 Part-5
Date: 2026-11-19 (Asia/Kolkata)
Scope: independent inspection of the already-triggered read-only IMF SDMX Central structure comparison. No endpoint retries, no authenticated operation, no production changes.

## Executive decision
**Public structure retrieval and XML parsing: PASS (4/4). Brazil dataflow identity: still BLOCKED / UNRESOLVED.**
The exact Brazil Provision Agreement (PA) is confirmed as `IMF:BR_BOP_BP6(1.0)`, with `StructureUsage -> IMF:BOP6(1.0)` and `DataProvider -> IMF:BR1`. The returned BOP6 Dataflow is explicitly named “Balance of Payments (BPM6) for Collection”. The distinct `IMF:BOP_BPM6(1.0)` Dataflow is named “Balance of Payments -- BPM6”. Both reference the same `IMF:ECOFIN_DSD(1.0)`, but they remain different Dataflow maintainables with different IDs and separate constraints. Shared DSD and similar labels do not prove identity, aliasing, or authorization to rewrite the BCB payload header.

The existing BCB payload declares `IMF:BOP_BPM6(1.0)`; the current Brazil PA still references `IMF:BOP6(1.0)`. The discrepancy is now better characterized as a collection-flow vs BPM6 reporting-flow identity conflict, but no official Brazil-specific crosswalk or correction was found. Keep Brazil admission BLOCKED.

## Progress Log
### Completed / reused
- Reused prior Brazil registration lifecycle: 40/40 events and transaction item XMLs parsed (run 44465947951; artifact 14502380926; ZIP SHA-256 `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`). No repeat.
- Reused known transaction ID 2 serialization probe: fusion-json and sdmx-json both HTTP 500; do not repeat.
- Triggered public structure GET comparison (four exact resources) with commit `786ac4a64ea8ab412c41907c0e1afe1e46d8dcb5`.
- Workflow run `44533595369`, run #36, completed SUCCESS at 2026-11-19T13:32:11Z. Workflow `.github/workflows/imf_brazil_public_api_probe.yml`; job `probe` completed SUCCESS. The two already completed lifecycle capture steps were intentionally skipped; structure probe and RSS capture succeeded; artifact upload succeeded.
- Artifact ID `14534769007`, name `imf-brazil-public-api-probe-44533595369`, 7,648,050 bytes. GitHub artifact digest and independently recomputed ZIP SHA-256 both `4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e`.

### Raw response integrity
All four public structure responses returned HTTP 200, application/xml, and parsed as SDMX 2.1 `message:Structure` XML. The original uncompressed response sizes exceed the compressed artifact size; raw bytes were retained inside the artifact.
| Response | Bytes | SHA-256 |
|---|---:|---|
| Brazil PA | 42,896,179 | `b4343e43bbf82047a011bfa813f6bafc5149f8ff03132fa736ba2b037a56ded2` |
| Dataflow BOP6 | 43,071,271 | `4b5c1028534487f0b96da66ae57bf1f26a53cdf5b87f78127dbcdf0b012d1a98` |
| Dataflow BOP_BPM6 | 42,908,746 | `7cc596edeffc0819b068829a605c2f5514726fcc859bf84498ecaeef38c73be4` |
| DataStructure ECOFIN_DSD | 42,905,001 | `d0b6a3301683a7dd4b4207982944ebdc904bc9092fa980dffda8f626ac94bc30` |
- Manifest SHA-256: `10f0dd5bb1c007d8dd0cc35cd79d87bb00c800c6748fa9c30cf617c1337351d9`.
- RSS response: HTTP 200, 28,299 bytes, SHA-256 `001b7fe9bb5fba306d5d478f35f5b7fd598ffa270954e1025d1136e43a1a2b6d`; XML parse PASS, feed 31 entries, Brazil match 0. This only closes the captured current RSS window, not historical chronology.

## Exact structural findings
### 1. Brazil PA
- Maintainable: `IMF:BR_BOP_BP6(1.0)`, name “Brazil Balance of Payments”.
- `StructureUsage` explicitly references Dataflow `IMF:BOP6(1.0)`.
- `DataProvider` explicitly references `IMF:DATA_PROVIDERS(1.0).BR1`.
- The same BOP6 Dataflow response also includes other PAs under BOP6, including Chile `IMF:CL_BOP(1.0)` -> provider CL2 and IMF `IMF:IMF_BOP6(1.0)` -> provider IMF. This proves BOP6 is not a Brazil-only ID; it does not establish any mapping to BOP_BPM6.

### 2. Dataflow identity
- `IMF:BOP6(1.0)`: English name “Balance of Payments (BPM6) for Collection”; references `IMF:ECOFIN_DSD(1.0)`.
- `IMF:BOP_BPM6(1.0)`: English name “Balance of Payments -- BPM6”; references `IMF:ECOFIN_DSD(1.0)`.
- These are separate maintainables with distinct URNs and IDs. The shared DSD is a shared schema basis, not a Dataflow alias.
- Separate allowed constraints are returned:
  - `IMF:BOP6_CONSTRAINT(1.0)` under BOP6 response.
  - `IMF:BOP_BP6_CONSTRAINT(1.0)` under BOP_BPM6 response.
- Prior compatibility test remains 234/237 (98.7342%) for BOP6 vs 27/237 (11.3924%) for BOP_BPM6. Do not treat these as equivalent or silently swap.
- The BCB payload header still declares `IMF:BOP_BPM6(1.0)`; PA currently references `IMF:BOP6(1.0)`. Neither the common DSD nor the “BPM6” wording overrides this exact reference conflict.

### 3. Transaction item and RSS boundary
- Both documented transaction-ID-2 formats again returned the same HTTP 500 body “Unable to return transaction for id '2'” (39 bytes; SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`). This is recorded as a known failure; no more equivalent retries.
- RSS capture has 31 entries and zero Brazil matches. It cannot prove there were no older or unlisted Brazil events.

## Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| Four public structure GETs | PASS | 4/4 HTTP 200, XML parse PASS |
| Raw response provenance | PASS | bytes, UTC, headers, SHA-256 in manifest |
| Brazil PA -> BOP6 | PASS | exact StructureUsage ref |
| Brazil PA -> BR1 | PASS | exact DataProvider ref |
| BOP6 and BOP_BPM6 are distinct IDs | PASS | exact maintainable URNs/IDs |
| Both reference ECOFIN_DSD | PASS | exact DSD refs |
| BOP6/BOP_BPM6 equivalence or alias | BLOCKED / NOT_PROVEN | shared DSD is insufficient; constraints differ |
| BCB payload vs Brazil PA identity | BLOCKED | BCB header BOP_BPM6 vs PA BOP6 |
| Brazil PA transaction-2 Changelog | BLOCKED | two documented serializations HTTP 500 |
| Full PA revisions / registration chronology | NOT_DONE | owner-side PA changelog and exact event export required |
| Brazil production/admission | BLOCKED / NOT_AUTHORIZED | identity and chronology gates open |

## Highest-value next action
Do not spend more time on equivalent public GETs. The only evidence path that can resolve the remaining Brazil-specific identity/chronology question is an authorized IMF/BCB provider-side export:
1. Exact PA `IMF:BR_BOP_BP6(1.0)` Revisions/Changelog/Compare/View export.
2. Registration detail for exact provider `IMF:BR1`, including dated transaction IDs, actions, Dataflow, PA and Data URL.
3. An official Brazil-specific mapping/correction note, if the provider confirms BOP6 collection registration intentionally accompanies a BOP_BPM6 payload.
No passwords, session cookies, or tokens should be shared. Do not perform registration/re-registration or any authenticated write.

## Invariants
₹0; official/free sources only. No synthetic observations, guessed IDs, fabricated timestamps, aliases, or inferred chronology. UNKNOWN is not PASS. No PR merge, production integration, macro weights, trading admission, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
