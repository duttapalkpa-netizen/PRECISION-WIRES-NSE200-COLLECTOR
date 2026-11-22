# FBIL Official USD/INR Historical Endpoint Verification — Continuation 253

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Scope: Resolve the USD/INR official-source blocker from C252 without introducing an unverified endpoint or non-official data.

## 1. Continuity and run-state check
- Re-read `research/GITHUB_MASTER_CONTINUITY_LEDGER.md` (blob SHA `7e91494b7dc9a14445a19b2c3120ce6e3865d8cb`) and C252 report (blob SHA `4744d79bf8f8132cb8904824ac53ffd3c6a837a1`).
- Latest audit-branch Actions list: Run #387 / ID `44994024678` completed `cancelled`; the same-head hard-gate run ID `44994024718` completed `failure` (C252 hard-gate analysis). No new PASS evidence supersedes C252.
- No production workflow or protected selector files changed.

## 2. Official-source facts verified
1. RBI states that FBIL took over computation and dissemination of USD/INR and other major-currency reference rates effective 2018-07-10. RBI's daily reference-rate publication stopped after 2018-07-09. Official sources:
   - https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393
   - https://rbi.org.in/Scripts/BS_DisplayReferenceRate.aspx
2. FBIL's published methodology states USD/INR is based on actual spot transactions in the 11:30–12:30 Mumbai time window, normally sourced from Refinitiv and CCIL:
   - https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf
3. FBIL official homepage is an Angular/SPA-style page that the available public text retrieval exposes with zero readable lines:
   - https://www.fbil.org.in/
4. Search indexing surfaces dated FBIL USD/INR observations, confirming that daily values are publicly displayed/indexed. It does not expose a verifiable historical download URL, API contract, response schema, pagination/date parameters, or a machine-readable full-range archive.
5. RBI historical archive explicitly directs users to FBIL for post-2018 rates. RBI publication Table 223 surfaced only partial 2026 coverage and is not evidence of complete coverage through the panel end date 2026-11-20.

## 3. Endpoint verification result
**BLOCKED — no implementation authorized.**

No exact public FBIL historical endpoint/download contract could be verified from the official homepage or official-source material inspected in this continuation. A search snippet or third-party statement about a “Historical Rates” menu is insufficient to establish an endpoint. No guessed URL, undocumented API, community mirror, paid/keyed service, or credentialed endpoint was used.

The current `pipeline/macro_geo_repair_p0.py` behavior is therefore correct to keep USD/INR BLOCKED when FRED fails and no directly verified official FBIL source is configured. Do not change this gate based on this research.

## 4. Exclusions
- Community GitHub mirrors and third-party CSV/Zenodo copies: excluded by project source policy.
- Paid/keyed API services: excluded by ₹0 spend constraint.
- RBI pre-2018 archive: wrong coverage for the current post-2018 requirement.
- RBI Table 223 partial publication: incomplete through 2026-11-20.
- FBIL homepage search snippets: display evidence only, not machine-readable archive/API proof.
- No fabricated timestamps, rows, or prices.

## 5. Acceptance decision
- FBIL official ownership/methodology: VERIFIED.
- Public daily display evidence: VERIFIED.
- Public machine-readable historical endpoint and schema: UNKNOWN / NOT VERIFIED.
- Complete panel-window coverage through 2026-11-20: NOT VERIFIED.
- USD/INR P0 group: BLOCKED.
- Overall Macro-Geo P0 gate: BLOCKED; no release eligibility inferred.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E: unchanged.

## 6. Next exact actions
1. Obtain inspectable FBIL frontend assets or an official download link from the website's own user-facing navigation; verify host ownership, date-range behavior, schema, units, and complete coverage before coding.
2. If the official public site does not expose a free full-range machine-readable archive, retain USD/INR BLOCKED and document the limitation rather than scraping guessed routes.
3. Independently assess the NSDL official FPI/DII archive already present in the Run #386 artifact for a properly sourced historical flow series; do not confuse it with the one-date NSE snapshot or promote it without date/schema/coverage checks.
4. Continue historical event-publication backfill only with source URLs and genuine publication timestamps; keep occurrence times distinct and event windows pending until market closes mature.
5. Re-run only targeted tests after a proven code change; do not repeat completed QA or weaken the strict hard gate.

## Sources
- RBI press release (2018-07-04): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393
- RBI Reference Rate page: https://rbi.org.in/Scripts/BS_DisplayReferenceRate.aspx
- FBIL official homepage: https://www.fbil.org.in/
- FBIL methodology PDF: https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf
- RBI archive guidance: https://www.rbi.org.in/scripts/FS_RTI_Diclosure_Logs.aspx?fn=6

## Operating guardrails
Audit branch only; ₹0 spend; official/free sources only; no synthetic data, fabricated timestamps, community mirrors, undocumented endpoint assumptions, or access-control bypass. UNKNOWN/BLOCKED never PASS. Skip PASS work unless regression evidence appears.
