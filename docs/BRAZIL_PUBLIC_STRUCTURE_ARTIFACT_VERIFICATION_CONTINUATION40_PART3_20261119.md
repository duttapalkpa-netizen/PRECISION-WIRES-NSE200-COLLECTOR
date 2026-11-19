# Brazil Public Structure Artifact Verification + CI Trigger Hygiene
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 40, Part-3
Scope: complete pending Continuation 76 artifact inspection; independently validate bytes/XML; stop repeated no-job EMDE persistence workflow failures. Read-only IMF evidence; one narrow workflow trigger edit. No production logic changes.

## Progress Log

### Completed / reused
- Reused Brazil registration lifecycle 40/40 PASS; no repeat.
- Reused exact PA/registration tuple: PA IMF:BR_BOP_BP6(1.0), provider IMF:BR1, registered BCB URL; current PA StructureUsage references IMF:BOP6(1.0).
- Reused known PA transaction-ID-2 serialization failure (fusion-json and sdmx-json both HTTP 500); do not repeat.
- Reused Continuation 76 report and workflow trigger/script commits; this part closes its pending artifact verification.

## 1. Continuation 76 workflow run and artifact — independently verified
- Workflow run 44533595369: SUCCESS.
- Job 135593069697 (probe): SUCCESS.
- Lifecycle/history steps 4–6 were intentionally skipped by [PA-TX2-ONLY]; current structure probe, RSS capture and artifact upload succeeded.
- Artifact ID 14534769007; name imf-brazil-public-api-probe-44533595369; size 7,648,050 bytes; expires 2027-02-17.
- GitHub artifact digest: 4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e.
- Downloaded ZIP independently recomputed with SHA-256: same exact digest. ZIP contains four current SDMX structure XMLs, manifest, two tx2 error bodies, and RSS raw XML.

## 2. Manifest/raw/XML integrity
All four current structure resources:
- Brazil PA: HTTP 200; 42,896,179 bytes; SHA-256 b4343e43bbf82047a011bfa813f6bafc5149f8ff03132fa736ba2b037a56ded2.
- Dataflow BOP6: HTTP 200; 43,071,271 bytes; SHA-256 4b5c1028534487f0b96da66ae57bf1f26a53cdf5b87f78127dbcdf0b012d1a98.
- Dataflow BOP_BPM6: HTTP 200; 42,908,746 bytes; SHA-256 7cc596edeffc0819b068829a605c2f5514726fcc859bf84498ecaeef38c73be4.
- DataStructure ECOFIN_DSD: HTTP 200; 42,905,001 bytes; SHA-256 d0b6a3301683a7dd4b4207982944ebdc904bc9092fa980dffda8f626ac94bc30.
- For each of the four resources: manifest byte count equals actual bytes; manifest SHA-256 equals independently recomputed SHA-256; XML parses successfully with SDMX-ML 2.1 message:Structure root. 4/4 PASS.
- ZIP digest independently matches GitHub artifact digest. Integrity check PASS.

## 3. Exact PA / Dataflow relationship confirmed from raw structures
- Exact Brazil PA maintainable: IMF:BR_BOP_BP6(1.0).
- Inside that PA, StructureUsage/Ref is exactly IMF:BOP6(1.0), class Dataflow.
- Inside that PA, DataProvider/Ref is exactly IMF:DATA_PROVIDERS(1.0).BR1.
- BOP6 Dataflow name: “Balance of Payments (BPM6) for Collection”.
- BOP_BPM6 Dataflow name: “Balance of Payments -- BPM6”.
- Both Dataflows reference the same IMF:ECOFIN_DSD(1.0), but have distinct IDs/URNs.
- Current returned BOP6 structure contains five Provision Agreements referencing BOP6: BR_BOP_BP6, CL_BOP, IMF_BOP6, RO_BOP_BP6, SE_BOP.
- Current returned BOP_BPM6 structure contains twelve Provision Agreements referencing BOP_BPM6: AT_BOP, BE_BOP, CH_BOP, GB_BOP, HU_BOP6, IMF_REPORT_BPM6, JP_BOP, LU_BOP, MT_BOP6, SK_BOP, US_BOP, US_BOP_BPM6. Brazil PA is not among these twelve.
- These counts describe only the current public structure responses and do not establish historical PA revisions or all possible private/unpublished structures.
- Official IMF Web Services Guide (May 2025) uses DATA_DOMAIN as a separate ECOFIN DSD dimension and shows registration as a private/authenticated POST. It does not state that a PA on BOP6 may submit a payload whose Dataflow reference is BOP_BPM6, and does not provide a Brazil-specific crosswalk.

