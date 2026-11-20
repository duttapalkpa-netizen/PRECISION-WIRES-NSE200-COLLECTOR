# PRECISION-WIRES — Official Data Source Permission & Coverage Register
Date: 2026-11-20
Research continuation: গবেষণা যাচাই অব্যাহত 41, Part 2
Scope: documentation and acceptance only. No collection, scraping, endpoint probing, selector change, model training, or production integration was performed.

## Decision summary
- PUBLIC ACCESS / REUSE RIGHTS SEPARATE: MoSPI's current GSDD 2026 classifies aggregated publications (including National Accounts, CPI and IIP at NIC 2-digit level) as Category A open-access, free on MoSPI website without registration; anonymized unit/item-level data are Category B, registered and free for non-commercial use (commercial use priced); Category C is restricted and non-shareable data cannot be disseminated. GSDD is a dissemination/access framework, not automatically a blanket copyright, redistribution or model-training licence. Apply GODL-India only when the exact dataset record explicitly carries it; otherwise record reuse/training rights as UNKNOWN pending applicable terms.
- GO IF DATASET LICENSE CONFIRMED: data.gov.in resources individually marked GODL-India. The portal's general terms expressly defer to each dataset's licence metadata; portal presence alone is not a blanket licence.
- RESEARCH-ONLY / COURTESY REQUIRED: RBI DBIE, based on its FAQ's explicit research-use answer. Do not assume commercial redistribution, model-training, or sublicensing rights from that short FAQ; keep those uses unapproved pending current dataset-specific terms/clarification.
- REPRODUCTION PERMITTED WITH LIMITS: PIB-authored website material may be reproduced free with prominent source acknowledgement and accuracy/non-misleading context. Third-party material is excluded and needs its copyright holder's permission. Do not treat PIB as a general market-price feed.
- CONDITIONAL / RIGHTS REVIEW: IMF Data APIs expose SDMX 2.1/3.0. API availability is technical access, not a blanket licence. IMF content rights are reserved except specifically allowed uses; publication content is for personal research/teaching/fair-use, no commercial/systematic distribution. Obtain permission for broader reuse and verify dataset-level rights.
- BLOCKED / AGREEMENT REQUIRED: NSE market data. Policy requires subscription/order and relevant agreement, sets out permitted handling/use, restricts redistribution except as agreed; commercial market data is priced. Research requests are routed through NSE Economic Policy Research Department; non-commercial/research users need underlying documentation and confidentiality declaration. No free general entitlement inferred.
- BLOCKED / NOT REVIEWED: BSE, CDSL, depositories, FBIL, FPI/FII daily data, bulk deals and other exchange/vendor datasets without a separately reviewed current source-specific licence. Do not infer terms from NSE or GODL.

