# PRECISION-WIRES V11.3 — Canonical Master Acceptance Register (initial controlled baseline)
Date: 2026-11-08
Branch: fix/iip-41-vintage-audit-clean
Status: REGISTER CREATED; GLOBAL PERCENTAGE NOT YET CERTIFIED

## Scope and dimensions
- 10 parent workstreams, provisionally allocated 10% each (equal-weight governance baseline; transparent and revisable only through a versioned decision).
- CORE-672 enumerated explicitly: 56 steps × 12 filters = 672 diagnostic acceptance rows.
- Additional cross-workstream acceptance rows include the exact recovered Final Research Paper criteria.
- Register CSV: `research_state/MASTER_ACCEPTANCE_REGISTER_V1_2026-11-08.csv`.

## Evidence statuses
- PASS: exact artifact and acceptance test both verified.
- PARTIAL: bounded sub-criterion met, remaining criteria open.
- PENDING: evidence not yet reconciled; not a failure and not a pass.
- BLOCKED: dependent on an unresolved prerequisite; contributes zero accepted completion until unblocked.
- UNKNOWN: source/value/implementation not available; neither PASS nor FAIL.
- NOT_CERTIFIED: implementation or column exists but the full acceptance standard is not evidenced.
- QUARANTINED: preserved for audit, excluded from current production joins.

## Scoring method
Each parent workstream has a 10% maximum. Child items within a parent are equally weighted unless a later evidence-backed, versioned specification defines a different internal weight. Parent score = accepted child weight / total child weight. Overall score = sum of the 10 parent scores. PARTIAL may earn credit only when the acceptance criterion itself has objectively separable subtests and the completed subtests are recorded; otherwise it remains PENDING. BLOCKED, UNKNOWN, NOT_CERTIFIED and QUARANTINED earn no PASS credit. No workstream can earn credit from a workflow job's SUCCESS label alone.

## Critical evidence already recovered (do not repeat)
- IIP April and May API vs latest PIB: 86/86 matched in Run 42381121341 (#12), Artifact 13577128037, ZIP SHA-256 2337b9ed18d0057cac3a4c503a6d0657f0750df720f5a50878f14b3fc67d5059.
- April native catalogue XLSX remains NOT RECOVERED; API evidence does not substitute for native XLSX provenance.
- 41-month XLSX ingestion 39/41 = 95.1% ingestion ratio only; full vintage audit BLOCKED_WITH_GAPS.
- 693 candidate transitions in scope; 431 unresolved. 54 prior batch rows were structural QA, not source-cell certification.
- Batch 006 crosswalk remains a final-paper acceptance criterion and must not be marked complete without source-cell evidence.
- Radar one-off artifact completed; daily automation is not enabled.
- README explicitly says the complete 672-signal live system is not implemented/claimed.
- Preserve the legacy 37-row April transcription unchanged but QUARANTINED from current-series joins due to base-year conflict and missing six use-based rows.

## Architecture and hard constraints
Production selector, RANKING_SCORE, +1 PRESSURE_FADE and the 56×12 CORE-672 architecture remain unchanged. No production edits, no main-branch merge, no automation enablement without approval. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, guessed IDs, unsupported source promotion or Hard Gate relaxation. Research spend ₹0; official free sources only.

## Global progress rule
This register is the first frozen denominator baseline, but **do not publish a numeric overall completion until all child statuses and evidence references are reconciled**. Historical 36% remains stale baseline only. The first score must be computed from this CSV, not from memory or informal impressions. This initial register creation itself is 100% complete as a bounded documentation task; it is not 100% project completion.
