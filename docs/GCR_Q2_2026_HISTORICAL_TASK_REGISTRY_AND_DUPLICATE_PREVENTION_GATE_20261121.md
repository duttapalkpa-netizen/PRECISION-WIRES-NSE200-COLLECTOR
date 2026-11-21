# GCR Q2-2026 Historical Task Registry & Duplicate-Prevention Gate
Date: 2026-11-21 (Asia/Kolkata)
Scope: immutable 63-country national BOP portfolio dual-leg validation.
Status: CONTROL DOCUMENTATION CREATED; registry is a rolling evidence index, not a claim that all 63 countries have been exhaustively indexed.

## Mandatory preflight before every task
1. Fetch the current Master Continuity Ledger and GCR Master Priority Queue from the default branch; record their blob SHAs.
2. Search the repository for the country code/name, authority, exact URL/endpoint, dataset/table, quarter and earlier continuation/report numbers. Fetch every relevant country report, not only the queue excerpt.
3. Check fixed-cohort membership and reuse existing IMF raw archive rows. Never rebuild the cohort or re-query IMF unless a documented archive defect/new authorization requires it.
4. Build a route fingerprint:
   `country | authority | exact URL/endpoint | dataset/table | method/format | period | required fields`.
   A previously BLOCKED/NOT_CAPTURED fingerprint is closed. Reopen only when a concrete NEW official URL/API/export, supported byte-transfer capability, permission/credential, or source revision is evidenced and recorded before execution.
5. PASS is skipped. PARTIAL is actionable only against a named unmet gate. BLOCKED route is not retried. NOT_DONE is a status, not permission to repeat.
6. Before selecting a country, search its complete report history and queue handoffs. A country already audited is not selected again unless the New-Evidence Gate passes.
7. At completion, re-fetch the changed report, ledger and queue; verify exact commit SHA, final blob SHA, continuation number and statuses. If any re-fetch/verification fails, report NOT_VERIFIED, never SUCCESS/PASS.
8. Record rejected duplicate routes and why they were rejected. No synthetic values, invented timestamps, unsupported scale/sign/FX, stocks-as-flows, annual/H1-to-quarter allocation, net-to-leg back-solving, or relaxing the acceptance gate.

