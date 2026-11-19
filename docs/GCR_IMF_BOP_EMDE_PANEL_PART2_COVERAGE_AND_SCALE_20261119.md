# GCR — WEO EMDE IMF BOP Panel, Coverage and Scale Gate (Part 2)
Date: 2026-11-19

## Executive decision
- October 2026 WEO G200 membership: **154/154 exact code matches** to IMF BOP COUNTRY codelist.
- Quarterly BOP P_F asset/liability panel: **9,299 non-empty observations**, **9,299 unique keys**, zero duplicate keys.
- Coverage is incomplete: 114/154 countries have at least one entry; 111 have both; 40 have neither; DZA and ETH are assets-only; ZWE is liabilities-only.
- **Do not aggregate or transform yet.** The IMF DSD maps SCALE to CL_UNIT_MULT and code 6 is “Millions (10^6)”, but the IMF-specific SCALE concept has no explicit description in the captured scheme. The raw USD values have not been reconciled against an independent official benchmark. No multiplier has been applied.

## 1. Membership provenance
Official October 2026 WEO Entire Dataset workbook:
- URL: https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx
- Retrieved HTTP 200; 5,480,592 bytes; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- G200 Country Group Composition sheet: 154 members, 154 unique ISO3 codes.
- Same-vintage Appendix cross-check: 154 EMDE labels, 154 unique, 154/154 mapped to workbook ISO3 codes; no unmapped/ambiguous labels.
- IMF BOP COUNTRY codelist code-presence check: 154/154, no missing code.
- WEO membership artifact: run [44474629873](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474629873), artifact 14506160317, ZIP SHA-256 `acdf014f5f19ba5e0d23dca7a8d57a4b1813b002a3274495d557f0cd05c0fbb1`.
- Note label variance: WEO uses “Naoero” while BOP codelist uses “Nauru”; both carry code NRU. Identity is exact-code matched; label variance retained.

## 2. EMDE panel capture and repeatability
- Dataflow `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`.
- Indicator `P_F`; entries `A_NFA_T` (assets, net acquisition) and `L_NIL_T` (liabilities, net incurrence); UNIT=USD; FREQUENCY=Q.
- Window 2015-Q1 to 2026-Q3; no currency conversion, no rescaling, no forward fill, no synthetic rows.
- Run [44474620936](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474620936), artifact 14505452613, ZIP SHA-256 `b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17`.
- Independent repeated acquisition run [44474218174](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474218174), artifact 14505862034, ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- Across the two independent runs, membership CSV, coverage CSV, normalized panel CSV and both raw entry CSVs were byte-identical; their SHA-256 values are recorded in `coverage_quality_gate.json`.
- Asset observations 4,681; liability observations 4,618; total 9,299; unique keys 9,299; duplicate keys 0. Both raw requests HTTP 200 and CSV parse PASS. Only reported unit code was USD; all 9,299 rows carry SCALE=6.
- Independent exact-key check: 12 EMDE countries × 2 entries = 24 exact requests; 24/24 HTTP 200; 24/24 series PASS; 1,106/1,106 exact observations matched broad panel values and attributes. Run [44474458684](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474458684), artifact 14505009889.

## 3. Coverage gate
| Coverage measure | Result |
|---|---:|
| WEO members | 154 |
| Countries with any BOP P_F observation | 114 (74.03%) |
| Countries with both assets and liabilities | 111 (72.08%) |
| Countries with neither entry | 40 |
| Assets-only | DZA, ETH |
| Liabilities-only | ZWE |
| Country-entry combinations with observations | 225/308 (73.05%) |
| Empty country-entry combinations | 83 |
| Series with interior missing quarters | 13 |
| Series contiguous but partial | 208 |
| Series complete for all 47 quarters | 4 |

The 40 countries with no observations in either entry are listed in `coverage_quality_gate.json`. The 13 series with interior gaps and exact missing quarters are also listed there. Do not interpret absent rows as zero. Do not fill any gaps. Four fully covered 47-quarter series are BRA assets/liabilities and PAK assets/liabilities.

