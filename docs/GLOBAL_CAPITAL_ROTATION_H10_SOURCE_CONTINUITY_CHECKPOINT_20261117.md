# Global Capital Rotation — Fed H.10 Source Continuity Checkpoint
Recorded: 2026-11-17 (Asia/Kolkata)
Status: SOURCE LIFECYCLE RISK VERIFIED; MIGRATION NOT IMPLEMENTED
Scope: Research-only source continuity; no classifier or production change.

## Prior work explicitly not repeated
- H.10 official raw ZIP capture workflow #8 / run ID 44036104490: PASS.
- Raw payload SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77; 2,088,268 bytes; HTTP 200.
- H.10 valid OBS_STATUS=A rows: 5,231; 214 OBS_STATUS=ND numeric sentinel rows excluded.
- Regression workflow #232 / run ID 44036012995: PASS, 72 tests.
- 20 prior valid observations + current = 21 valid dates; 2026-10-15 value 121.5693 to 2026-11-13 value 122.6503; derived +0.8892047581%. Research-only; not ICE DXY; not Indian trading sessions.
- Independent second-vintage cross-check and PIT replay remain NOT_DONE. Do not claim them complete.

## New official source lifecycle evidence
- Federal Reserve H.10 release page last updated 2026-11-16.
- The Board states the DDP Build Your Package feature was removed during the week of 2026-11-09, in preparation for eventual DDP retirement.
- The Board directs users to Federal Reserve Economic Data (FRED) for data and expanded download options.
- The current H.10 page states the Board normally releases daily bilateral exchange rates and US dollar indexes on Mondays at 4:15 p.m. for the previous business week (next business day when Monday is a Federal holiday).
- Official page: https://www.federalreserve.gov/Releases/H10/
- Official DDP choose page: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- The DDP page snapshot reports the 2026-11-12 announcement that preformatted packages are planned for retirement on 2027-03-31 and the DDP page on 2027-07-01. These are planned dates, not completed events.
- Official series preview confirms H10/H10/JRXWTFB_N.B = Nominal Broad Dollar Index, unit Index:_1997_Jan_100, multiplier 1; latest displayed observation 2026-11-13 = 122.6503 and 2026-11-11 = ND. This matches the captured latest value and ND exclusion logic, but is not a second publication vintage and does not validate all 21 observations.
- Preview URL: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10

## Engineering decision
1. Keep the existing official Federal Reserve H.10 release/series identity as the source definition.
2. Treat the legacy DDP ZIP retrieval route as a migration risk; do not assume it will remain available after retirement milestones.
3. Evaluate FRED as the next official Fed-linked retrieval route, but do not replace the current source URL, registry tuple, or collector until exact series identity, units, observation status, publication/revision vintage, response metadata and raw-payload hash are tested.
4. Keep source identity H10/H10/JRXWTFB_N.B separate from ICE DXY and separate from any dxy_change_pct_20d field.
5. No FRED series identifier is promoted in this checkpoint; no observation is added; no second vintage is claimed.
6. Preserve the current 90-day artifact expiry limitation; durable raw-payload archival remains NOT_DONE.

## Progress and acceptance
- Prior H.10 capture + ND correction + one-vintage 20-observation calculation: already PASS; not repeated.
- Official source lifecycle / migration risk verification: PASS for this bounded checkpoint.
- FRED endpoint and exact-series equivalence qualification: NOT_DONE.
- Second independent publication-vintage comparison: NOT_DONE.
- Long-term raw payload archive in repository: NOT_DONE.
- Historical PIT replay: NOT_DONE.
- Classifier integration: NOT_AUTHORIZED.
- Predictive validation and production use: NOT_AUTHORIZED.

## Next actions (ordered)
1. Inspect the official Fed/FRED linked route and identify the exact corresponding FRED series only if the Fed explicitly links or identifies it; verify description, unit, observation values and date coverage.
2. Capture a second dated publication package with immutable raw bytes, response metadata, retrieval time, SHA-256 and manifest; compare overlapping observations to the first capture and record revisions rather than overwrite.
3. Implement a bounded migration adapter only after equivalence tests pass; retain original Fed source identity and route provenance.
4. Archive the current raw ZIP and subsequent vintages durably in GitHub or a repository-controlled release before 90-day artifact expiry; do not claim archival until bytes and hash are fetched back and verified.

## Invariants
Research-only. No production change, no source-registry promotion, no classifier integration, no automatic stock/sector inference. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is neither PASS nor FAIL. ₹0 spend; no synthetic data or fabricated timestamps/hashes.