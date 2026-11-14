# NSDL FPI Sector-wise Cross-source Update — 2026-11-14

## Official latest report identified
- Official NSDL fortnightly sector-wise FPI report for 31-Oct-2026 is available at https://pilot.fpi.nsdl.co.in/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_Oct312026.html (web evidence turn177159search2).
- It reports the 01–15 Oct and 16–31 Oct fortnight windows, AUC as at 15-Oct and 31-Oct, with separate Equity, Debt, Hybrid, Mutual Funds and AIF categories.
- Grand Total net Equity investment for 16–31 Oct 2026: +₹13,112 crore. Equity AUC at 31-Oct: ₹65,25,808 crore. The same official report shows 01–15 Oct equity net investment −₹47,955 crore and 15-Oct equity AUC ₹65,94,378 crore.
- Sequential equity flow arithmetic across the two reported fortnights: −₹47,955 + ₹13,112 = −₹34,843 crore net across 01–31 Oct. This is a derived two-window sum, not a daily flow or a separate source observation.
- The NSDL report identifies itself as FPI sector-wise data and the report's full category structure should be retained; do not add debt/hybrid/MF/AIF flows into equity.
- Official report page's visible Automobile and Auto Components row: equity AUC ₹4,77,593 crore at 15-Oct; equity net investment −₹6,533 crore for 01–15 Oct; equity net investment −₹1,098 crore for 16–31 Oct; equity AUC ₹4,74,488 crore at 31-Oct. This is a single row check, not full sector-table reconciliation.
- NSDL 31-Oct data is later than CDSL's 15-Oct sector report. It extends the sector timeline but does not establish a CDSL-vs-NSDL same-date discrepancy. The two official depository reports' date, coverage and methodology must be explicitly aligned before any reconciliation.

## Research interpretation
- The sequence shows large first-half October equity outflow (−₹47,955cr) followed by a second-half inflow (+₹13,112cr); full-month net remains −₹34,843cr. This is a flow-horizon observation, not a price forecast.
- Auto & Auto Components second-half outflow slowed from −₹6,533cr to −₹1,098cr in the NSDL report. Do not call this a reversal to inflow.
- Do not infer sector stock returns, issuer-level exposures, causality or H+1/H+3/H+5 probabilities from flow alone.

## Status
- Official NSDL 31-Oct report discovery and key total/one-row extraction: DOCUMENTED; arithmetic PASS.
- Complete 24-sector extraction, all-category arithmetic, CDSL/NSDL method reconciliation, raw file bytes/hash, multi-period time series, NSE sector-index return joins and rolling predictive validation: NOT RUN / NOT ACQUIRED.
- No synthetic data, no production selector/ranking/CORE-672 changes, no PR/merge. Hard Gate remains BLOCKED.
