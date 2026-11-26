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


## Continuation 181 — POL Poland official route fingerprint update (2026-11-21)
| Country | Authority / route | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| POL Poland | NBP current BOP English PDF https://static.nbp.pl/dane/bilans-platniczy/bopa_en.pdf (PLN million); NBP public reporting list https://sprawozdawczosc.nbp.pl/pages/information/publication/common-publication-list.jsf; NBP Web API https://api.nbp.pl/en.html (exchange rates only) | C181 report docs/GCR_POLAND_POL_Q2_2026_NBP_USD_DUAL_LEG_PUBLICATION_SEARCH_CLOSURE_CONTINUATION181_20261121.md | PARTIAL / NOT PASS; prior Q2 legs exist in PLN; no current matched USD Q2 dual-leg table or transaction-date/currency weights; no USD conversion or same-vintage bridge | Do not retry same failed NBP XLSX/PDF transfer or convert PLN totals using daily/quarterly FX means without transaction weights | New official USD Q2 dual-leg aggregate or dated transaction-level currency/amount source with vintage metadata |


## Continuation 182 — MNE Montenegro official table-export route fingerprint update (2026-11-21)
| Country | Authority / route | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNE Montenegro | CBCG Bulletin archive https://cbcg.me/en/publications/regular-publications/cbcg-bulletin → Bulletin 9/2026 PDF https://cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf → BOP Tables 5.1–5.4 “download tables” affordance | C182 report docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_EXPORT_LOCATOR_CONTINUATION182_20261121.md | PARTIAL / NOT PASS; official PDF and methodology verified; export affordance identified, but linked table payload URL/bytes/hash and separate Q2-2026 portfolio legs not captured | Do not repeat C180 ZIP/XML/legacy Browse failures; PDF table link locator is new and may be resolved via supported link-annotation/download route | Raw official Tables 5.1–5.4 workbook/CSV with Q2-2026 asset/liability rows, metadata and SHA-256 |


## Continuation 183 — MNE CBCG Bulletin PDF annotation access boundary (2026-11-21)
| Country | Route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNE Montenegro | CBCG Bulletin 9/2026 PDF, BOP section printed p.55/PDF p.54, Tables 5.1–5.4 “download tables” annotation | C183 report: `docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_PDF_ANNOTATION_ACCESS_AUDIT_CONTINUATION183_20261121.md` | PDF and methodology reverified; available extraction exposes annotation text but not target URL; PDF byte download failed; table bytes/hash and Q2 separate portfolio legs NOT_CAPTURED; PARTIAL / NOT PASS | Closed for repeating same PDF text extraction/search and identical direct download attempt | A genuinely different supported PDF annotation extractor or distinct official workbook/CSV/API export locator |
- C183 does not establish that tables are absent; it records an access/tool boundary only. No guessed URL, timestamp, MIME, or hash. Fixed cohort unchanged; MNE remains PARTIAL; aggregate NOT_AUTHORIZED.


## Continuation 184 — MKD North Macedonia NBRNM quarterly BOP route fingerprint (2026-11-21)
| Country | Authority / route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MKD North Macedonia | NBRNM PxWeb, table “Balance of Payments, Republic of North Macedonia, financial account, by quarters”, matrix ES-001; SSO Bulletin 10/2026 BOP table | C184 report: `docs/GCR_NORTH_MACEDONIA_MKD_Q2_2026_NBRNM_PXWEB_AND_SSO_PORTFOLIO_SOURCE_BOUNDARY_CONTINUATION184_20261121.md` | Cohort row PASS; NBRNM official table metadata PASS (210 items, 114 quarters, million EUR/USD); SSO Q2-2026 portfolio net +227.7 USDm PASS as net-only; separate portfolio legs and raw query/export bytes/hash NOT_CAPTURED; PARTIAL / NOT PASS | Do not use SSO net as dual legs; do not relabel financial-account-wide net acquisition +144.9 or net incurrence +431.0 as portfolio-specific legs; do not repeat inaccessible methodology/revision PDF retrieval via same path | Successful official NBRNM PxWeb metadata/codebook + selected Q2-2026 portfolio asset/liability observation query, with original bytes/hash and revision metadata |
- MKD exact fixed-cohort row: both IMF legs present; national validation pending; aggregate NOT_AUTHORIZED. No cohort rebuild or IMF re-query.


## Continuation 185 — Indonesia (IDN) BI sign-presentation route fingerprint (2026-11-21)
| Country | Authority / exact source fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| IDN Indonesia | BI official BOP metadata `Indonesia_Summary_Balance_of_Payments_.pdf`, Section 4.3 (BPM6 concepts, published financial-account signs remain BPM5 inflow/outflow); BI SEKI Table V.7 `https://www.bi.go.id/SEKI/tabel/TABEL5_7.pdf`; IMF BPM6 Compilation Guide Table 8.10 | C185 report: `docs/GCR_INDONESIA_IDN_Q2_2026_BI_BPM5_TO_IMF_BPM6_SIGN_CROSSWALK_CONTINUATION185_20261121.md` | Asset sign crosswalk PASS; liability sign retained PASS; both Q2 numeric residuals within ±0.5 USDm PASS; BI Q2** very temporary; same-vintage/revision identity NOT_ESTABLISHED; overall PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED | Do not repeat the already completed exact IMF retrieval or sign-crosswalk derivation; do not reverse both legs or infer from net | New official BI SEKI V.7 Q2 revision/vintage record or a documented BI↔IMF same-vintage observation bridge |
- Reused existing cohort and exact-key receipt; no IMF re-query or cohort rebuild.


## Continuation 186 — IDN BI Q2-2026 revision-vintage fingerprint (2026-11-21)
| Country | Authority / source fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| IDN Indonesia | Bank Indonesia, *Neraca Pembayaran Indonesia — Realisasi Triwulan III 2026*, published 20-Nov-2026; official PDF Table 7 p.37 and Box 1 p.28; https://www.bi.go.id/id/publikasi/laporan/Documents/NPI_Tw-III_2026.pdf | C186 report: `docs/GCR_INDONESIA_IDN_Q2_2026_BI_NOV2026_REVISION_VINTAGE_RECHECK_CONTINUATION186_20261121.md` | Latest Q2 provisional legs: assets -1,466 USDm; liabilities +11,399 USDm; BI explicitly says Q1–Q2 2026 portfolio data revised due to LLD/ULN updates. BPM5→BPM6 mapping retained. Archived IMF 19-Nov snapshot residuals +21.605237 / +41.221642 USDm, outside ±0.5; same-vintage NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not reuse superseded BI Q2** values (-1,488 / +11,440) as current; do not repeat sign crosswalk; no new IMF GET or cohort rebuild | Later archived IMF snapshot with explicit retrieval/revision metadata, or official IMF observation vintage metadata that can be matched to BI's 20-Nov-2026 release |
- C186 establishes a national revision after the archived IMF transport snapshot; it does not establish the underlying IMF observation's source vintage. Aggregate remains NOT_AUTHORIZED.


## Continuation 187 — India Q1-2026 RBI Table 42 release fingerprint (2026-11-21)
| Country / scope | Official source fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| IND India, Q1-2026 | RBI Table 43 dated 22-Jun-2026 (₹ crore), Table 42 dated 22-Jul-2026 and 25-Aug-2026 (USDm); existing RBI October Table42 is Q2-only | C187 report: `docs/GCR_INDIA_IND_Q1_2026_RBI_TABLE42_RELEASE_PERSISTENCE_AUDIT_CONTINUATION187_20261121.md` | Q1 portfolio liabilities net -12,121 USDm and assets/by-India net +74 USDm unchanged in July/August; total -12,047. Existing IMF asset comparison PASS; liability residual -1,512.508347 USDm REVIEW; same-vintage/underlying cause NOT_ESTABLISHED; India Q1 PARTIAL / NOT PASS | Do not repeat the three RBI pages or IMF exact GET; no assumption that general revision policy proves this value changed | Distinct official RBI Q1 revision history / transaction-level liability series, or already archived IMF snapshot with explicit revision metadata |
- Q1 persistence does not explain the RBI/IMF liability residual; preserve REVIEW and aggregate NOT_AUTHORIZED.


## Continuation 188 — LKA CBSL page freshness / export fingerprint (2026-11-21)
| Country | Authority / source fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| LKA Sri Lanka | CBSL External Sector official search-indexed page; update marker 01-Oct-2026 11:30; page describes BPM6 quarterly BOP 2012Q1–Latest | C188: `docs/GCR_SRI_LANKA_LKA_Q2_2026_CBSL_EXTERNAL_SECTOR_PAGE_FRESHNESS_AND_EXPORT_GATE_CONTINUATION188_20261121.md` | Page freshness metadata PASS; current Table 2.10 export URL/bytes/hash and revision ID NOT_CAPTURED; C174 Treasury dual legs remain provisional strong reconciliation; same-vintage NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not repeat C175 direct Table 2.10 403, C177 stale 2017 SDDS BOP.xlsx route, or C176 secondary CSV/JSON click | Distinct official current export/API locator or an actual Table 2.10 Q2-2026 revision/vintage identifier |
- Page content update timestamp is not the statistical observation vintage. Aggregate NOT_AUTHORIZED.


## Continuation 189 — Guinea BCRG MPC attachment-link fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| GIN Guinea | BCRG 22nd MPC page https://www.bcrg-guinee.org/22eme-reunion-ordinaire-du-comite-de-politique-monetaire-de-la-republique-de-guinee/; visible “Télécharger” affordance | C189: `docs/GCR_GUINEA_GIN_Q2_2026_BCRG_MPC_DOWNLOAD_AFFORDANCE_AND_LINK_TARGET_ACCESS_GATE_CONTINUATION189_20261121.md` | Page PASS; attachment href/document URL NOT_EXPOSED; bytes/hash NOT_CAPTURED; Q2 separate portfolio legs NOT_CAPTURED; PARTIAL / NOT PASS | Do not guess URL or repeat same page extraction/static BOP page route | Distinct official attachment target or machine-readable BCRG export/API locator |
- This is an access-boundary record, not proof that national data are absent. Aggregate NOT_AUTHORIZED.


## Continuation 190 — Mongolia NSO PxWeb metadata API fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNG Mongolia | NSO PxWeb table `DT_NSO_0100_001V10_quarter`; exact API metadata route `https://data.1212.mn/api/v1/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter` | C190: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_API_METADATA_ROUTE_RECHECK_CONTINUATION190_20261121.md` | Table metadata PASS; API URL retrieval not accessible in current bridge; indicator labels/codebook and Q2 portfolio A/L NOT_CAPTURED; PARTIAL / NOT PASS | Do not repeat same API URL/surface or guess indicator codes | Different supported official export or NSO/Bank of Mongolia data attachment |
- Q2-2026 national dual-leg validation remains incomplete; aggregate NOT_AUTHORIZED.


## Continuation 191 — MNG corrected PxWeb metadata endpoint fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNG Mongolia | Corrected PxWeb metadata endpoint ending `DT_NSO_0100_001V10_quarter.px`; official table currently shows update marker 09-Nov-2026 | C191: `docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_CORRECTED_METADATA_ENDPOINT_AND_ACCESS_GATE_CONTINUATION191_20261121.md` | Endpoint syntax corrected, retrieval bridge still inaccessible; 69 indicator labels/codes and Q2 A/L cells NOT_CAPTURED; PARTIAL / NOT PASS | Do not repeat corrected URL through same retrieval surface; C190 omitted `.px` and is explicitly corrected | Distinct supported official export/attachment route or new raw payload |
- Page update marker is not an observation-level vintage. Aggregate NOT_AUTHORIZED.


## Continuation 192 — Albania legacy time-series route fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| ALB Albania | Bank of Albania legacy quarterly time-series detail: `https://www.bankofalbania.org/Statistics/External_sector_statistics/Balance_of_Payments/Time_Series-Balance_of_Payments.html?cregtab_id=705&evb=agregate&evn=agregate_detaje&periudha_id=3` | C192: `docs/GCR_ALBANIA_ALB_Q2_2026_BOA_Q2_RELEASE_CALENDAR_VS_LEGACY_TABLE_CEILING_CONTINUATION192_20261121.md` | Q2 release date PASS; legacy taxonomy EURm PASS; legacy method cites 2017 publication; Q2-2026 cells/export NOT_EXPOSED; PARTIAL / NOT PASS | Close same legacy Main-data route; do not repeat C140/C141 extraction | Distinct Q2-specific attachment, API response, or supported workbook export |
- The calendar date and landing-page update marker do not establish the Q2 observation vintage. Aggregate NOT_AUTHORIZED.


## Continuation 193 — IDN IMF vintage archive route fingerprint (2026-11-21)
| Country | Archive fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| IDN Indonesia | Repository archive docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json; 19-Nov-2026 IMF raw asset/liability receipts | C193: docs/GCR_INDONESIA_IDN_Q2_2026_IMF_ARCHIVED_VINTAGE_INVENTORY_AND_MATCH_GATE_CONTINUATION193_20261121.md | Later archived snapshot NOT_AVAILABLE; point-in-time vintage metadata NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not re-query IMF or repeat identical repository inventory | New archived IMF snapshot, official observation revision timestamp, or documented BI↔IMF vintage bridge |
- C186 residuals remain +21.605237 / +41.221642 USDm; aggregate NOT_AUTHORIZED.


