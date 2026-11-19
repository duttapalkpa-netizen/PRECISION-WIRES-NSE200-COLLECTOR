# GCR India FPI Raw Capture and Schema Audit — Continuation 72 (2026-11-19)

## Executive result
- GitHub Actions workflow: **GCR Official India FPI Raw Page Capture**, run #2 / ID `44515445620`, push event, head commit `4bbb1bdc6be289079869a72c4ea79a460ac6b219`, completed SUCCESS.
- Job `capture`: all steps SUCCESS, including GET-only capture and immutable artifact upload.
- Artifact: ID `14524707532`, name `gcr-india-fpi-raw-pages-2`, 184,876 bytes, not expired; GitHub digest `sha256:29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69`.
- Downloaded ZIP SHA-256 independently recomputed as `29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69`: exact match.
- Manifest says 7 sources, 7 HTTP 200, 0 non-200/error. Capture window 2026-11-19 11:30:42.275540Z to 11:30:59.881430Z. Method GET only. No forms submitted.

## Per-source capture evidence
| Source | HTTP | Retrieved UTC | Bytes | SHA-256 |
|---|---:|---|---:|---|
| NSDL Latest | 200 | 11:30:42.275540Z | 58,406 | 1181fb7f6e84e19a7e2ce96178a3f3e63416d811fdc90b260098eb10f9260e8d |
| NSDL Monthly | 200 | 11:30:45.686032Z | 227,853 | aeb94a183015bf8fa4d0b636949e0108381bcfee4db2e57cba7cd8d869f5f9e4 |
| NSDL Archive | 200 | 11:30:49.724826Z | 42,752 | 4a2623171119807524d0c4ac499602db987b59b25599dc9cd61a45c78e76cc9d |
| NSDL Fortnightly selector | 200 | 11:30:52.829076Z | 94,600 | b18ee34fc9477a2c415d12145e7aad61d42eb04eeb4f7f470740f1285cf48d2a |
| CDSL daily eServices | 200 | 11:30:56.848485Z | 38,924 | 2f7c75ed2233a1605784c140b472be34b7ef11dce12606977f8cef8476ba7116 |
| CDSL daily archive | 200 | 11:30:57.643482Z | 297,824 | fc95dc0dade735c9f413ef20a3239e138a6064f2694633aa9635864fd8c7ba2b |
| CDSL fortnightly sector landing | 200 | 11:30:58.927593Z | 191,120 | fd9cc347decc2fa4e6dbb387797c9b07620b8925c2be9ceb9230c634d125282d |

## Schema and freshness observations (raw artifact, not inferred)
1. **NSDL Latest** contains a daily cash investment table headed “Daily Trends in FPI Investments on 19-Nov-2026”, with columns Reporting Date, Debt/Debt-VRR/Equity/Hybrid, Investment Route, gross purchases/sales (Rs crore), net investment (Rs crore), net investment US$ million, and conversion rate. First row is dated 19-Nov-2026. It also explicitly distinguishes provisional exchange-member data on T day from confirmed custodian/depository reports for previous trading day(s). Do not label the 19-Nov row confirmed without source-specific status reconciliation.
2. NSDL Latest also contains a separate derivative table dated 19-Nov-2026; derivative trades/positions are not cash investment flows.
3. **NSDL Monthly** HTML has 331 rows in its first table and 132 rows in its second table. Its heading is dated 19-Nov-2026 but first visible cash and derivative reporting rows are 02-Nov-2026. Treat heading date and row reporting date as separate fields. Do not infer coverage continuity or freshness from heading alone.
4. **NSDL Archive** is an ASP.NET form with date field and hidden ViewState/EventValidation. Initial GET yielded no investment rows. No postback or export was attempted; date selection/export remains NOT_DONE.
5. **NSDL Fortnightly selector** exposes dates beginning 15-Nov-2026, then 31-Oct-2026 and 15-Oct-2026. It is a selector/index, not the sector dataset itself. Historical selector text includes a malformed “Feb 28, 2022” amid 2023 entries; retain as source anomaly, do not silently correct.
6. **CDSL daily eServices** contains daily cash investment rows dated 18-NOV-2026 and a separate derivative table dated 18-NOV-2026. Cash table schema includes asset category, route, gross purchases/sales INR crore, net INR crore, net USD million and conversion. Example first cash row: Equity / Stock Exchange / gross purchases 21,092.53 / gross sales 15,177.67 / net 5,914.86 INR crore / net USD 632.1301 million / conversion 93.5703. This is an observed raw-page value, not independently reconciled against NSDL.
7. **CDSL daily archive** cash investment table's first visible reporting date is 02-11-2026, although its page title says investment data “upto 18-Nov-2026”; the separate derivatives table has 18-NOV-2026. This confirms that the page-level latest date must not be attributed to the cash table. Cash freshness remains stale/partial relative to daily eServices.
8. **CDSL fortnightly sector landing** contains DDP application-pendency tables and navigation/index links; it does not embed the sector-wise investment observations in the captured HTML. It links the 15-Nov-2026 sector page. That separate page must be fetched as its own raw source before sector-flow parsing. The landing also lists older New Format daily XLS files only through 04-Apr-2025 in the captured listing.

