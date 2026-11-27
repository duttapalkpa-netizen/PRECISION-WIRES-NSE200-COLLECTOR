# GCR Continuation 277 — Part-7 regression gate recheck and export-recovery scope correction
Date: 2026-11-27 (Asia/Kolkata)

## 1. Preflight and no-repeat
Re-read the default-branch Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, C275 dispatch/access report, C276 Part-6 report and Failure Lessons Register. Re-read Library Mother File and the Phase-5 image reconciliation / Phase-6 recovery checklist. Reused all prior PASS evidence; no repeated matrix QA, code patch, workflow creation, NSE raw acquisition, ZIP/XLSX integrity check or attachment checklist generation.

## 2. Isolated regression workflow configuration re-read
On branch `audit/prospective-selector-tracking`, workflow `.github/workflows/macro_geo_archive_contract_regression.yml` is still present, blob SHA-1 `dd64726cd9da2690fea1e47b7a31b21886b0f823`. It has `workflow_dispatch`, 5-minute job timeout, pytest-only network-free AST test, writes `outputs/macro_geo/archive_report_contract_validation.json`, and uploads artifact `macro-geo-archive-contract-regression`.
No actual workflow Run URL/ID was supplied or verified during this continuation. The connected GitHub action inventory still exposes no dispatch action and no general workflow-run listing action. Therefore no job ID, artifact ID, test outcome or JSON read-back is established. Regression remains NOT_VERIFIED / PENDING. Do not infer PASS from workflow configuration, commit status, or missing run lookup.

## 3. Library Data Export status — reconcile newer phases
The C276 summary cited Phase-2's earlier state. This continuation also re-read newer Library Phase-5 and Phase-6 records:
- Phase-4 non-image 53-name reconciliation is treated as closed by Phase-5: 51 filename+size matches, 2 NOT_FOUND (presence-only, not cryptographic identity).
- Phase-5 image reconciliation: 322 unique image attachment IDs; 106 exact filename+size matches; 216 NOT_FOUND; zero size mismatches. The 106 matches are presence-only, not byte identity.
- Phase-6 checklist generation: 216 image rows, 8 fields, checklist PASS. Recovery of those 216 payloads NOT_DONE / BLOCKED.
- `export_manifest.json`, exact .dat paths and expected payload hashes remain unavailable. Original export byte identity remains UNKNOWN/BLOCKED.
- Do not repeat prior Phase-1/2 hash/container checks, Phase-3 index creation, Phase-4 non-image reconciliation, Phase-5 image listing, or Phase-6 checklist generation. Do not upload duplicate Library copies. Reopen export recovery only when the original `export_manifest.json` and/or exact mapped payload bytes are supplied.

## 4. Acceptance
| Gate | Status |
|---|---|
| Existing workflow config / isolated 5-minute scope | VERIFIED |
| Actual regression run | NOT_VERIFIED / PENDING |
| pytest result and JSON artifact read-back | NOT_VERIFIED |
| Macro-Geo P0 | BLOCKED |
| Strict GCR hard gate | BLOCKED / NOT_AUTHORIZED |
| candidate_release_allowed | false |
| Overall GCR | NOT_COMPUTABLE / NOT_CERTIFIED |
| Phase-4 non-image filename+size reconciliation | 51 MATCH / 2 NOT_FOUND (presence only) |
| Phase-5 image filename+size reconciliation | 106 MATCH / 216 NOT_FOUND / 0 SIZE_MISMATCH (presence only) |
| Phase-6 image recovery checklist | PASS (216 rows); actual recovery NOT_DONE |
| Export manifest / .dat identity | NOT_PROVIDED / UNKNOWN |

## 5. Exact next action
The only GCR engineering gate remains an actual execution of the existing workflow. User/authorized operator runs “Macro-Geo Archive Contract Regression (Audit Only)” on branch `audit/prospective-selector-tracking` and supplies its Actions Run URL/ID. Then inspect pytest step, logs, artifact metadata and JSON evidence; require a passing test and valid read-back before acceptance. Only after that may separate bounded audit-only Macro-Geo recovery be considered using retained Run #398 handoff artifact #14757294944, without re-acquiring NSE raw history.

## 6. Protected invariants
₹0; free official sources only; no IMF re-query, cohort rebuild, synthetic data, guessed IDs/timestamps, NSE raw re-acquisition, production selector/ranking/threshold change, merge or production integration. UNKNOWN is neither PASS nor FAIL. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 remain unchanged. Workflow runtime <=10 minutes.
