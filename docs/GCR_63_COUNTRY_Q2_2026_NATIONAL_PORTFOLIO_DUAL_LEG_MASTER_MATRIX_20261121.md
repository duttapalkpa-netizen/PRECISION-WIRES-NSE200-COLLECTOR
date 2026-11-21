# GCR 63-Country Q2-2026 National Portfolio Dual-Leg Master Matrix
Date: 2026-11-21 (Asia/Kolkata)
Status: BASELINE MATRIX v1 — country-by-country inventory; NOT an aggregate authorization.

## Immutable cohort and provenance
- Source roster: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`
- Source Git blob SHA-256-like Git blob identifier: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`
- Cohort derivation report: `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`, blob `1f767e22095865c8e5f87c2cfca55d9104b91e3e`.
- Exactly 63 members; every row has Q2-2026 A_NFA_T and L_NIL_T present in the archived IMF panel. This is panel availability only, not national-source PASS.
- No cohort rebuild, no IMF re-query, no change to raw cohort CSV.

## Status semantics
- `NOT_STARTED`: no country-specific national-source evidence recorded in this baseline.
- `SOURCE_FOUND`: official source/methodology/locator identified; Q2 dual-leg data not yet captured.
- `DATA_CAPTURED`: national Q2 values/observations have been captured or reported; at least one acceptance gate remains open.
- `ASSET_PASS` / `LIABILITY_PASS`: only that named leg has passed its numeric/source acceptance; the other leg or another gate remains open.
- `VINTAGE_PASS`: reserved for an explicit same-vintage/revision match. No row is assigned this without evidence.
- `FULL_PASS`: reserved for source, both legs, unit/sign/scope and vintage gates all passing. No row is assigned FULL_PASS in this baseline.
- `BLOCKED`: current identified official route is inaccessible/exhausted or the source does not publish the required separate Q2 legs. A new distinct source route may reopen it.
- Gate columns are deliberately conservative. `CAPTURED_REVIEW_OR_MATCH` means values/comparison evidence exists but does NOT imply PASS. `NOT_VERIFIED` is not FAIL and not PASS.
- Aggregate admission remains NOT_AUTHORIZED for every row.

## Snapshot counts
- SOURCE_FOUND: 10
- BLOCKED: 31
- DATA_CAPTURED: 17
- NOT_STARTED: 4
- LIABILITY_PASS: 1
- Total cohort rows: 63.
- Rows with national evidence beyond NOT_STARTED: 59.
- Rows not yet FULL_PASS: 63.
- FULL_PASS: 0; VINTAGE_PASS: 0.
- These are baseline inventory classifications, not claims of a weighted completion percentage. Several historical country reports need a full re-open before a stage can be promoted.

