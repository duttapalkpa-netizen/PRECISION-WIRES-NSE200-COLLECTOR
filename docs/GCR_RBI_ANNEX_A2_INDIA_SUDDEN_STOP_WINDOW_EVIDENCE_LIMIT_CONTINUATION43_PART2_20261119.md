# GCR — RBI Annex A2 India Sudden-Stop Window: Evidence-Limit Audit (Continuation 43, Part-2)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: BODY-TEXT COUNTRY WINDOW VERIFIED; ANNEX IMAGE VALUES NOT INDEPENDENTLY EXTRACTED; DO NOT INVENT QUARTER-LEVEL DATES.

## 1. Purpose
Reopen the exact RBI primary source used in Continuation 43 Part-1 and test whether Annex Table A2 supplies a more precise India window than the article body. Record only what the rendered source actually exposes.

Primary source: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Source title: "Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies"
Authors: Sujata Kundu, Anshu Kumari and Deepika Rawat.
Coverage: Q1:1992–Q1:2022.

## 2. Directly verified source text
The RBI article body states:
- Section III, India trends: a sudden stop in capital inflows occurred during the GFC.
- Section IV, sudden-stop identification: country-level sudden stops were recorded for India and other listed EMEs during H2:2015 and H1:2016, associated in the paper with August 2015 Chinese stock-market turmoil and the first US Federal Funds rate hike in December 2015.
- Section IV, gross-FPI extension: India and China recorded sudden stops during Q1:2022 with respect to gross FPI inflows.
- The paper states that neither the 2013 taper tantrum nor the 2021 taper-talk episodes were identified as sudden stops.
- The methodology defines sudden-stop phases from quarterly flow series and standard-deviation thresholds; therefore these labels are not daily market event timestamps.

## 3. Annex A2 inspection outcome
The article exposes an Annex Table A2 link in its rendered text, but the linked table did not resolve into independently readable table rows in this inspection. Therefore:
- Exact India quarter(s) within the H2:2015–H1:2016 span are NOT independently verified here.
- Whether the specific country-level India label in this table is gross capital inflow, net flow, or both cannot be assigned from the body-text excerpt alone.
- Do not infer exact start/end quarters, flow type, or episode duration from the broad H2/H1 wording.
- Keep Q1:2022 gross-FPI classification distinct; this is explicitly stated in the body text.

## 4. Correction / precision rule for Part-1
Part-1's register remains valid at the level of the broad RBI-stated window and event classification. The table's flow-type detail for the 2015–16 India country episode remains unresolved. The phrase "country-level sudden stop" must not be silently rewritten as "gross-FPI sudden stop" or "net-flow sudden stop" without Annex A2 evidence.

## 5. Event register fields for future quantitative work
For every event, keep these fields separately:
- source_event_label
- source_event_window_as_published
- source_flow_measure (gross capital inflow / net capital flow / gross FPI inflow / weekly net FPI)
- source_country_scope (India-specific / EME panel / EME excluding China)
- exact_start_quarter and exact_end_quarter (NULL until verified)
- event_announcement_timestamp (NULL unless independently sourced)
- India_market_response (NOT_MEASURED until raw data and aligned event times exist)
- source_vintage and retrieval metadata

## 6. Acceptance and current status
| Gate | Status |
|---|---|
| RBI body text independently reopened | VERIFIED |
| India H2:2015–H1:2016 broad window | VERIFIED |
| India Q1:2022 gross-FPI sudden stop | VERIFIED |
| Exact India 2015–16 quarters from Annex A2 | UNKNOWN / PENDING |
| 2015–16 India flow-type detail from Annex A2 | UNKNOWN / PENDING |
| Daily market/FX/sector response | NOT_MEASURED |
| Raw event-study panel | NOT_ACQUIRED |
| Observation overall | OPEN |
| Planning / Organizing | NOT_STARTED |
| GCR completion / production admission | NOT_AUTHORIZED |

## 7. Primary-source anchors
RBI article, lines corresponding to Section III and Section IV: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
In the current official HTML rendering, the body text is readable but Annex Table A2 is linked as a non-text table object and did not yield inspectable rows in this pass.

## 8. Invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed quarter boundaries or guessed flow classifications. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