## Route registry — known audited country routes
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| NPL Nepal | NRB; https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx; official BPM6 workbook; XLSX browser + separate byte-download; Q2-2026; separate portfolio assets/liabilities | Continuations 55, 56, 58, 94, 128 and 130; reports: `docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_RETRIEVAL_ROUTE_AUDIT_CONTINUATION58_20261120.md`, `docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_BYTE_ROUTE_CLOSURE_CONTINUATION94_20261120.md`; queue handoff at Continuation 128 | PARTIAL / BLOCKED; discovery PASS; XLSX bytes/sheets/values NOT_CAPTURED; Q2 legs NOT_EXTRACTED | CLOSED. Do not repeat HTTP 400 unsupported XLSX MIME, same direct byte-download, stale NSDP `NEPAL_BOP_2024_Q1.xml`, or wrong-family Banking & Financial Statistics archive | A genuinely distinct official API/export or supported XLSX-capable byte route, recorded with exact new locator before retrieval |
| RWA Rwanda | BNR; https://www.bnr.rw/esstatistics; JS portal “Balance of Payment” item dated 30-Jun-2026; portal locator/API route; Q2-2026; separate A_NFA_T/L_NIL_T | `docs/GCR_RWANDA_RWA_Q2_2026_BNR_PORTFOLIO_SOURCE_GATE_CONTINUATION97_20261120.md`, including Continuation 130 recheck | PARTIAL / NOT PASS; exact document locator/bytes unresolved; Q2 legs NOT_CAPTURED; H1 net-only +14 USDm and annual FY legs are not Q2 | CLOSED for identical JS-shell/portal locator route and August summary / October H1 net-only substitutes | A new exact downloadable document/API/export URL or supported portal payload route; must expose Q2 separate transaction legs |
| TUR Türkiye | TCMB; exact September-2026 official ZIP route already recorded in Continuation 118; monthly BPM6/EVDS + ZIP route; Q2-2026; separate USD portfolio legs | Continuation 166 report `docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_OFFICIAL_SERIES_AND_ZIP_ROUTE_CLOSURE_CONTINUATION166_20261121.md` | PARTIAL / NOT PASS; Q2 PDF assets 5,749 vs IMF 5,749; liabilities 9,183 vs 9,270 (87m unexplained); ZIP bytes/hash unavailable | CLOSED for identical ZIP timeout; do not re-request same endpoint | A distinct official API/export/byte route or a documented new source revision |
| POL Poland | NBP; Q2 report PDF and reporting-form FX methodology v1.8; Q2-2026; separate PLN portfolio legs | Continuations 163–165; report `docs/GCR_POLAND_POL_Q2_2026_NBP_TRANSACTION_FX_RULE_AND_RECONCILIATION_BOUNDARY_CONTINUATION165_20261121.md` | PARTIAL / NOT PASS; assets 24,144m PLN; liabilities 70,910m PLN; transaction-date FX rule known; no matched USD dual-leg table or transaction currency/date weights; same-vintage unresolved | No aggregate FX conversion; no retry of known failed XLSX/PDF routes | Official matched USD Q2 dual-leg aggregate or transaction-level currency/date data and vintage bridge |
| SLV El Salvador | BCR; quarterly BOP publication/SDDS/NSDP routes; Q2-2026; separate portfolio legs | Continuation 100 and subsequent queue history; queue search confirms prior country report | PARTIAL / NOT PASS in current queue history | Do not reselect as a “new” country; inspect exact Continuation 100 report before any further action | New official Q2 dual-leg export/API or source revision not previously tested |
| ROU Romania | BNR/ECB; ECB BPS catalogue/API CSV route; Q2-2026; separate legs | Continuation 95 report `docs/GCR_ROMANIA_ROU_Q2_2026_BNR_ECB_PORTFOLIO_SOURCE_GATE_CONTINUATION95_20261120.md` | PARTIAL / NOT PASS; API retrieval unavailable; no Q2 values/bytes | Closed for identical inaccessible ECB CSV requests | New supported BNR/ECB download/export with confirmed quarterly flow semantics |
| CHL Chile | BCCh/BDE; monthly BDE series and REST API / Canasta export; Q2-2026; separate legs | Continuations 160–161 | PARTIAL / NOT PASS; values arithmetically align, but raw bytes/hash and vintage missing; API credential-gated; public Excel export not executed | Do not repeat credential-gated API without authorization or claim raw-byte PASS | Authorized API access or completed public Excel export with bytes/hash/vintage |
| COL Colombia | BanRep SUAMECA quarterly series / multiple-download; Q2-2026; separate legs | Continuation 162 and queue 128 | PARTIAL / BLOCKED; 502 and dashboard timeout; no raw values/bytes | Closed for same 502/dashboard route | Distinct supported official download/API route |
| BLR Belarus | NBRB official data page/bulletin; Q2-2026; separate legs | Continuations 159–160 | PARTIAL / NOT PASS; official methodology PASS; Q2 values/raw bytes unavailable | No repeat of same timed-out page/PDF | Distinct supported official Q2 data export |
| BLZ Belize | CBB Q2 review Table A.22 / official BOP XLSX; Q2-2026; separate legs | Continuation 157 | PARTIAL / NOT PASS; table H1 only; XLSX bytes blocked | No H1-to-Q2 inference or same XLSX retry | Distinct supported XLSX byte/export route or actual Q2 table |
| BOL Bolivia | BCB Q2 XLSX routes; Q2-2026; separate legs | Continuation 158 | PARTIAL / NOT PASS; official Q2 locators but XLSX bytes blocked | No same XLSX retry; no H1 substitute | New supported official export/byte route |
| PER Peru | BCRPData API/catalogue; Q2-2026; separate legs | Prior PER source-boundary report and queue | PARTIAL; public-sector portfolio asset series absent from located catalogue; API inaccessible | Do not infer public assets from aggregate | New official public-sector portfolio asset series or supported API |
| SLB Solomon Islands | CBSI Table 1.17; Q2-2026; separate legs | Queue and Continuation 128 | PARTIAL / NOT PASS; sign convention conflict only conceptually reconciled; exact vintage/scale unresolved | No sign flip or unverified conversion | Official sign methodology and same-vintage/scale bridge |


