# PRECISION-WIRES V11.3 — Chapter 32 Progress Log
Date: 2026-11-17 (Asia/Kolkata)
Module: Global Capital Rotation & Relative-Attraction Overlay
Handover source: Chapters 1–31 continuity context plus GitHub records inspected at commit 645e66c50f2415cff6b5e4c6e19e84fc94e1c59c.
Status: CHAPTER 32 WORK PACKAGE OPEN; RAW CAPTURE RUNTIME NOT VERIFIED.

## 1. Completed Tasks (prior verified work; not repeated)
- H.10 official raw capture workflow #8 / run 44036104490: PASS; raw payload 2,088,268 bytes; SHA-256 c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- H.10 valid OBS_STATUS=A rows 5,231; 214 OBS_STATUS=ND sentinel rows excluded.
- Regression workflow #232 / run 44036012995: 72 tests PASS.
- One-vintage 20-prior-valid-observation calculation: 2026-10-15 121.5693 to 2026-11-13 122.6503, +0.8892047581%; research-only, not ICE DXY, not Indian trading sessions.
- Five-date H.10 JRXWTFB_N.B vs FRED DTWEXBGS displayed comparison: 5/5 exact, including 2026-11-11 unavailable.
- Official 2019 Broad Dollar Index re-indexing explanation found; Jan-2006=100 basis and factor 1.014163 documented. Do not reapply factor to already re-indexed post-2019 values.
- H.10 current release HTML confirms JAN06=100; stale H.10 Preview label conflict documented.
- Fed DDP retirement risk, official FRED route, and crosswalk schema/column names documented. Exact crosswalk row JRXWTFB_N.B -> DTWEXBGS remains unverified.
- Existing five-date preview comparison, 72-test regression and H.10 raw capture were not repeated in this chapter.
- Earlier Chapter 31 continuity context: 2,997 historical stocks excluded, 5,880 duplicate signal keys blocked, 17,640 trades audited; exact stock symbols/rejection reasons are not contained in this log and must be retrieved from their original exclusion artifact before naming them.

## 2. Rejected / Excluded List
- H.10 214 OBS_STATUS=ND numeric-sentinel rows excluded from numeric observations; preserve as unavailable, never convert to zero.
- 2,997 historical stocks and 5,880 duplicate signal keys were excluded/blocked in prior Chapter 31 work; do not reprocess. Exact symbols and individual reasons are not verified in this checkpoint.
- Future-dated or stale cash-flow archive snapshots are not admissible as current evidence.
- Do not conflate Federal Reserve Nominal Broad Dollar Index with ICE DXY.
- Do not treat IMF portfolio positions (PIP/CPIS) as portfolio transaction flows (BOP).
- Do not promote FRED DTWEXBGS based only on name similarity or five displayed matching dates.
- No synthetic observations, inferred timestamps, forward-filled missing values, or fabricated hashes.

## 3. Chapter 32 Work Completed in This Session
- Created isolated branch: `research/h10-fred-byte-capture-20261117` from `main`.
- Added bounded 8-minute research-only workflow: `.github/workflows/h10_fred_official_byte_capture.yml`.
- Added standard-library Python capture/parser: `scripts/research/capture_h10_fred_official_bytes.py`.
- Added workflow acceptance and operating note: `docs/GLOBAL_CAPITAL_ROTATION_H10_FRED_CAPTURE_WORKFLOW_20261117.md`.
- Workflow targets three official payloads: Board DDP/FRED crosswalk CSV, public FRED DTWEXBGS graph CSV, and Federal Reserve H.10 XML ZIP.
- Script records raw byte length, SHA-256, final URL, HTTP status, response headers and per-source retrieval timestamps; parses crosswalk by named columns and requires exactly one H10/JRXWTFB_N.B -> DTWEXBGS row; validates FRED CSV headers and H.10 ZIP CRC; writes manifest and preserves artifact even on failure.
- Latest script hardening commit: `12e9efc540cd412811c57c784dc380fd16103a77`.
- Workflow file commit: `752589192bcd87fa91d97b256e7011f20e780ff3`.
- Initial script commit: `689a622ba307dc99a275114e55b09ffc5fac394c`.
- Capture workflow documentation commit: `2f315af400470d618907863b25a5192b79061e9e`.
- All three files fetched back from the isolated branch and content-checked. No production files changed.

## 4. Next Action Items (exact order; do not repeat completed work)
1. Check GitHub Actions for the push-triggered run on branch `research/h10-fred-byte-capture-20261117`; if absent, manually dispatch `H10 FRED Official Byte Capture (Research Only)` once. The connected GitHub interface in this session did not expose a workflow-dispatch action, so no run ID is claimed.
2. Inspect the artifact even if the run fails. Verify the three raw files, HTTP metadata, byte counts, SHA-256 values, exact crosswalk row and ZIP CRC.
3. If capture passes, parse H.10 XML schema and perform full daily date/value/status reconciliation against FRED CSV; report matches, mismatches, missingness, duplicates, and pre-/post-2019 boundary separately.
4. Capture a second dated publication vintage and produce a revision-difference report before claiming point-in-time replay capability.
5. Only after these gates pass, propose a source alias/adapter; registry promotion, collector migration and classifier integration remain unauthorized.
6. After H.10/FRED gate, resume separate outstanding India-source work: CDSL/NSDL FPI historical raw archive and RBI DBIE USD/INR raw CSV, without confusing reference rate with interbank observations. Do not claim these acquired.

## 5. Acceptance / Progress
- Prior H.10 capture and 72-test regression: PASS (existing evidence; not rerun).
- New workflow/script implementation and fetch-back review: 100% of this bounded code work package.
- GitHub Actions runtime: NOT_VERIFIED.
- Three raw payloads / SHA-256 / manifest: NOT_DONE.
- Exact crosswalk row: NOT_VERIFIED.
- Full-history H.10/FRED reconciliation: NOT_RUN.
- Second vintage / revision archive / PIT replay: NOT_DONE.
- Registry migration / production integration: NOT_AUTHORIZED.
- Overall overlay percentage: NOT_CALCULABLE from this bounded work.

## 6. Protected Invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. Research-only; no PR merge or production integration. UNKNOWN is neither PASS nor FAIL. ₹0 spend; free official sources only; no synthetic data or fabricated provenance. CI target <10 minutes.
