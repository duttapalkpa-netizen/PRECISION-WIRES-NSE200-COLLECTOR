# Global Capital Rotation — FRED / H.10 Unit and Base-Year Resolution
Date: 2026-11-17 (Asia/Kolkata)
Status: OFFICIAL METHODOLOGY EXPLANATION FOUND; PREVIEW METADATA LABEL DISCREPANCY REMAINS
Scope: Research-only. No source registry or collector migration in this record.

## Prior work not repeated
- H.10 raw capture #8 / run 44036104490; 5,231 OBS_STATUS=A rows; 214 ND rows excluded.
- Regression workflow #232 / run 44036012995: 72 tests PASS.
- H.10 current-vintage 20-prior-valid-observation change: +0.8892047581%, research-only.
- FRED DTWEXBGS versus H.10 JRXWTFB_N.B five-date preview comparison: 5/5 exact displayed match, including 2026-11-11 unavailable.
- Earlier FRED/H.10 equivalence audit is docs/GLOBAL_CAPITAL_ROTATION_FRED_H10_EQUIVALENCE_AUDIT_20261117.md.

## New primary-source evidence
- Federal Reserve H.10 Technical Q&A: https://www.federalreserve.gov/releases/h10/h10_technical_qa.htm
- Federal Reserve FEDS Note, Revisions to the Federal Reserve Dollar Indexes: https://www.federalreserve.gov/econres/notes/feds-notes/revisions-to-the-federal-reserve-dollar-indexes-20190115.html
- Effective 2019-06-24, the daily Broad, AFE and EME dollar indexes were re-indexed so the January 2006 monthly average equals 100, matching the monthly series.
- The Federal Reserve states the re-indexed series equal the prior series multiplied by factors: Broad 1.014163; AFE 1.017881; EME 1.009396.
- The 2019 methodology revision for the new broad index took effect 2019-02-04; the new series has historical observations back to 2006-01-02. The revised index is based on total bilateral trade including goods and services; it is not the old goods-only index.
- FRED DTWEXBGS identifies its unit as Index Jan 2006=100, source as Board of Governors, and release as H.10 Foreign Exchange Rates.
- The currently surfaced H.10 Preview page still labels JRXWTFB_N.B as Index:_1997_Jan_100, while its displayed values match the FRED DTWEXBGS values for the five dates checked. This appears to be a stale or inconsistent preview unit label; do not silently overwrite source metadata.

## Resolution and limitations
- The apparent unit/base conflict has an official methodological explanation: the current daily series was re-indexed in 2019 to Jan-2006 monthly average = 100.
- This supports DTWEXBGS as the likely FRED route for the current post-2019 H.10 daily Broad Dollar Index, but does not yet prove full-history equivalence or all vintage/revision behaviour.
- Do not apply the 1.014163 factor again to the current post-2019 values; they are already on the re-indexed basis. Any historical pre-2019 transformation must be treated as a distinct documented series bridge and tested, not applied blindly.
- Keep the original H.10 series ID JRXWTFB_N.B and FRED series ID DTWEXBGS as separate source identifiers linked by a provisional equivalence record.
- Do not map either series to ICE DXY or to dxy_change_pct_20d.

## Acceptance status
- Official explanation of 2019 re-indexing and Broad factor: PASS.
- FRED unit description Jan-2006=100: PASS.
- H.10 Preview stale/contradictory unit label documented: PASS.
- Full daily overlap comparison: NOT_DONE.
- Pre-2019 / post-2019 boundary and historical bridge validation: NOT_DONE.
- FRED raw payload, HTTP metadata, retrieval timestamp, SHA-256 and immutable manifest: NOT_DONE.
- Registry promotion / collector migration: BLOCKED pending full overlap and raw-evidence tests.
- PIT replay / classifier integration / predictive validation: NOT_DONE / NOT_AUTHORIZED.

## Next bounded action
1. Retrieve complete official H.10 and FRED daily series as raw payloads, with source URLs, retrieval timestamps, HTTP metadata, byte lengths and SHA-256.
2. Compare every overlapping date; separately evaluate dates before and after 2019-06-24, preserving missing values and revisions.
3. Confirm the historical 1.014163 bridge only where the source methodology says it applies; do not double-adjust already re-indexed data.
4. Create a tested migration adapter and source registry alias only after full reconciliation passes.

## Invariants
Research-only; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic data, no fabricated timestamps or hashes, ₹0 spend.