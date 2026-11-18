# Independent Evidence Closure Checkpoint — Brazil + Global Capital Rotation
Date: 2026-11-19 (Asia/Kolkata)
Scope: read-only evidence reconciliation plus one bounded trigger; no production change.

## Executive decision
- Brazil Reconstruction: INCOMPLETE / BLOCKED.
- Global Capital Rotation & Relative-Attraction Overlay: INCOMPLETE / BLOCKED.
- This checkpoint is not a completion claim and assigns no overall percentage.
- ₹0; official/free sources only. UNKNOWN is not PASS.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged. No PR merge, production integration, macro weights, or trading admission.

## Brazil — evidence reused and current gap
### Confirmed
- Current IMF registration listing displays IMF:BOP6(1.0), provider IMF:BR1, and the BCB URL, last updated 2026-10-26T11:47:29Z. This is current-state evidence, not an original registration timestamp.
- Part-13 archived three official IMF structure responses and confirmed PA URN IMF:BR_BOP_BP6(1.0), PA -> Dataflow IMF:BOP6(1.0), PA -> Provider IMF:BR1.
- BCB payload declares IMF:BOP_BPM6(1.0). Distinct Dataflow identifiers remain a confirmed unresolved mismatch; shared DSD is not equivalence.
- Prior compatibility counts: BOP6 234/237 (98.7342%); BOP_BPM6 27/237 (11.3924%).
- Prior RSS raw capture run 44301482210: 33 items, 30,110 bytes, SHA-256 8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2. BCB raw capture: 4,840,062 bytes, SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c. Do not repeat these captures without a new reason.
- Parser offline QA run 44372942179 completed SUCCESS; job parser-qa completed. This is fixture/negative-control QA, not real transaction evidence or historical reconstruction.

### Remaining Brazil blockers
1. Brazil-specific historical registration event rows with actual transaction timestamps/actions.
2. Provision Agreement revision/changelog evidence and link to the exact registered BCB URL.
3. Complete Create/Replace/Delete/Append/Information/Re-register event chronology (do not map action names to lifecycle semantics without official schema/transaction semantics).
4. Reconciliation of each event's PA URN, Dataflow, Provider and Data URL to current registry row and BCB payload.
5. Official raw SDMX 2.1 XSD bytes and hashes; pinned third-party schema mirror is not an official-byte substitute.
6. Real Brazil transaction fixture validation; parser local tests alone are insufficient.

### Resolver trigger and operational state
- Updated only scripts/research/imf_transaction_resolver_trigger.txt to trigger the existing read-only 33-link resolver; commit f70161722899d40a13d6739d7ba875af61e1cde4.
- Workflow run 44376631635, run #2, workflow .github/workflows/imf_registry_transaction_resolver.yml, completed SUCCESS. Job `resolve-transactions` completed all steps. Artifact ID 14460348753, 29,627 bytes, ZIP SHA-256 `ec69e759db1ba45a1d5ca81f4c29daf6420dea453321339eb591d6236b1ff5c2`.
- Artifact contains 33 transaction XML files plus `transaction_resolution.json`. Independent local inspection/recomputation: 33/33 HTTP 200, 33/33 XML parse PASS, 33 QueryRegistrationResponse documents, 33 Registration records, 33 distinct PA URNs and 33 distinct Data URLs, zero Brazil `IMF:BR1`/BCB URL markers. Machine summary says `NO_BRAZIL_REGISTRATION_MATCH_IN_THIS_33_TRANSACTION_WINDOW`.
- Critical semantic limit: each returned payload is a `QueryRegistrationResponse` containing a current Registration snapshot, not a `SubmitRegistrationRequest` historical event. `Registration/@lastUpdated` is not proven to be the transaction timestamp. Therefore this closes only the bounded 33-item sample as “no Brazil match”; it does not close Brazil chronology, PA changelog or mismatch.
- Resolver scope is only the archived 33 RSS links. Even a clean 33/33 result cannot establish the full historical Brazil chronology; it only closes that bounded window.
- The IMF Data Registrations history UI and SDMX Transactions UI expose relevant fields/download controls, but browser/static extraction does not reveal Brazil-specific event rows. The owner must export actual Brazil-filtered rows, PA changelog and transaction XML/CSV if the UI requires an authorized session. No credentials or cookies should be shared.