## Continuation 194 — CHN SAFE time-series XLSX route fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| CHN China | SAFE BOP time-series page `https://www.safe.gov.cn/en/2019/0329/1496.html`; exact linked XLSX `https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx` | C194: `docs/GCR_CHINA_CHN_Q2_2026_SAFE_OFFICIAL_TIMESERIES_WORKBOOK_LOCATOR_AND_RAW_ACCESS_GATE_CONTINUATION194_20261121.md` | Official href PASS; XLSX raw retrieval BLOCKED / NOT_CAPTURED; workbook cells and asset sign bridge NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not retry same unsupported MIME/download route or substitute IIP/net | Exact workbook retrievable through supported file workflow or distinct official machine-readable export |
- Existing CHN magnitude checks remain unchanged; aggregate NOT_AUTHORIZED.


## C194 correction — CHN English/Chinese SAFE XLSX duplicate route (2026-11-21)
| Country | Route fingerprint | Evidence | Corrected status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| CHN China | SAFE English detail page `https://www.safe.gov.cn/en/2019/0329/1496.html` → XLSX `https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx`; Chinese attachment route previously recorded in C136 | C135 and C136 reports; C194 was a repeat of the known English XLSX endpoint | Locator already known; raw XLSX remains BLOCKED / NOT_CAPTURED; C194 DUPLICATE / NO PROGRESS | Do not retry either known English/Chinese XLSX via same unsupported retrieval surfaces | A genuinely different supported file-transfer path or distinct official dataset/export is available |
- C136's COL next action is restored; inspect prior COL route history before any new action. Mandatory full preflight and read-back gate added to Master Ledger.


## Continuation 195 — MKD NBRNM PxWeb API metadata route fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MKD North Macedonia | NBRNM ES-001 table `6_FinansiskaSmetkaTrimesecniEN.px`; tested PxWeb v1 metadata path ending in the same `.px` filename | C184 source report; C195 `docs/GCR_NORTH_MACEDONIA_MKD_Q2_2026_NBRNM_PXWEB_API_METADATA_ROUTE_ACCESS_GATE_CONTINUATION195_20261121.md` | Table metadata PASS; API retrieval inaccessible; codebook, Q2 portfolio A/L values, bytes/hash and vintage NOT_CAPTURED; PARTIAL / NOT PASS | Do not retry exact API URL through same retrieval surface; do not use SSO net-only or financial-account-wide legs | Supported API/export retrieval or distinct official Q2 portfolio dual-leg attachment |
- Aggregate NOT_AUTHORIZED.


## Continuation 196 — PER BCRP current catalogue scope fingerprint (2026-11-21)
| Country | Authority / exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| PER Peru | BCRP quarterly catalogue https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales; USD-million financial-account series; Q2-2026; full-economy portfolio A/L | C196: docs/GCR_PERU_PER_Q2_2026_BCRP_CATALOGUE_REFRESH_AND_PUBLIC_ASSET_SCOPE_GATE_CONTINUATION196_20261121.md | Catalogue refresh PASS; private portfolio A/L PN39278BQ/PN39285BQ and public portfolio liability PN39404FQ listed; no public portfolio-specific asset series in displayed public-sector 25-series group; full-economy scope NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not combine private portfolio assets with aggregate public-sector assets PN39402FQ; do not retry prior inaccessible BCRP API route through same retrieval surface | Distinct official public-sector portfolio asset transaction series or explicit official scope statement proving private asset series is full-economy |
- No Q2 raw values/bytes/hash captured; aggregate NOT_AUTHORIZED.


## Continuation 197 — ROU BNR Interactive Database route fingerprint (2026-11-21)
| Country | Authority / exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| ROU Romania | National Bank of Romania; https://www.bnr.ro/en/2550-interactive-database; Statistics → Interactive Database → Balance of payments; Q2-2026; total-economy portfolio investment transaction assets/liabilities | C197: docs/GCR_ROMANIA_ROU_Q2_2026_BNR_INTERACTIVE_DATABASE_OFFICIAL_ROUTE_DISCOVERY_CONTINUATION197_20261121.md | Distinct official route locator PASS; dynamic controls/table locator/export not exposed; Q2 A/L values and raw bytes/hash NOT_CAPTURED; ROU PARTIAL / NOT PASS | Not a repeat of closed ECB SDW API route; do not claim data retrieval | JS-capable browser executes official BNR query/export and captures exact Q2 dual legs, metadata, revision vintage and SHA-256 |
- Keep BNR external-custodian coverage caveat visible; aggregate NOT_AUTHORIZED.


## Continuation 198 — Cross-country interactive-portal execution gate (2026-11-21)
| Scope | Official route families | Evidence | Status | Duplicate / selection rule |
|---|---|---|---|---|
| ROU Romania | BNR Interactive Database; C197 official locator + IMF DSBB metadata | C198: `docs/GCR_INTERACTIVE_OFFICIAL_PORTAL_EXECUTION_CAPABILITY_GATE_CONTINUATION198_20261121.md` | Locator PASS only; current session lacks JS-capable browser action; Q2 A/L/export NOT_EXECUTED | Do not repeat JS-shell inspection or closed ECB API. Reopen only with actual interactive browser capability or user-supplied official export |
| GEO Georgia | NBG NSDP BOP SDMX label / Statistics Data UI | C154 + C198 | No BOP download href/target or data payload exposed in captured text; stale NSDP Q3/21 remains excluded; PARTIAL / NOT PASS | No repeat same page-shell inspection. Reopen only with exact official export/API target or browser capability |
| BIH Bosnia and Herzegovina | CBBH Panorama Necto | C156 + C198 | Anonymous portal and Excel/PDF controls documented; workboard/export NOT_EXECUTED | UI task requires actual JS-capable browser |
| MDA Moldova | BNM Reports Generator | C86 + C198 | Selectors and Generate/Export controls documented; report/export NOT_DONE | UI task requires actual JS-capable browser or user-supplied official export |
- Permanent rule: route type must be classified before task selection; UI route is not executable without an actual JS-capable browser action. Mark `NOT_EXECUTED — UI CAPABILITY UNAVAILABLE`; advance to a retrievable static official route. Never promote locator/page-shell discovery to data retrieval PASS.
- No country data or national validation promoted in C198; aggregate NOT_AUTHORIZED; immutable cohort and IMF archive unchanged.


## Continuation 199 — ARM current-domain CBA export route fingerprint (2026-11-21)
| Country | Official route fingerprint | Evidence | Status | Duplicate / selection rule |
|---|---|---|---|---|
| ARM Armenia | CBA Financial Account page https://www.cba.am/en/statistics/financial-account/275; exact Export all target https://www.cba.am/en/statistics/financial-account/275/export-all/; formats XLSX/XML/JSON; Q2-2026 BPM6 BOP portfolio A/L | C143 legacy XLS report + C199 docs/GCR_ARMENIA_ARM_Q2_2026_CBA_CURRENT_FINANCIAL_ACCOUNT_EXPORT_ROUTE_GATE_CONTINUATION199_20261121.md | New current-domain locator/control PASS; export target timed out; Q2 portfolio A/L and raw bytes/hash NOT_CAPTURED; ARM PARTIAL / NOT PASS | Do not retry C143 legacy XLS URL or same C199 export-all target via same retrieval surface. Reopen only on a distinct supported machine route or successful official export bytes |
- CBA metadata confirms USD million, quarterly BPM6 BOP and annual revision practice; Armstat Q2 NSDP summary omits separate portfolio flow line (not zero); IIP stocks excluded.
- No country validation promoted; aggregate NOT_AUTHORIZED; no IMF re-query/cohort rebuild. Apply C198 Execution-Mode Gate to future selections.


## Continuation 200 — 63-country master matrix inventory (2026-11-21)
- Immutable cohort source: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA-1 `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- Consolidated matrix: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_CONTINUATION200_20261121.md` and `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`.
- Snapshot: 63 rows; stage SOURCE_FOUND 20 / DATA_CAPTURED 23 / BLOCKED 19 / NOT_STARTED 1 / FULL_PASS 0. Per-leg asset PASS 15, liability PASS 15; vintage PENDING 23, UNKNOWN 40. 63/63 remain outside FULL_PASS and aggregate admission remains NOT_AUTHORIZED.
- The matrix is a conservative inventory, not an exhaustive line-by-line re-audit. Use the latest country continuation as authority; no status promotion from a source locator, numerical rounding match, IIP stock, net-only figure, or publication date alone.
- No IMF re-query/cohort rebuild; immutable constraints retained.


## Continuation 200 — 63-country Q2-2026 master status matrix (2026-11-21)
- Added `docs/GCR_2026Q2_63_COUNTRY_MASTER_STATUS_MATRIX_CONTINUATION200_20261121.md` and machine-readable companion `docs/evidence/gcr_2026q2_country_master_status_matrix.csv`.
- Immutable cohort input reused unchanged: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; 63 rows, both IMF Q2 legs present for each. No cohort rebuild or IMF re-query.
- Bounded inventory snapshot: SOURCE_FOUND or later 58/63; DATA_CAPTURED 12; ASSET_PASS 6; LIABILITY_PASS 6; VINTAGE_PASS 0; FULL_PASS 0; BLOCKED 24; NOT_STARTED 4. All aggregate_admission remain NOT_AUTHORIZED.
- Important limitation: matrix is a first conservative inventory, not exhaustive 63-country report-history re-audit. NOT_STARTED means no evidence surfaced in bounded inventory, not proof of no prior work. The per-country notes and gates are explicit in the matrix; statuses must be refined only after exact report inspection.
- Next: complete exhaustive 63-country report-history audit, then reconcile leg-specific and vintage statuses. Never promote a country to FULL_PASS without both separate national legs, scope/sign/scale, same-vintage and provenance gates.


## Continuation 201 — 63-country Q2-2026 national validation matrix reconciled (2026-11-21)
- Immutable cohort CSV SHA-1: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`; exactly 63 unique members.
- Matrix CSV: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`; explicit YES/NO flags added for NOT_STARTED, SOURCE_FOUND, DATA_CAPTURED, ASSET_PASS, LIABILITY_PASS, VINTAGE_PASS, FULL_PASS and BLOCKED.
- Exact cohort-to-matrix reconciliation: 63/63; missing 0; extra 0; duplicate 0.
- Current stages: NOT_STARTED 1; SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19. Therefore 40 countries remain below DATA_CAPTURED (20+19+1); 23 have captured national values, not necessarily accepted.
- Independent gates: ASSET_PASS 15; LIABILITY_PASS 15; VINTAGE_PASS 0; FULL_PASS 0. These gate counts overlap; do not sum them.
- No country has FULL_PASS; aggregate remains NOT_AUTHORIZED. Matrix is a status inventory, not a complete line-by-line re-audit of every historical report; latest country continuations control promotions.
- Detail: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_RECONCILIATION_CONTINUATION201_20261121.md`.
- CSV update commit: `f596dc889642e3a9262f2fd7b7dc9b02a6a57a0a`; CSV blob SHA-1: `45e466c72c034d460dfccf57474b07bfb6d12ea9`.
- Preserve immutable cohort, no IMF re-query/rebuild, no unsupported inference, ₹0, and all V11.3 production invariants.


## Continuation 200 — 63-country national validation master matrix (2026-11-21)
| Artifact | Result |
|---|---|
| Immutable cohort | 63 rows; both IMF entries present; unchanged |
| Master matrix | Existing file upgraded in place with normalized status columns |
| Membership/period/entry alignment | 63/63 exact; 0 mismatches |
| Overall statuses | SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19; NOT_STARTED 1; FULL_PASS 0 |
| Vintage | No VINTAGE_PASS established in this baseline |
| Aggregate | NOT_AUTHORIZED |
- Report: `docs/GCR_63_COUNTRY_Q2_2026_NATIONAL_VALIDATION_MASTER_MATRIX_AUDIT_CONTINUATION200_20261121.md`.
- DATA_CAPTURED is not FULL_PASS; inspect original gate and country report before promotion. Blocked route fingerprints remain closed absent new evidence.


### C201 read-back correction — final matrix snapshot
- Final read-back matrix CSV blob SHA-1: `64bb4a85cb2f004b5faa906b6353a6f71ecb9ad2`. The CSV currently has 63 data rows and 30 columns, including the eight requested YES/NO status flags plus detailed source/data/asset/liability/vintage/overall status and evidence_ref fields.
- The earlier C201 CSV commit blob SHA `45e466c72c034d460dfccf57474b07bfb6d12ea9` is a prior intermediate snapshot; use the final read-back blob SHA above.
- Recomputed from the final CSV: NOT_STARTED 1; SOURCE_FOUND 20; DATA_CAPTURED 23; BLOCKED 19; ASSET_PASS 15; LIABILITY_PASS 15; VINTAGE_PASS 0; FULL_PASS 0. Cohort membership remains exact 63/63.
- Interpretation unchanged: 40 are below DATA_CAPTURED; 23 have national data recorded but remain short of FULL_PASS; all 63 remain not fully accepted; aggregate NOT_AUTHORIZED.


## Continuation 202 — Nigeria NGA historical evidence reconciliation (2026-11-21)
- Existing report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md` was inspected; CBN Q2-2026 BOP Highlights national source and both portfolio legs are already captured. Six comparisons (assets/liabilities across Q2-2025, Q1-2026, Q2-2026) PASS within the report's ±USD 5m rounding tolerance. Q2-2026 is provisional; same-vintage bridge remains pending.
- Corrected stale NGA row in `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`: DATA_CAPTURED; ASSET_PASS; LIABILITY_PASS; VINTAGE_PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED. evidence_ref now points to the Nigeria report.
- Final matrix blob SHA-1 read-back verified: `f9d68b4a24d92c41e6c72db776d89254a8f6d7de` (63 rows, 30 columns; NGA row verified).
- Detail: `docs/GCR_NIGERIA_NGA_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION202_20261121.md`.
- Recomputed stages after this single-country correction: SOURCE_FOUND 19; DATA_CAPTURED 24; BLOCKED 19; NOT_STARTED 1; ASSET_PASS 16; LIABILITY_PASS 16; VINTAGE_PASS 0; FULL_PASS 0. Below DATA_CAPTURED: 39. Counts are not additive across independent gates.
- No IMF re-query/cohort rebuild; aggregate remains NOT_AUTHORIZED; ₹0; all production invariants unchanged; UNKNOWN never PASS.


