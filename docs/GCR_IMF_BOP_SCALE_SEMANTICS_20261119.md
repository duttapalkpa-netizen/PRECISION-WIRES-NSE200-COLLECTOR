# IMF BOP SCALE and numeric representation resolution — 2026-11-19

## 1. Authoritative metadata meaning — PASS
- DSD: `IMF.STA:DSD_BOP(24.0.0)`; optional series attribute `SCALE` references `IMF:CS_MASTER_SYSTEM(1.0.2).SCALE`.
- The concept's CoreRepresentation enumerates `IMF:CL_UNIT_MULT(1.0.2)`.
- Official codelist code `6` is **Millions**; English description: “In scientific notation, expressed as ten raised to the power of six (10^6)”.
- This is a unit multiplier, not decimal-place precision. The Arabic display label for SCALE is inconsistent with the enumerated codelist; the codelist definition is authoritative.
- Raw CL_UNIT_MULT XML SHA-256: `40a911ecceb0b96ff0ee2a166af3c2512f19fbbfca50e71b2e47936cad3bac78`; 31 codes; latest version 1.0.2.
- Concept scheme SHA-256: `e753812c45b8159c77e191f091c63d5364375f57daca179da9799040de48e568`; DSD SHA-256: `5953ac8b3a52fae9cd7c5821621446d046969bcef0e88540ef17520c2d39b098`.

## 2. Numeric API representation — empirically cross-checked
The official IMF API's returned `OBS_VALUE` values are in base-USD numerical magnitude for the tested country-periods. Dividing by 10^6 expresses them in USD million and reconciles against official national-source tables. The stored raw IMF values and `SCALE=6` attributes are not modified.

### Brazil
- BCB monthly series 22906 (assets) and 22924 (liabilities), million USD.
- 47 quarters × 2 entries = 94/94 PASS; maximum absolute residual 0.12192411 USD million.
- Report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`; run 44475693836, artifact 14506740234.

### India
- RBI Table 42, Standard Presentation of BoP in India as per BPM6 (US$ Million).
- Four calendar quarters tested; 12 comparisons (assets, liabilities, combined net): 10 PASS, 2 REVIEW.
- 2025-Q1, 2025-Q2 and 2026-Q2: all three comparisons PASS within ±0.5 USD million.
- 2026-Q1 asset comparison PASS; liability and combined net REVIEW. IMF liability = -13,633.508347 USD million versus RBI 3.2.A net = -12,121 USD million; residual = -1,512.508347 USD million. No silent reconciliation.
- Report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`; run 44477031402, artifact 14505649659. RBI raw HTML hashes and the exact 12-row comparison CSV are archived under `docs/evidence/imf_bop_20261119/india_scale_reconciliation/`.

## 3. Operational rule and limitations
- The empirical diagnostic is `USD_million = OBS_VALUE / 10^6` for the cross-checked country-periods.
- The code meaning SCALE=6 is PASS. Numeric API-to-national-source mapping is Brazil PASS, India PARTIAL.
- Do not transform the full 154-member EMDE panel or derive a global aggregate solely from these two countries' crosswalks. Keep the original raw `OBS_VALUE`, `UNIT`, `SCALE`, `PRECISION` and derivation attributes unchanged.
- India 2026-Q1 liability mismatch remains REVIEW; current-source vintage, reporting revision or definition differences are not inferred.
- Sign, FX policy, asynchronous reporting and point-in-time vintage handling remain open. No netting/aggregate or backtest admission yet.

## 4. Reproducible metadata capture
- Original metadata run 44475051442 / artifact 14505852262 / ZIP SHA-256 `391981ce19d89d8ccc6377580e33345a9d75adffdc3f4197c4e4c743a66e3cf3`.
- Corrected codelist capture run 44477031402 / artifact 14506293939 / ZIP SHA-256 `ffac629793da363b934321e00f43aaec7eabcd609bc9a029cb46356712a01858`.
- Durable evidence: `docs/evidence/imf_bop_20261119/scale_concept_route_summary.json`, `CL_UNIT_MULT.xml`, and `scale_unit_multiplier_authoritative/`.

No production changes; no paid sources; no synthetic data; ₹0 spend. UNKNOWN is not PASS.