## Global Capital Rotation — verified source routes and gaps
### Official source evidence
- IMF Data APIs support SDMX 2.1 and 3.0; Swagger explorer requires beta portal sign-in. The IMF BOP extraction spec remains a metadata/extraction contract only; no country observation panel has been accepted.
- IMF BOP portfolio transactions must be kept separate from PIP/CPIS positions. No EM total is valid until the DSD, codelists, transaction dimension, instruments, asset/liability entries, units, BPM basis, membership edition, currency conversion, period alignment, reporter coverage and vintage policy are validated.
- U.S. Treasury official XML endpoint supports all-history pagination: start at page=0, increment until no <entry>; daily nominal par yield begins 1990 and real par yield 2003. This is a qualified retrieval contract, not an acquired raw archive in this checkpoint.
- Federal Reserve H.10 current release (2026-11-16) and FRED DTWEXBGS provide daily broad dollar index on Jan-2006=100 basis. FRED table currently reports range 2006-01-02 to 2026-11-13 and last updated 2026-11-16. Keep this distinct from ICE DXY. Full H.10/FRED byte-level overlap, vintages and pre/post-2019 reconciliation remain incomplete.
- RBI Reference Rate Archive supports date-range search and Excel download. Reference rate must not be mixed with DBIE interbank OHLC or spot.
- EIA RBRTED is Europe Brent Spot Price FOB, not futures settlement. Missing days remain missing.
- Existing source register identifies CDSL/NSDL/SEBI FPI, DII, Cboe VIX, NSE/NSE Indices TRI and company disclosures, but live synchronized historical panel, global benchmark TRI, and sector/company bridge are not accepted.

### Remaining GCR blockers
1. Raw IMF BOP DSD 2.6.0 XML/codelists/dataflow and country transaction observations; no guessed SDMX keys.
2. Versioned EM membership/coverage and currency/aggregation methodology; no synthetic or partial EM aggregate.
3. Complete synchronized daily series with retrieval metadata, source timestamps, raw bytes, SHA-256, units, vintages and missingness.
4. Resolve H.10/FRED full-history equivalence and vintage behaviour; no source promotion on five-point preview match.
5. Official global total-return benchmark panel with matched dates/currencies.
6. Relative-attraction formula specification, deterministic calculations, no-lookahead and missing/stale gates.
7. India sector transmission and company beneficiary evidence with point-in-time disclosures.
8. Rolling out-of-sample event study/backtest with matured observations, transaction costs, drawdown, false positives, missed winners and ablation.
9. 35-factor registry closure: route discovery is not raw ingestion, predictive edge or production readiness.


## Treasury macro acquisition implementation added in this checkpoint
- Isolated research-only capture script: `scripts/research/capture_treasury_yield_history.py`; commit `4d623ea845e5a5bb5d7fc353f512e43c038a961a`.
- Dedicated workflow: `.github/workflows/treasury_macro_history_capture.yml`, manual/push-marker only, 8-minute timeout; commit `7164243e130e198821878f56e27b43eea2e4c33d`.
- NSE collector `paths-ignore` updated before trigger to exclude the new Treasury workflow/script/marker; commit `f62853f7c61ca1950f4ff8a2a92060b04b6dbad9`. This prevents the full NSE production research workflow from being started by the macro capture.
- Trigger commit `4d550c6cc936b6bf046ba13282f01a914e312c70`; Treasury run #1 / ID `44376975144`, currently observed IN_PROGRESS at checkout/setup stage. No Treasury raw files, manifest, or artifact are yet verified; do not claim acquisition PASS until artifact inspection.
- Workflow source contract: two official Treasury feeds (daily nominal par yield and daily real par yield), all-history pagination starts at page 0 and terminates only on an explicit empty-entry page; raw XML pages, HTTP metadata, timestamps, byte counts, SHA-256, normalized CSV, and manifest are uploaded together. No missing-value fill or production promotion.

## Independent reproducibility acceptance package
For every source and derived output, require:
- immutable raw response/file, canonical source URL, retrieval UTC timestamp, HTTP status/content-type/final URL, byte count, SHA-256;
- dataset/series/dataflow/DSD version, units, frequency, as_of_date, published_at, release/vintage and observation flags;
- parser/transform code commit, runtime and dependency versions;
- deterministic machine-readable output, schema, row counts, duplicate/missingness checks and independent validator;
- formula definitions, test vectors, reconciliation samples and no-lookahead assertions;
- artifact ID, workflow run ID, commit SHA and reproducible command;
- explicit PASS / PARTIAL / BLOCKED / UNKNOWN / NOT_DONE with no inferred PASS.

