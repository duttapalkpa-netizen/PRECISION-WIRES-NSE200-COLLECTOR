# GCR / Brazil — BOP 2.6.0 Migration Boundary Check
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 40, Part-1
Scope: read-only official registry and existing GitHub evidence reconciliation. No production or collector code changes.

## Progress Log — reused evidence, no repeated audit
- Brazil registration lifecycle: 40/40 PASS (run 44465947951; artifact 14502380926; ZIP SHA-256 2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41).
- Brazil national-source scale/sign benchmark: current superseding count 94/94 Brazil, 12/12 India, 6/6 Mexico, 6/6 Chile; vintage-aligned combined 118/118. Does not authorize 154-country admission.
- Official SDMx-BOP DSD v2.6.0: SDMX-ML 2.1 and 3.0 captures and XML parsing PASS. Reused report: docs/SDMX_BOP_260_LEGACY_ECOFIN_COMPATIBILITY_AUDIT_CONTINUATION44_PART1_20261119.md; run 44541286036; artifact 14537633127; ZIP SHA-256 b3475f7271324bf4577b5e99337c710e5defffe4f0244f1c8401e7b42b35e682.
- The legacy/new structural comparison remains 6 vs 18 dimensions and 5 vs 15 attributes. Shared concepts do not establish a full crosswalk.
- Brazil PA currently references IMF:BOP6(1.0), provider IMF:BR1; BCB payload declares IMF:BOP_BPM6(1.0). These are distinct Dataflow maintainables, even though both reference IMF:ECOFIN_DSD(1.0). The discrepancy remains unresolved.
- Do not repeat transaction-ID-2 fusion-json or sdmx-json requests; both prior documented requests returned HTTP 500.
- The earlier exact legacy IMF.STA DSD 24.0.0 / BOP 21.0.0 structure requests returned SDMX error 404 No Results Found through the tested routes. Those attempts are not metadata captures and must not be re-labelled as success.

## New live official page observations (read-only)
1. IMF SDMX Central registrations page:
   https://sdmxcentral.imf.org/data/registrations.html
   The rendered registration listing includes IMF:BOP6(1.0) with provider IMF:BR1 and the BCB registered URL. The listing does not show a Brazil registration against IMF:BOP(2.6.0). This is a rendered-page observation only; absence from this listing is not proof that no private or unpublished migration record exists.
2. IMF SDMX Central Data Structure listing:
   https://sdmxcentral.imf.org/data/datastructure.html
   Lists IMF:BOP version 2.6.0 as the current public structure.
3. IMF SDMX Central Dataflows overview:
   https://sdmxcentral.imf.org/data/overview.html
   The visible BOP 2.6.0 dataflows include ESTAT-maintained BPM6_BOP_M(2.6.0), BPM6_BOP_Q(2.6.0), and BPM6_ITS_A(2.6.0). These are not evidence of an IMF:BR1 Brazil provision or Brazil observations.
4. SDMx Global Registry schema guide:
   https://registry.sdmx.org/webservice/schema.html
   Public REST structure service entry point is https://registry.sdmx.org/sdmx/v2/. Provision Agreement structure is a distinct maintainable type. No Brazil-specific 2.6.0 migration record was established in this read-only check.

## Decision
- New official BOP 2.6.0 DSD capture: PASS (existing archived evidence).
- Public rendered IMF SDMX Central listing confirms Brazil currently appears under IMF:BOP6(1.0) / IMF:BR1.
- Brazil adoption of IMF:BOP(2.6.0): NOT_FOUND_IN_RENDERED_LISTING / UNKNOWN, not a global absence claim.
- Brazil BOP6 vs BOP_BPM6 identity: BLOCKED.
- Legacy IMF Data Portal v24.0.0 ↔ Global Registry v2.6.0 crosswalk: NOT_DONE / BLOCKED.
- No new Brazil observations, no migration record, no new raw archive or hashes were acquired in this check.
- No GCR country admission, aggregation, macro weighting, or production use is authorized.

## Exact next bounded actions
1. Use the IMF SDMX Central Provision Agreement GUI's Changelog/Compare and View Provision Agreement controls for the exact PA IMF:BR_BOP_BP6(1.0), recording the selected record, revision identifiers, exact exported XML/CSV, retrieval UTC, bytes and SHA-256. If an authenticated owner-only export is required, do not bypass access; request the authorized provider to supply the export.
2. Capture the exact legacy IMF Data Portal DSD_BOP(24.0.0), dataflow BOP(21.0.0), and referenced codelists/constraints only through a currently documented, accessible official route. Prior HTTP 404/400 error payloads are rejected as metadata evidence; do not repeat equivalent failed URLs without a documented endpoint change.
3. Build field/code-level mapping only where official concepts, codelists, constraints and semantics agree; otherwise mark NOT_MAPPED / UNKNOWN.
4. Keep all 154-country coverage, vintage, BPM-basis and aggregation gates closed until country-level observations and both accounting legs pass aligned period/unit/scale/sign/vintage checks.

## Rejected / excluded
- No inferred alias between BOP6 and BOP_BPM6.
- No use of the ESTAT-maintained v2.6.0 dataflows as a proxy for Brazil/IMF coverage.
- No mapping by dimension-name similarity alone.
- No synthetic observations, interpolation, forward fill, zero imputation, guessed timestamps, or guessed SDMX keys.
- No repetition of completed 40/40 registration lifecycle, 118/118 benchmark, or already-verified BOP 2.6.0 capture.

## Hard invariants
₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS. No production integration or trading admission.
