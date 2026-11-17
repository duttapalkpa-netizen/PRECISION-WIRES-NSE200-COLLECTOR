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

## Runtime result — PASS (2026-11-17)
- Corrected GitHub Actions Run #2 / ID `44095286184`: SUCCESS; https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44095286184.
- Raw official responses archived at `evidence/imf_bop_dsd/20261117T134325Z/` with manifest, untouched XML and per-resource HTTP metadata.
- BOP DSD 2.6.0: 895,438 bytes; SHA-256 `073afeeb971dfa797460ba2233c7af4aa7dfffe4908657b5364e24fc77314f2f`.
- BOP_BPM6 dataflow: 22,078 bytes; SHA-256 `74a8f3a58ff3e0bc6e6681c4143cd042cc642edee06f8080e86c29dc3b64e919`.
- Constraint: 18,675 bytes; SHA-256 `aa6c002fb3a2498420ed8796621664b492c18f58d75918d5c1bf8737fc917656`.
- Actual referenced DSD ECOFIN_DSD 1.0: 42,707,649 bytes; SHA-256 `81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045`.
- All four requests returned HTTP 200 / application/xml; all XML parsed and exact identities/attachments passed. The workflow captured 4 source resources, including the dataflow's actual DSD reference, and committed all nine files in commit `bd2a7d123b949f4ffcc426608a36de706a8fd658`.
- Artifact ID `14333192531`; archive SHA-256 `eb9abfe61d8f62e5d67c4b224e7f0e89f443a4aadccb3e5bc588f51a6a976c3f`; 1,997,984 bytes; expires 2027-02-15.
- Acceptance is metadata-only. BOP observations, country panel, actual-vs-estimate flags, publication vintage and production use remain NOT_DONE / NOT_AUTHORIZED.
