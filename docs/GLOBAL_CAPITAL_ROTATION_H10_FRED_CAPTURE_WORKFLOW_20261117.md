# H.10 / FRED Official Raw-Byte Capture Workflow
Date: 2026-11-17 (Asia/Kolkata)
Status: IMPLEMENTED ON ISOLATED RESEARCH BRANCH; RUNTIME NOT YET VERIFIED

## Purpose
A bounded, research-only GitHub Actions job to acquire the official Federal Reserve DDP/FRED crosswalk CSV, public FRED DTWEXBGS graph CSV, and Board H.10 XML ZIP using a byte-capable runner. Preserve raw bytes and HTTP metadata before parsing.

## New files
- `.github/workflows/h10_fred_official_byte_capture.yml`
- `scripts/research/capture_h10_fred_official_bytes.py`

## Acceptance behavior
- Three official payloads must download with HTTP 200 and non-empty bytes.
- Every raw payload receives byte length and SHA-256 in `h10_fred_capture/manifest.json`.
- Crosswalk is parsed by named columns `ddp_release`, `board_series_id`, `fred_series_id`; exactly one H10/JRXWTFB_N.B row must map to DTWEXBGS.
- FRED CSV must contain `observation_date` and `DTWEXBGS`.
- H.10 ZIP CRC is checked; full XML parsing and date-level reconciliation are deliberately separate follow-up gates.
- Artifact upload uses `if: always()` so failure evidence is retained; retention 90 days.
- Workflow timeout is 8 minutes; no paid API, API key, production change, or source-registry promotion.

## Current state
- Workflow and script committed to isolated research branch.
- Runtime dispatch is not available through the connected GitHub actions interface in this session; no run or artifact is claimed.
- Until a run completes and its artifact is inspected, all raw-byte capture, exact crosswalk-row, full-history comparison and vintage acceptance remain NOT_DONE / UNKNOWN.
- The next manual step is one `Run workflow` dispatch on this branch. Inspect artifact even on failure before any code change.

## Invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. Research-only. UNKNOWN never PASS. No synthetic data or fabricated timestamps/hashes. ₹0 spend.
