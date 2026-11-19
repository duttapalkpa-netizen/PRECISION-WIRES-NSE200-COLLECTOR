# GCR — RBI Sudden-Stop Replication Method & India Source Mapping (Continuation 43, Part-4)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: RBI REPLICATION ALGORITHM TRANSCRIBED FROM OFFICIAL SOURCE; INDIA RBI TABLE 42 IDENTIFIED AS A NATIONAL CROSS-CHECK, NOT A SUBSTITUTE FOR IMF BOPS REPLICATION.

## 1. Purpose
Translate the exact published sudden-stop methodology into an auditable reproduction specification, and map a free official Indian national source for a secondary comparison. This does not claim that the sudden-stop episodes have been independently reproduced.

Primary research: RBI Occasional Paper, "Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies", https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Relevant official text: lines 70–79 (definition and sample), methodology images linked at lines 75–76.

## 2. Exact method transcribed from RBI
The RBI source states:
1. For gross capital inflows, construct a four-quarter moving sum:
   C_t = GrossInflow_t + GrossInflow_(t-1) + GrossInflow_(t-2) + GrossInflow_(t-3).
2. Compute the year-on-year change in that four-quarter sum:
   ΔC_t = C_t − C_(t−4), for t = 5, 6, …, N.
3. Compute rolling mean and standard deviation of ΔC_t over the previous five years.
4. Apply the symmetric sudden-stop rule: an episode starts when the annual change first falls below the rolling mean minus one standard deviation; it must contain at least one observation at or below the rolling mean minus two standard deviations; it ends when the annual change rises above the rolling mean minus one standard deviation.
5. The paper uses quarterly IMF Balance of Payments Statistics data over Q1:1992–Q1:2022 for 19 EMEs. It also applies a similar methodology to net capital flows and gross FPI inflows.

Important: the formula image describes the four-quarter moving sum and year-on-year difference; the companion image states the previous-five-year rolling mean/standard deviation and symmetric Calvo threshold rule. Preserve strict source wording and verify endpoint inclusivity against the image/text before coding.

## 3. India episode labels to reproduce
Published RBI Annex A2 India row:
- Gross capital inflows: Q4 2008–Q2 2009 (3 quarters); Q1 2016–Q2 2016 (2).
- Gross FPI inflows: Q3 2006 (1); Q3 2008–Q1 2009 (3); Q1 2016 (1); Q1 2022 (1).
- Net capital flows: Q3 2004 (1); Q3 2006 (1); Q4 2008–Q2 2009 (3); Q1 2016–Q2 2016 (2).

These are published reference labels, not independently reproduced outcomes.

## 4. Official India cross-check source mapping
RBI Table 42, "Standard Presentation of BoP in India as per BPM6 (US$ million)":
- Official metadata URL: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=24094
- Frequency: quarterly.
- Unit: US$ million.
- Credit, Debit and Net components separately presented.
- Financial account includes direct investment, portfolio investment, financial derivatives, other investment and reserve assets.
- Classification: BPM6; residence principle; preliminary observations are marked P where applicable; revision policy says data are subject to revision.
- Dissemination route: RBI DBIE > Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector; or DBIE > Statistics > External Sector > International Trade.
- RBI Table 42 is a national cross-check candidate. It is not proven identical to the IMF BOPS vintage/definitions used in the RBI research paper, and cannot by itself certify reproduction of the IMF-sourced sample.

IMF BOP dataset landing page:
https://data.imf.org/en/datasets/IMF.STA%3ABOP
It identifies annual and quarterly BOP dataset and API/download entry points. The API link currently redirects to a sign-in page in this inspection; no unauthenticated API request schema or raw dataset bytes were verified here.

## 5. Required data contract before code
For the original IMF replication, acquire and archive:
- India quarterly IMF BOPS observations, Q1:1992–Q1:2022 (and all 19 EME country series if reproducing the full paper panel).
- Separate gross capital inflows, gross FPI inflows, and net capital flows, with exact IMF item codes, sign conventions, units, currency, BPM basis, frequency, seasonal adjustment status, country identifiers and vintage.
- Metadata / dataflow / codelist / series keys and download URL, exact retrieval timestamp, response headers/content type, byte count, raw file SHA-256, parser version and manifest.
- Missing-quarter and revision audit. Do not interpolate, forward-fill, net gross series, or map series by approximate names.
- A reproducibility notebook/script must print the rolling window, treatment of initial 20 quarters, sample standard-deviation convention, threshold inequalities, missing-value policy and episode-merge rule.
- Compare each output episode against Annex A2. A mismatch is a failure requiring diagnosis, not an opportunity to tune thresholds until the published answer matches.

For the RBI Table 42 national cross-check, preserve Credit/Debit/Net and BPM6 signs as published. Explicitly document any mapping from Table 42 components to the paper's IMF BOPS gross-inflow, gross-FPI and net-flow definitions before comparing.

## 6. Acceptance gates
| Gate | Status |
|---|---|
| RBI method formula transcribed from official text/image | VERIFIED |
| Four-quarter sum and YoY difference | VERIFIED |
| Previous-five-year rolling mean/SD and symmetric threshold | VERIFIED |
| India Annex A2 published target episodes | VERIFIED |
| RBI Table 42 official metadata and dissemination route | VERIFIED |
| IMF BOP dataset landing page and quarterly frequency | VERIFIED |
| IMF raw India quarterly series acquired | NOT_ACQUIRED |
| IMF item codes / dataflow / codelists verified | NOT_DONE |
| RBI Table 42 historical raw export acquired | NOT_ACQUIRED |
| Independent reproduction of Annex A2 | NOT_DONE |
| Daily NIFTY/FX/VIX event response | NOT_MEASURED |
| Observation overall | OPEN |
| Planning / Organizing | NOT_STARTED |
| GCR completion / production admission | NOT_AUTHORIZED |

## 7. Sources
- RBI research paper: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
- RBI Table 42 metadata: https://www.rbi.org.in/scriptS/PublicationsView.aspx?id=24094
- RBI Bulletin Table 42 example: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP

## 8. Invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed IMF codes, guessed sign conversions or invented missing quarters. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
