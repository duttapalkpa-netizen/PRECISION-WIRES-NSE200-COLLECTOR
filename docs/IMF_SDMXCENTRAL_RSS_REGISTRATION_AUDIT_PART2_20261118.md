# IMF SDMX Central RSS + Brazil XML Retrieval — Part 2
Audit date: 2026-11-18 (Asia/Kolkata)
Continuation: গবেষণা যাচাই অব্যাহত 36
Scope: official raw retrieval, feed parsing, Brazil payload retrieval and workflow hardening.

## 1. Prior evidence reused — no unnecessary re-acquisition
- Part-1 source discovery: `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART1_20261118.md`, commit `80c93853f0abf90e985d6b54cb6be893cd9963e8`.
- Earlier Brazil payload/contract reconciliation was already completed in workflow run `44290101769`, artifact `14420378420`, artifact digest `sha256:6435b5df856889ae1a48742681f0b127b04e1a4057c361b054c329a5049fc8aa`. Its report proves the exact BCB header Dataflow is `IMF:BOP_BPM6(1.0)`, while the registration snapshot says `IMF:BOP6(1.0)`; these are distinct Dataflow identities even though they reference the same DSD `ECOFIN_DSD`. Do not call them aliases.
- Existing reconciliation reported 237 series, 89,097 observations, 1995-01 through 2026-09; BOP6 constraint accepted 234/237 payload indicators (98.7342%), while BOP_BPM6 constraint accepted 27/237 (11.3924%). This is strong evidence of a registration/payload contract mismatch, not a harmless filename difference. No new observation panel is claimed.

## 2. Raw retrieval — actual successful GitHub Actions evidence
Dedicated workflow:
`.github/workflows/imf_sdmx_rss_registration_audit.yml`

The first dedicated run completed successfully:
- Run ID: `44301482210`, run #1, conclusion SUCCESS.
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44301482210
- Artifact ID: `14426565546`
- Artifact SHA-256 digest: `0a35ddb0f83ae2c14f5ce2a60dc365f5324e56de55a3442227b8a74e786a132f`
- Artifact size: 834,648 bytes.

Two subsequent duplicate runs also completed SUCCESS after trigger refinements:
- Run `44301625778`, artifact `14426296464`, digest `64bdb245a0d6242969615b7f86ba1fea3ea9f1605f721bdd65a396a0134bd66c`.
- Run `44301659461`, artifact `14425444941`, digest `036e81dd4e7c36ea2d653a05cc8dad4826b27b8fc98e9182d146f8a022422b02`.
These are duplicate transport checks, not independent economic observations. Preserve all run IDs/artifacts; do not repeat the fetch without a new requirement.

### Run #1 raw evidence
- IMF RSS: HTTP 200; Content-Type `application/xml`; final URL unchanged; retrieved `2026-11-18T12:11:06.691171+00:00`; 30,110 bytes; SHA-256 `8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2`.
- RSS parser: PASS; 33 feed items. Latest item is Transaction #38646, pubDate `Wed, 18 Nov 2026 12:01:46 GMT`; feed includes transaction IDs #38646 down to #38614 in the captured response.
- Brazil BCB XML: HTTP 200; Content-Type `text/xml`; retrieved `2026-11-18T12:11:07.589328+00:00`; 4,840,062 bytes; SHA-256 `3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c`.
- BCB XML well-formed parse: PASS; root `StructureSpecificData`.
- Independent local recomputation over downloaded artifact bytes matched the recorded raw-file SHA-256 values.
- Run #1 artifact was downloaded and inspected. It contains `imf_rss.xml`, `bcb_bop_bpm6.xml`, and `summary.json`.

## 3. RSS event limitation
The 33 RSS entries are real feed transaction notifications with links such as:
`https://sdmxcentral.imf.org/ws/registry/tx/transactions?txId=38646`.
The transaction detail URLs could not be retrieved through the browser interface. No linked RegistryInterface payload was archived or parsed in this part. Thus:
- RSS transport and feed XML parse: PASS.
- RSS transaction event details / Brazil-specific historical registration reconstruction: UNKNOWN / NOT_DONE.
- Do not infer that the latest transaction IDs refer to Brazil.

