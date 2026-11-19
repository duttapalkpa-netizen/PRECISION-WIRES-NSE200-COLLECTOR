# GCR — RBI Annex A2 India Quarter-Level Sudden-Stop Extraction (Continuation 43, Part-3)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: ANNEX A2 INDIA ROW EXTRACTED FROM RBI OFFICIAL HTML RENDERING; EXACT QUARTER WINDOWS AND FLOW TYPES NOW VERIFIED AT SOURCE-TABLE LEVEL.

## 1. Purpose
Resolve the specific open item in Continuation 43 Parts 1–2: India quarter-level sudden-stop windows and flow classifications in RBI Annex Table A2.

Primary source: RBI, "Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies".
URL: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Source table: Annex Table A2, "Sudden Stop Episodes in Major EMEs during Q1:1992-Q1:2022".
Official HTML rendered table rows are exposed at source lines 211–230, with India row at lines 227–230.

## 2. Exact India row transcription
RBI Annex Table A2 columns: Gross Capital Inflows (Episodes; Number of Quarters), Gross FPI Inflows (Episodes; Number of Quarters), Net Capital Flows (Episodes; Number of Quarters).

| Flow measure | Episode(s) printed for India | Number of quarters |
|---|---|---:|
| Gross capital inflows | Q4 2008 – Q2 2009 | 3 |
| Gross capital inflows | Q1 2016 – Q2 2016 | 2 |
| Gross FPI inflows | Q3 2006 | 1 |
| Gross FPI inflows | Q3 2008 – Q1 2009 | 3 |
| Gross FPI inflows | Q1 2016 | 1 |
| Gross FPI inflows | Q1 2022 | 1 |
| Net capital flows | Q3 2004 | 1 |
| Net capital flows | Q3 2006 | 1 |
| Net capital flows | Q4 2008 – Q2 2009 | 3 |
| Net capital flows | Q1 2016 – Q2 2016 | 2 |

The India table row explicitly prints the number of quarters for every listed episode. These are quarterly source classifications, not daily announcement dates or daily market event windows.

## 3. Reconciliation with Parts 1–2
- Part-1's broad 2015–16 India window is now refined: gross capital inflows Q1–Q2 2016 (2 quarters), gross FPI inflows Q1 2016 only (1 quarter), and net capital flows Q1–Q2 2016 (2 quarters).
- Part-2's earlier UNKNOWN/PENDING status for the exact India 2015–16 quarters and flow-type detail is superseded by this direct Annex A2 extraction.
- The paper's body text states the broader H2:2015 and H1:2016 country-level episode set and links it to August 2015 China market turmoil and the first US Federal Funds rate hike in December 2015. Annex A2 shows the India gross-capital/net-flow quarter sequence begins Q1 2016; do not rewrite this as Q3/Q4 2015.
- India Q1 2022 appears in the gross FPI inflow column only in the India row; this is consistent with the article body text stating India recorded a gross-FPI sudden stop in Q1 2022.
- GFC India classifications differ by measure but overlap substantially: gross capital inflows and net capital flows Q4 2008–Q2 2009; gross FPI Q3 2008–Q1 2009. Preserve this distinction.

## 4. Interpretation and guardrails
1. These episode labels derive from RBI's quarterly sudden-stop methodology and the source's IMF BOPS-based sample Q1:1992–Q1:2022.
2. The row does not provide exact daily shock timestamps, event-study announcement times, NIFTY/sector returns or causality.
3. Do not combine gross capital inflows, gross FPI inflows and net capital flows into one undifferentiated "capital flow" series.
4. Do not infer a 1–3 day market signal from a quarterly sudden-stop classification.
5. For future replication, source raw quarterly series with compatible definitions/vintage, reproduce the paper's threshold logic, and compare episode labels before any high-frequency event study.
6. The Annex table alone does not validate independent raw-data replication; it verifies the published source result.

## 5. Acceptance status
| Gate | Status |
|---|---|
| RBI official HTML source reopened | VERIFIED |
| Annex Table A2 India row located | VERIFIED |
| Gross capital inflow episode quarters | VERIFIED |
| Gross FPI episode quarters | VERIFIED |
| Net capital flow episode quarters | VERIFIED |
| Part-2 exact-quarter UNKNOWN/PENDING | SUPERSEDED |
| Independent reproduction from raw quarterly data | NOT_DONE |
| Daily market/FX/sector response | NOT_MEASURED |
| Raw high-frequency event-study panel | NOT_ACQUIRED |
| Observation overall | OPEN |
| Planning / Organizing | NOT_STARTED |
| GCR completion / production admission | NOT_AUTHORIZED |

## 6. Primary source
RBI official article and Annex Table A2:
https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Table lines: Annex Table A2 heading at 211–213; India row at 227–230 in the current official HTML rendering.

## 7. Invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed quarter boundaries or guessed flow classifications. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
