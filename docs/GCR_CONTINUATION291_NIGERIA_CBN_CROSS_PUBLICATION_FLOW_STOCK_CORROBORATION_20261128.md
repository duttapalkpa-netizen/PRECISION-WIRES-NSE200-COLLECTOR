# GCR Continuation 291 — Nigeria Q2-2026 CBN cross-publication flow/stock corroboration (28-Nov-2026)

## Objective
Use a second official Central Bank of Nigeria publication to corroborate the already captured Q2-2026 portfolio investment transaction legs, while keeping BOP flows separate from IIP stocks. Research-only; no country gate promotion and no production admission.

## Preflight and duplicate prevention
- Reused the fixed 63-country Q2-2026 cohort and existing Nigeria report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md`.
- Reused existing CBN Q2-2026 BOP Highlights evidence; no IMF re-query, no cohort rebuild, no repeated CBN download.
- Retrieved/inspected a distinct official CBN publication: `CBN Economic Report, Second Quarter 2026`, official PDF:
  https://www.cbn.gov.ng/Out/2026/RSD/Second%20Quarter%202026%20Economic%20Report.pdf
- Compared the financial-account portfolio figures in the Economic Report with the existing official Q2-2026 BOP Highlights PDF:
  https://www.cbn.gov.ng/Out/2026/STD/Q2%202026%20BOP%20Highlights_%20revised.pdf

## Exact cross-publication corroboration

| Metric | Q2 2026 BOP Highlights | Q2 2026 Economic Report | Result |
|---|---:|---:|---|
| Portfolio investment assets (transaction flow) | USD 0.70bn | USD 0.70bn | Exact match |
| Portfolio investment liabilities (transaction flow) | USD 7.09bn | USD 7.09bn | Exact match |
| Q1 comparison — portfolio assets | USD 0.26bn | USD 0.26bn | Exact match |
| Q1 comparison — portfolio liabilities | USD 6.03bn | USD 6.03bn | Exact match |

Economic Report lines 2088–2092 separately state portfolio liabilities inflow USD 7.09bn and portfolio assets acquisition USD 0.70bn for Q2-2026, compared with Q1 values USD 6.03bn and USD 0.26bn. The BOP Highlights page 4 independently states the same Q2/Q1 figures.

## Financial-account arithmetic cross-check
The Economic Report states:
- Net acquisition of financial assets: USD 12.58bn.
- Net incurrence of financial liabilities: USD 10.84bn.
- Financial-account net lending: USD 1.74bn.

Arithmetic: 12.58 - 10.84 = 1.74 (exact at displayed precision). This is an internal consistency check for the broad financial-account totals, not a replacement for the portfolio component legs.

## Flow versus stock separation — critical safeguard
The same Economic Report's IIP section reports end-June 2026 positions:
- Portfolio investment assets stock: USD 6.51bn.
- Portfolio investment liabilities stock: USD 65.23bn.
- Total financial assets stock: USD 145.72bn.
- Total financial liabilities stock: USD 238.66bn.

These are end-period IIP stocks, not Q2 BOP transaction flows. They must remain in a separate stock table and must never be substituted for the USD 0.70bn / USD 7.09bn flow observations. The reported USD 0.70bn change in portfolio assets stock happens to numerically equal the Q2 asset flow at displayed precision, but this numerical coincidence does not make the concepts interchangeable.

## Interpretation and vintage boundary
- **PASS — independent publication corroboration:** Q2 and Q1 portfolio A/L figures match exactly across two distinct CBN publications.
- **PASS — broad financial-account arithmetic:** 12.58 - 10.84 = 1.74.
- **PASS — concept separation:** BOP transaction flows and IIP end-period stocks are explicitly identified and separated.
- **NOT PASS — same-vintage bridge:** Both publications are CBN Q2-2026 publications. The available evidence does not establish an observation-level release/revision identifier proving that the archived IMF Q2-2026 rows and both CBN publications represent the exact same statistical vintage. Do not promote VINTAGE_PASS.
- No raw source values were inferred, no flow was back-solved from net, and no IIP stock was used as a flow.

## Updated Nigeria gate
- Existing country status remains: DATA_CAPTURED; ASSET_PASS; LIABILITY_PASS; VINTAGE_PENDING; FULL_PASS=NO.
- This C291 report adds a second official CBN publication cross-check only. It does not change the 63-country matrix gate, cohort membership, aggregate authorization or production admission.
- Nigeria remains excluded from any FULL_PASS-only aggregate until same-vintage evidence is independently established.

## Research value added
This evidence improves source triangulation and reduces the risk of a transcription or single-document error for Nigeria's Q2-2026 portfolio legs. It also supplies a clear anti-confusion rule for GCR: BOP flows, IIP stocks, and broad financial-account totals are different measures and must occupy separate fields.

## Next exact work
1. Seek an explicit CBN/IMF observation vintage or revision-cutoff record linking the Q2-2026 portfolio A/L rows to the archived IMF receipt.
2. Apply the same two-publication corroboration and flow/stock separation pattern only to other DATA_CAPTURED cohort members where a genuinely distinct official publication exists; do not repeat closed source routes.
3. Preserve current gate statuses until the exact vintage bridge is proven.

## Invariants
₹0; official/free sources only; no paid API/licence/subscription, external contact, fabricated values, unsupported FX/sign/scale transforms, IIP-stock-as-flow, net-to-leg back-solving, or silent correction. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
