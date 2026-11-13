# Global Capital Rotation Overlay — official-source access contract
Date: 2026-11-11
Scope: research-only source-access contract; no observations ingested and no production integration.

## Decision
This audit resolves source identity/frequency semantics for the next Global Capital Rotation ingestion slice. It does not claim that capital rotation itself has been measured. Positions, transactions/flows, FX rates, and benchmark returns remain distinct data types.

## Verified public official sources

| Signal family | Official source / identifier | Frequency / coverage | Permitted interpretation | Prohibited inference |
|---|---|---|---|---|
| Cross-border portfolio positions | IMF Portfolio Investment Positions by Counterpart Economy (PIP; formerly CPIS), dataset IMF.STA:PIP | Annual and semi-annual; equity/fund shares, long-term debt, short-term debt | Bilateral portfolio holdings/positions by counterpart economy; structural cross-border exposure | Not daily/weekly flow; valuation changes and exchange-rate effects can change positions |
| India PIP reporting | RBI PIP FAQ | India reporting half-yearly, end-March/end-September reference positions; RBI submits consolidated aggregates to IMF | India reporting cadence and confidentiality boundary | No entity-level holdings; no high-frequency flow proxy |
| US broad dollar index | Federal Reserve H.10 series H10/H10/JRXWTFB_N.B | Daily; available from 2006-01-02 to latest published observation in inspected package | Nominal Broad Dollar Index proxy, with explicit Fed definition | Do not label as ICE DXY; methodology/basket differs |
| US advanced-economy dollar index | Federal Reserve H.10 series H10/H10/JRXWTFN_N.B | Daily; available from 2006-01-02 | Nominal Advanced Foreign Economies Dollar Index | Not a broad all-country dollar index |
| US EM dollar index | Federal Reserve H.10 series H10/H10/JRXWTFO_N.B | Daily; available from 2006-01-02 | Nominal Emerging Market Economies Dollar Index | Not direct capital flow or an India-specific signal |
| Bilateral FX | BIS Bilateral Exchange Rates (XRU topic) | Daily for ~80 economies; monthly/quarterly/annual for broader coverage | USD bilateral exchange-rate history; source/methodology documented by BIS | Do not mix observation time conventions without recording them |
| US international holdings | Federal Reserve Enhanced Financial Accounts, International Portfolio Investment Holdings of Long-term Securities by Country (FRBCNA71) | Monthly country-level holdings | US-reported holdings of long-term securities by country | Holdings are not monthly net transactions; not complete global fund flows |
| India external position context | RBI International Investment Position | Quarterly reference dates | India external asset/liability and portfolio-position context | Not daily flow or same-day trading signal |

## Evidence and source URLs
- IMF PIP dataset: https://data.imf.org/datasets/IMF.STA%3APIP
- IMF PIP dataset page and frequency: https://data.imf.org/en/Datasets/PIP
- RBI PIP FAQ (updated 2026-06-01): https://rbi.org.in/scripts/FAQDisplay.aspx?Id=159
- Federal Reserve H.10 download program: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- Federal Reserve H.10 package review inspected the following identifiers and availability:
  - H10/H10/JRXWTFB_N.B — Nominal Broad Dollar Index
  - H10/H10/JRXWTFN_N.B — Nominal Advanced Foreign Economies Dollar Index
  - H10/H10/JRXWTFO_N.B — Nominal Emerging Market Economies Dollar Index
  - Inspected availability: 2006-01-02 through 2026-11-06
- BIS bilateral exchange rates: https://data.bis.org/topics/XRU
- Federal Reserve country holdings dataset: https://catalog.data.gov/dataset/international-portfolio-investment-holdings-of-long-term-securities-by-country
- RBI IIP archive: https://www.rbi.org.in/scripts/IIP.aspx

