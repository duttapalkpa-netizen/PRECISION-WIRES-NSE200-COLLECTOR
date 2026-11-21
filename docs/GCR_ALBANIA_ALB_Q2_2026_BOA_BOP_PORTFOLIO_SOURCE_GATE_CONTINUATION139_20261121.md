# Albania (ALB) Q2-2026 — Bank of Albania portfolio BOP source gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 139
Status: Fixed-cohort and official quarterly BOP route PASS; separate portfolio asset/liability taxonomy PASS; exact Q2 numeric extraction NOT_DONE; national sign/scale/vintage crosswalk NOT_ESTABLISHED; ALB PARTIAL / NOT PASS.

## 1. Continuity preflight and selection
- Reopened current Master Continuity Ledger (blob SHA b90cd6d7937e9f5a4ecb7c9b179fd4365089a41a), Master Priority Queue (blob SHA dcc0f758b6b5bfd4bdf1cb7b571123e521d451bc), immutable 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), HUN C138 report and existing archived IMF raw panels.
- HUN's MNB monthly portfolio route was bounded and closed: MNB says monthly time series are not published and its monthly page contains selected estimated components, not monthly portfolio legs. No further identical MNB monthly route retry.
- ALB is in the immutable 63-country Q2 both-leg cohort and no dedicated ALB Q2-2026 national portfolio report was present in the repository tree during preflight. Selected as the next candidate with a distinct official central-bank quarterly BOP route exposing portfolio assets and liabilities.
- No cohort rebuild and no IMF re-query.

## 2. Official Bank of Albania Q2-2026 BOP publication gate
- Official Statistics Calendar 2026 lists “Balance of payments and gross external debt — Q II 2026” for 10-Sep-2026.
- Official Bank of Albania Time Series — Balance of Payments page identifies the source as quarterly, Bank of Albania, and reports data update 10-Sep-2026.
- Official page: https://www.bankofalbania.org/Statistics/External_sector_statistics/Balance_of_Payments/Time_Series-Balance_of_Payments.html
- The table metadata describes values in millions of euros and quarterly basis. It exposes Financial account / Portfolio investment with distinct parent rows and component hierarchy:
  - C.2 Portfolio investment
  - C.2.A Assets, including C.2.A.1 equity and investment fund shares and C.2.A.2 debt instruments
  - C.2.L Liabilities, including C.2.L.1 equity and investment fund shares and C.2.L.2 debt instruments
- This is a national BOP transaction table, not an IIP stock table. Bank of Albania's external-sector overview distinguishes BOP transactions from IIP stocks and states that Albania's BOP is compiled under BPM6.
- Numeric rows for 2026-Q2 were not exposed in the browser-readable page response; the page's interactive controls/table data could not be captured as raw rows in this bounded task. Do not infer or invent values from table taxonomy.

## 3. Existing archived IMF exact ALB Q2 rows — reused
- Existing raw IMF panel files and hashes:
  - Asset panel blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8.
  - Liability panel blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Exact archived rows:
  - A_NFA_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=181700604.8387097, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
  - L_NIL_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=145011618.7096774, SCALE=6, PRECISION=6, DERIVATION_TYPE=O.
- Values and attributes remain raw and unchanged. No new IMF request, no rescaling or sign transformation.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| ALB fixed 63-country cohort membership | PASS |
| Official Bank of Albania Q2 BOP publication calendar | PASS |
| Official quarterly BOP table/data update 10-Sep-2026 | PASS |
| Quarterly EUR million presentation | PASS (table metadata) |
| Portfolio asset/liability hierarchy | PASS (C.2.A / C.2.L) |
| Equity/debt subcomponents | PASS (taxonomy only) |
| Exact Q2-2026 national asset/liability observations | NOT_DONE |
| Raw national export/bytes/retrieval receipt/SHA-256 | NOT_DONE |
| Country-specific sign and aggregation crosswalk | NOT_ESTABLISHED |
| Existing IMF exact Q2 raw rows | PASS (reused) |
| Numeric dual-leg reconciliation | NOT_DONE |
| Same-vintage alignment | NOT_ESTABLISHED |
| Full ALB national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Exact next actions
1. Retrieve the Bank of Albania interactive quarterly BOP table's machine-readable export or underlying official dataset response for Q2-2026; preserve exact raw bytes, response metadata, retrieval UTC and SHA-256.
2. Extract both C.2.A and C.2.L parent totals and their equity/debt child rows; determine whether parent totals are directly reported or must be derived from the children. Never double-count parent and child rows.
3. Capture the official sign convention and verify whether the source uses assets-minus-liabilities and whether the two legs correspond to IMF A_NFA_T and L_NIL_T.
4. Compare separately with the archived IMF raw observations, preserving original USD raw values and any admitted EUR conversion/tolerance method.
5. Seek an exact publication-vintage/revision bridge. If unavailable, retain PARTIAL / NOT PASS and advance.
6. No IMF re-query, no cohort rebuild.

## 6. Protected invariants
₹0; free official sources only. No synthetic data, no fabricated values/timestamps, no IIP stocks as BOP flows, no net-to-leg back-solving, no unsupported FX/sign/scale transform, no repeated IMF requests. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## Continuation 140 — ALB BPM6 sign, FX and revision gates; interactive export boundary (2026-11-21)