## Continuation 203 — PAK Pakistan matrix status correction (2026-11-21)
| Country | Existing evidence / report | Corrected matrix status | Duplicate prevention / open gate |
|---|---|---|---|
| PAK Pakistan | C51–C52 in `docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md`; C203 detail: `docs/GCR_PAKISTAN_PAK_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION203_20261121.md` | DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat SBP source fetch, archived IMF row extraction, BPM6 sign crosswalk or 2/2 numeric comparison. Reopen vintage only on observation-specific SBP revision history or an exact IMF same-vintage receipt/bridge. |
- Matrix CSV read-back SHA-1: `2e9b5a9246cebc249acc2e615cae5e43d4d8f4ac`; 63 rows / 30 columns. Counts: SOURCE_FOUND 18; DATA_CAPTURED 25; BLOCKED 19; NOT_STARTED 1; ASSET_PASS 17; LIABILITY_PASS 17; VINTAGE_PASS 0; FULL_PASS 0.
- PAK remains PARTIAL / NOT PASS; no aggregate admission. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS; production invariants unchanged.


## Continuation 204 — BOL Bolivia historical matrix reconciliation (2026-11-21)
| Country | Authority / route fingerprint | Evidence | Corrected status | Duplicate decision / reopen only if |
|---|---|---|---|---|
| BOL Bolivia | BCB Q2-2026 VI Manual BOP workbook and time-series XLSX; Q2-2026 separate portfolio assets/liabilities | C158 report `docs/GCR_BOLIVIA_BOL_Q2_2026_BCB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION158_20261121.md`; C204 matrix reconciliation `docs/GCR_BOLIVIA_BOL_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION204_20261121.md` | Official Q2 locators FOUND; both same-route XLSX retrievals HTTP 400; no bytes/values; BLOCKED / PARTIAL / NOT PASS | Do not retry identical XLSX routes via same retrieval surfaces. Reopen only with a distinct supported official export/byte-transfer path. No H1/annual substitution. |

- C204 corrected the stale BOL row in `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv` from NOT_STARTED/NOT_FOUND to BLOCKED with source_gate=FOUND, data_capture=NO, both national legs NOT_CAPTURED, vintage UNKNOWN, FULL_PASS=NO, aggregate NOT_AUTHORIZED.
- Matrix read-back: 63 rows; NOT_STARTED 0; SOURCE_FOUND 18; DATA_CAPTURED 25; BLOCKED 20; ASSET_PASS 17; LIABILITY_PASS 17; VINTAGE_PASS 0; FULL_PASS 0. Gate counts overlap.
- No IMF re-query/cohort rebuild, no national XLSX retry, no synthetic values, no production changes; UNKNOWN never PASS.


## Continuation 205 — IND India Q2-2026 official RBI dual-leg matrix fingerprint (2026-11-21)
| Country | Official source / period | Evidence | Corrected status | Duplicate prevention / remaining gate |
|---|---|---|---|---|
| IND India | RBI Table 42, Apr-Jun 2026, published 23-Oct-2026; USD million; BPM6 | docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md; C205 docs/GCR_INDIA_IND_Q2_2026_HISTORICAL_EVIDENCE_MATRIX_RECONCILIATION_CONTINUATION205_20261121.md; crosswalk CSV blob 8ff2534dc730c822b20351530b9379fb86369cb2 | Q2 asset, liability and combined net each PASS within ±0.5 USDm; matrix DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat RBI Table 42 Q2 capture, IMF comparison, or sign/scale mapping. Q1-2026 liability remains REVIEW under C187. Reopen only for exact RBI/IMF same-vintage bridge or Q1 underlying liability evidence. |
- Q2 raw RBI HTML SHA-256: 075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396. Archived crosswalk confirms Q2 residuals: asset -0.489413221 USDm; liability +0.240053743 USDm; combined net -0.270533037 USDm.
- C205 matrix read-back is pending; Q2 vintage remains PENDING and India is not FULL_PASS.


### C205 read-back closure — 2026-11-21
- Matrix row IND re-fetched from default branch and verified as DATA_CAPTURED / asset PASS / liability PASS / vintage PENDING / FULL_PASS NO / aggregate NOT_AUTHORIZED.
- Recomputed matrix: 63 rows; SOURCE_FOUND 17; DATA_CAPTURED 26; BLOCKED 20; NOT_STARTED 0; ASSET_PASS 18; LIABILITY_PASS 18; VINTAGE_PASS 0; FULL_PASS 0. Aggregate remains NOT_AUTHORIZED.
- C205 detail report and updated Master Ledger, Priority Queue, Registry and Matrix all re-fetched after writes. No additional source or data status was promoted.


## Continuation 206 — ARG matrix evidence-reference correction (2026-11-21)
- Existing ARG report `docs/GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md` confirms separate Q2-2026 numeric asset/liability comparisons PASS at published USDm rounding; same-vintage NOT_ESTABLISHED. Failed INDEC text/xml and Datos Argentina CSV routes remain closed for identical retries.
- Matrix defect: evidence_ref was stale placeholder despite existing report. Corrected evidence_ref only to the dedicated report basename; DATA_CAPTURED, ASSET_PASS, LIABILITY_PASS, VINTAGE_PENDING, FULL_PASS=NO, aggregate NOT_AUTHORIZED unchanged.
- Matrix commit `c8b346302cea6197b0de577ef26045fd7dc0eb70`; blob SHA-1 `1fa8a1e7c57b064ad58f51e6ae18ebe8c3336daf`; detail report `docs/GCR_ARGENTINA_ARG_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION206_20261121.md`.
- Do not repeat numerical comparison or closed vintage routes. Reopen only with a distinct official versioned Q2 source/revision record. No IMF re-query, cohort rebuild or production changes; UNKNOWN never PASS.


## Continuation 207 — BDI matrix evidence-reference correction (2026-11-21)
- BDI C155 BRB source-boundary report exists and documents historical Q4/Q3-2025 dual-leg tables, but explicitly does not capture Q2-2026 national legs. The matrix evidence_ref was stale placeholder.
- Corrected BDI evidence_ref only to `GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121`. No Q2 data, unit/sign, comparison or vintage gate promotion.
- Matrix commit `641e119f6a7dd13a2fd4893bf3549592152acb62`; blob SHA-1 `7a27ec249675fb40721340f3ed065ca9a2c5bb5c`; C207 detail report `docs/GCR_BURUNDI_BDI_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION207_20261121.md`.
- BDI remains PARTIAL / NOT PASS; Q2 legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. No repeated BRB/IMF routes; ₹0; UNKNOWN never PASS.


## Continuation 208 — MEX matrix evidence-reference correction (2026-11-21)
- Existing Banxico report already contains separate Q2-2026 asset/liability numeric PASS comparisons; the matrix evidence_ref remained a stale placeholder.
- Corrected MEX evidence_ref only to `GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120`. Numeric gates remain PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. Exact same-vintage bridge remains NOT_ESTABLISHED.
- Matrix commit `f9094b380ff959e13d59a9d68713cb35fe82e42c`; blob SHA-1 `efcc44b085abd2ff250a82c988b9a4fa2dc69c23`; C208 report `docs/GCR_MEXICO_MEX_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION208_20261121.md`.
- Do not repeat completed numeric comparison or infer vintage from close residuals. ₹0; UNKNOWN never PASS.


