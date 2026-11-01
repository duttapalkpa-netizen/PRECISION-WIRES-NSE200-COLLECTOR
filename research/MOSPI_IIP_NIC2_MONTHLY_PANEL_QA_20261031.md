# MoSPI IIP NIC-2 Monthly Panel — implementation and QA gate

This stage preserves raw HTML and extracted source tables, inventories them, and attempts semantic normalization only for a table whose own headers explicitly identify NIC 2025, Description, Weight and at least 12 month-labelled columns.

Normalized output: `iip_nic2_monthly_panel.csv`, one row per NIC-2 code and month, with period, NIC-2025 code, description, published weight, index, base year, frequency, unit and source table ID.

QA rejects duplicate (NIC, period) keys and records row count, unique NICs, unique periods and period bounds. It does not infer data from table position or fill missing observations.

This is a release-vintage panel from the PIB release, not yet a complete e-Sankhyiki back-series. Every monthly release must be appended as a new vintage; revised values must not overwrite earlier published estimates. A subsequent revision reconciliation stage must distinguish quick estimate, first revision and final estimate.

The MoSPI portal describes the IIP detailed dataset and public CSV download facility; its current IIP base is 2022-23. The portal's published release schedule and revision rules must be stored with the source metadata. Until multi-vintage reconciliation and e-Sankhyiki back-series coverage pass, macro_indicators remains unpromoted.
