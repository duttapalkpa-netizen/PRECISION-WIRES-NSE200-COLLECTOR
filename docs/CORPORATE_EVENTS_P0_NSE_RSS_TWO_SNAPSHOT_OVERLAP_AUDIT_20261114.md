# NSE Announcements RSS — Two-Snapshot Replay and Overlap Audit
Date: 2026-11-14
Source: https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml
Runs: #1 `43489286657`; #2 `43490004265`
Both workflow runs completed SUCCESS on the isolated research branch.

## Snapshot timing
| Field | Snapshot 1 | Snapshot 2 |
|---|---|---|
| Retrieved UTC | 2026-11-13T19:08:23Z–19:08:24Z | 2026-11-13T19:12:42Z |
| HTTP status | 200 | 200 |
| Response bytes | 6,270 | 6,270 |
| Raw XML SHA-256 | `21de2c9b2d1f39cad81600cdca22556e813d2854eeee28d5082c913ec95aa1a4` | `ee92888d16048899cffe4da9f57a6c246a7d4db2e133822e223e0674722bdaf0` |
| RSS lastBuildDate | Sat, 14 Nov 2026 00:38:09 +0530 | Sat, 14 Nov 2026 00:41:41 +0530 |
| Parsed items | 13 | 13 |

Snapshots are 4m18s apart; RSS lastBuildDate advanced by 3m32s.

## Exact comparison
- Parsed JSONL byte-for-byte identical: 11,622 bytes; SHA-256 `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`.
- Item-level comparison: 13/13 exact same records (title, link, original pubDate, description and raw item XML); 13 unique links; 0 added, 0 removed, 0 changed items between snapshots.
- Raw XML differs, but normalization of the single volatile `lastBuildDate` element makes the entire XML byte stream identical. No other XML difference observed.
- Snapshot 2 artifact ZIP SHA-256: `302a080ad812d577e64694d0230bc7b09b7d2f46d27b088aa1b17225c38dce96`.
- Snapshot 2 raw XML SHA-256 independently recomputed from downloaded artifact: `ee92888d16048899cffe4da9f57a6c246a7d4db2e133822e223e0674722bdaf0`.
- Snapshot 2 JSONL SHA-256 independently recomputed: `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`.
- Snapshot 2 manifest SHA-256: `036fdd72c40c9dab7ba57a4a2220c65c089b9d6f83f8f8427ed14aa6e0732931`.

## GUID and timestamp caveats (unchanged)
- Both snapshots have no GUID on any of the 13 items. No GUID synthesized.
- Original pubDate strings are timezone-naive; exact strings retained. No timezone assumed.
- This 4m18s window produced no new items; it does not establish feed completeness, event throughput, historical retention, or absence of missing announcements. RSS may be a rolling limited window.

## Artifact 2
- Run ID: `43490004265`; job success.
- Artifact ID: `14068698333`.
- Name: `nse-corporate-announcements-rss-43490004265`.
- ZIP size: 4,275 bytes; ZIP SHA-256 above.
- Members: `announcements.xml`, `announcements.jsonl`, `manifest.json`.
- Expires: 2026-12-13T19:12:42Z.

## Acceptance
| Criterion | Status |
|---|---|
| Second bounded workflow execution | PASS |
| 4 parser tests in second run | PASS |
| HTTP 200 and raw artifact | PASS |
| Raw XML hash independently recomputed | PASS |
| Parsed item replay equality | PASS (13/13) |
| Volatile lastBuildDate isolated | PASS |
| GUID presence | 0/13 — unresolved source limitation |
| PubDate timezone | UNKNOWN |
| Longer-horizon item coverage / official page reconciliation | NOT RUN |
| Historical completeness and retention | UNKNOWN |
| Corporate Events P0 | BLOCKED |

No code/production change, no PR/merge, no synthetic event or timestamp, no paid source. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Hard Gate unchanged.
