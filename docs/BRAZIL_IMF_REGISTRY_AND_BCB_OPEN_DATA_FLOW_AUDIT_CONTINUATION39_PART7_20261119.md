# Brazil BOP Identity & GCR Independent Flow Feed Audit — Continuation 39 Part-7
Date: 2026-11-19
Scope: use new public IMF registration evidence and official BCB open-data resources; avoid known failed IMF transaction-ID-2 calls.

## Executive result
**New independent evidence path found: PASS (source discovery). Brazil reconstruction remains BLOCKED for IMF identity/chronology; GCR flow-panel ingestion remains NOT_DONE pending raw archival and QA.**

## 1. New IMF registry evidence
The public IMF SDMX Central Registrations page lists:
- Dataflow: `IMF:BOP6(1.0)`
- Data Provider: `IMF:BR1`
- Registered URL: `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`
- Last Updated: `2026-10-26T11:47:29.000Z`
Public registry page: https://sdmxcentral.imf.org/data/registrations.html
This is direct public evidence that the current registry row associates BR1 with BOP6 and that URL. It corroborates the previously parsed Brazil PA -> BOP6 / BR1 structure reference. It does NOT by itself establish the XML payload's internal Dataflow declaration, prove BOP6/BOP_BPM6 equivalence, reveal historical registration actions, or provide the PA revisions/changelog. The registered XML URL returned an unsupported XML content-type error in the web reader; no byte-level hash is claimed.

The public historical activity/data-log page was inspected, but it did not return usable event rows in the public page rendering. The IMF SDMX Central Web Services Guide states registration POST operations are private and require agency/data-provider/admin access; no private operation attempted.

## 2. New BCB independent official flow source path
Official BCB Open Data Portal, Department of Economics (BCB/Depec), publishes free ODbL datasets with JSON/CSV resources and monthly SGS series. This is a separate national-source path and can support GCR independently of resolving the IMF registry identity.
- Portfolio investment — monthly net: SGS 22905, unit million USD, monthly, temporal coverage from 1995-01. JSON resource: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json . The public JSON response shows observations through 2026-09; latest visible observation: 2026-09-01, value 4967.8 (million USD). Dataset description covers portfolio assets and liabilities; treat 22905 as a broad portfolio net series only, not as a separately identified assets or liabilities series.
- Portfolio investment — net acquisition of financial assets, monthly net: SGS 22906. The dataset metadata explicitly describes financial-asset acquisitions and gives million USD/monthly coverage from 1995-01.
- Portfolio investment — net incurrence of liabilities, monthly inflows: SGS 22925. The metadata identifies liability inflows separately, million USD/monthly coverage from 1995-01.
- Portfolio investment — debt securities, monthly inflows: SGS 22940; separate instrument category.
Sources:
https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net
https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
https://opendata.bcb.gov.br/pt_BR/dataset/22925-portfolio-investment---net-incurrence-of-liabilities---monthly---inflows
https://opendata.bcb.gov.br/dataset/22940-portfolio-investment---debt-securities---monthly---inflows
The public portal identifies BCB/Depec as author/maintainer and Open Data Commons Open Database License (ODbL). BCB's dataset 22905 page exposes JSON and CSV resources; the JSON endpoint returned visible observations via the public web reader. CSV reader did not render due unsupported text/csv. No raw file download, retrieval UTC, headers, byte count, or SHA-256 was captured in this task; therefore this is source discovery and a sample data visibility check, not immutable archival PASS.

## 3. Interpretation safeguards
- Do not combine 22905, 22906, 22925 and 22940 without reconciling definitions, instrument coverage and sign conventions.
- 22905 is not a substitute for the IMF BOP6 SDMX payload and does not resolve PA identity.
- Monthly national-source observations cannot be daily-interpolated.
- Keep portfolio assets, portfolio liabilities, debt securities, equity/investment-fund shares, direct investment, reserve assets and other investment as separate families.
- A value displayed for 2026-09 is an observation period, not publication timestamp or retrieval timestamp.

## 4. Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| Public IMF registry shows BOP6 / BR1 / BCB URL | PASS | Live public registrations page row |
| Registry last-updated timestamp captured | PASS | 2026-10-26T11:47:29Z |
| Historical BR1 registration actions | BLOCKED / NOT_EXPOSED | Public activity rendering no usable event rows |
| Exact PA revision/changelog | BLOCKED | Requires provider-side evidence |
| BOP6 vs BOP_BPM6 equivalence | NOT_PROVEN | Separate IDs/constraints; registry row alone is not alias evidence |
| BCB ODbL portfolio dataset discovery | PASS | Official BCB/Depec pages |
| 22905 JSON observation visibility | PASS (sample/render) | Public JSON endpoint shows data through 2026-09 |
| 22905 immutable raw archive + SHA-256 | NOT_DONE | No raw download capture in this task |
| 22906 assets / 22925 liabilities candidate series | PASS (metadata discovery) | Official dataset descriptions |
| Exact 22906/22925 data retrieval and QA | NOT_DONE | Not downloaded/validated here |
| Brazil reconstruction complete | BLOCKED | Identity and chronology gates open |
| GCR synchronized country panel / score | NOT_READY | Multi-source raw archive, matched periods/vintages and QA remain incomplete |

## 5. Next actions
1. Extend the collector with small isolated jobs for SGS 22905, 22906, 22925 and 22940 JSON/CSV: fetch, response headers, retrieval UTC, byte count, SHA-256, schema/date/duplicate/null checks, latest observation and manifest.
2. Keep each series in its own immutable family and add a metadata contract for unit, frequency, sign, definition, temporal coverage, publication timestamp (if separately available), retrieval timestamp, source vintage and URL.
3. Compare 22906 and 22925 against corresponding IMF BOP6 portfolio asset/liability dimensions only after exact instrument and sign mapping.
4. For Brazil identity, retain the public registry row as corroborating evidence, but obtain the provider-side PA Revisions/Changelog/Compare export and dated BR1 registration actions through authorized official access. No credentials in chat; no registry writes.
5. Reconcile Chile old/current BDE vintage separately; do not use Brazil data as a proxy.

## Invariants
₹0; official/free sources only; no synthetic values, guessed IDs, fabricated timestamps/hashes, unapproved aliases/crosswalks, interpolation or private authenticated actions. UNKNOWN is never PASS. No production integration, macro weights, EMDE aggregate, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
