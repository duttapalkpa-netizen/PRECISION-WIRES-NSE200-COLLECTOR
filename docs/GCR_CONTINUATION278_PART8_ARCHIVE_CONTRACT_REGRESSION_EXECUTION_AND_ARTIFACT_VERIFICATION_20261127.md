# GCR Continuation 278 — Part-8 isolated archive-contract regression execution and artifact verification
Date: 2026-11-27 (Asia/Kolkata)

## 1. Preflight / no-repeat
Re-read the current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, C277 Part-7 report, and Library Mother File / export-recovery evidence. C273 matrix QA, C274 schema fix/AST test/workflow creation, C275 access-boundary audit, and C276/C277 export Phase-4/5/6 reconciliations were treated as closed and not repeated. No NSE raw re-acquisition, IMF re-query, cohort rebuild, or Library duplicate upload.

## 2. Newly discovered actual workflow run
The prior assumption that no run could be found was superseded by a direct read-only GitHub Actions run-list query scoped to branch `audit/prospective-selector-tracking`.
- Workflow: Macro-Geo Archive Contract Regression (Audit Only)
- Run ID: `45946811444`; Run number: 1
- Event: `push`; status/conclusion: `completed / success`
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45946811444
- Head branch: `audit/prospective-selector-tracking`
- Head commit: `12cce4a15fdf9defa099fc17fa1675e2972505ee`
- Job `archive-contract`, job ID `140333274465`: completed / success.
- Step 5 “Run network-free producer-consumer contract regression”: success; pytest output `1 passed in 0.02s`.
- Step 6 machine-readable evidence generation: success; Step 7 artifact upload: success.
- Job logs were fetched and inspected; no failing step.

## 3. Artifact and JSON read-back
- Artifact: `macro-geo-archive-contract-regression`
- Artifact ID: `15174937795`; size 505 bytes; not expired.
- GitHub artifact digest / downloaded ZIP SHA-256: `0175914054f725206d0862771277f04c300da085f509a50a1900ba34d0e8b732` (exact match).
- ZIP integrity: PASS; one member only: `archive_report_contract_validation.json`.
- JSON member SHA-256: `c804f0187c42ed1fe0e462990c19971694a1963da8bf47781f6e1c947d82b13c`.
- JSON read-back: `schema_version=1`; scope = network-free AST producer/consumer contract only; producer keys = failures, observed_session_requests, rows; consumer keys = failures, observed_session_requests; required producer keys present = true; observed_session_requests consumed = true; stale weekday_requests consumer absent = true; collector SHA-256 = `d0a1c6e0f2d920c5441883d8c0df110f3136ab0298d2718f3282cb17d6b31b90`; test SHA-256 = `667eacce6f0d2ae20294185d9a9483ad85e6b6adf1bb9700ceb386c242f9f2ff`; `status=PASS`.
- The JSON evidence was read from the downloaded artifact ZIP, not inferred from the workflow conclusion.

## 4. Acceptance boundary
| Gate | Status |
|---|---|
| Isolated archive producer/consumer contract regression | PASS |
| pytest test | PASS (1 passed) |
| Artifact upload and ZIP digest verification | PASS |
| JSON artifact read-back and status | PASS |
| Macro-Geo P0 source coverage | BLOCKED (unchanged) |
| Strict GCR hard gate | BLOCKED / NOT_AUTHORIZED |
| candidate_release_allowed | false |
| Overall GCR | NOT_COMPUTABLE / NOT_CERTIFIED |

This PASS closes only the isolated Python/AST producer-consumer contract defect (the prior `weekday_requests` vs `observed_session_requests` mismatch). It does not validate live source coverage, P0 collection, FX/FPI/DII history, event studies, Macro-Geo recovery, GCR weights, or trading performance.

## 5. Next action
The isolated regression gate is now closed; do not rerun it absent code change. The next dependency is a separately authorized, <=10-minute, audit-only Macro-Geo recovery attempt using retained Run #398 handoff artifact `14757294944`, without re-acquiring NSE raw history. Before that recovery, confirm the authorization boundary and re-read current source inventory; only consume already-retained inputs. If required external inputs remain absent, stop and preserve BLOCKED/UNKNOWN rather than broadening collection.

## 6. Protected invariants
₹0 spend; official/free sources only; no IMF re-query, 63-country cohort rebuild, NSE raw re-acquisition, synthetic data, guessed IDs/timestamps, production selector/ranking/threshold changes, merge or production integration. `UNKNOWN` is neither PASS nor FAIL. CORE-672 (56×12), Engines A–E, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE` and IPO-PLX V2.0 unchanged. Workflow runtime remains <=10 minutes.