## Source register
| ID | Owner / source | Official access point | Free access / cadence | Permitted use evidenced | Attribution / retention / redistribution | Model training | Acceptance |
|---|---|---|---|---|---|---|---|
| IN-MOSPI-ES | MoSPI / e-Sankhyiki | https://esankhyiki.mospi.gov.in/ ; API catalogue linked from portal | Portal says open access, no registration; dataset-specific cadence (e.g. IIP monthly with ~4-week reference lag) | MoSPI GSDD 2026 classifies specified aggregate series as Category A and unit/item data as Category B/C; catalogue shows GSDD release label. No universal GODL licence established for every e-Sankhyiki record | Record exact GSDD category, source-specific terms, attribution and permitted purpose. Reuse, redistribution and model-training rights remain UNKNOWN unless an explicit dataset licence/terms grants them. GODL attribution applies only to records explicitly licensed under GODL-India | GODL-India permits lawful derivative works subject to exclusions and attribution; still verify data provider authority and exact resource licence before training | CONDITIONAL GO — resource-level licence check mandatory |
| IN-OGD-GODL | NIC / data.gov.in and publishing ministry | https://data.gov.in/terms-of-use ; https://data.gov.in/Godl | Open portal; individual resource terms control | GODL-India grants worldwide royalty-free non-exclusive lawful commercial/non-commercial use, adaptation, publication and derivative works for data validly licensed under it | Explicit attribution statement with provider, year, dataset, repository, version/date, URL and licence. Third-party, personal, sensitive or non-shareable material excluded. Provider does not guarantee continued updates | Derivative works allowed for properly licensed data; dataset-specific rights and exclusions still apply | GO IF individual dataset licence metadata = GODL-India (or other explicit compatible licence); otherwise UNKNOWN |
| IN-RBI-DBIE | Reserve Bank of India / DBIE | https://data.rbi.org.in/ ; RBI DBIE FAQ | Public portal; time-series downloadable; release cadence dataset-specific | DBIE FAQ says data may be used for research work with courtesy to DBIE/RBI. RBI handbook identifies validated central repository and publication process | Cite RBI/DBIE and exact table/publication/vintage. FAQ does not establish redistribution, retention, or sublicensing rights; no bulk republication assumed | UNKNOWN — FAQ's research-use statement does not expressly grant model-training rights | RESEARCH GO WITH COURTESY for internal research; redistribution/model training remain UNKNOWN pending current clarification |
| IN-PIB | Press Information Bureau, Government of India | https://www.pib.gov.in/ContentPage.aspx?lang=2&menuid=19&reg=48 ; https://www.pib.gov.in/content/102_2_Copyright-Policy.aspx?lang=1&reg=30 | Public press releases; publication time per release | PIB-authored website material may be reproduced free without prior approval if accurate, not derogatory/misleading, and source prominently acknowledged | Third-party material is expressly excluded; obtain rights from relevant department/copyright holder. Record release ID, publication timestamp, URL and exact version | Reproduction permission is not a blanket model-training licence; UNKNOWN for systematic ingestion/training | GO for accurate attributed reproduction of PIB-owned text; third-party attachments UNKNOWN |
| INT-IMF-DATA | International Monetary Fund | https://data.imf.org/en/Resource-Pages/IMF-API ; https://www.elibrary.imf.org/page/Rights%20and%20Permissions/rights-and-permissions ; https://www.elibrary.imf.org/help | SDMX 2.1/3.0 APIs documented; beta portal account for API explorer; dataset/publication access varies | API supports programmatic import. IMF eLibrary content may be used for individual research/teaching and typical personal/fair use; no commercial/systematic distribution | IMF copyright is reserved except specifically allowed uses; reuse permissions through Copyright Clearance Center / rights contacts. Preserve dataset IDs, vintage, metadata and citation | UNKNOWN / PERMISSION REQUIRED; no blanket training rights inferred | CONDITIONAL — internal analytical use only after dataset-level terms checked; broader reuse requires permission |
| IN-NSE-MD | NSE / NSE Data & Analytics | https://www.nseindia.in/static/market-data/nse-data-policy ; https://www.nse.in/static/market-data/real-time-data-subscription | Public website pages exist; licensed market-data products are contract/subscription-based; real-time/1m snapshot are formal products | Subscribers must submit requirements and execute relevant agreement. Research requests route via NSE Economic Policy Research Department. No automatic free entitlement | Agreement defines handling, use, end-user restrictions and redistribution; redistribution prohibited unless agreed. Non-commercial/research users sign confidentiality declaration. Commercial data priced | No training rights inferred; NSE MCP separately disclaims AI training/fine-tuning rights | BLOCKED until written terms/permission; not a free feed for V11.3 live gate |
| IN-SEBI-PRICE-EDU | SEBI circular / regulatory constraint | https://www.sebi.gov.in/legal/circulars/may-2026/norms-for-sharing-and-usage-of-price-data-for-educational-purposes_101293.html | Circular dated 2026-05-08 | For investor education/awareness sharing and usage, market price data lag is 30 days; NISM simulation lab has a 1-day exception with appropriate legal agreement | This is a regulatory constraint, not a data licence. Applicability to a private trading research pipeline needs legal/source-specific interpretation | Does not grant training rights | CONTROL / REVIEW REQUIRED; do not infer permission |
| IN-BSE / IN-CDSL / IN-FBIL / IN-FPI | Other exchange/depository/official data owners | Source-specific official domains to be added after review | Not yet established | Not established in this audit | Not established | UNKNOWN | BLOCKED / NOT REVIEWED |

## Dataset-level mandatory metadata contract
For every downloaded or API-sourced series, archive the following alongside the raw file:
1. `source_id`, legal owner, exact official URL/API endpoint, dataset/resource ID and dataset title.
2. Publisher, original source (if re-hosted), licence name/version and exact licence metadata URL captured at retrieval.
3. Permitted purpose flags: internal research, trading decision support, model training, publication, redistribution, commercial use — each independently PASS/BLOCKED/UNKNOWN.
4. Publication timestamp, reference period, retrieval timestamp (UTC and IST), timezone, revision/vintage, frequency, expected release lag.
5. Format, schema/version, units, classification/base year, coverage, known gaps, source status and HTTP/API status.
6. Attribution string, retention/deletion conditions, redistribution restrictions, authentication/registration requirement, written permission evidence/reference.
7. SHA-256 of exact raw bytes; immutable archive path; manifest entry; parser version and QA result.