## 4. BCB header / registry mismatch — independently established earlier
The current raw BCB payload root attributes include a schemaLocation identifying:
`IMF:BOP_BPM6(1.0)`
and the dataflow schema URL:
`.../schema/dataflow/IMF/BOP_BPM6/1.0?format=sdmx-2.1`.
The earlier run `44290101769` performed the full authoritative contract reconciliation:
- Registry snapshot: `IMF:BOP6(1.0)`, provider `IMF:BR1`.
- BCB payload Header/Structure namespace: `IMF:BOP_BPM6(1.0)`.
- Both Dataflows reference `IMF:ECOFIN_DSD(1.0)`, but shared DSD does not make their Dataflow IDs equivalent.
- Constraint compatibility: BOP6 98.7342%; BOP_BPM6 11.3924%.
Decision: mismatch CONFIRMED; keep Brazil registration/dataflow admission BLOCKED pending IMF-side registration correction or formally authoritative explanation. Do not rewrite the payload ID or registry row.

The first new workflow's generic element scanner returned an empty list for Header reference elements because the BCB file expresses the Dataflow in the root schemaLocation/Structure namespace rather than a literal `DataflowRef` element. This is a parser coverage limitation, not evidence of absent Dataflow. Workflow parser was corrected in commit `0e4fd08428f0fcaf2ae34b2e48a0ceac58e36b00` to extract Dataflow from schemaLocation and Structure/structureRef attributes. That corrected parser has NOT yet been rerun; the prior contract reconciliation remains the accepted evidence.

## 5. Workflow trigger incident and corrective guard
- Initial workflow commit `2e5361d2ef46d4ae7b052f0846c8c5e78fe7d430` unintentionally also triggered the broad NSE collector workflow, run #169 / ID `44301482238`, because the existing `nse_collector.yml` push paths-ignore list did not exclude the new IMF workflow file.
- Run #169 was observed in progress at step “Acquire 200 NSE market sessions”. This audit connector has no Actions cancel write operation. Owner should cancel it in GitHub Actions if it is still running: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44301482238
- Corrective guard commit `00bbdf1f00d3d8ec633df4ca85f004a03c1e20fa` added the IMF workflow path to the main collector's paths-ignore.
- Further guard commit `e75a1326647c8e256bde8fec2b8fba5035f5edc0` added `scripts/research/imf_audit_trigger.txt` to paths-ignore.
- Trigger marker commit `a13e30b8414beab8c5a3c9c62769d6550f17f653` started the isolated workflow after its definition existed.
- IMF workflow was then made manual-only (workflow_dispatch) and parser hardened in commit `0e4fd08428f0fcaf2ae34b2e48a0ceac58e36b00`. Future runs should be deliberately dispatched, avoiding duplicate automatic retrievals.

## 6. Current acceptance matrix
| Check | Status |
|---|---|
| Official IMF RSS raw HTTP 200 | PASS |
| RSS raw bytes archived + SHA-256 | PASS |
| RSS XML parse and 33 items extracted | PASS |
| BCB raw XML HTTP 200 | PASS |
| BCB raw bytes archived + SHA-256 | PASS |
| BCB XML well-formed parse | PASS |
| Exact BCB Dataflow vs registry mismatch | PASS — CONFIRMED by prior contract audit |
| Full BCB header scanner in new workflow | PARTIAL — parser fix committed, not rerun |
| RSS transaction detail / RegistryInterface payload | UNKNOWN / NOT_DONE |
| Brazil historical registration event reconstruction | UNKNOWN / NOT_DONE |
| Brazil BOP registration admission | BLOCKED — mismatch confirmed |
| EM aggregation / trading admission | NOT_AUTHORIZED |

## 7. Next highest-value action
Do not repeat raw RSS/BCB download. Next work should be a small read-only registry transaction-detail resolver:
1. Use captured RSS links/transaction IDs and retrieve transaction XML via GitHub runner.
2. Parse RegistryInterface SubmitRegistrationRequest records, identify whether any event references IMF:BR1 or the BCB registered URL.
3. If none in the 33-item window, record that bounded window as “no Brazil event found”; do not claim no historical event exists.
4. Reconcile event Dataflow and URL against the registry snapshot and prior mismatch report.
5. Keep runtime under 8 minutes; no NSE collector run.

## 8. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Engines A–E unchanged. No PR merge, production integration, paid API, synthetic data, guessed timestamp, guessed identifier or trading admission. UNKNOWN is not PASS.
