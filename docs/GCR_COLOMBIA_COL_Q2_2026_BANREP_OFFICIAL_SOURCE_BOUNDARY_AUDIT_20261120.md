# Colombia (COL) Q2-2026 — Banco de la República official-source boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: official Q2 report and SDDS page inspected; direct Q2 portfolio transaction legs NOT_EXTRACTED; national numeric validation NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.

## Continuity and duplicate rejection
- Reused the fixed 63-country 2026-Q2 dual-leg cohort. Its existing coverage matrix records COL with 46 observations in each of A_NFA_T and L_NIL_T, both ending 2026-Q2. This is panel availability only, not numeric admission.
- Repository search found no prior COL national-source report or COL Q2-2026 portfolio-flow reconciliation. No cohort rebuild, IMF re-query, or panel reconstruction was performed.
- Existing IMF normalized panel and exact-key receipt were not modified. No raw COL IMF observation values were transcribed or asserted in this source-boundary task.

## Official Banco de la República evidence
1. Banco de la República Q2-2026 Balance of Payments and International Investment Position report:
   https://banrep.gov.co/es/publicaciones-investigaciones/informe-balanza-pagos/segundo-trimestre-2026
   Publication date: 2026-09-01. The official report states Q2 financial-account net capital inflows of USD 3,719m and says these include net liquidation of external assets (USD 6,149m), derivative gains paid by nonresidents (USD 804m), partially offset by decreases in external liabilities (USD 2,683m), plus reserve-asset transactions (USD 550m). It describes net liquidation of portfolio instruments as a partial offset, but does not publish Q2 portfolio asset and liability transaction legs separately in the inspected report text/PDF.
2. Exact official report PDF rendering:
   https://banrep.gov.co/es/print/pdf/node/66270
   Inspected PDF pages 0–4. Page 1 lines 22–32 and page 3 lines 44–53 contain the financial-account summary and the BPM6 sign explanation. The report says financial-account presentation uses the same sign as the current account. This is a general financial-account presentation note; it is not a sufficient portfolio-component-specific crosswalk for A_NFA_T/L_NIL_T.
3. Banco de la República SDDS economic/financial data page:
   https://www.banrep.gov.co/economia/dsbb/imfcolom.htm
   Page states last updated 2026-11-13. Its Q2/26 portfolio rows under International Investment Position show ASSET STOCKS: portfolio investment USD 125,046.1m (equity 72,701.1; debt instruments 52,344.9) and LIABILITY STOCKS: USD 118,800.9m (equity 7,692.1; debt instruments 111,108.8). These are end-period IIP positions, NOT Q2 BOP transaction flows. They are explicitly excluded from comparison to IMF A_NFA_T/L_NIL_T.
   The same page defines (p) provisional and (r) revised in its footnotes; no observation-specific vintage/revision timestamp for the Q2 portfolio-flow legs was identified.
4. BanRep's statistics portal link from the report resolves to a series page for current-account/financial-account statistics but the web reader timed out. No values, export, or raw bytes were obtained from that route in this task.

## Source boundary / fail-closed decision
- Q2 portfolio transaction legs (net acquisition of financial assets and net incurrence of liabilities): NOT_EXTRACTED.
- Q2 financial-account aggregate: USD 3,719m, but it includes reserves and derivatives and is not a portfolio-only net flow; do not use as proxy.
- Q2 portfolio IIP stocks: available, but wrong measurement type for a flow reconciliation; explicitly NOT_ADMITTED.
- National sign mapping: general BPM6 financial-account presentation note located, but portfolio-row direction mapping remains NOT_ESTABLISHED.
- Same-vintage bridge to the existing IMF Q2 panel: NOT_ESTABLISHED.
- No numeric residual, tolerance, dual-leg PASS, or aggregate authorization is claimed.

## Next exact action
Use the official BanRep statistics portal's underlying public series/export metadata (not the IIP stock rows) to identify the two Q2-2026 portfolio transaction series, their exact labels, units, signs, source update/revision metadata and raw export route. If the public export remains inaccessible or does not expose separate legs, preserve COL as BLOCKED / NOT PASS and move to the next eligible cohort member. Do not re-query IMF or rebuild the cohort.

