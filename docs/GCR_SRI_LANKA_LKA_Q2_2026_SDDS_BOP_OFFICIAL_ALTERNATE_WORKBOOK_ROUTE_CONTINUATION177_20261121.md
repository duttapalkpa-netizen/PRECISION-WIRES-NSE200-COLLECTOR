# Sri Lanka LKA Q2-2026 — Official SDDS BOP alternate workbook route gate (Continuation 177)
Date: 2026-11-21 (Asia/Kolkata)
Decision: A DISTINCT OFFICIAL CBSL SDDS “More Data” BOP.XLSX ROUTE WAS DISCOVERED; THE LEGACY SDDS NSDP PAGE IS LAST UPDATED 11-NOV-2017 AND ITS TABLE SHOWS Q2/17 OBSERVATIONS, SO THIS WORKBOOK CANNOT BE ASSUMED TO CONTAIN Q2-2026; WEB CLICK REJECTED XLSX AS UNSUPPORTED CONTENT TYPE AND CONTAINER DOWNLOAD FAILED; NO BYTES/HASH/WORKBOOK CONTENT; ROUTE DISCOVERY PASS, Q2-2026 DATA VALIDATION NOT_DONE; LKA REMAINS PROVISIONAL; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger (blob SHA `3d8e995218405013018fe68865ec4d7b3de74c55`), GCR Priority Queue (`92b31f78d32f901155ab0bb3e261abb92f47432a`), Historical Registry (`4be3be236c2ebe96b98863ba6506828033e18da8`), C176 (`4f8770f924ad2907ebd50441e095702fc94e023f`), C175 (`e1d4c34c20e64fc87567499d777e511463cac4a2`), C174 (`36363f9a1e85cc1922ee96005f5f310b1bb6c67f`) and fixed cohort (`31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- LKA remains in immutable cohort; no cohort rebuild or IMF re-query.
- Did not repeat the prior direct Table 2.10 XLSX route, nor the Macro Lab HTML/JSON-click attempts.

## 2. Official alternate route discovery
- Re-opened CBSL official SDDS page: https://www.cbsl.gov.lk/en/node/1809 .
- The page identifies itself as “National Summary Data Page [NSDP]” and states data are preliminary when first released; page explicitly says “Last Updated On: 11th November 2017”.
- Under EXTERNAL SECTOR > Balance of Payments, the “More Data” link is link 191. Clicking it resolves to the distinct official file:
  https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sdds/BOP.xlsx
- Web retrieval returned: HTTP 400 / unsupported content-type for XLSX.
- Separate container download attempt also failed; no file created.
- CBSL NSDP “SDDS National Summary Data” link (erd.cbsl.gov.lk) click timed out HTTP 400. This is a distinct official portal route but not an accessible dataset response.

## 3. Critical temporal boundary
- The legacy NSDP page is explicitly dated 11-Nov-2017. Its BOP table rows show Q2/17 observations (e.g. Portfolio Investment Assets and Liabilities at lines 374–400 of the page).
- Therefore, the BOP.xlsx route is a real official alternate file locator, but there is no evidence from the retrieved page that the workbook contains Q2-2026. It may be a stale legacy workbook. No Q2-2026 claims are permitted until workbook bytes/sheets/periods are inspected.
- Do not infer that the file is current simply because the link is still live.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort / continuity preflight | PASS |
| Distinct official CBSL SDDS workbook locator found | PASS |
| Official page freshness | FAIL for currentness: last updated 11-Nov-2017 |
| BOP.xlsx bytes / headers / workbook inspection | NOT_CAPTURED |
| Q2-2026 observations in BOP.xlsx | NOT_VERIFIED |
| Raw file SHA-256 | NOT_CAPTURED |
| LKA Q2-2026 dual-leg reconciliation | remains C174/C176 strong provisional only |
| LKA final national source validation | NOT_PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Rejected list
- Do not treat legacy 2017 NSDP table as current Q2-2026 evidence.
- Do not infer file contents or vintage from filename BOP.xlsx.
- Do not retry the same unsupported-content-type web click or same container download route absent a genuinely new transfer capability.
- Do not substitute Macro Lab secondary data or old BOP mirror series for primary CBSL evidence.
- No IIP stock, net-only back-solving, annual/H1 substitute, IMF re-query or cohort rebuild.

## 6. Next exact action
1. If a supported file-transfer mechanism can retrieve the official BOP.xlsx as bytes, inspect its workbook sheets, dates, units, financial account components and revision metadata; only proceed if it contains Q2-2026.
2. Otherwise close this legacy route as stale/blocked and advance to the next fixed-cohort country after full preflight.
3. Aggregate remains NOT_AUTHORIZED until cohort-level acceptance is complete.

## 7. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or acceptance relaxation. Research spend ₹0. UNKNOWN is never PASS.
