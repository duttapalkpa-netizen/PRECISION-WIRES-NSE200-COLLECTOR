# IMF BOP four-reporter series and observation attribute audit

Audit date: 2026-11-15 UTC
Dataset: `IMF.STA:BOP(21.0.0)`
DSD: `IMF.STA:DSD_BOP(24.0.0)`
Series: portfolio financial flows (`P_F`), USD, quarterly; assets `A_NFA_T`, liabilities `L_NIL_T`.
Scope: re-open and parse the previously accepted 2000-Q1–2014-Q4 and 2015-Q1–2025-Q4 raw response artifacts. No new observation API calls.

## 1. Source artifact integrity

Both downloaded artifact ZIPs were re-hashed and match their prior recorded values:
- Historical Run #43626075930, Artifact #14125219608; ZIP SHA-256 `539e34fca42394d5ae53da27d44243f7aea6c79a1631178465f351b5d8bf1157`.
- Recent Run #43624740474, Artifact #14125517628; ZIP SHA-256 `daaedd6c4d186ac87ba6694ff3ae4816b544ba487fd12589b1b128b87f6cc861`.

The four raw response bodies were also re-hashed and matched the accepted historical/recent report:
- Historical assets: `93025fe023aac9d301f6799d13ada7b0f04d27703012d8b3e1373db6c5527226`.
- Historical liabilities: `78ffa2a1492667cc2979f357acafecb490875a80f609726838f1be5ea44b5d25`.
- Recent assets: `68f865c2578f5d3dd21a145de71c0cb1f731041bf7b626fb5d1d3cd64e704664`.
- Recent liabilities: `b6875e20f20b279b2ce17131a42ba4af320adbc61f9c3bd28e9fb1067e597db1`.

## 2. Exact series-level metadata extracted

The existing responses requested `attributes=all`. Parsed the SDMX series attribute index and observation attribute index using the attribute order returned by the same response structure. Eight exact series keys were found for DZA, ETH, HTI and ZWE; one key (ZWE historical liabilities) has zero observations.

| Reporter | Side | Period / observations | IFS_FLAG | Methodology |
|---|---|---|---|---|
| ETH | Assets | 2003-Q1–2009-Q4, 28 | true | BPM6 |
| ETH | Assets | 2024-Q1–2024-Q4, 4 | true | BPM6 |
| ETH | Liabilities | 2003-Q1–2009-Q4, 28 | null | BPM6 |
| HTI | Assets | 2004-Q4–2012-Q3, 32 | true | BPM6 |
| HTI | Liabilities | 2004-Q4–2012-Q3, 32 | null | BPM6 |
| DZA | Assets | 2021-Q1–2025-Q4, 20 | true | BPM6 |
| ZWE | Liabilities | 2017-Q1–2025-Q4, 36 | null | BPM6 |
| ZWE | Liabilities | no observations | null | BPM6 |

Series-level attributes across all eight keys:
- `SCALE=6`; `METHODOLOGY=BPM6`.
- `DECIMALS_DISPLAYED` and `OVERLAP` are null.
- `IFS_FLAG=true` on the four observed asset-series keys; null on the three observed liability-series keys and the empty ZWE liability series key.
- This is a descriptive pattern in the selected series only. Null is not interpreted as false, not treated as an eligibility code, and not used to infer why a series is absent.

## 3. Observation-level attribute audit

Across the 180 non-empty observations (28+32+28+32+20+4+36):
- `PRECISION=6` on all 180.
- `DERIVATION_TYPE=O` on all 180 (raw code preserved; no semantic expansion made).
- `ACCESS_SHARING_LEVEL=PUBLIC_OPEN` on all 180.
- `SECURITY_CLASSIFICATION=PUB` on all 180.
- `STATUS`, `ACCESS_SHARING_NOTES`, and `SOURCE` are null on all 180.
- The historical ZWE liabilities series key has zero observations; no observation attributes exist for that empty key.

No null observation status was converted to “normal”, “final”, “not confidential”, or any other inferred state. No null source was inferred. No scale multiplier or unit conversion was applied.

## 4. Reconciliation result

This audit strengthens the description of the four reporters with observed values, but does not establish eligibility for any of the 39 countries with no observations in either tested window.

- 4/43 priority codes have at least one observation somewhere in 2000-Q1–2025-Q4: DZA, ETH, HTI, ZWE.
- 39/43 still have no returned observations in either tested interval.
- DZA assets only; ETH both sides but separated/incomplete spans; HTI both sides only in 2004-Q4–2012-Q3; ZWE liabilities only.
- The IFS_FLAG pattern is side-asymmetric in these four reporters (true on selected assets; null on selected liabilities). This does not mean liabilities are ineligible or non-IFS; missing attribute semantics remain UNKNOWN.
- Reporter-specific applicability/eligibility for the 39 absent countries remains UNKNOWN.
- Historical coverage acceptance remains NOT PASS; EMDE aggregation remains BLOCKED.

## 5. Derived evidence artifact

- CSV: `data/research/IMF_BOP_4_REPORTER_ATTRIBUTE_AUDIT_20261115.csv`
- Rows: 8 exact series keys.
- CSV SHA-256: `cf88ebfd39bd934a16ceac11cb08015426061c00290c4083e74b661d948c5cc1`.
- The CSV records all series attributes, observation-attribute distributions, period spans and the corresponding raw body SHA-256. The source raw responses remain in their original GitHub Actions artifacts; they were not modified.

## 6. Next step

The remaining high-value gap is reporter-specific applicability for the 39 no-observation countries. DSD codelists alone enumerate allowed dimension codes, not country-by-series reporting obligations. The next investigation must find official IMF reporting/applicability documentation or country-specific metadata that explicitly links reporters to this exact `BOP_ACCOUNTING_ENTRY × INDICATOR × UNIT × FREQUENCY` combination. If no such public rule exists, keep eligibility UNKNOWN. Do not run EMDE aggregation or reinterpret absent observations as zero/ineligibility.

## 7. Invariants

₹0 spend; public official IMF evidence only; no credentials, paid APIs, synthetic rows/timestamps, external contact, PR merge, or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56 × 12), engines A–E and Hard Gate unchanged.