## Pipeline acceptance rules
- A public URL, successful HTTP response, free download, API key, or open portal does not by itself establish reuse permission.
- Dataset-level licence metadata overrides portal-level assumptions. Third-party content is separately licensed.
- Unknown purpose/retention/training/redistribution rights remain UNKNOWN and are not ingested into that use.
- NSE equity price/volume/delivery, corporate disclosures, and 1-minute live feed must remain separated by source and licence. Macro sources cannot silently license exchange data.
- Only PASS-permitted sources may flow into the relevant research module; a research-only PASS does not imply live-trading or model-training PASS.
- Preserve source timestamp and vintage; never substitute retrieval time for publication time.
- No paid API/subscription, no synthetic observations, no access-control bypass, no fabricated timestamps.

## Current PRECISION-WIRES impact
1. MoSPI/e-Sankhyiki and data.gov.in are the best candidates for free macro/statistical inputs, but every selected series must be individually licensed and versioned.
2. RBI DBIE is suitable for cited internal macro research based on its FAQ, but broad redistribution and training rights remain unproven.
3. PIB is suitable for attributed official news/catalyst text reproduction within its copyright policy; third-party attachments must be excluded.
4. IMF API availability does not remove copyright restrictions; broader reuse/training stays gated.
5. NSE market data remains BLOCKED without a source-specific agreement/permission. NSE MCP does not resolve the live 1-minute feed gate.
6. Consequently, this register does not authorize a new stock pick, production selector change, GCR score boost, or live alert. Qualified actionable candidates remain 0 until the independent market-data and stock-readiness gates pass.

## Prior experience carried forward
- Run #407 T20_H5 discrepancy was caused by default float parsing; use `pd.read_csv(..., float_precision="round_trip")` for threshold outcomes and do not round labels.
- Run #407 live source 403 is handled fail-closed; never bypass exchange access controls.
- NSE MCP's 1–3 minute snapshot must not be treated as 1-minute candles or a trading licence.
- The SEBI 30-day educational/awareness rule is not interpreted here as a blanket private-research exemption.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.

## Evidence sources
- NSE Data Sharing & Usage Policy: https://www.nseindia.in/static/market-data/nse-data-policy
- NSE pricing schedule (shows student/researcher historical-data fees; no assumption of free access): https://nsearchives.nseindia.com/web/mediaattachment/2026-03/NSE_Pricing_file_-_Domestic_clients_20260309171343.pdf
- SEBI Circular 08-May-2026: https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1778242522289.pdf
- MoSPI e-Sankhyiki: https://esankhyiki.mospi.gov.in/
- OGD e-Sankhyiki catalog: https://data.gov.in/catalog/e-sankhyiki
- OGD Terms: https://data.gov.in/terms-of-use
- Government Open Data License-India: https://data.gov.in/Godl
- RBI DBIE: https://data.rbi.org.in/
- RBI DBIE FAQ (research-use answer): https://dbieold.rbi.org.in/DBIE/doc/Frequently%20Asked%20Questions%20-%20DBIE.pdf
- RBI DBIE April-2026 handbook: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=24094
- PIB Terms/Copyright: https://www.pib.gov.in/ContentPage.aspx?lang=2&menuid=19&reg=48
- IMF API: https://data.imf.org/en/Resource-Pages/IMF-API
- IMF Rights & Permissions: https://www.elibrary.imf.org/page/Rights%20and%20Permissions/rights-and-permissions
- IMF eLibrary use FAQ: https://www.elibrary.imf.org/help
- World Bank summary terms (CC BY 4.0 except dataset-specific third-party restrictions): https://data.worldbank.org/summary-terms-of-use

## Audit status
- Source-policy research: COMPLETED for the listed sources.
- Source-specific licence capture for each future series: REQUIRED at ingestion time.
- Written NSE permission: NOT OBTAINED.
- IMF broader reuse/model-training permission: NOT OBTAINED.
- Live 1-minute official free feed: NOT ESTABLISHED.
- Production integration: NOT AUTHORIZED / NOT PERFORMED.
