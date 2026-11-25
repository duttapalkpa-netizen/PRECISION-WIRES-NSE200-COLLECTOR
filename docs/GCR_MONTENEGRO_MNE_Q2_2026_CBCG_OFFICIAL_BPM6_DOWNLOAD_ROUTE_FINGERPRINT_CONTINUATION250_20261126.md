# GCR Continuation 250 — Montenegro (MNE) Q2-2026 official CBCG BPM6 download route fingerprint and transfer boundary
Date: 2026-11-26 (Asia/Kolkata)
Decision: A DISTINCT OFFICIAL CBCG BALANCE-OF-PAYMENTS STATISTICS PAGE WAS FOUND AND ITS BPM6 (2010–2026) DOWNLOAD LINK WAS RESOLVED TO AN EXACT ZIP URL. The official page states quarterly EUR BPM6 compilation and is updated 19-Nov-2026. The web retrieval surface rejects the ZIP as unsupported application/zip and a separate direct byte-download attempt failed. No ZIP bytes, workbook/CSV, Q2-2026 separate portfolio asset/liability legs, metadata or SHA-256 were captured. MNE remains BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity / duplicate-prevention preflight
- Re-fetched the current GitHub Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, fixed 63-country matrix, and task-specific MNE C241 report before selecting the task.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`; it is a curated continuity record, not a verbatim export. Reused the C182/C241 MNE route history and C249 handoff.
- Skipped C249 Poland work and all previously accepted PASS work. No IMF re-query, cohort rebuild, CBCG Bulletin PDF byte retry, old CBCG ZIP route retry, MONSTAT NSDP SDMX/XML/Browse retry, or use of Q2 IIP stocks/net totals.
- C241's exact PDF text-reader and byte-download routes remain closed. This continuation tests a different official CBCG statistical-data page and a distinct BPM6 download link.

## 2. New official CBCG statistical-data page
- Official CBCG Balance of Payments page (Montenegrin): https://www.cbcg.me/me/statistika/statisticki-podaci/ekonomski-odnosi-sa-inostranstvom/platni-bilans
- The page states that CBCG compiles Montenegro's BOP under IMF BPM6 and publishes data quarterly in euros. It explains the financial account presentation as net acquisition of assets and net incurrence/increase of liabilities.
- The page was updated 19-Nov-2026 and exposes two distinct downloads: BPM5 (2005–2009) and BPM6 (2010–2026). The BPM6 download was followed through its official page link.
- Exact BPM6 download URL resolved from the official page link: https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip
- This is a distinct route from the earlier CBCG bulletin archive ZIP, CBCG Bulletin 9/2026 PDF, and MONSTAT NSDP XML/Browse routes.

## 3. Transfer/access boundary
- Opening the official BPM6 download link through the available retrieval surface returned HTTP 400 / Unsupported content-type: application/zip. This is a reader capability boundary, not evidence that the CBCG origin server itself returned HTTP 400.
- A separate direct byte-download attempt of the exact official ZIP URL also failed in the current runtime.
- No response headers, content length, archive listing, ZIP bytes, workbook/CSV bytes, sheet names, table headers, row counts or SHA-256 were obtained.
- The URL basename indicates `bop_sep_2026`; it is not proof of the archive's internal period coverage or of Q2-specific portfolio-leg rows. Do not infer archive content from its name.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / fixed 63-country matrix preflight | PASS |
| Library Mother File reviewed | PASS (curated 1–53; scope caveat retained) |
| MNE fixed-cohort membership | PASS (reused) |
| Distinct official CBCG BOP statistical page located | PASS |
| CBCG BPM6 quarterly frequency / EUR presentation | PASS (page methodology) |
| BPM6 (2010–2026) official download link / exact URL resolved | PASS (locator only) |
| Official ZIP bytes / headers / size / archive listing | NOT_CAPTURED |
| Q2-2026 portfolio asset transaction leg | NOT_CAPTURED |
| Q2-2026 portfolio liability transaction leg | NOT_CAPTURED |
| Separate-leg labels / signs / units from downloaded table | NOT_ESTABLISHED |
| National-to-IMF comparison | NOT_DONE |
| Observation-specific vintage bridge | UNKNOWN |
| MNE national validation | BLOCKED / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Decision and next action
- C250 closes this distinct official route-fingerprint attempt. It improves source discovery by resolving the exact CBCG BPM6 download URL, but it does not capture or validate the data.
- Do not retry the same URL with the same unsupported web reader or failed direct downloader. Reopen only if a supported browser download/session, archive retrieval connector, or another distinct official CBCG endpoint can retrieve the ZIP bytes.
- If ZIP bytes become accessible, preserve the original archive, compute SHA-256, inspect workbook/table metadata, identify Q2-2026 period rows and separate portfolio asset/liability transactions, establish units/sign conventions, and only then compare separately to the already archived IMF legs. Vintage remains an independent gate.
- If no supported official byte retrieval capability is available, keep MNE BLOCKED and advance to the next eligible fixed-cohort member after full report-history/route preflight.

## 6. Protected invariants
₹0; official/free sources only; no external contact; no IMF re-query; no cohort rebuild; no synthetic values, fabricated timestamps or hashes; no net-to-leg back-solving; no stock-as-flow substitution; no unsupported FX/sign/scale conversion; UNKNOWN never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No merge, workflow dispatch or production integration.