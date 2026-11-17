# IMF BOP Portfolio Indicator Semantic Crosswalk — 2026-11-17

## Decision
The official metadata capture passed. The exact IMF:BOP_BPM6:1.0 dataflow references IMF:ECOFIN_DSD:1.0, not IMF:BOP:2.6.0. Therefore the structures are not treated as identical. A definition-based semantic candidate crosswalk is built between BOP DSD concepts and the dataflow's allowed indicator codes.

## Source evidence
- BOP DSD: IMF:BOP:2.6.0, 895,438 raw bytes.
- Dataflow: IMF:BOP_BPM6:1.0, 22,078 raw bytes.
- Dataflow's actual referenced DSD: IMF:ECOFIN_DSD:1.0, 42,707,649 raw bytes.
- Constraint: IMF:BOP_BP6_CONSTRAINT:1.0, 18,675 raw bytes.
- All four endpoints returned HTTP 200 and application/xml; exact request/final URLs, UTC retrieval timestamps, byte lengths and SHA-256 are in the immutable capture manifest.
- Capture ID: 20261117T134325Z. GitHub Actions Run #2 / ID 44095286184 SUCCESS; commit bd2a7d123b949f4ffcc426608a36de706a8fd658.

## Semantic candidates
- BOP DSD `CL_FUNCTIONAL_CAT` code `P`: Portfolio Investment.
- BOP DSD `CL_ACCOUNT_ENTRY` code `A`: Assets (Net Acquisition of).
- BOP DSD `CL_ACCOUNT_ENTRY` code `L`: Liabilities (Net Incurrence of).
- BOP_BPM6 dataflow's ECOFIN_DSD uses `DATA_DOMAIN`, `REF_AREA`, `INDICATOR`, `COUNTERPART_AREA`, `FREQ`, `TIME_PERIOD`; the BOP concept dimensions are not the same dimensions.
- Constraint explicitly allows `BFPA_BP6_USD` (portfolio investment, net acquisition of financial assets) and `BFPL_BP6_USD` (portfolio investment, net incurrence of liabilities), plus EUR and XDC variants.
- `BFP_BP6_EUR` aggregate portfolio investment appears in the constraint; `BFP_BP6_USD` aggregate does not. Do not infer that the aggregate USD series is available.
- The allowed portfolio indicator candidates are extracted from the exact 98 allowed indicator values and reconciled to the referenced DSD's `CL_INDICATOR` code names/annotations.

## Interpretation limits
- BFPA is not gross capital inflow; it is net acquisition of financial assets.
- BFPL is not equity-only foreign portfolio investment; it is net incurrence of liabilities and includes the portfolio investment aggregate as defined by IMF metadata.
- No country-level observation, coverage, vintage, actual-vs-estimate flag or publication-lag acceptance is proven by this crosswalk.
- No BOP DSD-to-ECOFIN DSD formal equivalence is asserted. This is a metadata-definition candidate mapping only.
- No production overlay integration or trading-trigger use is authorized.

## Acceptance
- Raw capture integrity and XML semantic identity: PASS.
- Dataflow's declared DSD identity followed and captured: PASS.
- Dataflow/constraint attachment: PASS.
- Portfolio indicator definitions reconciled to allowed constraint values: pending runtime QA.
- Country observation panel / EM coverage / PIT vintage: NOT_DONE.
