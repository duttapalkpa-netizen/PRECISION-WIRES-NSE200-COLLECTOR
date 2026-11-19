# GCR — IMF BOPS dataflow and constraint registry audit
Date: 2026-11-19 (Asia/Kolkata)
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Stage: Observation only
Status: LEGACY IMF BOP DATAFLOW FAMILY IDENTIFIED; INDIA-SPECIFIC DATA ROUTE NOT FOUND

## 1. Purpose
Continue Continuation 44 Part-1 using the current public IMF SDMX Central registry pages. Determine whether the registry exposes exact BOP-family Dataflow IDs and constraints, and whether an India-specific registration appears.

## 2. Official registry findings
### 2.1 Dataflow registry overview
Official page: https://sdmxcentral.imf.org/data/overview.html
- Public Dataflows overview is indexed and reachable.
- The visible first-page listing includes ESTAT quarterly `BPM6_BOP_Q` (version 2.6.0) and monthly `BPM6_BOP_M` (version 2.6.0). These belong to ESTAT, not IMF; they are not the IMF global BOP dataset and must not be substituted.
- The page reports 216 dataflow entries in the registry. Search-indexed first-page output is not a complete listing and does not establish that an IMF BOP global dataflow is absent.

### 2.2 IMF reporting constraints
Official page: https://sdmxcentral.imf.org/data/constraints.html
- The current public listing contains IMF agency constraint `BOP6_CONSTRAINT`, whose target dataflow is `BOP6[1.0]`.
- It separately contains `BOP_BP6_CONSTRAINT`, target dataflow `BOP_BPM6[1.0]`.
- These are exact registry-listed legacy IMF dataflow IDs and their constraints. They provide concrete structure-query targets, but they are not proof that either dataflow is the exact current IMF STA BOP dataset behind the current data.imf.org BOP landing page.
- The same page lists `BOP5_CONSTRAINT` targeting `BOP5_COLLECTION[1.0]`; this is BPM5-related and not suitable for the BPM6 sudden-stop replication unless the original source definition explicitly requires it.

### 2.3 Public registration list — India check
Official page: https://sdmxcentral.imf.org/data/registrations.html
- The visible listing includes national registrations for IMF BOP-family dataflows, including Brazil `IMF:BR1` and Chile `IMF:CL2` for `BOP6(1.0)`, and multiple countries under `BOP_BPM6` / `BOP_GBPM6`.
- No India provider/registration was visible in the reviewed public output. Because the page is paginated/indexed and the inspected output is not a complete machine-readable exhaustive query, absence is NOT proof that no India registration exists.
- The previously known Brazil BOP6 vs payload BOP_BPM6 mismatch remains a separate unresolved issue; this audit does not alter it.

## 3. What this narrows — and what it does not
- The registry provides two concrete IMF BPM6-era dataflow candidates: `IMF:BOP6(1.0)` and `IMF:BOP_BPM6(1.0)`.
- The public Data Structure listing still surfaces `IMF:BOP(2.6.0)`; no successful dataflow-to-DSD reference payload was captured to prove a relationship between these objects.
- No current India REF_AREA code, DSD dimension order, item/indicator code, frequency constraint, unit multiplier, sign convention or observation-status attribute was verified.
- No public IMF observation data query was executed. No raw quarterly observations or metadata payload bytes/hashes were acquired.
- The current IMF BOP dataset landing page describes quarterly and annual frequency but does not identify the SDMX dataflow in its visible text.

## 4. Next safe retrieval sequence
1. Use the public SDMX Central Structure UI/API to retrieve, separately and explicitly, IMF Dataflow `BOP6` version `1.0`, IMF Dataflow `BOP_BPM6` version `1.0`, Data Structure `BOP` version `2.6.0`, and the referenced constraints/codelists.
2. Preserve each exact raw response and metadata: final URL, HTTP status, content type, retrieval timestamp, byte count, SHA-256.
3. Inspect each Dataflow's actual DSD reference and constraint references. Do not assume the similarly named BOP DSD is linked.
4. Check whether either flow is the same product/data vintage as IMF STA BOP landing page. If not proven, classify as national SDDS/NSDP submission structures, not the global BOP dataset.
5. Search the complete provider/registration records for India only after the API or pagination contract is validated.
6. Do not attempt observation data retrieval until the exact DSD, dimension/codelist and dataflow are proven.

## 5. Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| Current public dataflow overview page reachable | PASS | IMF SDMX Central Dataflows overview |
| IMF BOP6 dataflow ID surfaced | PASS (registry identity only) | BOP6_CONSTRAINT targets BOP6[1.0] |
| IMF BOP_BPM6 dataflow ID surfaced | PASS (registry identity only) | BOP_BP6_CONSTRAINT targets BOP_BPM6[1.0] |
| Current global STA BOP dataflow identity | UNKNOWN | No verified dataflow-to-DSD/product link |
| Exact current DSD relationship/version | NOT_DONE | No live structure response |
| India registration exhaustively checked | NOT_DONE | Indexed visible listing is not exhaustive |
| India series codes / units / signs | NOT_DONE | No DSD/codelist payload |
| Raw India quarterly observations | NOT_ACQUIRED | No data query |
| Independent RBI sudden-stop replication | NOT_DONE | Requires validated raw series |

## 6. Decisions and invariants
- BOP6 and BOP_BPM6 are recorded as registry-listed candidates, not promoted as the target IMF STA global dataset.
- ESTAT BPM6_BOP_Q is a different agency's flow and is not substituted.
- No India absence claim from partial search output.
- Observation remains OPEN; Planning/Organizing remain NOT_STARTED.
- ₹0 spend; official/free sources only; no guessed keys, units, signs, transformations or missing-value handling.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged.
- UNKNOWN is never PASS. GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.

## 7. Next highest-value action
Retrieve the exact structure payloads for IMF:BOP6(1.0), IMF:BOP_BPM6(1.0), and IMF:BOP(2.6.0) through the public structure service or registry's built-in query UI; resolve their DSD/constraint relationships and codelists. Stop if the live response remains inaccessible; do not infer a global dataset mapping from names alone.
