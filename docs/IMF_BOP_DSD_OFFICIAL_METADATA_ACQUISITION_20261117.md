# IMF BOP DSD 2.6.0 — Official Metadata Acquisition Gate
Date: 2026-11-17
Status before run: NOT_DONE — prior local DNS/download attempt failed in the execution environment.

## Purpose
Acquire the exact official IMF BOP DSD 2.6.0 SDMX-ML 2.1 structure, the registered IMF BOP_BPM6 dataflow and its BOP_BP6_CONSTRAINT using a bounded GitHub Actions runner. This avoids repeating local DNS retries and does not infer any observation-data access.

## Exact official requests
1. IMF BOP DSD 2.6.0: `https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true`
2. IMF BOP_BPM6 dataflow 1.0: `https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF/BOP_BPM6/1.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true`
3. IMF BOP_BP6_CONSTRAINT 1.0: `https://sdmxcentral.imf.org/sdmx/v2/structure/contentconstraint/IMF/BOP_BP6_CONSTRAINT/1.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true`

## Acceptance
- Preserve raw response bytes untouched.
- For each source capture request/final URL, HTTP status, Content-Type, response headers, UTC retrieval time, byte length and SHA-256.
- Parse XML and verify DSD identity IMF:BOP:2.6.0, dataflow identity IMF:BOP_BPM6:1.0 and explicit structure reference, and constraint identity/attachment IMF:BOP_BP6_CONSTRAINT:1.0 -> IMF:BOP_BPM6:1.0.
- Capture failure or malformed/semantically mismatched XML fails closed; partial artifacts retained for diagnosis.
- Five-minute workflow timeout; research branch only; no default/production branch changes.

## Hard boundary
A successful metadata capture is not a country-observation payload, not a complete EM panel, not proof of public unauthenticated observation access, and not production feature approval. Exact codelist codes, flow-direction interpretation, country coverage, actual-vs-estimate flags and PIT vintage still require separate audits. No BOP_AGG estimate substitution, no IIP-to-flow conversion, no synthetic observations, no paid API, no production selector/scoring/CORE-672/Engines A-E changes.
