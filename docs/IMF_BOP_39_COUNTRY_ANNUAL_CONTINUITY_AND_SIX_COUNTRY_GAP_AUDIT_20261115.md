# IMF BOP 39-country annual continuity and six-country missing-series audit

Audit date: 2026-11-15
Source evidence: immutable artifact #14128182046 from successful Run #43630656519.
Source artifact ZIP SHA-256: `058ae62904bec701959175076d3d2aa9de20f402eb3425083bbfad2d36accc12`.
Source dataset: `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`.
Exact series: assets `A_NFA_T.P_F.USD.A`; liabilities `L_NIL_T.P_F.USD.A`.
Observation window: 2000–2025 inclusive. Target set: exact 39 countries from the preceding quarterly-gap audit.

## 1. Reproducibility and validation

The two original raw SDMX-JSON response bodies were read from the downloaded, SHA-256-verified source artifact. The audit decoded SDMX attribute indexes using the value lists in the response structure; it did not mistake integer indexes (for example, 0) for the attribute values (for example, SCALE=6 or METHODOLOGY=BPM6).

The observation-year list is derived only from non-null observation values whose TIME_PERIOD is 2000–2025. The year grid is explicitly 2000 through 2025. No fill, interpolation, extrapolation, annual-to-quarterly conversion, or synthetic rows were used.

Outputs:
- Side matrix: 78 rows (39 countries × 2 series), SHA-256 `69840fa287cf14eb5d50e0ca51465720c315e1fda7b5bf1a594ad3777a7f805e`.
- Country summary: 39 rows, SHA-256 `3003f065ed3d1b459c5c932b19ab6882b4be4ccbe8968600d2d0391097842259`.
- Detailed JSON audit: SHA-256 `090174bf4f89750c5425f779a8dda826345ab51d05f31b94caf281aaf6baa258`.
- Source artifact raw response hashes remain: assets `711431c957199292cfb37e884a3e9344e7e519e23e9bb4baea2ff9f5523addfc`; liabilities `a256a5f5baaef80f48e7d3747c39db80d644078b896abe49a5190f21003b60aa`.

## 2. Continuity results

| Measure | Assets | Liabilities |
|---|---:|---:|
| Countries with ≥1 observation | 33/39 | 31/39 |
| Countries with all 26 years (2000–2025) | 9 | 9 |
| Countries with latest observation in 2025 | 13 | 11 |
| Countries with at least one interior missing year between first and last observation | 3 | 6 |
| Interior missing years across reporters | 9 | 29 |
| Total non-null observations across target set | 649 | 599 |

Nine reporters have all 26 years on both sides: `ATG, DMA, GRD, KEN, KNA, LCA, MDV, OMN, VCT`. This is the only complete 26-year annual subset demonstrated by this audit. The other 22 reporters with both-side observations have a truncated span and/or gaps; do not call them continuous.

Largest observed interior-gap counts:
- Assets: MWI 5 years, COG 3, GAB 1.
- Liabilities: MHL 9 years, LBY 8, COG 5, SLE 4, GNB 2, GAB 1.

A series may have missing years before its first or after its last observation; those are edge gaps, not interior gaps. The full side matrix records the exact observed years, every missing year within the 26-year window, first/last year, longest consecutive run, and internal gap ranges for each country and side.

## 3. Attribute decoding and coverage

For the 39 target reporters' non-null annual observations:
- Assets: 649 observations; `DERIVATION_TYPE=O` (649), `ACCESS_SHARING_LEVEL=PUBLIC_OPEN` (649), `SECURITY_CLASSIFICATION=PUB` (649), `STATUS=null` (649), `SOURCE=null` (649). `PRECISION=6` for 558 and null for 91.
- Liabilities: 599 observations; `DERIVATION_TYPE=O` (599), `ACCESS_SHARING_LEVEL=PUBLIC_OPEN` (599), `SECURITY_CLASSIFICATION=PUB` (599), `STATUS=null` (599), `SOURCE=null` (599). `PRECISION=6` for 516 and null for 83.

Series-level attributes on non-empty target series:
- Assets: SCALE=6 and METHODOLOGY=BPM6; IFS_FLAG=true on all 33 series with observations.
- Liabilities: SCALE=6 and METHODOLOGY=BPM6; IFS_FLAG is null on all 31 series with observations.

These are recorded metadata values only. The meaning or eligibility effect of `IFS_FLAG` is not inferred. Null STATUS/SOURCE/precision fields remain null.

## 4. Six countries with no non-empty annual observations on either side

| Code | Assets series state | Liabilities series state |
|---|---|---|
| CAF | Empty key; SCALE=6, BPM6, IFS_FLAG=true | Empty key; SCALE=6, BPM6, IFS_FLAG=null |
| ERI | No series key returned | No series key returned |
| GNQ | Empty key; SCALE=6, BPM6, IFS_FLAG=true | Empty key; SCALE=6, BPM6, IFS_FLAG=null |
| SOM | Empty key; SCALE=6, BPM6, IFS_FLAG=true | Empty key; SCALE=6, BPM6, IFS_FLAG=null |
| TCD | Empty key; SCALE=6, BPM6, IFS_FLAG=true | Empty key; SCALE=6, BPM6, IFS_FLAG=null |
| TKM | Empty key; SCALE=6, BPM6, IFS_FLAG=true | No series key returned |

The prior 39-country annual result is thereby refined: four countries have empty series keys on both sides (CAF, GNQ, SOM, TCD); TKM has an empty assets key and no liabilities key; ERI has no key returned on either side. Empty series keys contain no non-null observations. These states do not establish formal ineligibility, non-reporting, suppression, or economic zero.

## 5. Coverage and gate decision

- Annual continuity audit: PASS as a descriptive audit of the archived response.
- 26-year complete annual continuity: demonstrated for 9/39 on both sides, not for the other 30.
- Annual frequency reachability: previously PASS for 31 both-side reporters plus 2 assets-only reporters.
- Quarterly reporter eligibility: UNKNOWN.
- Quarterly coverage acceptance: NOT PASS.
- EMDE aggregation: BLOCKED.

No annual values are substituted into quarterly research. No aggregation, rescaling, annualization, or synthetic data was performed.

## 6. Next action

For the six no-observation countries, inspect authoritative IMF country-specific reporting metadata and dataflow constraints, and determine whether any alternative documented account/unit/frequency is relevant. Do not broaden the series definition without documenting the exact series and rationale. For the 22 both-side reporters with incomplete annual continuity, keep their exact gaps visible; only the nine fully observed reporters can be tagged as complete for this 26-year annual window. Continue to keep quarterly eligibility UNKNOWN until direct quarterly evidence or an authoritative reporting rule supports a change.

## 7. Protected invariants

₹0 spend; official free source data only; no credentials, paid API, external contact, synthetic observations, or PR merge. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, engines A–E, and Hard Gate unchanged.
