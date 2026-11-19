# Global Capital Rotation — IMF BOP EMDE Portfolio-Flow Panel
Date: 2026-11-19
Status: **PUBLIC DATA ACCESS PASS; 154-MEMBER RAW PANEL PASS; COVERAGE GAPS AND SCALE INTERPRETATION BLOCK DERIVED AGGREGATE**

## Progress Log
### Completed
- Anonymous official WEO October-2026 workbook retrieval and G200 EMDE membership extraction.
- All 154 unique WEO member codes mapped to the IMF BOP country codelist; 0 unmatched codes.
- Public IMF SDMX 3.0 BOP dataflow `IMF.STA:BOP(21.0.0)` queried for `P_F`, quarterly, two accounting entries and period 2015-Q1–2026-Q3.
- Raw CSVs, normalized panel, country-entry coverage matrix and provenance committed to GitHub.
- Independent exact-key sample validation: 12 EMDE countries × 2 entries = 24 requests; 24/24 HTTP 200 and PASS; 1,106/1,106 exact observations and source attributes match the broad multi-country panel.

### Rejected / excluded
- 40 of the 154 WEO EMDE members have no observations for either of the two selected portfolio-flow entries in the requested period; they remain in the membership and coverage matrix, not fabricated into the panel.
- 83 of 308 country-entry combinations have zero observations.
- Three one-sided cases: ZWE has liabilities but no assets; DZA and ETH have assets but no liabilities.
- No substitution of CPIS/PIP positions for BOP flows.
- No sign flip, scale conversion, currency conversion, forward-fill, synthetic rows, aggregation or trading signal.
- Quarterly BOP is not a daily 1–3 day swing trigger.

### Exact next actions
1. Reconcile the `SCALE=6` unit multiplier against the IMF portal display and official national-source values for at least Brazil and India.
2. Confirm the BPM6/BPM7 basis and revision/vintage metadata country by country.
3. Only after scale and basis are resolved, construct a coverage-weighted, currency-consistent EMDE aggregate; publish missingness and membership-version effects.
4. Treat BOP as a low-frequency macro context layer only.

## 1. Official sources and structure
- WEO October 2026 workbook: `https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx`
  - HTTP 200, 5,480,592 bytes, SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- IMF BOP country codelist: `https://api.imf.org/external/sdmx/3.0/structure/codelist/IMF.STA/CL_BOP_COUNTRY/1.0.0?references=all`
  - HTTP 200, 5,737,234 bytes, SHA-256 `190c0ab3196a85bba890e2fd0cf40eebda654de2eb8e7d1f16c9644572d59f39`.
- Dataflow: `IMF.STA:BOP(21.0.0)`.
- DSD: `IMF.STA:DSD_BOP(24.0.0)`.
- Indicator: `P_F` — Portfolio investment, Total financial assets/liabilities.
- Entries: `A_NFA_T` — Assets, Net acquisition of financial assets; `L_NIL_T` — Liabilities, Net incurrence of liabilities.
- Frequency: quarterly `Q`; requested period 2015-Q1 to 2026-Q3.
- Public API requests used anonymous GET; no key, login, cookies or paid API.

## 2. Membership and coverage
- WEO G200 “Emerging Market and Developing Economies”: 154 unique members.
- BOP codelist: 345 codes; all 154 WEO member codes map (154/154).
- Raw observations: 9,299 unique rows; duplicate keys 0.
- Country-entry coverage: 225/308 pairs contain observations; 83 pairs are empty.
- Countries with any observations: 114/154; 40 countries have neither selected entry.
- Assets: 4,681 observations, 113 country codes, 45 empty source rows.
- Liabilities: 4,618 observations, 112 country codes, 43 empty source rows.
- Both entries present: 111 countries. One-sided: ZWE (liabilities only); DZA and ETH (assets only).
- Unit dimension returned only `USD` in both broad queries. No currency conversion applied.