| HND Honduras | BCH; quarterly BOP dynamic page; XLSX locator https://www.bch.hn/estadisticos/EME/Series%20pblicas/Balanza%20de%20Pagos.xlsx?d=wb684924b7bd14bdca0d4bc95686dcbab; WOPI frame and SDMX XML route; Q2-2026; separate portfolio legs | Continuation 167: `docs/GCR_HONDURAS_HND_Q2_2026_BCH_OFFICIAL_BOP_SOURCE_AND_XLSX_ACCESS_GATE_CONTINUATION167_20261121.md` | PARTIAL / NOT PASS; official quarterly BOP + XLSX/SDMX locators PASS; XLSX/WOPI/XML bytes blocked; Q2 portfolio legs NOT_CAPTURED | CLOSED for same XLSX/WOPI and XML retrieval routes | Distinct supported official API/export/byte route capturing Q2 separate portfolio assets/liabilities and metadata |

## Selection and handoff control
- The immediately preceding queue text named NPL after TUR, but NPL has already been investigated in multiple continuations and its exact routes are closed. That handoff was stale and must not be followed.
- RWA was subsequently investigated in Continuations 97 and 130; its exact JS-only portal route was rechecked and remains unresolved. It is not a fresh country task.
- SLV has an earlier Continuation 100 history; it must not be treated as new without inspecting that report and the full queue.
- Therefore this registry creation does NOT authorize a new country selection. Next country must be chosen only after a fresh full-queue/report-inventory preflight; candidate sequence in stale snippets must not override historical evidence.

## Immutable constraints
Free official sources only; ₹0; no IMF re-query/cohort rebuild; no synthetic data or fabricated timestamps; preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2. UNKNOWN is never PASS. Aggregate remains NOT_AUTHORIZED until all required gates pass.


## Continuation 168 — KOS Kosovo route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| KOS Kosovo | BQK; https://bqk-kos.org/wp-content/uploads/2024/09/ROW%20Matrix%20%E2%80%93%20Transactions.xls; ROW Matrix (S.2) Transactions; XLS; Q2-2026; verify separate portfolio asset/liability transaction legs | Continuation 168: docs/GCR_KOSOVO_KOS_Q2_2026_BQK_ROW_TRANSACTION_MATRIX_SOURCE_GATE_CONTINUATION168_20261121.md | PARTIAL / NOT PASS; official locator and flow methodology PASS; XLS bytes HTTP 403; portfolio legs NOT_VERIFIED / NOT_CAPTURED | CLOSED for identical XLS URL and same browser retrieval path; separate monthly Financial account XLS route also failed HTTP 400 and container download | A genuinely new supported public XLS byte-transfer capability or distinct official export/API endpoint |
- KOS is in the immutable 63-country Q2-2026 both-leg cohort; no cohort rebuild/IMF re-query. Q2 IIP portfolio is stocks and NOT_ADMITTED as a BOP flow substitute. Aggregate NOT_AUTHORIZED.


## Continuation 169 — GMB The Gambia route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| GMB The Gambia | CBG; https://www.cbg.gm/downloads-file/a89fbf16-b8fc-11f1-8725-02e599c15748; Aug-2026 MPC report PDF; Q2-2026; separate portfolio transaction legs. Secondary: https://gambia.datawarehousepro.com/ → app.datawarehousepro.com/go/cbg; interactive macro data warehouse | Continuation 169: docs/GCR_GAMBIA_GMB_Q2_2026_CBG_BOP_QUARTERLY_REPORT_AND_DATAWAREHOUSE_SOURCE_GATE_CONTINUATION169_20261121.md | PARTIAL / NOT PASS; Q2 BOP report confirmed but only financial-account net totals; no portfolio legs; data warehouse app shell, no export payload | Closed for same PDF-as-dual-leg assumption and same app-shell inspection path | Distinct official detailed Q2 BOP table or documented public API/export payload exposing separate portfolio assets/liabilities |
- Do not infer zero from omission; do not use Q2 financial-account net USD95.4m, older 2017/18 portfolio rows, IIP stocks or IMF-only rows as national dual-leg validation. No IMF re-query/cohort rebuild.


