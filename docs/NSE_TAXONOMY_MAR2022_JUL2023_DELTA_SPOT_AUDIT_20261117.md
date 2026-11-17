# NSE Industry Classification — March 2022 vs July 2023 Delta Spot Audit

Date: 2026-11-17
Branch: research/taxonomy-crosswalk-contract-20261117

## Official source snapshots

1. NSE Indices, Industry Classification Structure, March 2022:
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE%20Indices_Industry%20Classification%20Structure-2022-03.pdf
   Document title/date explicitly visible. March-2022 structure and row examples are in the extracted PDF text.
2. NSE Indices, Industry Classification Structure, July 2023:
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf
   Document title/date explicitly visible. July-2023 structure and row examples are in the extracted PDF text.
3. NSE classification methodology page (updated 21-Sep-2023):
   https://www.nseindia.com/static/products-services/industry-classification
   States current page counts 12 macro-economic sectors, 22 sectors, 59 industries and 197 basic industries, and describes annual structural review.

## Verified sample deltas (not exhaustive)

### A. Automobile sub-classification

- March-2022: IN020101002 “2/3 Wheelers” definition includes bicycles; IN020101003 is “Trading - Automobiles”. Separate “Cycles” appears as IN020201002 in Consumer Durables. “Air Conditioner” appears as IN020201001 and “Toys” as IN020201014.
- July-2023: IN020101002 “2/3 Wheelers” explicitly excludes bicycles and tricycles; “Cycles” remains a separate Basic Industry under Consumer Durables. “Auto Dealer” appears as IN020101004. In the inspected July-2023 Consumer Durables rows, the 2022 Air Conditioner and Toys entries are not present.
- These examples show definition/code changes and candidate removals/renames in the inspected pages. Absence from the inspected excerpt is not sufficient to classify a row as formally deleted from the complete July-2023 taxonomy; complete table accounting is still required.

### B. Code format

- March-2022 examples include Basic Industry codes such as IN0101010001 and IN020101003.
- July-2023 examples use codes such as IN010101001 and IN020101004.
- The observed Basic Industry code formatting/length differs between snapshots. Never join by truncated code, label alone, or numeric suffix alone. Exact raw string and parent path must be retained.

### C. Count evolution evidence

- Joint BSE/NSE press release dated 21-Mar-2022 states 12/22/58/200 and effective date 31-Mar-2022:
  https://www.niftyindices.com/Press_Release/ind_prs21032022_1.pdf
- NSE March-2022 guideline states 12/22/58/200:
  https://niftyindices.com/docs/default-source/default-document-library/nse-indices_industry-classification-guideline-2022-03.pdf
- NSE page updated 21-Sep-2023 states 12/22/59/197 and describes annual review of industry structure:
  https://www.nseindia.com/static/products-services/industry-classification
- BSE Index Services October-2025 paper also states 12/22/59/197:
  https://www.bseindices.com/Downloads/BSE_India_Sector_Leader_Paper_Oct_2025.pdf
- This supports a change between the 2022 baseline and later published count. It does not yet identify the complete additions/deletions/splits/merges or prove the effective date of each change.

## Acceptance state

| Work item | State |
|---|---|
| March-2022 official snapshot identity | VERIFIED |
| July-2023 official snapshot identity | VERIFIED |
| 2022 count baseline 58/200 | VERIFIED |
| 2023 count baseline 59/197 | VERIFIED |
| Selected row/definition deltas | VERIFIED — SPOT AUDIT ONLY |
| Code-format change observation | VERIFIED — sampled codes |
| Exhaustive 2022→2023 code-set diff | NOT_DONE |
| Exact additions/deletions/renames/splits/merges | NOT_DONE |
| Effective date per changed code | UNKNOWN |
| BSE current PDF effective vintage | UNKNOWN |
| Raw source bytes + SHA-256 manifests | NOT_ACQUIRED |
| BSE↔NSE complete codebook reconciliation | NOT_DONE |
| Issuer mapping / PIT history / parser / registry | NOT_AUTHORIZED |

## Next bounded task

Build a complete code inventory for both NSE snapshots, preserving raw code strings and full parent paths, then produce bidirectional exact-code and normalized-label comparisons with separate categories for exact, renamed, re-parented, definition-changed, added, removed and ambiguous. Only after the NSE 2022→2023 transition is accounted for should the equivalent BSE snapshot comparison be accepted.

## Invariants

No issuer mapping, parser, registry, tests, workflows or production logic changed. No inferred code equivalence or synthetic timestamps/hashes. ₹0. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows unchanged.
