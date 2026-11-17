# H.10 Historical Vintage Availability and Row-Level Diff Contract
Date: 2026-11-17 (Asia/Kolkata)
Status: OFFICIAL HISTORICAL-ARCHIVE LIMITATION CONFIRMED; ROW-LEVEL REVISION DIFF NOT_DONE

## Executive finding
The Federal Reserve's official DDP Retirement FAQ, last updated 2026-11-12, explicitly states that release XML files are overwritten as the release updates. The current XML always reflects the current/latest version and all available observations; archived versions from previous dates will not be available from that release XML location.

Official source:
https://www.federalreserve.gov/data/ddp-retirement-frequently-asked-questions.htm
Relevant FAQ: "Will XML files for individual releases continue to be available after the BYP functionality is removed?" The Board answers that XML files are overwritten on updates and prior-date archived versions will not be available.
This is a Board statement about the release XML archive behavior. It does not prove that no independent third-party or user-held archive exists.

## Implication for known H.10 correction notices
The Board's H.10 feed documents:
- 2026-08-10 H.10 release contained incorrect 2026-08-03 values for all currencies and dollar indexes; corrected 2026-08-12.
- 2026-05-01 G.5 release was followed by a correction on 2026-05-11 affecting some historical AFE, EME and Broad dollar index data.
- 2025-01-06 H.10 release was followed by a correction on 2025-01-07 affecting some historical AFE, EME and Broad dollar index data.
These notices establish that corrections occurred. They do not provide the pre-correction row values or a complete list of changed observations.

Official feed:
https://www.federalreserve.gov/feeds/h10.html

## Vintage retrieval decision
- Do not assume a dated H.10 XML snapshot is available at the current release XML URL.
- Do not invent historical values, timestamps, archive URLs, or hashes.
- Do not label the current 2026-11-17 capture as the 2026-08-10 or 2026-08-12 vintage.
- Do not use the current corrected snapshot to infer the prior erroneous value.
- Search only for independently preserved, explicitly dated source artifacts when a real archive candidate is identified. A file's upload time alone is not proof of its source publication vintage.
- Historical vintage archive and row-level correction quantification remain NOT_DONE until two authentic source snapshots exist.

## Row-level diff input contract (future, only when two real snapshots are supplied)
Each vintage input must carry:
1. Exact official source URL or independently verifiable archive provenance.
2. Source publication/release timestamp as published by the source (not local download time).
3. Retrieval timestamp with timezone, recorded separately.
4. Raw byte length and SHA-256 calculated from the exact downloaded bytes.
5. File format, series ID, source release identifier and parser/schema version.
6. Explicit vintage label: pre-correction or post-correction only when the source evidence supports that label.

Diff acceptance requirements:
- Verify both raw archives before parsing.
- Resolve the exact Board series ID (for Broad Dollar Index: JRXWTFB_N.B) and do not substitute a FRED prefix match.
- Validate date uniqueness and chronological ordering in each vintage.
- Compare the union of observation dates.
- Report unchanged, changed, added, removed and missing/status-changed rows separately.
- Preserve raw source values and status codes; ND/-9999 is missing, never zero or forward-filled.
- Report absolute and relative numeric deltas only for valid numeric pairs.
- Emit deterministic CSV/JSON output plus input/output hashes and a machine-readable QA summary.
- If either vintage lacks trustworthy publication provenance, classify the comparison UNKNOWN and do not claim a correction diff.

## Current source evidence and known limitations
- Current H.10 raw XML archive acceptance: PASS (as separately recorded in the H.10 offline acceptance and unit/vintage provenance records).
- Effective numeric index base: January 2006 monthly average = 100, already verified; do not repeat or rescale.
- Current XML raw UNIT label conflict remains preserved as source metadata.
- FRED full-history equivalence remains BLOCKED after repeated runner timeouts; do not repeat the same graph endpoint route without a materially different access path.
- Board's official XML overwrite policy confirms that current release XML is not a historical vintage archive.
- No authentic pre-correction H.10 snapshot for 2026-08-10 or post-correction dated snapshot pair was verified in this task.
- No row-level revision diff was produced.

## Progress and state
| Work item | State | Completion |
|---|---|---:|
| Official XML overwrite/archive policy verified | PASS | 100% |
| Known correction notices distinguished from row-level evidence | PASS | 100% |
| Historical pre/post vintage artifacts acquired | NOT_DONE | 0% |
| Row-level revision diff | NOT_DONE | 0% |
| Deterministic diff contract specified | PASS | 100% |
| Production integration | BLOCKED / NOT_AUTHORIZED | 0% |

## Project invariants
Research-only. No production migration or selector changes.
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A-E remain unchanged.
UNKNOWN never PASS. No synthetic observations, fabricated timestamps or hashes, paid APIs, or spend (₹0).