### Official methodology/sign crosswalk — PASS
- Bank of Albania External Sector Statistics page states Albania's BOP is compiled according to IMF BPM6 and explicitly distinguishes BOP transactions over a period from IIP asset/liability stocks at a point in time.
- Bank of Albania's official 2014 “Commentary for changes in the publication of external sector statistics according to BPM6” states for the financial account: increases in assets and liabilities carry positive signs; decreases in assets and liabilities carry negative signs; financial-account balance is change in assets minus change in liabilities. This is a directly relevant national sign-convention document, not an inferred generic rule.
- IMF GDDS/DQAF Albania BOP metadata states data are published in EUR millions; transactions in other currencies are converted to ALL using monthly exchange rates applicable at transaction time; financial transactions are recorded on accrual basis; revision policy is published in methodological notes and revisions occur at fixed publication moments. It also says the time-series table can be downloaded in Excel and the online dynamic table can be copied to Excel.
- These establish the broad BPM6 sign and conversion framework, but not the exact Q2-2026 values, observation-level revision vintage, or item-by-item IMF series equivalence.

### Exact value extraction — retrieval boundary
- Reopened official Bank of Albania Main data page (cregtab_id=645). It exposes the quarterly BOP dataset, EUR-million unit, period controls and portfolio rows C.2.A / C.2.L with equity/debt children. Official page metadata says data updated 10-Sep-2026.
- Web-readable response exposes the index and interactive controls only; it does not return the selected quarter's observation cells or downloadable workbook bytes. No numeric C.2.A/C.2.L Q2 values, export bytes, retrieval receipt, or national SHA-256 were captured.
- This is a limitation of the current retrieval channel, not evidence that Bank of Albania does not publish the values. The IMF DQAF says the detailed time-series tables are downloadable as Excel and the dynamic HTML table is copyable to Excel. Therefore the next valid route is a supported interactive browser/Excel export, not a guessed API endpoint.
- No values were invented; no net-to-leg back-solving; no IIP-stock substitution; no parent/child double counting.

### Updated acceptance
| Gate | Status |
|---|---|
| Official Q2 BOP dataset / quarterly / EURm / update 10-Sep-2026 | PASS |
| C.2.A and C.2.L separate hierarchy | PASS |
| BPM6 national financial-account sign rule | PASS |
| Transaction FX basis / accrual / revision policy metadata | PASS (general methodology only) |
| Exact national Q2 C.2.A / C.2.L observations | NOT_CAPTURED |
| Raw export bytes / national SHA-256 | NOT_CAPTURED |
| IMF archived Q2 rows | PASS (reused; no new request) |
| Numeric dual-leg reconciliation | NOT_DONE |
| Exact source-vintage bridge | NOT_ESTABLISHED |
| Full ALB validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

### Next action
- Obtain official Bank of Albania interactive table export through a supported browser/Excel route (owner-side export is an acceptable recovery path). Preserve original workbook/HTML, retrieval UTC, source page URL and SHA-256. Extract only Q2 2026 C.2.A and C.2.L plus C.2.A.1/.2 and C.2.L.1/.2; reconcile parent-child totals without double counting. Then compare separately with existing IMF rows, retaining raw values and explicit conversion/vintage status.
- If interactive export is unavailable, keep ALB PARTIAL and move to the next unvalidated member of the fixed 63-country cohort. No IMF re-query or cohort rebuild.

### Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, guessed API, net-to-leg inference, stock-as-flow, unapproved FX/sign/scale transform, duplicate IMF requests, cohort rebuild, or production changes. UNKNOWN is never PASS.


## Continuation 141 — ALB legacy Main-data period ceiling and retrieval boundary (2026-11-21)

- Reopened Bank of Albania public Balance of Payments page and its Main data link. The indexed Main data table explicitly identifies quarterly frequency and EUR-million units, and exposes C.2.A/C.2.L plus equity/debt children. However, its selectable period range in the browser-readable page terminates at Q3-2025; Q2-2026 is not selectable in that rendered table. Its methodology note also describes a 2017 revision vintage. This Main-data rendering therefore cannot be used as the Q2-2026 national numeric source, despite the separate statistics index advertising the aggregate BOP dataset updated 10-Sep-2026.
- A second direct attempt to open the selected interactive detail URL was rejected by the web retrieval layer (inaccessible). No endpoint guessed; no hidden request synthesized. The separate official statistics index and calendar continue to support that a Q2-2026 BOP release exists, but the current retrievable Main-data view does not expose its numeric rows.
- Official BPM6 commentary directly confirms the new financial-account signs: asset/liability increases positive, decreases negative; balance equals asset change minus liability change. It also notes BOP flows are published in EUR and users may convert using average exchange rate for flows (not end-period rate for stocks). This corrects the prior broad conversion note: the 2014 commentary provides a flow-conversion reference, but it does not establish the exact Q2-2026 transaction-level FX path or exact IMF series bridge.
- ALB updated acceptance: national sign convention PASS; taxonomy PASS; Q2-2026 numeric observations NOT_CAPTURED; raw bytes/hash NOT_CAPTURED; dual-leg comparison NOT_DONE; exact Q2-2026 vintage/FX bridge NOT_ESTABLISHED; PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Stop repeating the same Main-data route. Next, obtain a Q2-2026-specific downloadable export from the Bank of Albania statistics index through an actual supported browser/export route, or advance to another fixed-cohort member. No IMF re-query/cohort rebuild.
