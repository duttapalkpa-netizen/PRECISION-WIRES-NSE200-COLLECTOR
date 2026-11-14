# NSE RSS Collector QA Hardening + Fresh Snapshot Structural Audit
Date: 2026-11-14

## Code QA change
- Updated `collector/nse_announcements_rss.py`: after validating RSS root and channel, reject a zero-item feed with `RSS_ITEM_COUNT_ZERO`. A syntactically valid but empty channel is not evidence that the official source has no announcements and must not pass acquisition parsing.
- Added unit test `test_rejects_empty_channel_as_non_evidence` in `qa/test_nse_announcements_rss.py`.
- Collector blob: `90b0dba02ddaeaa336a4c410a1349337282843ac`.
- Test blob: `2234e0eb85669824e3e0ea415a32861d2db1ca4e`.
- Workflow run: 43558025207; head SHA `244348a2a2e0a78370ed97b1e6e1ecd6e22e9dfd`; job `acquire` SUCCESS. Parser tests, bounded official acquisition and artifact upload all PASS. Runtime <1 minute by UTC timestamps 04:43:06–04:43:21Z.

## Fresh official RSS acquisition
- Requested/final URL: `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml`.
- HTTP 200; Content-Type `application/xml`; retrieval 2026-11-14T04:43:20Z–04:43:21Z.
- Raw XML 74,162 bytes; SHA-256 `b76717de6777404a56ded5cae962c922f199b32534364800a96ef059918a9990`.
- JSONL 157,661 bytes; SHA-256 `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`.
- Manifest 6,251 bytes; SHA-256 `dc4435c3043f323aa79abfeba4b571184dd44ce0b6935be69f01dc8f0ab7a052`.
- Artifact ID 14098814399; ZIP 18,730 bytes; SHA-256 `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`; expires 2026-12-14T04:43:21Z.

## Structural audit of 190 items
- XML parse PASS; 190 items, all pubDate strings preserved verbatim.
- 190/190 have no GUID.
- 35/190 have non-empty link; 155/190 have an empty link element.
- 35 distinct non-empty links; no repeated non-empty links.
- 174 unique titles; 16 repeated-title rows (including repeated issuer names across separate filings). 189 unique descriptions; one repeated description. Raw item XML unique 190/190.
- All 190 pubDate strings are on 14-Nov-2026, ranging 00:00:02 to 09:54:42 (source-native format `DD-Mon-YYYY HH:MM:SS`, no timezone suffix).
- Comparison to earlier 13-item snapshots: all 13 prior links occur in this 190-item snapshot. This is a link-level overlap observation, not proof that the earlier snapshot's other 177 items were absent then or that feed is a complete historical archive.
- The 155 empty-link rows are real source payload records; they are not dropped or assigned fabricated attachment URLs. The feed contains a broad mixture of issuer and fund/NAV notices. Do not infer a company symbol where the source fields do not provide one.

## Decision and follow-up
- Zero-item rejection regression: PASS.
- Official RSS acquisition and parser: PASS.
- Snapshot schema quality limitation: significant; GUID absent 190/190, link absent 155/190.
- RSS is useful as a raw-first discovery channel, but item identity and attachment matching are incomplete without a separate official filing-row join. Preserve empty links as null/empty and use exact official dated rows for mapping.
- Corporate Events P0 remains BLOCKED; general-announcement CSV UI acquisition and full official reconciliation still pending.

No paid services, no synthetic values, no guessed symbols/URLs, no PR/merge, no production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.
