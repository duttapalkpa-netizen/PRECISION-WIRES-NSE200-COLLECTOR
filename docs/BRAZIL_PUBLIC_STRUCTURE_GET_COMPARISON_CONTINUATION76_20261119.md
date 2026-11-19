# Brazil Public Structure GET Comparison — Continuation 76
Date: 2026-11-19 (Asia/Kolkata)
Scope: bounded, read-only IMF SDMX Central structure comparison; no production change.

## Progress Log

### Completed / reused
- Continuation 75 accepted as baseline; no completed lifecycle/archive replay repeated.
- Brazil Registration lifecycle: 40/40 PASS (run 44465947951; artifact 14502380926; ZIP SHA-256 2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41).
- Brazil PA identity is confirmed as IMF:BR_BOP_BP6(1.0), referencing Dataflow IMF:BOP6(1.0) and Provider IMF:BR1.
- Current BCB XML declares IMF:BOP_BPM6(1.0); mismatch remains unresolved. Do not alias or rewrite.
- PA transaction ID 2 alternate serialization probe: 2/2 requests executed, both HTTP 500; exact 39-byte error body SHA-256 76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825. Do not repeat these endpoints.
- GCR CDSL archive replay: run 44521501249 SUCCESS; artifact 14527843295; ZIP SHA-256 2c8952476f58637c0f346e695793d2b8c8fd170dac551386ace1e37e0e7aea99; archive completeness remains BLOCKED because same URL returned materially different date-selected bodies.

### New evidence-based design decision
The IMF SDMX Central Web Services Guide (May 2025) documents:
- Public structure queries use GET under https://sdmxcentral.imf.org/sdmx/v2/.
- Structure query blueprint is /structure/{resource}/{agencyID}/{resourceID}/{version}/ with optional references and format parameters.
- The guide's BOP example explicitly distinguishes Dataflow IMF:BOP_BPM6(1.0) from DATA_DOMAIN BOP6.
- Registration/re-registration is a separate private authenticated POST operation.
Sources:
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- https://sdmxcentral.imf.org/data/registrations.html
- https://sdmxcentral.imf.org/data/constraints.html

Interpretation boundary: this namespace distinction is verified in the guide, but it does NOT prove that the Brazil registry registration IMF:BOP6(1.0) is equivalent to IMF:BOP_BPM6(1.0), nor resolve the BCB payload mismatch.

### New bounded implementation
- Updated scripts/research/probe_imf_brazil_pa_structure_revision.py to add four public, read-only XML GETs:
  1. Brazil PA IMF:BR_BOP_BP6(1.0), references=all
  2. Dataflow IMF:BOP6(1.0), references=all
  3. Dataflow IMF:BOP_BPM6(1.0), references=all
  4. DataStructure IMF:ECOFIN_DSD(1.0), references=all
- Existing transaction-ID-2 JSON requests remain in the script for provenance only; prior known HTTP 500 results are not to be reinterpreted as missing PA evidence.
- Each response is archived with UTC retrieval time, HTTP status, safe headers, byte count, SHA-256 and parsed XML root/reference attributes.
- Script commit: c1365fbbccbd773d7ad61dd1fdfc42138c4af98e.
- Trigger marker commit: 786ac4a64ea8ab412c41907c0e1afe1e46d8dcb5.
- Workflow: .github/workflows/imf_brazil_public_api_probe.yml; 8-minute timeout.
- Trigger commit includes [PA-TX2-ONLY] to skip already completed Brazil lifecycle/history capture steps. Workflow run/artifact has NOT yet been independently verified in this checkpoint. Do not claim execution PASS or structure comparison results until the Actions run and raw artifact are inspected.
- NSE collector paths-ignore was checked to include both the Brazil probe workflow and script/trigger paths, avoiding an accidental full NSE collector run.

## Current acceptance status
| Workstream | Status | Evidence / reason |
|---|---|---|
| Brazil Registration lifecycle | PASS | 40/40 prior verified |
| Brazil PA identity | PASS | PA -> BOP6 + BR1 confirmed |
| Brazil PA transaction-2 Changelog | BLOCKED | two documented formats returned HTTP 500 |
| Brazil BOP6 vs BOP_BPM6 payload identity | BLOCKED | no authoritative Brazil-specific crosswalk or correction evidence |
| Public structure GET comparison | PENDING | new workflow trigger committed; run/artifact not inspected |
| GCR CDSL archive replay integrity | PASS | run/artifact digest verified |
| GCR CDSL archive completeness | BLOCKED | three inconsistent HTTP-200 bodies from same URL |
| NSDL/CDSL matched-date reconciliation | NOT_DONE | reporting dates differ |
| GCR predictive event study | NOT_DONE | synchronized accepted panel unavailable |
| Production integration | BLOCKED | no source/coverage/event-study acceptance |

## Exact next actions
1. Inspect the workflow run created by trigger commit 786ac4a64ea8ab412c41907c0e1afe1e46d8dcb5; capture run ID, terminal conclusion, job steps and artifact ID.
2. Download and independently verify the artifact ZIP digest; validate raw response hashes against manifest.
3. Compare exact PA, Dataflow BOP6, Dataflow BOP_BPM6 and DSD references. If the API returns errors or missing structures, record them and stop equivalent retries.
4. For CDSL archive, inspect raw page scripts and documented date selector/GET links; do not POST until request semantics are documented.
5. Brazil owner-side PA revision/changelog export remains a distinct external evidence dependency; no credentials or cookies requested.
6. Build GCR accepted panel only after raw date-aligned provider series, schema, status and source-vintage checks.

## Hard invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed hashes, interpolation, unapproved crosswalk or aliases. UNKNOWN is never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged. No PR merge, production integration, macro weights or trading admission without explicit approval.
