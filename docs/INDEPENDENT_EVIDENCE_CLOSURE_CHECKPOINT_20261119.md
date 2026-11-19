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


## Full lifecycle cross-check against global transaction index — 2026-11-19
- Run 44466324080 completed SUCCESS; artifact 14501663276; ZIP SHA-256 `3b968f502447b870b1220bafda7ffdf1071f6cfdda9410631c5ec4d3b71f8b33`.
- Public global `searchTransactions?max=50000&orderDesc=false` returned 38,668 records, tx IDs 1–38,668, raw JSON 2,719,795 bytes, SHA-256 `74725cb58eb6d612e67e7af41df870edaa58f81e95b5ba1c4c3713ccb72ae709`.
- Cross-match of the 40 exact Registration-URN history rows against this global index: 40/40 transaction IDs found; 40/40 millisecond timestamps exactly equal; 40/40 Registry Action values exactly equal; no missing IDs and no date/action mismatches.
- Global index Type field is populated as `Registration` for tx667 only among these 40; absent/null for 39. This is preserved as missing/UNKNOWN, not filled from expectation. The embedded original payloads independently parse as SubmitRegistrationsRequest for all 40.
- This provides independent confirmation that the 40 event timestamps/actions are consistent with the global transaction index as captured at retrieval time.


## Brazil PA / BOP structure route probe — 2026-11-19
- Run 44466544327 completed SUCCESS; artifact 14502018034; ZIP SHA-256 `9bee1463dc3db65055e31a374d6f0300a04b42ebbe7b0d38eb48711a9afe29ec`.
- Historical tx2 item retrieval tested for exact PA URN, Dataflow BOP6, DSD ECOFIN_DSD and Provider Scheme IMF:DATA_PROVIDERS(1.0); all four returned HTTP 400 HTML (94,438 bytes each). This does not disprove tx2 history; it establishes the tested item-download route did not return those old structure items.
- Current SDMX v2 structure retrieval succeeded:
  - BOP6 Dataflow: HTTP 200, 43,060,682 bytes, SHA-256 `fdaa5fbb6836469da9e7d87b19c623ef921c93c1ef614b3a4195f4aad5cbe664`.
  - BOP_BPM6 Dataflow: HTTP 200, 42,897,366 bytes, SHA-256 `a1ab2015713003424a2488897030f02686f9a99865fdfb8fc9359b96550de676`.
  - ECOFIN_DSD structure response: HTTP 200, 42,892,145 bytes, SHA-256 `46996db04da7bc764927ec330fe943fcb42e2fdefb92008206e31e9304562f08`.
- Both Dataflow structures reference the same DSD `IMF:ECOFIN_DSD(1.0)`, but their exact Dataflow URNs and names remain distinct: BOP6 = “Balance of Payments (BPM6) for Collection”; BOP_BPM6 = “Balance of Payments -- BPM6”. This confirms the prior accepted interpretation: shared DSD is not Dataflow alias equivalence. The BOP6 structure response also includes the Brazil PA `IMF:BR_BOP_BP6(1.0)` in its referenced structures.
- This re-confirms structure identities only; it does not authorize rewriting the BCB header, substituting Dataflow IDs, or resolving the constraint mismatch. Existing contract reconciliation run 44290101769 / artifact 14420378420 remains the accepted 237-series evidence (234/237 allowed by BOP6 constraint vs 27/237 by BOP_BPM6 constraint).


## Durable GitHub evidence archive added — 2026-11-19
- Human-readable lifecycle report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md`, commit `cb2576201e5e5eab3c2faa0743607c64d150fa6a`.
- 40-event machine-readable CSV: `docs/evidence/IMF_BRAZIL_REGISTRATION_HISTORY_40_EVENTS.csv`, commit `0b490a8373de2f8be2a443bfdd5d150d5f6ef424`.
- Original Brazil SubmitRegistrationsRequest XML for tx667: `docs/evidence/IMF_BRAZIL_REGISTRATION_TX_00667.xml`, commit `b47e74956b899c1ef2402779d61d6dd6c0b1ede3`.
- Full 40 raw transaction ZIP/XML payloads remain in artifact 14502380926 with 90-day retention; the report and compact 40-event index are committed durably to the repository.


## Global Capital Rotation — IMF BOP observation API access boundary (2026-11-19)
- Official IMF BOP dataset page (`IMF.STA:BOP`) exposes an API link; following it without authentication redirects to the IMF API Management sign-in page. IMF API docs state SDMX 2.1/3.0 are supported and Swagger requires a beta portal sign-in. Official references: https://data.imf.org/en/datasets/IMF.STA:BOP and https://data.imf.org/en/Resource-Pages/IMF-API.
- IMF SDMX Central Web Services Guide (May 2025) documents public structure retrieval at `https://sdmxcentral.imf.org/sdmx/v2/` and public validation/transform services, but does not specify an anonymous public BOP observation query endpoint. Do not invent a query key or treat public DSD access as observation access.
- IMF BOP observation extraction remains BLOCKED until a public Download/View Data route is verified or official data are exported by an authorized user. No credentials/cookies requested; CPIS/PIP positions not substituted for BOP flows.
- Detailed source boundary and next steps: `docs/GCR_IMF_BOP_OBSERVATION_ACCESS_BOUNDARY_20261119.md`.


## IMF BOP public release route discovery — 2026-11-19
- Official BOP dataset page exposes API, VIEW DATA and DOWNLOAD controls and confirms annual/quarterly frequency. Static page extraction does not expose direct destinations for View Data/Download; the API control still leads to the documented sign-in boundary. No observation data were downloaded in this step.
- Identified separate official BOPSY dataset `IMF.STA:BOP_AGG`: annual World and Country Group Aggregates; latest page update shows BOPSY Dashboard release 18 Nov 2026 and Explanatory Notes November 2026. Official page: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG.
- IMF states BOPSY country-level data are reported to IMF or obtained from country NSDP (with IMF-counterparty exceptions); World/country-group aggregates other than Euro Area combine reported country data and estimates for nonreporting economies using sources including WEO and External Wealth of Nations; Euro Area data are ECB-reported. Hence BOPSY can be a separate annual macro benchmark, but not a substitute for quarterly country-reported BOP portfolio flow observations or a pure reported-data EM aggregate.
- BOPSY dashboard: https://data.imf.org/en/dashboards/bopsy%20dashboard. November 2026 Explanatory Notes target: https://data.imf.org/-/media/BOPSY-Explanatory-Notes-November-2026.docx (static web extractor did not parse DOCX; not represented as downloaded/validated).
- Status: BOP dataset route discovery PASS; actual direct download URL NOT_RESOLVED; anonymous BOP observations BLOCKED; BOPSY supplementary annual benchmark ELIGIBLE_FOR_SEPARATE_VALIDATION but numeric data ingestion NOT_DONE. Full detailed caveats: `docs/GCR_IMF_BOP_PUBLIC_RELEASE_DISCOVERY_20261119.md`.


