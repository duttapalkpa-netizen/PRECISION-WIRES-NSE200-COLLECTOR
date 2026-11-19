# GCR — Cross-country IMF BOP SCALE / sign validation (Part 3)
Date: 2026-11-19
Decision: **118/118 vintage-aligned comparisons PASS across four countries; latest Chile vintage exposes a separate revision mismatch. Global 154-country admission remains blocked.**

## Progress Log
### Completed
- WEO October 2026 G200 EMDE membership: 154/154 unique codes; exact IMF BOP COUNTRY code presence 154/154.
- IMF Data Portal BOP P_F quarterly panel: 9,299 observations, 9,299 unique keys, zero duplicates; 24 exact series checks across 12 countries matched 1,106/1,106 observations.
- Independent official national-source benchmarks:
  - India RBI Table 197: 12/12 PASS, 2024-Q2 to 2025-Q1.
  - Brazil BCB SGS 22906/22924: 94/94 PASS, 2015-Q1–Q4 and 2026-Q3.
  - Mexico Banxico CE174: 6/6 PASS, 2025-Q4 to 2026-Q2.
  - Chile Banco Central BDE older page vintage (updated 2026-09-07): 6/6 PASS, 2025-Q4 to 2026-Q2.
- Combined vintage-aligned sample: **118/118 PASS**. For these tested Data Portal rows, raw `OBS_VALUE / 1,000,000` reconciles to official national US$ million values. Preserve raw observations unchanged; conversion is derived-output only.
- Current Chile BDE page (updated 2026-11-18) was independently captured. Its 2025-Q4 values still match, but 2026-Q1/Q2 values are revised and no longer match the IMF panel; Q3 2026 national observations exist while the IMF panel has no CHL Q3 row. This is a source-vintage alignment gate, not a failed scale conversion.

### Rejected / not authorized
- Do not apply `×10^6) to the raw IMF Data Portal payload; national benchmarks support `OBS_VALUE / 10^6) for the tested series.
- Do not declare a universal all-154-country transform solely from four country benchmarks.
- Do not blend Chile's 2026-09-07 and 2026-11-18 vintages. The older snapshot is a web-rendered official page capture; raw bytes were not archived, so it is supporting evidence but not byte-level reproducible.
- Do not fill 40 countries with no data, 83 empty country-entry cells or 13 interior-gap series.
- No EMDE aggregate, no production selector/ranking/pressure-fade/CORE-672/Engine A–E change.

## 1. Benchmark results
| Country | National official source | Matched vintage/window | Comparisons | Result |
|---|---|---|---:|---|
| India | RBI Table 197, BPM6, quarterly USD million | 2024-Q2–2025-Q3 | 12 | 12 PASS |
| Brazil | BCB SGS 22906 assets / 22924 liabilities, monthly USD million | 2015-Q1–2026-Q3 | 94 | 94 PASS |
| Mexico | Banxico CE174, BPM6, quarterly USD million | 2025-Q4–2026-Q2 | 6 | 6 PASS |
| Chile | Banco Central BDE portfolio assets/liabilities, monthly USD million | 2025-Q4–2026-Q2, page vintage 2026-09-07 | 6 | 6 PASS |
| **Total** | **4 countries** | **Vintage-aligned comparisons** | **118** | **118 PASS** |

