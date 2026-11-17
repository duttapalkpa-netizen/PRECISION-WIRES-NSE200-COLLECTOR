# CDSL–BSE–NSE Code-Level Crosswalk Acceptance Contract
Audit date: 2026-11-17 (Asia/Kolkata)
Branch: research/taxonomy-crosswalk-contract-20261117
Purpose: define a reproducible, fail-closed path from the already-completed authority/version audit to a real code-level comparison. This contract is not a crosswalk dataset and does not authorize registry or production use.

## 1. Verified source authority and scope
- CDSL's 15-Oct-2026 fortnightly sector report says its common classification is the BSE-provided structure effective 30-Apr-2022; issuers outside its approximately 4,800-issuer classified set are placed in "Others": https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/October%2015%2C%202026.html
- BSE official codebook: https://www.bseindia.com/Downloads1/India_Industry_Classification_Structure.pdf . Fields: MEI_CODE, SECT_CODE, IND_CODE, BASIC_IND_CODE, labels and definitions. BSE example: IN010302002 = Copper, under IN010302 Non-Ferrous Metals and IN0103 Metals & Mining.
- BSE's 2023 methodology notice states 12 macro indicators, 22 sectors, 58 industries and 200 basic industries: https://www.bseindia.com/downloads/SPDJ_ANN/MediaReleasePDF/1461969_mediareleasemodificationtothemethodologiesofthespbseindices20230310.pdf
- NSE official classification page (updated 21-Sep-2023) describes a four-tier revenue-based taxonomy with 12 macro-economic sectors, 22 sectors, 59 industries and 197 basic industries, and links its July-2023 codebook: https://www.nseindia.com/static/products-services/industry-classification
- NSE July-2023 PDF: https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf
- BSE and NSE both expose four-tier codes with the same visible Copper example (IN010302002); this single example is a semantic spot-check only, not evidence of whole-codebook equivalence.

## 2. Version and count discrepancy — hard gate
Published counts differ: BSE 58 industries / 200 basic industries; NSE 59 industries / 197 basic industries. Macro and sector counts match (12 / 22). The NSE public page identifies a July-2023 structure; the currently linked BSE PDF does not, in the inspected extraction, expose a clear effective-date/version identifier. Therefore:
- Never merge the two taxonomies by label alone.
- Never infer that matching code prefixes guarantee identical membership or definitions across vintages.
- Keep BSE and NSE raw codebooks as separate source snapshots with source URL, retrieval timestamp, published/effective date (or UNKNOWN), byte count, SHA-256 and parser version.
- If a vintage cannot be established, mark it UNKNOWN; do not assign a guessed effective date.
- Count mismatch must be explained by a row-level diff before any equivalence claim.

## 3. Required crosswalk row schema
Each candidate mapping row must contain:
- source_system (BSE or NSE), source_vintage, source_url, source_code_level;
- source_code, source_label, source_definition;
- target_system, target_vintage, target_code_level, target_code, target_label, target_definition;
- mapping_status = EXACT_CODE_AND_DEFINITION | EXACT_CODE_LABEL_ONLY | SEMANTIC_PARTIAL | ONE_TO_MANY | MANY_TO_ONE | NO_MATCH | UNRESOLVED;
- evidence_ref, evidence_locator (PDF page/line or official row identifier), reviewer_note;
- valid_from, valid_to, observed_at, published_at (nullable only with explicit UNKNOWN state);
- issuer_id / ISIN only in a separate issuer assignment table, never embedded as an inferred taxonomy crosswalk.

## 4. Matching and fail-closed rules
1. Compare exact codes at each level before comparing labels; normalize whitespace/punctuation only in a separate comparison field, never overwrite source labels.
2. Compare definitions and parent paths; same leaf label under a different parent is not an exact match.
3. Detect duplicate codes, duplicate labels, orphan parents, missing levels, code-format violations and hierarchy cycles.
4. Report row counts by level and code-prefix uniqueness; totals must reconcile to the published source counts or be explicitly explained.
5. Every BSE code must end in a documented target outcome; every NSE code must also be accounted for. Unmatched rows remain NO_MATCH/UNRESOLVED, not force-mapped.
6. "Others" in CDSL is a coverage residual for issuers outside its classified set, not an NSE taxonomy code or sector.
7. Do not use issuer/company names, business intuition or a single example to infer code assignments.
8. Issuer mapping requires an official, dated BSE/NSE issuer-to-code record or an equivalent primary exchange/depository source, plus stable issuer identifier (ISIN/official security ID), source vintage and effective date. Company name-only joins are prohibited.
9. If the source only supports sector-level aggregation, do not claim issuer-level or basic-industry precision.
10. Preserve all ambiguity and source disagreement; UNKNOWN is never PASS.

## 5. Required QA and release artifacts
- Immutable raw source manifest for each BSE and NSE codebook (URL, retrieved_at with timezone, HTTP metadata if available, byte length, SHA-256).
- Parsed source tables preserving original text and source page/row locators.
- Four separate level-wise comparisons: macro, sector, industry, basic industry.
- Full mismatch report with exact-match, label-only, semantic-partial, one-to-many, many-to-one, no-match and unresolved counts.
- Parent-path integrity report and source-count reconciliation.
- Issuer mapping coverage report using official identifiers and effective-dated records; no name-only mapping.
- Deterministic tests and a replay manifest. A missing/failed source retrieval or count mismatch blocks PASS.
- Versioned crosswalk artifact and review ledger; never edit historical vintages in place.

## 6. Acceptance gates and current state
| Gate | Required evidence | State on 2026-11-17 |
|---|---|---|
| CDSL authority and "Others" semantics | Official CDSL report footnote | PASS |
| BSE four-tier codebook identity | Official BSE PDF | PASS |
| NSE four-tier codebook identity | Official NSE page + July-2023 PDF | PASS |
| Published count mismatch detected | BSE 58/200 vs NSE 59/197 | PASS |
| Raw BSE/NSE payload bytes + SHA-256 | Immutable source manifests | NOT_ACQUIRED |
| BSE effective vintage resolved | Official publication/effective date | UNKNOWN |
| Full code-level diff | All rows and four hierarchy levels | NOT_STARTED |
| Difference explanation / complete accounting | Row-level evidence and reconciled totals | BLOCKED |
| Issuer-level assignment | Official dated identifier-to-code records | NOT_STARTED |
| Historical PIT taxonomy archive | Effective-dated source vintages | NOT_STARTED |
| Parser/registry integration | Reviewed crosswalk + tests | NOT_AUTHORIZED |
| Production overlay use | Separate acceptance and backtest | NOT_AUTHORIZED |

## 7. Explicit non-effects / invariants
This is a research-only documentation contract. It changes no source observations, classifications, parser, registry, tests, workflows, selector, ranking, or production logic. No synthetic data, labels, timestamps, identifiers or hashes are permitted. Research spend: ₹0.
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows remain unchanged.