## IMF BOP public observation access + validated BRA/IND pilot — 2026-11-19
- Corrected previous API access assumption: official IMF docs say IMF data are available through SDMX 2.1 and 3.0; Swagger explorer requires beta portal sign-in, but the tested public SDMX 3.0 metadata and observation routes work without an API key/cookie. Official BOP dataset page describes Annual and Quarterly frequency. Sources: https://data.imf.org/en/Resource-Pages/IMF-API and https://data.imf.org/en/datasets/IMF.STA%3ABOP.
- Public Dataflow metadata: `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`; DSD SHA-256 `1541c0e65af5801acb86767a183a124537aa4b6a04d2a4e528c23d73d4b2019b`.
- DSD dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY. Code lists independently retrieved: CL_BOP_COUNTRY(1.0.0), CL_BOP_ACCOUNTING_ENTRY(3.3.0), CL_BOP_INDICATOR(10.0.0), CL_UNIT(2.13.0), CL_FREQ(1.2.0).
- Exact series used: indicator `P_F` = Portfolio investment, Total financial assets/liabilities; accounting entries `A_NFA_T` = Assets, Net acquisition of financial assets; `L_NIL_T` = Liabilities, Net incurrence of liabilities; unit USD; quarterly. The first `P_MV` exact-key test returned HTTP 200 with no observations; rejected from this panel. `P_F` was confirmed populated in broad raw country responses, then extracted with exact keys.
- Panel: 4 exact series; BRA assets 47 quarters 2015-Q1–2026-Q3; BRA liabilities 47 same; IND assets 46 quarters 2015-Q1–2026-Q2; IND liabilities 46 same. Total 186 non-empty observations. India 2026-Q3 remains missing; no fill.
- Final validation run 44472944620 / artifact 14504732476 / ZIP size 7,784,894 / ZIP SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- Independent QA: 4/4 HTTP 200; 4/4 CSV parse; 186/186 exact-query vs broad-raw values match; 186/186 raw source attributes preserved in normalized panel; zero duplicate keys; zero missing/mismatched values; all observed quarter sequences contiguous; PASS.
- Normalized CSV SHA-256 `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`; compressed SHA-256 `7de9dd096eb7eae1dde5fbd38bc8d8dd09f07737e108fcfbe6d333c1642ff869`.
- Durable compressed evidence committed:
  - normalized panel `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.csv.gz`, blob `2da01b588eb113931689555608ca5e1f225cf59f`.
  - BRA A_NFA_T raw CSV.gz blob `96b8fbee5c214a40d5c279f579c3e2942c87c89c`.
  - BRA L_NIL_T raw CSV.gz blob `2f7d9aab5b647b8ab997043458e384afd6ff905b`.
  - IND A_NFA_T raw CSV.gz blob `d0fbc5b6f2fc98fa365afc2328ff8aa4e210bbd1`.
  - IND L_NIL_T raw CSV.gz blob `e2b27069e0c489b078332a3a4b5727f0b454449f`.
  - report `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_PART1_20261119.md`; machine summary `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.json`.
- Data interpretation limits: `SCALE=6` and `PRECISION=6` preserved; no rescaling or currency conversion until SCALE semantics are independently resolved. BOP quarterly flows are not daily SEBI FPI/FII flows. Brazil/India are only a pilot, not approved EM universe. Do not aggregate or admit to production.
- Next exact tasks: resolve SCALE semantics; version an approved EM membership list; inspect BOP_AGG as a separate annual aggregate (official IMF says group totals include estimates for non-reporting economies); then expand country panel and validate vintage/missingness. CPIS/IIP positions remain separate from BOP transactions.


## GCR IMF BOP public observations — Part 1, 2026-11-19 (supersedes "BOP observations BLOCKED" as a blanket access statement)
- Critical update: IMF API Swagger explorer sign-in is not the same as public observation access. Direct no-credential SDMX 3.0 data GET at `https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}` returned CSV HTTP 200 and actual observations.
- Run 44472944620 / artifact 14504732476; 7,784,894 bytes; ZIP SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- Dataflow `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`; dimensions COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY, TIME_PERIOD. Exact codelist/concept responses 7/7 HTTP 200 and XML parse PASS.
- Exact quarterly portfolio investment flow pilot uses `P_F`, entries `A_NFA_T` (assets net acquisition) and `L_NIL_T` (liabilities net incurrence), USD, Q, BRA and IND, 2015-Q1..2026-Q3.
- 186 normalized observations; BRA 47 per entry through 2026-Q3; IND 46 per entry through 2026-Q2; no forward fill, no synthetic rows, no rescaling/conversion; all source attributes preserved.
- Independent raw/broad reconciliation: exact query vs broad raw 186/186 values; raw-to-normalized attributes 186/186; 0 duplicates; 0 missing/mismatches; contiguous quarters per series; validator PASS. Normalized panel SHA-256 `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.
- `P_MV` (market value) exact-key test returned 4 empty series. This is an explicit rejected indicator for this BOP flow extraction, not a successful observation test. Use `P_F` as observed flow series.
- Separate public SDMx Global Registry BOP DSD V2.6.0 capture: run 44473409770 / artifact 14505177819 / ZIP SHA-256 `ba2ce640bb3a4c1cf614341103facec5b9b9aea820100fe7e28a3447993576fe`; SDMX 2.1 XML hash `642fa30fa3ee76be08bf2cdcebdef452e38a421355dd3516fe4666d9cce7b122`; SDMX 3.0 XML hash `5296c0fa950d19dea53a5a477a98915bcb14b1cecb673fbac9a0dcc87ebb11a2`; both parse PASS.
- Do not conflate Global Registry `IMF:BOP(2.6.0)` (17 dimensions + time; includes counterpart/sector etc.) with Data Portal `IMF.STA:DSD_BOP(24.0.0)` (5 dimensions + time). No crosswalk, scale conversion, or net-flow calculation made. Data Portal `SCALE=6` preserved; not interpreted as multiplier.
- Report: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_AND_PILOT_PART1_20261119.md`, commit `b719b0a7cb937be75a2eb198631a29471bc76abd`. Continuity ledger updated at commit `a38db33795d0e6b33583796356544ff60c59ea60`.
- Updated decision: IMF BOP public observations access PASS; BRA/IND pilot panel PASS; full EMDE membership mapping/panel NOT_DONE; net flow/aggregation methodology PARTIAL; relative-attraction formula/sector transmission/backtest NOT_DONE. Overall GCR remains INCOMPLETE / NOT_PRODUCTION_READY.


## 2026-11-19 — WEO October 2026 EMDE membership + IMF BOP code crosswalk PASS
- Official WEO October 2026 Entire Dataset workbook acquired directly from IMF: HTTP 200; 5,480,592 bytes; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- Exact authority is workbook sheet `Country Group Composition`, group code `G200`, group name `Emerging Market and Developing Economies`; 154 rows, 154 unique three-letter country codes, no duplicate members.
- Official October 2026 WEO Appendix also acquired HTTP 200; 985,701 bytes; SHA-256 `cd4e2829d7e621d43134728bfc128547f776e909e08ef1d38b837e2d39e5ae2a`.
- IMF BOP codelist `IMF.STA:CL_BOP_COUNTRY(1.0.0)` acquired HTTP 200; 345 codes; raw XML 204,795 bytes; SHA-256 `54647ef3ac6439ecd059fd80a7954c35e447415d53bf41fbee02728e7cfb6bcb`.
- Exact code-ID crosswalk: 154/154 exact matches; 0 unmapped; 0 duplicate WEO codes. No fuzzy name matching or guessed aliases.
- Nauru (NRU) is the only normalized display-name mismatch: WEO label `Nauru, Republic of`, BOP codelist includes `Naoero, Republic of` and `Nauru` among localized names; code NRU matches exactly. Preserve label discrepancy as metadata, not a failed code mapping.
- Run 44474502699 SUCCESS; artifact 14505617102; 6,204,691 bytes; ZIP SHA-256 `3246d18f7ef6a1d74c2a08ddc37a94542fc0d42c14acf14470e0a8d7bb2783bb`; retained until 2027-02-17.
- Durable GitHub files:
  - `docs/evidence/WEO_OCT2026_EMDE_G200_BOP_CODES_154.csv`, commit `a343a0a92840a2dab01e8bdbcaf236b9fe38fd21`.
  - `docs/evidence/WEO_OCT2026_EMDE_G200_CROSSWALK_SUMMARY.json`, commit `d8fdea10445a7b98e987248cf8d5fa37946d3112`.
  - Report `docs/GCR_WEO_OCT2026_EMDE_MEMBERSHIP_CROSSWALK_PART1_20261119.md`, commit `488693924be34c8d8a6bf8a81f5149a6ed2a99ad`.