## Continuation 209 — Thailand THA Q2-2026 matrix evidence-link correction (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and dedicated BOT–IMF report before selection. Rejected repeat numeric PASS and same-page source retrieval.
- Existing BOT report records Q2 assets +4,679.07 USDm and liabilities -238.36 USDm; archived IMF residuals +0.00342150334 / +0.001811289819 USDm, both PASS at ±0.005 USDm. BOT source remains preliminary; same-vintage NOT_ESTABLISHED.
- Corrected only THA matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120. THA remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_THAILAND_THA_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION209_20261121.md`. Matrix commit `0c3e3c46b5d56678295e2e02dfe0f4637ccc9b78`; matrix blob SHA `a9162af9a86514eaf78f741ba5e8c5927da50a7d`. Detail report commit `0be627c2d5aed9f94e017e4752602f71ad406209`.
- No BOT/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 210 — Costa Rica CRI Q2-2026 matrix evidence-link correction (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, 63-country matrix and dedicated SECMCA/BCCR report before selection; no repeat numeric work or source retrieval.
- Existing report records Q2 portfolio assets +1,275.5 USDm and liabilities +1,167.5 USDm; residuals +0.04033796522 / -0.00633015469 USDm, both PASS at 0.1 USDm display precision. Direct BCCR raw-file SHA-256 and exact same-vintage bridge remain NOT_ESTABLISHED.
- Corrected only CRI matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_COSTA_RICA_CRI_Q2_2026_SECMCA_BCCR_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION148_20261121. CRI remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_COSTA_RICA_CRI_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION210_20261121.md`. Matrix commit `a442364f24dc3bfae527e2a6d3965613da9d1138`; matrix blob SHA `027d23b1a5ba868dad697d92061425d6c7915c37`; detail report commit `f42b0369004e20c3bc1034c64885683b4d64cc85`.
- No SECMCA/BCCR re-fetch, IMF re-query/cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 211 — Ecuador ECU Q2-2026 matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and dedicated BCE report before selection. Rejected repeat numeric comparison and source retrieval.
- Existing BCE report records Q2 assets -595.2 USDm and liabilities +1,000.3 USDm; residuals -0.03583203999 / -0.048809 USDm, both PASS at 0.1 USDm publication precision. National raw-file SHA-256 NOT_CAPTURED; same-vintage NOT_ESTABLISHED.
- Corrected only ECU matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121. ECU remains DATA_CAPTURED; asset/liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_ECUADOR_ECU_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION211_20261121.md`; matrix commit `7ab32d8bb18a77b6c4ed8837a71fc4de2d8b444d`; matrix blob SHA-1 `15b89466d49e1f38c2d9c01a9dd3041f7971126b`; detail report commit `b48a52c2b92ad0a61e8df2a4f7920218b27568de`.
- No BCE/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 212 — Philippines PHL Q2-2026 matrix evidence-link reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and controlling BSP–IMF report before selection. Completed parser/capture/numeric work and closed generic vintage-search routes were not repeated.
- Existing report records BSP Q2 assets +1,331 USDm and liabilities +1,798 USDm; IMF differences -0.35704894474 / +0.28261626536 USDm, both within ±0.5 USDm. Successful raw/parsed artifact and release parity are documented; same-vintage remains NOT_ESTABLISHED.
- Corrected only PHL matrix evidence_ref from NO_DEDICATED_REPORT_REF_IN_BASELINE to GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120. Preserved DATA_CAPTURED, asset REVIEW, liability REVIEW, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED; no gate promotion.
- Detail: `docs/GCR_PHILIPPINES_PHL_Q2_2026_HISTORICAL_MATRIX_EVIDENCE_LINK_RECONCILIATION_CONTINUATION212_20261121.md`; matrix commit `4de3e0c125678ba9dfbe75b8358ae29478f9cdb8`, blob SHA-1 `a1a49e1d9517f09afcf584286d698aac637307a4`; report commit `270f5714db041305fd8839639804e2a4cb5c6c9e`.
- No BSP/IMF re-fetch, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 213 — Cabo Verde CPV Q2-2026 BPM6 methodology conflict resolution (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Task Registry, 63-country matrix and C153 BCV source-gate report. Excluded repeated failed XLS retrieval; selected the distinct open BPM5/BPM6 methodology conflict.
- Official BCV June-2016 external-sector methodology explicitly documents BPM6 adoption, distinguishes BOP flows from IIP stocks, defines portfolio investment, and states BPM6 sign convention/gross reporting. The IMF e-GDDS BPM5 entry is therefore treated as likely legacy metadata, not current proof. The 12-Nov-2026 BCV methodology notice concerns monetary/financial statistics and does not supersede the external-sector note.
- Updated only CPV matrix descriptive note; retained SOURCE_FOUND, NOT_CAPTURED legs, UNKNOWN vintage, FULL_PASS NO and aggregate NOT_AUTHORIZED. No numeric gate promotion.
- Detail: `docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_BPM5_BPM6_METHODOLOGY_CONFLICT_RESOLUTION_CONTINUATION213_20261121.md`; matrix commit `d5c778f5ad1063a3d39ade392d2224bb6c04b1ce`, blob SHA-1 `1569f1eb77b5ad3eaddea881f72e5ca23ab5522e`; report commit `79d2ff1f143d1e17ce3b1d6013a101846978fd72`.
- No BCV XLS retry, IMF re-query, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.


## Continuation 214 — CPV C213 matrix evidence-reference read-back correction (2026-11-21)
- Preflighted the current Master Ledger, Priority Queue, Historical Task Registry and 63-country matrix; reopened C213. Found C213 had updated the CPV descriptive note but left evidence_ref at older C153.
- Corrected only CPV evidence_ref to `GCR_CABO_VERDE_CPV_Q2_2026_BCV_BPM5_BPM6_METHODOLOGY_CONFLICT_RESOLUTION_CONTINUATION213_20261121`. Matrix commit `e794becb96cf8342c3a285f156138b444f29731e`; blob SHA-1 `c14f4f8799e2c25cf054fbac4366c5840cf3c66e`.
- Preserved SOURCE_FOUND; data_capture NO; asset/liability NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED. No numeric or country gate promotion.
- Detail: `docs/GCR_CABO_VERDE_CPV_Q2_2026_MATRIX_EVIDENCE_REFERENCE_READBACK_CORRECTION_CONTINUATION214_20261121.md`; report commit `f0483d5696df1122b98195e273de5b0363d58cdf`.
- No BCV XLS retry, IMF re-query, cohort rebuild, synthetic data or production changes; ₹0; protected invariants unchanged; UNKNOWN never PASS.


## Continuation 215 — ZAF official SARB daily FX API route discovery (2026-11-21)
- Preflighted current Master Ledger, Priority Queue, Historical Task Registry and 63-country matrix; reopened controlling ZAF reconciliation and C127 FX boundary. Existing liability PASS and asset REVIEW were not recalculated.
- Discovered official SARB OpenAPI contract: `GET /WebIndicators/HistoricalExchangeRatesDaily`; live snapshot identifies “Rand per US Dollar”, series `EXCX135D`, latest observation 2026-11-20 = 17.4429. OpenAPI also documents date-bounded `GetTimeseriesObservations/{timeseriesCode}/{startDate}/{endDate}`.
- Attempted Q2 2026 date-bounded endpoint; current retrieval channel returned inaccessible/internal error. No Q2 rows, raw bytes/hash or response metadata captured. This is a retrieval-channel boundary, not proof SARB lacks the data. BOP transaction FX convention remains NOT_ESTABLISHED; ZAF asset REVIEW / NOT PASS; aggregate NOT_AUTHORIZED.
- Updated only ZAF matrix descriptive note; all stage/gate fields preserved. Matrix commit `95540297274a9a6f001e7b0f49dd47050f5acce2`; blob SHA-1 `3758ed7d60f65fffeffbd43d7228ffeb92bbc3f6`.
- Detail: `docs/GCR_ZAF_Q2_2026_SARB_OFFICIAL_DAILY_FX_API_ROUTE_DISCOVERY_CONTINUATION215_20261121.md`; report commit `51b16cb4e839ca32337be1c6e1becfa4739f4a7f`.
- Next: obtain the documented historical payload through a supported HTTP/API-capable route; validate dates/coverage and only use a daily mean if SARB's BOP conversion convention supports it. No IMF re-query/cohort rebuild, synthetic data, tolerance widening or production change; ₹0; UNKNOWN never PASS.


### C215A — ZAF matrix gate-orientation correction (2026-11-21)
- Independent read-back found the ZAF matrix asset/liability gates inverted relative to the controlling reconciliation: matrix had asset PASS / liability REVIEW, while the report has asset REVIEW / liability PASS.
- Corrected matrix to asset_gate REVIEW, liability_gate PASS; status_ASSET_PASS NO, status_LIABILITY_PASS YES; asset_status DATA_CAPTURED, liability_status LIABILITY_PASS. Stage DATA_CAPTURED, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED preserved.
- Matrix correction commit `86dfe96ae4b3a71a78a0eebbabd4fd36bd4ac4e3`; blob `a4ed9fcf8732dd81a1d1563aaf5388ed6c2bbd0a`. C215 report addendum commit `96cf932d5345859c01b7fb92ade0986f992b0ec5`.
- New SARB API Q2 historical payload remains NOT_CAPTURED; asset FX REVIEW remains open. No gate promotion, IMF re-query, cohort rebuild, tolerance widening or production change; UNKNOWN never PASS.

## Continuation 217 — ZAF SARB Online Statistical Query export-family boundary (2026-11-21)
- Preflighted and re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and controlling C215/C215A/C216 reports before selection. Existing PASS work was excluded.
- Verified SARB's official Online Statistical Query workflow: KBP code/keyword search, available-version selection, frequency/date-range selection, and Excel/CSV/PDF/DOC exports for Quarterly Bulletin time series. The page documents the 29-Sep-2026 KBP1 Week 5 date-format change.
- Explicit boundary: this KBP-prefixed Quarterly Bulletin export facility is not proven to expose daily FX series EXCX135D. No code mapping, export URL or Q2 FX payload was guessed or claimed. It is not a substitute for the daily SARB API series.
- ZAF asset REVIEW / NOT PASS; liability PASS retained; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. No matrix gate changes, IMF re-query, cohort rebuild or production change.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_ONLINE_STATISTICAL_QUERY_EXPORT_FAMILY_BOUNDARY_CONTINUATION217_20261121.md.
- Next C218: establish whether any official KBP daily USD/ZAR series is documented and independently inspect the Selected Historical Rates export request via a supported HTTP-capable route. ₹0; UNKNOWN never PASS.
## Continuation 218 — ZAF official SARB KBP5339M monthly USD/ZAR series verification (2026-11-21)
- Preflighted current Master Ledger, GCR Priority Queue, Historical Task Registry and C216/C217. Completed daily API discovery, matrix correction and C217 export-family boundary were excluded from repeat work.
- Official SARB September 2026 Quarterly Bulletin, External economic accounts, p. S-114, identifies the USA Dollar monthly-average middle-rate series as (5339M), in SA cents per USD. Footnote: weighted average of banks' daily rates at approximately 10:30, weighted by banks' FX transactions.
- Q2 values verified: April 1,653.90 cents = R16.5390/USD; May 1,648.06 = R16.4806/USD; June 1,639.70 = R16.3970/USD. No quarterly aggregation.
- This is monthly KBP5339M, not daily API EXCX135D. The 10:30 footnote does not establish BOP portfolio-transaction conversion convention. Daily history and BOP methodology remain NOT_ESTABLISHED; ZAF asset REVIEW / NOT PASS; liability PASS retained; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_KBP5339M_OFFICIAL_MONTHLY_USD_ZAR_SERIES_VERIFICATION_CONTINUATION218_20261121.md. Next C219: verify any official daily USD/ZAR series separately and locate current SARB BOP portfolio FX conversion methodology. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.
## Continuation 219 — ZAF SARB B03/B31 reporting-currency and FX-methodology boundary (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue and Historical Task Registry; reopened C127 methodology boundary and C216–C218 reports plus original ZAF numeric reconciliation. Completed work was excluded.
- New official sources inspected: SARB B03 guide (May 2021) and B31 guide (June 2021). Both use ZAR-thousand reporting; B03 requires accrual/transaction-time recording and market-price valuation for traded equity/debt; B31 covers quarterly cross-border transactions of institutional investors, records at transaction value/time and requires ZAR thousands.
- Neither public guide specifies the compiler-side FX rate source or method used to translate foreign-currency transaction records into published BOP USD series. IMF BPM6 3.104–3.106 supplies the international benchmark (transaction-date midpoint; daily average approximation; shortest-period average if daily unavailable; convert underlying flows before derived aggregates), but does not prove SARB's exact implementation.
- Prior ZAF liability arithmetic PASS and asset REVIEW remain historical arithmetic only; conversion-method equivalence remains NOT_ESTABLISHED. Daily EXCX135D payload NOT_CAPTURED; ZAF overall PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ZAF_Q2_2026_SARB_B03_B31_REPORTING_CURRENCY_FX_METHODOLOGY_BOUNDARY_CONTINUATION219_20261121.md. ZAF public guide route is bounded/closed pending new evidence. Resume cohort rank-1 next country CHN per C127, without IMF re-query or cohort rebuild. ₹0; UNKNOWN never PASS.
## Continuation 220 — MNE CBCG Bulletin 9/2026 alternate-host route fingerprint update (2026-11-21)
- MNE route: CBCG Bulletin archive → official PDF `https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf` → printed page 54 Tables 5.1–5.4 download affordance.
- New evidence: alternate official `www` hostname successfully renders PDF; direct raw-byte transfer failed; hyperlink destination not exposed by text extraction. No table export URL/bytes/values/hash. Existing C182 ZIP/XML routes remain closed; this is only an alternate PDF rendering path.
- Status: PDF rendering PASS; export destination NOT_RESOLVED; national dual legs NOT_CAPTURED; MNE PARTIAL / NOT PASS. Reopen only on raw PDF annotation access or distinct official table export URL.
- Next candidate MNG NSO PxWeb API; require exact endpoint/request method from official documentation before any query. No guessed indicator codes or payload.
## Continuation 221 — MNG official NSO PxWeb API terms / route fingerprint (2026-11-21)
- Official NSO Terms of Use URL `https://www.nso.mn/en/terms_of_use`: OPEN DATA API exists; JSON/XML outputs; CC BY 4.0; maximum one request per second per IP.
- Official table `DT_NSO_0100_001V10_quarter` page confirms 69 Indicator values, 71 Quarter values, Q2 `2026-2`, million USD, quarterly frequency and Bank of Mongolia as source.
- Exact official API root/path, method, query schema and indicator keys NOT_DOCUMENTED in inspected official sources. No API call or national data extraction performed. MNG PARTIAL / NOT PASS; no aggregate authorization.
- Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_OFFICIAL_API_CONTRACT_BOUNDARY_CONTINUATION221_20261121.md. Reopen only on official API contract/export evidence.

## Continuation 222 — MNG matrix evidence-reference/read-back correction (2026-11-21)
- Matrix evidence_ref corrected to C221 official API-contract boundary report; descriptive note records quarterly USDm/Q2 2026-2 metadata and the unresolved exact API contract.
- No country gate promotion: MNG BLOCKED; national A/L NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Final matrix commit `2074feae218e6890088d95412fbf7a1013c71bbf`; C222 report commit `7eea1f9e2341be21351a7e5201e95aa3c49a283b`.
- Duplicate prevention: do not repeat C221 terms/table metadata checks or failed C179/C190/C191 API routes. Reopen only with official endpoint contract or official export bytes.


## Continuation 223 — GEO NBG Statistics Data route fingerprint
- Official NBG Statistics page and Statistics Data search surface verified; rendered content states static Excel/interactive dashboard dissemination but does not expose a Q2 BOP workbook locator, API contract or payload.
- C154 Q2 release/BPM5 and stale NSDP boundaries reused. Matrix evidence_ref corrected to C154; national data/gates unchanged. GEO remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Matrix commit `9655247cb907dee8e4846bd9dd33e6b5d91f67c0`; blob `de7b182d3a3debee674c35c1e9fd980e99ab83b3`; C223 report commit `e279d4262f50e73311d1e306c812efb7909fdf67`.
- Do not repeat C154 press-release/NSDP extraction; reopen only on an exact official Q2 BOP dataset locator or export/API contract.


## Continuation 224 — GIN BCRG attachment target route fingerprint
- Official 2026 archive entry and 22nd MPC article were reopened. Archive links to the article; article contains a “Télécharger” label but inspected content exposes no file URL, attachment name or payload. No guessed media/API route used.
- C170 remains controlling for Q2 BOP scope; no Q2 portfolio legs/raw bytes captured. GIN BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Matrix commit `0c4f29eebc6b508e7f17473a26f0c28f6bbd90be`; blob `d6b1986f1c029f0ea4b69dd77549e0b6cbd596b3`; C224 report commit `9415534d63c43c5d3d64acf3b225ad8fb0e7eb23`.
- Duplicate gate: do not repeat this article/archive inspection; reopen only on a distinct official attachment locator or data export/API.


## Continuation 225 — AZE CBAR external-sector route fingerprint
- Official route: CBAR External Sector Statistics index https://www.cbar.az/page-43/external-sector-statistics?language=en; 2026 section exposes eight publication entries; Interactive Statistic Database link routes to navigation.e-cbar.az but text retrieval returns an empty shell.
- Q2 bulletin Table 1.4 has asset/liability financial-account rows; portfolio remains combined with other investment (-302/+2,466 USDm). Not admissible as portfolio-only national legs. No raw detailed Q2 export captured.
- C225 report: `docs/GCR_AZERBAIJAN_AZE_Q2_2026_CBAR_EXTERNAL_SECTOR_INDEX_AND_Q2_COMBINED_CATEGORY_BOUNDARY_CONTINUATION225_20261121.md`; matrix commit `b85f7d9cfc927b7301bf91591ae0b004d54a0282`.
- Duplicate gate: do not repeat C146/C225 bulletin/index inspection; reopen only with distinct detailed Q2 portfolio-only export/API and revision metadata.


## Continuation 226 — BDI BRB June-2026 monthly indicators source fingerprint
- Official BRB index `https://www.brb.bi/indicateurs_de_conjoncture` lists a distinct June-2026 “Indicateur de conjoncture” PDF. The official 18-page PDF covers macro indicators, trade, FX, fiscal, monetary and banking statistics; it has no BOP section and no “Balance des paiements” text match.
- This is not the Q2 BOP report and contains no separate portfolio asset/liability transaction legs. No raw BOP data, Q2 portfolio values, revision metadata or hash captured.
- C155 historical dual-leg Q4/Q3-2025 reports and C207 matrix evidence correction remain controlling; no repeat of those tasks. BDI remains PARTIAL / NOT PASS; both legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.
- C226 detail: `docs/GCR_BURUNDI_BDI_Q2_2026_BRB_JUNE_2026_INDICATEURS_NON_BOP_SOURCE_BOUNDARY_CONTINUATION226_20261121.md`. Duplicate gate: do not repeat this monthly indicators PDF; reopen only on a distinct official Q2 BOP portfolio dual-leg export/API with revision metadata.


