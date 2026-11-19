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

- Reusable independent validator added at `scripts/research/validate_treasury_yield_artifact.py` (standard-library only; ZIP integrity, raw page hashes/bytes/status, Atom entries, empty terminator, raw-vs-CSV dates/values, CSV hashes and duplicates); commit `f98449bc9f893521a2e9c971950a9933d9f1449f`.


## Brazil public API probe — 2026-11-19: first independent findings
- Run 44463995841 / commit 43b40e489bd9d007b06091127a6017bc07ce2f40 completed SUCCESS. Artifact 14500384474; ZIP SHA-256 `1ae0dcb1dcf51f0aa9a66f306088dbbc58318fb15322dbb7cef23690e14c6db1`.
- Public endpoint `GET /ws/registry/tx/history?urn=<PA-URN>` returned one row: transaction ID 2, Action Replace, Type Structure Submission, epoch-ms 1695371169491 = 2023-09-22T08:26:09.491Z. This is a structure-submission event, not itself a registration event and not a complete PA lifecycle.
- Exact PA structure endpoint returned HTTP 200, 42,886,195 bytes, SHA-256 `f9688024c3906aed8496ff2444af1405d2c9be84752decb0bacee0571fb11a7a`. The PA object is `IMF:BR_BOP_BP6(1.0)`, name “Brazil Balance of Payments”, Dataflow ref `IMF:BOP6(1.0)`, Data Provider ref `IMF:DATA_PROVIDERS(1.0).BR1`. Provider scheme identifies BR1 as “Central Bank of Brazil”. This confirms current PA linkage, not historical registration event linkage.
- A second run (44464529697 / commit 6ceb3098dd33c9c04441d24406525dfee82ae0d2) completed SUCCESS. Artifact 14501493024; ZIP SHA-256 `7209bc5523ef19f15fc5e019d6f30f42d875fa9a6f97468fd81a6f9e6454f7d8`.
- PA history and linked Dataflow history both returned the same single event ID 2 / Replace / Structure Submission / 2023-09-22T08:26:09.491Z. Provider BR1 history returned empty list (HTTP 200).
- Global `searchTransactions` query for 2023-09-01 through 2023-09-30 with max=1000 returned exactly 1,000 records, IDs 1–1000, timestamp range 2023-09-22T08:17:24.983Z through 2023-09-28T17:00:10.774Z. Counts: 906 Registration, 8 Registration Query, 6 Structure Submission, 80 with no Type field; actions: 992 Replace, 8 Delete. Because the result hit max=1000 and does not cover the requested date window fully, this is a truncated sample, not an exhaustive month. It demonstrates a much larger registration transaction cluster on 2023-09-22 than the earlier RSS window.
- Retrieval of txId=2 full payload returned HTTP 500 body “Unable to return transaction for id '2'”; PA-item transaction ZIP route returned HTTP 400 HTML. Therefore transaction content retrieval for ID 2 is not yet verified. These are endpoint outcomes, not evidence that the event did not occur.
- The first probe manifest archived Set-Cookie response headers. Treat that artifact as evidence only; do not copy/use its cookie. The revised probe script explicitly strips Set-Cookie and authentication-related headers before archiving.
- FMR Transaction Web Service public documentation specifies `/ws/registry/tx/searchTransactions` filters (dateFrom/dateTo in epoch ms, max, orderDesc), `/ws/registry/tx/history?urn=`, and `/ws/registry/tx/transactions?txId=`. It describes transaction IDs as atomic registry changes and includes data registrations. Official docs: https://fmrwiki.sdmx.io/11.25.4/rest-api/special-purpose/TransactionWebService/ and https://fmrwiki.sdmx.io/12.5.0/rest-api/special-purpose/TransactionWebService/ .
- Next bounded probe run 44464638286 is intended to test transaction payload IDs 3–12, which the September transaction index classifies as Registration. Status must be checked before any result claim.


## Early transaction payload spot-check — 2026-11-19
- Run 44464638286 / commit d2a27951dad6f1022382695841a752c51a9cc4fa completed SUCCESS; artifact 14501826326; ZIP SHA-256 `ac8b5d1ffd2d2db7af3d207514924add3fa7d12e4c3eca4f36c0ae86d8cb781f`.
- Exact payloads for transaction IDs 3–12 all returned HTTP 200 and parsed as SDMX 3.0 `RegistryInterface` containing `QueryRegistrationResponse` snapshots. Independent inspection confirms IDs 3–12 relate to Switzerland, Finland, Italy, Sweden and Canada; none is Brazil. Examples: ID 3 PA `IMF:CH_PPI(1.0)`, URL `https://nsdp.admin.ch/variable/64.xml`; ID 9 PA `IMF:SE_BOP(1.0)`, URL `https://share.scb.se/AA0102/data/ECOFIN_BOP6_Q_SE1.xml`. These are current registration snapshots, not historical SubmitRegistrationRequest payloads.
- The September 2023 index is capped at 1,000 items, so ID 3–12 is only a spot-check and cannot establish Brazil absence. Next use the documented Transaction Collection API, which exposes each transaction's affected URNs (del/ins/upd), to filter for the Brazil PA and linked Dataflow before downloading any more individual transactions.
- Next run 44464760170 probes `GET /ws/registry/transactions?updatedAfter=1693526400000`, `GET /ws/registry/transactions/3`, and the Fusion-JSON variant for txId 3. Status and content must be inspected before relying on this newer API; IMF deployment version may differ from current FMR documentation.


