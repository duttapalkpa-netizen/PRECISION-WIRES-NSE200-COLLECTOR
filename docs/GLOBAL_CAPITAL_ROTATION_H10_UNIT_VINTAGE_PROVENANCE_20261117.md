# H.10 Broad Dollar Index — Unit Base and Vintage Provenance Decision
Date: 2026-11-17 (Asia/Kolkata)
Status: JAN-2006 BASE CONFIRMED FROM OFFICIAL METHOD + RAW OBSERVATIONS; XML UNIT LABEL IS STALE/CONFLICTING METADATA; HISTORICAL VINTAGE RECONSTRUCTION NOT_DONE

## Executive decision
For target series H10 / H10 / JRXWTFB_N.B (FRED crosswalk DTWEXBGS), the effective published daily indexation is January 2006 monthly average = 100, not January 1997 = 100. The raw XML and current DDP preview both expose UNIT=Index:_1997_Jan_100, but the Board's own technical Q&A explicitly states the June 24, 2019 re-indexing sets the January 2006 monthly average to 100. The preserved daily observations independently confirm this: 22 active January 2006 observations average 100.00000454545454.

Decision: retain raw UNIT metadata exactly as source-provided and flag it as a metadata-label conflict/stale descriptor. Interpret the numeric series' effective base as January 2006 monthly average = 100, supported by the Board's technical Q&A and raw-data calculation. Do not rewrite the raw metadata and do not multiply the current published values by 1.014163 again. The Board says the series after the revision is the current series multiplied by 1.014163; the already captured series is already on that re-indexed scale.

## Official evidence
1. Federal Reserve Technical Q&A, updated February 6, 2023:
   https://www.federalreserve.gov/releases/h10/h10_technical_qa.htm
   Posted May 28, 2019; Q: changes implemented June 24, 2019. It states the previous daily base was January 2, 2006 = 100, and after revision the monthly average of January 2006 is 100. It specifies Broad factor 1.014163 (AFE 1.017881, EME 1.009396).
2. Federal Reserve H.10 release page, last update November 16, 2026:
   https://www.federalreserve.gov/Releases/H10/
   It repeats that the June 24, 2019 indexation change applies to daily Broad, AFE and EME indexes.
3. Federal Reserve current DDP Preview:
   https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10
   It reports Unit=Index:_1997_Jan_100 and latest value 122.6503 on 2026-11-13. This descriptor conflicts with the method Q&A and the empirical January 2006 base check; preserve it as raw metadata, not as the operative base.
4. Federal Reserve methodological note, January 15, 2019:
   https://www.federalreserve.gov/econres/notes/feds-notes/revisions-to-the-federal-reserve-dollar-indexes-20190115.html
   Explains the February 2019 methodology revision, new weights based on goods and services, and historical series back to January 2, 2006.

## Independent raw-data calculation
Input archive from Run 44061789458, artifact 14319270830:
- H.10 ZIP SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- Target series: JRXWTFB_N.B.
- January 2006: 22 observations with OBS_STATUS=A.
- Arithmetic mean: 100.00000454545454.
- Minimum: 99.3434; maximum: 101.4155.
- This is a direct calculation over source observations; no values were changed, imputed, or rescaled.

## Revision / vintage notice register (official Board announcements)
| Notice date | Release affected | Board-stated issue / correction | Implication |
|---|---|---|---|
| 2024-08-07 | G.5, Aug 1 2024 | July 2024 data for most currencies and dollar indexes incorrect; corrected Aug 7 | Preserve dated vintages; affected scope requires row-level identification |
| 2024-10-03 | G.5, Oct 1 2024 | Historical data for AFE and Broad incorrect; corrected Oct 3 | Historical rows may be revised after initial release |
| 2025-01-07 | H.10, Jan 6 2025 | Some historical data for AFE, EME and Broad incorrect; corrected Jan 7 | Current XML alone is not a historical vintage archive |
| 2026-05-11 | G.5, May 1 2026 | Some historical data for AFE, EME and Broad incorrect; corrected May 11 | Need archived pre/post snapshots to quantify revisions |
| 2026-08-12 | H.10, Aug 10 2026 | Aug 3 values for all currencies and dollar indexes incorrect; corrected Aug 12 | At least one known daily correction must be captured in vintage tests |

Official announcement feed:
https://www.federalreserve.gov/feeds/h10.html
The Board announcement feed also records the DDP transition: Build Your Package retired in November 2026; preformatted packages planned for removal March 31, 2027 and DDP page removal July 1, 2027. Board directs users to XML on release pages or expanded FRED retrieval. This is a source-access continuity risk, not permission to assume FRED equivalence.

## Durable regression assertion
- qa/test_h10_xml_acceptance.py updated to assert 22 active January 2006 observations average 100.0 within 0.00001.
- Update commit: 23bf3de434e88841a54cffb0bda8fd67c68844d3.
- New blob SHA: 976bdd2bbb1134ece571c3e629989e76bfadc1c8.
- The test is committed; do not call the newly added assertion CI-PASS until a workflow explicitly runs it against the archived XML.

## CI outcome reviewed after prior checkpoint
- Capture Run #6 44063756752: FAILURE at acceptance, not download. H.10 XML and DDP/FRED crosswalk both HTTP 200 and passed checks; crosswalk exact match count=1; H.10 5,445 rows, A=5,231, ND=214, zero duplicates, chronology true, active finite values=0 errors, ND sentinel count=214. All five FRED segmented windows again timed out; captured_window_count=0.
- Artifact 14318684758; size 2,271,044 bytes; artifact ZIP SHA-256 5e2fdf098cee01f910f10892d9802c28613a3bda91a2d7ab5f7a7fcc428d2d3d.
- Overlay Run #241 44063756763: overlay unit-test job 133972010507 SUCCESS; embedded capture job 133972010867 FAILURE for same FRED timeouts; overall workflow FAILURE.
- This confirms the runner-to-FRED graph route is persistently unavailable under both monolithic and segmented requests. Do not repeat this exact route again absent a materially different access path.

## Still open
- FRED full-history equivalence against all 5,445 Board observations: BLOCKED / NOT_DONE.
- Pre/post correction vintage archive and row-level revision diff: NOT_DONE; latest current snapshot does not reconstruct earlier vintages.
- Exact raw UNIT metadata correction/clarification by Board: UNKNOWN; effective numerical base is resolved, but metadata label itself remains unexplained.
- Production collector/registry migration: BLOCKED / NOT_AUTHORIZED.

## Invariants
Research-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic values, no fabricated timestamps/hashes, no paid API, ₹0 spend.
