# NSE March-2022 / July-2023 Full Inventory — Acquisition Gate

Date: 2026-11-17

## Official source snapshots
- March 2022: https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE%20Indices_Industry%20Classification%20Structure-2022-03.pdf
- July 2023: https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf
- Web document-reader inspection: March-2022, 34 pages / 1,135 extracted lines; July-2023, 23 pages / 1,064 extracted lines. Title pages identify the exact vintages; tables expose MES, Sector, Industry, Basic Industry codes/names and definitions.

## Execution result
- Attempted binary acquisition of the March-2022 PDF into the working runtime; download failed.
- Raw bytes: NOT_ACQUIRED.
- Byte length / HTTP headers / retrieval timestamp: NOT_ACQUIRED.
- SHA-256: NOT_COMPUTED (must not be inferred or fabricated).
- Machine-readable full inventory: NOT_DONE.
- Bidirectional exact-code + hierarchy + definition diff: NOT_DONE.
- Zero-unexplained-row acceptance gate: NOT_MET.

## Why this is a blocker
Web-rendered extracted text supports targeted source review but does not itself provide a locally acquired immutable binary or a deterministic parser run. A full inventory cannot be certified from selected excerpts or manually guessed row counts. The five targeted examples already documented in the companion correction audit are not repeated here; Air Conditioner and Toys remain consolidation/reclassification candidates, Cycles a scope-boundary clarification, and the two trading rows candidate rename/recode lineages.

## Required next action (bounded)
1. Acquire both exact official PDF binaries through a working permitted route or exact user-provided files.
2. Record source URL, document vintage, retrieval time with timezone, HTTP metadata where available, byte length and SHA-256.
3. Parse page-bounded chunks into a canonical inventory with exact raw codes, full four-level hierarchy, names and full definitions.
4. Validate each chunk against the official rendered pages; reject duplicate codes, missing parents, malformed codes and truncated definitions.
5. Run both 2022→2023 and 2023→2022 diffs. Classify each changed row; do not infer lineage from label similarity alone and do not call deletion until the entire target snapshot is searched.
6. Require zero unexplained rows before BSE crosswalk or issuer mapping work.

## Guardrails
No synthetic data, timestamps or hashes; ₹0; no production/parser/registry/issuer mapping changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows remain unchanged. UNKNOWN is not PASS.