- Interpretation: this is a WEO October 2026 vintage membership edition; exact code mapping does NOT mean quarterly BOP observations exist for all 154 members. No aggregate is authorized.
- Next: query exact IMF BOP keys for 154 × 2 accounting entries (`A_NFA_T`, `L_NIL_T`) using `P_F`, USD, Q; produce a country/entry/quarter coverage matrix with raw provenance, preserve empty series and missing quarters; resolve SCALE/sign semantics before summing.
- No production selector/ranking/pressure-fade/CORE-672/Engines A–E changes; no synthetic data; UNKNOWN is not PASS.


## GCR IMF BOP — WEO 2026 EMDE full-member panel capture and independent exact sample validation (2026-11-19)
- Official WEO October 2026 workbook raw download HTTP 200; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`. Exact group `G200` membership = 154 unique ISO3 codes.
- IMF BOP country codelist XML HTTP 200; 154/154 membership codes mapped, no unmapped codes; raw SHA-256 `190c0ab3196a85bba890e2fd0cf40eebda654de2eb8e7d1f16c9644572d59f39`.
- Public IMF BOP dataflow `IMF.STA:BOP(21.0.0)` / DSD `IMF.STA:DSD_BOP(24.0.0)`; `P_F`; quarterly 2015-Q1..2026-Q3; entries `A_NFA_T` and `L_NIL_T`; both 154-country multi-value GETs HTTP 200.
- Panel run 44474218174 / artifact 14505862034 / ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`. 4,681 asset obs + 4,618 liability obs = 9,299; unique keys 9,299; duplicates 0; 114 countries with any observations.
- Coverage: 225/308 country-entry pairs (73.05%); 111 countries both legs; 40 countries neither; DZA/ETH assets-only; ZWE liabilities-only. Country coverage is asynchronous, most latest periods 2026-Q2, only two series reach 2026-Q3. No fill/zero substitution/synthetic data/currency conversion/rescaling.
- Independent exact-key sample validation run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`: 24/24 exact queries HTTP 200; 24/24 series PASS; 1,106/1,106 values and all source attributes exact-match the multi-country panel; no missing/mismatches.
- Durable GitHub evidence: `docs/evidence/imf_bop_emde_20261119/`, persistence run 44474596292 SUCCESS, commit `a6eb5865c0a77d6bdaf1c6a3c6925e6e1e69bdf0`. Detailed report `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`, commit `487f7ca6758a105dfe1280e5af8ed5b7b3a0369d`.
- Decision: 154-member panel capture PASS; exact sample cross-check PASS; full EMDE aggregate/net-flow remains BLOCKED/NOT_AUTHORIZED because 43 member country-entry pairs lack at least one required leg and reporting periods are asynchronous. SCALE=6 remains raw/uninterpreted; no net inflow calculation. GCR formula, sector transmission and rolling backtest NOT_DONE.


## IMF BOP public observations and 154-member WEO EMDE panel — 2026-11-19
### Public observation access
- The earlier blanket IMF BOP observation access BLOCKED conclusion is superseded for the tested dataflow/keys: anonymous public SDMX 3.0 GET to `api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}` returned HTTP 200 CSV without key/login/cookies.
- Dataflow `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`; dimensions COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY.
### EMDE panel
- Official WEO October-2026 G200 EMDE membership: 154 unique codes. All 154/154 map to IMF BOP country codelist; no unmatched codes.
- Broad panel capture run 44474218174 / artifact 14505862034; ZIP 5,997,777 bytes; SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- Exact sample validation run 44474458684 / artifact 14505009889; ZIP 26,684 bytes; SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- 9,299 unique observation rows; 0 duplicate keys; 4,681 asset observations across 113 country codes; 4,618 liability observations across 112 country codes; 114/154 countries have any observations; 40/154 have neither entry; 225/308 country-entry combinations have data and 83/308 are empty. 111 countries have both entries; ZWE liabilities-only; DZA and ETH assets-only.
- Exact validation: 12 EMDE countries × 2 entries = 24/24 HTTP 200 and PASS; 1,106/1,106 exact-to-broad matches; no observation/attribute mismatch. This is same-source query-shape reconciliation, not external economic validation.
- Unit dimension returned USD only; all 9,299 observations carry `SCALE=6`; 9,119 have PRECISION=6, 180 blank; STATUS blank for all; blanks preserved. No rescaling or conversion.
- `SCALE` concept resolves via `CS_MASTER_SYSTEM(1.0.2)` to `CL_UNIT_MULT`; code 6 = Millions (10^6). Raw values and scale need national-source/portal reconciliation because mechanically applying the multiplier yields implausible magnitudes for some smaller economies. Therefore economic unit conversion remains BLOCKED; no aggregation.
### Durable GitHub archive
- Panel evidence commit `a6eb5865`; WEO workbook + BOP country codelist raw-source addition commit `79bfbeb3`.
- Report: `docs/GCR_IMF_BOP_EMDE_PORTFOLIO_PANEL_20261119.md`, commit `a55c51b3995307d3a3b644e4f4c067be28cfc299`.
- Access boundary status update: `docs/GCR_IMF_BOP_OBSERVATION_ACCESS_BOUNDARY_20261119.md`, commit `a6522218a64d7c13c21a167c9eafc3f705b1ee94`.
- Evidence folder: `docs/evidence/imf_bop_emde_20261119/`; includes WEO workbook, BOP country codelist XML, membership, coverage matrix, raw two-entry CSVs, normalized panel, 24 exact sample CSVs, validation summary and source receipts.
### Acceptance decision
- Public access and raw data capture: PASS.
- WEO membership to BOP codelist: PASS.
- Internal exact-query reconciliation: PASS.
- Coverage completeness: PARTIAL (40 member countries absent; 83 empty country-entry pairs).
- Scale/unit interpretation: BLOCKED.
- BPM basis/revision-vintage controls: NOT_DONE.
- EMDE aggregation: NOT_DONE.
- Daily swing signal use: NOT_SUITABLE (quarterly/annual source).
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No synthetic data, no paid APIs, UNKNOWN is not PASS.


## IMF BOP SCALE payload reconciliation — India, four quarters (2026-11-19)
- Official RBI Table 197, Standard Presentation of India's BOP as per BPM6, Quarterly, US$ million, published 2026-07-31: https://rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24022. Relevant rows are Portfolio Investment in India and Portfolio Investment by India.
- IMF Data Portal panel run 44474620936 / artifact 14505452613 / ZIP SHA-256 `b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17`; normalized panel SHA-256 `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`.
- India 2024-Q2..2025-Q1, 4 quarters × 2 entries = 8 comparisons. Raw IMF API `OBS_VALUE / 1,000,000` (not ×1,000,000) matches RBI's published US$ million values within integer rounding. `A_NFA_T) is sign-reversed against RBI's Portfolio Investment by India net; `L_NIL_T) matches RBI's Portfolio Investment in India net. Max absolute difference 0.490 USD million; all 8/8 within ±0.5.
- IMF CL_UNIT_MULT(1.0.2) code 6 = Millions; exact route evidence artifact 14505992737 / ZIP SHA-256 `f70981e1511a709526851eee59548ca237f8ac4c9a02c8d0eb1e8c9410b1017e`. The India test shows the Data Portal observation API payload is empirically already in base USD for these series/periods; do not apply the multiplier a second time. This is a payload serialization observation, not a universal rule yet.
- Durable evidence: `docs/evidence/IMF_BOP_IND_SCALE_RECONCILIATION_2024Q2_2025Q1.csv`, commit `39ec6fbb36c409ba3dd108f3433fb5961adcf4d5`; report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_PART1_20261119.md`, commit `d48fae88a376fa9e2097b3c8bfd458cae2f14610`.
- Decision: India-specific scale/sign empirical check PASS; global transform remains PARTIAL pending Brazil and at least two more country benchmarks. Existing Brazil SGS reconciliation has 201/381 monthly mismatches from 2010-01; do not reuse it as a PASS benchmark. No EMDE aggregation or production admission.

## WEO Appendix / full EMDE coverage QA / SCALE metadata update — 2026-11-19
- Official WEO October-2026 Appendix top-level EMDE list = 154 unique; same-vintage workbook G200 = 154 unique ISO3; Appendix-to-workbook match 154/154; 0 unmapped/ambiguous; all 154 ISO3 exist in IMF BOP country codelist. Run 44474629873 / artifact 14506160317 / ZIP SHA-256 acdf014f5f19ba5e0d23dca7a8d57a4b1813b002a3274495d557f0cd05c0fbb1.
- Raw sources and crosswalk are durably archived under docs/evidence/imf_bop_emde_20261119/weo_membership_validation/.
- Latest panel run 44474620936 / artifact 14505452613 / SHA-256 b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17: 9,299 unique observations, 0 duplicate keys.
- Full missingness QA run 44475089564 / artifact 14505623598 / SHA-256 5f24a529aa0d3c918d598faedeb057c39e328ff043f1f1a86fec587fc1fa8cd8: raw-to-normalized 9,299/9,299 exact; 30 attributes, 278,970 cell comparisons, 0 mismatch. 225/308 country-entry pairs have data (73.05%); 83 empty; 111 countries both legs; 3 one-sided; 40 no data; 13 series have internal gaps totalling 71 missing quarters; 4 complete 47-quarter series; only BRA and PAK have both legs through 2026-Q3.
- Coverage report docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md; full detailed tables are on the research branch and the QA artifact. Do not admit a full 154-country aggregate.
- SCALE metadata capture run 44475051442 / artifact 14505852262 / ZIP SHA-256 391981ce19d89d8ccc6377580e33345a9d75adffdc3f4197c4e4c743a66e3cf3: SCALE enumerates CL_UNIT_MULT; code 6 = Millions (10^6). Metadata meaning PASS; numeric conversion BLOCKED until direct IMF portal and official national values reconcile. Raw OBS_VALUE and SCALE remain unchanged.
- Durable main archive persistence run 44475086587 SUCCESS; commit 13bdd96d. Latest reports and ledger commits: coverage c57913487aa3915da0a88c2622a1ab42b649e059; scale 3cd7c4b0eb7de639750ee030cccb1eb50ee8108f; Part-2 report 3fe5d09b034b48b79dfeeb30559ff853f8ea578c; continuity ledger 39d6e9302be899cc93b1bb7cb6ffdad807de2a16.
- Current GCR decision: WEO membership PASS; BOP panel acquisition and raw integrity PASS; coverage PARTIAL; SCALE metadata code meaning PASS but numeric application BLOCKED; net-flow aggregation BLOCKED / NOT_AUTHORIZED; vintage/revision controls, relative-attraction formula, sector transmission and rolling backtest NOT_DONE. Production invariants unchanged.


## IMF BOP SCALE/sign gate — Brazil + India (supersedes India-only / Brazil-pending note)
- Two independent national-source benchmarks now pass for the IMF Data Portal quarterly portfolio-flow series:
  - Brazil BCB SGS 22906 (net acquisition assets) + SGS 22924 (net incurrence liabilities), monthly USD million. Sum three monthly observations per quarter and compare to IMF `OBS_VALUE / 1e6`: 10/10 comparisons pass over 2015-Q1..2015-Q4 and 2026-Q3; max absolute residual 0.121925 USD million; tolerance 0.15 USD million. Official BCB metadata pages identify both series and unit: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net and https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net.
  - India RBI Table 197 (BPM6 quarterly, USD million): 8/8 comparisons pass over 2024-Q2..2025-Q1 within integer-million rounding ±0.5; max absolute difference 0.490 USD million.
- Combined 18/18 comparisons PASS. For these tested Data Portal API payloads, raw `OBS_VALUE` is already base USD; compare to official USD-million national sources using `OBS_VALUE / 1,000,000`. Do not multiply raw payload by 10^6 a second time. Preserve SCALE=6 metadata and raw values unchanged.
- Brazil assets `A_NFA_T) match BCB 22906 with same sign; liabilities `L_NIL_T) match BCB 22924 with same sign. India RBI credit-minus-debit table uses opposite sign for “Portfolio Investment by India” compared with `A_NFA_T), while “Portfolio Investment in India” net matches `L_NIL_T`.
- Brazil comparison CSV: `docs/evidence/IMF_BOP_BRA_SCALE_RECONCILIATION_2015Q1_2026Q3.csv`, commit `29af9453d49e52efb6ab2c6e1b36bf52157be4a0`; SHA-256 `f9d0fca9015694f41db4353361db862362c56c03dfe17d5f2d02de9a281d0a98`.
- Consolidated report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_INDIA_PART2_20261119.md`, commit `26cfe8203b993b89e257e77256ddaaa01ac2f6fe`.
- The combined pilot workflow run 44475474198 passed source fetch, BCB comparison, exact-panel integrity and raw-to-normalized QA; it failed only at final Git push because a concurrent commit moved the main ref. Independently recomputed the ten Brazil comparisons from archived BCB raw JSON and IMF panel; all ten passed.
- Scope boundary: this establishes a two-country benchmark for this BOP Data Portal series only. The legacy BCB-registered BOP_BPM6 XML vs SGS monthly series still has its separate 2010 structural break and 201/381 mismatches; do not conflate or silently substitute that legacy file. Full 154-country EMDE aggregation remains BLOCKED by coverage/missingness and revision/vintage gates.


## Brazil BOP scale/sign normalization independently verified — 2026-11-19
- Official BCB SGS 22906 (net acquisition of financial assets, monthly, USD million) and SGS 22924 (net incurrence of liabilities, monthly, USD million) were retrieved anonymously; both HTTP 200.
- Five quarters tested (2015-Q1–Q4 and 2026-Q3) × two entries = 10/10 PASS. IMF raw `OBS_VALUE / 1,000,000` compared with the sum of the three monthly BCB values. All BCB monthly values are one decimal; maximum cumulative rounding bound = 0.15 USD million; maximum absolute residual = 0.12192411 USD million.
- Raw BCB hashes: SGS22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; SGS22924 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb`.
- Run 44475693836 / artifact 14506740234 / ZIP SHA-256 `08e7702d9c5e393779d6ff635f6d532ddcfcb79be1eb2be18fd840a13f37b79b`; evidence commit `45d2ce937be6c2f89d1ba4ae7fe0d1ad14842266`.
- Report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`, commit `c7cfefadbcad4703df81ec43b461ab941d85b698`.
- Decision refinement: Brazil scale/sign mapping PASS for tested assets/liabilities and periods. India and other EMDE members remain UNKNOWN; no global conversion or EMDE aggregate. BOP6/BOP_BPM6 identity remains unresolved. Quarterly BOP remains unsuitable as a daily swing trigger.


## Final 2026-11-19 checkpoint refinement — Brazil scale validated
- Brazil scale/sign report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`, commit `c7cfefadbcad4703df81ec43b461ab941d85b698`.
- 10/10 Brazil comparisons PASS (2015-Q1–Q4 and 2026-Q3 × assets/liabilities); max residual 0.12192411 USD million under 0.15 million monthly-rounding bound. Conversion validated for Brazil: IMF raw OBS_VALUE / 1e6 = USD million.
- BCB raw JSON and quarter reconciliation durably archived under `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/`, commit `45d2ce937be6c2f89d1ba4ae7fe0d1ad14842266`.
- EMDE panel remains raw-only until India and additional country scale/concept crosswalks pass. No EMDE aggregate.
- Latest continuity ledger entry commit: `ab27d5e8bda383991ac8c52d938bf1960b04078c`.