## 4. SCALE semantics gate
A dedicated no-credential metadata probe retrieved:
- DSD_BOP(24.0.0): HTTP 200, 23,825 bytes, SHA-256 `5953ac8b3a52fae9cd7c5821621446d046969bcef0e88540ef17520c2d39b098`.
- CS_MASTER_SYSTEM(1.0.2): HTTP 200, 6,402 bytes, SHA-256 `e753812c45b8159c77e191f091c63d5364375f57daca179da9799040de48e568`.
- CL_UNIT_MULT(1.0.2): HTTP 200, 54,278 bytes, SHA-256 `40a911ecceb0b96ff0ee2a166af3c2512f19fbbfca50e71b2e47936cad3bac78`.
- DSD attribute `SCALE` is optional and series-attached through the dimensions COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, FREQUENCY and UNIT.
- Concept scheme labels the concept “Scale” and enumerates it to `IMF:CL_UNIT_MULT`; no explicit English description is supplied.
- Codelist code 6 is “Millions”, described as 10^6.
- The general SDMX glossary defines UNIT_MULT=6 as observations in millions and says it is an exponent used to calculate the actual value in the unit of measure. Sources: https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_2_0_October_2018-2.htm and https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_1_0_February_2016.htm.
- However, the IMF-specific `SCALE` concept does not expose a definition clarifying whether this is a unit multiplier applied to OBS_VALUE or a preferred display scale. The raw observations are already labelled UNIT=USD and carry large numeric values. Applying 10^6 without an independent official benchmark could misstate the data by six orders of magnitude.
- Decision: metadata mapping PASS; numerical transformation BLOCKED. Keep raw OBS_VALUE untouched and retain SCALE=6.

## 5. Exact next actions
1. Obtain an IMF-specific definition or authoritative benchmark that establishes how `SCALE=6` relates to the returned OBS_VALUE for this dataflow; test at least two country series against independent official values before any rescaling.
2. Build the 154×2 country-entry completeness matrix as a hard gate; preserve 40 no-data countries, 3 one-sided cases and all 13 interior-gap series as missing/partial.
3. Investigate missingness only through official source routes and source vintages; do not substitute CPIS/PIP positions for BOP flows.
4. After scale and sign semantics are proven, define the EM aggregate eligibility threshold and vintage rules. No aggregate yet.
5. Then test annual BOP_AGG separately as a benchmark, not as a replacement for the quarterly country-reported panel.

## Decision
Membership: PASS. Panel acquisition: PASS. Byte-identical repeatability: PASS. Exact sample validation: PASS. Coverage completeness: PARTIAL/BLOCKED. SCALE numeric transformation: BLOCKED. Cross-country aggregation: BLOCKED. No production admission, no selector/ranking/pressure-fade/CORE-672/Engines A–E changes.


## 6. Extended attribute audit — SCALE / PRECISION / DECIMALS_DISPLAYED
A second exact metadata probe extended the DSD and concept scheme audit:
- Run [44475456706](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44475456706), artifact 14506176762, ZIP SHA-256 `18c4ed7ba1fafc6ae8024c8678780b7c8fc5af142d39d6e3d212de149f48e913`.
- The DSD exposes three separate optional attributes:
  - `SCALE`: series-level; relationship dimensions COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, FREQUENCY, UNIT; concept name “Scale”; enumerated to `CL_UNIT_MULT`.
  - `PRECISION`: observation-level; concept name “Precision”; also enumerated to `CL_UNIT_MULT`.
  - `DECIMALS_DISPLAYED`: series-level; concept name “Decimals Displayed”; enumerated to `CL_DECIMALS`.
- The IMF concept scheme provides no English Description for any of these three custom concepts.
- In the 9,299-row panel, `SCALE=6` on 9,299/9,299; `PRECISION=6` on 9,119 and missing on 180; `DECIMALS_DISPLAYED` is missing on all 9,299.
- SDMX Glossary distinguishes **Preferred scale** (6 means display in millions while data are in unit scale) from **Unit multiplier** (6 means observations are in millions for calculating actual unit values). These are not interchangeable concepts. See https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_2_0_October_2018-2.htm and https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_1_0_February_2016.htm.
- IMF's DSD uses a custom concept ID `SCALE`, not `UNIT_MULT`, but reuses the `CL_UNIT_MULT` code list. That code-list link alone does not prove whether the IMF attribute means unit multiplier or preferred display scale. The separate `PRECISION` and `DECIMALS_DISPLAYED` fields further confirm that a simple conversion rule cannot be inferred from the code alone.
- Decision remains: metadata mapping PASS; semantic equivalence BLOCKED; no numeric transformation. Preserve raw `OBS_VALUE`, `SCALE`, `PRECISION` and `DECIMALS_DISPLAYED` exactly.