## IMF API compatibility finding — 2026-11-19
- Run 44464760170 / commit ad14695bc0571f4463b8dbea8fa192d88f6678bf completed SUCCESS. Artifact 14501617039; ZIP SHA-256 `9c30a8abbee2437332b47674810df531a87f461fa49e5c1599425803272975c6`.
- IMF SDMX Central's live overview reports Fusion Metadata Registry version 11.24.0. The newer FMR Transaction Collection endpoints `/ws/registry/transactions` and `/ws/registry/transactions/3` returned HTTP 404 with HTML response bodies (94,303 bytes); this API is not available at the IMF deployment route tested. Do not use this endpoint for this project.
- The legacy endpoint `/ws/registry/tx/transactions?txId=3&format=fusion-json` returned HTTP 200 and a parseable Fusion-JSON registration object. It exposes Registration URN, Registration lastUpdated, data URL and exact Provision Agreement reference. TX 3 was Switzerland PA `IMF:CH_PPI(1.0)`, not Brazil. This is a usable method for identifying target registration objects by exact PA URN, provided the returned content is treated as the transaction's registration snapshot and event timestamp comes from the transaction index, not `lastUpdated`.
- A bounded parallel batch scanner has been added: `scripts/research/probe_imf_brazil_registration_batch.py`, standard-library only, max batch 200, concurrency 12, archives each raw response with URL, UTC retrieval time, status, safe headers, byte count, SHA-256, parse status, Registration URN, PA reference, Data URL and lastUpdated. It emits JSON/CSV index and exact Brazil PA matches. Commit `0e750c03cdf8d6795cb9b99593e405b9064fc5b8`.
- Workflow updated to 8-minute timeout and run batch IDs 13–112, commit `8216a9afbf7f53e7c1e0a89fab48aea0928e099d`; NSE collector paths-ignore includes the batch script, commit `f9b9f0aa4d94ce255ded32d4383078cfd7b6dd84`. An intermediate YAML quoting error caused several workflow parse failures and an accidental NSE collector run; cancellation workflow completed SUCCESS (run 44464967535) and was instructed to cancel run 44464895192. These failed parse attempts are NOT evidence of a data failure. The workflow YAML and ignore paths were corrected before retry.
- Retry run 44465053880 is the first valid batch execution after the YAML fix. Do not mark batch complete until its artifact is inspected.


## Brazil registration transaction batch 13–112 — 2026-11-19
- Run 44465053880 completed SUCCESS; artifact 14500984210; ZIP SHA-256 `3ca1f37953d403c7368783c6db73816522e37120b59a5f01d872769ca4077b89`.
- Independent ZIP inspection: 100/100 transaction responses HTTP 200; 100/100 Fusion-JSON parse PASS; 100 Registration objects extracted; 0 exact matches to target PA `IMF:BR_BOP_BP6(1.0)`; zero non-200 or parse failures.
- Each record includes transaction ID, registration URN/ID, PA reference, data URL and Registration.lastUpdated; raw JSON bytes, URL, UTC retrieval time, status, safe headers, byte count and SHA-256 are preserved. The summary expressly limits scope to transaction IDs 13–112.
- The 100 records are not a random sample; they are the next contiguous ID block after IDs 3–12. Zero matches does not imply Brazil is absent from later IDs. Continue sequential batches until the complete target date-window transaction index has been covered, or until a direct exact match is found.


## Brazil registration transaction batch 113–212 — 2026-11-19
- Run 44465172878 completed SUCCESS; artifact 14500864958; ZIP SHA-256 `d414cd94594b5e20ae7b0233a6e9420c832f993da18cd3f81cf11b304f536fc1`.
- Independent ZIP inspection: 100/100 HTTP 200; 100/100 Fusion-JSON parse PASS; 100 Registration objects; 0 target PA matches; no failed requests or parse errors. All 100 PA references are distinct; none equals `IMF:BR_BOP_BP6(1.0)`.
- This is a contiguous ID block and only a bounded negative result. It does not establish that Brazil is absent from transaction IDs above 212.


## Brazil registration transaction batch 213–412 — 2026-11-19
- Run 44465302480 completed SUCCESS; artifact 14502051707; ZIP SHA-256 `1d4e6caa2667d5e1d777e4f76be18b7e692581497bb7e8d1732ab4c00383a4a8`.
- Independent ZIP inspection: 200/200 HTTP 200; 200/200 Fusion-JSON parse PASS; 200 Registration objects; zero exact matches to target Brazil PA; no non-200 or parse failures.
- Cumulative contiguous transaction-ID scan 13–412: 400/400 Registration snapshots inspected; 0 exact target PA matches. Still not exhaustive for the September transaction index because IDs 413 onward remain uninspected.