## WEO G200 EMDE BOP coverage QA and SCALE concept audit — 2026-11-19
- Independent raw-to-normalized audit: 9,299/9,299 exact observation keys; 30 source fields × 9,299 = 278,970 exact field comparisons; zero duplicates, missing keys or attribute mismatches.
- Coverage: 225/308 country-entry pairs with data; 111/154 members both legs; 3 one-sided (DZA/ETH assets only; ZWE liabilities only); 40 no data; 43/154 lack at least one leg. Only 4 series complete 47/47 quarters; 13 series have internal gaps (71 quarters); 2026-Q3 only BRA and PAK.
- All 9,299 observations have DERIVATION_TYPE=O and UNIT=USD; SCALE=6; PRECISION=6 for 9,119 and blank for 180. No forward-fill, zero substitution, rescaling, FX conversion or aggregation.
- Official concept scheme `IMF:CS_MASTER_SYSTEM(1.0.2)` HTTP 200, 6,192,546 bytes; SHA-256 `9ef243509d7b3edc93b5ef2326ba49c89ced79044ae38674c806d1310367420d`. SCALE English Name=Scale; Arabic label `عدد الخانات العشرية` translates to “number of decimal places”; no English definition or referenced codelist. BOP DSD makes SCALE series-level and distinct from UNIT; do not treat as UNIT_MULT or apply 10^6 multiplier. Preserve raw values.
- Coverage QA run 44475665715 SUCCESS; coverage artifact 14506017682; SCALE artifact 14506356045.
- Detailed report: `docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md`; matrices under `docs/evidence/imf_bop_emde_20261119/coverage_qa/`; scale metadata manifest under `docs/evidence/imf_bop_emde_20261119/scale_semantics/`.
- Decision: data integrity PASS; country coverage PARTIAL; EMDE aggregate BLOCKED / NOT_AUTHORIZED. Sign convention, FX and point-in-time vintage remain unresolved.


