# H.10 Vintage Archive Discovery and Revision Risk Audit — 2026-11-13

## Scope
Research-only source discovery for the already-defined H.10 point-in-time vintage reconstruction. This is not a raw-vintage acquisition and does not claim row-level availability has been reconstructed. Existing raw panels and NSE-200 alignment are not re-ingested.

## Newly verified official-source findings

### 1. Official H.10 publication cadence
The Federal Reserve H.10 page states that daily bilateral exchange rates and U.S. dollar indexes for the previous business week are released Mondays at 4:15 p.m. Eastern Time, shifted to the following business day when Monday is a Federal holiday. The Country Data page says data are updated Mondays at 4:15 p.m. and extend through Friday of the previous business week.
Sources:
- https://www.federalreserve.gov/releases/h10/
- https://www.federalreserve.gov/releases/h10/hist/default.htm

### 2. Historical release vs current revised data
The Federal Reserve H.10 About page distinguishes:
- Release Dates: archive of historical H.10 releases; past releases are not revised and may differ from subsequent revisions.
- Country Data: historical bilateral rates current through the latest H.10 release and updated weekly.
Therefore Country Data/current DDP values cannot be substituted for the archived release vintage when proving what was known at an earlier signal time.
Source: https://www.federalreserve.gov/RELEASES/H10/About.HTM

### 3. Material correction notice discovered
The Federal Reserve H.10 RSS/announcement feed reports that the August 10, 2026 release contained incorrect August 3 values for all currencies and dollar indexes due to a technical issue; the issue was corrected on August 12, 2026, and corresponding DDP entries were corrected.
Source: https://www.federalreserve.gov/feeds/H10.html

Decision: treat the August 10 release and August 12 correction as separate immutable vintage events. The corrected current DDP value must not overwrite or be backdated into the August 10 first-published vintage. Any signal between the original publication and correction must use the value actually available then, if the archived payload is recoverable; otherwise status UNKNOWN.

### 4. ALFRED release-date list is a discovery index, not a complete vintage payload
The St. Louis Fed ALFRED H.10 release-date download page identifies the release as H.10 Foreign Exchange Rates and describes its release dates as dates when any series from the release was revised. It explicitly notes that dates may come from the source, data providers, or first availability in FRED if a date cannot be determined. The visible index currently ends at 2026-10-13, while the Federal Reserve H.10 page is updated through November 9, 2026.
Source: https://alfred.stlouisfed.org/release/downloaddates?rid=17

Decision: ALFRED release dates may help enumerate candidate vintage/revision dates but are not sufficient proof of exact publication timestamp or per-series archived content. Do not treat the date list as a substitute for Federal Reserve archived payloads.

### 5. Historical release archive access path
The Federal Reserve H.10 Release Dates page and historical Country Data page are publicly accessible. Country Data exposes historical country tables (including India) but represents current historical series, not a set of immutable weekly release payloads. The current release page also exposes an XML download, but the observed link is a current release package and is not evidence that date-specific historical XML packages were acquired.
Sources:
- https://www.federalreserve.gov/releases/h10/
- https://www.federalreserve.gov/releases/h10/hist/default.htm

## Acquisition status and next technical gate
- Official release cadence: VERIFIED.
- Archived-vintage semantics: VERIFIED.
- August 10 / August 12, 2026 correction event: VERIFIED.
- ALFRED release-date index semantics and cutoff limitation: VERIFIED.
- Immutable historical payloads covering every required H.10 release: NOT ACQUIRED.
- Actual publication timestamps per vintage: NOT VERIFIED.
- Row-level available_at reconstruction for the 26 series × 200 NSE sessions: NOT EXECUTED.
- Point-in-time eligibility: UNKNOWN.
- Matched event study: BLOCKED.

Next action must obtain the original archived weekly H.10 release payloads (including the August 10 and August 12 correction states), preserve exact bytes, URL, release date, retrieval timestamp, byte count, and SHA-256, then reconstruct availability using actual publication evidence and DST-aware America/New_York timezone conversion. If date-specific archived payloads or timestamps cannot be established from free official sources, keep affected rows UNKNOWN and stop; do not infer availability from a nominal Monday schedule.

## Invariants
Research-only. ₹0 spend, free official sources only, no paid APIs or external contact. No synthetic values/timestamps, no forward-fill, no backdating, no overwriting vintages. UNKNOWN is neither PASS nor FAIL. No PR merge without explicit user approval. No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Engines A–E, or Hard Gate.


## Follow-up: date-specific archived release pair located
A targeted archive-path search located both date-specific Federal Reserve weekly H.10 release pages for the correction case:
- Original release dated 2026-08-10: https://www.federalreserve.gov/releases/h10/20260810/
- Corrected release dated 2026-08-12: https://www.federalreserve.gov/releases/h10/20260812/

The two official HTML pages expose the same observation week (Aug 3–7) with materially different Aug 3 values. Example: India INR per USD is 95.9100 in the Aug 10 release and 95.3400 in the Aug 12 corrected release. The Broad Dollar Index is 120.7739 vs 119.6951; AFE is 114.2972 vs 112.8653; EME is 129.0609 vs 128.3599. The remaining Aug 4–7 entries shown in these tables match for these four example series. This confirms a real first-publication/correction vintage difference, not merely a generic theoretical revision risk.

Evidence: official Federal Reserve archived HTML release pages above, plus the official H.10 correction announcement dated Aug 12 at https://www.federalreserve.gov/feeds/H10.html.

Limitations: web inspection established the archived page contents and release dates, but the raw HTML payloads were not downloaded into the research archive in this run; therefore no byte count or SHA-256 is claimed for these two pages. The release dates are explicit, but an exact intraday publication timestamp for the Aug 12 correction has not yet been established. Do not convert the Aug 12 date to a guessed 4:15 p.m. timestamp; keep intraday availability UNKNOWN until independently evidenced.

Status update:
- Archived page pair discovery for the Aug 10 / Aug 12 correction case: PASS.
- Direct raw payload acquisition + SHA-256: PENDING.
- Exact Aug 12 correction publication time: UNKNOWN.
- Full required vintage archive acquisition: PENDING.
- Row-level 26 × 200 point-in-time reconstruction: PENDING.
