# IMF BOP EMDE quarterly portfolio reporter coverage audit

Audit date: 2026-11-14 (UTC)
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
DSD: `IMF.STA:DSD_BOP(24.0.0)`
EMDE membership basis: IMF WEO April 2026, 154-member list; exact dataset-specific `CL_BOP_COUNTRY(1.0.0)` crosswalk.
Observation scope: portfolio financial flows (`P_F`), USD, quarterly, 2015-Q1 through 2025-Q4 (44 quarters), assets `A_NFA_T`, liabilities `L_NIL_T`.
Method: public unauthenticated SDMX 3.0 wildcard query `*` over the COUNTRY dimension; no country aggregation, netting, unit conversion, scaling, forward-fill, or synthetic rows.

## 1. Verified run and artifacts

- Corrected coverage Run #43624740474 — SUCCESS.
- Workflow URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43624740474
- Commit: `e2bcf99383c0ddaa54c089ac2a30c2f06e38a45b`.
- Job ID: `132537959631`.
- Artifact ID: `14125517628`.
- Artifact ZIP SHA-256: `daaedd6c4d186ac87ba6694ff3ae4816b544ba487fd12589b1b128b87f6cc861`.
- Artifact contains raw response bodies, parsed reporter inventories and two 154-row EMDE coverage matrices. ZIP downloaded and inspected.
- Assets raw response: 320,788 bytes; SHA-256 `68f865c2578f5d3dd21a145de71c0cb1f731041bf7b626fb5d1d3cd64e704664`.
- Liabilities raw response: 310,236 bytes; SHA-256 `b6875e20f20b279b2ce17131a42ba4af320adbc61f9c3bd28e9fb1067e597db1`.
- Assets coverage CSV: 154 rows; SHA-256 `5939c155abcbdb5687f41d8f79831f02a75da02a9dda2d85aae9b748d0bc7cdc`.
- Liabilities coverage CSV: 154 rows; SHA-256 `726f4fcfdaa7f41b165bf9d4ff837bf0c3708e472249d2d78f94fea1ea8654cc`.

The exact series dimension order was checked as COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY; observation dimension was TIME_PERIOD. Every returned series key matched the requested account/indicator/unit/frequency. Values were non-null and finite; periods were unique and within the requested interval.

## 2. Observation-based coverage results

| Metric | Assets A_NFA_T | Liabilities L_NIL_T |
|---|---:|---:|
| WEO EMDE members in denominator | 154 | 154 |
| EMDE reporters with at least one observation | 113 | 112 |
| Coverage rate | 73.38% | 72.73% |
| No series returned in selected range | 41 | 42 |
| Present reporters with all 44 quarters | 88 | 84 |
| Present reporters with fewer than 44 quarters | 25 | 28 |
| Total returned reporter series (all country codes) | 156 | 155 |
| Returned non-EMDE reporter codes | 43 | 43 |

Cross-series comparison:
- 111 EMDE reporters have both asset and liability series.
- 2 have assets but no liability series in this filtered interval: DZA (Algeria), ETH (Ethiopia).
- 1 has liabilities but no asset series in this filtered interval: ZWE (Zimbabwe).
- 40 EMDE members have no series returned for either side in the selected 2015-Q1 to 2025-Q4 query.
- 114/154 (74.03%) have at least one side; 111/154 (72.08%) have both sides.
- 83/154 have both sides with all 44 quarterly observations.
- 28 have both sides present but at least one side is partial.
- Asset-only and liability-only results are not treated as complete country coverage.

## 3. The 40 codes with no series returned on either side

`ARE, ATG, BEN, BFA, BRB, CAF, CIV, COG, COM, DMA, ERI, FSM, GAB, GNB, GNQ, GRD, HTI, IRN, KEN, KNA, LBY, LCA, MDV, MHL, MLI, MWI, NER, NRU, OMN, PLW, SEN, SLE, SOM, SSD, SYR, TCD, TGO, TKM, TUV, VCT`.

These are **NO SERIES RETURNED FOR THIS EXACT FILTER AND PERIOD**, not proof that the country never reports BOP data. The 2015–2025 period filter and selected portfolio flow/account/quarterly/US-dollar dimensions define the test. No reason for absence (non-reporting, suppression, confidentiality, data gap, code mapping, or API behavior) is inferred. Keep the status UNKNOWN pending targeted historical/metadata investigation.

## 4. Coverage depth matters

The 113/112 counts mean at least one quarter was returned, not full period coverage. Among EMDE reporters with any series:
- Assets: 88/113 have 44/44 quarters; 25/113 are partial.
- Liabilities: 84/112 have 44/44 quarters; 28/112 are partial.
- Only 83 EMDE reporters have complete 44-quarter coverage on both sides.
- Partial series include early starts, early stops and internal gaps; do not fill gaps or infer continuity from first/last period alone.

## 5. False-positive query lesson and workflow hardening

An earlier run #43624650170 used the literal `all` as the COUNTRY key. Both HTTP requests returned 200 and parsed, but yielded zero reporter series; the workflow incorrectly completed SUCCESS because it checked only HTTP/parse status. This is a false-positive diagnostic and must not be treated as a valid 0/154 coverage result.

The valid wildcard token is `*`, used in Run #43624740474. It returned 156 asset reporter series and 155 liability reporter series and the full 154-row crosswalk comparisons.

Workflow hardening commit: `735f9191317aa578e8cccc8148c1e8ca9482574c`.
- Workflow now rejects zero reporter series as an error.
- Push-triggered automatic reruns were disabled; manual dispatch only, to avoid redundant expensive queries.
- The earlier false-positive run remains preserved as a diagnostic, not deleted or relabelled.

## 6. Acceptance matrix

| Gate | Status |
|---|---|
| 154 WEO EMDE members mapped to exact BOP COUNTRY codes | PASS (prior crosswalk evidence) |
| Public exact BOP dataflow and DSD identity | PASS (prior metadata evidence) |
| Asset wildcard query HTTP 200 and parse | PASS |
| Liability wildcard query HTTP 200 and parse | PASS |
| Exact series dimensions/keys and finite observations | PASS |
| 154-row asset coverage matrix generated | PASS |
| 154-row liability coverage matrix generated | PASS |
| Full 154/154 reporter coverage for assets | NOT PASS — 113 present, 41 no series in range |
| Full 154/154 reporter coverage for liabilities | NOT PASS — 112 present, 42 no series in range |
| Both sides complete for all 44 quarters across 154 EMDE | NOT PASS — 83 complete on both sides |
| Missing-series causes resolved | UNKNOWN |
| EMDE aggregation eligibility | BLOCKED |

**Work-package result: QUERY AND COVERAGE AUDIT PASS; DATA COVERAGE GATE NOT PASS; AGGREGATION BLOCKED.**

## 7. Next action

Run a targeted historical reach-back for the 40 codes absent on both sides and the 3 asymmetric cases, using the same exact dataflow and dimensions but a clearly documented earlier interval (start with 2000-Q1 to 2014-Q4). This distinguishes "not present in the recent 2015–2025 interval" from "no historical series in the earlier interval". Preserve UNKNOWN if still absent. Separately investigate partial-quarter gaps for the 28 both-present incomplete reporters. Do not aggregate until country coverage, period continuity, observation attributes, flags and revision/vintage rules are verified.

## 8. Invariants

₹0 spend; official public sources only; no credentials or authentication bypass; no synthetic values/timestamps; no external contact; no PR merge; no production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.
