# H.10 Point-in-Time Vintage Reconstruction Contract — 2026-11-13

## Scope and status
Research-only methodology and acceptance contract for reconstructing what H.10 information was actually public at each historical NSE signal timestamp. This document does not claim that the 200-session vintage reconstruction has been executed. It closes the methodology ambiguity and defines the evidence required for a PASS.

Status: METHOD CONTRACT = PASS; RAW VINTAGE ACQUISITION = PENDING; OBSERVATION-LEVEL POINT-IN-TIME JOIN = PENDING; EVENT-STUDY ELIGIBILITY = BLOCKED.

## Verified Federal Reserve publication rules
The Federal Reserve H.10 page states that daily bilateral exchange rates and U.S. dollar indexes for the previous business week are released on Mondays at 4:15 p.m. Eastern Time; if Monday is a Federal holiday, release moves to the following business day. The Country Data page states that the current historical series is updated weekly, while past release pages are an archive of historical H.10 releases and are not revised to reflect later revisions.

Official evidence:
- H.10 release methodology and release dates: https://www.federalreserve.gov/releases/h10/
- Historical H.10 release archive / Country Data: https://www.federalreserve.gov/releases/h10/hist/
- H.10 release archive RSS / delay and correction notices: https://www.federalreserve.gov/feeds/H10.html
- Official statistical release calendar: https://www.federalreserve.gov/data/releaseschedule.htm
- Current H.10 data download package page: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10

Important distinction: the current Country Data time series is not a substitute for historical release vintages. The Fed's H.10 About page explicitly says archived past releases are not revised and may differ from subsequent revisions. The archived release is therefore the point-in-time evidence object; a current revised series alone cannot establish historical availability.

## Canonical reconstruction model
For each H.10 observation:
1. Preserve the observation date, series identifier, raw value, raw missing marker, and source file unchanged.
2. Identify the first actual archived H.10 release whose archived table contains that observation. Record the release page URL, release date, published timestamp, retrieval timestamp, and SHA-256 of the archived source payload.
3. Use the actual release timestamp, not the observation date, as `available_at`. The regular Monday 4:15 p.m. ET schedule is a cross-check, not a replacement for an archived release timestamp.
4. Convert the publication timestamp from America/New_York to UTC and Asia/Kolkata using a timezone database (DST-aware); never hard-code a fixed ET-to-IST offset.
5. For each NSE signal timestamp, the value is point-in-time eligible only when `available_at <= signal_timestamp`. If the archived release was published after the signal timestamp, the value is NOT_YET_PUBLISHED for that signal.
6. If the archived release cannot be located, the release timestamp is ambiguous, or the vintage does not contain the value, classify UNKNOWN. Do not infer availability from the current revised series.
7. Preserve corrections and delayed-release notices as separate append-only evidence. Where an official notice documents a delayed release or correction, the actual affected vintage/timestamp takes precedence over the nominal schedule.
8. Never forward-fill across a missing marker, synthesize an observation, backdate a publication timestamp, or overwrite an earlier vintage.

## Required row-level fields
`series_id, observation_date, raw_value, raw_status, vintage_release_date, vintage_published_at_et, vintage_published_at_utc, available_at_ist, archive_url, archive_payload_sha256, retrieved_at_utc, signal_timestamp_ist, point_in_time_status, reason_code`.

Allowed `point_in_time_status` values:
- `AVAILABLE_AT_SIGNAL_TIME`
- `NOT_YET_PUBLISHED`
- `UNKNOWN`
- `SOURCE_MISSING_MARKER`
- `NO_ARCHIVED_VINTAGE`

## Acceptance tests
- Every one of the 26 H.10 series retains its original series identifier and raw missingness.
- Each claimed vintage is an official archived Federal Reserve release, not a current revised download.
- Every archive payload has a reproducible SHA-256 and byte count.
- Actual release timestamp is evidenced; timezone conversion is DST-aware and reproducible.
- Every historical NSE signal timestamp is joined using `available_at <= signal_timestamp`.
- Delayed and corrected releases are represented without overwriting prior vintages.
- UNKNOWN remains UNKNOWN; no inferred PASS from schedule alone.
- A per-series and per-session reconciliation explains all unmatched observations.
- No synthetic rows, forward-fill, or timestamp fabrication.
- Tests complete within the project's 10-minute workflow budget; split immutable acquisition and deterministic local reconstruction if needed, without weakening acceptance criteria.

## Known verified anchor example
The official H.10 page currently identifies the November 9, 2026 release and states the previous-business-week publication rule. The Federal Reserve statistical release calendar lists H.10 at 4:15 p.m. on November 9 and November 16, 2026. This confirms the schedule for this anchor window only; it does not prove all historical vintage rows for the full 200-session panel.

## Current evidence ledger
- Existing raw H.10 full-history panel: previously verified, 26 series.
- Existing NSE alignment: previously verified, 200 sessions; 190 observed, 6 source missing markers, 4 no-source rows per series.
- Existing raw artifact ZIP digests: previously verified against GitHub artifact metadata.
- Official H.10 publication rule: verified from Federal Reserve H.10 pages.
- Historical release archive semantics (past releases not revised): verified from Federal Reserve H.10 About page.
- Complete archive payloads for all required release dates: NOT YET ACQUIRED.
- Row-level `available_at` reconstruction: NOT YET EXECUTED.
- Historical point-in-time availability: UNKNOWN until the two preceding items pass.
- Matched diagnostic/event study: BLOCKED until point-in-time reconstruction passes.

## Invariants
Research-only. ₹0 spend; free official sources only. No paid API, no external contact, no synthetic data or timestamps. No PR merge without explicit user approval. No changes to Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56 × 12), Engines A–E, or Hard Gate logic.