## Ingestion contract (must be applied before any source is admitted)
1. Preserve raw source file/API response unchanged; calculate SHA-256 before transformation.
2. Record exact URL/endpoint, query parameters (redacting credentials), UTC retrieval timestamp, source publication/vintage timestamp, reference period, file size, media type, and source series identifier.
3. Store source type explicitly as POSITION, TRANSACTION/FLOW, FX_RATE, PRICE_INDEX, or TOTAL_RETURN_INDEX.
4. Never relabel positions as flows. For position changes, decompose/label valuation and FX effects only if the source provides a defensible decomposition; otherwise keep the cause UNKNOWN.
5. Keep source frequency and observation calendars explicit. Do not forward-fill or fabricate daily values from semi-annual/monthly observations.
6. Keep Federal Reserve Broad Dollar Index separate from ICE DXY. Do not substitute one under the other's name.
7. Keep provisional/revised vintages immutable and append-only; do not overwrite prior releases.
8. Missing, stale, inaccessible, or schema-unverified observations remain UNKNOWN/BLOCKED, never PASS by assumption.

## Acceptance gates
- Source identity/frequency semantics: PASS for the sources and series explicitly listed above.
- Exact raw download and ingestion with SHA-256: NOT DONE.
- Data schema/coverage/vintage QA: NOT DONE.
- Global flow/position bridge and valuation-effect treatment: NOT DONE.
- Daily FX and benchmark return panel: NOT DONE.
- India sector attraction bridge: NOT DONE.
- Historical event study/backtest: NOT DONE.
- Overlay completion: NOT COMPLETE.
- Production integration: PROHIBITED without separate explicit approval.

## Project invariants
No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E, or Hard Gate. No composite stock score, stock ranking, buy/sell instruction, or automatic trading. ₹0 spend; free public official sources only; no synthetic observations; no paid API; no external contact.

## Research interpretation note
IMF PIP is semi-annual/annual positions data. The Federal Reserve H.10 dollar indices are FX indices, not flows. BIS bilateral exchange rates are rates, not flows. FRB country-level long-term holdings are positions. These can support a macro/structural context layer, but none independently establishes contemporaneous capital rotation into India. Any flow claim requires transaction/flow evidence at a matching frequency and coverage.


## High-value source addition: U.S. Treasury TIC monthly transaction files (2026-11-13)
Decision: add Treasury International Capital (TIC) Securities A as a candidate TRANSACTION/FLOW source family. This is a materially different evidence class from H.10 FX indices and IMF/Federal Reserve position/holdings series, so it advances the overlay without repeating the H.10 vintage-discovery loop.

Official source page:
https://home.treasury.gov/data/treasury-international-capital-tic-system-home-page/tic-forms-instructions/securities-a-us-transactions-with-foreign-residents-in-long-term-securities

Official monthly country files listed by Treasury:
- Net U.S. sales of U.S. long-term securities by month, global country file; current SLT-era data begin February 2023; HTML and tab-delimited text formats.
- Net U.S. purchases of foreign long-term securities by month, global country file; current SLT-era data begin February 2023; HTML and tab-delimited text formats.
- Gross purchases and sales by country and country groups also published.

Treasury states the new expanded SLT-based series began with February 2023 data and introduced a structural break from legacy Form S data ending January 2023. The new data are presented from the U.S. point of view. For U.S. purchases/sales of foreign securities, the new country breakdown identifies the country that issued the securities, unlike legacy S-form data which identified the transaction counterparty/country. Do not concatenate the two regimes without an explicit break flag and semantic mapping.

Critical interpretation constraints:
1. These are U.S.-reported cross-border transactions in long-term securities, not global all-market capital flows and not direct India FPI net flows into NSE.
2. The country attribution semantics differ across the Feb-2023 break; legacy Form S suffered transaction bias, with financial centers receiving outsized attribution. Do not treat pre-2023 country allocations as directly comparable to post-2023 issuer-country data.
3. Do not infer foreign investor residence from issuer-country fields or vice versa. Preserve field-level definitions from the downloaded file.
4. Do not combine net U.S. sales of U.S. securities with net U.S. purchases of foreign securities into a single flow without retaining direction and asset geography.
5. Treasury FAQ notes TIC data are U.S.-centric and limitations make precise conclusions about country-specific changes in foreign holdings difficult. Use as a global liquidity/cross-border transaction context feature only; no India-directed rotation claim without India-specific corroboration.
6. Release cadence is monthly and delayed; signal availability must use the actual dated Treasury release, not observation month. Historical release archive must be used for point-in-time backtests; current revised/download files alone are not sufficient to prove what was known at earlier dates.

