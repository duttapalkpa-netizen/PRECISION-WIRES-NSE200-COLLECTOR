# CORE-672 Independent Semantic Audit — Static Source Findings

Date: 2026-11-16
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch inspected: `research/nse-raw-manifest-retention-20261115`
Source: `pipeline/diagnostics_672.py`
Source blob SHA: `af0a8ddc17d72024509167533585713600a4b845`
Audit type: read-only static source audit; no dataset execution and no production modification.

## Executive result

**BLOCKED — the source declares a 56 × 12 = 672 output matrix, but its implementation does not calculate 672 independent diagnostics.**

The nested loops iterate over every `step` and `filt`, but `filt` is only used to construct the output column name. It is not used in any calculation, threshold, evidence lookup, or state decision. Therefore, for every candidate row and every Step, all 12 Filter columns are identical by construction.

The source also calculates one generic candidate-level `base` for almost all Steps:
`mean(ENERGY, LEAD_TIME, min(RVOL20 * 25, 100))`
and classifies it with the same fixed `state(v, good=60, bad=40)` thresholds. Step-specific branches exist for FII/DII, India VIX, geopolitical article count, and hard-coded UNKNOWN event/live groups, but those values are also repeated unchanged across all 12 Filters.

## Evidence and findings

### F1 — Filter dimension is not implemented
- The loop is `for step in STEP_NAMES: for filt in FILTERS:`.
- `filt` is used only in `col=f"D{STEP_NAMES.index(step)+1:02d}_{filt}"`.
- No branch reads the filter name to select an evidence field, freshness rule, materiality rule, surprise calculation, information-gap calculation, price/volume/delivery reaction, earnings/institutional response, repricing, risk, or path calculation.
- Consequence: the 12 columns for each Step are guaranteed duplicates. The matrix has 672 named columns, not 672 independently evaluated Step×Filter signals.

### F2 — Most Steps collapse onto one generic technical proxy
- For each candidate row, the same `base` is calculated from ENERGY, LEAD_TIME and RVOL20.
- For every Step not matched by the special branches, the implementation appends `state(base)`.
- This generic branch includes macro, rates, inflation, crude, currency, liquidity, stress, sector, price/volume, absorption, relative strength, event-adjacent and global-theme Steps. The names do not alter the evidence used.
- The eight names explicitly listed in the later technical `elif` branch also use exactly `state(base)`; that branch is functionally equivalent to the final `else`.

### F3 — Special branches are repeated across Filters and have narrow evidence
- `FII_DII_SMART_MONEY`: one aggregate FII/DII context-derived scalar, repeated for all 12 filters and every candidate row.
- `GLOBAL_VIX`: India VIX percentChange compared with fixed 10 threshold; repeated across all 12 filters. This is not a global VIX series or a freshness/materiality/surprise matrix.
- `GEOPOLITICAL_TRADE_WAR`: geo-news article_count compared with fixed 40 threshold; repeated across all 12 filters. Article count alone does not establish geopolitical impact or stock-level transmission.
- Event Steps `WHY_NOW_CATALYST`, `CATALYST_REPRICING`, `CORPORATE_EVENT`, `EARNINGS_SHOCK`, `EVENT_SHOCK_LIVE` are hard-coded UNKNOWN.
- Live Steps `LIVE_1PCT`, `PROGRESSION`, `REVERSAL_TIME_DECAY` are hard-coded UNKNOWN.

### F4 — NOT_APPLICABLE is declared but never emitted
- `STATES` declares POSITIVE, NEGATIVE, UNKNOWN and NOT_APPLICABLE.
- `state()` emits only UNKNOWN, POSITIVE or NEGATIVE.
- Other branches likewise emit only UNKNOWN/POSITIVE/NEGATIVE.
- Therefore the implementation does not distinguish structurally inapplicable diagnostics from missing/unavailable evidence.

### F5 — Output report overstates implementation semantics
- The report counts `len(STEP_NAMES) * len(FILTERS)` and labels the implementation “data-derived adaptive matrix”.
- That count proves only the number of named output columns. It does not test filter independence, evidence provenance, per-step source mapping, or semantic distinctness.
- No unit tests for `pipeline/diagnostics_672.py` were found in the inspected research test file. This is a bounded observation, not proof that no such tests exist elsewhere in the repository.

## Impact on PRECISION-WIRES

1. CORE-672 cannot currently be accepted as 672 independent diagnostic signals on the basis of this implementation.
2. Any aggregation, confidence, coverage, or engine analysis consuming these columns risks counting the same generic technical proxy multiple times.
3. Macro, catalyst, earnings, institutional, path and live claims are not supported by the implementation for most Steps.
4. The current UNKNOWN event/live treatment is safer than fabricating positive evidence, but missing evidence must not be re-labelled PASS.
5. This finding does not establish that the entire PRECISION-WIRES project or all five engines are invalid; it establishes that this specific diagnostics generator does not implement the declared 56×12 semantic contract.

## Acceptance matrix

| Requirement | Finding | Status |
|---|---|---|
| 56 Step names declared | Source list present | DECLARED |
| 12 Filter names declared | Source list present | DECLARED |
| 672 named columns emitted | Nested loop constructs names | STRUCTURAL ONLY |
| Filter-specific calculation | Filter name unused in logic | FAIL |
| Step-specific evidence for all 56 Steps | Most use same generic base | FAIL |
| Event/catalyst/earnings evidence | Five groups hard-coded UNKNOWN | BLOCKED |
| Live/progression evidence | Three groups hard-coded UNKNOWN | BLOCKED |
| FII/DII provenance and filter-specific response | Single aggregate repeated 12x | PARTIAL |
| VIX provenance and filter-specific response | Single threshold repeated 12x | PARTIAL |
| Geopolitical source quality/transmission | Article count only | PARTIAL |
| NOT_APPLICABLE state | Declared but never emitted | FAIL |
| Independent tests for this generator | Not found in inspected test file | NOT_VERIFIED |

## Required repair plan (not performed)

1. Freeze this audit finding; do not change Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 production contracts, engines A–E, or collector workflows.
2. Create an explicit Step×Filter evidence registry: each cell must define source, field, as-of/freshness, transformation, threshold/rule, applicability, missing-data behavior, and provenance.
3. Implement only evidence-backed cells. Missing sources remain UNKNOWN; structurally irrelevant cells may be NOT_APPLICABLE with documented rationale.
4. Add tests proving (a) changing a Filter's relevant evidence can change that filter output, (b) unrelated filter columns do not alias, (c) unavailable inputs remain UNKNOWN, (d) NOT_APPLICABLE is explicit, and (e) no future data is read.
5. Run a bounded read-only audit and report per-cell coverage; do not claim 672 PASS until all 672 cells have independently evidenced semantics and tests.
6. Only after user approval, plan any implementation changes in a research-only branch. No production merge without explicit approval.

## Progress

- Source retrieval and exact-blob identification: 100%.
- Static loop/branch/state audit: 100%.
- Semantic gap classification: 100%.
- Runtime column-correlation audit on a real candidates dataset: NOT DONE (0%).
- Evidence registry and cell-by-cell provenance audit: NOT DONE (0%).
- Repair and regression tests: NOT DONE (0%).
- CORE-672 acceptance: BLOCKED.

No code, data, production selector, ranking score, engine or workflow was modified by this audit.