## 4. Transaction and RSS evidence boundary
- Transaction ID 2 fusion-json and sdmx-json: both HTTP 500; each 39 bytes; identical SHA-256 76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825. These are rejected error bodies, not valid transaction XML/JSON or PA revisions.
- RSS raw XML was captured and uploaded in the artifact; the earlier audit found 31 entries and zero Brazil matches. That only describes the captured RSS window; it does not prove no older transaction exists.
- The artifact does not contain the BCB registered payload XML itself. The BCB browser retrieval previously failed on XML content type. Therefore this part does not independently reparse the BCB payload's schemaLocation/structureRef or compare it to the current PA.
- No selected PA Changelog/revision export was captured. PA chronology remains UNKNOWN.

## 5. CI hygiene repair — one-time archive workflow
- Multiple pushes updating only research documentation triggered .github/workflows/persist_imf_emde_panel.yml and ended as failure with no jobs and no artifacts. Examples verified: runs 44548677773 and 44548701772; both return empty job lists and empty artifact lists. This is not an executed research failure; the workflow's persistence job did not run.
- The WEO/IMF EMDE archive is already committed in docs/evidence/imf_bop_emde_20261119/; the workflow is a one-time persistence workflow, not a continuous collector.
- Updated .github/workflows/persist_imf_emde_panel.yml to retain only workflow_dispatch and remove the push path trigger. No scripts, data, production selectors, scores, weights or collectors changed.
- Workflow edit commit: 0e9260223baf0bad766e5c68ee15568a28cfd878.
- Re-fetched workflow from GitHub and confirmed manual-only trigger. This prevents routine documentation commits from invoking the one-time archive workflow. Manual replay remains available if explicitly needed.

## Acceptance matrix
| Gate | Status | Reason |
|---|---|---|
| Continuation 76 workflow run | PASS | run 44533595369, job success |
| Artifact download / digest | PASS | artifact 14534769007; exact SHA-256 match |
| Four structure HTTP responses | PASS | 4/4 HTTP 200 |
| Manifest bytes / hashes | PASS | 4/4 exact matches |
| SDMX XML parsing | PASS | 4/4 valid Structure XML |
| Brazil PA -> BOP6 / BR1 | PASS | exact nested refs |
| BOP6 vs BOP_BPM6 separate IDs | PASS | distinct maintainables; shared DSD only |
| Brazil PA revision/changelog | UNKNOWN / BLOCKED | no selected export |
| BCB payload structureRef vs PA | NOT_RECHECKED | payload XML not in this artifact |
| BOP6/BOP_BPM6 alias or Brazil-specific crosswalk | NOT_PROVEN | no official mapping evidence |
| Brazil Reconstruction admission | BLOCKED | identity/chronology external dependency remains |
| EMDE persistence workflow trigger hygiene | PASS | manual-only trigger re-fetched |

## Rejected / excluded
- No retry of transaction-ID-2 HTTP 500 endpoints.
- No inference of BOP6/BOP_BPM6 alias from shared DSD or similar names.
- No inference that absence of Brazil PA in the current BOP_BPM6 response proves historical absence.
- No claim that the selected Brazil PA Changelog is empty.
- No production integration, macro weighting, aggregate, or trading admission.
- No credentials, cookies, authenticated UI or registration writes.

## Next exact actions
1. Brazil: obtain authorized owner-side exact PA IMF:BR_BOP_BP6(1.0) Changelog/Revisions/Compare export and matching IMF:BR1 registration detail export. The IMF guide confirms registration is private/authenticated; no bypass.
2. Brazil: obtain the original BCB payload XML through the official BCB endpoint via reproducible GET capture; parse root schemaLocation/structureRef, provider/dataflow metadata and dataset dimension values. Browser content-type failure is not endpoint failure. Compare only exact structure references, not filenames.
3. GCR: resolve Chile current-vintage Q1/Q2 revision matrix and India 2026-Q1 REVIEW; preserve source vintages and missingness. Do not publish a full 154-member aggregate while 40 countries have no selected-entry observations and 83/308 country-entry cells are empty.

## Invariants
₹0, official/free sources only. No synthetic data, guessed IDs, fabricated timestamps, guessed hashes or inferred aliases. UNKNOWN is never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged.