## Continuation 227 — MYS matrix evidence-reference read-back correction
- Existing controlling report `GCR_MALAYSIA_MYS_Q2_2026_BNM_OFFICIAL_FX_AND_DUAL_LEG_RECONCILIATION_20261120.md` already contains official BNM 1200-middle raw capture, separate asset/liability numeric checks and the unresolved same-vintage boundary.
- Corrected only the MYS matrix evidence_ref to that report; retained asset/liability PASS, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED. No numeric gate promotion.
- Matrix commit `7e544e73de2aac8c8f12d1e6e43391ae00ec3f05`; C227 report: `docs/GCR_MALAYSIA_MYS_Q2_2026_MATRIX_EVIDENCE_REFERENCE_READBACK_CORRECTION_CONTINUATION227_20261121.md`; queue appended under C227.
- Duplicate gate: do not repeat BNM FX raw capture, monthly/daily mean QA, IMF row extraction or dual-leg numeric comparisons. Reopen only on new dated BNM/DOSM revision-cutoff evidence or later archived IMF vintage.


## Continuation 228 — Run #339 raw-source artifact allowlist root cause
- Run #339 artifact 14660032260 independently downloaded and inspected: 17 entries; raw NSE CSVs, sessions, acquisition diagnostics, security master and manifest absent, despite job log/QA recording 200 raw files.
- Run #416 artifact 14632139339 also lacks original raw files/manifest; it contains normalized 200-session data and security master only.
- Exact defect: prospective workflow upload-artifact path allowlist omitted `data/raw/sec_bhavdata_full_*.csv`, sessions, acquisition diagnostics and security master. Corrected those paths on isolated audit branch; commit `46f4a359f21da676cb0c92e874fb08f14ee20d90`.
- Future-run artifact proof PENDING; per-file URL/retrieval-time/bytes/SHA manifest NOT_DONE; historical Run #339 raw recovery BLOCKED. Do not redownload or fabricate original provenance.
- Detail: `docs/NSE_RUN339_RAW_SOURCE_ARTIFACT_PACKAGING_ROOT_CAUSE_AND_RETENTION_FIX_CONTINUATION228_20261121.md`. Duplicate prevention: do not repeat artifact inventory/hash inspection absent a new artifact; next step is verify the next bounded workflow artifact and then implement acquisition-time manifest capture.

## Continuation 229 — CDSL archive capture fingerprint and duplicate-prevention update
| Country / stream | Exact route fingerprint | Evidence | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| India FPI / CDSL daily archive | https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx; GET; artifact 14527092174; capture 2026-11-19T11:57:09.076562Z; 73,784 bytes; displayed cutoff 02-Mar-2026 | docs/GCR_CDSL_DAILY_ARCHIVE_RAW_FRESHNESS_AND_ARITHMETIC_QA_CONTINUATION229_20261125.md; raw member SHA-256 aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df | Raw capture / displayed arithmetic PASS; archive freshness/completeness NOT PASS / UNKNOWN | Do not repeat same artifact parse/hash/arithmetic. Preserve C39 30-Sep, C68 31-Oct and C229 02-Mar snapshots as distinct HTTP-200 bodies; no canonical archive body inferred. | New official capture with reproducible date-specific query/export contract and matched NSDL/CDSL reporting semantics. |
- C229 arithmetic: daily/March/YTD 75/75 purchases-sales-net identities; cumulative 8/8; INR category subtotal 3/3 exact; USD daily/March -0.01 USDm residual retained as REVIEW.
- Next: NSDL Archive fresh-state interactive date selection and View Report once, only through supported browser interaction; no stale ViewState replay or guessed POST body. If unavailable, retain NOT_DONE.

## Continuation 230 — NSDL archival permission gate reconciliation (2026-11-25)
- C76/C229 public-form handoff is subordinate to the current Continuity Ledger's explicit NSDL FPI/DII archival BLOCKED-pending-written-permission gate. No written permission evidence was found; no postback attempted or authorized.
- NSDL rows NOT_CAPTURED; matched-date NSDL/CDSL reconciliation NOT_DONE. No guessed POST, stale ViewState, scraping or reverse engineering. Detail: docs/GCR_NSDL_ARCHIVAL_PERMISSION_GATE_RECONCILIATION_CONTINUATION230_20261125.md.
- Duplicate prevention: do not execute NSDL archival until written permission is evidenced. CHN/COL/POL existing blocked routes remain closed; proceed only with a genuinely new official route after exact route-history preflight. ₹0; UNKNOWN never PASS.


## Continuation 231 — RWA BNR WebDash route fingerprint and NPL handoff closure (2026-11-25)
| Country | Exact route fingerprint / prior evidence | C231 finding | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| NPL Nepal | NRB External Sector BPM6 XLSX + NSDP BOP SDMX; C58/C94/C130 | Current NSDP BOP SDMX link still resolves to stale NEPAL_BOP_2024_Q1.xml; known XLSX locator unchanged; no new official Q2 API/export | PARTIAL / BLOCKED | Keep both known routes closed; no repeated unsupported XLSX/XML requests | Distinct official Q2 BOP API/export or supported XLSX byte route with exact new locator |
| RWA Rwanda | BNR https://www.bnr.rw/esstatistics June-30-2026 JS portal item; new official subdomain https://webdash.bnr.rw/; C97/C130 | WebDash indexed BOP data is annual 2019–2023, combined portfolio row; no Q2-2026 separate legs or API/export contract. BNR June item URL unresolved; H1 net +14 USDm excluded | PARTIAL / NOT PASS; Q2 legs NOT_CAPTURED | Do not retry identical JS shell or treat annual/H1 net as Q2; preserve C231 route fingerprint | Exact BNR downloadable June-2026 Q2 BOP dataset/API exposing separate asset/liability transactions, metadata and vintage |

- RWA matrix evidence_ref/note now points to C231; all acceptance gates unchanged (BLOCKED; asset/liability NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED).
- Detail: docs/GCR_RWANDA_RWA_Q2_2026_BNR_WEB_DASH_ALTERNATE_ROUTE_BOUNDARY_CONTINUATION231_20261125.md. Next follow-up: SLB C132 unresolved official transaction-FX conversion-method boundary; do not use generic quarterly FX or infer conversion method. ₹0; UNKNOWN never PASS.


## Continuation 232 — SLB CBSI Q2 dataset locator and transaction-FX boundary (2026-11-25)
| Country | New official route / evidence | C232 finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| SLB Solomon Islands | CBSI BOP page https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments; linked Q2 workbook https://www.cbsi.com.sb/sites/default/files/2026-09/Balance-of-Payment-Statistics-2006-2026-Q2.xlsx; C99/C132 | Official page says BPM6, quarterly/annual, SB$ millions, latest 2026-Q2; XLSX URL resolves but raw byte retrieval fails (HTTP 400 unsupported XLSX MIME). Quarterly-average SBD/USD 8.08 is published, but CBSI does not say it is BOP transaction conversion rate. | PARTIAL / NOT PASS; transaction FX method NOT_ESTABLISHED; workbook bytes NOT_CAPTURED | Do not retry same XLSX through same unsupported path; reopen only on distinct supported raw-byte route or explicit CBSI BOP compilation methodology naming transaction conversion method |
- SLB matrix evidence_ref now points to C232; asset/liability REVIEW, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED unchanged.
- Detail: docs/GCR_SOLOMON_ISLANDS_SLB_Q2_2026_CBSI_OFFICIAL_DATASET_AND_TRANSACTION_FX_METHOD_BOUNDARY_CONTINUATION232_20261125.md. Next: SRB same-vintage/revision bridge; preflight C101/C103/C104/C109/C112 and do not repeat accepted monthly arithmetic/sign/FX work. ₹0; UNKNOWN never PASS.


## Continuation 233 — SRB route fingerprint / duplicate-prevention update (2026-11-25)
| Country | Route fingerprint / prior evidence | C233 finding | Status | Duplicate decision / reopen condition |
|---|---|---|---|---|
| SRB Serbia | NBS July 2026 Statistical Bulletin PDF candidate `https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf`; C107–C111; September-vintage C109 | Current official archive still exposes generic interactive Select/Input/Show controls; XLS link routes to general Statistics landing page. No new July PDF/workbook byte route or Table 2.3 header found. | PARTIAL / NOT PASS; July vintage NOT_VERIFIED; revision NOT_DONE; raw bytes/hash NOT_CAPTURED | Do not repeat known direct July PDF timeout or infer month from unheaded 3,932 row. Reopen only with supported browser DOM+download or a genuinely new official NBS byte route. |
- C233 report: ${reportPath}; report commit ${created.result.commit_sha}. Existing PASS arithmetic, sign/FX method, IMF semantics and September-vintage rows retained; no IMF re-query/cohort rebuild. ₹0; UNKNOWN never PASS.


## Continuation 234 — MNG official Open Data API route-contract fingerprint (2026-11-25)
| Country | New official source / route evidence | C234 finding | Status | Duplicate decision / reopen condition |
|---|---|---|---|---|
| MNG Mongolia | NSO Open Data documentation https://www.1212.mn/en/data-base/open-data; documented GET example under https://data.1212.mn/api/v1/; official BOP table DT_NSO_0100_001V10_quarter.px | GET route pattern, metadata response schema (title, variables/code/text/values/valueTexts), JSON/XML formats now officially documented. MNG table-specific metadata response not retrieved; 69 indicator codes and separate portfolio A/L remain NOT_CAPTURED/NOT_VERIFIED. | BLOCKED / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN | Do not repeat old C190/C179 endpoint attempts. Reopen only with supported GET client to fetch exact MNG table metadata; obey <=1 request/sec/IP; do not infer indicator codes. |
- Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_OFFICIAL_OPEN_DATA_API_DOCUMENTATION_AND_TABLE_ROUTE_BOUNDARY_CONTINUATION234_20261125.md; report commit fc9d3bfb4503c75e30341f90277823977a417d52. No matrix gate promotion, IMF re-query, cohort rebuild or production change. ₹0; UNKNOWN never PASS.

## Continuation 235 — MNG documented .px GET endpoint fingerprint (2026-11-25)
| Country | Exact route / source | C235 finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| MNG Mongolia | Official NSO Open Data GET route pattern; candidate https://data.1212.mn/api/v1/en/NSO/NSO__Economy,%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px; C179/C190/C221/C234 | One .px suffix route variant returned “URL not accessible” from current retrieval surface; no HTTP status/headers/body/bytes/hash; no indicator codes or Q2 national legs. | BLOCKED / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN | Do not repeat exact URL through same reader. Reopen only with genuinely different supported GET-capable client/browser or official downloadable Q2 export. |
- Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_DOCUMENTED_GET_METADATA_ENDPOINT_SUFFIX_TEST_CONTINUATION235_20261125.md; report commit 08c32ffc9d205e7141118a98c71c9637bcee1ee0. No IMF re-query/cohort rebuild, no matrix gate promotion, no production changes; ₹0; UNKNOWN never PASS.



## Continuation 236 — AGO BNA dissemination-calendar / public-access route fingerprint (2026-11-25)
| Country | New official evidence | C236 finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| AGO Angola | INE PASEN 2026 PDF https://ine.gov.ao/arquivos/geral/sen2026.pdf; IMF e-GDDS metadata https://dsbb.imf.org/e-gdds/dqaf-base/country/AGO/category/INR00; C142 | BNA Q2 BOP/IIP production is quarterly MBP6; public availability quarter n+1; BNA calendar says bimonthly website release after 60 days. Current IMF metadata says quarterly external-sector data are publicly posted simultaneously; this refines the earlier mailing-list-only reading. Q2 public release is confirmed but exposes only account-level totals, not portfolio A/L. No detailed attachment/API/schema or raw bytes/hash captured. | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat BNA SPA or guess API. Reopen only if supported official BNA public download/browser surface exposes detailed Q2 portfolio asset/liability rows with raw bytes, metadata and revision information. |
- C236 report: docs/GCR_ANGOLA_AGO_Q2_2026_BNA_DISSEMINATION_CALENDAR_AND_PUBLIC_ACCESS_BOUNDARY_RECONCILIATION_CONTINUATION236_20261125.md; commit 7aec846aef1f3a1079ad503215fba3579f72eeae.


## Continuation 237 — ALB official Q2 PDF dual-leg capture route fingerprint (2026-11-25)
| Country | New exact official route | C237 finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| ALB Albania | Bank of Albania Monthly Statistical Report 08/2026 PDF https://www.bankofalbania.org/rc/doc/RSM_gusht_2026_anglisht_35170.pdf; Table 2-1, Q2 2026 | Official quarterly BOP EURm table reports portfolio assets +156.25, liabilities +124.70, net +31.55; parent arithmetic exact. PDF text reader captured; raw bytes/response receipt/SHA-256 unavailable. Existing IMF raw legs reused; no FX conversion admitted. | DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW; liability REVIEW; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat C140/C141/C192 legacy Main-data route or identical PDF text retrieval. Reopen only for independently supported raw-byte capture, dated revision record, or explicit official transaction-FX bridge. |
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_MONTHLY_STATISTICAL_REPORT_OFFICIAL_DUAL_LEG_CAPTURE_CONTINUATION237_20261125.md; commit 214a86283beb2ecc1cca5dfabf7d39201ac748cd.


