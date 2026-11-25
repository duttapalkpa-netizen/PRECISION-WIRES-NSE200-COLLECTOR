# GCR — Bangladesh (BGD) Q2-2026 official Bangladesh Bank source-period and net-only boundary

Date: 2026-11-25 (Asia/Kolkata)
Continuation: 239

Decision: **A distinct official Bangladesh Bank Quarterly publication covering April–June 2026 was inspected. Its Table V.1 reports portfolio investment only as a net item, not separate asset and liability transaction legs. This confirms a current-period official source but does not satisfy national dual-leg capture. BGD remains SOURCE_FOUND / PARTIAL / NOT PASS; both national legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate-prevention preflight
- Re-fetched the current GitHub Master Continuity Ledger (blob `cacc98d3ea0ff98d9a1cd86b3b5be204e79cbbd4`), GCR Priority Queue (blob `f3606590fb4916436e6bb2d8d1001aae55a5d15d`), 63-country matrix (blob `afebb8e75f2b371d29020f7b33918680588d6bfb`) and Historical Task Registry (blob `8bcfbd494f6eb9e838f9961b63e1421bc7743d5a`).
- Searched the Library Mother File and GCR context. The Mother File preserves the 63-country cohort, separate-leg and vintage gates. No BGD-specific continuation report was located in the current task registry search; the matrix currently records BGD as SOURCE_FOUND with national Q2 legs not verified.
- Reused the fixed cohort and existing IMF panel; no IMF re-query or cohort rebuild.
- Selected a bounded new official publication artifact, not an attempt to repeat a prior Bangladesh Bank route.

## 2. New official source
- Bangladesh Bank Quarterly, Volume XXIII, No. 4, titled “April-June, 2026”.
- Official PDF: https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol%20xxiii%2C%20no%204.pdf
- The document cover identifies the reporting period as April–June 2026 (calendar Q2 2026).
- Annexure 1, Table V.1 “Balance of Payments”, PDF text-reader page 74, reports values in million USD.
- Table columns are FY25, FY26, FY25 Q2–Q4, FY26 Q1–Q4. Bangladesh FY26 Q4 is April–June 2026 and therefore corresponds to calendar Q2-2026.
- Table V.1 contains a single row “Portfolio investment” (net) and does not separately display portfolio investment assets and liabilities.
- The same table separately displays asset/liability detail for certain other-investment and reserve-asset subcategories. Those rows are not portfolio investment and cannot be substituted for the missing portfolio legs.
- The publication marks FY26 values provisional (P) and FY25 revised (R). The document itself does not provide an observation-specific revision timestamp or IMF-matched vintage identifier.

## 3. Scope and acceptance boundary
| Gate | Status |
|---|---|
| Fixed 63-country BGD Q2-2026 cohort membership | PASS (reused) |
| New official Bangladesh Bank publication artifact | PASS |
| Calendar Q2-2026 period mapping (Apr–Jun 2026 = FY26 Q4) | PASS |
| Reporting unit (USD million) | PASS |
| Portfolio investment reported as a net line | PASS |
| Separate portfolio asset transaction leg | NOT_CAPTURED |
| Separate portfolio liability transaction leg | NOT_CAPTURED |
| Other-investment / reserve-asset subrows as portfolio substitutes | REJECTED |
| Observation-specific revision timestamp / IMF vintage bridge | UNKNOWN |
| Full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Decision
- This report improves the BGD evidence boundary by identifying a dated, official Q2 calendar-period publication and its fiscal-quarter mapping.
- The net-only portfolio row cannot be used to back-solve assets and liabilities.
- Do not infer the missing portfolio legs from total financial-account balance, net portfolio investment, other-investment rows, or IIP stocks.
- Preserve BGD at SOURCE_FOUND / PARTIAL / NOT PASS. No gate promotion.

## 5. Next exact action / duplicate prevention
- Reopen only if Bangladesh Bank publishes a distinct Q2-2026 table or downloadable dataset exposing portfolio investment assets and liabilities separately, with units, methodology and revision metadata.
- Do not repeat this same Quarterly PDF text extraction or substitute FY26 net-only figures for dual legs.
- If no distinct official dual-leg source is available, advance to the next eligible fixed-cohort member after a fresh route-history preflight.

## 6. Protected invariants
₹0; free official sources only; no synthetic values, fabricated timestamps, net-to-leg back-solving, IIP stock substitution, unsupported sign/scale/FX conversion, paid source or external contact. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No production integration or merge.
