# India BOP Portfolio-Flow Scale/Sign Crosswalk — 2026-11-19

## Scope
Compare four calendar quarters of IMF BOP India portfolio-flow series with RBI Table 42, “Standard Presentation of BoP in India as per BPM6 (US$ Million)”. This is a country-period crosswalk, not a full-history pass.

## Source mapping
- RBI 3.2.A Portfolio Investment in India net ↔ IMF `L_NIL_T` (net incurrence of liabilities).
- RBI 3.2.B Portfolio Investment by India net ↔ negative IMF `A_NFA_T` (net acquisition of assets).
- RBI 3.2 Portfolio Investment net ↔ IMF `L_NIL_T - A_NFA_T`.
- RBI table values are US$ million; IMF raw `OBS_VALUE` is divided by 1,000,000 only for this comparison. Stored IMF values remain unchanged.
- Rounding tolerance: ±US$0.5 million because RBI publishes integer US$ million values.

## Results
- Comparisons: 12; PASS: 10; REVIEW: 2.
- 2025-Q1, 2025-Q2 and 2026-Q2: both asset and liability legs match RBI within ±US$0.5m; combined portfolio net also matches.
- 2026-Q1: asset leg matches, but liability leg and combined net do not. IMF liability = -13633.50834733219 US$ million; RBI 3.2.A net = -12121 US$ million. Residual = -1512.50834733219 US$ million. Do not silently reconcile or override.
- Therefore India scale/sign mapping is PARTIAL, not full-history PASS. The 2026-Q1 liability discrepancy remains REVIEW pending vintage/definition reconciliation.

## Provenance
- RBI Table 42 Jan-Mar 2025 / Jan-Mar 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424 (published 2026-08-25).
- RBI Table 42 Apr-Jun 2025 / Apr-Jun 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 (published 2026-10-23).
- Raw HTML bytes, retrieval timestamps, headers and SHA-256 are in `docs/evidence/imf_bop_20261119/india_scale_reconciliation/`.
- Full comparison rows: `docs/evidence/imf_bop_20261119/india_scale_reconciliation/india_bop_scale_sign_crosswalk.csv`.

## Decision
- Empirical unit scaling and sign mapping are supported for 3/4 tested quarters, with 1 material review.
- Do not apply the Brazil/India 10^6 conversion to other EMDE countries without independent official-source crosswalks.
- Do not aggregate, backtest or admit this panel to GCR production until missing-country coverage, scale crosswalks, point-in-time vintages and net-flow policy are closed.
- No synthetic data, no forward-fill, no paid API, no production selector/ranking/pressure-fade/CORE-672/Engines A–E changes.