## Continuation 170 — GIN Guinea route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| GIN Guinea | BCRG; https://www.bcrg-guinee.org/22eme-reunion-ordinaire-du-comite-de-politique-monetaire-de-la-republique-de-guinee/; 22nd MPC Q2-2026 document page (download URL unresolved). Secondary: https://www.bcrg-guinee.org/satistiques/balance-des-paiements/; BOP statistics page | Continuation 170: docs/GCR_GUINEA_GIN_Q2_2026_BCRG_OFFICIAL_BOP_SOURCE_BOUNDARY_AND_REPORTING_ROUTE_CONTINUATION170_20261121.md | PARTIAL / NOT PASS; official index/pages found; rendered Q2 data download/API not exposed; prior BCRG report format contains net portfolio only | CLOSED for same static page-only inspection; historical 2024–Q1 2025 net rows are not Q2-2026 evidence | A distinct official Q2-2026 downloadable report URL, public API/export payload or series endpoint with separate portfolio assets/liabilities |
- Do not use Q2 current-account surplus as portfolio evidence; do not back-solve from historic net-only portfolio values; aggregate NOT_AUTHORIZED.


## Continuation 171 — LAO Lao PDR route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LAO Lao PDR | Bank of the Lao P.D.R.; https://www.bol.gov.la/en/External_Sectors; External Sector Statistics catalogue, BOP row with Download Excel/Metadata columns; current BOP export links not exposed in indexed rendering; historical Table 13: https://www.bol.gov.la/en/fileupload/28-06-2024_1719576615.pdf | Continuation 171: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_OFFICIAL_BOP_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION171_20261121.md | PARTIAL / NOT PASS; official catalogue located; historic 2023 Table 13 split portfolio assets/liabilities; Q2-2026 raw export/legs not captured; catalogue page direct open HTTP 502 | Closed for identical External_Sectors page retrieval through same 502 path; historic 2023 table is schema-only | Actual BOL download Excel/metadata URL, distinct official BOL export/API or new supported retrieval path exposing Q2-2026 separate legs |
- Historical BOL Q4/2016 table net-only; do not presume 2026 layout. No annual/H1/stock/IMF-only substitution or net-to-leg inference. Aggregate NOT_AUTHORIZED.


## Continuation 172 — LAO official NSDP export locator fingerprint (2026-11-21)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LAO Lao PDR | Lao Statistics Bureau NSDP https://www.lsb.gov.la/lsb-en.htm → Balance of Payments → Browse Data: https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx ; Download in SDMX: https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml ; DSBB Metadata: https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 | Continuation 172: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_NSDP_SDMX_EXPORT_LOCATOR_DISCOVERY_CONTINUATION172_20261121.md | Exact official XLSX/XML/metadata locators PASS; XLSX/XML retrieval HTTP 400 timeout; no bytes/hash/observations; Q2 dual legs NOT_VERIFIED; PARTIAL / NOT PASS | Closed for same direct XLSX/XML fetch route after timeout | Genuinely new supported byte-transfer capability or distinct official mirror/export endpoint |
- No Q2-2026 or portfolio-leg claims until file inspection. Historical 2023 Table 13 remains schema-only; aggregate NOT_AUTHORIZED.


## Continuation 173 — LAO BOL/NSDP retrieval cross-check (2026-11-21)
| Country | Route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LAO Lao PDR | NSDP https://www.lsb.gov.la/lsb-en.htm → XLSX https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx ; SDMX XML https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml ; DSBB https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 ; IMF registry https://sdmxcentral.imf.org/data/registrations.html | Continuation 173 report | XLSX/XML HTTP 502 on live click; DSBB generic dynamic shell; no LAO match in inspected IMF public registrations page; no bytes/hash/observations; PARTIAL | Closed for same direct links and same registry-page lookup | Distinct official BOL mirror/export, public NSDP data service, or new supported byte-transfer capability |
- No conclusion that data are absent; no Q2 portfolio leg claims; aggregate NOT_AUTHORIZED.


