# V11.4 Forward-Label V2 — Research-Only Acceptance Specification
Date: 2026-11-20
Status: SPECIFICATION DRAFTED; IMPLEMENTATION NOT AUTHORIZED; PRODUCTION NOT AUTHORIZED
Scope: Corrected historical forward labels for research-only shadow evaluation. This document does not alter V11.3/V11.4 production selectors, rankings, gates, CORE-672, Engines A–E, or IPO-PLX V2.

## 1. Preflight and evidence basis
- Re-fetched the Master Continuity Ledger, GCR priority queue, Morocco Continuation 87/88 report, and the existing Daily Historical Rolling Backtest Performance Acceptance Contract before selecting this task.
- The latest Nightly Rotation Backtest report records a forward-label defect: symbol-only shifting across missing market sessions, partial windows accepted as mature, H+5 metrics JSON vs row-level CSV disagreement (613 vs 616 hits), and a contaminated state/probability assignment path.
- Existing report identifies Run #416, source label/config/script hashes, and output hashes. This specification requires reuse and independent re-verification of those existing artifacts; it does not redownload or rerun completed work.
- Existing acceptance contract is authoritative for the general rolling protocol, chronology, source provenance, and the >=50 fully matured observation floor for H+3 state calibration.
- No code, label output, metrics, production setting, or workflow was changed in this task.

## 2. Version and isolation rules
- Create a separately versioned research-only label schema, e.g. `forward_label_v2`; never overwrite or silently reinterpret v1 labels.
- Store schema version, code commit, config hash, dataset/manifest hash, run ID, artifact ID, cutoff, source period, retrieval/publication vintage and output hashes on every run.
- Keep v2 outputs in a shadow/research namespace. No production selector, rank, score, state calibration, alert eligibility or execution path may consume v2 until a separate explicit approval and all admission gates pass.
- Existing v1 metrics are quarantined from performance claims wherever their labels or training path are affected. Do not backfill a v2 metric into an old v1 report.

## 3. Canonical cutoff and forward-session spine
For each security and cutoff T:
1. Establish the exchange-wide canonical NSE trading-session calendar, with exact session dates and calendar version/hash.
2. Freeze the eligible security identity at T using the point-in-time security master and the strongest available stable identifier (ISIN/security ID); symbol is a dated display attribute, not a durable join key.
3. Define the forward outcome sessions as exactly the next h exchange sessions after T: T+1 ... T+h. Do not use row-offset shifting within an individual symbol table to infer these sessions.
4. Join each expected session explicitly. A missing security observation, suspension, trading halt, delisting, symbol/ISIN ambiguity, or source gap must receive a reason code and must not cause later rows to slide backward and fill the missing slot.
5. Do not substitute calendar days for trading sessions, and do not silently bridge a missing session. If a documented market-wide closure changes the exchange calendar, use the archived calendar vintage and record it.

## 4. Label construction contract
- Preserve the existing approved target definitions, cutoff reference-price convention, corporate-action adjustment policy, and target thresholds; do not invent or modify these semantics in the v2 repair. Before implementation, freeze their exact names, formulae, price fields, adjustment basis and inclusivity rules in a versioned config.
- For each target/horizon pair, evaluate only the declared forward window T+1..T+h. No observation from T itself may be counted as a forward hit.
- Label only after every one of the h expected market sessions has a valid, identity-matched, source-validated observation and all required price fields exist. A partial window is IMMATURE/INCOMPLETE, never a negative label and never included in any denominator.
- If a target is defined by an intraday high/low excursion, preserve that exact field and distinguish target-hit from close-return. Never replace high/low excursion with close-return or vice versa.
- Corporate actions, price adjustments, symbol changes, series changes, suspensions and delistings must follow a documented, point-in-time rule. If the rule cannot be applied from verified evidence, quarantine the row; do not infer an adjusted path.
- Features must be point-in-time knowable at T. No future price, future corporate action publication, later revised source, future universe membership, or future state/probability information may enter features or the ranking path at T.

## 5. Maturity and exclusion state machine
Each security/cutoff/horizon must resolve to exactly one state:
- MATURED_VALID: all h expected sessions and required fields pass; eligible for target label and denominator.
- IMMATURE_FUTURE: one or more expected future sessions have not yet occurred by evaluation time.
- INCOMPLETE_SOURCE: expected session exists but source/security observation is missing or invalid.
- IDENTITY_UNRESOLVED: point-in-time symbol/security identity cannot be established.
- ACTION_ADJUSTMENT_UNRESOLVED: corporate-action or price basis cannot be resolved.
- QUARANTINED_CONFLICT: conflicting duplicate rows, conflicting sources, or irreconcilable values.
Only MATURED_VALID may contribute to label counts and metrics. Every other state is excluded from TP/FP/FN/TN denominators and reported separately by reason. No exclusion is silently dropped.

## 6. Data integrity and anti-leakage gates
- Uniqueness: one canonical row per security identity + cutoff + horizon + expected session + field. Exact duplicate source rows may be retained in raw evidence but must be deterministically resolved only under an explicit, source-backed rule; conflicting duplicates fail/quarantine.
- Session completeness: for each MATURED_VALID row, exactly h distinct expected session dates must be present; no compressed symbol-local sequence.
- Temporal integrity: every feature/source observation has an availability/publication timestamp <= cutoff under its source's documented timestamp semantics. Retrieval timestamp alone is not evidence of publication availability.
- Vintage integrity: later revisions may not be retroactively treated as known at historical T. Preserve original and revised vintages separately.
- Identity integrity: assert exact security key, cutoff, horizon and session key before joins; never reuse another country's/symbol's extracted values based on positional similarity.
- Leakage tests must include a deliberately future-dated feature and prove it is rejected; a same-day T observation must not satisfy T+1; a missing middle session must not shift later observations into its place.
- Denominator integrity: matured positive + matured negative equals MATURED_VALID rows for each target/horizon/universe/cutoff set. Exclusions reconcile separately to all candidate rows.