## Brazil registration transaction batch 413–612 — 2026-11-19
- Run 44465408909 completed SUCCESS; artifact 14501124987; ZIP SHA-256 `11d864620e92b0c50bd9c8ffb470926bb8fbf8c856bd4afd23c5764291902516`.
- Independent ZIP inspection: 200/200 HTTP 200; 200/200 Fusion-JSON parse PASS; 200 Registration objects; 0 exact matches to target Brazil PA; no non-200 or parse failures.
- Cumulative contiguous scan 13–612: 600/600 registration snapshots inspected; zero exact matches. Transaction IDs 613–1000 remain to be inspected; this is still a bounded negative result, not full chronology.


## Exact Brazil registration found and full lifecycle captured — 2026-11-19
### Exact registration identity
- Sequential scan transaction IDs 613–812 located exact Brazil PA match at transaction ID 667.
- Batch run 44465513792 completed SUCCESS; artifact 14502470283; ZIP SHA-256 `2f2fdf7168bc5e6bcc25b378bfa3b5e2e5e20bc42f0d3d4fbda64e3fdc3ad060`.
- Batch result: 200/200 HTTP 200; 200/200 Fusion-JSON parse PASS; 199 Registration objects; one exact target match:
  - Transaction ID 667
  - Transaction timestamp from index: 2023-09-22T09:42:16.389Z
  - Registry Action Replace; Type Registration
  - Registration URN `urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`
  - Registration ID `D429E36CD161E2F2A34ECAF137994E89`
  - PA `IMF:BR_BOP_BP6(1.0)`
  - exact BCB data URL `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`
  - Registration.lastUpdated `2023-09-22T09:42:05` (not the transaction timestamp).
### Original registration payload
- Exact item export `GET /ws/registry/tx/transaction?txId=667&urn=<Registration-URN>` returned HTTP 200 ZIP with one SDMX-ML 2.1 RegistryInterface document containing `SubmitRegistrationsRequest` and `RegistrationRequest action="Information"`. It contains the exact Registration ID, PA reference and BCB URL. This proves original registration payload retrieval for tx667.
- Transaction 667 full transaction endpoint also returned HTTP 200 QueryRegistrationResponse snapshot; keep distinct from the original SubmitRegistrationsRequest ZIP export.
- Registration history for the exact Registration URN returned 40 events, from ID 667 (2023-09-22T09:42:16.389Z) through ID 37877 (2026-10-26T11:47:33.098Z). The endpoint response history SHA-256 is `23fe31fafad2f08bfe63473d4f45792365f92c53f3a27b6158472f0c8e232072`, 2,131 bytes.
### Full lifecycle capture
- Run 44465947951 completed the focused exact registration probe and 40-event transaction item capture. Artifact 14502380926; ZIP SHA-256 `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`.
- Independent inspection: history events 40/40; transaction item ZIP downloads HTTP 200 40/40; embedded XML parse PASS 40/40; Registration ID matches 40/40; PA reference matches 40/40; BCB data URL matches 40/40; failed items [].
- All 40 embedded XMLs are SDMX-ML 2.1 RegistryInterface documents and contain SubmitRegistrationsRequest. The Registry history Action is `Replace` for 40/40, while the embedded SDMX RegistrationRequest action is `Information` for 40/40. These are separate fields from separate layers; no semantic equivalence is assumed. Registration.lastUpdated also remains distinct from the millisecond transaction timestamp.
- History Type field is present as `Registration` for tx667; the field is absent in the other 39 returned history records. Preserve nulls; do not fill the missing Type values.
- All 40 lifecycle events preserve the same Registration ID, PA and BCB URL. This closes the public API-observed lifecycle for this exact Registration URN through the latest returned event (2026-10-26), not the PA's own full structure revision/changelog or the BOP6/BOP_BPM6 mismatch.
- Exact registration structure query `/sdmx/v2/structure/registration/IMF/<id>/1.0` returned HTTP 404 No Results Found; this route is not accepted. Exact transaction item export is the supported evidence path used here.
### Remaining Brazil blockers after lifecycle closure
1. PA structure transaction ID 2 payload/changelog remains unavailable from tested legacy transaction retrieval endpoints (HTTP 500 for full transaction, HTTP 400 for PA item ZIP); current PA history only returns ID 2.
2. Official BOP6(1.0) vs BOP_BPM6(1.0) DSD/dataflow/schema compatibility still unresolved.
3. Official SDMX 2.1 XSD bytes/hashes and actual BCB data payload conformance remain to be independently archived/validated.
4. Need verify whether any older/parallel Brazil Registration URNs exist outside this exact Registration URN. The exact current registration's own 40-event lifecycle is now captured.
