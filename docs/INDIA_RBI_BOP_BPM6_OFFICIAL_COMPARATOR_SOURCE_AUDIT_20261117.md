# Chapter 34 — India RBI BPM6 BOP Official Comparator Source Audit
Date: 2026-11-17 (Asia/Kolkata)
Scope: qualify an official India-side comparator for the IMF BOP_BPM6 pilot; source semantics and release route only. No raw workbook bytes or observations admitted in this checkpoint.

## 1. Decision
The Reserve Bank of India (RBI) publishes an official quarterly BPM6-standard India Balance of Payments table suitable as an independent semantic/comparison source for the India BOP pilot:
- RBI Monthly Bulletin Comprehensive Guide, Table 42: Standard Presentation of BoP in India as per BPM6 (US$ million).
- Table 43: same BPM6-standard presentation in ₹ crore.
- Both are quarterly, compiled by RBI Department of Economic and Policy Research (DEPR), primary data source RBI, and subject to revision.
- Table 42 includes Financial Account functional categories, including Portfolio Investment, and presents Credit, Debit and Net separately; preliminary observations are marked P.
- Table 43 is the INR counterpart; reserve-asset sign convention is BPM6-specific.
- This is an independent official comparator, NOT an IMF API endpoint and NOT an exact series-level crosswalk to IMF BFPA/BFPL without inspecting underlying table rows and definitions.

## 2. Official RBI metadata verified
RBI Comprehensive Guide for Current Statistics of the RBI Monthly Bulletin:
- Official page: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24094
- Publication page date: 08-Oct-2026; handbook edition April 2026.
- Table 42: quarterly; unit US$ million; source department DEPR; primary source RBI; revision policy: subject to revision.
- Coverage includes Current Account, Capital Account, Financial Account (Direct Investment, Portfolio Investment, Financial Derivatives, Other Investment, Reserve Assets), Total Assets/Liabilities and Net Errors and Omissions.
- Presentation: Credit, Debit and Net; BPM6 functional classification; residence principle and double-entry accounting.
- Table 43: same BPM6 classification in ₹ crore.
- DBIE mapping: Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector; Statistics > External Sector > International Trade.
- MoSPI Compendium of Datasets and Registries in India lists RBI BoP as quarterly, All India, dissemination formats PDF/MS Excel, and points to DBIE. This is a secondary official catalog reference, not raw data.

## 3. Current official release calendar and exact downloadable route
RBI SDDS page: https://www.rbi.org.in/scripts/SDDS_ViewDetails.aspx?ID=5&SDDSID=284
- Calendar posted 01-Apr-2026.
- April–June 2026 BOP release date: 01-Sep-2026.
- July–September 2026 BOP release date: 01-Dec-2026.
- Therefore as of 17-Nov-2026, July–September 2026 quarter is not yet scheduled for publication; do not expect or fabricate that observation.
- The April–June 2026 publication link resolves to this official RBI XLSX route: https://rbidocs.rbi.org.in/rdocs/content/docs/BOPS01092026FULL.xlsx
- Browser retrieval returned an anti-bot challenge page for the XLSX route. No workbook bytes, response headers, byte length, retrieval timestamp or SHA-256 were captured here. Raw workbook acquisition remains NOT_VERIFIED.

## 4. Latest monthly release is not a substitute for quarterly BPM6 table
RBI press release dated 13-Nov-2026, Developments in India’s Balance of Payments for the Month of September 2026: https://www.rbi.org.in/scripts/bs_pressreleasedisplay.aspx/BS_PressReleaseDisplay.aspx?prid=63974
- Shows monthly September 2026 and April–September 2026 cumulative BOP summary in US$ billion.
- September 2026 Foreign Portfolio Investment (Net) is -US$6.7bn; In India (Net) -US$6.5bn; Abroad (Net) +US$0.1bn.
- April–September 2026 FPI (Net) is -US$10.4bn; In India (Net) -US$8.9bn; Abroad (Net) +US$1.4bn.
- These are monthly/cumulative press-release summary values, not quarterly Table 42 observations and not exact BFPA/BFPL series equivalents. Do not mix units or periods.

## 5. Mapping guardrails
- RBI Table 42 is a suitable independent BPM6 classification comparator for India.
- Do not equate RBI Credit/Debit/Net columns mechanically with IMF BFPA_BP6_USD / BFPL_BP6_USD until row-level direction, sign convention, resident/nonresident interpretation and exact portfolio investment subcomponents are confirmed.
- Do not substitute monthly press-release FPI summary for quarterly BPM6 Table 42.
- Do not treat the RBI XLSX URL as raw payload evidence until exact bytes and HTTP metadata are captured.
- RBI quarterly BOP is macro context and a cross-source reconciliation input, not a 1–3 day trading trigger.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| Official RBI BPM6 Table 42 and Table 43 identification | PASS — documented |
| Publisher, department, primary source, unit and frequency | PASS — documented |
| Revision policy and preliminary marker semantics | PASS — documented |
| Official SDDS release calendar | PASS — documented |
| Exact April–June 2026 XLSX URL resolution | PASS — official link resolved |
| XLSX raw bytes / HTTP status / content type / byte length / SHA-256 | NOT_VERIFIED — anti-bot challenge |
| Row-level Portfolio Investment Credit/Debit/Net extraction | NOT_DONE |
| Exact RBI ↔ IMF BFPA/BFPL semantic reconciliation | NOT_DONE |
| Source registry parser allowlist / trusted admission | NOT_DONE |
| Production/classifier use | NOT_AUTHORIZED |

## 7. Next bounded action
Use a short research-only GitHub Actions collector run to retrieve the official RBI XLSX without bypassing access controls; if RBI server presents an anti-bot challenge or denies automated access, stop and preserve the exact response as a blocked attempt. If bytes are returned, archive untouched XLSX, final URL, status, Content-Type, retrieval UTC, byte length, SHA-256, workbook sheet names and relevant table rows. Then perform row-level semantic reconciliation against already-captured IMF metadata. No guessed endpoints, no credentials, no scraping challenge bypass.

## 8. Invariants
₹0; official/free sources only; no synthetic observations or timestamps; no forward-fill; UNKNOWN remains UNKNOWN. Do not change Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission or production workflows. No PR merge or production integration.

## 9. Official references
1. RBI Comprehensive Guide, Table 42/43 and methodology: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24094
2. RBI SDDS BOP release calendar and XLSX link: https://www.rbi.org.in/scripts/SDDS_ViewDetails.aspx?ID=5&SDDSID=284
3. RBI September 2026 BOP monthly press release (13-Nov-2026): https://www.rbi.org.in/scripts/bs_pressreleasedisplay.aspx/BS_PressReleaseDisplay.aspx?prid=63974
4. MoSPI Compendium of Datasets and Registries in India 2024, Balance of Payments Statistics entry: https://mospi.gov.in/sites/default/files/publication_reports/Compendium_of_Datasets_and_Registries_in_India_2024_1.pdf