## Continuation 238 — ALB BoA flow FX convention / revision route fingerprint (2026-11-25)
| Country | New official evidence | Finding | Status / duplicate decision |
|---|---|---|---|
| ALB Albania | BoA June-2014 BPM6 commentary PDF; BoA monthly-average FX metadata; IMF BPM6 §§3.105–3.106 | Flow conversion convention = published average FX; stock = end-period. Monthly BoA rates to ALL are simple daily-rate averages. Exact Q2 portfolio transaction aggregation and same-vintage revision cutoff not established. | Keep numeric gates REVIEW, vintage UNKNOWN, aggregate NOT_AUTHORIZED. Do not repeat commentary PDF, C237 PDF, legacy Main-data routes or IMF query. Reopen only on distinct Q2 dated revision record, detailed FX compilation note or transaction-level official FX inputs. |
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_OFFICIAL_FLOW_FX_RULE_AND_REVISION_BOUNDARY_CONTINUATION238_20261125.md; commit 01d226cb0c6d751643e988ff6f5377600e87adc7.


## Continuation 239 — BGD Bangladesh official Q2 publication route fingerprint (2026-11-25)
| Country | New official route | Finding | Status / duplicate prevention |
|---|---|---|---|
| BGD Bangladesh | Bangladesh Bank Quarterly Vol XXIII No.4, Apr-Jun 2026; Annexure 1 Table V.1; https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol%20xxiii%2C%20no%204.pdf | Calendar Q2-2026 maps to FY26 Q4; USDm; portfolio investment appears net-only. No separate portfolio A/L rows. Other-investment/reserve rows are different instruments. FY26 provisional; no exact IMF vintage ID. | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Do not back-solve net or substitute other instruments. Reopen only on distinct official Q2 dual-leg export with revision metadata. |
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BB_Q4FY26_NET_ONLY_SOURCE_BOUNDARY_CONTINUATION239_20261125.md; report commit 68b6eb13da5ca33ba26f4f8d0ec5734f041642f3.


## Continuation 240 — TJK Tajikistan NBT workbook route fingerprint (2026-11-25)
| Country | Authority / exact route fingerprint | Prior evidence | Last known status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| TJK Tajikistan | National Bank of Tajikistan; https://www.nbt.tj/en/payments_balance/; 2026 Standard XLSX st_pr_2026_2.xlsx and Analytical XLSX an_pr_2026_2.xlsx | C240 official page and exact 2026 locators; document reader returned unsupported XLSX MIME / HTTP 400; direct standard XLSX byte download failed; no raw bytes/schema/Q2 legs | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Closed for same reader click and same direct download path; do not substitute IIP stock/operations, annual forecast or banking balance-sheet data | Distinct supported XLSX byte-transfer/browser route or new official NBT export with Q2 portfolio A/L and revision metadata |
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_OFFICIAL_STANDARD_BOP_XLSX_LOCATOR_AND_BYTE_ACCESS_BOUNDARY_CONTINUATION240_20261125.md; commit 35f0059e6d7a884db9f606d288c4d5919d0d1e85.


## Continuation 241 — MNE Montenegro CBCG PDF table-annotation route fingerprint (2026-11-25)
| Country | Authority / exact route fingerprint | New finding | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| MNE Montenegro | CBCG Bulletin archive https://www.cbcg.me/en/publications/regular-publications/cbcg-bulletin → Bulletin 9/2026 PDF https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf → BoP printed p.55 / PDF p.54, “Tables 5.1–5.4 - download tables” | Document reader exposes label and BPM6 quarterly EUR methodology but not the PDF annotation target/direct export URL. Same PDF byte download failed; no table bytes, Q2 portfolio legs, headers or hash. Preliminary/revisable warning retained. | PARTIAL / NOT PASS; Q2 A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Close identical PDF text-reader and byte-download routes; keep C180 ZIP and NSDP XML/Browse routes closed | Supported PDF annotation/link extraction or distinct official CBCG export page/API yielding Tables 5.1–5.4 payload and revision metadata |

- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_ANNOTATION_ACCESS_BOUNDARY_CONTINUATION241_20261125.md; report commit c7eb31705caef3183f90a848a08551210026402a. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 242 — PRY Paraguay BCP Statistical Annex route fingerprint (2026-11-25)
| Country | Authority / exact route fingerprint | New finding | Status | Duplicate decision | Reopen only if |
|---|---|---|---|---|---|
| PRY Paraguay | BCP Statistical Annex page https://www.bcp.gov.py/en/web/institucional/anexo-estadistico- → current XLSX https://www.bcp.gov.py/documents/20117/213069/Anexo_Estad%C3%ADstico_del_Informe_Econ%C3%B3mico_23_11_2026.xlsx/1fc7fda2-74cf-e07c-be5b-535f02a89ba3?t=1795456089070 | Distinct periodically updated official annex is described as including BOP statistics. XLSX reader rejects MIME (400); direct byte download failed. No bytes/sheets/Q2 scope/A-L/vintage/hash. BOP page says quarterly/annual dissemination with 3-month lag; next quarterly calendar date 30-Dec-2026. | PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat C60 Q2-specific workbook or identical annex reader/download attempts | Distinct supported XLSX-capable byte route or official API/export exposing Q2 portfolio transaction legs and revision metadata |

- Detail: docs/GCR_PARAGUAY_PRY_Q2_2026_BCP_STATISTICAL_ANNEX_ALTERNATE_EXPORT_ACCESS_BOUNDARY_CONTINUATION242_20261125.md; report commit ec6e16fb0507a278cf1cc23e6c98548596cc81a5. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 243 — WSM Samoa official CBS index release-status recheck (2026-11-25)
| Country | Authority / route fingerprint | New finding | Status | Duplicate decision / reopen only if |
|---|---|---|---|---|
| WSM Samoa | CBS official Quarterly Bulletin index https://cbs.gov.ws/quarterly-bulletin; controlling C125/C126 | Directly opened index still lists June 2026 as latest and footer says last updated 18-Aug-2026. Search-index snippet naming September 2026 conflicts with direct page and is unconfirmed. June issue is Q1/2026, ending 2026-I; Q2-II legs not captured. | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat June 2026 PDF extraction. Reopen only when the direct official CBS index lists a later issue or a distinct official Q2-2026 BOP table file is published; inspect internal reporting period before extracting. |
- Detail: docs/GCR_SAMOA_WSM_Q2_2026_CBS_OFFICIAL_INDEX_RELEASE_STATUS_RECHECK_CONTINUATION243_20261125.md; commit 3fe2ccb003850611f6a9e7b4def92e04d13c79e9. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 244 — MEX Banxico Q3 scheduled release / Q2 vintage gate (2026-11-25)
| Country | Authority / route fingerprint | New finding | Status | Duplicate prevention / reopen only if |
|---|---|---|---|---|
| MEX Mexico | Banxico BOP publication page https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/balanza-pagos-comercio-invers.html; November dissemination calendar https://www.banxico.org.mx/viewers2/JSP/calendarioDifusion_es.jsp; controlling C137/C208 | Q2 assets/liabilities numeric comparisons already PASS at ±USD0.5m; vintage remains open. Official indexed calendar scheduled Q3 BOP for 25-Nov-2026 09:00 Mexico City; at 19:10 IST (07:40 Mexico City) the time had not arrived. No Q3 release or revised Q2 legs captured. | DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat Q2 PDF/SIE or IMF extraction. Reopen after scheduled time only if official Q3 release is posted; inspect Q2 revisions and explicit vintage bridge. No release date alone as vintage proof. |
- Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_SCHEDULE_AND_VINTAGE_GATE_PRECHECK_CONTINUATION244_20261125.md; commit 86196e69abcd73f494e19e3ec2519e112f50e0d7.


## Continuation 245 — UZB Uzbekistan CBU Q2 latest-vintage / release-calendar boundary (2026-11-25)
| Country | Authority / route fingerprint | New finding | Status | Duplicate prevention / reopen only if |
|---|---|---|---|---|
| UZB Uzbekistan | CBU standard BOP dataset https://cbu.uz/en/statistics/bop/4616923/; e-GDDS BOP locator https://cbu.uz/en/statistics/e-gdds/data/127982/?mobile=Y; official release calendar https://cbu.uz/en/statistics/calendar/; H1 review https://cbu.uz/en/press_center/releases/4616748/ | Q2 dataset indexed update 29-Sep-2026; Q2 latest. Release calendar Q2 BOP 30-Sep, Q3 BOP 31-Dec. H1-2026 review has net portfolio inflows ~USD2bn, not separate Q2 A/L. H1 statistical bulletin XLSX search-index lead on 24-Nov could not be opened from stale dynamic page; no bytes/headers/hash. “million USD, end of period” time basis unresolved; same-vintage not established. | DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat C123 numeric comparison, IMF panel retrieval or same failed XLSX route. Reopen only with byte-preserving H1 bulletin/Q2 workbook capture plus workbook headers and revision metadata. |
- Detail: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_LATEST_VINTAGE_AND_RELEASE_CALENDAR_BOUNDARY_CONTINUATION245_20261125.md; report commit 5a4efbb7d5608682b482419d48e18070826ca6e9. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 245 — URY Uruguay BCU Q2 preliminary status / Q3 vintage release gate (2026-11-25)
| Country | Official route / new finding | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| URY Uruguay | BCU Q2-2026 BOP/IIP report https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf; official calendar https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Default.aspx | Q2 report still marks figures preliminary; Table 9 is sector-level portfolio transaction flow. Calendar schedules Q3-2026 Cuentas Internacionales for 30-Dec-2026. No observation-specific Q2 revision ID/timestamp or BCU↔IMF vintage bridge found. Existing numeric dual-leg PASS reused; no new calculation. | DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat prior Table 9 extraction or dual-leg arithmetic. Reopen after 30-Dec Q3 release only to inspect Q2 revised legs and explicit vintage bridge. |
- Detail: docs/GCR_URUGUAY_URY_Q2_2026_BCU_PRELIMINARY_STATUS_AND_Q3_RELEASE_VINTAGE_GATE_CONTINUATION245_20261125.md. Sources turn142592view0 / turn795836view0 / turn874156search0 / turn874156search4. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 246 — MEX Banxico Q3 post-release Q2 portfolio vintage recheck (2026-11-25)
| Country | New official route / fingerprint | Finding | Status | Duplicate prevention / reopen condition |
|---|---|---|---|---|
| MEX Mexico | Banxico BOP publication index; Q3-2026 PDF dated 25-Nov-2026: https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/%7BFE2A999A-C9E0-98B0-F65D-01340BA453AC%7D.pdf | Q2 portfolio assets USD 9,480m; liabilities USD 10,561m; net -1,082m. Release footnote identifies principal revisions in profits/dividends, direct investment and services, not portfolio-specific revision identity. No observation-specific revision timestamp/version bridge; raw PDF bytes/hash not captured. | DATA_CAPTURED; existing asset/liability PASS reused; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat the same Q3 PDF extraction. Reopen only to compare exact Q2 portfolio rows against 25-Aug first release and obtain explicit revision/vintage metadata. No IMF re-query/cohort rebuild. |
- Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_POSTPUBLICATION_VINTAGE_RECHECK_CONTINUATION246_20261125.md. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 247 — CHN China SAFE Q2 source / sign-vintage audit (2026-11-25)
| Country | Official source and new evidence | Status | Reopen only if |
|---|---|---|---|
| CHN China | SAFE Q2 2026 release 29-Sep, index 000014453-2026-0068, https://www.safe.gov.cn/en/2026/0929/2458.html; archived IMF CHN exact-sample A/L CSVs | SAFE portfolio assets -USD48.8bn and liabilities +USD43.3bn (rounded); archived IMF A +USD48.794459bn, L +USD43.286601bn. Asset sign mapping unresolved; rounded USD100m table cannot test ±USD0.5m. Q3 13-Nov standalone lacks portfolio row; cumulative table not back-solved. Detailed XLSX bytes/schema/hash/vintage bridge NOT_CAPTURED. | DATA_CAPTURED; asset REVIEW; liability PASS retained only from prior matrix; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED | Distinct supported official SAFE XLSX route or unrounded official machine-readable A/L + sign definitions + revision/vintage metadata. Do not repeat failed route or IMF query. |
- Report: docs/GCR_CHN_C247_STATUS_20261125.md. ₹0; fixed cohort; UNKNOWN never PASS.


## Continuation 248 — COL Colombia official portfolio-series scope / alternate-route boundary (2026-11-26)
| Country | Official route / new evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| COL Colombia | BanRep SUAMECA official catalogue; quarterly national BOP portfolio net acquisition of financial assets and net incurrence of liabilities, current USDm, Q2-2026 coverage. Separate monthly “Flujo de inversión extranjera de cartera en el mercado local colombiano” also appears in catalogue. | Quarterly BOP A/L series identity/coverage PASS at metadata scope only; exact series IDs, Q2 observations, export bytes/hash, sign crosswalk and vintage NOT_CAPTURED/NOT_ESTABLISHED. Monthly local-market series is NOT_EQUIVALENT and NOT_ADMITTED. COL BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. | Do not repeat C162 SUAMECA 502, dashboard timeout, C152 desktop-procedure review or SDMX route (BOP excluded by guide). Reopen only with a genuinely distinct official export/API or supported desktop basket/export yielding both quarterly Q2 legs and metadata. |
- Detail: docs/GCR_COLOMBIA_COL_Q2_2026_OFFICIAL_PORTFOLIO_SERIES_SCOPE_AND_ALTERNATE_ROUTE_AUDIT_CONTINUATION248_20261126.md; report commit a1206349a0ae0285e97b5e406fdbfc05651296b2. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 249 — POL Poland NBP v2.1 publication / latest vintage route fingerprint (2026-11-26)
| Country | New official evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| POL Poland | NBP public reporting list shows explanatory-notes v2.1 dated 13-Jul-2026; retrievable v2.0 notes specify transaction-date/prior-day rate and four-decimal conversion precision; latest 13-Nov monthly BOP release is preliminary September data | Existing Q2 legs remain 24,144 mn PLN assets / 70,910 mn PLN liabilities PASS; no matched USD Q2 dual-leg values, transaction-level FX weights or observation-specific vintage bridge; POL PARTIAL / NOT PASS | Do not infer v2.1 contents from listing metadata, repeat NBP PDF/XLSX downloads, use quarter-end/average FX or re-query IMF. Reopen only if v2.1 bytes/new conversion metadata, matched official Q2 USD dual legs, or transaction-level dated currency/amount source with vintage becomes available |
- Report: docs/GCR_POLAND_POL_Q2_2026_NBP_VERSION21_PUBLICATION_AND_LATEST_VINTAGE_BOUNDARY_RECHECK_CONTINUATION249_20261126.md; commit 37573606aa47bb1fa65a14ddbf66032088e98e42. Next candidate MNE; exact CBCG table export route only.