Evidence:
- Securities A file inventory and February 2023 start: https://home.treasury.gov/data/treasury-international-capital-tic-system-home-page/tic-forms-instructions/securities-a-us-transactions-with-foreign-residents-in-long-term-securities
- Structural break and attribution change notice: same page, notices dated 2023-03-15 and 2023-03-31.
- TIC data scope and timing: https://home.treasury.gov/data/treasury-international-capital-tic-system-home-page/frequently-asked-questions-regarding/ticfaq2
- Monthly release archive: https://home.treasury.gov/archives-of-tic-monthly-data-releases

Status:
- Official source identity and monthly country-file availability: VERIFIED.
- Transaction-vs-position classification: VERIFIED as transaction data.
- Feb-2023 structural break and country attribution change: VERIFIED.
- Raw country-file download, byte size, retrieval timestamp, SHA-256: NOT ACQUIRED.
- Schema/field/India-country row audit: PENDING.
- Release-vintage/available_at reconstruction: PENDING.
- India-specific inference: PROHIBITED until independently corroborated.

Next bounded execution task: acquire the two current official monthly country files (HTML/TXT) once, preserve exact raw bytes and SHA-256, then perform schema/period/country/duplicate/missingness checks. Do not re-run H.10 archive discovery, ALFRED calendar enumeration, or already-passed source identity audits unless new contradictory evidence appears.


## Follow-up: official TIC country-file schema and India-row spot-check (2026-11-13)
The two official Treasury tab-delimited files were opened directly from the official Securities A page (content inspection only; raw-byte download/hash not performed in this step):
- Table 1: https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table1.txt
- Table 2: https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table2.txt

Table 1 header exposes country, country_code, date and instrument-specific holdings, net transaction, and valuation-change fields (USD millions). For total U.S. securities the fields include for_lt_total_pos, for_lt_total_net, for_lt_total_valchg; corresponding Treasury, agency, corporate/other bond, and equity fields are also present. The file header says positive net U.S. sales to foreigners denotes an increase in a foreign position. India is present as country_code 42102. The inspected India rows in this file extend through 2026-03 (latest India row seen), with net transaction and valuation change separate. This separation is valuable: do not treat holdings change as transaction flow where the file supplies both.

Table 2 contains U.S. holdings and net U.S. purchases of foreign long-term securities by country of issuer. India country_code 42102 is present and inspected rows extend through 2026-06 (latest India row seen). Its header and definitions must be retained independently from Table 1; never merge Table 1 and Table 2 as though they describe the same direction or resident side.

The files contain later monthly dates for some other countries than the latest India rows found. Do not claim full current-month coverage for India based on the file's global maximum date. India-specific row coverage is currently Table 1 through 2026-03 and Table 2 through 2026-06 in the inspected text response; this is a spot-check, not a complete coverage audit.

Status update:
- Official table1/table2 endpoints and column schemas: VERIFIED at text-preview level.
- India row exists, country code 42102: VERIFIED.
- Latest India row in inspected table1/table2 preview: 2026-03 / 2026-06 respectively (spot-check only).
- Separate net transaction and valuation-change fields in table1: VERIFIED.
- Raw bytes, byte size, retrieval timestamp, SHA-256: NOT ACQUIRED.
- Full-file row counts, all country-period coverage, duplicate/missingness and sign QA: PENDING.
- Table2 full semantic/sign mapping: PENDING.
- No direct India FPI/NSE flow interpretation: remains PROHIBITED.


## Bounded release-calendar gate (2026-11-13)
Treasury's official 2026 release calendar lists the next monthly TIC release for **2026-11-18 at 4:00 p.m. Washington, D.C. time**. The monthly release is scheduled to report data for **September 2026** (the month before last). This is a planned release date, not proof that the release or India observations are already available. Verify the actual press release and archive after publication before acquisition.