## Country-by-country matrix
| Code | Country | Overall status | Source | Data | Asset | Liability | Vintage | Note |
|---|---|---|---|---|---|---|---|---|
| AGO | Angola | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BNA source-family gate; Q2 national portfolio A/L not captured; no net-to-leg inference. |
| ALB | Albania | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BPM6/sign methodology found; Q2 export/values inaccessible; legacy Main-data route closed. |
| ARG | Argentina | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | INDEC Q2 dual-leg observations examined; provisional release; same-vintage bridge unresolved. |
| ARM | Armenia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBA current export route timed out; legacy XLS route closed; no national Q2 legs. |
| AZE | Azerbaijan | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBAR source scope found; combined portfolio+other rows excluded; Q2 portfolio-only legs absent. |
| BDI | Burundi | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BRB source boundary recorded; Q2 national A/L not captured. |
| BGD | Bangladesh | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Net-only/annual survey routes exhausted; separate Q2 portfolio legs unavailable. |
| BIH | Bosnia and Herzegovina | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBBH interactive portal; export not executed in current environment. |
| BLR | Belarus | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | NBRB methodology/source found; H1 cannot substitute for Q2; raw Q2 legs unavailable. |
| BLZ | Belize | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBB Q2 review shows H1 only; XLSX byte route blocked. |
| BOL | Bolivia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCB Q2 XLSX routes blocked; no H1 substitution. |
| BRA | Brazil | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCB/IMF PA/Dataflow mismatch; public retries exhausted; owner-side evidence dependency. |
| CHL | Chile | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | BCCh values arithmetic aligned; raw bytes/hash and same-vintage bridge remain missing. |
| CHN | China | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | SAFE Q2 values captured; asset sign crosswalk unresolved; workbook byte route blocked. |
| COL | Colombia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BanRep SUAMECA/dashboard routes failed; Q2 legs not captured. |
| CPV | Cabo Verde | NOT_STARTED | NOT_STARTED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | No country-specific Q2 national dual-leg acceptance evidence established in this baseline. |
| CRI | Costa Rica | NOT_STARTED | NOT_STARTED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | No country-specific Q2 national dual-leg acceptance evidence established in this baseline. |
| DOM | Dominican Republic | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | National-source route history exists; source/data gate remains incomplete; recheck report before any route retry. |
| ECU | Ecuador | NOT_STARTED | NOT_STARTED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | No country-specific Q2 national dual-leg acceptance evidence established in this baseline. |
| GEO | Georgia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | NBG NSDP/UI shell; no exposed Q2 BOP export target. |
| GIN | Guinea | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCRG page/attachment target not exposed; static-page route closed. |
| GMB | The Gambia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBG Q2 report contains financial-account net only; no separate portfolio legs. |
| HND | Honduras | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCH XLSX/WOPI/SDMX locators found; raw bytes and Q2 legs not captured. |
| HUN | Hungary | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Country-specific source research recorded; full dual-leg/vintage acceptance not evidenced in current inventory. |
| IDN | Indonesia | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | BI Q2 legs captured; latest revision differs from archived IMF snapshot; same-vintage unresolved. |
| IND | India | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | RBI Q2 table evidence exists; full matched-vintage two-leg acceptance not established. |
| KAZ | Kazakhstan | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Country source locator/research recorded; Q2 dual-leg evidence incomplete. |
| KOS | Kosovo | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BQK official XLS locator; HTTP 403; no data bytes. |
| LAO | Lao PDR | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BOL/NSDP XLSX/XML locators; retrieval failed; no Q2 legs. |
| LKA | Sri Lanka | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | Treasury Q2 provisional A/L match archived IMF rounded values; primary CBSL bytes/vintage unresolved. |
| LSO | Lesotho | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Country source locator/research recorded; full Q2 dual-leg evidence incomplete. |
| MAR | Morocco | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Country source locator/research recorded; full Q2 dual-leg evidence incomplete. |
| MDA | Moldova | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BNM report generator requires interactive execution; not executed. |
| MEX | Mexico | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | Banxico dual-leg work exists; same-vintage/complete acceptance must be verified against detailed report. |
| MKD | North Macedonia | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | NBRNM metadata and SSO net-only found; separate portfolio A/L and raw export missing. |
| MNE | Montenegro | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBCG bulletin tables annotation target unresolved; no Q2 A/L captured. |
| MNG | Mongolia | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | NSO PxWeb metadata route found; API payload inaccessible; Q2 A/L not captured. |
| MYS | Malaysia | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | BNM national portfolio source crosswalk exists; exact same-vintage acceptance not established in reviewed summary. |
| NGA | Nigeria | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | RECHECK_REQUIRED | Earlier queue records 6/6 national comparisons; preserve as captured/comparison evidence, but do not elevate to FULL_PASS without vintage and raw-source gate recheck. |
| NPL | Nepal | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | NRB XLSX retrieval routes exhausted; no Q2 national A/L captured. |
| PAK | Pakistan | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | SBP public table did not expose separate Q2 portfolio legs; net/stock substitutes excluded. |
| PAN | Panama | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Official-source research locator recorded; national Q2 A/L and vintage evidence incomplete. |
| PER | Peru | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCRP catalogue lacks demonstrated public-sector portfolio asset series; API inaccessible. |
| PHL | Philippines | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Earlier country research exists; full raw-source dual-leg/vintage acceptance not evidenced in current summary. |
| POL | Poland | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | NBP national PLN values captured; no matched USD dual-leg/vintage bridge. |
| PRY | Paraguay | NOT_STARTED | NOT_STARTED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | No country-specific Q2 national dual-leg acceptance evidence established in this baseline. |
| ROU | Romania | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BNR interactive database locator found; JS-capable execution unavailable; no export. |
| RWA | Rwanda | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BNR JS portal; no exact downloadable Q2 dual-leg payload. |
| SAU | Saudi Arabia | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | Country source locator/research recorded; full Q2 dual-leg evidence incomplete. |
| SLB | Solomon Islands | SOURCE_FOUND | SOURCE_FOUND | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBSI Table 1.17 reviewed; sign/scale/vintage bridge unresolved. |
| SLV | El Salvador | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCR quarterly routes reviewed; Q2 separate portfolio legs not accepted. |
| SRB | Serbia | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | NBS bulletin series/values researched; FX/scope/vintage equivalence unresolved. |
| THA | Thailand | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | BOT Q2 USD dual legs numerically compare 2/2; observation-level same-vintage not established. |
| TJK | Tajikistan | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | NBT archive label/filename period conflict; PDF bytes inaccessible; no Q2 A/L. |
| TLS | Timor-Leste | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BCTL latest chart/archive/report do not expose Q2 separate A/L. |
| TUR | Türkiye | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | TCMB Q2 values compared; liability residual remains; ZIP bytes/vintage gate unresolved. |
| TZA | Tanzania | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | BoT Q2 table exposes portfolio net only; separate A/L not published in inspected source. |
| UKR | Ukraine | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | NBU transaction-change A/L compare numerically; formal BOP P_F equivalence and vintage bridge unresolved. |
| URY | Uruguay | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | BCU Q2 numeric dual-leg comparison matches; raw PDF bytes and same-vintage bridge missing. |
| UZB | Uzbekistan | DATA_CAPTURED | SOURCE_FOUND | DATA_CAPTURED | CAPTURED_REVIEW_OR_MATCH | CAPTURED_REVIEW_OR_MATCH | NOT_ESTABLISHED | CBU Q2 values compared; time-basis/unit and same-vintage bridge unresolved. |
| VNM | Vietnam | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | SBV official quarterly dual-leg Q2 route not found; no raw Q2 legs. |
| WSM | Samoa | BLOCKED | BLOCKED | NOT_CAPTURED | NOT_VERIFIED | NOT_VERIFIED | NOT_ESTABLISHED | CBS Q2-2026 national A/L not captured; reports are net-only/stale. |
| ZAF | South Africa | LIABILITY_PASS | SOURCE_FOUND | DATA_CAPTURED | REVIEW | PASS | NOT_ESTABLISHED | SARB liability leg passes rounding bound; asset leg REVIEW outside bound; overall not full pass. |

## Controls / next action
1. This matrix is a baseline built from the immutable 63-row cohort and currently indexed country reports/ledger/queue. It is not an exhaustive re-audit of every historical report.
2. Before any promotion to ASSET_PASS, LIABILITY_PASS, VINTAGE_PASS or FULL_PASS, reopen the exact country report and verify primary-source evidence, raw bytes/hash where required, period, scope, units, sign, and same-vintage alignment.
3. Do not convert `DATA_CAPTURED` to `FULL_PASS` merely because rounded values match. Do not infer legs from net, stocks, H1/annual values, or adjacent quarters.
4. First follow-up should be an evidence-reconciliation pass on countries already marked DATA_CAPTURED / LIABILITY_PASS, prioritizing any near-complete country without repeating closed routes.
5. ₹0, official/free sources only. UNKNOWN is never PASS. Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged.
