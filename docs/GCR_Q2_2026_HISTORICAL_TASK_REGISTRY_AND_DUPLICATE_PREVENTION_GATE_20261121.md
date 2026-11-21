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
- Updated only CPV matrix descriptive note; retained BLOCKED, NOT_CAPTURED legs, UNKNOWN vintage, FULL_PASS NO and aggregate NOT_AUTHORIZED. No numeric gate promotion.
- Detail: `docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_BPM5_BPM6_METHODOLOGY_CONFLICT_RESOLUTION_CONTINUATION213_20261121.md`; matrix commit `d5c778f5ad1063a3d39ade392d2224bb6c04b1ce`, blob SHA-1 `1569f1eb77b5ad3eaddea881f72e5ca23ab5522e`; report commit `79d2ff1f143d1e17ce3b1d6013a101846978fd72`.
- No BCV XLS retry, IMF re-query, cohort rebuild, synthetic data or production change; ₹0; UNKNOWN never PASS.
