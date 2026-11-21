# GCR Continuation 203 — Pakistan (PAK) historical evidence / 63-country matrix reconciliation
Date: 2026-11-21 (Asia/Kolkata)

## 1. Mandatory continuity preflight
Re-fetched the current main-branch artifacts before selecting this task:
- Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `0c6173ba7ef3e659f62d953e6a2c1661185daf73`.
- GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `6accec0825233063a6965d7a654030e8d2b73e9d`.
- Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `3eec21119b875adc871caf9d525be03b93c589be`.
- 63-country matrix CSV: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`, pre-task blob SHA `f9d68b4a24d92c41e6c72db776d89254a8f6d7de`.
- PAK detailed country report: `docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md`, blob SHA `dc5d939ce280d937fe6275212f22ba9e8de3c846`.

The current ledger, queue and registry were checked; the fixed 63-country Q2-2026 cohort and existing IMF panel were reused. No IMF request, cohort rebuild, or national source re-download was performed.

## 2. Duplicate / completed work rejected
- The original PAK source-boundary finding that Q2 values were not extracted was superseded by the report's Continuation 51 addendum.
- Continuation 52 already extracted exact archived IMF rows, reviewed SBP BPM6 sign definitions, and compared the two legs independently.
- The SBP revision-policy follow-up already established only generic R/P status semantics; it did not identify the Q2 row's exact revision timestamp or a matching IMF vintage.
- Therefore no source retrieval, IMF extraction, sign-crosswalk derivation, or numeric comparison was repeated.

## 3. Existing accepted evidence
- Official SBP calendar-year BPM6 quarterly table: `https://www.sbp.org.pk/assets/document/BPM6_c.pdf`; CY26 Q2 is marked revised (R), units USD million.
- SBP Q2-2026 values: portfolio investment abroad (asset-side comparator) = **-2 USDm**; portfolio investment in Pakistan (liability-side comparator) = **-243 USDm**.
- Existing archived IMF exact rows (raw CSV blob SHAs retained in the PAK report):
  - A_NFA_T: -2,000,000 USD, SCALE=6, PRECISION=6, ACTION=R, 2026-Q2.
  - L_NIL_T: -243,000,000 USD, SCALE=6, PRECISION=6, ACTION=R, 2026-Q2.
- SBP's official BPM6 revision notice and FY23 BPM6 introduction support the financial-account framework: increases in assets/liabilities are positive, decreases negative; NAFA/NIL are the relevant concepts.
- Separate comparison at SBP's USD-million display precision:
  - Asset: SBP -2 vs IMF -2 USDm; residual 0; PASS.
  - Liability: SBP -243 vs IMF -243 USDm; residual 0; PASS.
- No netting, sign inversion, or inferred values were used.

## 4. Matrix reconciliation
The matrix still showed PAK as SOURCE_FOUND even though Continuations 51–52 had already captured both national Q2 legs and passed the separate numeric comparisons. Corrected only the stale PAK row:
- current_stage: DATA_CAPTURED
- source_gate: FOUND
- data_capture_gate: YES
- asset_gate: PASS
- liability_gate: PASS
- vintage_gate: PENDING
- full_pass: NO
- aggregate_admission: NOT_AUTHORIZED
- status_SOURCE_FOUND=NO; status_DATA_CAPTURED=YES; status_ASSET_PASS=YES; status_LIABILITY_PASS=YES; status_VINTAGE_PASS=NO; status_FULL_PASS=NO; status_BLOCKED=NO
- source_status=SOURCE_FOUND; data_capture_status=DATA_CAPTURED; asset_status=ASSET_PASS; liability_status=LIABILITY_PASS; vintage_status=DATA_CAPTURED; overall_status=DATA_CAPTURED
- evidence_ref points to `GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120`.

The vintage status remains pending because SBP's Q2 column is labelled revised (R) and the archived IMF rows also carry ACTION=R, but neither provides the observation-specific revision timestamp or exact same-vintage identity. This is not FULL_PASS.

## 5. Recomputed matrix snapshot after the one-row correction
- Immutable cohort: 63 rows; unchanged.
- Current stages: SOURCE_FOUND 18; DATA_CAPTURED 25; BLOCKED 19; NOT_STARTED 1.
- Independent gates: ASSET_PASS 17; LIABILITY_PASS 17; VINTAGE_PASS 0; FULL_PASS 0.
- Below DATA_CAPTURED: 38 (18 SOURCE_FOUND + 19 BLOCKED + 1 NOT_STARTED).
- Gate counts overlap and are not additive. No country is promoted to FULL_PASS. Aggregate remains NOT_AUTHORIZED.

## 6. Acceptance result
| Gate | Status |
|---|---|
| Continuity / queue / registry / matrix preflight | PASS |
| Fixed 63-country cohort preserved | PASS |
| Existing SBP national values and IMF raw rows reused | PASS |
| SBP BPM6 sign/framework crosswalk | PASS |
| Separate asset numeric comparison | PASS |
| Separate liability numeric comparison | PASS |
| Exact observation-level same-vintage bridge | NOT_ESTABLISHED |
| PAK full national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 7. Protected invariants
₹0; official/free sources only; no IMF re-query; no cohort rebuild; no synthetic values, fabricated timestamps, unsupported FX/sign/scale conversion, stock-flow substitution, netting, or aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