## SCALE operational handling resolved for Brazil — 2026-11-19 (supersedes earlier unresolved note)
- Latest IMF master-system concept scheme: `IMF:CS_MASTER_SYSTEM(1.0.2)`; BOP DSD `SCALE` references `CL_UNIT_MULT(1.0+.0)). Exact codelist code 6 label is `Millions`. Raw master-system and unit-multiplier codelist XMLs are archived under `docs/evidence/imf_bop_20261119/`.
- Official BCB SGS source series 22906 = net acquisition of financial assets, monthly, USD million; series 22924 = net incurrence of liabilities, monthly, USD million. Raw source JSON SHA-256s: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22924 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb`.
- Full Brazil source reconciliation covers 47 quarters (2015-Q1–2026-Q3) × 2 entries = 94 checks. Method: sum the three BCB monthly observations in USD million; compare with IMF API `OBS_VALUE / 1,000,000`. Result: 94 PASS, 0 REVIEW, 0 BLOCKED; tolerance 0.15 USD million (monthly source values rounded to one decimal); maximum absolute residual 0.12192411 USD million.
- Conclusion for tested Brazil BOP portfolio series: IMF API `OBS_VALUE` is already expressed in USD even though `SCALE=6` (Millions) metadata is retained. Do not apply a second `×10^6` multiplier. The pilot panel values remain unchanged.
- Final full-run validation artifact: run 44476176136 / artifact 14505944936 / 8,974,699 bytes / SHA-256 `1c9c1975717764aea11230f9fb659270a43c98b198e0154605589a1a8a19f317`.
- Detailed evidence: `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/summary.json`, `quarter_reconciliation.csv`, `quarter_reconciliation.json`; BCB source series URLs are in the summary.
- Limitation: this direct scale/sign cross-check is for Brazil only. India and other EMDE country sources need independent source-to-source validation before full GCR aggregation.


## India BOP scale/sign validation — 2026-11-19
- RBI Table197 official BPM6 quarterly USD-million data (published 2026-07-31) captured anonymously, HTTP 200, 146,017 bytes, SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`.
- Six aligned calendar quarters (2024-Q2 through 2025-Q3) × two entries = 12/12 PASS. RBI 3.2.B Portfolio Investment by India maps to IMF A_NFA_T with sign reversal; RBI 3.2.A Portfolio Investment in India maps directly to IMF L_NIL_T. IMF `OBS_VALUE/1e6` compared within 0.5 USD million integer-publication rounding bound; max residual 0.4899709189 million.
- Run 44476434148 / artifact 14506542277 / ZIP SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`; durable evidence commit `451b9e203fd6edb1541c42432b47a393e030372c`.
- Report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`, commit `4a3bcc34a19d92e747f50609a7cabebe489af69a`.
- Two-country pilot scale/sign validation now: Brazil 10/10 (BCB) + India 12/12 (RBI) = 22/22 PASS. The remaining 152 WEO EMDE members are UNKNOWN; no full-panel conversion or EMDE aggregate. BPM/revision-vintage controls remain open.


## Cross-country BOP scale/sign validation — 2026-11-19 (supersedes two-country pilot status)
- Four-country vintage-aligned national benchmark set: Brazil 94/94, India 12/12, Mexico 6/6, Chile 2026-09 vintage 6/6 = **118/118 PASS** for `OBS_VALUE / 1e6) comparisons.
- Full reports: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART3_20261119.md`; full 126-row matrix `docs/evidence/IMF_BOP_SCALE_CROSS_COUNTRY_VALIDATION_20261119.csv`.
- Brazil 94/94 run 44476176136 / artifact 14505944936; India 12/12 run 44476434148 / artifact 14506542277; Mexico 6/6 run 44476089607 / artifact 14506696311.
- Chile latest raw BDE pages updated 2026-11-18: run 44476957975 / artifact 14507305215; Q4 2025 2/2 PASS, Q1-Q2 2026 4 REVIEW, Q3 2026 2 IMF panel rows missing. Older official web-rendered page snapshot updated 2026-09-07 matched 6/6; old snapshot raw bytes were not archived. Treat as explicit vintage mismatch, not a clean current-vintage pass.
- Operational rule is empirically supported for four countries and tested vintages: preserve raw API values; derived USD-million comparison uses `OBS_VALUE / 1e6`; preserve SCALE=6; do not multiply by 1e6 again. This is not yet universalized to all 154 EMDEs.
- Panel remains coverage PARTIAL; 40 countries no observations, 83 empty country-entry combinations, 13 series with interior gaps. EMDE aggregate remains BLOCKED until vintage/coverage gates are implemented.

- Latest cross-country report correction commit: `ca294d2d8ce416f306dba580d90286bca903f168`; report now reflects Brazil 94/94 and India 12/12 full validations and corrected period windows.


 
## India current-vintage 2026-Q1/Q2 supplement — 2026-11-19
- Earlier India RBI Table197 BPM6 baseline 2024-Q2–2025-Q3 remains 12/12 PASS.
- New RBI Table42 BPM6 current-vintage sample covers 2025-Q1/Q2 overlap and 2026-Q1/Q2: 10/12 comparisons PASS; 2 REVIEW.
- 2026-Q2 asset/liability/combined net PASS; 2026-Q1 asset PASS, liability and combined net REVIEW. IMF L_NIL_T /1e6 = -13,633.508347 USD million vs RBI 3.2.A net = -12,121 USD million; residual -1,512.508347 USD million.
- Raw RBI HTML, manifest, summary and comparison CSV are committed under `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/`; report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`.
- Workflow run 44477031402 / artifact 14505649659 / ZIP SHA-256 `8db4f9536a57df1e8635855af5bb90225de0f800e6e9164bd20d99d1f355b4e2`.
- India current-vintage status PARTIAL; 2026-Q1 REVIEW remains open. This supplements but does not invalidate the historical 12/12 baseline.


