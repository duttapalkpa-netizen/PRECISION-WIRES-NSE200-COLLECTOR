# V11.3 behavioral calibration artifact — QA contract (draft)

Status: User-approved fail-closed policy implemented on the draft QA branch; awaiting full CI verification and review. Missing, invalid, incomplete, or unproven calibration evidence blocks final selection readiness.

## Confirmed source defect

At `pipeline/v11_3_abcd_e.py` blob `34ad08f130254a0e8c5f09ae5a0e2d93590757df`, calibration loading initializes an empty mapping, catches every JSON-read exception and restores an empty mapping. Missing state/field values default to 0.0, and an empty maximum rate produces a calibration score of 50.0. Consequently missing, malformed, incomplete and genuine zero-rate evidence are not distinguishable.

## Required fixture matrix

| Fixture | Expected QA classification | Required assertion |
|---|---|---|
| Valid schema, matching engine/version, finite rates in [0,1] | VALID | Preserve exact measured rates; no coercion |
| Valid measured rate = 0.0 with complete provenance | VALID_ZERO | Distinct from missing/invalid |
| File absent | UNKNOWN_MISSING | Must not be represented as measured zero or neutral evidence |
| Invalid JSON | UNKNOWN_MALFORMED | Explicit parse failure; no silent empty-map fallback |
| Root is list/string/null instead of object | UNKNOWN_SCHEMA | Reject wrong root type |
| State absent | UNKNOWN_INCOMPLETE | No implicit state-level zero |
| hit10_h3 absent/null/string | UNKNOWN_INCOMPLETE | No implicit field-level zero |
| NaN, +Inf, -Inf, negative, >1, boolean | INVALID_VALUE | Reject; do not clip/coerce |
| Producer timestamp older than declared freshness policy | STALE | Classification only after freshness policy is approved |
| Engine/schema/feature version differs | VERSION_MISMATCH | Reject compatibility; do not auto-upgrade |
| Dataset fingerprint/cutoff does not match consumer context | PROVENANCE_MISMATCH | Reject reuse |
| Correct artifact but wrong source run/commit lineage | PROVENANCE_UNKNOWN or MISMATCH | Require explicit lineage validation |

## Draft metadata contract (not yet implemented)

A future versioned artifact should carry:
- `schema_version`
- `producer_engine` and `producer_engine_version`
- `feature_contract_version`
- `producer_run_id`
- `producer_commit_sha`
- `dataset_sha256` (or a canonical dataset fingerprint)
- `cutoff_start`, `cutoff_end`, and `generated_at_utc`
- `target_definition` and `label_maturity_cutoff`
- state-level `sample_count`, `hit10_h3_count`, and `hit10_h3_rate`

All counts must be non-negative integers, with hit count <= sample count. Rates must be finite and in [0,1], and must reconcile to counts within a documented floating-point tolerance. A zero sample count is not a measured zero rate; it is UNKNOWN/insufficient evidence.

## Approved policy (user approval recorded 2026-11-10)

Policy A: when calibration evidence is missing, malformed, incomplete, lacks required provenance metadata, or contains invalid rates, the calibration-dependent final selection is BLOCKED. The engine may retain provisional research rankings for diagnosis, but they are not actionable finalists.

Implementation boundary:
- The V11.3 candidate-generation step writes a separate `calibration_validation.json` status record.
- The final readiness gate adds a calibration blocker unless status is exactly `VALID` and `block_selection=false`.
- The existing score calculation, sort keys, ranking weights, Production Selector ordering, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and 672 diagnostics are not edited by this policy.
- A complete metadata-bearing artifact with a measured zero rate remains VALID_ZERO in meaning (valid evidence), and is not treated as missing.
- This validator checks structural metadata and numeric rates. Freshness, dataset fingerprint equality, and source-lineage verification still require explicit machine-verifiable producer/consumer context; they are not silently marked PASS here.

## Acceptance criteria for implementation

1. Tests exercise the actual production loader through an isolated temporary path; no NSE downloads or live feeds.
2. Every fixture above has an explicit expected classification.
3. Missing/malformed/incomplete/stale/version-mismatch cases cannot silently produce a valid neutral score.
4. Valid zero and valid non-zero cases remain distinguishable and reproducible.
5. Tests prove no changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, or Hard Gate.
6. CI reports the matrix result and fixture hashes; no synthetic market rows or fabricated timestamps.
7. No production policy is implemented until approved.

## Scope and status

- User-approved fail-closed calibration readiness gate added on this draft branch.
- Candidate score calculation and ranking order remain unchanged; final readiness is blocked on UNKNOWN/invalid calibration evidence.
- Dedicated QA-only GitHub Actions workflow added; it performs unit tests only and does not download market data.
- No paid source or external service used.
