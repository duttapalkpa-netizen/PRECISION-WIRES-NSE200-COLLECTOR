# Poland POL Q2-2026 — NBP portfolio flow methodology, revision vintage and raw-PDF gate
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 12
Continuation sequence: 164
Decision: NBP METHODOLOGY AND REVISION CYCLE DOCUMENTED; EXACT TRANSACTION FX CONVERSION FOR Q2 PORTFOLIO LEGS NOT SPECIFIED IN INSPECTED OFFICIAL METHODOLOGY; RAW PDF DOWNLOAD FAILED; SAME-VINTAGE BRIDGE NOT_ESTABLISHED; POL PARTIAL / NOT PASS.

## 1. Continuity preflight
- Re-fetched Master Continuity Ledger, GCR Priority Queue and exact POL Part-11 report.
- Reused the correctly titled official NBP Q2 report and captured dual-leg values from Part 11. No duplicate extraction, no IMF re-query, no cohort rebuild.
- Scope: determine whether NBP's official methodology gives a valid transaction-level PLN/USD conversion rule and how its Q2 revision cycle affects vintage comparability; retry raw PDF only via one different container transfer route.

## 2. Official NBP methodology findings
Official NBP Department of Statistics “Balance of payments Statistics — Methodological notes”, Warsaw, September 2023:
https://nbp.pl/wp-content/uploads/2022/11/BoP-methodological-notes.pdf
- NBP states quarterly BOP is compiled/distributed three months after the reference quarter; quarterly data are presented in PLN, EUR and USD (PDF lines 180–188).
- NBP's quarterly revision policy: first version is verified in the next quarter; September compilation revises Q2, with revision depth limited to nine quarters to adapt to new annual data (lines 208–219).
- Portfolio investment BOP is defined as cross-border transactions/positions in debt/equity securities excluding direct investment and reserves. Data source is security-by-security reports from Polish holders for assets and issuers/intermediaries for liabilities; transaction market values (including accrued/paid interest) are calculated security-by-security; repo transactions are adjusted/excluded (lines 851–894).
- For securities without ISIN, reported transactions and separate valuation/exchange-rate/other changes are included in reports (lines 889–892). This is not a universal transaction conversion rule.
- Crucially, this methodology edition does NOT state the exact exchange-rate convention or conversion date/rate used to translate the Q2 portfolio transaction legs from source currency into the published PLN and USD presentations. It does not justify using the quarter-average, quarter-end rate, daily rate, or a simple ratio of published aggregate totals. No such conversion is inferred.
- NBP IIP DSBB metadata confirms portfolio assets/liabilities are reported separately and portfolio flows/positions are sourced from security-by-security reports; however this is an IIP metadata page and not proof of Q2 BOP USD conversion method: https://dsbb.imf.org/sdds/dqaf-base/country/POL/category/IIP00 .

## 3. Revision-vintage finding
- NBP official methodology explicitly identifies September as the Q2 compilation/revision cycle, with revisions reaching back nine quarters.
- Therefore a Q2 value in a September 30, 2026 release is a Q2 publication-vintage value. Existing IMF raw archive was captured 19-Nov-2026, but this alone does not prove its Q2 observation shares the same national revision cut-off. Exact IMF observation-vintage metadata/receipt mapping to NBP's 30-Sep vintage remains NOT_ESTABLISHED.
- Do not assume the November IMF archive is equivalent to NBP's September publication vintage.

## 4. Raw PDF integrity route
- Official PDF URL retained: https://static.nbp.pl/dane/bilans-platniczy/bop_kw_en.pdf
- A new container-backed direct byte download attempt failed. No file bytes, byte count, HTTP headers, response timestamp or SHA-256 captured. Do not substitute web-extracted text or Git blob SHA for raw PDF SHA-256.

## 5. Acceptance matrix
| Gate | Result |
|---|---|
| NBP Q2-2026 national asset and liability values | PASS — Part 11 |
| NBP official portfolio methodology and source concepts | PASS |
| NBP Q2 revision cycle identified | PASS |
| Exact transaction FX conversion rule for these portfolio flows | NOT_ESTABLISHED |
| NBP Q2 PDF raw bytes/SHA-256 | NOT_CAPTURED |
| NBP Sep-2026 vs IMF Nov-2026 same-vintage bridge | NOT_ESTABLISHED |
| Cross-currency comparison | NOT_DONE |
| POL national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 6. Decision and next bounded action
- Methodology work narrows the blocker: NBP's official methodology documents the source and security-by-security transaction valuation but not the exact currency conversion convention needed for a defensible USD/PLN bridge.
- Next only if a genuinely new official source is available: locate NBP's transaction currency conversion instructions in reporting-form technical specifications/metadata or obtain the matched-vintage USD Q2 portfolio asset/liability table. Separately establish IMF observation vintage. If unavailable, retain the observed PLN legs as valid national evidence and advance to next cohort country; do not repeatedly retry the same PDF download or infer FX from totals.
- ₹0; official/free sources only. No synthetic data, fabricated timestamps, net-to-leg inference, ad-hoc currency conversion, stock-as-flow, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