## Continuation 250 — MNE Montenegro official CBCG BPM6 data-page route fingerprint (2026-11-26)
| Country | New official source route | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| MNE Montenegro | CBCG BOP statistics page updated 19-Nov-2026; BPM6 (2010–2026) official download link resolves to https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip; page states quarterly EUR BPM6 and net-acquisition/net-incurrence financial-account presentation | Locator PASS only; ZIP transfer unsupported in web reader and direct download failed; no bytes/hash/Q2 separate A/L legs/signs/vintage; MNE BLOCKED / PARTIAL / NOT PASS | Do not repeat C241 Bulletin PDF reader/byte attempt, old CBCG ZIP or MONSTAT NSDP XML/Browse. Reopen only if supported official ZIP retrieval or distinct CBCG endpoint supplies bytes and Q2 portfolio legs |
- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_OFFICIAL_BPM6_DOWNLOAD_ROUTE_FINGERPRINT_CONTINUATION250_20261126.md; commit 0026acf7352ff6711b31b292fe2ab41963aad04c. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.

## Continuation 251 — ALB Albania official USD archive Q2-2026 eligibility route fingerprint (2026-11-26)
| Country | New official evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| ALB Albania | BoA archive navigation exposes quarterly USD BOP and Financial Account series; legacy USD BOP child selector ends Q4-2013 and carries 11-Sep-2017 revision note; new-format USD Financial Account page shows A/L portfolio taxonomy but no Q2-2026 values and same 2017 revision note | Route discovery PASS; archive Q2-2026 ineligible; Q2 EUR→USD conversion and vintage unresolved; ALB PARTIAL / NOT PASS | Do not repeat legacy USD child URLs absent new official 2026 observations, a dated revision record or supported current export with Q2 USD portfolio dual legs |
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_LEGACY_USD_ARCHIVE_Q2_ELIGIBILITY_AND_VINTAGE_BOUNDARY_CONTINUATION251_20261126.md; commit 9835344450ed796d63bbaedbf633fb3bcc531296.

## Continuation 252 — HUN Hungary MNB monthly BOP calendar / vintage trigger (2026-11-26)
| Country | New official evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| HUN Hungary | MNB calendar lists 13-Nov-2026 monthly BOP for September 2026; MNB homepage BOP/IIP latest remains Q2-2026 updated 25-Sep; no monthly portfolio A/L values or Q2 revision/vintage ID exposed | Existing C138 Q2 legs remain DATA_CAPTURED; cross-currency comparison NOT_DONE; vintage NOT_ESTABLISHED; PARTIAL / NOT PASS | Do not repeat C138 PDF/IMF or C139 monthly-data route. Reopen only on distinct monthly portfolio A/L dataset, Q2 revision artifact or Q3 BOP/IIP report with portfolio legs and revision metadata |
- Detail: docs/GCR_HUNGARY_HUN_Q2_2026_MNB_POST_C138_RELEASE_CALENDAR_AND_MONTHLY_BOP_VINTAGE_TRIGGER_RECHECK_CONTINUATION252_20261126.md; commit 8af5f5c0e9197078651f219b6aa14c058f60b89b.

## Continuation 253 — CHL Chile BCCh Q3-2026 Q2 revision / portfolio-vintage trigger (2026-11-26)
| Country | New official evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| CHL Chile | BCCh Q3 report dated 18-Nov says Q1/Q2 BOP revised; Q2 portfolio net is USD +154m vs +299m in prior Q2 release (-USD145m). Revision table's Q2 asset/liability totals are whole financial-account aggregates, not portfolio-only legs. | Existing BDE A/L observations retained as earlier-vintage source-page evidence; current-vintage portfolio A/L NOT_CAPTURED; vintage PENDING; CHL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED | Do not repeat C160 BDE extraction or C161 credential-gated API request. Reopen only with executed authorized public BDE Excel export or distinct official export exposing both revised Q2 portfolio legs, update/vintage metadata and raw bytes/hash; never infer legs from net/aggregate totals |
- Detail: docs/GCR_CHILE_CHL_Q2_2026_BCCH_Q3_RELEASE_PORTFOLIO_NET_REVISION_AND_VINTAGE_BOUNDARY_CONTINUATION253_20261126.md; report commit 02c7ff97ea91d09423ec1a30c9e589aa016a3ec2.


## Continuation 254 — MEX Mexico later IMF archive inventory / revision-vintage gate (2026-11-26)
| Country | New audit evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| MEX Mexico | Inspected 19-Nov IMF panel report, exact-sample JSON receipt and both raw CSVs; bounded GitHub/Library search located no later MEX exact-key IMF snapshot. Exact MEX receipt remains 19-Nov-2026 06:45:19 UTC. | C246 Banxico Q3 shows Q2 assets +543m revision; liabilities unchanged. Existing archived IMF rows match the earlier release, not latest asset value. Asset REVIEW; liability PASS; vintage PENDING; MEX PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. | Do not re-query IMF or repeat Banxico Q3/first-release comparison. Reopen only on later archived IMF raw receipt with timestamp/hash or Banxico observation-specific Q2 revision/version bridge. |
- Detail: docs/GCR_MEXICO_MEX_Q2_2026_IMF_LATER_ARCHIVE_INVENTORY_AND_VINTAGE_BRIDGE_BOUNDARY_CONTINUATION254_20261126.md; commit ab937972f13098af06f4a25e35e47f0f7d3f35a0.


## Continuation 255 — ZAF South Africa SARB EXCX135D Q2 historical coverage boundary (2026-11-26)
| Country | New official evidence | Status | Duplicate decision / reopen only if |
|---|---|---|---|
| ZAF South Africa | SARB OpenAPI confirms EXCX135D Rand per US Dollar, daily bank-weighted rate around 10:30am. No-date endpoint response exposes 24 visible rows, only 3 Q2 dates (1, 2, 7-Apr); date-bounded Q2 endpoint inaccessible through current retrieval channel; no May/June, raw Q2 bytes/hash or SARB BOP conversion rule captured. | Existing liability PASS retained; asset REVIEW; Q2 daily FX coverage NOT_CAPTURED; BOP FX convention NOT_ESTABLISHED; vintage PENDING; ZAF PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED | Do not repeat no-date 24-row response, date-format guesses, IMF fetch, SARB PDF extraction or OECD quarterly-average arithmetic. Reopen only with complete official Q2 daily export plus raw provenance and SARB-specific BOP conversion method |
- Detail: docs/GCR_SOUTH_AFRICA_ZAF_Q2_2026_SARB_EXCX135D_DAILY_SERIES_Q2_COVERAGE_AND_HISTORICAL_ENDPOINT_ACCESS_BOUNDARY_CONTINUATION255_20261126.md; report commit 81d155fe62f823d317c6d678f2f3bead446efd8e.


## Continuation 256 — CPV Cabo Verde BCV updated BOP statistical-table locator fingerprint (2026-11-26)
| Country | Authority / route fingerprint | New finding | Status | Duplicate prevention / reopen only if |
|---|---|---|---|---|
| CPV Cabo Verde | BCV official BOP statistical page https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Paginas/BalancadePagamentos.aspx; page indexed 17-Nov-2026; “Balança de Pagamentos” XLS covering Q1-2012–Q2-2026 | New page-level locator found; actual attachment href/filename/MIME/bytes and workbook schema not exposed; page retrieval cache miss/timeout. No Q2 portfolio A/L cells or raw hash. C213 BPM6 methodology reused. | SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED | Do not repeat old C153 XLS/XLSX route unless actual href proves a distinct attachment and supported byte-transfer path. Reopen only with exact XLS href, raw bytes/hash and workbook A/L/vintage evidence. |
- Detail: docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_UPDATED_BOP_STATISTICAL_TABLE_LOCATOR_AND_XLS_ACCESS_BOUNDARY_CONTINUATION256_20261126.md; report commit 47c8575c83f201653b7da3be67288547fa1d3e27. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 257 — UKR Ukraine NBU IIP transaction-to-BOP methodology route fingerprint (2026-11-26)
| Country | Authority / route fingerprint | New evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|---|
| UKR Ukraine | NBU official BPM6 methodology https://p4.bank.gov.ua/admin_uploads/article/BoP_methodological_notes_en.pdf; IIP integrated statement; transaction column and financial-component row structure | Methodology states IIP data sources are same as BOP financial-account sources; component rows correspond to BOP financial-account structure; transaction column represents financial-account transactions, with valuation/FX/other changes separate. C134 Q2 legs +159/+34 USDm and numeric checks reused. | Asset PASS; liability PASS; semantic bridge PASS; vintage PENDING / NOT_ESTABLISHED; FULL_PASS NO; aggregate NOT_AUTHORIZED | Do not repeat C134 numeric extraction or stale BOP PDF. Reopen only on Q2-specific official revision/version metadata or a later release explicitly bridging Q2 observations to IMF vintage. |
- Detail: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_IIP_TRANSACTION_TO_BOP_FINANCIAL_ACCOUNT_METHOD_BRIDGE_CONTINUATION257_20261126.md; commit 36b77c6e189a53d1616a236a8aef49e5c2a467b3. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 258 — UKR Ukraine official Q2 revision-vintage recheck (2026-11-26)
| Country | New official evidence / route check | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| UKR Ukraine | Current NBU Q2 IIP PDF remains last updated 23-Sep-2026; visible revision note concerns 2022–2025 FDI/trade-credit/currency-deposit assets, not Q2 portfolio A/L. NBU revision notice and external-sector page returned 403 in this retrieval channel; bounded official-domain search found no new Q2-specific revision/version ID. | Asset PASS; liability PASS; semantic bridge PASS; vintage PENDING / NOT_ESTABLISHED; FULL_PASS NO; aggregate NOT_AUTHORIZED. | Do not repeat C134 IIP extraction, C257 methodology bridge, stale BOP PDF or IMF query. Reopen only with new official Q2-specific revision/version metadata or later official release explicitly identifying Q2 portfolio A/L revision and observation vintage. |
- Detail: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_OFFICIAL_REVISION_VINTAGE_RECHECK_CONTINUATION258_20261126.md; report commit 77eeab7e188bbda9e110c7f8ae18b7c308805b6a. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 259 — MNE Montenegro CBCG Bulletin 10/2026 annotation route fingerprint (2026-11-26)
| Country | New official route / evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| MNE Montenegro | Distinct CBCG Bulletin 10/2026 PDF opened; printed p.55 shows Tables 5.1–5.4 download anchor, but annotation target not exposed. PDF says data are preliminary; methodology confirms BPM6 quarterly EUR and transaction-day/monthly-average/period-end FX conventions. Current BOP statistics page resolves to the exact C250 `bop_sep_2026.zip` URL. | Source/methodology metadata PASS only; attachment URL/bytes, Q2 portfolio A/L, raw hash and observation vintage NOT_CAPTURED; BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. | Do not repeat C241 Bulletin 9 PDF/byte attempt or C250 exact ZIP route. Reopen only with supported annotation-target extraction or genuinely distinct official raw table export/API with Q2 A/L and vintage metadata. |
- Detail: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_10_2026_TABLE_ANNOTATION_AND_PRELIMINARY_VINTAGE_BOUNDARY_CONTINUATION259_20261126.md; report commit 63dc9b93dccc553e8e0f77cfe0ee72fafef1f88c. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.

- C259 matrix evidence-link reconciliation: MNE row evidence_ref now points to C259; exact 30-column width preserved; no gate changed. Matrix commit 627add7c79f92effc7f5a21b4d9e64cdab53564d; blob 7ba199d908e441b0e3bc39cd8a35822d23576e4d.


