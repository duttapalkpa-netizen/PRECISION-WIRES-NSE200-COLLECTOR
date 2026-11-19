# Brazil PA transaction 2 — alternate serialization probe (Part 1, 2026-11-19)

## Purpose
The exact Brazil registration lifecycle is now captured, but the linked Provision Agreement (PA) structure transaction ID 2 / dated Changelog payload remains unresolved. Prior probes reported HTTP 500 for the whole transaction and HTTP 400 for PA/Dataflow/DSD/Provider item ZIP requests. Do not reinterpret these errors as evidence that the PA did not exist.

## Evidence preserved before this probe
- Exact Brazil Registration URN: `urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`.
- Registration ID: `D429E36CD161E2F2A34ECAF137994E89`.
- PA: `IMF:BR_BOP_BP6(1.0)`; provider `IMF:BR1`.
- Registration history: 40/40 events and 40/40 transaction item XMLs parsed; run 44465947951, artifact 14502380926, ZIP SHA-256 `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`.
- Registry Action is Replace for all 40 events; embedded RegistrationRequest action is Information for all 40. Keep these separate.
- PA/dataflow identity conflict remains: registry PA references `IMF:BOP6(1.0)`, while BCB payload declares `IMF:BOP_BPM6(1.0)`. Existing compatibility evidence is 234/237 vs 27/237; no alias or admission is authorized.

## New probe implementation
The read-only script `scripts/research/probe_imf_brazil_pa_structure_revision.py` was extended to request transaction 2 in two additional representations:
1. `/ws/registry/tx/transactions?txId=2&format=fusion-json`
2. `/ws/registry/tx/transactions?txId=2&format=sdmx-json`

For HTTP 200 JSON responses, the script records parse status, top-level keys, and counts/IDs for ProvisionAgreement, Dataflow, DataStructure, DataProviderScheme, DataProvider and Registration objects. Existing ZIP and current-structure probes are retained. The probe sends no credentials/cookies and performs no registry mutation.

- Script commit: `5230a74409a96555fe0f598cd5258f55f42ed11a`.
- Trigger marker commit: `032a1871a9713f7330ebaad6455597393639eec3`.
- Production collector path-ignore was verified to include the trigger marker path before dispatch.

## Execution status
**IMPLEMENTED / DISPATCH TRIGGER COMMITTED — RUN RESULT NOT YET VERIFIED.** Do not mark PA history or Brazil Reconstruction PASS until the workflow artifact is independently inspected and the PA URN, structure content and dated revision evidence are actually present.

## Acceptance criteria for the next checkpoint
- Confirm the workflow run created by trigger commit `032a1871a9713f7330ebaad6455597393639eec3`.
- Inspect both alternate endpoint status codes, raw bytes, timestamps, headers, byte counts and SHA-256.
- If either response is 200, parse it and reconcile exact PA URN, Dataflow and revision/changelog content.
- If both fail, record the exact observed errors and stop repeating equivalent endpoints; Brazil remains BLOCKED pending official PA Changelog/structure evidence.
- Preserve all Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E invariants; UNKNOWN is not PASS; spend ₹0.
