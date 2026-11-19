# Brazil Asset-side Gross-flow Identity Audit — Continuation 45
Date: 2026-11-19 (UTC capture; Asia/Kolkata reporting)
Scope: research-only validation of BCB SGS 22906/22907/22908; no production change.

## Decision
PASS: the unique empirical identity is **22906 = 22908 - 22907** (net acquisition of financial assets = outflows minus inflows), not the reverse convention.

## Official series and raw capture
Source: Banco Central do Brasil / BCData SGS public API.
- SGS 22906: 381 monthly rows, 1995-01 to 2026-09; 14,594 bytes; SHA-256 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`.
- SGS 22907: 381 monthly rows, 1995-01 to 2026-09; 14,567 bytes; SHA-256 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`.
- SGS 22908: 381 monthly rows, 1995-01 to 2026-09; 14,593 bytes; SHA-256 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- All three HTTP 200, valid JSON arrays, 381 unique months each, exact common coverage 381/381.
- Metadata descriptions are explicitly recorded in the capture script; sign is not assumed from labels and both conventions are tested.

## Identity results
- Candidate A: `22906 = 22908 - 22907`: 381/381 within 0.15 USD million; maximum absolute residual 0.1 USD million.
- Candidate B: `22906 = 22907 - 22908`: 0/381; maximum absolute residual 17,048.8 USD million.
- Unique decision: `IDENTITY_PASS_NET_EQUALS_OUTFLOWS_MINUS_INFLOWS`.
- Tolerance 0.15 USD million is applied only because source values are recorded to one decimal place.
- This is a source-data reconciliation, not proof of causal capital flows or an investment signal.

## GitHub provenance
- Script: `scripts/research/validate_bcb_asset_flow_identity.py`.
- Script metadata-basis documentation commit: `90b1a68aa5c5a36f88293e4c857530268101a86c`.
- Workflow: `.github/workflows/bcb_asset_flow_identity.yml`, run #2.
- Run ID: `44542505681`; SUCCESS; job ID `135624309676`.
- Artifact ID: `14538393352`; name `bcb-asset-identity-44542505681`; size 16,753 bytes.
- Artifact ZIP SHA-256: `51ab88b418ebbaa88595a45eb2a94cf8507c454c3c637075b935c8de07dcf762`.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44542505681

## Failure lesson retained
The earlier exploratory workflow run `44542407481` failed its identity gate because it used an incorrect assumed sign convention; it nevertheless captured all three 381-row series and uploaded artifact `14537174964` (ZIP SHA-256 `102a1d135fceb52493e4fe93f7194dfa99e2a977371487c5a2abf51d9cd7dbf4`). Its reported maximum residual 170,488 was from that wrong formula and is not a data-quality failure. Do not repeat the same assumed-sign test. The replacement validator tests both signs and rejects the reverse one.

## Boundary / remaining gates
- Asset-side identity is now independently reconciled alongside the previously completed liability-side identity.
- Brazil Reconstruction remains BLOCKED by the IMF PA/Dataflow mismatch and missing authoritative Brazil PA revision/history evidence; this identity does not close those registry gates.
- GCR remains BLOCKED pending synchronized multi-country coverage, vintage/sign/basis gates, global benchmark TRI, formula/no-lookahead tests, sector transmission and matured out-of-sample event study.
- No BOP6/BOP_BPM6 alias, no BOP 2.6.0 crosswalk, no production integration, no macro weights, no trading admission.
- ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. UNKNOWN is not PASS.

## Reproducibility
Run: `python scripts/research/validate_bcb_asset_flow_identity.py`.
The workflow captures raw JSON, retrieval timestamps, HTTP metadata, byte counts, SHA-256, monthly identity CSV and manifest. Artifact retention: 90 days.
