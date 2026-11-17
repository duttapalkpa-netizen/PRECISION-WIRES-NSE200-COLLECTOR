# Global Capital Rotation — FRED / H.10 Broad Dollar Equivalence Audit
Date: 2026-11-17 (Asia/Kolkata)
Status: STRONG OBSERVATION MATCH; UNIT METADATA CONFLICT; MIGRATION BLOCKED
Scope: Research-only source equivalence review. No source registry or collector change.

## Prior work not repeated
- H.10 capture workflow #8 / run ID 44036104490: PASS; raw payload SHA-256 c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- H.10 valid observations 5,231; OBS_STATUS=ND numeric sentinel rows excluded 214.
- Regression workflow #232 / run ID 44036012995: PASS, 72 tests.
- Existing one-vintage 20-prior-valid-observation calculation +0.8892047581% remains research-only and is not repeated.
- DDP retirement risk already recorded in docs/GLOBAL_CAPITAL_ROTATION_H10_SOURCE_CONTINUITY_CHECKPOINT_20261117.md.

## Candidate FRED series
- FRED series: DTWEXBGS, Nominal Broad U.S. Dollar Index.
- FRED series URL: https://fred.stlouisfed.org/series/DTWEXBGS
- FRED graph URL: https://fred.stlouisfed.org/graph/?graph_id=1628604
- FRED describes source as Board of Governors of the Federal Reserve System (US), release H.10 Foreign Exchange Rates, daily frequency.
- Federal Reserve H.10 raw series identity remains H10/H10/JRXWTFB_N.B, Nominal Broad Dollar Index.
- Official H.10 preview: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10

## Displayed overlapping observations
| Date | H.10 JRXWTFB_N.B | FRED DTWEXBGS |
|---|---:|---:|
| 2026-11-13 | 122.6503 | 122.6503 |
| 2026-11-12 | 122.5433 | 122.5433 |
| 2026-11-11 | ND | missing (.) |
| 2026-11-10 | 122.1143 | 122.1143 |
| 2026-11-09 | 121.6623 | 121.6623 |
- These five displayed points match exactly, including the unavailable observation on 2026-11-11.
- This is strong evidence of a matching H.10 data lineage and candidate route equivalence, but only a five-point web-preview comparison, not a full-series byte-for-byte or multi-vintage reconciliation.

## Blocking metadata discrepancy
- H.10 Preview reports unit Index:_1997_Jan_100 and multiplier 1.
- FRED DTWEXBGS page reports Index Jan 2006=100.
- The displayed numeric observations nevertheless match exactly for the five checked dates.
- Do not silently normalize, relabel, or choose one unit definition. The unit/base-year conflict must be explained by the source owner or an archived official methodology/series metadata document before migration.
- This candidate is not ICE DXY and must not be mapped to dxy_change_pct_20d.

## Decision
- Candidate identity/lineage: PROVISIONAL_MATCH (5/5 displayed dates).
- Frequency and broad nominal index concept: MATCH at displayed metadata level.
- Unit/base-year metadata: CONFLICT / UNKNOWN.
- Full historical overlap, revisions/vintages, API/raw CSV payload, response headers, retrieval timestamp, raw SHA-256 and evidence manifest: NOT_DONE.
- Source registry promotion: NOT_AUTHORIZED.
- Collector URL migration: BLOCKED pending unit/base-year resolution and full overlap QA.
- Existing H.10 route remains canonical until migration acceptance.

## Next actions
1. Retrieve the FRED CSV/series metadata and Federal Reserve H.10 methodology/source metadata using free official endpoints; archive raw responses and calculate SHA-256.
2. Compare full overlapping daily history by date, preserving missing values and revision vintages; report exact match, mismatch, additions and removals.
3. Resolve why H.10 Preview unit label is Jan-1997=100 while FRED reports Jan-2006=100 despite identical displayed levels; require official explanation, not inferred rebasing.
4. Only after all gates pass, add a separate FRED retrieval alias/manifest while preserving original H.10 source identity and exact source provenance.

## Protected invariants
No production integration, no classifier promotion, no new market observation admitted, no fabricated timestamps/hashes, no synthetic data, ₹0 spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.