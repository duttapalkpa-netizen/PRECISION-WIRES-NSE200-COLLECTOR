# GCR — RBI DBIE Table 42 BPM6 quarterly data route and sign-convention audit
Date: 2026-11-19 (Asia/Kolkata)
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Stage: Observation only
Status: OFFICIAL NATIONAL CROSS-CHECK ROUTE VERIFIED; RAW EXPORT NOT ACQUIRED

## 1. Purpose
Resolve a practical India-data bottleneck without conflating RBI national statistics with the IMF BOPS dataset used by the RBI sudden-stop paper. Identify a concrete official quarterly BPM6 data table, its public download formats, period coverage and sign semantics.

## 2. Official RBI/DBIE route
### 2.1 Table identity and DBIE mapping
RBI April-2026 “Comprehensive Guide for Current Statistics of the RBI Monthly Bulletin” identifies:
- Table 42: Standard Presentation of BoP in India as per BPM6 (US$ million).
- Frequency: Quarterly.
- Unit: US$ million.
- Source Department: DEPR; primary data source: RBI.
- Revision policy: subject to revision.
- DBIE paths: Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector; and Statistics > External Sector > International Trade.
- Table 43 is the ₹ crore BPM6 counterpart; Table 42 and Table 43 should remain distinct unit representations.

Official guide URL: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24094
Source lines inspected: 1497–1526.

### 2.2 DBIE public table page
Official DBIE table page:
https://dbie.rbihub.in/tables?table=external_sector.r143_standard_presentation_of_india_s_balance_of_payments_as_pe

Search-indexed page metadata reports:
- Title: “Standard presentation of India’s balance of payments as per BPM6-quarterly - US dollar”.
- Source: Reserve Bank of India (DBIE).
- Frequency: Quarterly.
- Period: 30-06-2011 to 30-06-2026.
- Reported rows: 91.
- Download controls: CSV and JSON.
- Rendered table page states “No Rows To Show” in the captured search output while metadata and CSV/JSON controls are visible. This is evidence of a public export route, not proof that a successful raw export was downloaded in this audit.
Source URL is a DBIE first-party route, but page HTML inspection through the research browser returned only a JavaScript shell; container-side network retrieval also failed DNS resolution. No direct CSV/JSON URL, response bytes or HTTP status was captured.

### 2.3 Scope and BPM6 categories
RBI Table 42 covers:
- Current account: goods/services, primary income, secondary income.
- Capital account: acquisition/disposal of non-produced non-financial assets and capital transfers.
- Financial account: direct investment, portfolio investment, financial derivatives, other investment and reserve assets.
- Total assets/liabilities and net errors and omissions.
- Credit, debit and net components; financial account by functional classification; residence principle and double-entry accounting.
- Preliminary observations are marked P where applicable.

## 3. Sign convention — important for flow interpretation
RBI's April-2026 handbook general BoP convention states:
- Increase in assets or decrease in liabilities is recorded as a debit.
- Increase in liabilities or decrease in assets is recorded as a credit.
This means:
- A portfolio-liability increase (foreign investors adding claims on India) is represented on the credit side under the stated convention.
- A portfolio-asset increase (Indian residents acquiring foreign portfolio assets) is represented on the debit side.
- Do not infer gross inflow by taking a signed net column without identifying whether the row is assets, liabilities, credit or debit.
- Table 42 presents net as credit minus debit where the guide specifies this for BoP presentation; reserve assets carry special BPM6 sign treatment in the financial-account presentation.
- Table 43 explicitly notes increase in reserve assets is shown with a negative sign, consistent with BPM6. Do not apply this reserve sign rule to portfolio liabilities/assets.

This convention is a safe semantic mapping, not a substitute for checking each downloaded row's exact label, credit/debit/net values and footnotes.

## 4. Relationship to the IMF/RBI sudden-stop replication
- RBI Table 42 is a national BPM6 quarterly cross-check source.
- It is not proven identical to the IMF BOPS vintage, item codes, coverage, revisions or transformation used in RBI Occasional Paper's historical sudden-stop exercise.
- The paper's event register covers Q1:1992–Q1:2022; Table 42 DBIE page currently reports coverage beginning 2011-06-30. Thus Table 42 alone cannot reproduce the full Q1:1992–Q1:2022 event register.
- Do not backfill pre-2011 values from other RBI tables without a separately verified series bridge and matching definitions.
- Use Table 42 only to test overlapping quarters once raw CSV/JSON and row definitions are acquired; retain IMF source as a separate target.

## 5. Acquisition acceptance protocol
Before using the DBIE export:
1. Download CSV and JSON separately from the official table page; record final URL, HTTP status, content type, retrieval timestamp, byte count and SHA-256 for each raw file.
2. Confirm the export covers the page's reported 2011-06-30 through 2026-06-30 period and inspect all 91 reported rows; do not treat page metadata as proof of actual exported rows.
3. Preserve original column labels, quarter-end dates, row/item codes, credit/debit/net values, unit, P/PR/revision markers and blank cells.
4. Validate duplicate keys, quarter chronology, row count, column count, missing values and arithmetic net = credit - debit only for rows where RBI defines net that way.
5. Separately inspect reserve asset sign and all assets/liabilities row semantics.
6. Compare overlapping quarters to the relevant RBI Bulletin Table 42 release, preserving vintage differences and publication dates.
7. Only then create an explicitly labelled national cross-check series. Do not label it IMF BOPS or use it to claim replication of 1992–2022 episodes.

## 6. Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| RBI Table 42 official BPM6 definition | PASS | RBI handbook |
| Frequency/unit/source/revision metadata | PASS | Quarterly; US$ million; RBI; revisable |
| DBIE first-party table route | PASS | Official table page and DBIE mapping |
| CSV/JSON export controls surfaced | PASS (route only) | Search-indexed DBIE page |
| Reported coverage 2011-06-30 to 2026-06-30 | PASS (page metadata only) | DBIE page metadata |
| 91 rows confirmed in raw export | NOT_DONE | No raw file |
| CSV/JSON bytes and SHA-256 | NOT_ACQUIRED | No raw export |
| Full item-level credit/debit/net mapping | NOT_DONE | Need downloaded table schema |
| IMF-to-RBI vintage/definition equivalence | UNKNOWN | No equivalence proof |
| Full Q1:1992–Q1:2022 sudden-stop reproduction | NOT_DONE | Table 42 begins 2011-06-30 |

## 7. Decisions and invariants
- RBI Table 42 is a separately labelled national cross-check only.
- Table 43 ₹ crore series must not be mixed with Table 42 US$ million.
- No synthetic pre-2011 extension, interpolation, sign guessing or revision erasure.
- No raw export or SHA-256 is claimed.
- Observation remains OPEN; Planning/Organizing remain NOT_STARTED.
- ₹0 spend; official/free sources only.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged.
- UNKNOWN is never PASS. GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.

## 8. Next highest-value action
Obtain the DBIE Table 42 CSV and JSON using the visible official download controls in a browser-capable environment, archive raw bytes and hashes, and validate the 91-row schema and all quarter keys. If the download control cannot be executed in the current environment, retain this route as VERIFIED / RAW_ACQUISITION_NOT_DONE and do not fabricate a download URL.