## Invariants
No paid sources, no fabricated values/timestamps, no stock-flow substitution, no inferred sign flip, no netting, no forward-fill, no aggregate. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## Continuation 47 — BanRep datawarehouse series catalogue discovery (2026-11-20)
- Followed the official BanRep Balance of Payments page's datawarehouse link and its official SUAMECA statistical portal. The general BanRep page explicitly states the datawarehouse contains quarterly BPM6 Balance of Payments from 2000 onward and exposes a dedicated “Annex for Portfolio Investment” view; it describes financial-account presentation as the same sign as the current account. This general note still does not by itself establish the exact IMF component mapping.
- Official BanRep “Descarga múltiple de datos” catalogue search result exposes three distinct quarterly series, all in current USD millions, coverage 2000-Q1 through 2026-Q2, last update 2026-09-01: (i) “Balanza de pagos - Cuenta financiera - inversión de cartera - Trimestral” (portfolio total); (ii) “... inversión de cartera - adquisición neta de activos financieros - trimestral” (portfolio net acquisition of financial assets); and (iii) “... inversión de cartera - pasivos netos incurridos - trimestral” (portfolio net incurrence of liabilities). The latter two are the exact national concepts needed for A_NFA_T and L_NIL_T, subject to series-level sign/metadata confirmation.
- This narrows the previous blocker: the two separate Q2 portfolio series do exist in the official catalogue and have matching frequency, currency and endpoint period. However the SUAMECA download-multiple page times out in the web reader; no series IDs, raw export, exact Q2 values, response metadata or SHA-256 were obtained. The catalogue discovery is metadata-only, not numerical extraction.
- Q2 values remain NOT_EXTRACTED; sign mapping remains NOT_ESTABLISHED; numeric comparison NOT_DONE; same-vintage NOT_ESTABLISHED; COL national acceptance PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Do not infer exact row values from aggregate report or IIP stocks.
- Official source references: BanRep BOP datawarehouse description https://www.banrep.gov.co/es/node/35018 ; SUAMECA multiple-download catalogue https://suameca.banrep.gov.co/descarga-multiple-de-datos/ .
- Next exact action: use an available browser/owner-side supported route to access SUAMECA's exact three series entries, obtain the two component series identifiers and raw quarterly CSV/XLS export, preserve retrieval receipt and SHA-256, then inspect Q2 values and series metadata/sign definitions. No IMF re-query, no cohort rebuild, no production changes.


## Continuation 48 — official SDMX access-route audit (2026-11-20)
- New official BanRep SDMX consumer guide, version 4.0 (October 2026), was inspected: https://suameca.banrep.gov.co/archivos/webservices/sdmx_v_3_1/GUIA_CONSUMO_SDMX_V_3_1.pdf . It confirms public REST access without registration, XML/JSON/CSV response formats, endpoint https://totoro.banrep.gov.co/sdmx/rest/, and the required flowRef/period parameters.
- Critical scope check: the guide's Annex 1/2 lists the supported SDMX topics and flow IDs (IBR, DTF, TRM, TPM, TIB, COLCAP, monetary aggregates, UVR, TES); it does not list Balance of Payments / portfolio investment. Therefore the documented SDMX REST service cannot currently be treated as a validated BOP export route. Do not guess a flow ID or issue a fabricated data request.
- Official multiple-download catalogue remains evidence that both portfolio component series exist (current USD millions, quarterly, through 2026-Q2, published 2026-09-01): https://suameca.banrep.gov.co/descarga-multiple-de-datos/ . But catalogue discovery supplies no series IDs or Q2 values in the captured response. SUAMECA series page access still returned 502 in the web reader; no export/raw bytes/receipt/hash acquired.
- Decision unchanged: discovery PASS; raw capture NOT_DONE; numeric comparison NOT_DONE; sign mapping NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; COL PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. IIP stocks and aggregate financial-account totals remain excluded.
- Next: close this specific SDMX route as NOT_APPLICABLE to BOP under the published guide; pursue exact series export only through a distinct supported SUAMECA browser/export route. If unavailable, advance to the next not-yet-audited country in the fixed cohort after repository preflight. No IMF re-query or cohort rebuild.
- Web evidence: BanRep SDMX guide v4.0 and official SUAMECA catalogue were inspected on 2026-11-20; no data observation extracted.