## GCR — Nigeria independent national-source validation added (2026-11-19)
- Fifth EMDE country benchmark: Nigeria (NGA), CBN Q2 2026 BOP Highlights Table 2, printed page 6.
- IMF exact-key assets/liabilities quarterly GETs both HTTP 200; Q2 2025, Q1 2026 and Q2 2026 = six comparisons, 6/6 PASS at ±US$5m tolerance based on CBN publication precision (USD 0.01bn).
- Values: assets −0.66, +0.26, +0.70 USD bn; liabilities +5.28, +6.03, +7.09 USD bn. IMF raw values and exact residuals are in the committed CSV.
- CBN PDF: 2,206,494 bytes; SHA-256 `b77c0066385cac4bb3bcbe150321c8da28da7d76c91b78423808a31deaea4cf9`; official URL: https://www.cbn.gov.ng/Out/2026/STD/Q2%202026%20BOP%20Highlights_%20revised.pdf.
- Run 44485137974 SUCCESS; artifact 14510920161; ZIP SHA-256 `bf80b403e072c8eae39f4ec32de77b55d776ef77b7ff4a88e157e3023da7febf`.
- Five-country benchmark total is now 124/124 vintage-matched comparisons (Brazil 94, India 12, Mexico 6, Chile older vintage 6, Nigeria 6). This remains a sample, not universal validation for 154 members.
- Durable report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md`; consolidated Part 4: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART4_20261119.md`; raw IMF CSVs, comparison CSV, summary JSON and extracted CBN page text: `docs/evidence/gcr_nigeria_bop_20261119/`.
- CBN vintage notes: Q2 2025 provisional; Q1 2026 revised; Q2 2026 release narrative describes provisional statistics. Preserve these flags.
- Decision unchanged: no 154-member aggregate, no universal conversion, no production/backtest admission; India Q1-2026 liability REVIEW and Chile current-vintage revisions remain open. Coverage gaps preserved; UNKNOWN is not PASS.


## Nigeria evidence archive commit receipts and workflow guard repair
- Nigeria comparison report commit: `1c63abed6b184118563fad276fe3875a1d300c43`.
- Consolidated Part 4 commit: `4db15a0728c07361a00736760ddd0a0664898c6e`.
- Raw IMF assets CSV commit: `9d794f2089e86bb4103152eadc7e390bbd66eb95`; raw IMF liabilities CSV commit: `95c94e728f3de4956c509e39a9021bb9a0ba70f8`.
- Nigeria comparison CSV corrected and committed at `8213e4de80d2d1361fcd24d391421a1c0bafb467`; summary JSON commit `0443d83f28c7487d581793132bd9c48cf97a0314`; extracted CBN Table 2 text commit `6029bf7942aed9e1397c5229d0eaf7b29ad54861`.
- Master continuity ledger latest commit `aeb6aba173e191663eb3841685a7201119b26fa0`.
- Path-ignore syntax repair commit `9ef1922f63c3091519fe5208ee63e259fcc571c5`; unintended long collector runs 44484649213, 44484666061 and 44485482464 were all cancelled by helper run 44485600055 SUCCESS. No production source code was intentionally changed; research-only paths now excluded from the production collector workflow.


## Brazil PA transaction 2 alternate serialization probe Part 2 — 2026-11-19
- Focused run #34 / 44493473476 SUCCESS; prior registration/history steps intentionally skipped; PA tx2 probe step and artifact upload both SUCCESS.
- Artifact 14513337963, 1,275 bytes, ZIP SHA-256 `824a09425db76982ba73a1b9f51cd768669d560a5b017b732f0cf224ce7720e6`; manifest SHA-256 `994aa5f6b7e5ce7bb5257097a51f7d94a2cfbaf6b55eee1cdfbc2202260ef987`.
- Both documented formats were tested against tx2: `format=fusion-json` and `format=sdmx-json`. Both returned HTTP 500, 39-byte body `Unable to return transaction for id '2'`, SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`. Header Content-Type was application/zip although body was plain text; do not treat as archive/JSON.
- Focused script commit `46bd48fcaecc6d866061d21f9151508bf841afb7`; corrected workflow commit `e96942c1d809dd36a6c596621a967e8668af8444`; trigger commit `431006c2893cb6882b33edd9fc3465b8602febf4`.
- Earlier workflow attempts #29–32 failed at workflow parsing/step-condition indentation; this was an orchestration defect, not a source-data failure. Corrected workflow was verified by successful focused run #34. Longer redundant runs #28 and #33 were not used as evidence.
- FMR docs confirm the format options, but IMF deployment cannot serialize tx2 in either. Do not retry identical endpoints. Next route: official Registry UI Activity / Structure Submissions and PA detail Changelog/Compare; archive exact downloaded revisions only. If unavailable without authorized access, preserve UNKNOWN.
- Decision: alternate format probe PASS; tx2/PA Changelog BLOCKED; Brazil Reconstruction BLOCKED; BOP6 vs BOP_BPM6 mismatch remains BLOCKED. No alias, admission, production changes, or paid spend.
- Report: `docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART2_20261119.md`.


## Brazil PA official RSS transaction archive probe Part 3 — 2026-11-19
- Focused run #35 / 44493898103 SUCCESS; artifact 14513872121 (4,410 bytes), ZIP SHA-256 `e88d37e4054c304618ed1af4be14337a6e0b583d791b4cf2e93115410854639a`.
- Official `https://sdmxcentral.imf.org/rss.xml` returned HTTP 200; 34,559 raw bytes; SHA-256 `ff0c03df5d6b9557d6f6c21a341a7d589baef38893291fcfc2ff715257619e73`; XML parse PASS. It contains 38 latest transactions, oldest 2026-11-18T09:11:47Z (tx #38637), newest 2026-11-19T08:43:07Z (tx #38674); 0 matches for Brazil, BR_BOP_BP6, BOP6/BOP_BPM6 or transaction #2. RSS is not a historic archive for 2023-09-22.
- tx2 fusion-json and sdmx-json repeated in same workflow and both remain HTTP 500 with same 39-byte error body/hash `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`; no further identical retries.
- RSS script `fab0b0051d4f1673b2d6f6c5e36eff85d94444c5`; workflow integration `8afdcd8030f07313d6cfcb4a249cd88872d3822a`; trigger `48aabd06fd3697eea2853a5706a566a68fb94501`.
- An initial missing paths-ignore entry caused accidental production collector run #381 / 44493879791. Corrected paths-ignore (commit `110c8e6d6abbe536165c760d919c4c3926030501`) now excludes both Brazil probe scripts and trigger. Cancellation helper run 44493979049 SUCCESS; target collector run 44493879791 final CANCELLED at 09:10:54Z. No production code changes.
- Next: interactive official IMF UI/authorized historical export only; otherwise preserve UNKNOWN/BLOCKED and pivot to GCR coverage. No production selector, ranking, pressure fade, CORE-672 or engines changes; ₹0.
- Report: `docs/IMF_BRAZIL_RSS_TRANSACTION_ARCHIVE_PROBE_PART3_20261119.md`.