Execution rule to avoid repeated work:
1. Do not poll or re-download the same current table1/table2 files before the release solely to seek newer India rows.
2. On/after 2026-11-18, make one bounded check of the official release page and archive; record actual publication timestamp and release vintage.
3. Acquire the two raw text files once per release vintage, preserving bytes and calculating SHA-256 before parsing.
4. Run one consolidated QA pass: schema/header, full country-period coverage, India code 42102 coverage, duplicate keys, missing/nonnumeric values, units, sign semantics, and Table 1/2 direction separation.
5. If release is delayed or India rows remain stale/missing, record UNKNOWN/BLOCKED with exact evidence; do not repeat unchanged discovery or invent observations.
6. Historical backtests must use the release publication timestamp (available_at), not merely the reference month. No production feature admission until raw-byte and full QA gates pass.

Official release calendar: https://home.treasury.gov/data/treasury-international-capital-tic-system/release-dates-of-tic-data
Official monthly archive: https://home.treasury.gov/archives-of-tic-monthly-data-releases
Status: release date / expected reference month VERIFIED from official calendar; November release publication and September 2026 India rows NOT YET VERIFIED; raw bytes/hash and full QA NOT DONE.


## Branch integrity and CI acceptance gate (2026-11-13)
A repository-state check after the duplicate-observation guard commits found:
- Global Capital Rotation PR #20 remains OPEN and DRAFT, head `research/global-capital-rotation-overlay-v1` at `5bcffa040477d3a5850305467f6c6e9446d34a2c`, base `main` at the inspected PR snapshot.
- GitHub reports PR #20 `mergeable=false` and `mergeable_state=dirty`.
- Branch comparison reports `main` vs overlay branch as `diverged`, overlay branch 107 commits ahead and 18 commits behind; merge base `1b61bea4cfbadc456775fdfb626f7788f1bd36fb`.
- The newest known successful overlay test run is `43204879661`, for older head `7bc769b002c9c4bb26aa3bb464888e962944e580`. No completed workflow run or check status was found for the newer duplicate-guard head `5bcffa040477d3a5850305467f6c6e9446d34a2c`; commit status currently reports pending with zero statuses. Therefore the new duplicate regression test is committed but NOT runtime-verified.

Required resolution before any merge consideration:
1. Reconcile the 18 commits on `main` with the overlay branch using a non-force, reviewed integration strategy; preserve all branch history and unrelated research artifacts.
2. Re-run the bounded `global_capital_rotation_overlay_tests.yml` workflow against the reconciled PR head; require success and inspect test logs.
3. Re-fetch PR mergeability and verify changed-file scope; do not merge without explicit owner approval.

No branch rebase, force-push, PR retarget, or merge was performed in this audit. This is an acceptance blocker, not a claim that the source code itself has a merge conflict in every file. Keep the PR draft and production integration prohibited until the gates pass.


## Duplicate-guard exception-path correction (2026-11-13)
A follow-up code inspection found the first duplicate-key guard raised `ValueError` inside a parsing `try` block whose broad `except ValueError` converted it into the generic invalid-row error. The regression test expected the specific duplicate-key message, so the original implementation would not satisfy that assertion. Corrected by moving duplicate-key detection after the date/timestamp/numeric parsing exception handler. The duplicate-specific failure now remains distinguishable and includes the CSV row number.
- Fix commit: `99e374373bc5e21f71aafff9700c039f01da8f74`
- Parser blob: `aad350327cbd68bdff87bca424aad3530450c151`
- The file was re-fetched from the branch and the guard's placement after the parsing exception handler was verified.
- GitHub Actions has not produced a run for this new head at audit time; runtime test status remains UNKNOWN/PENDING, not PASS.


