# IMF SDMX Central RSS transaction archive probe — Brazil PA (Part 3, 2026-11-19)

## Decision
**RSS retrieval and parsing PASS; historical PA/transaction-2 recovery BLOCKED.** The official public RSS feed returned HTTP 200 and parsed cleanly, but it contains only the latest 38 transaction entries, spanning 2026-11-18T09:11:47Z through 2026-11-19T08:43:07Z. It does not include transaction #2, the Brazil PA identifier, BOP6/BOP_BPM6, or any matching historical entry. The feed is a recent-activity feed, not a historical archive for the 2023-09-22 transaction.

## Raw feed receipt
- URL: https://sdmxcentral.imf.org/rss.xml
- Retrieved: 2026-11-19T09:10:19.290692+00:00
- HTTP 200; Content-Type application/xml.
- Raw bytes: 34,559.
- Raw RSS SHA-256: `ff0c03df5d6b9557d6f6c21a341a7d589baef38893291fcfc2ff715257619e73`.
- XML parse: PASS.
- Entries: 38; matched Brazil/PA/BOP6/transaction-2 entries: 0.
- Newest item: Transaction #38674 at 2026-11-19T08:43:07Z.
- Oldest item: Transaction #38637 at 2026-11-18T09:11:47Z.
- The feed items expose transaction IDs, timestamps and modified Registration URNs; they do not provide the older transaction #2 body or its Changelog.

## Workflow and artifact
- Focused workflow run #35 / ID `44493898103`: SUCCESS.
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44493898103
- Artifact ID `14513872121`; name `imf-brazil-public-api-probe-44493898103`; size 4,410 bytes.
- Artifact SHA-256: `e88d37e4054c304618ed1af4be14337a6e0b583d791b4cf2e93115410854639a`.
- RSS probe script commit: `fab0b0051d4f1673b2d6f6c5e36eff85d94444c5`.
- Workflow integration commit: `8afdcd8030f07313d6cfcb4a249cd88872d3822a`.
- Trigger commit: `48aabd06fd3697eea2853a5706a566a68fb94501`.

## Negative evidence from the same run
The two transaction #2 alternate-format requests were repeated by the workflow and again returned HTTP 500, with the same 39-byte body and SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`. No new attempt should be made against those identical URLs.

## Operational guard correction
The new RSS research script was initially absent from the NSE production workflow's `paths-ignore`, which started unintended collector run #381 / ID `44493879791`. A helper cancellation workflow successfully cancelled that run at 2026-11-19T09:10:54Z. The production collector `paths-ignore` now explicitly includes:
- `scripts/research/probe_imf_brazil_pa_structure_revision.py`
- `scripts/research/probe_imf_brazil_rss_transaction_archive.py`
- `scripts/research/imf_brazil_public_api_probe_trigger.txt`

Guard fix commit: `110c8e6d6abbe536165c760d919c4c3926030501`.
Cancellation workflow/trigger commits: `e9ab2ecf3dc4fbc1a138c81626bcf5c0fe088e6d`, `9bab2a8c36715c1f91770a14c6eaf1a60957de88`.
Cancellation workflow run: `44493979049` SUCCESS; collector run `44493879791` final conclusion CANCELLED. No production source code was changed.

## Next decision
The public RSS route is exhausted for this old event. Do not keep polling it or retry tx2's identical API variants. The only viable next step for the 2023 PA history is actual interactive IMF SDMX Central UI access to Activity / Structure Submissions / Provision Agreement Changelog and Compare, or an authorized historical export. The public HTML pages expose these controls, but static retrieval does not expose the dynamic selected-row contents. No credentials were used and no write action was attempted. If no authorized read-only route is available, preserve PA chronology UNKNOWN/BLOCKED and pivot to remaining Global Capital Rotation coverage blockers.

## Acceptance
- RSS public retrieval: PASS.
- XML parse and 38-entry archival: PASS.
- Historical Brazil PA/transaction #2 recovery: BLOCKED.
- Brazil Reconstruction: BLOCKED.
- BOP6/BOP_BPM6 identity reconciliation: BLOCKED.
- Production selector, ranking score, pressure-fade, CORE-672, Engines A–E unchanged. UNKNOWN is not PASS. Spend ₹0.