## Continuation 260 — CPV Cabo Verde exact XLS attachment route fingerprint (2026-11-26)
| Country | Official route / exact identity | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| CPV Cabo Verde | Current BCV BOP statistical page link resolves to the exact C153 XLS URL: `https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Documents/2026/Setembro/Balan%C3%A7a%20de%20Pagamentos%20%28Estat%C3%ADsticas%20do%201%C2%BA%20trimestre%20de%202012%20a%202%C2%BA%20trimestre%20de%202026%29.xls`. Reader 400 unsupported application/vnd.ms-excel. | Exact attachment identity PASS; raw bytes/sheets/Q2 A/L/hash/vintage NOT_CAPTURED; CPV SOURCE_FOUND / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. | CLOSED as duplicate of C153. Do not repeat same browser click or direct-byte route. Reopen only on genuinely distinct official BCV API/export/file revision or supported byte-transfer route not used in C153. |
- Detail: docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_EXACT_XLS_ATTACHMENT_DUPLICATE_ROUTE_CLOSURE_CONTINUATION260_20261126.md; report commit 44c6004361efc7a7fd28e2f28ff7c6eab5cc9603. Matrix evidence_ref linked to C260; all gate states unchanged. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## Continuation 261 — GEO Georgia NBG Q3-2026 release-calendar / revision-trigger recheck (2026-11-26)
| Country | New official evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| GEO Georgia | NBG Advance Release Calendar currently lists Balance of Payments `30 Q3/2026` in the November-2026 column; date is 30-Nov-2026, still future on 26-Nov. NBG Data Revision Policy confirms preliminary data are regularly revised upon next-period release and extraordinary revisions can be notified publicly. | Calendar/revision-policy evidence PASS; Q2 portfolio A/L NOT_CAPTURED; BPM5/BPM6 conflict unresolved; vintage UNKNOWN; GEO SOURCE_FOUND / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. | Do not repeat C154 Q2 release text, C223 Statistics Data shell, or stale NSDP Q3/21. Reopen after 30-Nov only if the Q3 release is actually available and exposes Q2 separate portfolio A/L revision values and methodology/vintage evidence. |
- Detail: `docs/GCR_GEORGIA_GEO_Q2_2026_NBG_Q3_RELEASE_CALENDAR_AND_REVISION_TRIGGER_RECHECK_CONTINUATION261_20261126.md`; report commit `5f37661b9378a46518356dff8a14d3da2f28b9ac`. Matrix evidence_ref linked to C261; all gate columns unchanged. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## Continuation 262 — WSM Samoa September 2026 bulletin dual-leg route (2026-11-26)
| Country | New official source / period | Result | Duplicate prevention / remaining gates |
|---|---|---|---|
| WSM Samoa | CBS Quarterly Bulletin index directly lists September 2026 (updated 19-Nov); official PDF `https://cbs.gov.ws/media/Quarterly-Bulletin---September-2026.pdf`; Table B-1, printed p.35/PDF p.38, 2026-II/Q2, Tala million, BPM6. | Portfolio assets +9.5; liabilities +0.2; net +9.3; internal arithmetic consistent. National dual legs CAPTURED; WSM DATA_CAPTURED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. | Do not repeat C125/C126 June-issue extraction or C243 stale-index check. PDF raw bytes/hash unavailable; USD FX bridge and same-vintage link unresolved. Reopen only for supported byte route/hash and official conversion/vintage metadata. |
- Detail: `docs/GCR_SAMOA_WSM_Q2_2026_CBS_SEPTEMBER_2026_BULLETIN_TABLE_B1_DUAL_LEG_CAPTURE_CONTINUATION262_20261126.md`; report commit `9844972ddad36175a2c392bf87d1f165e97759e4`; matrix commit `cc12d52820b6ca2a4f6cf117b78375c564ccde58`. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 263 — SRB Serbia September 2026 Bulletin Table 2.3 route and capture (2026-11-26)
| Country | New official route / evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| SRB Serbia | Distinct NBS September 2026 Statistical Bulletin PDF, Table 2.3, BPM6, preliminary EURm; Q2 monthly legs Apr/May/Jun assets +149/−25/+124; liabilities −19/+3,932/+199; net +168/−3,957/−75. Q2 sums +248/+4,112/−3,864 EURm. | National dual legs CAPTURED; quarterly arithmetic PASS; EUR/USD transaction comparison REVIEW; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. | Do not repeat C233 July PDF/XLS route. Reopen only for official NBS transaction-period EUR/USD conversion methodology, observation-specific Q2 revision/version bridge, or later official corrected Table 2.3. |
- Detail: `docs/GCR_SERBIA_SRB_Q2_2026_NBS_SEPTEMBER_2026_BULLETIN_TABLE_2_3_MONTHLY_DUAL_LEG_CAPTURE_CONTINUATION263_20261126.md`; report commit 49f163b8b8a8477240060fc2b16f255314eda935; matrix commit 3dcc6132e83dbd8986796212bea09c3350f6fb81. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 264 — CHN China SAFE Q3 post-publication recheck (2026-11-26)
| Country | New official evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| CHN China | Inspected SAFE official Q3 preliminary BOP release (13-Nov-2026): Q3 and first-three-quarters aggregates, but no distinct revised Q2 portfolio A/L pair in inspected release. Reused SAFE Q2 29-Sep rounded table and archived IMF exact-key rows. | Asset sign REVIEW / NOT ESTABLISHED; liability numeric PASS retained; vintage PENDING; detailed XLSX/raw hash NOT_CAPTURED; DATA_CAPTURED / PARTIAL / NOT PASS; FULL_PASS NO; aggregate NOT_AUTHORIZED. | Do not repeat Q2/Q3 page checks, failed XLSX route or IMF query. Reopen only on distinct supported SAFE Q2 detailed export with unrounded A/L, explicit sign definitions, observation-specific vintage/revision metadata and raw bytes/hash. |
- Detail: docs/GCR_CHINA_CHN_Q2_2026_SAFE_POSTPUBLICATION_Q3_REVISION_AND_SIGN_VINTAGE_RECHECK_CONTINUATION264_20261126.md; report commit 264e9044d0e9328056feda3fd98c8f1e91b8c754. ₹0; no cohort rebuild; UNKNOWN never PASS.


## Continuation 265 — SRB Serbia NBS transaction-date FX / sign methodology (2026-11-26)
| Country | New official evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| SRB Serbia | NBS BPM6 Explanatory Notes: EURm/USDm dissemination; official NBS middle exchange rate on transaction date; assets/liabilities increase positive, decrease negative; net=assets−liabilities. Current official monthly and detailed XLS URLs found but reader returned HTTP 400 unsupported Excel MIME. NBS 18-Nov Jan–Sep report has portfolio net cumulative EUR4.4bn only. | Methodology/sign semantics PASS (scope only); C263 EUR legs retained; USD Q2 A/L NOT_CAPTURED; numeric comparison REVIEW; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. | Do not use quarter-average FX or cumulative net back-solving. Reopen only on supported official USD Q2 workbook/transaction-level source and Q2-specific revision/vintage metadata. |
- Detail: `docs/GCR_SERBIA_SRB_Q2_2026_NBS_TRANSACTION_DATE_FX_AND_SIGN_METHODOLOGY_VINTAGE_BOUNDARY_CONTINUATION265_20261126.md`; report commit `9bc2128c3a56cecf749d8a18b02f4e22197a3ed5`. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## Continuation 266 — TZA Tanzania Bank of Tanzania Q2-2026 portfolio net-only boundary (2026-11-26)
| Country | Official evidence | Status | Duplicate prevention / reopen only if |
|---|---|---|---|
| TZA Tanzania | Bank of Tanzania September-2026 Statistical Bulletin, Table 6.1, Quarterly BOP, USDm: Q2-2026 Portfolio investment net -14.0. No separate portfolio assets/liabilities. Adjacent A/L subrows are under Other Investment. | Net-only observation captured; separate portfolio A/L NOT_CAPTURED; TZA SOURCE_FOUND / PARTIAL / NOT PASS; vintage UNKNOWN; aggregate NOT_AUTHORIZED. | Do not use net as a leg or reclassify Other Investment A/L. Reopen only on distinct official Q2 portfolio A/L table/export with sign/unit/vintage metadata. |
- Detail: docs/GCR_TANZANIA_TZA_Q2_2026_BOT_SEPTEMBER_2026_STATISTICAL_BULLETIN_PORTFOLIO_NET_ONLY_BOUNDARY_CONTINUATION266_20261126.md; commit e7ee982ada8a6b2624028e2aef466ed51f310765. No IMF re-query/cohort rebuild; ₹0; UNKNOWN never PASS.


## Continuation 267 — GCR progress denominator reconciliation (2026-11-26)
| Measure | Current defensible interpretation | Value |
|---|---|---|
| Historical Overlay V1 milestone checkpoint | 5 of 8 milestones at the historical checkpoint; not full-project weighted completion | 62.5% historical |
| Q2-2026 63-country national-source capture | DATA_CAPTURED rows / fixed 63-country cohort | 29/63 = 46.03% |
| Overall GCR completion | Eight milestones and dependent hard gates not fully re-audited under one explicit scoring scheme | NOT_COMPUTABLE / NOT_CERTIFIED |
- Latest Mother File addenda 55–57 show Macro-Geo P0 6/8 and strict hard gate BLOCKED. Do not conflate denominators. C267 report docs/GCR_PROGRESS_BASELINE_RECONCILIATION_8_MILESTONE_VS_63_COUNTRY_CAPTURE_CONTINUATION267_20261126.md; commit bfcaef37166002e34614d0bc8caaea4119136368.


## GCR Continuation 268 — FBIL USD/INR public archive/export access boundary (26-Nov-2026)
- Re-read current Ledger, Priority Queue, Historical Registry, fixed 63-country matrix, C267 progress-baseline report and Library Mother File addenda 55–57. Selected unfinished Milestone 6 (Global Macro Data Ingestion); no repeat of prior RBI form/NSDL terms route attempts, IMF query or cohort rebuild.
- Fresh official FBIL homepage inspection confirms publicly rendered INR/1 USD reference-rate rows, but no documented complete historical daily export/API, schema, full date coverage, raw bytes or SHA-256 was exposed. Homepage displays a Terms of Use and Subscription Disclaimer notice; actual reuse/archival permission was not established.
- FBIL official 11-Jun-2018 methodology: actual spot USD/INR transactions during 11:30–12:30 Mumbai window; random 15-minute sample, >=10 transactions and USD25m threshold, +/-3SD filter, volume-weighted average; fallback polled quotes; published around 13:30 on Mumbai business days. This is benchmark data, not OHLC/DXY/carry.
- NSE/SEBI data-sharing list identifies FII/FPI & DII exchange trading activity as first-basket research data; separate NSE research page states research access is restricted to accredited academic institutions/recognized research organizations/think tanks and non-commercial research. No project eligibility assumed; do not substitute provisional exchange activity for final depository FPI.
- USD/INR remains BLOCKED/UNKNOWN; no raw daily archive or terms clearance; no collector code, workflow, or source-coverage change. Detail: docs/GCR_FBIL_USDINR_PUBLIC_REFERENCE_RATE_ARCHIVE_EXPORT_ACCESS_BOUNDARY_CONTINUATION268_20261126.md; report commit 6ebf881cd6bf72b503406c92e31612d8b566a989. ₹0; UNKNOWN never PASS; production unchanged.


## Continuation 269 — Milestone 6 next-action precondition / duplicate prevention (26-Nov-2026)
| Work item | Current evidence | Status | Reopen only if |
|---|---|---|---|
| FBIL USD/INR | C268 public rows only; complete historical export/API, schema, raw bytes/hash and reuse permission absent. | BLOCKED / UNKNOWN | Distinct documented official export/API plus terms clearance and raw observations. |
| H.10/FRED INR | Historical source, unit/base, equivalence and byte-route audits already exist; NY noon buying rate is not FBIL benchmark. | Existing audit retained; no repeat or silent substitution. | Explicit separate source-definition decision and fresh permitted evidence. |
| NSDL/CDSL FPI/DII | Daily routes identified; permitted export/schema and >=60-date/90-day coverage remain unverified. | BLOCKED / UNKNOWN | Documented lawful export/permission, source semantics, raw bytes/hash and coverage. |
| UKR Q2 vintage | C258 recheck found no observation-specific Q2 revision/version identity. | Asset/liability/semantic PASS; vintage PENDING; full NO. | New official NBU Q2 revision/version artifact with observation-level vintage linkage. |
| GEO Q2 revision | C261 NBG Q3 BOP release scheduled 30-Nov-2026. | WAIT; trigger not yet due. | After 30-Nov only if release is published and includes Q2 separate A/L revision plus vintage/methodology. |
- No new data or acceptance promotion. Macro-Geo P0 6/8; USD/INR disconnected; FPI/DII insufficient; strict hard gate BLOCKED. Detail: docs/GCR_CONTINUATION269_MILESTONE6_NEXT_ACTION_PRECONDITION_AND_NO_DUPLICATE_ROUTE_DECISION_20261126.md; commit adeee1a2a8ab820cbe94ffcf9c768b4fdd2d91f8. ₹0; no IMF re-query/cohort rebuild; UNKNOWN never PASS.


## GCR Continuation 270 — Mexico Q2-2026 Banxico Q3-release revision / vintage recheck (26-Nov-2026)
- New official Banxico Q3-2026 BOP release published 25-Nov-2026 (Cuadro 3) reports Q2 portfolio assets +USD9,480m and liabilities +USD10,561m; portfolio balance -USD1,082m. Prior 25-Aug Q2 release reported assets +USD8,937m and liabilities +USD10,561m. Q2 asset changed +USD543m; liability unchanged. Published balance differs from A-B by USD1m, consistent with whole-million rounding note.
- Reused IMF receipt 44474458684 / artifact 14505009889 (19-Nov): A_NFA_T +8,937.255098 USDm; L_NIL_T +10,561.285114 USDm. New Banxico Q3-release Q2 asset residual -542.744902 USDm (REVIEW / NOT MATCHED); liability residual +0.285114 USDm (PASS at ±0.5). IMF receipt predates new Banxico release; same-vintage not established. Revision cause/observation-level revision ID not established.
- MEX remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_REVISION_VINTAGE_RECHECK_CONTINUATION270_20261126.md; report commit d65bcb9cd08485ab4271f6a9dfef65ef8bc24609. Next: official observation-level revision/version bridge only; no repeat August extraction, IMF GET, cohort rebuild or IIP substitution. ₹0; UNKNOWN never PASS; production unchanged.
