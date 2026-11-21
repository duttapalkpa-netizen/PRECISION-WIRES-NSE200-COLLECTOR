# GCR 63-country Q2-2026 national validation master matrix — reconciliation (Continuation 201)

Date: 2026-11-21 (Asia/Kolkata)

## Decision

The existing Continuation 200 matrix was independently reconciled against the immutable 63-country cohort. All 63 country codes match exactly, with no missing, extra or duplicate country rows. The CSV has been extended with eight explicit per-country status flag columns so that the requested states are machine-filterable. This is a roster/status inventory, not a claim that all national validations are complete.

## Preflight and immutable inputs

- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, Continuation 200 report, matrix CSV and immutable cohort CSV before editing.
- Immutable cohort: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`; blob SHA-1 `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- Cohort rows: 63; unique country codes: 63; every row has both IMF Q2-2026 panel entries present.
- Continuation 200 source matrix was preserved as the starting point; no cohort rebuild, country addition/deletion, IMF re-query or national data inference.
- Continuation 200 report: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_CONTINUATION200_20261121.md`.

## Exact reconciliation result

- Cohort rows: 63.
- Matrix rows: 63.
- Unique country codes in each: 63.
- Missing cohort members in matrix: 0.
- Extra matrix members: 0.
- Duplicate matrix country codes: 0.

### Current stage counts (mutually exclusive)

| Stage | Countries |
|---|---:|
| NOT_STARTED | 1 |
| SOURCE_FOUND | 20 |
| DATA_CAPTURED | 23 |
| BLOCKED | 19 |
| **Total** | **63** |

### Independent validation-gate counts (overlapping)

| Requested status | Countries |
|---|---:|
| ASSET_PASS | 15 |
| LIABILITY_PASS | 15 |
| VINTAGE_PASS | 0 |
| FULL_PASS | 0 |

The stage counts and gate counts are not additive to one another: a country can be DATA_CAPTURED and have one or both leg gates PASS, while its vintage remains pending. No country currently meets FULL_PASS.

## CSV enhancement

Updated `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv` with explicit boolean columns:

- `status_NOT_STARTED`
- `status_SOURCE_FOUND`
- `status_DATA_CAPTURED`
- `status_ASSET_PASS`
- `status_LIABILITY_PASS`
- `status_VINTAGE_PASS`
- `status_FULL_PASS`
- `status_BLOCKED`

Each flag is YES/NO and derives only from the existing row's current_stage, asset_gate, liability_gate, vintage_gate and full_pass fields. It does not upgrade any country or alter the original evidence notes.

CSV update commit: `f596dc889642e3a9262f2fd7b7dc9b02a6a57a0a`; resulting blob SHA-1: `45e466c72c034d460dfccf57474b07bfb6d12ea9`.

## Interpretation: how many remain?

- 63/63 rows are now accounted for in the matrix.
- 48 countries are not yet at DATA_CAPTURED stage (20 SOURCE_FOUND + 19 BLOCKED + 1 NOT_STARTED = 40; the remaining 8? No — this subtotal is 40, not 48). The correct count of countries below DATA_CAPTURED is **40**.
- 23/63 are DATA_CAPTURED, but none has passed the vintage gate; therefore none is FULL_PASS.
- 15 asset gates and 15 liability gates pass independently; these are overlapping country sets and do not imply same-vintage/full country validation.
- 63-country aggregate remains NOT_AUTHORIZED.

## Status semantics and safeguards

- NOT_STARTED: no country-specific national-source task/report was found in the bounded repository inventory; not proof no source exists.
- SOURCE_FOUND: official source/locator exists, but Q2 separate national portfolio transaction legs have not been captured.
- DATA_CAPTURED: national Q2 values are recorded in a report; this alone does not pass either leg.
- ASSET_PASS / LIABILITY_PASS: independent per-leg source/concept/unit/sign/rounding acceptance only.
- VINTAGE_PASS: requires an exact source revision/vintage bridge; publication-date proximity or rounded numerical match is insufficient.
- FULL_PASS: requires both leg passes, vintage pass, provenance/raw-byte and unit/sign/period acceptance, and no unresolved scope issue.
- BLOCKED: named route/access dependency prevents the next required capture; it does not mean the data do not exist.
- UNKNOWN is never PASS. No IIP stocks as flows, H1/annual allocation, net-to-leg back-solving, unsupported FX/sign/scale transform, synthetic values or fabricated timestamps.

## Next exact work

1. Keep the 63-row matrix as the single country-status index.
2. Select the next country only by rechecking the latest country report and current priority queue; skip all PASS gates and do not retry closed routes.
3. For each country update, preserve the previous evidence and record report reference, official source locator, retrieval receipt/raw bytes/hash, Q2 period, both leg outcomes, unit/sign, and vintage.
4. Promote a country to FULL_PASS only when all acceptance criteria are met. Do not authorize the GCR aggregate before the defined cohort inclusion rule is satisfied.

## Protected invariants

₹0; official/free sources only; no synthetic data, fabricated timestamps, unsupported conversion, stock-as-flow, net-to-leg back-solving, IMF re-query or cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. Aggregate NOT_AUTHORIZED.