## Official source cross-check
- CDSL eServices official indexed page: `https://www.cdslindia.com/eservices/publications/fiidaily`; official search snapshot shows a daily investment table and explains confirmed custodian/depository data, provisional exchange data, RBI reference-rate conversion and coverage. Web source ref `turn900033search0`.
- CDSL archive official indexed page: `https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx`; snapshot heading through 18-Nov-2026 while cash rows start 02-Nov and derivatives show 18-Nov. Ref `turn900033search1`.
- CDSL FPI landing official page: `https://www.cdslindia.com/Publications/ForeignPortInvestor.html`; lists fortnightly sector dates through 15-Nov-2026. Ref `turn900033search2`.
- Search-index snapshots are supplementary evidence only; raw artifact and exact row dates govern this capture.

## Acceptance
- Workflow/job execution: **PASS**.
- Artifact upload and digest match: **PASS**.
- Seven requested landing pages captured with HTTP 200: **PASS**.
- Per-page raw hashes/UTC retrieval provenance: **PASS**.
- Cash-flow schema discovery: **PARTIAL PASS** (CDSL daily + NSDL latest visible; other pages are selectors/archive or mixed freshness).
- Confirmed-vs-provisional status mapping across providers: **PARTIAL / NOT_RECONCILED**.
- Same-date NSDL/CDSL cash flow reconciliation: **NOT_DONE**.
- CDSL sector observation raw page and parsing: **NOT_DONE**.
- NSDL Archive date-select/postback/export: **NOT_DONE**.
- India daily FPI production ingestion: **BLOCKED**.
- GCR synchronized global/India panel, weights/OOS event study: **BLOCKED / NOT_DONE**.
- Brazil PA transaction-2 Changelog and BOP6/BOP_BPM6 identity: unchanged **BLOCKED**; 40/40 Registration lifecycle remains PASS. No Brazil endpoint re-probe in this continuation.

## Next actions
1. Fetch the exact CDSL 15-Nov-2026 fortnightly sector report linked from the landing page using a separate GET-only capture; hash raw bytes and inspect its table schema.
2. Retrieve matched-date cash rows from NSDL and CDSL and reconcile categories/routes/units/conversion only where dates and classifications align. Keep provisional exchange observations separate from confirmed custodian/depository observations.
3. Inspect NSDL Latest table footnotes and available page status markers before assigning confirmed/provisional labels; do not submit archive forms until a read-only route is documented and approved.
4. Continue Brazil only through the official PA UI/owner-side export route; do not repeat the known failing transaction-2 JSON endpoint.
5. Preserve all research-only changes outside production; no change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E.

No synthetic values, no forward-fill, no daily interpolation, no unsupported aliasing, no paid source, no credentials, no production admission. ₹0.