## 7. Serialization and metric reconciliation
- Derive all published metrics from one canonical row-level prediction ledger. JSON, CSV, tables and summaries must be generated from that exact ledger, not independent code paths.
- For each target/horizon, independently recompute TP, FP, FN, TN (where applicable), precision, recall, F1, false-positive rate, missed-winner rate, target-hit rate, coverage and confidence intervals from the row-level ledger.
- Assert exact equality of integer counts across row-level CSV, metrics JSON, summary table and manifest. A mismatch of even one row fails the run; no tolerance/rounding exception for integer counts.
- Explicitly reconcile selector Top-N, eligible-universe, matured-universe, immature and exclusion denominators. Every cutoff has a denominator ledger.
- H+5 JSON/CSV historical 613-vs-616 mismatch must be resolved by source-row provenance before any v2 acceptance; do not choose one count merely because it is preferred.
- Report fixed-baseline and latest-window metrics only on identical protocol, labels, eligibility and maturity rules. Methodology changes require a new series and prohibit direct improvement claims against incompatible v1 outputs.

## 8. Required tests (offline, bounded, deterministic)
Tests must use clearly marked test-only fixtures and must never add fixture rows to market-performance denominators:
1. Exact next-session mapping: T+1..T+h uses exchange calendar, not symbol row offsets.
2. Missing middle session: later rows do not compress; horizon remains incomplete.
3. Partial H+1/H+3/H+5: immature, excluded from metrics.
4. Same-day leakage: T cannot count as T+1.
5. Future feature/publication timestamp: rejected from cutoff feature set.
6. Point-in-time identity: symbol rename with verified stable ID remains correctly mapped; ambiguous/reused symbol quarantined.
7. Corporate-action ambiguity: quarantine rather than guessed adjustment.
8. Duplicate exact vs conflicting rows: explicit policy; conflicting rows fail.
9. Label formula parity: hand-check selected actual archived rows against the frozen formula and independently recorded source fields.
10. Count parity: JSON/CSV/summary/manifest integer counts identical.
11. Denominator conservation: eligible candidates = matured-valid + all mutually exclusive exclusion states.
12. Reproducibility: same immutable inputs/config/commit yield identical row ledger and hashes.
13. Runtime: each isolated audit job <10 minutes; prefer 20–60 seconds. No 120-minute prospective workflow for this repair.

## 9. Acceptance gates and failure outcomes
A v2 research run is ACCEPTED only if all gates pass:
A. Source artifact, raw/derived manifest, SHA-256, retrieval/publication semantics and point-in-time universe are verified.
B. Exact exchange-session spine and security identity joins pass.
C. Full h-session maturity enforced; no partial window admitted.
D. Feature, vintage, identity and corporate-action leakage tests pass.
E. Independent hand-checks of real archived rows match v2 labels.
F. Candidate, eligible, matured and exclusion denominators reconcile exactly.
G. JSON/CSV/summary/manifest counts match exactly, including H+5.
H. Independent metric recomputation matches every published count and metric within declared numeric rounding only.
I. H+3 state calibration retains the user-approved minimum of 50 fully matured observations per State; below 50 remains UNKNOWN. DATA_CONTAMINATED remains quarantined until its label and assignment path are independently repaired.
J. Run completes under 10 minutes and outputs are reproducible by hashes.
Any failed or unverified gate => v2 status BLOCKED/PARTIAL; no performance claim, no state calibration and no production admission.

## 10. Required deliverables for a future approved implementation
- Versioned v2 label-generation code and immutable config.
- Offline unit/integration test report with each gate and failure reason.
- Row-level v2 prediction/label ledger with security ID, cutoff, target, horizon, expected session dates, actual source dates, maturity state, exclusion reason, raw source references and label formula version.
- Per-cutoff denominator reconciliation.
- JSON metrics generated from the canonical row ledger.
- Immutable raw-source/derived manifest and SHA-256 receipt.
- Independent hand-check worksheet for actual archived observations.
- Leakage/identity/corporate-action QA report.
- Reproducibility/runtime report and artifact ZIP.
- New dated research report and updated continuity ledger/priority queue.

## 11. Approval boundary and current decision
- This document is a research-only acceptance specification. It is not an implementation request, a production change, or approval to alter the current observation-only boundary.
- Implementation must wait for explicit user approval. Even after implementation, production admission requires a separate decision and all applicable acceptance gates.
- Current V11.4: BLOCKED / NOT_ADMISSIBLE pending corrected labels and a fresh leakage-safe shadow walk-forward.
- V11.3 cost-aware replay: UNKNOWN / NOT_AUTHORIZED / NOT_RUN; G0 execution assumptions remain unapproved.
- GCR: UNKNOWN / BLOCKED; no synchronized vintage-aligned macro-sector-stock panel.
- No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A–E, IPO-PLX V2, weights, gates, or production workflows.
- ₹0; official/free sources only; no synthetic market data, fabricated timestamps, forward-fill, guessed mappings or unapproved collection. UNKNOWN is never PASS.

## 12. Prior evidence references
- Nightly review: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261120.md (Run #416 and corrected-label audit findings).
- General rolling acceptance contract: docs/DAILY_HISTORICAL_ROLLING_BACKTEST_PERFORMANCE_ACCEPTANCE_CONTRACT_20261119.md.
- Continuity ledger and priority queue: current repository master files at time of this continuation.