## Continuation 174 — LKA Sri Lanka official Q2 BOP dual-leg source fingerprint (2026-11-21)
| Country | Official route / fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LKA Sri Lanka | Ministry of Finance Sri Lanka, Budget Economic and Fiscal Position Report–2027, issued 12-Nov-2026, official PDF https://treasury.gov.lk/api/file/04b45c52-3ded-4621-86c7-b8c67455c9d8 , Table 7 page 102, BOP 2026, USD mn, explicitly sourced to CBSL; Q2 provisional portfolio assets +26, liabilities -351 | Continuation 174 report | Separate legs present; both independently match archived IMF raw at whole USD-million rounding; same-vintage bridge and primary CBSL raw hash pending; strong reconciliation / provisional | Do not repeat Table 7 extraction; no Macro Lab secondary data; no IIP stock | Underlying CBSL Table 2.10 export/metadata or release revision date becomes accessible |
- Archived IMF raw row values: assets +25,676,196.5415909 USD; liabilities -350,932,889.850796 USD. These round to national +26/-351 USD mn. National table values provisional. Aggregate NOT_AUTHORIZED.


## Continuation 175 — LKA CBSL Table 2.10 source-version / access fingerprint (2026-11-21)
| Country | Route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LKA Sri Lanka | Official CBSL External Sector page https://www.cbsl.gov.lk/en/statistics/statistical-tables/external-sector ; exact Table 2.10 workbook locator https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sheets/table2.10_20260930_e.xlsx | C175 report | Official landing page identifies quarterly BPM6 BOP; page and XLSX direct retrieval HTTP 403; third-party metadata reports filename date 2026-09-30, Last-Modified 30-Sep-2026 15:06:48 GMT, SHA-256 2d6e3ebd5c4305028a3693d9e1c25a0c64c606616f0b24cf334695e1ad3d62f6; hash not independently verified, bytes not captured; vintage bridge NOT_ESTABLISHED | Do not repeat same direct CBSL page/XLSX fetch through same paths; do not treat third-party hash as verified | Genuinely different supported byte-transfer route or official alternate download endpoint |
- CBSL-authored revision-policy article says quarterly BOP releases revise monthly statistics and annual publication revises two consecutive years; no exact Q2-2026 revision vintage identified. LKA provisional; aggregate NOT_AUTHORIZED.


## Continuation 176 — LKA Table 2.10 secondary series and revision-risk fingerprint (2026-11-21)
| Country | Route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LKA Sri Lanka | Macro Lab series pages attributed to CBSL Table 2.10: assets https://macrolab.lk/data/series/LK.EXT.BOP_Q.ASSETS_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS.Q/ ; liabilities https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS.Q/ ; equity liabilities https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFO_S_EQUITY_AND_INVESTMENT_FUND_SHARES.Q/ ; debt liabilities https://macrolab.lk/data/series/LK.EXT.BOP_Q.LIABILITIES_FINANCIAL_ACCOUNT_PORTFOLIO_INVESTMENTS_DEBT_SECURITIES.Q/ | C176 report | Secondary Q2 values corroborate CBSL Table 2.10 release dated 30-Sep-2026; CSV/JSON raw export not captured; primary CBSL bytes/hash unavailable; 2021 old-mirror discrepancies reported; vintage bridge NOT_ESTABLISHED | Do not repeat HTML series-page extraction or promote secondary data to primary | New official CBSL/SDDS export or explicit official release-vintage metadata |
- LKA provisional; aggregate NOT_AUTHORIZED. Historical discrepancy values and caveats are detailed in C176.


## Continuation 177 — LKA official SDDS BOP.xlsx route fingerprint (2026-11-21)
| Country | Route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LKA Sri Lanka | CBSL SDDS NSDP https://www.cbsl.gov.lk/en/node/1809 → BOP “More Data” → https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sdds/BOP.xlsx | C177 report | Distinct official locator PASS; linked NSDP page last updated 11-Nov-2017 and shows Q2/17; XLSX retrieval HTTP 400 unsupported content-type; container download failed; bytes/hash/Q2-2026 content NOT_CAPTURED | Do not retry same click/download path; do not treat stale 2017 NSDP as current | New supported byte-transfer route or refreshed official SDDS/NSDP link |
- LKA remains provisional; aggregate NOT_AUTHORIZED.


