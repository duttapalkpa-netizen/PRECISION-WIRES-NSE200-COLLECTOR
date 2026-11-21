# Mongolia (MNG) Q2-2026 — NSO PxWeb quarterly BOP source and API gate (Continuation 179)
Date: 2026-11-21 (Asia/Kolkata)
Decision: FIXED-COHORT MEMBERSHIP PASS; OFFICIAL NATIONAL STATISTICS OFFICE QUARTERLY BOP PXWEB TABLE IDENTIFIED; METADATA CONFIRMS BANK OF MONGOLIA SOURCE, QUARTERLY FLOW FREQUENCY, MILLION USD UNIT AND Q2-2026 PERIOD AVAILABILITY; TABLE HAS 69 INDICATOR VALUES AND QUARTER DIMENSION; HOWEVER THE WEB-RENDERED TABLE DOES NOT EXPOSE THE INDICATOR CODEBOOK OR SELECTED OBSERVATION CELLS, AND THE PXWEB JSON API REQUEST/RAW RESPONSE WAS NOT EXECUTED; SEPARATE PORTFOLIO ASSET/LIABILITY INDICATORS AND Q2 VALUES NOT_VERIFIED; MNG PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger (blob SHA `04d88a488c264a6a97dfc8ef397414dd7060ce20`), GCR Master Priority Queue (`5f09558fc290d450a96d1f5cc03579f7c6f947f0`), Historical Task Registry (`aa4d58d6ad86cc9b7455bd1b9c5743f43db06fc3`) and C178 report (`2c922f3bf97ac1514440df22ea92d24d8855fc7f`).
- Reused immutable cohort `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. MNG is a fixed member with both IMF panel legs present, national validation pending, aggregate not authorized. No cohort rebuild and no IMF re-query.
- Repository searches for `MNG Mongolia Q2 2026 portfolio assets liabilities`, `Mongolia Q2 2026 BOP portfolio investment assets liabilities` and `MNG Q2-2026 national dual-leg` returned no dedicated prior MNG report.
- MAR is already covered by Continuations 87/92/93; MDA is covered by C86 and its BNM interactive report-generator export gate remains unresolved; MYS is already covered by several existing reports. These were excluded from duplicate work.
- LSO C178's BOP6 net-only source family remains closed; no repeat.

## 2. Official NSO quarterly BOP PxWeb table
- Official table: https://data.1212.mn/pxweb/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/
- Title: “BALANCE OF PAYMENTS, by quarter by Indicator and Quarter”.
- Table is hosted by Mongolia's National Statistical Office (NSO); metadata identifies Bank of Mongolia as the source.
- Metadata describes BOP as transactions between residents and non-residents over a specified period, including portfolio investment and other investment flows.
- Table dimensions: Indicator (69 available values) and Quarter (70/71 values, depending on page capture). Q2-2026 appears in the available period examples as `2026-2`.
- Measurement: million USD. Frequency: quarterly.
- Search-indexed metadata for this same table reports information updated 11-Sep-2026 and periods through 2026-3. The live page opened in this audit reports “Information updated date” 10-Aug-2026 and next update 09-Sep-2026, with 2026-2 and 2026-1 among the period examples. This is a metadata freshness inconsistency; preserve both representations and do not choose a preferred vintage without source confirmation.
- The live HTML page states that table data are selected in three stages (Choose table, Choose variable, Show result), and that a query must select at least one Indicator and Quarter. It currently shows zero selected cells; the actual 69 indicator labels and observations are not rendered in the text extraction.
- The page's metadata link is the NSO national portal; the table is explicitly an official BOP flow table and not an IIP stock table.

## 3. PxWeb API discovery and retrieval boundary
- Public PxWeb API client documentation for Mongolia's NSO identifies the base endpoint as `https://data.1212.mn/api/v1` and documents the API model: retrieve table metadata, construct a JSON query selecting dimension codes, and request JSON-stat2 data. Supporting public technical references:
  - https://rdrr.io/cran/mongolstats/src/R/pxweb.R
  - https://github.com/temuulene/mongolstats
  - https://github.com/makhgal-ganbold/NSO1212v1
- These are technical client references, not national observations or primary data. They establish a documented route pattern but do not prove the Q2 portfolio legs.
- Attempted the metadata endpoint using the documented PXWeb API base and the official table path. The web retrieval layer returned “URL not accessible”; container-side direct HTTP attempt failed DNS resolution for `data.1212.mn`. No successful HTTP response, request payload, response bytes, or raw hash was obtained.
- No unsupported values, indicator codes, API payload, or URL response were fabricated. No portfolio asset/liability label was assumed based on BPM6 conventions.
- A separate public PxWeb table is promising because it may allow a native query of the 69 indicator dimension values and Q2-2026 observations; it is not yet a completed extraction.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| MNG fixed 63-country cohort membership | PASS |
| No dedicated prior MNG country dual-leg report in scoped repository search | PASS |
| Official NSO quarterly BOP PxWeb table identified | PASS |
| Source = Bank of Mongolia | PASS (table metadata) |
| BOP transaction-flow definition / portfolio coverage | PASS (table metadata) |
| Q2-2026 period available in table period dimension | PASS (period example) |
| Unit = million USD / frequency = quarterly | PASS |
| Exact 69 indicator labels/codebook | NOT_CAPTURED |
| Separate portfolio asset and liability indicator rows | NOT_VERIFIED |
| Q2-2026 national portfolio asset observation | NOT_CAPTURED |
| Q2-2026 national portfolio liability observation | NOT_CAPTURED |
| PxWeb API query/response bytes and SHA-256 | NOT_CAPTURED |
| National sign, scope and vintage bridge | NOT_ESTABLISHED |
| IMF exact-key numeric comparison | NOT_DONE |
| Full MNG national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Rejected substitutes and next exact action
- Rejected IMF Article IV annual/forecast portfolio-net values and Mongolia Ministry of Economy H1-2026 aggregate balance-of-payments surplus as Q2 national dual-leg evidence.
- Rejected IIP positions, external debt, and commercial-bank balance sheets as BOP portfolio transaction legs.
- Do not infer asset/liability rows from net portfolio balance.
- Next: retrieve the official PxWeb metadata and indicator codebook via a functioning supported API or interactive export, select only the two verified portfolio asset/liability indicators and Quarter `2026-2`, preserve the exact JSON request/response and SHA-256, then compare each leg separately with the already archived IMF raw rows. If API access remains unavailable, request the official NSO/Bank of Mongolia Q2 export as an attachment and advance to the next cohort member rather than retrying the same inaccessible route.
- No IMF re-query, no cohort rebuild.

## 6. Protected invariants
₹0; free official sources only. No synthetic values/timestamps, no net-to-leg back-solving, no annual/H1 allocation, no stock-as-flow, no unsupported sign/scale/FX conversion, no duplicate IMF requests or cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
