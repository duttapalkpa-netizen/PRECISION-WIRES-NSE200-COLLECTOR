# GCR Q2-2026 — 10-country national dual-leg validation batch (Continuation 128)
Date: 2026-11-21
Mode: fixed batch of 10 countries; sequential execution, no need for the user to reselect countries between turns.
Scope: existing immutable 63-country Q2-2026 A_NFA_T + L_NIL_T cohort only. This batch is a work queue, not an assertion that any country is validated or aggregate-ready.

## 1. Preflight — current files and prior evidence
Re-fetched from main before selecting work:
- Master Continuity Ledger blob SHA: `41c6751ae38f3406b6fda8e557dea4ce59cb091e`.
- GCR Master Priority Queue blob SHA: `8b144d8c92b72bb8006c049486cf2bdba1e22da4`.
- Immutable 63-country cohort blob SHA: `1f767e22095865c8e5f87c2cfca55d9104b91e3e`.
- ZAF Continuation 127 report blob SHA: `d38433991363d420dd1f9e874de3f9068d8051bb`.
- CHN detailed SAFE access audit blob SHA: `0fbf24a0ef403e3076be22e911b924d4eefecf32`.
- COL source-boundary audit blob SHA: `d2990310af8edbd2787c153f9f5852fa75b977c3`.
- POL source-gate audit blob SHA: `fe17767c7842d462c1ebba7199180a892f4583a8`.
- TUR numeric reconciliation blob SHA: `cfe1a2aa5d21bac95b18f89be78804f26496f19c`.
- PER source-boundary audit blob SHA: `68205c0cf5b2a23b6a699943ec67075f21023295`.
- ROU source-gate audit blob SHA: `37f744511aeab33539d1fca15be0bce08536cd90`.
- NPL source-boundary audit blob SHA: `3b0ed641da92cbe383f0e4ef7bf021f4d1c89186`.
- RWA source-gate audit blob SHA: `af725eba157789e16e65a783e886d96f66fdc727`.
- SLV source-family gate blob SHA: `658b83d795529e9eecd99879039e6e8bcdb6a8c3`.
- SLB source/sign conflict report blob SHA: `7a696af5f0562941f59363d10bb6b58199319049`.

Completed work was excluded from duplicate extraction. Existing MEX/ARG/THA/MYS/SAU/PHL/IDN reports and comparisons are not repeated in this batch; their remaining vintage/revision issues stay in the master queue. ZAF is not re-extracted: liability comparison remains previously PASS, asset remains REVIEW, and quarterly-average FX equivalence is NOT_ESTABLISHED.

## 2. Fixed batch of 10 — execution order and exact work

| Order | Country | Current state | Next bounded action |
|---:|---|---|---|
| 1 | CHN — China | PARTIAL / BLOCKED | Attempt only a genuinely different supported byte-transfer route for SAFE official Q2-2026 detailed BOP XLSX. If still blocked, preserve exact error and move on; no repeated identical retries. |
| 2 | COL — Colombia | PARTIAL / BLOCKED | Use the new official BanRep SUAMECA multiple-download/catalogue route to identify/export exact Q2-2026 portfolio asset and liability quarterly series; capture raw bytes, metadata, timestamp and SHA-256. |
| 3 | POL — Poland | BLOCKED / NOT_DONE | Obtain NBP official Q2 quarterly workbook bytes through an XLSX-capable route; inspect sheet, period, units, revision and separate portfolio legs. |
| 4 | TUR — Türkiye | PARTIAL / NOT PASS | Obtain TCMB September 2026 official ZIP via a different supported transfer route; inspect revision/vintage and investigate existing USD87m liability residual. |
| 5 | PER — Peru | PARTIAL / NOT PASS | Inspect BCRP official public-sector portfolio-asset series metadata and documented API/export route; do not use total public assets as proxy. |
| 6 | ROU — Romania | PARTIAL / NOT PASS | Resolve official BNR/ECB Q2 source route; establish quarterly vs cumulative basis, exact portfolio asset/liability concepts, currency and signs. |
| 7 | NPL — Nepal | PARTIAL / NOT PASS | Retrieve official NRB External Sector BPM6 workbook through an XLSX-capable route; verify monthly flows vs cumulative fiscal-year values and separate legs. |
| 8 | RWA — Rwanda | PARTIAL / NOT PASS | Resolve official BNR June-2026 external-sector data item and determine whether it exposes Q2 separate legs rather than H1/net-only values. |
| 9 | SLV — El Salvador | PARTIAL / NOT PASS | Locate official BCR quarterly BOP source/export with separate portfolio transaction assets and liabilities; exclude central-bank balance-sheet stocks and annual IMF staff estimates. |
| 10 | SLB — Solomon Islands | PARTIAL / NOT PASS | Resolve CBSI Table 1.17 sign/presentation conflict using primary methodology and archived exact IMF rows; do not infer sign from aggregate financial-account arithmetic. |

