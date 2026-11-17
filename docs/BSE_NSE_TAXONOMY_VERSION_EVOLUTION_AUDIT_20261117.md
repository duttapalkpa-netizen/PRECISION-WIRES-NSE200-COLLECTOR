# BSE–NSE Taxonomy Version-Evolution Audit — 2026-11-17

## Scope and decision

This is a bounded evidence checkpoint following the discovery of the BSE Index Services official subsidiary-hosted classification PDF. It is NOT a complete row-level crosswalk, issuer mapping, raw-byte manifest, or production approval.

## Official evidence reviewed

1. BSE Index Services, *BSE India Sector Leaders*, October 2025:
   https://www.bseindices.com/Downloads/BSE_India_Sector_Leader_Paper_Oct_2025.pdf
   The report identifies BSE Index Services Pvt. Ltd. as a wholly owned subsidiary of BSE and states the India Industry Classification Structure contains 12 Macro-Economic Indicator categories, 22 Sectors, 59 Industries and 197 Basic Industries (PDF extracted lines 0–23). It provides example issuer paths (Reliance Industries, HDFC Bank, TCS, HUL, Maruti Suzuki) at lines 24–67.

2. BSE Index Services official subsidiary-hosted classification PDF:
   https://www.bseindices.com/Downloads/India_Industry_Classification_Structure.pdf
   Document retrieval exposes a 16-page PDF and the four hierarchy fields MEI_CODE, SECT_CODE, IND_CODE, BASIC_IND_CODE. The extracted table contains the Copper path IN01 / IN0103 / IN010302 / IN010302002 (lines 75–100). This PDF does not expose a clear effective date/version in the inspected metadata.

3. BSE Index Services notice 20220517-6, dated 17-May-2022:
   https://www.bseindices.com/DisplayNoticescircular/20220517-6
   The notice says the common structure announced on 31-Mar-2022 comprised 12 Macro-Economic Indicators, 22 Sectors, 58 Industries and 200 Basic Industries.

4. NSE Indices, *Industry Classification Structure, July 2023*:
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf
   The PDF explicitly identifies its vintage as July 2023 and uses the four corresponding hierarchy levels. It lists the same Copper path and definition in the inspected table (PDF extracted lines 71–101). NSE's official classification page states 12/22/59/197 and was updated 21-Sep-2023:
   https://www.nseindia.com/static/products-services/industry-classification

## Findings

- The 58 Industries / 200 Basic Industries figure is explicitly attached to the 2022 launch-era BSE notice.
- BSE Index Services' October-2025 report explicitly states 59 Industries / 197 Basic Industries. This matches NSE's published 59/197 structure.
- Therefore, the former 58/200 vs 59/197 discrepancy is now best classified as a likely version/time-baseline discrepancy, not evidence by itself of a current structural incompatibility.
- This does NOT prove which individual Industry or Basic Industry codes were added, removed, split, merged, or renamed between the 2022 and 2025 vintages. That requires dated machine-readable or complete codebook snapshots and exhaustive code/definition/parent-path comparison.
- Sampled code-path checks across the current BSE-hosted PDF and NSE July-2023 PDF match:
  - IN010302002 — Copper; parent IN010302 Non-Ferrous Metals; IN0103 Metals & Mining.
  - IN060101001 — Pharmaceuticals under Healthcare.
  - IN090101001 — Dredging under Services / Engineering Services.
  These are spot checks only, not a full crosswalk.
- PDF page counts (BSE 16; NSE 23) and extracted line counts are rendering/extraction properties and must not be treated as taxonomy row counts.
- BSE current PDF effective vintage remains UNKNOWN. The 2025 report establishes a 59/197 count statement but does not identify the exact version/effective date of the separate downloadable PDF.
- No raw PDF bytes, HTTP response headers, byte lengths, retrieval timestamps or SHA-256 payload manifests were acquired. Document-layer text extraction is not a substitute for immutable byte evidence.

## Acceptance state

| Work item | State |
|---|---|
| 2022 BSE baseline (58/200) source | VERIFIED |
| BSE October-2025 count statement (59/197) | VERIFIED |
| NSE July-2023 count statement (59/197) | VERIFIED |
| Count discrepancy temporal hypothesis | SUPPORTED / NOT FULLY PROVEN |
| Sampled code-path concordance | PASS — spot checks only |
| BSE downloadable PDF effective vintage | UNKNOWN |
| Raw PDF payload manifests / SHA-256 | NOT_ACQUIRED |
| Exhaustive four-level code diff | NOT_DONE |
| Change list for 58/200 → 59/197 | NOT_DONE |
| Issuer-level mapping / PIT history | NOT_AUTHORIZED |
| Parser / registry integration | NOT_AUTHORIZED |
| Production use | NOT_AUTHORIZED |

## Next bounded action

Acquire an authoritative dated BSE classification snapshot or change notice that identifies the 58/200 → 59/197 transition, then perform exhaustive code-set reconciliation. Until then, preserve separate source-vintage namespaces and do not promote candidate label mappings.

## Invariants

No observations, issuer mappings, parser, registry, tests, workflows, selector, ranking, pressure-fade, CORE-672, Engines A–E, Hard Gate or collector production logic changed. No synthetic data, timestamps or hashes. Research spend ₹0.
