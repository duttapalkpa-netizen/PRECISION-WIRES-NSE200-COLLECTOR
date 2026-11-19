# Global Capital Rotation — IMF BOP Portfolio-Flow Pilot
Date: 2026-11-19

## Outcome
**Anonymous IMF BOP observations access VERIFIED for the IMF.STA:BOP 21.0.0 dataflow. Brazil and India raw portfolio-flow pilot PASS. Economic scale reconciliation and EM aggregation remain BLOCKED.**

The IMF BOP dataset is annual/quarterly. IMF's official API documentation says SDMX 2.1 and 3.0 APIs are available; the Swagger explorer requires beta-portal sign-in. The direct public API endpoint tested below returned observations without API key, cookie, login or paid service.

## Exact structure
- Dataflow: `IMF.STA:BOP(21.0.0)`
- DSD: `IMF.STA:DSD_BOP(24.0.0)`, SDMX-ML 3.0, references=all, HTTP 200, 3,787,209 bytes, SHA-256 `4ddd46730f8d279f59348854065cd090936454678e4422c32b67b52a1a88a6bb`.
- Dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY.
- DSD-referenced codelists: `IMF.STA:CL_BOP_COUNTRY(1.0.0)`, `IMF.STA:CL_BOP_ACCOUNTING_ENTRY(3.3.0)`, `IMF.STA:CL_BOP_INDICATOR(10.0.0)`, `IMF:CL_UNIT(2.13.0)`, `IMF:CL_FREQ(1.2.0)`.
- Selected codes: BRA=Brazil, IND=India; A_NFA_T=Assets, Net acquisition of financial assets; L_NIL_T=Liabilities, Net incurrence of liabilities; P_F=Portfolio investment, Total financial assets/liabilities; USD=US dollar; Q=Quarterly.
- P_MV was tested and returned no observations for these exact country/entry combinations; it was not promoted.

## Pilot results
- Query window: 2015-Q1 to 2026-Q3.
- Brazil: 47 quarters for assets + 47 for liabilities, through 2026-Q3.
- India: 46 quarters for assets + 46 for liabilities, through 2026-Q2.
- Total 186 raw observations in 4 exact series.
- All four requests HTTP 200; all CSV parse PASS.
- Exact series vs broad-query comparison: 186/186 values match; raw-to-normalized attribute match 186/186; 0 duplicates; 0 missing from broad reference; 0 mismatches; quarterly periods contiguous.
- Assets and liabilities remain separate. No sign flip, rescaling, conversion, annualisation, aggregation, forward-fill or synthetic rows.

## Scale interpretation is still BLOCKED
The DSD maps `SCALE` to `IMF:CL_UNIT_MULT(1.0.2)`; code `6` is “Millions” (10^6). All extracted rows carry `UNIT=USD` and `SCALE=6`, while raw OBS_VALUE magnitudes already reach the billions. Raw values and SCALE are preserved exactly; no converted USD amount is asserted. The meaning/application must be reconciled against the IMF portal display and an official national source for Brazil and India before deriving USD, USD millions/billions or aggregating.

## Reproducibility
- Workflow: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44473935153
- Artifact ID 14504768485; ZIP 7,780,435 bytes; SHA-256 `ca8d63649955c3a698c1f674af8f075c195384903145f1ec672378876334ed49`; retained until 2027-02-17.
- Normalized panel SHA-256: `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.
- Exact CSV hashes:
  - BRA assets `3feca530a6495a3877370ad21bbacece69de87f3ebb725af4cbc455e1f84183c`
  - BRA liabilities `2d6b4a22740fe4df16ab4b84e71f69fd6d2833e12c32d94fa0db7bee2925a254`
  - IND assets `c86388af35f1b83b0b9d2a451d35c3c78541ea03af1d9a9c826a12bb34f04a82`
  - IND liabilities `25d41406425a78d575273a7b3fc63cfb3ecc05cda3789c25787b5a610b5c138d`

## Decision / next gates
- Raw access and pilot reconciliation: PASS.
- Daily trading use: NOT SUITABLE; BOP is quarterly/annual.
- Scale conversion: BLOCKED pending independent reconciliation.
- EM aggregate: NOT DONE; pilot is Brazil and India only.
- Next: validate scale against portal/national source, then extend across versioned October-2026 WEO EMDE membership with coverage/vintage controls.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No paid APIs, synthetic data or fabricated timestamps. UNKNOWN is not PASS.


## 8. Scale gate update — Brazil independently validated (2026-11-19)
- Official BCB SGS 22906 (assets) and 22924 (liabilities) monthly net-flow series were captured and compared with IMF Brazil P_F quarterly observations.
- 2015-Q1 through Q4 plus 2026-Q3, both entries: 10/10 PASS. `OBS_VALUE / 1,000,000` matches the three-month BCB sum within the 0.15 USD million rounding bound; maximum residual 0.12192411 million.
- Brazil scale/sign mapping is now PASS for these two series and five tested quarters. Raw IMF observations remain unchanged; the converted panel is not yet promoted.
- India and the rest of the EMDE universe remain unvalidated. India Table 196 uses fiscal quarters and is not a direct calendar-quarter match; no conversion is generalized.
- Full evidence: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`; raw BCB receipts and 10-row reconciliation in `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/`.


## 9. India scale/sign validation completed — two-country pilot status
- RBI Table197 official BPM6 quarterly USD-million table was cross-checked for 2024-Q2–2025-Q3: 12/12 asset/liability comparisons PASS within the 0.5 million rounding bound.
- RBI assets mapping requires sign reversal from its credit-minus-debit “Portfolio Investment by India” net to IMF A_NFA_T; liabilities map directly from “Portfolio Investment in India” to IMF L_NIL_T.
- Brazil 10/10 BCB checks plus India 12/12 RBI checks now support `OBS_VALUE / 1e6` for the two pilot countries.
- Do not generalize to the remaining 152 WEO EMDE members until country-level checks and vintage/BPM controls are complete. Full 154-member converted panel and aggregate remain NOT_AUTHORIZED.
- India report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`; evidence: `docs/evidence/imf_bop_emde_20261119/india_scale_reconciliation/`.
