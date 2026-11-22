# Macro-Geo P0 Source-Policy Audit — Continuation 250

Date: 2026-11-22
Branch: audit/prospective-selector-tracking
Active workflow: Run #383 (`44992957027`), head `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`

## Continuity check
Read `research/GITHUB_MASTER_CONTINUITY_LEDGER.md`, C249, and inspected the exact P0 collector and repair scripts. PASS work was not repeated. Rechecked the live Run #383 job before choosing this audit.

## Live workflow state
- Corrected-label walk-forward step: SUCCESS.
- P0 market panel and timestamped geopolitical news collection: IN_PROGRESS.
- Four-group Macro-Geo P0 repair: PENDING.
- Remaining source coverage, event study, selector, historical audits, joins and hard-gate steps: PENDING.
- No Run #383 artifact was available at the latest check.

## Source-policy findings from current code
1. `pipeline/macro_geo_collect_p0.py` explicitly uses Yahoo Finance chart API as a secondary fallback for multiple market series after FRED errors. It labels these rows `AVAILABLE_SECONDARY`, but the required-series readiness predicate currently accepts both `AVAILABLE` and `AVAILABLE_SECONDARY`. This can make a non-official fallback satisfy a P0 readiness flag, which conflicts with the project requirement to use official sources only.
2. The same collector uses GDELT DOC 2.0 for news discovery and mixes it with public publisher RSS feeds. The script correctly warns that publication timestamps are proxies, not verified event occurrence timestamps, but this collection is not an official government event source. It must remain media-discovery context, not official event ground truth.
3. `pipeline/macro_geo_repair_p0.py` contains a USD/INR fallback to a community GitHub mirror of RBI/FBIL reference-rate data and labels it `AVAILABLE_SECONDARY`. This is not a direct official RBI/FBIL feed and must not satisfy official-only acceptance.
4. The Brent fallback to US EIA is an official source, but must be separately identified as an official EIA series, not silently treated as FRED. Direct source identity and units remain important.
5. The NSE FPI/DII branch has a strict minimum coverage test (>=60 dated observations spanning >=90 days); retain that gate. Snapshot-only data remains blocked.

## Acceptance decision
- These secondary feeds may be retained for explicitly exploratory context only if clearly separated and never allowed to satisfy official P0 hard gates.
- Official-source acceptance must require an explicit official-source status and source identity. `AVAILABLE_SECONDARY` must never count as official P0 PASS.
- GDELT/publisher RSS publication times must not be represented as confirmed geopolitical occurrence times.
- No code was changed while Run #383 is actively executing its existing checkout; changing pipeline code now would trigger another workflow and could create overlapping/queued runs.

## Next action
After Run #383 completes, patch the audit-branch source gate:
- remove the community GitHub USD/INR mirror as an acceptance fallback; on FRED failure keep USD/INR BLOCKED until an official RBI/FBIL endpoint is verified;
- make Yahoo secondary series ineligible for `required_series_available` and official P0 hard-gate acceptance;
- keep GDELT/RSS as media-publication discovery only, with separate provenance and no verified-event claim;
- retain official EIA Brent provenance where used;
- add regression tests proving `AVAILABLE_SECONDARY` cannot satisfy official P0 readiness and community mirror cannot be marked official;
- run targeted tests only, then record exact CI evidence.

## Invariants
Audit branch only. ₹0 spend; official free sources only for accepted research inputs. No synthetic data, fabricated timestamps, third-party mirrors, or access-control bypass. UNKNOWN/BLOCKED never becomes PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged.