Batch selection is grounded in existing unresolved reports, national-source availability and material blockers. If an item becomes externally blocked after one genuinely new route, record it and advance to the next item in this fixed batch; do not spin on the same failed endpoint.

## 3. New work completed in this batch
### CHN — distinct browser route attempt
- Reopened the official SAFE time-series detail page, index 000014453-2019-0016, dispatch date 2026-09-29.
- Followed its exact XLSX attachment link via the browser's numbered-link route.
- The browser returned HTTP-layer fetch error: unsupported XLSX content type (400). No workbook bytes, headers, content length or SHA-256 were obtained. This is a different retrieval surface from the prior direct download attempt, but it does not resolve the file-access blocker.
- Official SAFE page confirms the attachment is the detailed time-series file; the separate 29-Sep-2026 abridged release confirms Q2 exists but only publishes rounded aggregate capital/financial account data. Do not use IIP stocks as transaction flows.
- CHN remains PARTIAL / BLOCKED; no values/sign mapping newly admitted.

### COL — new official public series discovery
- BanRep's official SUAMECA “Descarga múltiple de datos” page is indexed with quarterly BOP series, all in current USD millions, covering 2000-Q1 through 2026-Q2 and last updated 2026-09-01.
- The official catalogue search result explicitly lists:
  1. “Balanza de pagos - Cuenta financiera - inversión de cartera - adquisición neta de activos financieros - trimestral”
  2. “Balanza de pagos - Cuenta financiera - inversión de cartera - pasivos netos incurridos - trimestral”
  plus the portfolio net series.
- These are the correct separate-flow concepts in principle, unlike IIP stock rows. The SUAMECA multiple-download page returned HTTP 502 when opened through the current retrieval bridge; no series IDs, export bytes, exact Q2 observations, raw hash or source vintage were captured.
- Official BanRep methodological note states BOP is quarterly, transaction-flow data, and financial-account categories include portfolio investment; it does not replace the missing exact series export.
- COL remains PARTIAL / BLOCKED; discovery improved, raw capture and numeric comparison NOT_DONE. No IMF re-query.

## 4. Batch control rules
- Work these ten sequentially; no need to ask the user to choose each country again.
- At each country: reopen only its latest report and relevant queue entry; do not repeat PASS extraction.
- Preserve exact raw OBS_VALUE and SCALE separately; no universal divide-by-million rule without supported scale semantics.
- Require national series identity, Q2 period, unit, sign, instrument scope, publication/revision vintage, raw bytes and SHA-256 before numerical admission.
- Compare assets and liabilities separately. Never infer one leg from net.
- Keep PARTIAL/BLOCKED/REVIEW until every acceptance gate is met.
- After these ten, choose the next ten from the remaining fixed cohort based on market relevance, official-source feasibility and dependency value; update this queue without rebuilding the cohort.

