# India IMF BOP Current-Vintage Scale/Sign Supplement — 2026-11-19

## Relationship to the six-quarter baseline
The existing India report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md` remains valid: RBI Table197 (BPM6, USD million) validated 2024-Q2 through 2025-Q3, 12/12 PASS. This supplement adds later RBI Table42 source pages for 2025-Q1/Q2 and 2026-Q1/Q2. The overlapping 2025 quarters are cross-source confirmation; 2026-Q1/Q2 are the new current-year extension.

## Official sources
- RBI Table 42, “Standard Presentation of BoP in India as per BPM6 (US$ Million)”, Jan-Mar 2025 and Jan-Mar 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24424 (published 2026-08-25).
- RBI Table 42, same table, Apr-Jun 2025 and Apr-Jun 2026: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 (published 2026-10-23).
- Both pages were retrieved anonymously; raw HTML, retrieval timestamps, safe headers and SHA-256 are archived with this supplement.

## Mapping
- RBI 3.2.A “Portfolio Investment in India” credit-minus-debit net ↔ IMF `L_NIL_T` (net incurrence of liabilities), same sign.
- RBI 3.2.B “Portfolio Investment by India” credit-minus-debit net ↔ negative IMF `A_NFA_T` (net acquisition of financial assets).
- RBI 3.2 total portfolio investment net ↔ IMF `L_NIL_T - A_NFA_T`.
- RBI table unit is US$ million; diagnostic comparison uses IMF raw `OBS_VALUE / 1,000,000`. No raw IMF values are altered.
- RBI publishes integer US$ millions; tolerance ±US$0.5m.

## New four-quarter sample results
- 12 comparisons (assets, liabilities and combined net for 2025-Q1, 2025-Q2, 2026-Q1, 2026-Q2): 10 PASS, 2 REVIEW.
- 2025-Q1, 2025-Q2 and 2026-Q2: all three comparisons PASS within ±US$0.5m.
- 2026-Q1 asset leg PASS; liability and combined net REVIEW.
  - IMF liability: -13,633.508347 US$ million.
  - RBI 3.2.A net: -12,121 US$ million.
  - Residual: -1,512.508347 US$ million.
  - Combined net residual: -1,512.457994 US$ million.
- No silent adjustment, no substitution and no inferred cause. The discrepancy may reflect a vintage/revision or definition difference, but that is not established.

## Combined India evidence status
- Baseline six quarters 2024-Q2–2025-Q3: 12/12 asset/liability checks PASS.
- New 2026-Q1/Q2 leg extension: 3/4 PASS, 1 REVIEW.
- Across eight unique quarters, asset/liability checks: 15/16 PASS, 1 REVIEW.
- Combined net checks for 2025-Q1/Q2 and 2026-Q1/Q2: 3/4 PASS, 1 REVIEW.
- Therefore the operational conversion `OBS_VALUE/10^6` and sign mapping are strongly supported for India, but the current 2026-Q1 liability discrepancy remains open.

## Authoritative SCALE metadata
- BOP DSD SCALE enumerates `IMF:CL_UNIT_MULT(1.0.2)`; code 6 = Millions, description 10^6.
- Preserve the raw IMF observation, `UNIT=USD`, `SCALE=6`, `PRECISION` and derivation attributes. The derived USD-million comparison is a separate output.
- This evidence does not authorize universal numeric conversion for all 154 WEO G200 countries; national-source validation remains country- and vintage-specific.

## Reproducibility
- Workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44477031402
- Crosswalk artifact ID: `14505649659`; ZIP SHA-256 `8db4f9536a57df1e8635855af5bb90225de0f800e6e9164bd20d99d1f355b4e2`.
- Comparison CSV: `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/india_bop_scale_sign_crosswalk.csv`.
- RBI raw HTML hashes:
  - Jan-Mar 2025/2026: `a92ac0f8196efbd8f503984620d7c0291c6d704405e52d64eec4f96948ddf744`.
  - Apr-Jun 2025/2026: `075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396`.

## Decision
India scale/sign validation remains **PARTIAL for the latest current-year vintage**: the six-quarter historical baseline is 12/12 PASS, the 2026-Q2 extension passes, but 2026-Q1 liability/combined net is REVIEW. Do not blend the conflicting 2026-Q1 values or use the full panel for aggregate/backtest/production until vintage alignment is resolved. No paid data, no synthetic observations, no forward-fill, and no production selector/ranking/pressure-fade/CORE-672/Engines A–E changes.


## Continuation 187 — Q1-2026 RBI release-persistence addendum (2026-11-21)
- RBI official Q1 Table 43/42 releases inspected: 22-Jun-2026, 22-Jul-2026 and 25-Aug-2026. The published Q1 portfolio investment in India net remains -12,121 USDm in July/August; portfolio investment by India net +74 USDm; total -12,047 USDm. No published Q1 value change is evidenced across those releases.
- The archived IMF Q1 L_NIL_T remains -13,633.508347 USDm; the residual vs RBI -12,121 remains -1,512.508347 USDm. Asset remains PASS; liability and combined net remain REVIEW. No cause or same-vintage identity inferred.
- October 2026 Table42 used for Q2 in this supplement does not provide a later Q1 value. Preserve Q1 as PARTIAL / NOT PASS pending a distinct official RBI revision history/transaction-level series or already archived IMF revision metadata.
- C187 detail: `docs/GCR_INDIA_IND_Q1_2026_RBI_TABLE42_RELEASE_PERSISTENCE_AUDIT_CONTINUATION187_20261121.md`.