## GCR alternate national BOP source map — 2026-11-19
- Existing QA country-readiness confirms 40/154 G200 members have no IMF P_F observations on either A_NFA_T or L_NIL_T; three one-sided members DZA/ETH/ZWE; 13 series with internal gaps.
- Found official alternate sources for 11 of 40 zero-data members: seven WAEMU members with 2024 BCEAO national BOP reports (BEN/BFA/CIV/GNB/MLI/SEN/TGO), Niger 2023 report (NER), UAE annual BOP metadata (ARE), Kenya annual + quarterly sources (KEN), and Oman official BOP XLSX/CSV listing (OMN).
- BCEAO annual reports are BPM6 and CFA-franc denominated, but annual only. UAE DSBB says BOP currently disseminated annually and quarterly dissemination planned; don't treat as quarterly-ready. Kenya sources have different frequencies/units/vintages (KES million annual, USD million quarterly/cumulative). Oman file bytes/frequency still NOT_CAPTURED.
- No raw national files archived and no exact IMF A_NFA_T/L_NIL_T reconciliations performed yet. Source discovery only; no series admission, no synthetic quarterly data, no aggregation.
- Next work: retrieve original files for cohort A in short batches; extract financial-account assets/liabilities separately; reconcile frequency, BPM6 classification, sign, currency/scale, and vintage before assigning country-entry-period PASS/REVIEW/BLOCKED/UNKNOWN.
- Report: `docs/GCR_ALTERNATE_NATIONAL_BOP_SOURCE_COVERAGE_MAP_20261119.md`.


## BCEAO 2024 Annual Report UEMOA BOP extraction — 2026-11-19
- Official BCEAO-hosted Annual Report 2024 PDF Annexes A23–A27 was inspected; source text identifies eight individual UEMOA BOP tables, reference years 2022–2024(*), unit FCFA billion; 2024(*) is marked estimate.
- Extracted 2024 financial-account net balances and net subcomponents (direct investment, portfolio investment, derivatives, other investment) for BEN/BFA/CIV/GNB/MLI/NER/SEN/TGO. Component sum residuals: 6/8 zero; BFA -0.1 and CIV -0.1, TGO +0.1? Correction: 3/8 nonzero residuals, BFA -0.1, CIV -0.1, TGO +0.1. All are within one-decimal presentation precision; reported totals preserved.
- Crucial limitation: source reports only net component balances, not the separate asset and liability legs. A_NFA_T and L_NIL_T mapping remains NOT_SEPARATELY_DISCLOSED; no mapping, sign transform, or annual-to-quarterly imputation performed.
- Raw PDF bytes not yet archived; no raw-byte hash claimed. Extracted CSV and report are evidence transcriptions from the official indexed PDF text, pending raw-PDF archival and second-person/source-image verification.
- CSV: `docs/evidence/gcr_bceao_2024/bceao_2024_uemoa_financial_account_net.csv`; report: `docs/GCR_BCEAO_2024_ANNUAL_NET_BOP_BENCHMARK_20261119.md`.
- CSV commit `67483e3af1782abde81c5d1800ae49694623e9ac`; report commit `5d4c01bd634c697086a40347a9209192f68ed1ba`.
- Decision: annual net benchmark PARTIAL PASS (8 rows); IMF leg reconciliation BLOCKED; quarterly repair and aggregate BLOCKED / NOT_AUTHORIZED. Production and CORE-672 invariants unchanged; ₹0.


- Arithmetic QA correction (2026-11-19): the report and ledger initially misstated the count. Correct result is **5/8 exact component sums and 3/8 residuals of 0.1 FCFA billion** (BFA −0.1, CIV −0.1, TGO +0.1). Published total values remain unchanged. Corrected report commit: `9fa25ec6a9c3d642df8dcc96405e5dfa69985a97`.


## BCEAO 2024 Annual Report raw PDF archive — 2026-11-19
- Focused workflow run `44494766325`: SUCCESS. Official URL returned HTTP 200, application/pdf; retrieved UTC `2026-11-19T09:15:44.644765+00:00`; 7,076,916 bytes; PDF magic `%PDF-1.5`.
- Raw PDF SHA-256: `d1d69c4772e244174c754552b52f4206e8eaf98a6b839bdcd5af1990cf1a3d84`.
- Artifact ID `14514282771`, name `bceao-annual-report-2024-raw`, ZIP size 6,167,993 bytes, artifact digest `7b5865d7c38f45b3d311c7e3cea0e9381ba35f4ed46d0025411ffdcb27e060df`, retention through 2027-02-17. Artifact downloaded and raw PDF byte count/hash independently rechecked.
- Script commit `1afcc080a25467cc814c1654b5da03d61e899c85`; workflow `37ea952bd3083e6238424a6dedd5d587dd88e7d2`; collector paths-ignore fix `ca27927d0e1e706ed43bc48c01075a8af14a1efe`; trigger `9be9ab68b06b5ff51bebc393c889afd19201ebe0`.
- Accidental NSE collector runs `44494746703` and `44494753220` were cancelled before market data acquisition; both job step 5 (Acquire 200 NSE market sessions) concluded CANCELLED and later production steps SKIPPED. Cancellation helper run `44494822191` SUCCESS. No production source code changed.
- Benchmark report: `docs/GCR_BCEAO_2024_ANNUAL_NET_BOP_BENCHMARK_20261119.md`.


