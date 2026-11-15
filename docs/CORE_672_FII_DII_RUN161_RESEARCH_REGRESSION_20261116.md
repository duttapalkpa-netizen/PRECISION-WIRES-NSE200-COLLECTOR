# FII/DII Run #161 Research-Only Contract Regression Tests

Date: 2026-11-16  
Status: **PASS — 10/10 local unit tests; schema validation only**  
Scope: isolated research test files; no production imports or trading-state output.

## Provenance-pinned fixture
- Source workflow run ID: `43696699698` (Run #161)
- Artifact ID/name: `14154408713` / `precision-wires-adaptive-161`
- ZIP SHA-256: `b4623c28d30d04a73d21eb67662caeeab56123b2eba637d9eb652225df0305e8`
- Member: `data/context/market_context.json`
- Member SHA-256: `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`
- The committed fixture is a literal, provenance-labelled excerpt of the two real rows, not synthetic market data.
- Observation date remains date-only: `13-Nov-2026`; `generated_at` remains file-generation time.

## Implemented validation
- Recognized groups: `FII_FPI`, `DII`.
- Required source provenance and generation timestamp.
- Date-only observation format.
- Finite numeric `net_value`.
- Duplicate group/date rejection.
- Missing/empty rows and invalid groups/values rejected.
- No lookup of legacy `fii_net` / `dii_net`.
- Missing category is not zero-filled.
- Validator returns only `SCHEMA_VALIDATED_ONLY`; it does not aggregate, classify market direction, or emit POSITIVE/NEGATIVE.

## Test result
Local command: `python -m unittest -v`  
Result: **10 tests passed, 0 failed**, runtime 0.001 sec.  
No GitHub Actions run was dispatched.

## Explicitly unresolved
Aggregation period (latest common date vs rolling window), sign/units interpretation, freshness threshold, and missing-side policy remain BLOCKED pending owner approval. This fixture contains one observation date only and cannot establish rolling coverage. No CORE-672 signal/state acceptance is claimed.

## Scope protection
No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 definitions, engines A–E, collector code, workflows, datasets, or production branch changed. No PR merge, paid API, or spend.