## PR #20 changed-scope reconciliation snapshot (2026-11-13)
Fresh GitHub compare (`main...research/global-capital-rotation-overlay-v1`) and PR metadata were re-read after the parser fix:
- Compare status: `diverged`; `main` head `bae1ee47cea62b145cde090a997e65248f9cc721`; overlay head `5c78fec7d9dc929b660fbdcf97ea0dc6dc4d980a`; merge base `1b61bea4cfbadc456775fdfb626f7788f1bd36fb`.
- Overlay branch is 107 commits ahead and 18 commits behind `main` (107 commits in compare range).
- Compare reports 46 changed paths, all additions relative to merge base. The change set is broader than the overlay: it includes CPI-2024-back reconciliation documents, FBIL reference-rate workflows/data, RBI DBIE/USDINR audits, macro source matrices, and the global-capital-rotation overlay files. Thus PR #20 is not a narrowly scoped overlay-only change set.
- PR #20 remains OPEN and DRAFT, 107 commits, 46 changed files, `mergeable=false`, `mergeable_state=dirty`. No evidence from the compare response establishes that every file has a textual conflict; `dirty` is the current GitHub mergeability state and requires a reviewed reconciliation.
- The overlay's relevant paths in this compare are: `.github/workflows/global_capital_rotation_overlay_tests.yml`, `data/global_capital_rotation/2026-11-07_seed_observations.csv`, `data/global_capital_rotation/2026-11-10_seed_observations.csv`, `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_ACCESS_CONTRACT_20261111.md`, `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md`, `docs/GLOBAL_CAPITAL_ROTATION_OVERLAY_V1.md`, `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md`, `docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md`, `pipeline/global_capital_rotation_overlay.py`, and `qa/test_global_capital_rotation_overlay.py`.
- The latest known successful test run remains `43204879661` on older commit `7bc769b002c9c4bb26aa3bb464888e962944e580`; commit `5c78fec7d9dc929b660fbdcf97ea0dc6dc4d980a` has zero commit statuses and no associated PR workflow run at inspection.

Decision: do not merge PR #20 as currently scoped. A safer next integration path is a separately reviewed, overlay-only candidate branch based on the current `main`, carrying only the ten overlay paths listed above (after confirming each path is absent or reconciling any existing main-branch counterpart), then run its CI. This audit did not create that branch or PR and did not alter PR #20.


## Main-branch path-collision audit for overlay-only extraction (2026-11-13)
The ten proposed overlay paths were checked individually against `main` before creating any candidate branch:

| Path | On `main`? | Finding |
|---|---:|---|
| `.github/workflows/global_capital_rotation_overlay_tests.yml` | No | New path on overlay branch |
| `data/global_capital_rotation/2026-11-07_seed_observations.csv` | No | New path on overlay branch |
| `data/global_capital_rotation/2026-11-10_seed_observations.csv` | No | New path on overlay branch |
| `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_ACCESS_CONTRACT_20261111.md` | No | New path on overlay branch |
| `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md` | Yes | Same path, different blob; main blob `5df9fa2bb3507039c677db554d4cd3d2033307d3`, overlay blob `c89cbda07fe0973f09b26709cfd733e9bf29dc40` |
| `docs/GLOBAL_CAPITAL_ROTATION_OVERLAY_V1.md` | No | New path on overlay branch |
| `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md` | Yes | Identical blob on both branches: `1d37270a01446347c0423213da0ed238ea52c743` |
| `docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md` | No | New path on overlay branch |
| `pipeline/global_capital_rotation_overlay.py` | No | New path on overlay branch |
| `qa/test_global_capital_rotation_overlay.py` | Yes | Same path, different blob; main blob `b65f49329ae639deed900007ea1bc0f9be5f4b60`, overlay blob `95aecafbeb24ee83c878e1b128d322392376276b` |

Decision: **do not create or populate an overlay-only branch yet**. Eight paths are cleanly additive or identical, but the source register and QA test are divergent same-path files. Blindly copying the overlay versions would overwrite main-branch work; keeping main versions could leave the overlay pipeline/test contract inconsistent. These two files require a line-level three-way reconciliation against merge base `1b61bea4cfbadc456775fdfb626f7788f1bd36fb` before extraction. No branch was created and no main-branch file was modified. This is a concrete, verified extraction blocker, not a test failure.
