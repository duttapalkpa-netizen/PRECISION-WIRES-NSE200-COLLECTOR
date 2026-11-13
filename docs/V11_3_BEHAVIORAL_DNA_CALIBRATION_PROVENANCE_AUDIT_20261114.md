# V11.3 Behavioral DNA Calibration Provenance Audit
Date: 2026-11-14
Scope: read-only static source audit of the current default-branch implementation. No production code or ranking logic changed.

## Source identity inspected
- `pipeline/walk_forward_backtest.py` — blob `d085f7a2d35a88b4c4eaba65144a429a06961b09`
- `pipeline/v11_3_abcd_e.py` — blob `34ad08f130254a0e8c5f09ae5a0e2d93590757df`
- `.github/workflows/nse_collector.yml` — blob `8860fd4f7bb43164ad1b514c884f5e9adf750973`
- `pipeline/final_selection.py` — blob `8bf216c866030d92f8066e9183c9636880577910`
- `pipeline/diagnostics_672.py` — blob `af0a8ddc17d72024509167533585713600a4b845`

## Confirmed producer-consumer chain
1. The workflow runs `python pipeline/walk_forward_backtest.py` before `python pipeline/v11_3_abcd_e.py` in the same job, then uploads `outputs/backtest/` with the workflow artifact.
2. The walk-forward producer builds `dna` by grouping its prediction table on `STATE`; for each state it writes sample count, H+1 +5% rate, H+3 +10% rate, H+5 +20% rate and median winner probability. It writes this object to `outputs/backtest/behavioral_dna_library.json`.
3. The V11.3 consumer imports `add_features` and `add_tomorrow_features` from the V11.4-labelled `walk_forward_backtest.py`, reads the JSON from the same path, and uses state-specific `hit10_h3` to compute a 10%-weighted calibration component in `V11_3_CORE_SCORE`.
4. The dependency is therefore shared in executable source and same-workflow order. This audit does not establish that this cross-version coupling was intentionally versioned or contractually frozen.

## Calibration fallback behavior — exact semantic finding
- The V11.3 consumer initializes `calib={}`.
- If the file is absent, it remains empty. If JSON parsing raises an exception, it is reset to empty.
- For an empty library, `hist_rate` resolves to 0 and `max_rate` resolves to 0. The expression `50 + 50 * (hist_rate / max_rate if max_rate else 0)` therefore returns **50**, not zero.
- The same calibration value 50 is also produced when a valid non-empty library has all `hit10_h3` values equal to zero, or when a candidate state is absent while other states establish a positive maximum.
- Consequently, missing, unreadable, empty, all-zero, and some state-unseen cases are not distinguishable in the candidate score. The code silently maps these conditions to the same neutral calibration component.
- The score contribution is 10% × 50 = 5 points of the composite score under these conditions. This is a static arithmetic implication of the current code, not a claim about any historical run's actual scores.

## Provenance and reproducibility gaps
- The JSON contains per-state metrics but no embedded producer commit SHA, workflow run ID, artifact ID, source dataset digest, source session range, generation timestamp, schema/version identifier, or checksum.
- The workflow ordering ensures the producer normally executes before the consumer in a single successful job, but the consumer itself does not assert producer success, non-empty content, schema validity, data-vintage match, or provenance match before scoring.
- The workflow uploads the JSON as an artifact, but this source audit cannot bind a particular historical candidate output to the exact JSON bytes used in that run without retrieving that run's artifact and metadata.
- The current source does not expose a frozen V11.3-specific feature/calibration contract. Shared helper imports make future edits to the V11.4-labelled module capable of changing V11.3 feature semantics.

## Acceptance matrix
| Requirement | Result | Reason |
|---|---|---|
| Producer-consumer order in workflow | PASS | Walk-forward step precedes V11.3 candidate step |
| Shared V11.4-labelled helper dependency | PASS / CONFIRMED | V11.3 imports helper functions directly |
| Calibration output content identified | PASS | Per-state samples and H+1/H+3/H+5 hit rates |
| Missing/unreadable artifact distinguishable from valid zero rate | FAIL | Both collapse to calibration 50 |
| Embedded producer/run/data provenance | FAIL | Metadata not written into JSON |
| Historical run-level artifact binding | UNKNOWN | Requires exact run artifact retrieval and digest |
| Intentional version-contract decision | UNKNOWN | Cannot infer design intent from code alone |
| Production invariants changed | NO | Read-only audit only |

## Required remediation decision (not applied)
1. Owner must decide whether V11.4 helpers are intentionally shared or whether V11.3 requires a frozen/versioned contract.
2. Define an explicit fail-closed policy for missing, unreadable, empty, stale, schema-invalid or state-incomplete calibration: keep the calibration state UNKNOWN/BLOCKED rather than silently assigning a numeric value. This is a recommendation only; no code changed.
3. Bind each produced library to producer commit, workflow run, artifact ID, source dataset digest, source date range, schema version and file SHA-256; validate these before consumer scoring.
4. Add regression tests distinguishing valid measured 0% hit rate from absent/unreadable calibration, while preserving selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Hard Gate semantics unless separately approved.

## Safety statement
No selector, ranking score, pressure fade, diagnostic formula, engine, or Hard Gate was changed. No synthetic data was created. No workflow was run, no PR was opened or merged, no production integration occurred, and no paid source was used.
