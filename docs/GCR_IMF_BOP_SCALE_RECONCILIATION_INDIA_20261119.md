# IMF BOP Scale / Sign Reconciliation — India
Date: 2026-11-19
Status: **PASS — 12/12 comparisons across six calendar quarters**

## Progress Log
### Completed
- Captured RBI Table 197 official BPM6 quarterly Balance of Payments page (USD million).
- Mapped RBI “Portfolio Investment in India” to IMF `L_NIL_T` (liabilities), and RBI “Portfolio Investment by India” to IMF `A_NFA_T` (assets) with the required sign reversal.
- Reconciled six calendar quarters, 2024-Q2 through 2025-Q3: 12/12 comparisons PASS within the RBI page's integer-million rounding bound.
- Raw RBI HTML and machine-readable comparison files are archived in GitHub.

### Rejected
- The old 2019 RBI Table 196 comparison is not used: it was an older table and the quarter label was not aligned in the initial comparison.
- No generalization to the other 152 EMDE members without additional country-level cross-checks.
- No production signal or aggregate release.

### Next actions
1. Validate at least one additional EMDE country against its official national BPM6 source.
2. Add country-specific vintage/revision controls; RBI states Table 197 data are subject to revision.
3. After enough country checks, apply the Brazil/India-validated scale convention to a pilot multi-country subset, then reconcile coverage and aggregate.

## 1. Official RBI source
- Table 197: “Standard Presentation of India’s Balance of Payments as per BPM6 — Quarterly — US Dollar”
- Publication date: 31 July 2026.
- Unit: US$ million; quarterly; standard BPM6 classification; credit, debit and net values shown separately.
- Source page: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24022
- RBI handbook (April 2026) defines Table 42 as quarterly, US$ million, BPM6, with financial account by functional classification; the DBIE provides longer historical series. The current Table197 page is the selected published data source for this comparison.

## 2. Mapping and method
- RBI `3.2.A Portfolio Investment in India` (credit − debit net) maps to IMF `L_NIL_T` (net incurrence of liabilities), with no sign reversal.
- RBI `3.2.B Portfolio Investment by India` (credit − debit net) maps to IMF `A_NFA_T` (net acquisition of financial assets) after sign reversal: `IMF asset = − RBI net`.
- IMF raw `OBS_VALUE / 1,000,000` is compared with the RBI value in USD million.
- RBI Table197 displays integer USD millions; maximum rounding error per displayed net value is 0.5 million USD.
- Calendar alignment is explicit: April–June = Q2; July–September = Q3; October–December = Q4; January–March = Q1.

## 3. Results
<text>All values are USD million. RBI asset net is sign-reversed for comparison with IMF A_NFA_T.</text>

| IMF quarter | RBI period | Entry | RBI comparable | IMF raw ÷ 1e6 | Residual | Result |
|---|---|---|---:|---:|---:|---|
| 2024-Q2 | Apr–Jun 2024 | Assets | -48 | -47.510029 | 0.489971 | PASS |
| 2024-Q2 | Apr–Jun 2024 | Liabilities | 897 | 897.230199 | 0.230199 | PASS |
| 2024-Q3 | Jul–Sep 2024 | Assets | -35 | -34.990039 | 0.009961 | PASS |
| 2024-Q3 | Jul–Sep 2024 | Liabilities | 19,815 | 19,815.071032 | 0.071032 | PASS |
| 2024-Q4 | Oct–Dec 2024 | Assets | -63 | -62.610017 | 0.389983 | PASS |
| 2024-Q4 | Oct–Dec 2024 | Liabilities | -11,435 | -11,434.646504 | 0.353496 | PASS |
| 2025-Q1 | Jan–Mar 2025 | Assets | -136 | -135.999311 | 0.000689 | PASS |
| 2025-Q1 | Jan–Mar 2025 | Liabilities | -5,995 | -5,994.630947 | 0.369053 | PASS |
| 2025-Q2 | Apr–Jun 2025 | Assets | 872 | 872.453922 | 0.453922 | PASS |
| 2025-Q2 | Apr–Jun 2025 | Liabilities | 2,481 | 2,480.700912 | -0.299088 | PASS |
| 2025-Q3 | Jul–Sep 2025 | Assets | 279 | 278.550001 | -0.449999 | PASS |
| 2025-Q3 | Jul–Sep 2025 | Liabilities | -5,468 | -5,468.379504 | -0.379504 | PASS |

- 12/12 PASS; 0 REVIEW; 0 missing.
- Maximum absolute residual: 0.4899709189 million USD, within the 0.5 million integer-rounding bound.
- The sign mapping also matches across both legs.

## 4. Decision
For the India BOP P_F series tested, the empirically validated normalization is:
`USD_million = OBS_VALUE / 10^6`.
The asset sign must be compared as the negative of RBI's “Portfolio Investment by India” credit-minus-debit net; liabilities compare directly to RBI's “Portfolio Investment in India” net.
This confirms the Brazil-derived scale/sign convention also for India over six quarters. It does not authorize applying it to all 154 EMDE members or to unvalidated vintages.

## 5. Reproducibility
- Workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476434148
- Artifact ID: `14506542277`; ZIP 28,097 bytes; SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`.
- Raw RBI HTML: 146,017 bytes; SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`.
- Durable evidence commit: `451b9e203fd6edb1541c42432b47a393e030372c`.
- Evidence folder: `docs/evidence/imf_bop_emde_20261119/india_scale_reconciliation/`.

## 6. Decision boundary
- Brazil scale/sign validation: PASS (10/10).
- India scale/sign validation: PASS (12/12).
- Remaining 152 WEO EMDE members: UNKNOWN pending official national-source checks.
- No EMDE-wide conversion/aggregate is yet authorized. No synthetic rows, forward-fill or production signal. CORE-672, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and Engines A–E remain unchanged.


## Supersession note — additional countries validated
This India 12/12 result remains valid. Additional country benchmarks are now documented in `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART3_20261119.md`: Brazil 94/94, Mexico 6/6, and Chile 6/6 against the 2026-09 source vintage. The current Chile 2026-11 vintage differs for four Q1/Q2 comparisons; keep the revision/vintage gate open.
