# Brazil PA transaction 2 — alternate serialization probe (Part 2, 2026-11-19)

## Outcome
**Probe execution PASS; PA transaction payload retrieval BLOCKED.** The exact transaction ID 2 endpoint was tested in both documented JSON serializations. Both returned the same HTTP 500 body; no PA structure or dated Changelog was returned.

## Scope and method
Read-only public IMF SDMX Central requests; no credentials, cookies, POSTs, registry changes, or paid APIs. The focused workflow skipped the already completed registration lifecycle/history steps and ran only the two transaction-ID-2 serialization requests.

- Fusion-JSON: `GET https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=2&format=fusion-json`
- SDMX-JSON: `GET https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=2&format=sdmx-json`

## Independently inspected raw results
| Field | Fusion-JSON | SDMX-JSON |
|---|---|---|
| HTTP status | 500 | 500 |
| Retrieval UTC | 2026-11-19T09:07:18.953391Z | 2026-11-19T09:07:23.412058Z |
| Content-Type | application/zip | application/zip |
| Body bytes | 39 | 39 |
| Body | `Unable to return transaction for id '2'` | Same |
| Raw SHA-256 | `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825` | Same |

The Content-Type says application/zip, but the actual 39-byte body is the plain-text error above. It must not be treated as a ZIP or as a valid JSON response.

## Reproducibility receipt
- Workflow run #34 / ID `44493473476`: SUCCESS.
- Workflow URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44493473476
- Artifact ID `14513337963`, name `imf-brazil-public-api-probe-44493473476`, 1,275 bytes.
- Artifact ZIP SHA-256: `824a09425db76982ba73a1b9f51cd768669d560a5b017b732f0cf224ce7720e6`.
- Manifest SHA-256: `994aa5f6b7e5ce7bb5257097a51f7d94a2cfbaf6b55eee1cdfbc2202260ef987`.
- Both raw response files are 39 bytes and have the SHA-256 above.
- Probe script narrowed to the two documented JSON formats only; timeout 15 seconds per request. Script commit `46bd48fcaecc6d866061d21f9151508bf841afb7`.
- Workflow focused-mode correction commit `e96942c1d809dd36a6c596621a967e8668af8444`; trigger commit `431006c2893cb6882b33edd9fc3465b8602febf4`.

## Interpretation
FMR documentation describes both `fusion-json` and `sdmx-json` as valid format options for the general transaction endpoint, but the IMF deployment returned HTTP 500 for transaction ID 2 in both. This is a transaction-specific retrieval/serialization failure, not proof that the PA or its Changelog never existed.

The previously established exact PA, provider, Registration URN and 40-event Registration lifecycle remain valid. This probe does not resolve the separate Dataflow identity mismatch:
- PA registry reference: `IMF:BOP6(1.0)`
- BCB payload declaration: `IMF:BOP_BPM6(1.0)`
- Prior compatibility counts: BOP6 234/237; BOP_BPM6 27/237.
No aliasing, rewriting, or Brazil admission is authorized.

## Next evidence route — no duplicate endpoint retries
Use the official Registry UI's Activity / Structure Submissions and Data Registrations / Provision Agreement detail views. FMR's documented UI exposes transaction downloads, details/log CSV, historical structure revisions and PA Changelog/Compare views. Capture only the exact Brazil PA row and actual downloadable revision files with source URL, UTC retrieval time, and SHA-256. If the IMF UI does not expose the PA history without authorized access, record that limitation and leave the historical PA chronology UNKNOWN. Do not use the FMR v12 `asOf` time-travel feature against IMF SDMX Central v11.24.0.

## Acceptance decision
- Alternate serialization probe: PASS (2/2 requests executed and raw responses archived).
- PA transaction 2 payload / PA Changelog: BLOCKED (2/2 HTTP 500).
- Brazil Reconstruction: BLOCKED.
- BOP6/BOP_BPM6 identity reconciliation: BLOCKED.
- No production selector, ranking score, pressure-fade, CORE-672 or Engines A–E changes. UNKNOWN is not PASS. Research spend ₹0.