## 5. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, inferred sign/scale transformations, stock-as-flow, annual-to-quarter allocation, net-to-leg back-solving, IMF re-query, cohort rebuild, or aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## 6. Sequential execution update — POL, TUR, PER and ROU (2026-11-21)

### POL — second distinct official workbook route exhausted
- Re-opened official NBP workbook URL `https://static.nbp.pl/dane/bilans-platniczy/bop_q.xlsx` through the direct browser open route. It returned HTTP-layer 400 unsupported XLSX content-type.
- A separate container byte-download attempt also failed. No workbook bytes, response headers, content length, sheet names, revision timestamp or SHA-256 captured.
- This is now a second distinct retrieval surface beyond the earlier browser and direct file attempt documented in the prior POL audit. No more identical XLSX retries in this cycle.
- POL remains BLOCKED / NOT_DONE; national legs NOT_CAPTURED; no comparison. Advance to TUR.

### TUR — official ZIP direct route remains inaccessible
- Reused exact official TCMB ZIP URL already recorded in the prior country report and opened it directly through a separate browser route.
- Browser returned “URL is not accessible via this tool”. No ZIP bytes, headers, timestamp, content length or SHA-256 captured.
- Existing August/September PDF cross-check remains unchanged: assets 5,749 USDm reconcile at displayed precision; liabilities 9,183 vs IMF 9,270 USDm, residual +87 USDm; same-vintage identity NOT_ESTABLISHED.
- No repeated IMF query and no new PDF extraction. TUR remains PARTIAL / NOT PASS. Advance to PER.

### PER — official BCRP quarterly series page values independently rechecked
- Reopened official BCRPData quarterly Financial Account catalogue. It lists 58 quarterly series, with private-sector block (17) and public-sector block (25), USD millions, through T2-2026, last updated 20-Aug-2026.
- Reopened three official result pages and verified Q2 values:
  - Private-sector portfolio assets, PN39278BQ: T226 = +1,749 USDm.
  - Private-sector portfolio liabilities, PN39285BQ: T226 = +279 USDm.
  - Public-sector portfolio liabilities, PN39404FQ: T226 = +1,421 USDm.
  - Combined national liabilities = 279 + 1,421 = 1,700 USDm; against archived IMF L_NIL_T 1,699.66407147559 USDm, residual +0.33592852441 USDm, within ±0.5 USDm published precision.
- The public-sector catalogue contains aggregate assets PN39402FQ but no portfolio-specific public asset subseries in the complete listed 25-series block. Do not substitute the aggregate.
- The private asset + public asset full-sector coverage remains incomplete; the earlier private-only 1,749 vs IMF 1,999.15568669433 is not a valid like-for-like residual. PER national liability leg remains numeric PASS at whole-USDm precision; full asset leg PARTIAL / NOT_DONE; same-vintage/sign-definition not established; full dual-leg PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Official HTML result pages are the evidence; no raw API payload/bytes or SHA-256 archived. The documented BCRP API endpoint had already failed once; do not repeat the same exact API call.

### ROU — official methodology boundary reconfirmed; Q2 legs remain unavailable in this bounded step
- Search surfaced official BNR methodology material stating the BOP/IIP compilation uses title-by-title monthly data for portfolio investment at market value/accrual basis and quarterly surveys for other non-FDI/non-portfolio positions.
- BNR monthly bulletin methodology distinguishes IIP stock positions from BOP financial-account flows and notes quarterly IIP data are revised in March/September for previous reference periods. This is not a Q2-2026 transaction-leg extract and cannot be substituted for it.
- Official BNR pages/documents encountered through the retrieval bridge frequently returned “Request Rejected”; no Q2 national portfolio asset/liability rows, raw bytes/hash or exact vintage bridge captured.
- ROU remains PARTIAL / NOT PASS; both Q2 legs NOT_CAPTURED; numeric comparison NOT_DONE; aggregate NOT_AUTHORIZED.
- Batch next item is NPL (Nepal). Reuse existing NRB source discovery; do not retry known monthly archive route or identical unsupported XLSX fetch. Find a genuinely different supported NRB API/export route; otherwise document blocker and advance to RWA.

