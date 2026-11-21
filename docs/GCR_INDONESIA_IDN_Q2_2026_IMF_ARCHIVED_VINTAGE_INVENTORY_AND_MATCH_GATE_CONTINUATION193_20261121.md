# Indonesia (IDN) Q2-2026 — IMF archived-vintage inventory and BI match gate (Continuation 193)
Date: 2026-11-21 (Asia/Kolkata)
Decision: NO LATER IMF SNAPSHOT OR OBSERVATION-LEVEL REVISION METADATA WAS FOUND IN THE CURRENT REPOSITORY ARCHIVE. THE ONLY PRESERVED IMF EXACT-KEY TRANSPORT RECEIPT FOR IDN IS THE 19-NOV-2026 SNAPSHOT, WHICH PREDATES THE BANK INDONESIA Q3-2026 REPORT PUBLISHED 20-NOV-2026 THAT REVISED Q1–Q2 PORTFOLIO DATA. THE C186 MISMATCH REMAINS VINTAGE-UNRESOLVED. NO IMF GET, COHORT REBUILD OR NATIONAL RE-EXTRACTION. IDN PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, IDN C185 sign-crosswalk report, IDN C186 revision-vintage report, fixed 63-country cohort and archived IMF exact-sample/coverage manifests.
- Reused cohort SHA-256 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8; IDN remains a fixed-cohort member with both Q2 legs present.
- Reused C186 national revision evidence; no duplicate Bank Indonesia Table V.7 extraction, no IMF request and no cohort rebuild.

## 2. Repository archive inventory
- Recursive main tree inventory was checked for IMF snapshot/archive/vintage/revision artifacts and the full docs/evidence/imf_bop_emde_20261119/ tree.
- The preserved IDN exact-key asset/liability CSVs and exact-sample summary.json are under the 19-Nov-2026 archive. The exact-sample receipt records transport retrieval timestamps:
  - A_NFA_T: 2026-11-19T06:45:17.435091Z
  - L_NIL_T: 2026-11-19T06:45:17.874893Z
- Existing raw CSV SHA-256 values remain:
  - A_NFA_T: db7198b4c2ccc7bcbe6c45312506913c71507339c6e7bd609c5e1ff6500aae8b
  - L_NIL_T: 4ec6d04eae8187bd4235c6120f3be5f67972ff32ebfea1accf6cd0a1ab2b4108
- The broader coverage QA manifest is generated 2026-11-19T06:55:17.094910Z and explicitly describes the data as a current retrieval snapshot with no point-in-time historical vintages captured.
- No later dated IMF IDN observation snapshot, point-in-time vintage archive, submission timestamp, or revision identifier is present in the repository tree inspected. This is a bounded repository/archive finding, not proof that IMF has no such metadata elsewhere.

## 3. Preserve the existing national revision comparison (not recalculated)
- Bank Indonesia Q3-2026 report published 20-Nov-2026, Table 7 p.37, revised Q2 portfolio assets to -1,466 USDm and liabilities to +11,399 USDm; Box 1 p.28 attributes Q1–Q2 revisions to updated LLD/ULN data.
- Retain the already accepted BI BPM5→IMF BPM6 sign mapping: reverse the BI asset sign only; retain liability sign.
- C186 comparison against the 19-Nov IMF snapshot remains:
  - Assets: BI mapped +1,466 vs IMF +1,487.605237 USDm; residual +21.605237 USDm.
  - Liabilities: BI +11,399 vs IMF +11,440.221642 USDm; residual +41.221642 USDm.
  - Both exceed BI's ±0.5 USDm whole-million rounding bound.
- No evidence permits attributing the residual to IMF revision, or declaring the IMF observation same-vintage with the later BI release.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / C185 / C186 preflight | PASS |
| Fixed cohort IDN row and both IMF legs | PASS (reused) |
| 19-Nov IMF exact raw values, receipt timestamps and SHA-256 | PASS (existing evidence) |
| Repository inventory for later archived IMF snapshot | PASS — none found in current repo tree |
| IMF point-in-time observation/revision metadata in archive | NOT_AVAILABLE |
| BI 20-Nov Q2 revised national values and revision notice | PASS (C186) |
| Same-vintage BI↔IMF observation identity | NOT_ESTABLISHED |
| Latest BI vs archived IMF numeric match | REVIEW / outside rounding |
| IDN full national validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Duplicate decision and next action
- Close the C186 “later IMF snapshot already in repository” branch as NOT_AVAILABLE. Do not issue a new IMF GET or repeat the same archive inventory absent a newly added snapshot/metadata artifact.
- Retain IDN's current mismatch and PARTIAL / NOT PASS status. The next country task must be selected from the same immutable 63-country cohort after a fresh report-history and route-fingerprint preflight.
- No changes to BI sign crosswalk, no net-to-leg back-solving, no interpolation, no scale/sign/FX inference, no synthetic timestamps, no production changes. ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.