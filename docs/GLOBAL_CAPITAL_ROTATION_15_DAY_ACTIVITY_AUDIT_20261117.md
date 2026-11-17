# Global Capital Rotation — 15-Day Activity Audit
Audit date: 2026-11-17 (Asia/Kolkata)
Window reviewed: 2026-11-03 through 2026-11-17 inclusive, based on dated repository evidence available in the research branch.
Branch: research/global-capital-rotation-overlay-v1
PR #20: OPEN / UNMERGED. Current PR metadata at audit: created 2026-11-07; updated 2026-11-17; 139 commits; 50 changed files; +3,791 additions; 0 deletions. These are PR totals, not 139 commits or 3,791 lines all necessarily created in this 15-day window.

## Executive correction
The 62.5% figure was the last recorded overall overlay status from 2026-11-12 (5/8 gates). It is stale as a current-day progress measurement and was not recomputed on 2026-11-17. The 2026-11-17 work adds evidence and closes bounded source/methodology checks, but does not yet demonstrate closure of another full overlay acceptance gate. Do not present 62.5% as a freshly audited current percentage.

## Dated work and evidence
### 2026-11-07 to 2026-11-10 — overlay implementation and source-contract work
- PR #20 opened 2026-11-07 as a research-only Global Capital Rotation & Relative-Attraction Overlay V1. Its scope includes provenance-aware parsing, stale/UNKNOWN handling, separate global EM flow vs India FPI/DII categories, FX/rates/oil/volatility/relative-return fields, and policy-event context. It does not modify production logic.
- IMF BOP portfolio-flow extraction specification dated 2026-11-10 was added. It identifies IMF BOP financial-account portfolio transactions as the candidate flow source, distinguishes them from PIP/CPIS positions, specifies metadata-first extraction and full SDMX dimension/vintage handling. No country observation panel or EM aggregate was extracted.
- Official source register dated 2026-11-10 records source identity/frequency and gaps for IMF BOP/PIP, CDSL/NSDL FPI, NSE/SEBI DII, Fed H.10, RBI FX, Treasury yields, EIA Brent, Cboe VIX and India/global total-return benchmarks.

### 2026-11-11 — FBIL live acquisition slice
- Official FBIL endpoint returned HTTP 200 for 2026-10-15 to 2026-10-16; 14 records (7 currency products × 2 dates) were preserved and validated.
- Raw response SHA-256: aeec99630a30d4b5961755c35e05b1e795dec1c39a373e48d95eca5edd165e27; workflow Run ID 42983033561; artifact ID 13837574133; artifact ZIP SHA-256 48340a456b11aa8b3cc7e6133d00dcd92794b08c8460cbe65742cc25986c56f4.
- Eight overlapping USD/GBP/EUR/JPY cells matched FBIL/NSE displays (8/8).
- Freshness probes for 2026-11-05 through 2026-11-11 repeatedly returned an empty JSON array, including after 13:30 IST and after zero-padded date parameters. Cause remains UNKNOWN; do not call this a confirmed outage. No recent observations were imputed.
- Scope boundary: first historical sample acquisition PASS; full historical coverage and daily collection NOT_DONE.

### 2026-11-12 — Fed H.10 historical panel
- Workflow Run ID 43276577238 SUCCESS; artifact ID 13970661965; ZIP SHA-256 a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691.
- 26/26 raw series file hashes verified; 304,510 dated rows; 291,831 numeric observations; 12,679 missing markers retained; date union 1971-01-04 to 2026-11-06.
- 200-session NSE calendar join passed. Point-in-time vintage availability remained UNKNOWN/PENDING.
- The three Fed indices and 23 bilateral FX series are FX/index evidence, not portfolio flow. Fed broad dollar is not ICE DXY.

### 2026-11-13 — Treasury TIC source addition
- U.S. Treasury TIC Securities A monthly country files were added as a candidate transaction/flow source, distinct from holdings/positions and FX indices.
- The post-February-2023 SLT series has a structural break and changed country-attribution semantics. India rows and table schema were spot-checked from official tab-delimited files, with transaction and valuation-change fields kept separate.
- Raw country-file byte capture, SHA-256, complete schema QA and release-vintage reconstruction remained pending. TIC is U.S.-centric and cannot prove direct India FPI.

### 2026-11-15 — H.10 artifact and broad-dollar revalidation
- Existing H.10 artifact was downloaded and independently revalidated: 26/26 raw series files and both derived panels matched manifest sizes/hashes.
- Fed DTWEXBGS 20-interval change calculated as +0.3568637816% over valid observations 2026-10-08 to 2026-11-06. This is the Fed Nominal Broad U.S. Dollar Index, not ICE DXY and not a portfolio-flow series.
- This is a derived FX indicator, not proof of global capital rotation.

