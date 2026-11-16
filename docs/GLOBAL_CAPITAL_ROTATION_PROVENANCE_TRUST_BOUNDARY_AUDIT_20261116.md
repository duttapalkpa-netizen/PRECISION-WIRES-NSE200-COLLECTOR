# Global Capital Rotation — Observation Provenance Trust-Boundary Audit
Audit date: 2026-11-16 (Asia/Kolkata)
Branch: `research/global-capital-rotation-overlay-mainline-20261113`
Scope: static review of research-only parser `pipeline/global_capital_rotation_overlay.py` and its current unit tests. No runtime execution, no external data acquisition, no production changes.

## Evidence inspected
- Parser blob: `3009306ad59e8efd75bf2d8a3a6f4859afee1ece`
- Test blob: `c7a72386f9633b09841e0f1630fa3e2ae24bd01d`
- Parser `load_observations()` checks required columns, allowed quality labels, non-empty provenance fields, ISO dates, finite numeric value, duplicate key, observation date <= as_of_date, and HTTPS URL scheme.
- Parser then accepts rows labelled `VERIFIED_OFFICIAL` or `VERIFIED_SECONDARY` into the classifier's grouped observations. The supplied `source`, `source_url`, `quality_status`, and `unit` are not matched against an authoritative source/indicator registry in this function.
- The test helper deliberately uses `https://example.org/data` with default `VERIFIED_OFFICIAL`; tests validate parser mechanics, not source authenticity.

## Finding: provenance labels are caller assertions, not authenticated evidence
**Severity: HIGH for research-signal integrity; not a production incident.**

A CSV row can declare `quality_status=VERIFIED_OFFICIAL` while naming an arbitrary HTTPS host and arbitrary source label. The parser checks HTTPS, but does not establish that:
1. the host is authorized for the given indicator;
2. the source label matches that host or a pinned official source;
3. the unit matches the indicator's required unit;
4. the row's publication timestamp is supported by an archived source response/manifest;
5. the raw payload hash and retrieval timestamp exist and match the row.

Therefore `VERIFIED_OFFICIAL` currently means “the input file says this” at parser level, not independently verified official provenance. This is a static trust-boundary finding; no malicious or false row was observed in the seed dataset, and no live signal was generated.

## Secondary contract gaps
- The required CSV schema does not include `retrieved_at`, raw-payload SHA-256, response status/content type, source class, or source-vintage identifier, although the source contract requires immutable provenance.
- `unit` is required to be non-empty but is not validated per indicator. A value in an incorrect unit could enter threshold/sign classification.
- `source_url` is required to be HTTPS but host allowlisting and URL-path/series binding are absent at this parser boundary.
- Existing tests use `example.org` as a generic fixture and thus cannot demonstrate official-source authentication.

## Safe decision
- Existing unit-test result (27/27 on run `43370022907`) remains a parser-behavior test result only; it does not cover this provenance-authentication gap.
- Do not promote any observation to VERIFIED_OFFICIAL solely because the CSV label says so.
- Until a source-evidence manifest/registry is bound to each indicator, keep externally supplied observations at UNKNOWN for any decision-grade use. Preserve raw source files separately with SHA-256 and retrieval metadata.
- No seed values changed, no rows added, no fabricated evidence, no production selector/ranking/engine changes.

## Next bounded remediation
1. Define a versioned indicator-to-source registry: indicator, allowed host(s), exact series/report path, unit, source class, expected frequency, and provenance requirements.
2. Require an immutable per-payload evidence manifest (retrieved_at UTC, final URL, HTTP status, content type, byte length, SHA-256, source publication/vintage if explicitly supplied).
3. Parser must reject or downgrade to UNKNOWN any row whose source/host/path/unit does not match the registry or whose referenced manifest is absent/hash-mismatched.
4. Add offline tests using synthetic *metadata fixtures only* (not synthetic market observations) for untrusted host, mismatched unit, missing manifest, hash mismatch, and valid manifest binding.
5. Keep all outputs research-only; no production integration without explicit approval.

Status: STATIC_FINDING_CONFIRMED; REMEDIATION_NOT_STARTED; RUNTIME_TEST_NOT_RUN; PRODUCTION_UNCHANGED.