### Current Chile vintage exception
The current BDE series pages show “Actualizado: 18.Nov.2026” and are explicitly in millions of US dollars. Raw capture run [44476957975](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476957975), artifact 14507305215, ZIP SHA-256 `155fffc6fbc46df12f0905cd00b011651ced7df1368ceb0a65b736a090052691`.
- Assets raw HTML: 85,218 bytes, SHA-256 `0083083710e9419cb16fc8a07351f1913fa7466a429f8b045ef77a988c00b3d0`.
- Liabilities raw HTML: 85,063 bytes, SHA-256 `7857d8420f17886f32b05a0b50d2c1755df206223ee18e50c26645586268d116`.
- 2025-Q4: 2/2 PASS within ±1.5 USD million (three integer-million monthly observations summed).
- 2026-Q1/Q2: 4/4 REVIEW; current BDE monthly sums differ from IMF panel by +267.579, -376.101, -102.821 and +77.502 USD million.
- 2026-Q3: BDE quarterly monthly values can be summed, but both IMF CHL P_F rows are absent from the 154-country panel.
- The official BDE page snapshot last updated 2026-09-07 exposes the earlier monthly values; those sum to values matching the IMF panel 6/6. The later 2026-11-18 page has revised Q1/Q2 values. This supports a vintage/revision mismatch; the reason for the revisions has not yet been independently identified.
- Official series pages: [Chile portfolio assets](https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_BDP/MN_BDP42/BP6M_CF_ACT?idSerie=F068.G2.FLU.Z.0.S.A.Z.T.Z.Z.6.0.M) and [Chile portfolio liabilities](https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_BDP/MN_BDP42/BP6M_CF_PAS?idSerie=F068.G2.FLU.Z.0.S.P.Z.T.Z.Z.6.0.M).
- Older page-vintage evidence is from the official BDE page snapshot visible in the web research capture, updated 2026-09-07; original bytes were not saved, so treat it as lower-grade historical evidence, not a raw-hash archive.

## 2. Evidence files and runs
- India full six-quarter report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`; detailed CSV `docs/evidence/imf_bop_emde_20261119/india_scale_reconciliation/quarter_reconciliation.csv`.
- Brazil + India report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_INDIA_PART2_20261119.md`; Brazil CSV `docs/evidence/IMF_BOP_BRA_SCALE_RECONCILIATION_2015Q1_2026Q3.csv`.
- Brazil full 47-quarter workflow [44476176136](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476176136), artifact 14505944936, ZIP SHA-256 `1c9c1975717764aea11230f9fb659270a43c98b198e0154605589a1a8a19f317`; 94/94 PASS, max residual 0.12192411 USD million.
- India workflow [44476434148](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476434148), artifact 14506542277, ZIP SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`; RBI raw HTML 146,017 bytes, SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`.
- Mexico workflow [44476089607](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476089607), artifact 14506696311, ZIP SHA-256 `26ba04369dfba423609c313f68995dd7eeb7c5c44727d1df29a8062a3998c58c`; Banxico raw HTML 2,232,477 bytes, SHA-256 `c23bc36238c48a4e9b27582ebe519369761f9dafcb2ec9ea6b25b5dd62db21bd`.
- Chile current-vintage workflow [44476957975](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44476957975), artifact 14507305215, ZIP SHA-256 above.
- Consolidated machine-readable comparisons: `docs/evidence/IMF_BOP_SCALE_CROSS_COUNTRY_VALIDATION_20261119.csv` (126 rows: 94 Brazil, 12 India, 6 Mexico, 6 Chile 2026-09 vintage, and 8 Chile 2026-11 vintage).

## 3. Interpretation and admission gate
- Empirical transform for tested dataflow rows: `OBS_VALUE / 1,000,000` yields national US$ million values.
- Keep `SCALE=6`, `UNIT=USD`, `PRECISION`, raw observation and vintage metadata intact. Never overwrite raw values.
- The RBI asset comparator requires sign reversal because RBI presents “Portfolio Investment by India” credit-minus-debit; Brazil, Mexico and Chile direct series comparisons preserve the raw asset/liability sign.
- Chile demonstrates that matching the correct scale is not sufficient: vintage alignment changes values materially. Any country aggregate must carry a common vintage policy or an explicit revision matrix.
- No EMDE aggregate until: (1) vintage alignment is versioned, (2) all 154×2 coverage gaps remain explicit, (3) 13 interior-gap series are preserved, (4) sign conventions are proven per national source, and (5) BPM6/BPM7 basis is reconciled.

## 4. Exact next actions
1. Build a vintage-aware country-entry observation matrix that records source release/update dates and panel retrieval timestamp; flag national revisions against IMF Data Portal values rather than overwriting.
2. Resolve the Chile 2026-Q1/Q2 revision differences and add an archived old-vintage source if a legitimate official archive can be retrieved.
3. Validate one further current-vintage national source to reduce the chance that the 4-country sample is unrepresentative.
4. Only after vintage and coverage gates, create a clearly named observed-country subtotal; do not call it a full EMDE aggregate while 40 countries have no data and 83 country-entry cells are empty.

## Invariants
₹0 spend, official free sources only. No synthetic observations, no fabricated timestamps. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
