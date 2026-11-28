# GCR Continuation 300 — Thailand (THA) Q2-2026 BOT annual-revision and IMF vintage boundary audit
Date: 2026-11-28 (Asia/Kolkata)
Task ID: GCR-C300-THA-BOT-ANNUAL-REVISION-VINTAGE-01
Scope: Research-only reinspection of new official revision-policy evidence and the already-captured BOT Q2-2026 portfolio dual-leg publication; no repeated raw capture, IMF query or numeric comparison.

## 1. Mandatory continuity / duplicate-prevention preflight
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and immutable 63-country Q2-2026 matrix.
- Re-read Library Mother File Continuation 1–53 and searched Library for country-specific prior evidence.
- Reopened the controlling THA report: `docs/GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md`.
- Reused the existing BOT raw HTML artifact, exact IMF raw rows, script, workflow, artifact and 2/2 numeric comparisons. No repeat BOT byte acquisition, no IMF re-query, no cohort rebuild and no arithmetic rerun.
- Selected the newly identified official NESDC Q3-2026 report's September 2026 BOT annual-revision description as a new methodology/vintage evidence item.

## 2. New official revision-policy evidence
- Official source: NESDC, *Thai Economic Performance in Q3 of 2026 and Outlook for 2026–2027*, press release 16-Nov-2026, revision section pp.34–35.
- URL: https://www.nesdc.go.th/wp-content/uploads/2026/11/Economic-report-Q3-69.pdf
- NESDC states that BOT conducted its annual BOP revision in September 2026 following preliminary figures published in July 2026.
- The report describes a change-of-ownership / FOB trade-statistics adjustment and reports that the first-half 2026 current-account deficit changed from USD16.3bn in the July release to USD4.3bn after revision. This establishes that the September annual revision was material for at least the current-account/trade-related series.
- NESDC also notes that international trade data in the September 2026 release were revised to conform to BPM7. This statement is specifically about international trade data; it is not evidence that the Q2 portfolio-investment transaction legs were reclassified or revised under BPM7.
- The cited revision discussion does not identify a Q2-2026 portfolio-investment asset revision, liability revision, portfolio-specific revision ID, or an observation-level update timestamp.

## 3. Existing official BOT Q2 portfolio pair — carried forward, not recalculated
- BOT EC_XT_049_S2, “Balance of Payments (US$)”: https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?language=ENG&reportID=1022
- Official page states Q2/2026 p (preliminary), last updated 30-Sep-2026 14:33, unit USD million.
- Existing retained values from the 20-Nov capture:
  - Portfolio assets: +USD4,679.07m
  - Portfolio liabilities: -USD238.36m
  - Portfolio net: +USD4,917.43m
- BOT's displayed financial-account convention: positive means an increase in net financial assets or liabilities; negative means a decrease; net financial-account balance is assets minus liabilities.
- Existing arithmetic identity and dual-leg comparison are preserved exactly as recorded in the controlling report. No new numeric calculation or tolerance change was made.
- Existing raw BOT HTML: 551,847 bytes; SHA-256 `b4a42305fe18668c91e1feadd70ada0537f6e2f8c5b13ef59dd1fdcbd4d00f80`; retrieved 20-Nov-2026 06:41:16.952209 UTC. Existing artifact and provenance remain the evidence source; the current web rendering was used only to confirm the public table metadata and displayed values.

## 4. IMF receipt chronology and vintage boundary
- Existing archived IMF panel receipt: 19-Nov-2026 06:43–06:45 UTC, dataflow IMF.STA:BOP(21.0.0), P_F, Q2-2026, country THA.
- BOT table's displayed last-updated timestamp (30-Sep-2026) precedes the IMF research-panel receipt (19-Nov-2026). This is transport/retrieval chronology only; the IMF receipt timestamp is not the statistical observation's source-vintage timestamp.
- IMF captured rows do not expose observation-specific first-publication date, last-update timestamp, revision ID or a matched BOT release identifier.
- BOT page still labels Q2/2026 as preliminary. The NESDC statement confirms a September annual revision of BOP accounts generally, but does not prove that the portfolio A/L pair changed in that revision or identify the exact vintage of each leg.
- Therefore the new source does not close the BOT↔IMF same-vintage bridge.

## 5. Gate decision
| Test | Result | Boundary |
|---|---|---|
| New official NESDC revision-policy evidence | PASS | September annual BOP revision after July preliminary release |
| September revision materially affected current-account/trade-related data | PASS | Not a portfolio A/L-specific revision |
| BPM7 transition statement | PASS, narrow scope | International trade data only; no blanket portfolio reclassification inference |
| Existing BOT Q2 portfolio asset/liability capture | PASS (carried forward) | No new raw capture |
| Existing separate asset/liability numeric comparisons | PASS (carried forward) | No arithmetic rerun |
| Q2 portfolio-specific revision pair / revision ID | NOT_CAPTURED | NESDC revision discussion does not provide it |
| IMF observation-specific source vintage | NOT_CAPTURED | Archived row has no matching timestamp/revision key |
| BOT↔IMF same-vintage | NOT_ESTABLISHED | Retrieval chronology is insufficient |
| THA national validation | PARTIAL / NOT PASS | VINTAGE_PENDING; FULL_PASS=NO |
| 63-country aggregate | NOT_AUTHORIZED | No aggregate promotion |

## 6. Exact next action
- Do not repeat the BOT page capture or existing IMF extraction.
- Reopen THA only if BOT publishes an observation-specific Q2 portfolio A/L revision history, a new Q2 portfolio pair with release/revision identifiers, or IMF provides matching observation-vintage metadata.
- Until then preserve the existing asset PASS and liability PASS, keep vintage PENDING, and proceed to the next eligible fixed-cohort member.
- Do not infer portfolio revisions from current-account changes, BPM7 trade-statistics notes, page update date or matching numeric values.

## 7. Protected invariants
₹0; official/free sources only. No paid APIs, external contact, fabricated timestamps, inferred revision IDs, synthetic values, net-to-leg back-solving, netting, interpolation, forward-fill or proxy substitution. Fixed 63-country cohort unchanged. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge, production integration or aggregate release.
