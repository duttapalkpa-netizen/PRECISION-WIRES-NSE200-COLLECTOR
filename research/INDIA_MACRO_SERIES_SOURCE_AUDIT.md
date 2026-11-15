# India Macro Series Source Acquisition and Provenance QA

GDP/CPI: MoSPI e-Sankhyiki NAS/CPI catalogue; preserve table IDs, reference periods, release dates, filenames, URLs and raw SHA-256. WPI: OEA/DPIIT 2022-23 index download catalogue. Government capex: CGA Union Government Monthly Accounts Dashboard. PMI: S&P Global is the primary publisher, not a Government of India source; underlying historical survey data requires publisher access/licensing.

Raw source capture is not normalized observation coverage. Do not promote any series to AVAILABLE until reviewed source-specific parsers emit nonempty observations with period, unit, release/publication timestamp, vintage/revision, unique keys, freshness and hash QA. PMI remains public-headline-only absent licensed underlying data.

Next gate: inspect acquired workbooks and implement schema-specific GDP/CPI/WPI/CGA parsers. Only then merge their independently QA-passed rows into one immutable source_coverage snapshot and rerun Factor Registry, P0, Event Study and Hard Gate.