## Continuation 178 — LSO Lesotho route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LSO Lesotho | Central Bank of Lesotho Statistical Research Portal https://statisticalwebportal.azurewebsites.net/ → Balance of Payments 6 category → `BPI_BPM6_XDC` Portfolio investment, Million Maloti; CBL Quarterly Economic Review September-2025 Table 19 | Continuation 178: `docs/GCR_LESOTHO_LSO_Q2_2026_CBL_BPM6_PORTAL_PORTFOLIO_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION178_20261121.md` | PARTIAL / NOT PASS; official BOP6 catalogue exposes one aggregate portfolio series only; Q2-2026 separate national portfolio assets/liabilities NOT_CAPTURED; report-family table is net-only and ends Q3-2025 | CLOSED for treating BPI_BPM6_XDC or “Portfolio Investments net” as dual-leg evidence; government-finance balance-sheet assets/liabilities are wrong source family | Distinct official Q2-2026 detailed BOP report/export/API exposing separate portfolio asset and liability transaction legs, with supported raw-byte capture |
- LSO is in the immutable 63-country cohort; no IMF re-query/cohort rebuild. Aggregate NOT_AUTHORIZED.


## Continuation 179 — MNG Mongolia route fingerprint update (2026-11-21)
| Country | Authority / exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNG Mongolia | National Statistical Office of Mongolia PxWeb; https://data.1212.mn/pxweb/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/ ; table `DT_NSO_0100_001V10_quarter`; Bank of Mongolia source; quarterly BOP; million USD; Q2-2026 period code `2026-2`; PxWeb API base documented as https://data.1212.mn/api/v1 | Continuation 179: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_BOP_QUARTERLY_SOURCE_AND_API_GATE_CONTINUATION179_20261121.md` | PARTIAL / NOT PASS; official table and metadata PASS; 69 indicator labels/codebook not captured; separate portfolio legs not verified; Q2 observations and raw API response/hash NOT_CAPTURED; metadata update-date discrepancy remains | Do not use net-only or IMF-only rows; no API response claimed; no guessed indicator codes or back-solving | Successful supported PxWeb metadata/codebook and JSON-stat2 query returning explicit portfolio asset/liability observations for `2026-2`, with original response bytes/hash and vintage metadata |
- MNG fixed-cohort member; no IMF re-query/cohort rebuild; aggregate NOT_AUTHORIZED.


## Continuation 180 — MNE Montenegro official route fingerprint (2026-11-21)
| Country | Authority / exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNE Montenegro | CBCG BPM6 BOP page https://www.cbcg.me/en/statistics/statistical-data/international-economic-relations/balance-of-payments → BPM6 2010–2026 archive ZIP https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip ; MONSTAT NSDP https://monstat.org/cg/page.php?id=1491&pageid=1491 → BOP Download in SDMX → https://dsbb.imf.org/xml/MNE/BOP6_Montenegro.xml ; Browse Data legacy CBCG endpoint https://www.cb-cg.org/eng/index.php?mn1=statistics&mn2=international_economic_relations&mn3=balance_of_payments | Continuation 180 report: `docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BOP6_NSDP_SDMX_SOURCE_BOUNDARY_CONTINUATION180_20261121.md` | PARTIAL / NOT PASS; official CBCG page and Q2 release calendar PASS; ZIP transfer HTTP 400 application/zip; SDMX XML transfer HTTP 400 text/xml; Browse Data timeout; no Q2 separate portfolio legs or raw hashes; exact fixed-cohort row membership pending recheck | Do not retry same ZIP/XML/legacy Browse endpoints via same transfer method; do not treat locator as parsed data | New supported transfer mechanism or distinct official export endpoint yielding raw Q2-2026 dual-leg bytes, plus exact MNE cohort row verification |
- IIP and external-debt sources are not BOP portfolio transaction legs; no net-to-leg back-solving. Aggregate NOT_AUTHORIZED.