## BCEAO Côte d'Ivoire 2024 report — partial gross FDI legs (2026-11-19)
- Official 63-page national BOP report PDF archived: HTTP 200, 3,596,808 bytes, retrieved UTC `2026-11-19T09:18:58.398586Z`, SHA-256 `99aee45e2f75464e85b9b319c9acd93bfd706779119e8c6bfac8db0f5a1a2f28`, PDF 1.7.
- Focused workflow run `44495255971` SUCCESS; artifact `14515150693`, ZIP digest `6ad9941564fbed0c144e6d65e7065acbef5c6511df19fb7cd5c59ce5f9659baa`, expires 2027-02-17.
- Report printed pages 24–25 (PDF pages 27–28) separately state outward direct-investment net acquisition of financial assets 138.1 FCFA bn and inward direct-investment net incurrence of liabilities 1,892.8 FCFA bn. Difference 138.1 − 1,892.8 = −1,754.7, exactly matching Table 13 direct-investment net balance. Liability subcomponents 1,176.9 + 426.3 + 289.6 = 1,892.8; asset subcomponents 92.7 + 45.4 = 138.1.
- Table 13 also reports portfolio net −1,055.5, derivatives +0.1, other investment net −1,233.0, total financial account net −4,043.1. These non-FDI components are net only in this report. It explicitly says BCEAO optical presentation excludes banking-system flows for certain categories.
- Result: direct-investment component gross-leg extraction PARTIAL PASS; not whole financial account. IMF A_NFA_T/L_NIL_T aggregate mapping remains BLOCKED / NOT_MAPPED; do not use the FDI-only legs as aggregate entries.
- CSV `docs/evidence/gcr_bceao_2024/civ_2024_fdi_gross_legs.csv`, commit `9c7731c2e1ba68035f384848db13df7aa5fbb517`; report `docs/GCR_BCEAO_CIV_2024_FDI_GROSS_LEGS_PARTIAL_20261119.md`, commit `738c4cfd0aea326d50a11ad2b1be8581a5bddebf`.
- Script commit `20b3637ecc7169558df15456e5cd204d45f7dbb0`; workflow `247b88e5c06bd6f91eaa2eca8f0c0c8a86991a2c`; collector guard `f82444e347be43490c643dd7894066020f572ce6`; trigger `ac0b8977db9fc48a735793d14e64c206d15ff673`.
- Two accidental collector runs `44495237321` and `44495240272` cancelled before market data acquisition; cancellation helper run `44495300530` SUCCESS. Production collector step 5 was cancelled and later steps skipped. No production source code changed.
- Historical source lead: BCEAO Côte d'Ivoire 2021 report Table 1 also contains separate aggregate acquisition-of-assets and incurrence-of-liabilities columns, but it is a different vintage and must not be mixed with the 2024 vintage without reconciliation.


## BCEAO Côte d'Ivoire 2024 gross FDI split — 2026-11-19
- Archived official 63-page national BOP PDF; raw 3,596,808 bytes; SHA-256 `99aee45e2f75464e85b9b319c9acd93bfd706779119e8c6bfac8db0f5a1a2f28`; run `44495255971` SUCCESS; artifact `14515150693`, digest `6ad9941564fbed0c144e6d65e7065acbef5c6511df19fb7cd5c59ce5f9659baa`.
- Printed pp.24–25: FDI asset acquisitions 138.1, FDI liability incurrence 1,892.8 FCFA bn; difference -1,754.7 exact to Table 13 direct-investment net. Asset and liability subcomponents also reconcile exactly.
- Portfolio (-1,055.5), derivatives (+0.1), other investment (-1,233.0) and total financial account (-4,043.1) are net balances. This is FDI-only gross-leg extraction, not aggregate A_NFA_T/L_NIL_T; mapping remains BLOCKED.
- CSV `docs/evidence/gcr_bceao_2024/civ_2024_fdi_gross_legs.csv`; report `docs/GCR_BCEAO_CIV_2024_FDI_GROSS_LEGS_PARTIAL_20261119.md`.

## BCEAO BEN/BFA/SEN 2024 raw archive and screen — 2026-11-19
- Focused run `44495561543` SUCCESS; artifact `14514373729`, ZIP 17,363,969 bytes, SHA-256 `6a670ead73df28b6766aef0c0e5004f795867903dc9bdb3ad59b248c0921518d`, expires 2027-02-17. Three original PDFs HTTP 200 and independently hashed: BEN 5,606,445 bytes / `15af93618aafee0446eef191ab9e208dcc1c807e3507eadf306c1ce6dbc92193`; BFA 6,707,349 bytes / `6a4b7149d5abb13d4aac7600cc13a7c0b157cb1d6aa06f8fed41e2b12e33a8ba`; SEN 6,055,592 bytes / `ee8e7794d2ad85f337d6c1536edcda973f3f7f322cb3b131e332fdb38a133395`.
- Initial source screen: BEN has net financial-account components and separate portfolio stocks (not transaction flows); BFA has total net financial-account balance and an inward-FDI liability-side change of -122.6bn, but no full gross asset/liability pair established; SEN gross-leg extraction UNKNOWN pending page-image review. No inference or leg completion from net balances.
- Full report `docs/GCR_BCEAO_BEN_BFA_SEN_2024_SOURCE_SCREEN_20261119.md`, commit `b0eca5eff4129b84ee7603a49ed7a36837144aeb`.
- Script `d0329a779aa002f516ce973bffb3011b889b491a`; workflow `1939e57aad83c5cddd9cd6ba088fdfcb801c4bd2`; production collector pre-guard `afa8fbcf080ad2f6e5daa6af192013f2a9f2f3d7`; trigger `b972bc997bc8a757384c03b2eb2eb836b4ab4d99`. Guard applied before script/workflow/trigger commits; no NSE collector run triggered by this batch.
- Next: page-image/OCR review BFA and SEN; then acquire GNB/MLI/TGO 2024 reports. Aggregate IMF A_NFA_T/L_NIL_T mapping remains BLOCKED / NOT_MAPPED.


## Continuation 42 — BFA gross leg split + BEN/SEN source-page verification (2026-11-19)
- New exact evidence: official Burkina Faso Ministry of Economy and Finance/BCEAO 2024 report Table 15 (printed p.36) publishes non-monetary-sector net acquisition of assets 342.6 and net incurrence of liabilities 1,120.4 FCFA bn; total balance -777.8, exact 342.6−1,120.4. Category pairs: direct 34.6/−122.6 (+157.2); portfolio −3.7/246.1 (−249.8); derivatives 0/0; other investment 311.7/996.9 (published −685.1; 0.1 rounding residual). Component sums: assets 342.6; liabilities 1,120.4.
- Important scope: Annex 1 states BCEAO analytical optic excludes central bank and other deposit-taking institutions' portfolio, derivatives and other-investment operations; monetary-sector flows are in external net assets/liabilities. Therefore this is NOT whole-country IMF A_NFA_T/L_NIL_T. Full aggregate mapping BLOCKED.
- BFA CSV `docs/evidence/gcr_bceao_2024/bfa_2024_gross_legs_scoped.csv`; report `docs/GCR_BCEAO_BFA_2024_GROSS_LEGS_SCOPED_PARTIAL_20261119.md`.
- BEN Table 14 (printed p.30) has only net category balances. SEN Table 16 (printed p.27; PDF p.44) confirmed by page-image inspection to have only net category balances. SEN total -2,139.9; direct -1,963.1; portfolio -395.9; derivatives 0.0; other investment +219.2 FCFA bn.
- Corrected prior report `docs/GCR_BCEAO_BEN_BFA_SEN_2024_SOURCE_SCREEN_20261119.md`, commit `0d9ce750ff9acbc50a4b680a98dbc516e7433bed`. Official web source for BFA Table 15 and scope: https://www.finances.gov.bf/fileadmin/user_upload/storage/fichiers/Rapport_BdP_2024_au_10-12-2025_TS_AG_13h00__2_.pdf.
- Next: source the excluded monetary-sector gross flows for BFA; search the other UEMOA reports for similar detailed tables, while preserving BCEAO vs IMF scope distinctions. No quarterly interpolation or production/backtest admission.