## 3. Integrity and sample checks
- Broad assets raw CSV: 484,139 bytes; SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`.
- Broad liabilities raw CSV: 451,290 bytes; SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`.
- Normalized panel: 9,299 unique rows; source attributes preserved; no forward-fill; no synthetic rows.
- Exact sample countries: ARG, BGD, BRA, CHN, IDN, IND, MEX, NGA, POL, SAU, TUR, ZAF.
- 24 exact-key requests (12 countries × 2 entries): 24/24 HTTP 200, 24/24 series PASS; 1,106 exact observations; 1,106/1,106 exact-to-broad matches; no missing or mismatched observations/attributes.
- This is an internal query-shape reconciliation against the same IMF source, not an independent external-source economic validation.

## 4. Critical scale interpretation gate
- The DSD's `SCALE` attribute is linked to `IMF:CL_UNIT_MULT(1.0.2)`; code `6` is labelled “Millions” (10^6).
- All 9,299 observations carry `UNIT=USD` and `SCALE=6`; 9,119 carry `PRECISION=6`, 180 have blank precision; `STATUS` is blank for all rows. These blanks are preserved, not interpreted as PASS.
- Under the standard SDMX unit-multiplier convention, the numeric observation is interpreted with the power-of-ten multiplier. However, raw values already reach large magnitudes; applying 10^6 mechanically would yield implausible values for some small EMDE economies.
- Therefore raw retrieval/integrity = PASS, but economic unit conversion = BLOCKED pending reconciliation with the IMF portal display and official national-source values. Do not derive USD millions/billions, growth, net flows or aggregates yet.

## 5. Reproducibility and durable archive
- Panel capture workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474218174
- Panel artifact ID `14505862034`; ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- Exact sample validation run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474458684
- Validation artifact ID `14505009889`; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- Durable evidence commit `a6eb5865` (panel, membership, coverage, raw BOP CSVs, 24 exact-check CSVs, provenance and receipts).
- Durable raw-source addition commit `79bfbeb3` (WEO October-2026 workbook and BOP country codelist XML).
- GitHub evidence folder: `docs/evidence/imf_bop_emde_20261119/`.

## 6. Decision
The prior blanket “IMF BOP observations inaccessible” blocker is superseded: public anonymous SDMX 3.0 observations are confirmed for the tested dataflow and keys, and a 154-member raw panel has been archived. However, this does **not** mean the Global Capital Rotation overlay is complete. Coverage is incomplete, scale semantics remain blocked, revisions/BPM basis still require review, and no EMDE aggregate or production factor is authorized.

No changes to Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 or Engines A–E. ₹0 spend; no synthetic observations; UNKNOWN is not PASS.


## 7. Scale validation update — Brazil only (2026-11-19)
- Official BCB SGS 22906 assets and SGS 22924 liabilities monthly series independently validate `IMF OBS_VALUE / 10^6` for Brazil in 2015-Q1–Q4 and 2026-Q3: 10/10 quarter checks PASS; maximum absolute residual 0.12192411 USD million versus a 0.15 million rounding bound.
- Brazil scale/sign mapping is now PASS for those tested series/quarters. This is not yet generalized to India or the remaining 152 EMDE members.
- India national-source period/concept crosswalk and all-country scale validation remain UNKNOWN. No EMDE-wide conversion or aggregate is authorized.
- Detailed comparison and raw source receipts: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`.


## 8. India scale/sign validation update — two pilot countries now pass
- RBI Table197 (BPM6 quarterly BoP, USD million) provides a like-for-like national-source cross-check for India.
- Six calendar quarters (2024-Q2–2025-Q3) × assets/liabilities = 12/12 PASS. RBI assets row is sign-reversed against IMF `A_NFA_T`; RBI liabilities row maps directly to IMF `L_NIL_T`. `OBS_VALUE/1e6` matches within the 0.5 USD million integer-publication rounding bound.
- Combined with Brazil's 10/10 BCB monthly checks, Brazil and India both validate the scale/sign normalization for their tested periods.
- This remains a two-country pilot validation. The remaining 152 WEO EMDE members are not yet cross-checked; no 154-member converted panel or aggregate is authorized.
- India evidence report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`; raw RBI page and 12 comparisons: `docs/evidence/imf_bop_emde_20261119/india_scale_reconciliation/`.
