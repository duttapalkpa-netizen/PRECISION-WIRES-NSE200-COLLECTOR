# Current-series monthly NIC-2 IIP catalogue route audit

Audit date: 2026-11-08  
Scope: identify a public official route to the April 2026 NIC-2025 Output-PPI IIP observations without guessing a historical catalogue ID or mixing vintages.

## Confirmed official evidence

1. MoSPI's 29 June 2026 May IIP release states that the entire 2022-23 IIP series was revised using Output PPI, superseding the 1 June WPI-based series, and advises users to use the PPI-based series. It identifies detailed NIC-2025 tables as available through e-Sankhyiki.
   - PIB release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
   - Release ID: `IIPMFY26006MAY`
2. MoSPI's e-Sankhyiki public catalogue currently exposes the dataset:
   - Title: `Monthly NIC-2 digit and sectoral indices and growth rates of industrial production upto August 2026`
   - Product: IIP
   - Frequency: Monthly
   - Reference period: Aug 2026
   - Release date: 28 September 2026
   - Table ID: `IIPMFY26018AUG`
   - Catalogue: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
3. The e-Sankhyiki portal FAQ states that Macro Indicators supports filtered CSV downloads and Data Catalogue datasets can be downloaded in Excel. Registration is not required.
   - Portal: https://esankhyiki.mospi.gov.in/
   - IIP Macro Indicators: https://esankhyiki.mospi.gov.in/macroindicators?product=iip

## What this establishes / does not establish

- CONFIRMED: an official current-series monthly NIC-2/sectoral IIP catalogue record exists through August 2026, table ID `IIPMFY26018AUG`.
- HIGH-VALUE NEXT ROUTE: inspect/download this latest monthly NIC-2 table or the IIP Macro Indicators filtered CSV and determine whether its monthly time-series includes April 2026 revised Output-PPI values.
- NOT CONFIRMED: that the August catalogue workbook includes the full historical month panel, or that it contains the April 2026 row/value fields needed for NIC codes 10-32. The public search-index metadata alone does not expose workbook contents.
- NOT CONFIRMED: a separate April 2026 catalogue record/table ID. Do not derive an April ID by counting or interpolating monthly release IDs.
- NOT EXTRACTED: the 23 April 2026 current Output-PPI NIC-2025 IIP values; no file bytes or SHA-256 were captured in this step.

## Correct next retrieval procedure

1. Open the official catalogue and locate table ID `IIPMFY26018AUG`; download its Excel table and preserve the original bytes, filename, download URL, release date and SHA-256.
2. Inspect workbook sheets, headers, notes, reference-period coverage, base year, deflator, classification and NIC code set.
3. Accept April 2026 values only if the downloaded source explicitly identifies base 2022-23, Output PPI, NIC-2025, and an April 2026 monthly observation for each code 10-32.
4. If the August workbook is not a historical monthly panel, use the public IIP Macro Indicators page, select the current base-2022-23 monthly NIC-2 series and April 2026 filter, then download the portal-generated CSV. Record all selections and file provenance.
5. Independently reconcile all 23 values and retain UNKNOWN for any missing or ambiguous row.

## Guardrails and status

- No API credentials, private endpoint, guessed API parameters, or access-control bypass used.
- No cumulative-to-monthly derivation and no 2011-12/2022-23 cross-base arithmetic.
- No values, table IDs, timestamps or hashes fabricated.
- WPI first-release April data remains historical-only and superseded.
- IIP current April extraction: BLOCKED pending official workbook/CSV bytes.
- Project-wide Hard Gate: BLOCKED.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and CORE-672 remain unchanged.
- Spend: ₹0; official public sources only.

This audit records a confirmed public retrieval route and a candidate current monthly table, not completion of the April 2026 value extraction.
