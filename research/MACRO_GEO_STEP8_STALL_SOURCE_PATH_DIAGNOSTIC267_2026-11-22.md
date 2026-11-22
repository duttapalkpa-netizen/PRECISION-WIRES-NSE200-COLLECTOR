# Macro-Geo Step 8 Stall and Source-Path Diagnostic — C267

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity check
Re-fetched the Master Continuity Ledger (C266 present), C266 report, and C264 report before work. C254 clipping and C260 holiday-scope PASS work was not repeated. No production code or selector invariants were changed.

## Live workflow state
Run #317 / ID `45001040455`, head SHA `885528a076e98996455358ee236f1a2960a276ea`:
- status IN_PROGRESS; conclusion null; updated_at remains `2026-11-22T08:07:02Z`.
- Job `137143161030` IN_PROGRESS.
- Steps 1–7 SUCCESS.
- Step 8 “Collect P0 market series and timestamped media evidence” IN_PROGRESS.
- Steps 9–19 pending; step 11 official NSDL historical flow collection has not started.
- No artifacts published.
- Job-log download again returned Azure BlobNotFound at 08:22:51Z. This is a log retrieval limitation, not a workflow conclusion.

Run #393 / ID `45001043441` remains completed/cancelled as documented in C266; no new evidence was inspected from its binary artifact.

## Source-path inspection
Fetched workflow YAML `.github/workflows/macro_geo_p0_event_study.yml` (blob `c7c6683494c90cdbaa18f81ee2bfe1ff11294b49`) and collector `pipeline/macro_geo_collect_p0.py` (blob `7feb0bab9a2843149f0b2191310e3a212a80e1df`).

The workflow's step 8 runs the complete `macro_geo_collect_p0.py` script. The script performs, in sequence:
1. NSE Indices historical API bootstrap and multi-index requests.
2. If official API coverage is under 100 rows, bounded recent official NSE daily-index archive requests (up to 550 calendar days).
3. Yahoo historical fill for missing benchmark/sector/volatility dates, explicitly labelled secondary.
4. GLOBAL VIX Cboe then FRED fallback.
5. FRED and Yahoo collection for remaining registered macro series, with bounded retries/chunks.
6. GDELT 14-day slices across a 90-day publication window, including up to three attempts and retry sleeps.
7. Five direct publisher RSS feed requests.
8. NSE corporate-announcement and FPI/DII endpoint attempts.
9. Writes collection outputs and manifest only after the above collection sequence.

This explains why step 8 is a large, serial collection stage. However, the missing job log prevents identifying which specific request or substage is currently waiting. No precise root cause is proven; the observed fact is only prolonged IN_PROGRESS with unchanged updated_at.

The workflow has concurrency group `macro-geo-p0-audit-v5` and `cancel-in-progress: true`. Therefore launching a duplicate run in the same group can cancel an existing run. No duplicate dispatch is warranted.

## Decision
Do not edit the collector or workflow while Run #317 is active. Do not dispatch a duplicate run. The highest-value next step remains waiting for the active run to advance, then inspect its job step transitions and artifact. If it completes or fails, use exact job logs/step evidence to isolate the slow or failing request before designing any bounded-timeout/checkpoint repair.

## Rejected
- Rejected claiming GDELT, FRED, NSE archive, Yahoo, RSS or NSE endpoint as the proven cause; logs are unavailable.
- Rejected treating BlobNotFound as run failure.
- Rejected treating step 8 IN_PROGRESS as success.
- Rejected duplicate run dispatch because concurrency cancellation is enabled.
- Rejected speculative code edits while the active run consumes the collector.
- Rejected claiming NSDL 2026-07-17 or 2026-08-26 was queried; step 11 is pending.
- No paid API, synthetic data, guessed timestamps, third-party mirror, or production changes.

## Exact next actions
1. Re-poll Run #317 and job `137143161030` after updated_at or step state changes.
2. If step 8 completes, verify steps 9–11 and inspect the artifact, especially exact official NSDL outcomes for 2026-07-17 and 2026-08-26.
3. If step 8 fails or times out, obtain its logs/annotations and isolate the exact request/substage before any repair.
4. If the workflow remains active with unavailable logs, preserve IN_PROGRESS and do not dispatch a competing run.
5. Keep USD/INR and mature event windows BLOCKED; keep unresolved NSDL dates UNKNOWN.
6. Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged.
