# Fed H.10 ZIP safety validation — 2026-11-12

## Scope
This audit records bounded ZIP inspection safeguards added to the research-only Federal Reserve H.10 raw collector. It does not establish live source availability or data ingestion.

## Implemented safeguards
- Compressed response ceiling remains 40 MiB.
- Maximum ZIP member count: 10,000.
- Maximum uncompressed size per member: 128 MiB.
- Maximum aggregate uncompressed size: 256 MiB.
- Reject duplicate member names and encrypted members.
- Reject absolute paths, drive-qualified paths, traversal components, empty/repeated path components, NUL bytes, and Windows backslash separators.
- Validate ZIP metadata limits before calling CRC test, bounding decompression work.

These are conservative engineering limits for this raw-archive collector; if the official package legitimately exceeds them, the run fails closed and requires a reviewed limit change rather than silent truncation.

## Regression validation
- GitHub Actions run: 43181479256
- Workflow: Federal Reserve H.10 raw collector contract tests
- Run number: 8
- Conclusion: SUCCESS
- Job: `tests` — SUCCESS
- Python: 3.12.16
- Test command: `python -m unittest qa.test_fed_h10_raw_collector -v`
- Result: 12 tests passed; 0 failures; test execution 0.013 seconds.
- Tested safeguards include URL origin/redirect validation, raw-byte/hash manifest behavior, append-only collision, non-ZIP response, duplicate names, encrypted members, member-count limit, per-member and aggregate uncompressed-size limits, and unsafe path variants.

## Evidence boundary
- CI validates mocked/offline behavior only.
- No actual Fed H.10 ZIP was downloaded in this run.
- No live ZIP member list, archive SHA-256, XML parsing, or observation panel is claimed.
- Official XML link access remains separately documented as verified link / raw download blocked in the current execution environment.

## Release boundary
Research-only. PR #32 remains open and unmerged. No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, Engine A–E, or Hard Gate changes. No paid service used.
