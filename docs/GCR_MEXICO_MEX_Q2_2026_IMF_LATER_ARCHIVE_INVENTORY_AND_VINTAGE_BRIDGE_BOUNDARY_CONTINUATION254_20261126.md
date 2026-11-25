# GCR Continuation 254 — Mexico (MEX) Q2-2026 later IMF archive inventory / vintage bridge boundary
Date: 2026-11-26 (Asia/Kolkata)

## Decision
The existing repository and accessible Library search were checked for an already archived IMF BOP snapshot later than 19-Nov-2026 that could be compared with Banxico's 25-Nov Q3 release. The only MEX exact-key IMF receipt located in the repository is the 19-Nov-2026 exact-sample archive under `docs/evidence/imf_bop_emde_20261119/`. No later MEX A_NFA_T/L_NIL_T raw snapshot, later IMF receipt timestamp, or versioned observation archive was located in the bounded repository/Library search. This is a negative inventory result, not proof that no later IMF snapshot exists elsewhere. No IMF request was made. MEX remains DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity / source preflight
- Re-fetched the current default-branch Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country national validation matrix.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`.
- Re-opened MEX C137 (original Banxico–IMF numeric reconciliation), C208 (matrix evidence-link correction) and C246 (25-Nov Q3 release / first-release revision comparison).
- Reused the 25-Nov Banxico Q3 comparison already completed in C246; did not re-extract the same Banxico Q3 PDF or repeat the 25-Aug vs 25-Nov portfolio-row comparison.
- Selection target was solely C246's open next action: determine whether a later IMF vintage already exists in the repository archive. No IMF API call, query, or cohort rebuild was performed.

## 2. Repository IMF archive inventory
- Controlling broad panel report: `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`, blob SHA-1 `192a425b42eb53008a043b8afc0bf93c10e8d0c4`; report date and capture window: 19-Nov-2026 UTC.
- Controlling exact-sample receipt: `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`, blob SHA-1 `053fa26e9feaab26d5bb4c35911a09fc3f71d1bd`.
- Broad raw panel asset CSV: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, blob SHA-1 `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
- Broad raw panel liability CSV: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, blob SHA-1 `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
- The exact-sample summary records 24/24 exact requests successful and 1,106/1,106 exact-to-broad matches. It is explicitly a 19-Nov receipt; it does not provide a later observation vintage.
- Targeted GitHub repository searches for MEX exact-key archive paths and IMF BOP/EMDE archives dated 20–26-Nov returned no later MEX archive or newer dated IMF panel artifact. A Library search for later MEX/IMF archive material returned conversation-export records and no later IMF raw receipt. These are bounded search results, not a claim of exhaustive byte-level repository-tree enumeration.

## 3. Exact MEX IMF rows and receipt metadata (reused, not refreshed)
From the archived raw CSVs:
- Asset: `MEX,A_NFA_T,P_F,USD,Q,2026-Q2`, OBS_VALUE `8937255098`, SCALE=6, PRECISION=6.
- Liability: `MEX,L_NIL_T,P_F,USD,Q,2026-Q2`, OBS_VALUE `10561285114`, SCALE=6, PRECISION=6.
From the exact-sample receipt:
- Asset retrieved_at_utc: `2026-11-19T06:45:19.095563+00:00`; HTTP 200; 4,893 bytes; SHA-256 `a404aca5a719b9558e75b9483b925d18011fa2d9199937d275956782a84c5014`.
- Liability retrieved_at_utc: `2026-11-19T06:45:19.493209+00:00`; HTTP 200; 4,741 bytes; SHA-256 `1a7de8eb3d258875fbffbde987ce22db437eadbdd9c93e05acec12a4ab7785c7`.
- These remain the archived 19-Nov receipt values; no scale conversion or new numeric reconciliation was performed in this continuation.

## 4. Banxico comparison carried forward from C246
C246 already compared the 25-Aug-2026 first-release Q2 table with the 25-Nov-2026 Q3-release Q2 table:
- Portfolio assets: USD 8,937m → USD 9,480m (+USD543m).
- Portfolio liabilities: USD 10,561m → USD 10,561m (unchanged).
- The archived 19-Nov IMF values match the first release within whole-USDm rounding, but the asset does not match the latest Banxico Q3 snapshot: C246 residual +USD542.744902m against the Q3 asset value; liability residual -USD0.285114m remains within ±USD0.5m.
- C246 also records that Banxico did not publish a portfolio-specific Q2 revision timestamp/version identifier. The principal revision footnote does not independently identify portfolio rows.
- No newer IMF snapshot in the accessible repository inventory can presently adjudicate whether the 19-Nov IMF asset reflects the pre-revision or post-revision Banxico vintage.

## 5. Acceptance / gate disposition
| Gate | Result |
|---|---|
| Current Ledger / Queue / Registry / Matrix preflight | PASS |
| Library Mother File 1–53 read | PASS |
| C137/C208/C246 controlling MEX reports reviewed | PASS |
| Existing IMF exact MEX asset/liability receipt located | PASS — 19-Nov-2026 only |
| Existing broad IMF panel receipt located | PASS — 19-Nov-2026 only |
| Later IMF MEX raw snapshot dated after 19-Nov found in repository search | NOT_FOUND in bounded search |
| Later IMF MEX raw snapshot in accessible Library search | NOT_FOUND in bounded search |
| New IMF request/query | NOT_PERFORMED (prohibited for this task) |
| Banxico Q2 portfolio revision amount | C246: asset +USD543m; liability unchanged |
| Banxico–IMF same-vintage identity | NOT_ESTABLISHED |
| MEX asset gate | REVIEW |
| MEX liability gate | PASS (prior gate retained) |
| MEX vintage gate | PENDING |
| MEX full national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 6. Exact next action / duplicate prevention
- Do not repeat the IMF query or rebuild the 154-country panel/cohort.
- Reopen MEX only if a later IMF raw snapshot is added to the repository with a verifiable receipt timestamp and raw hashes, or Banxico publishes an observation-specific Q2 portfolio revision/version record that can be matched to an IMF vintage.
- If neither appears, preserve the mismatch and PENDING vintage state and advance to the next eligible fixed-cohort member. Never infer that the archived 19-Nov IMF row is the current Banxico vintage merely because it matched the 25-Aug first release.
- No net-to-leg inference, no invented revision timestamp, no aggregate promotion.

## 7. Protected invariants
₹0; free official sources only. No new IMF query, cohort rebuild, synthetic data, imputation, forward-fill, sign/scale conversion, or aggregate authorization. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E and IPO-PLX V2.0 remain unchanged. No merge, workflow dispatch or production integration.
