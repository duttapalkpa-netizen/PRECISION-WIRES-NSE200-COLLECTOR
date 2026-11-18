# IMF SDMX Central RSS + Brazil XML Retrieval — Part 2
Audit date: 2026-11-18 (Asia/Kolkata)
Continuation: গবেষণা যাচাই অব্যাহত 36
Scope: isolated GitHub Actions retrieval workflow prepared; execution/result verification pending.

## 1. Prior evidence reused
Part 1: `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART1_20261118.md`
Part 1 report commit: `80c93853f0abf90e985d6b54cb6be893cd9963e8`
Part 1 master-ledger update: `7ebf107aa973d5a8e5158a951925297f90c16798`

Preserved facts:
- Official RSS endpoint: https://sdmxcentral.imf.org/rss.xml
- Official IMF registration listing previously showed Brazil row IMF:BOP6(1.0), provider IMF:BR1, registered BCB XML URL and Last Updated 2026-10-26T11:47:29.000Z.
- Prior screenshot records BCB header/Dataflow mismatch CONFIRMED.
- RSS retrieval and raw XML validation were NOT_RETRIEVED / NOT_DONE. No PASS inherited.

## 2. New isolated workflow
Created:
`.github/workflows/imf_sdmx_rss_registration_audit.yml`

Commit: `2e5361d2ef46d4ae7b052f0846c8c5e78fe7d430`
Blob SHA: `82c35eec26a2fd93797c7325553cb727fef04c29`
Verified by fetching the committed file back from GitHub. It contains:
- workflow_dispatch trigger and a narrowly scoped push trigger on this workflow file;
- contents:read permission only;
- one ubuntu-latest job with timeout-minutes: 8;
- standard-library urllib retrieval of IMF RSS and the registered BCB XML;
- response final URL, HTTP status, Content-Type, retrieval timestamp, byte count and SHA-256 capture;
- raw XML preservation when a body is received;
- XML parsing and extraction of RSS item fields and BCB DataflowRef / ProviderRef elements;
- machine-readable summary.json;
- upload of evidence as a 90-day GitHub Actions artifact, including failed retrieval diagnostics.

## 3. Execution status — do not overclaim
The workflow definition was committed and fetched back successfully.
The GitHub workflow-run listing could not be read through the available read interface in this audit. Therefore:
- workflow execution: NOT_VERIFIED;
- run ID: NOT_AVAILABLE;
- RSS retrieval: NOT_RETRIEVED_PENDING_RUN;
- BCB XML retrieval: NOT_RETRIEVED_PENDING_RUN;
- raw XML hashes: NOT_AVAILABLE;
- artifact ID: NOT_AVAILABLE;
- XML validation: UNKNOWN.
A committed workflow is not a successful workflow run. Do not mark retrieval PASS until a completed run and artifact are inspected.

## 4. Known transport limitation
Direct browser retrieval of the RSS endpoint failed in this research interface with an internal/access error. Direct browser opening of the BCB XML failed because the browser interface does not support text/xml. These are limitations of the browser retrieval interface, not proof that either official endpoint is down. The isolated GitHub Actions runner is intended to perform the raw HTTP request.

## 5. Acceptance matrix
| Check | Status |
|---|---|
| Part 1 evidence reused | PASS |
| Isolated workflow definition committed | PASS |
| Workflow file fetched back / blob verified | PASS |
| Workflow run ID and status independently verified | NOT_VERIFIED |
| IMF RSS raw response + SHA-256 | NOT_DONE |
| BCB XML raw response + SHA-256 | NOT_DONE |
| RSS parse and event extraction | UNKNOWN |
| BCB DataflowRef / ProviderRef validation | UNKNOWN |
| Historical Brazil registration event reconstructed | UNKNOWN |
| EM flow / trading admission | NOT_AUTHORIZED |

## 6. Next action after execution
1. Inspect the workflow run triggered by commit `2e5361d2ef46d4ae7b052f0846c8c5e78fe7d430`.
2. If the push trigger did not fire, ask the repository owner to use the workflow's workflow_dispatch control; this audit connector has no workflow-dispatch write operation.
3. Inspect the artifact summary and raw files; independently recompute SHA-256 from downloaded bytes.
4. If RSS returns valid XML, inspect actual items and follow only an actual registration event link; never fabricate an event.
5. Validate BCB XML references against IMF registry dataflow/provider identifiers. Preserve exact values and namespaces.
6. If the job fails, keep diagnostics and make only a minimal isolated fix; do not run the 60-minute NSE collector workflow.

## 7. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12) and Engines A–E remain unchanged. No PR merge, production integration, paid API, synthetic data, guessed timestamp, guessed XML identifier, or trading admission.
