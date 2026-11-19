# Brazil IMF Dataflow Identity and Access Boundary Audit — Continuation 75
Date: 2026-11-19
Scope: official public IMF registry and IMF SDMX Central Web Services Guide. No authenticated action, no data mutation, no credentials.

## Official public registry evidence
- IMF SDMX Central current Registrations page lists Brazil provider IMF:BR1 under dataflow IMF:BOP6(1.0), with BCB URL:
  https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
  Registry listing also shows other providers under IMF:BOP_BPM6(1.0), and some providers under versioned IMF:BOP_GBPM6 flows. This is evidence of distinct registered Dataflow IDs/provider registrations, not equivalence.
- IMF SDMX Central Reporting Constraints listing separately identifies IMF:BOP_BP6_CONSTRAINT targeting dataflow BOP_BPM6[1.0]. This proves a constraint is attached to that specific dataflow/version; it does not establish that Brazil's IMF:BOP6(1.0) registration is an alias.
- IMF SDMX Central Web Services Guide (last updated May 2025) documents public GET structure queries under https://sdmxcentral.imf.org/sdmx/v2/ and explains structure references can retrieve related data structures, dataflows, codelists and constraints.
- Same guide's example for BOP data submission labels Dataflow IMF:BOP_BPM6(1.0), DataStructure IMF:ECOFIN_DSD(1.0), and DATA_DOMAIN BOP6. These are different SDMX fields. The presence of DATA_DOMAIN=BOP6 must not be confused with a Dataflow ID IMF:BOP6(1.0).
- The guide states registration/re-registration is a private operation for admin/agency/data provider of the Provision Agreement; the secure endpoint uses authenticated POST. Public structure GET and private registration POST are separate capabilities.
- Public registrations page exposes a JavaScript-driven table and buttons; static retrieval alone does not export selected row revision/changelog details. Public page includes Login. No authenticated owner-side UI session was used.

## Brazil identity decision
- Current Brazil PA registration evidence: PA URN IMF:BR_BOP_BP6(1.0); Dataflow IMF:BOP6(1.0); Provider IMF:BR1; BCB URL above.
- BCB payload declaration: IMF:BOP_BPM6(1.0) (previously captured and hashed in prior continuity reports).
- Registry listing for other countries uses IMF:BOP_BPM6(1.0); the official constraint table also targets BOP_BPM6[1.0].
- Official guide example uses BOP_BPM6 as the Dataflow and BOP6 as DATA_DOMAIN. This makes a domain-vs-dataflow namespace confusion a plausible hypothesis to test, but does not resolve Brazil's actual registration mismatch.
- No official structure map, crosswalk, or Brazil-specific PA change event was obtained that authorizes rewriting IMF:BOP6 to IMF:BOP_BPM6. Therefore identity remains BLOCKED; no alias or automatic remap.
- Required closure evidence: exact PA revision/changelog for IMF:BR_BOP_BP6(1.0), original/current registration messages with timestamps/actions, exact Brazil-specific Dataflow and DSD references, and authoritative structure map/crosswalk or provider-side correction evidence if mismatch is a registration error.

## Access boundary and next exact owner action
- The public IMF guide documents that registration operations require private access and authenticated POST; re-registration is a distinct action that updates the Last Updated timestamp. We must not perform it, simulate it, or request/store credentials.
- Exact owner-side action: authorized IMF/BCB data-provider operator opens the exact PA record IMF:BR_BOP_BP6(1.0), exports the PA revision/changelog and registration details, and provides non-secret export files/screenshots with transaction IDs/timestamps/actions and referenced Dataflow/Provider/Data URL. No passwords, session cookies or tokens.
- Until those source records are available, historical PA revision chronology and Brazil dataflow identity stay BLOCKED. This is a real external evidence dependency, not a software parser defect.

## GCR controlled archive replay
- Trigger marker commit: 85e89033c37c6f5f00071446c195b00694c16af9.
- Actions run 44521501249 was IN_PROGRESS at audit preparation; capture step running and artifact pending. No replay conclusion or hash claimed yet.
- Purpose: compare same CDSL archive URL response bytes/table date coverage across three captures, to test whether previous 13-row vs 1-row discrepancy recurs.
- Existing evidence: artifact 14524707532 body 297,824 bytes / hash fc95dc0dade735c9f413ef20a3239e138a6064f2694633aa9635864fd8c7ba2b (13 dates 02–18 Nov); artifact 14527092174 body 73,784 bytes / hash aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df (only 02-Mar-2026). Both HTTP 200.
- No archive completeness or provider flow reconciliation promotion until replay artifact inspection.

## GCR status and controls
- Official raw page capture: PASS (prior runs 44515445620 and 44519322726).
- Dated CDSL sector raw capture: PASS.
- NSDL 19-Nov and CDSL 18-Nov daily totals: within-source arithmetic PASS; matched-date provider reconciliation NOT_DONE.
- CDSL archive historical completeness BLOCKED due conflicting same-URL bodies.
- No production ingestion, weights, or event study admission.
- ₹0; official/free sources only; no synthetic data, daily interpolation, net-to-gross inference, or unapproved conversion. UNKNOWN is never PASS.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged.

## Sources
- IMF registrations: https://sdmxcentral.imf.org/data/registrations.html
- IMF reporting constraints: https://sdmxcentral.imf.org/data/constraints.html
- IMF SDMX Central Web Services Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- IMF BOP dataset: https://data.imf.org/Datasets/BOP


## GCR replay result addendum
- Controlled replay Actions run `44521501249` completed SUCCESS; capture job and artifact upload steps SUCCESS.
- Artifact ID `14527843295`, `gcr-india-fpi-raw-pages-4`, 195,431 bytes; GitHub digest equals independently recomputed ZIP SHA-256 `2c8952476f58637c0f346e695793d2b8c8fd170dac551386ace1e37e0e7aea99`.
- Manifest: 8/8 HTTP 200, zero non-200/error.
- Replay CDSL archive raw body: 70,430 bytes, SHA-256 `3cd92be518721d84e697d42e3f2f8dc8cd6a03df6efea75a3576bf384132c2ec`; visible archive date in body is only `01-Jul-2021`.
- Three captures of same archive route now show materially inconsistent body/date coverage: 13 dates 02–18-Nov-2026 (artifact 14524707532); one 02-Mar-2026 (artifact 14527092174); one 01-Jul-2021 (artifact 14527843295). All HTTP 200. This strongly indicates the initial GET is a date-selection landing/state response rather than a stable complete archive extract. It does not prove the archive itself is missing; archive completeness remains BLOCKED pending documented selection/export semantics.
- Do not infer coverage, merge snapshots, or treat HTTP 200 as valid archive data. No POST or form submission attempted.
- Replay ZIP entry `cdsl_daily_archive.html` hash above; manifest hash `80dd5662a619f44fe9a661dcc64d4895286efddce1d2ea2ce01529661a43c239`; summary reports 8 sources, 8 HTTP 200, 0 errors.
- Replay run/artifact result is research-only. India daily matched-date reconciliation remains NOT_DONE; production ingestion BLOCKED.