### 2026-11-17 — H.10/FRED methodology and raw-capture investigation
- Current H.10 release dated 2026-11-16 and official review metadata were checked; the Broad Dollar Index is listed through 2026-11-13 with 5,445 observations.
- Five displayed overlapping dates between H.10 JRXWTFB_N.B and FRED DTWEXBGS matched exactly (5/5), including the missing 2026-11-11 observation.
- Federal Reserve methodology explains the 2019 re-indexing: Jan-2006 monthly average = 100, Broad factor 1.014163. The H.10 Preview's 1997=100 unit label remains stale/inconsistent; preserve that metadata conflict. Do not apply the 2019 factor twice.
- Official DDP-to-FRED crosswalk route and column schema were identified, but the exact row mapping JRXWTFB_N.B -> DTWEXBGS was not extracted from the CSV. Candidate remains provisional; no registry promotion.
- H.10 XML ZIP and FRED public CSV full-history endpoints were identified. Byte downloads failed in the available runtime; no new raw bytes, hashes or full-history reconciliation were produced. These are tool acquisition failures, not proof the official sources are broken.
- H.10 raw capture #8 (Run 44036104490) and its existing SHA-256 remain the prior verified capture; 5,231 valid observations and 214 ND rows excluded. Regression workflow #232 / Run 44036012995 had 72 tests PASS. A prior 20-valid-interval result of +0.8892047581% remains research-only and is not a new raw acquisition.

### 2026-11-17 — BCB extraction code and India flow semantics
- Added `scripts/research/extract_bcb_domestic_portfolio_release_vintage.py` to extract domestic-market portfolio investment rows and headers from two existing BCB release workbooks (202601 and 202603), retaining input byte counts and SHA-256 in the generated QA JSON. The script was inspected in the repository; this audit did not establish a successful execution or a new output artifact. Do not claim BCB extraction completed from script presence alone.
- Added `docs/GLOBAL_CAPITAL_ROTATION_INDIA_FPI_DII_SEMANTICS_CHECKPOINT_20261117.md` (commit 66271d77c685f348943af804945ec1e9e3f65684). CDSL displayed 16-Nov-2026 category arithmetic reconciled: FPI categories subtotal +₹4,845.93 crore; separately shown Mutual Funds -₹18.74 crore; page total +₹4,827.19 crore. The page total is not pure FPI.
- NSE-only and combined NSE+BSE+MSEI remain distinct provisional series; DII is Trading Member/client-category classified, not custodian-confirmed DII. Existing NSE raw CSV URLs/bytes were not acquired.
- Added this activity audit and continuity addendum to the research branch. These are documentation/provenance records, not new raw data ingestion.

## What was actually completed vs not completed
### Bounded PASS / completed evidence
- Overlay code/schema and bounded QA exist in PR #20; PR remains unmerged.
- FBIL 14-row historical sample raw acquisition, hash and scoped validation: PASS.
- Fed H.10 26-series historical panel archive/hash validation and 200-session calendar join: PASS, with vintage caveat.
- H.10 current broad-dollar displayed five-date FRED comparison: 5/5 match; 2019 re-indexing methodology explanation found.
- CDSL 16-Nov displayed arithmetic reconciliation: PASS (displayed values only).
- Source semantics for Treasury TIC, IMF BOP vs PIP, CDSL vs NSE and broad USD index were clarified and documented.

### Still NOT_DONE / UNKNOWN / BLOCKED
- IMF BOP raw DSD/codelists plus country-level portfolio transaction extraction and defensible EM aggregate.
- CDSL raw archive bytes and immutable hash for the new 16-Nov data; full historical daily CDSL panel.
- NSE-only and combined NSE+BSE+MSEI raw CSV downloads, SHA-256 and parsed historical DII panel.
- Matched CDSL/NSE FPI/DII panel with reporting lag and provisional-vs-custodian status.
- Treasury TIC raw country-file archive/hash, full schema/India QA and release-vintage reconstruction.
- H.10/FRED full-history raw byte acquisition and date-by-date reconciliation; exact official DDP/FRED crosswalk row extraction; revision-vintage archive.
- Synchronized USD/INR, yields, oil, volatility, India-vs-World/EM total-return panel.
- Sector-to-stock exposure bridge and matured event-study/predictive validation.
- Production integration: NOT_AUTHORIZED.

## Progress percentage correction
- Last recorded overall overlay status: 62.5% (5/8) as of 2026-11-12.
- As of 2026-11-17, no complete new major acceptance gate has been demonstrated by this activity audit. Some source sub-gates have progressed, but the full 8-gate denominator and weights were not re-audited.
- Therefore current overall percentage: NOT_RECALCULATED / NOT_VERIFIED. 62.5% must be labelled historical last-recorded value, not current measured progress.
- Do not report 100% for the overlay or infer 75% merely by counting new documents or commits.

## Next highest-value work
1. Execute BCB domestic portfolio vintage extractor against the two pinned raw workbooks; independently inspect output and hashes, then commit the QA artifact only if it actually exists and validates.
2. Acquire CDSL raw daily/archive bytes and both NSE CSV scopes using a real browser-capable or verified official export route; never guess endpoints.
3. Complete independent source-level QA, then construct a lag-aware matched India FPI/DII panel.
4. Acquire IMF BOP DSD/codelists and actual transaction observations; derive EM aggregate only after country coverage, instrument, sign and vintage rules pass.
5. Finish H.10/FRED byte capture, exact crosswalk row and full-history reconciliation using a byte-capable runner.
6. Recalculate all eight overlay acceptance gates from evidence; publish a new percentage only after this reconciliation.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A-E and Hard Gate unchanged. No synthetic observations, fabricated timestamps/hashes, forward-fill, paid APIs, external contact, stock ranking, buy/sell instruction or automatic trading. ₹0 research spend. UNKNOWN never PASS.