## Immediate next actions
1. Resolve/inspect run 44376631635 terminal state and artifact; if it is stuck beyond the 8-minute timeout, record failure and fix the workflow runner/trigger rather than rerunning blindly.
2. Obtain owner-exported IMF:BR1 registration history rows, exact PA changelog and transaction XML/CSV; no passwords/cookies.
3. Treasury nominal+real acquisition and independent raw-to-CSV reconciliation are now complete for run 44376975144; next add a committed reusable validator and retain artifact/manifest references.
4. Retrieve and archive public H.10 XML ZIP and FRED DTWEXBGS CSV via a byte-capable runner; full date-by-date comparison.
5. Parse IMF BOP DSD/codelists before any observation key is formed; if the public observation endpoint requires authenticated beta portal access, keep that gate BLOCKED rather than inventing a route.
6. Only after raw panels pass, proceed to formula, sector bridge and rolling event study.

## Official sources
- IMF registrations: https://sdmxcentral.imf.org/data/registrations.html
- IMF historical registration activity: https://sdmxcentral.imf.org/activity/data-log.html
- IMF SDMX transactions: https://sdmxcentral.imf.org/activity/activity-log.html
- IMF Provision Agreements: https://sdmxcentral.imf.org/data/provisionAgreements.html
- IMF API documentation: https://data.imf.org/en/Resource-Pages/IMF-API
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Treasury XML feed: https://home.treasury.gov/treasury-daily-interest-rate-xml-feed
- Treasury XML pagination notice: https://home.treasury.gov/developer-notice-xml-changes
- Federal Reserve H.10 current release: https://www.federalreserve.gov/releases/h10/current/default.htm
- FRED DTWEXBGS: https://fred.stlouisfed.org/data/DTWEXBGS
- RBI Reference Rate Archive: https://rbi.org.in/scripts/ReferenceRateArchive.aspx
- EIA Brent RBRTED: https://www.eia.gov/dnav/pet/hist/RBRTED.htm

## No-change statement
No production code, selector, ranking score, pressure fade, CORE-672, Engines A-E, macro weights, or trading admission changed. No paid source, synthetic observation, inferred timestamp, guessed transaction ID, or undocumented endpoint used.


## Treasury artifact independent audit — 2026-11-19
- Run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44376975144 (completed SUCCESS); artifact ID 14462186283; artifact digest / ZIP SHA-256: aedf0578d96539b2a70c3222fc7b84355a92f6f4d20d9c61b3469c603005ce9c.
- Independent ZIP inspection confirmed raw page hashes and byte counts match the manifest, all HTTP statuses are 200, XML pages parse, and pagination terminates only at empty feeds.
- Nominal: 32 pages including empty terminator (31 populated), 9,226 raw observations and 9,226 CSV rows, 1990-01-02 through 2026-11-17, zero duplicate dates, exact raw-to-CSV date/value match. CSV SHA-256 94678bc88b52ad5ed8e260cf3a16f407de882bd17f7f3a212c00c054530ff4cf.
- Real: 21 pages including empty terminator (20 populated), 5,973 raw observations and 5,973 CSV rows, 2003-01-02 through 2026-11-17, zero duplicate dates, exact raw-to-CSV date/value match. CSV SHA-256 9851ca6ca08e758d73d0188a08f9958f7eb97ab960ee9da8e3e5978db9fb662a.
- No interpolation/fill was applied; blank source cells remain blank. This is a bounded PASS for the Treasury capture and its normalization only.

## New official BOP structure route discovered
- SDMx Global Registry's official BOP package page states BOP DSD V2.6.0 (published December 2025), IMF maintenance agency, downloadable in SDMx-ML 2.1 and 3.0 without authentication; registry stores related codelists, dataflows and constraints: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/ .
- The IMF SDMX Central legacy registration listing still displays IMF:BOP6(1.0) for IMF:BR1; BCB XML declares IMF:BOP_BPM6(1.0). New BOP DSD V2.6.0 must be versioned and compared, not treated as an automatic fix or as identical to the legacy dataflow/PA. Exact DSD + codelist + constraint archive and schema compatibility are still NOT_DONE.
- Official structure docs explain DSD components/codelists and dataflow/provision-agreement constraints; web-service entry point is https://sdmxcentral.imf.org/sdmx/v2/ . No guessed observation query key has been used.
