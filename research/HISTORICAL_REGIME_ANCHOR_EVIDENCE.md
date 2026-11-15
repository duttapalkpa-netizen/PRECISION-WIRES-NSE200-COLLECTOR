# Historical regime anchor evidence — R01 and R02

This sidecar records primary-source provenance for the two regimes that have no event windows in the current market panel. It does not fabricate market closes or imply that historical price backfill is complete.

| Regime | Verified anchor | Primary source | What it proves | Remaining gap |
|---|---|---|---|---|
| R01 GFC 2008 | 2008-09-15 | [FRASER archive of SEC Form 8-K](https://fraser.stlouisfed.org/archival-collection/securities-exchange-commission-5147/lehman-brothers-holdings-inc-519324/fulltext) | Lehman Brothers Holdings Inc. filed a voluntary Chapter 11 petition on 15 Sep 2008. | Current panel starts 2015-08-04; no H+1/H+5/H+20 price windows. |
| R02 Taper Tantrum 2013 | 2013-05-22 | [Federal Reserve testimony](https://www.federalreserve.gov/newsevents/testimony/bernanke20130522a.htm) | Bernanke's testimony/Q&A discussed possible future adjustment to asset purchases. The Fed's [balance-sheet policy timeline](https://www.federalreserve.gov/monetarypolicy/timeline-balance-sheet-policies.htm) identifies May 22 and June 19 remarks as the taper-tantrum trigger context. | Current panel starts 2015-08-04; no H+1/H+5/H+20 price windows. |

NSE Indices states that NIFTY 50 history is available from 3 July 1990 and directs users to its historical data portal. This confirms an official index-history route exists, but does not prove the missing observations have been downloaded, normalized, and reconciled. See [NSE Indices FAQ](https://www.nseindia.com/static/products-services/indices-faqs) and [historical data portal](https://www.niftyindices.com/reports/historical-data).

- Anchor event provenance for R01 and R02 is independently sourced.
- Market-price history for those anchors remains absent from the current panel.
- Regime study must remain COMPUTED_EXPLORATORY_WITH_HISTORICAL_GAPS.
- Hard Gate must continue to block release until the required price panel and event windows pass QA.
