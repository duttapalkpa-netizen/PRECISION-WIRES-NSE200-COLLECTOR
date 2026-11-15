# CORE-672 FII/DII Context Contract & Regression-Test Specification

Date: 2026-11-16  
Scope: read-only research specification; no implementation or production change  
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## 1. Source-backed finding

Inspected source blobs:

| File | Blob SHA | Observed contract |
|---|---|---|
| `collector/context_data.py` | `f38e17979774d1439eea79e4dc7728ba92a790d1` | NSE `/api/fiidiiTradeReact` rows normalized to `category`, `group`, `date`, `buy_value`, `sell_value`, `net_value`; coverage metadata records FII/DII row and date counts |
| `pipeline/diagnostics_672.py` | `af0a8ddc17d72024509167533585713600a4b845` | FII/DII branch searches each row for `fii_net` and `dii_net`, then averages those fields |
| `pipeline/risk_modifier.py` | `4115a1247992ef8a075b2fd247efb9ce8f8663f6` | Uses `group` and `net_value`; sums first 20 values separately for `FII_FPI` and `DII` |

**Verified schema mismatch:** the collector does not emit `fii_net` or `dii_net`; it emits `group` and `net_value`. Therefore the diagnostics branch's list comprehensions receive no usable FII/DII values from the current collector output. With a nonempty list, the resulting empty-array mean is NaN (and may emit a NumPy warning); the branch then substitutes zero for each missing side and classifies 50, which resolves to `UNKNOWN` under the 60/40 thresholds. This is a source-level deterministic mismatch, not a newly measured runtime observation.

## 2. Do not silently choose aggregation semantics

The repository currently contains two different aggregation patterns:
- Diagnostics: mean of fields named `fii_net` / `dii_net` (fields not emitted by the collector).
- Risk modifier: sum of the first 20 category-normalized `net_value` rows for each group.

Neither source establishes an approved CORE-672 aggregation policy. Before implementation, the owner must decide whether the diagnostic should use latest common date, a specified rolling window, or another documented period; how missing FII versus DII sides are handled; and what units/sign convention are authoritative. Do not copy the risk modifier's 20-row sum into CORE-672 without approval.

## 3. Proposed canonical input contract (approval required)

A future adapter should consume the existing normalized shape without rewriting the collector:
- `fii_dii[]`: `group` in `FII_FPI` or `DII`; `date`; numeric `net_value`; optional `buy_value` and `sell_value`.
- `fii_dii_coverage`: source-provided row/date counts, used as coverage metadata, not as a substitute for observations.
- `sources.fii_dii`: expected provenance string identifying the NSE endpoint.
- `generated_at`: context file generation time. This is not the same as the observation date and must not be treated as a market publication timestamp.

Fail-closed rules:
1. Missing file, malformed JSON, absent `fii_dii`, unknown group, nonnumeric `net_value`, or invalid date must not create POSITIVE/NEGATIVE.
2. Missing one category must not be converted to zero unless an explicitly approved policy says so.
3. Duplicate category/date rows must be detected and resolved by an explicit rule; never silently double count.
4. Stale data must remain UNKNOWN unless an approved freshness limit and timestamp semantics exist.
5. A date-only observation must remain date-only; do not invent intraday availability time.
6. The output must expose provenance, selected observation dates, aggregation window, sample counts and missing-side status for auditability.

## 4. Regression-test specification (tests to write only after approval)

| Test ID | Fixture / condition | Required assertion |
|---|---|---|
| FII-01 | Collector-shaped FII_FPI and DII rows with `net_value` | Adapter reads the actual schema; no lookup of nonexistent `fii_net`/`dii_net` |
| FII-02 | Only FII row present | Result remains UNKNOWN unless missing-side policy is explicitly approved |
| FII-03 | Only DII row present | Same fail-closed behavior |
| FII-04 | Both categories with positive/negative values | Result follows the approved sign and aggregation rule, not an inferred one |
| FII-05 | Rows arrive in shuffled order | Result unchanged; selection based on explicit date/group keys |
| FII-06 | Duplicate group/date row | Explicit duplicate handling; no silent double count |
| FII-07 | Missing, null, string-invalid or infinite net_value | UNKNOWN / validation failure; never synthetic zero |
| FII-08 | Stale context or missing generated_at/source | UNKNOWN or explicit provenance blocker |
| FII-09 | Date-only observations | No fabricated timestamp; observation date retained |
| FII-10 | Empty list / absent context file / malformed JSON | UNKNOWN; no crash that converts absence to a market state |
| FII-11 | Change FII data while holding DII constant | Only the FII-dependent evidence changes, per approved formula |
| FII-12 | Change DII data while holding FII constant | Only the DII-dependent evidence changes, per approved formula |

Additional CORE-672 contract tests:
- The same Step's 12 Filter outputs must not be identical by construction; each implemented Filter must respond to its own declared evidence predicate.
- Unavailable evidence remains UNKNOWN.
- NOT_APPLICABLE is emitted only where a documented applicability rule says so.
- No future-dated context or look-ahead is permitted.
- Repeated execution on identical inputs is deterministic.

## 5. Acceptance gates

| Gate | Acceptance condition | Current status |
|---|---|---|
| Source schema reconciliation | Collector and consumer field names agree | FAIL — mismatch confirmed |
| Aggregation policy | Explicit approved period/sign/missing-side policy | BLOCKED — not specified by current source |
| Freshness contract | Approved observation-time and maximum-age policy | BLOCKED |
| Adapter implementation | Research-only, independently tested adapter | NOT_STARTED |
| Regression tests | All applicable tests pass on collector-shaped fixtures | NOT_STARTED |
| Runtime artifact | Real archived context with provenance and hashes | NOT_VERIFIED |
| CORE-672 cell acceptance | Independent Step×Filter semantics and evidence | BLOCKED |

## 6. Scope protection

This document does not modify `collector/context_data.py`, `pipeline/diagnostics_672.py`, `pipeline/risk_modifier.py`, the 56×12 contract, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, engines A–E, workflows, datasets or production branches. No CI run was dispatched and no PR was merged.

## 7. Progress

- Exact source retrieval and blob identification: 100%.
- Collector/diagnostic schema comparison: 100%.
- Mismatch classification: 100%.
- Aggregation policy: BLOCKED pending explicit decision.
- Test specification: 100%.
- Implementation and regression execution: 0% (not authorized / not performed).
- CORE-672 acceptance: BLOCKED.
