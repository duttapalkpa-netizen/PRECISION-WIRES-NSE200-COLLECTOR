# IMF Registry Transaction Detail Resolution — Part 3
Date: 2026-11-18 (UTC)
Continuation: গবেষণা যাচাই অব্যাহত 37
Scope: only the 33 transaction links already present in archived IMF RSS evidence; no RSS or BCB raw payload re-download.

## 1. Source and reproducibility
- Source RSS run: `44301482210`; artifact `14426565546`; archived RSS raw SHA-256 `8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2`.
- Exact RSS transaction links were extracted from that archived `imf_rss.xml`, not guessed from a numeric range.
- Resolver run: `44302351313`, run #1, SUCCESS; URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44302351313
- Resolver artifact: `14426702319`; GitHub artifact digest `sha256:270aad8014a246c6a3aca6b2f03d22ee027f6fde575e3f5760cb06b5bc552dfd`; downloaded ZIP SHA-256 independently recomputed to the same value.
- Artifact contains all 33 raw transaction XML responses plus `transaction_resolution.json`. Every raw XML file was independently parsed from the downloaded ZIP.

## 2. Actual payload format — correction to the initial parser assumption
All 33 transaction URLs returned:
- HTTP 200;
- root `RegistryInterface`;
- a `QueryRegistrationResponse` (not `SubmitRegistrationRequest`);
- `StatusMessage status="Success"`;
- a `Registration` record containing a `ProvisionAgreement` URN and a `SimpleDataSource` URL.

Counts: 33/33 transport success, 33/33 XML well-formed, 33/33 response status Success. The first resolver parser looked only for Submit* request/response names and did not classify QueryRegistrationResponse; it did nevertheless archive every raw response and extract Registration/SimpleDataSource elements. The raw artifact was therefore re-parsed independently and the parser was corrected in source commit `59710ea3a8a9b7133859a2d571b2cd165cc18a7a` to recognize QueryRegistrationResponse, StatusMessage, ProvisionAgreement and Datasource. This parser fix has NOT been rerun; no new network fetch is claimed.

## 3. Exact bounded-window finding
No one of the 33 returned records contains literal `IMF:BR1`, the registered Brazil BCB URL/host path, or a Brazil BOP_BPM6 Dataflow reference. No Brazil registration candidate was found in this bounded RSS window.

Provision Agreement URN prefixes in the 33 records:
| URN prefix | Count | Transaction IDs |
|---|---:|---|
| IMF:IL_* | 21 | 38615–38635 |
| IMF:CL_* | 6 | 38614, 38642–38646 |
| IMF:AT_* | 2 | 38636, 38638 |
| IMF:HU_* | 2 | 38639–38640 |
| IMF:NL_* | 1 | 38637 |
| IMF:PT_* | 1 | 38641 |

Important false-positive control:
- Transaction `38642` is `IMF:CL_BOP(1.0)` and its source URL is `https://si3.bcentral.cl/SieteSdmx/SieteSdmx.ashx?SDMXCategory=SDMX_BOP6`.
- This is a Chile-prefixed ProvisionAgreement and Chilean `bcentral.cl` host, not the Brazil Central Bank `bcb.gov.br` registered URL. Do not classify it as Brazil merely because the ID contains BOP6 or the hostname contains “bcentral”.
- Transactions `38643`–`38646` are also `IMF:CL_*` entries from the same Chilean source.
- Israel-prefixed records `38615`–`38635` use `IMF:IL_*` ProvisionAgreement IDs and CBS Israel datasource URLs.

The RSS window covers transactions #38614–#38646 dated 17–18 Nov 2026. This is only a bounded recent window, not the full historical registration ledger. The result is strictly:
`NO_BRAZIL_REGISTRATION_MATCH_IN_THIS_33_TRANSACTION_WINDOW`.
It does NOT prove that no Brazil registration event exists outside this window.

## 4. Reconciliation with the already-confirmed Brazil mismatch
Keep prior independent evidence unchanged:
- Registry listing snapshot: Dataflow `IMF:BOP6(1.0)`, provider `IMF:BR1`, BCB registered XML URL.
- BCB payload: Dataflow `IMF:BOP_BPM6(1.0)`.
- Earlier full contract reconciliation run `44290101769`, artifact `14420378420`, digest `6435b5df856889ae1a48742681f0b127b04e1a4057c361b054c329a5049fc8aa`.
- Mismatch remains CONFIRMED. The recent 33-item RSS window contains no Brazil-specific record that explains or resolves it.
- Historical registration event time / correction chronology: UNKNOWN.
- Brazil admission: BLOCKED pending authoritative IMF-side registration correction or explanation.
- EM aggregation / trading admission: NOT_AUTHORIZED.

## 5. Current acceptance
| Check | Status |
|---|---|
| Reuse exact archived 33 RSS links | PASS |
| Fetch all 33 transaction URLs | PASS — 33/33 HTTP 200 |
| Parse all transaction XML | PASS — 33/33 |
| Registry response status | PASS — 33/33 Success |
| Extract ProvisionAgreement and datasource | PASS — independently re-parsed raw artifact |
| Brazil marker in this 33-item window | PASS — none found in bounded sample |
| Historical Brazil event outside window | UNKNOWN |
| Brazil Dataflow mismatch | CONFIRMED / BLOCKED |
| Brazil registration admission | BLOCKED |
| Trading admission | NOT_AUTHORIZED |

## 6. Trigger incident and prevention — fully recorded
The first two commits that added the resolver script/workflow preceded the collector-ignore guard and inadvertently triggered full NSE collector runs:
- Run #170 / ID `44302281284` (triggered by resolver script commit `6751823c58594409a1e241bf605aba6d40424050`).
- Run #171 / ID `44302288225` (triggered by workflow commit `a3fcdb135ee02c4aa4ec04944045f628b40c28a1`).
The earlier accidental Run #169 / ID `44301482238` from the preceding IMF workflow incident was still active at the last check.
- Run #169 had passed 200-session acquisition, Security Master, dataset build and Strict QA; 100-session walk-forward backtest was in progress.
- Runs #170 and #171 were in the 200-session acquisition step.
- This connector has no GitHub Actions cancel write operation. Owner should cancel duplicate/overlong collector runs from the Actions UI if still active. Do not treat these runs as evidence for this IMF task.
- Prevention is now committed in `nse_collector.yml` commit `ea7381135a388fe291e85d62cddbd9c37aec49d4`: its `paths-ignore` includes the resolver workflow, resolver script and trigger marker.
- Resolver trigger is narrowly scoped to marker file `scripts/research/imf_transaction_resolver_trigger.txt`; resolver workflow itself has an 8-minute timeout. No more commits should be used to trigger this workflow.

## 7. Next highest-value action
The recent RSS window does not contain the Brazil event. Next work should be a targeted historical lookup for the exact Brazil registration identifiers (`IMF:BR1`, registered BCB URL, and relevant ProvisionAgreement/Dataflow URNs) using IMF SDMX Central's official Activity / Provision Agreement views and only documented public read endpoints. Do not broaden into an unbounded full registry scrape, do not infer event IDs, and do not alter either Dataflow identifier.

## 8. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Engines A–E unchanged. No PR merge, production integration, paid API, synthetic data, guessed event timestamp, guessed identifier, or trading admission. UNKNOWN is not PASS.
