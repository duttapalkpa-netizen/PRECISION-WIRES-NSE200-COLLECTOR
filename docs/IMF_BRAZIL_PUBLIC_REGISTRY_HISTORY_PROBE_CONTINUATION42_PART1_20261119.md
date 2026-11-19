# Brazil IMF Public Registry Transaction-History Probe
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 42, Part-1
Decision: **Public transaction-history endpoint is reachable and returns one structure transaction for the Brazil PA and both BOP Dataflows. This is partial registry evidence, not a complete Brazil registration chronology. Brazil Reconstruction remains BLOCKED.**

## Progress Log
### Reused / completed
- Reused existing Brazil PA URN `IMF:BR_BOP_BP6(1.0)`, registered Dataflow `IMF:BOP6(1.0)`, and the separately declared BCB payload Dataflow `IMF:BOP_BPM6(1.0)`. No repeated SDMX structure downloads.
- Reused known IMF registry page current BR1 row (last updated 2026-10-26T11:47:29Z) and earlier UAT snapshot (2026-09-28T12:11:30Z) only as separate current-page snapshots; neither is full registration history.
- Found documented public Fusion Registry transaction endpoint `/ws/registry/tx/history?urn=...`. Documentation says public, returns date, transaction ID and action; administrator authentication adds user identity.

## GitHub run and artifact
- Research-only script: `scripts/research/probe_imf_brazil_public_tx_history.py`
- Workflow: `.github/workflows/imf_brazil_public_tx_history.yml`
- Run ID `44539721149`, SUCCESS; URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44539721149
- Artifact ID `14537831415`, name `imf-brazil-public-tx-history-44539721149`, size 1,946 bytes.
- ZIP SHA-256, independently recomputed and matching GitHub digest: `042b32108ccbf42dc906af2b616ce7d5a91abdf5065448c8b96abcec9a5ccf0e`.
- Manifest SHA-256: `3003c20193b5c5518e09555e125c9f91a467cc430f713008d617bfeb91c4af2b`.

## Raw results
Three public history queries returned HTTP 200 and byte-identical 80-byte JSON:
`[{"Date":1695371169491,"Id":2,"Action":"Replace","Type":"Structure Submission"}]`
- PA URN: `urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)`
- Dataflow URN: `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP6(1.0)`
- Dataflow URN: `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0)`
- All three bodies: 80 bytes, SHA-256 `335149e69147d8b99c9c6b5d0303cdb3b72401510b5bfed64cb3f519ced0b411`.
- Transaction timestamp converts to **2023-09-22 08:26:09.491 UTC**. Action: Replace. Type: Structure Submission. Transaction ID: 2.
- This is one shared registry structure transaction returned for each of the three maintainables. It does not establish three independent submissions or a country-specific PA registration event.

## Important boundary / failed detail lookup
- The transaction-detail endpoint returned HTTP 500, body 88 bytes: `When querying for transaction, the parameter 'txId' must be specified with a legal value`; SHA-256 `4a83e68fc334d09b4bb7d5d1229abbb4880b8cc21ee39bb6e323fc09bc49430f`.
- The probe used `transactionId=2`; response indicates the endpoint expects `txId`. Do not retry txId=2 blindly: prior research already recorded HTTP 500 for transaction ID 2 fusion-json and sdmx-json requests. Keep this as an unresolved public-service detail boundary; no guessed retry or authenticated request.
- The public transaction history is the maintainable structure history. It does not expose the data registration history or PA-to-payload association chronology needed to reconcile the current BR1 registration.
- Current registration listing still reports BOP6 / BR1, source URL BCB, last updated 2026-10-26T11:47:29Z. This later date is not proven to be a registration event date by the history response.

## Acceptance matrix
| Gate | Status |
|---|---|
| Public transaction-history endpoint reachable | PASS |
| Brazil PA history query HTTP 200 | PASS |
| BOP6 and BOP_BPM6 Dataflow history queries HTTP 200 | PASS |
| Raw responses and retrieval metadata archived | PASS |
| Artifact digest independently verified | PASS |
| One shared structure transaction identified | PASS |
| Detailed transaction XML retrieved | BLOCKED (HTTP 500; no retry) |
| BR1 data-registration event chronology | BLOCKED / NOT_EXPOSED |
| PA-to-payload Dataflow identity resolved | BLOCKED |
| Brazil Reconstruction complete | NO — BLOCKED |

## Exact next action
- Use the public `getAllUrns` and `searchTransactions` read-only endpoints only if needed to determine whether any public Registration maintainable/event identifiers exist; archive raw responses and filter locally. Do not repeat transaction-ID-2 detail calls.
- If registration events are not publicly exposed, the remaining dependency is an official owner-side IMF SDMX Central export of Data Registrations / View Activity / transaction XML or provider-supplied history. No credentials, cookies, API keys or external contact.
- Continue to keep `BOP6` and `BOP_BPM6` distinct until authoritative crosswalk or registration evidence resolves them.

## GCR and production status
- This probe does not close GCR country coverage, vintage or BPM-basis gates. Keep Chile 2026-Q1/Q2 as REVIEW_VINTAGE_MISMATCH; 40 countries without observations, 83 empty country-entry cells and 13 interior gaps remain explicit.
- No aggregate or relative-attraction score; no production admission. ₹0. No synthetic rows, guessed chronology or fabricated hashes. UNKNOWN is not PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged.