## 7. Current batch position
- CHN: BLOCKED (official SAFE XLSX bytes unavailable after distinct route).
- COL: BLOCKED (official SUAMECA page 502; series concepts discovered).
- POL: BLOCKED (NBP XLSX direct browser 400 and container download failed).
- TUR: BLOCKED for ZIP byte retrieval; numeric liability REVIEW +87m remains.
- PER: national liability numeric PASS; asset full-sector coverage PARTIAL; overall PARTIAL / NOT PASS.
- ROU: PARTIAL / NOT PASS; Q2 national legs NOT_CAPTURED.
- Next: NPL, then RWA, SLV, SLB.


## 8. Sequential execution update — NPL and RWA (Continuation 130, 2026-11-21)

### NPL — distinct NRB NSDP route tested; no current Q2 export
- Reopened NRB External Sector page; it lists Monthly Balance of Payments (BPM 6). The linked official September-2026 workbook remains the correct candidate, but direct retrieval still returns HTTP 400 unsupported XLSX MIME; no bytes/sheets/values/hash.
- Tested NRB NSDP separately. Its BOP Browse Data link resolves to a general macroeconomic report archive, not a BOP series browser. Its SDMX Download link points to NEPAL_BOP_2024_Q1.xml, stale for Q2-2026 and unsupported by current XML retrieval. DSBB link is metadata only.
- No alternate usable official Q2 export/API route found. Separate national portfolio assets/liabilities NOT_EXTRACTED; period basis/sign/unit/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE. NPL PARTIAL / BLOCKED. Do not retry identical XLSX, NSDP XML or wrong BFR monthly archive route. Advance to RWA.

### RWA — BNR June-2026 portal locator rechecked
- Official BNR External Sector portal search-indexed text lists “Balance of Payment” dated 30-Jun-2026 and states BPM6 compilation. Direct portal open returns a JavaScript-app shell; exact document URL/bytes remain unresolved.
- Official BNR August-2026 Monetary Policy Report Table 2 is only a 2025Q1/2026Q1 summary BOP table, omits portfolio legs, and cannot validate Q2. Existing H1 net-only +14 USDm and annual fiscal-year separate legs are not Q2 evidence.
- RWA Q2 A_NFA_T/L_NIL_T NOT_CAPTURED; PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: resolve June-30 BNR item through supported route, otherwise advance to SLV.


## 9. Sequential execution update — SLV (Continuation 131, 2026-11-21)

### SLV — official BCR quarterly publication calendar found; Q2 transaction rows not captured
- Located official BCR Revista Trimestral Abril–Junio 2026. Its publication calendar schedules quarterly Balance of Payments T2-26 for 30-Sep-2026; this is a planned publication date, not proof of actual availability.
- Table II.2 in that PDF still shows only 2025-Q3, 2025-Q4 and 2026-Q1. Q1-2026 portfolio assets net acquisition +282.76 USDm and liabilities net incurred -56.61 USDm are Q1-only; do not use as Q2.
- BCR SDDS quarterly BOP Data Base link (cdr=130) was followed as a distinct current data route and timed out. NSDP is stale (last update 2022-12-23). No exact Q2 row/value, raw file/hash or current database vintage retrieved.
- SLV Q2 assets/liabilities NOT_CAPTURED; sign/unit/concept/same-vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; PARTIAL / BLOCKED; aggregate NOT_AUTHORIZED. Do not interpret no search result as definitive non-publication.
- Next batch item: SLB (Solomon Islands), resolve CBSI Table 1.17 sign/presentation conflict using primary methodology and archived exact IMF rows; no inferred sign.
