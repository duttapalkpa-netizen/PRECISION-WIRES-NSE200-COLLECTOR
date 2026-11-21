# CHN SAFE Chinese attachment route and COL BanRep official-series discovery — Continuation 136
Date: 2026-11-21 (Asia/Kolkata)
Status: CHN remains PARTIAL / BLOCKED; COL official series discovery PASS, exact data retrieval BLOCKED / NOT_DONE.

## 1. Continuity preflight
- Reopened the current GCR Master Priority Queue, 63-country Q2-2026 both-leg cohort, CHN SAFE detailed-workbook audit, CHN SAFE-vs-IMF comparison, UKR C134/C135 evidence and current Continuation 135 decision.
- Prior PASS work was excluded: CHN abridged release arithmetic and IMF exact-key receipt; UKR IIP transaction-column numerical check; all earlier country-level checks. No IMF re-query and no cohort rebuild.
- Fixed 63-country cohort remains immutable. The next sequence after the blocked CHN route is COL, consistent with the prior batch order and the cohort.

## 2. CHN — genuinely distinct Chinese-language SAFE attachment
- Official English detailed time-series page: https://www.safe.gov.cn/en/2019/0329/1496.html ; attachment URL already tested: https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx
- Located the separate official Chinese-language record: https://www.safe.gov.cn/safe/2019/0627/13519.html
- Chinese record metadata: index 000014453-2019-00427; dispatch date 2026-09-29; title “中国国际收支平衡表时间序列(BPM6)”.
- Its attachment resolves to a different XLSX URL: https://www.safe.gov.cn/safe/file/file/20260929/6674650e17de4f20a45c64610118a96f.xlsx
- Browser retrieval returned HTTP/tool 400 unsupported XLSX MIME. A separate direct container download attempt also failed. No workbook bytes, response headers/content length, sheet names, workbook hash, exact Q2 rows, or revision metadata were captured.
- This is a distinct official attachment endpoint, but retrieval remains blocked. Do not retry either known XLSX URL through the same unsupported retrieval paths. CHN asset sign mapping remains unresolved; CHN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 3. COL — BanRep official portfolio transaction series discovery
- Official BanRep SUAMECA multiple-download catalogue: https://suameca.banrep.gov.co/descarga-multiple-de-datos/
- Search-indexed official catalogue explicitly lists two separate quarterly BOP portfolio-investment transaction series:
  1. “Balanza de pagos - Cuenta financiera - inversión de cartera - adquisición neta de activos financieros - trimestral”
  2. “Balanza de pagos - Cuenta financiera - inversión de cartera - pasivos netos incurridos - trimestral”
- Both are labelled current USD millions, quarterly, available 2000-03-31 through 2026-06-30, disclosure date 2026-09-01. This is a valid national BOP transaction-series locator and not an IIP stock proxy.
- The catalogue page and SUAMECA series page could not be opened through the retrieval bridge (HTTP 502 / timeout). No series IDs, downloadable export, exact Q2-2026 observations, raw bytes, SHA-256, or revision-vintage metadata were captured.
- BanRep's official Q2-2026 BOP report (published 2026-09-01) confirms the Q2 reporting period and discusses net portfolio-instrument liquidations, but its accessible narrative does not provide the separate portfolio asset/liability values needed for this gate. It must not be used to infer either leg.
- COL status: official separate-series discovery PASS; exact values/raw capture/sign-vintage validation NOT_DONE; COL PARTIAL / BLOCKED; aggregate NOT_AUTHORIZED.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| CHN Chinese-language SAFE detail record identified | PASS |
| CHN attachment is distinct from English endpoint | PASS |
| CHN XLSX bytes / SHA / workbook inspection | BLOCKED |
| CHN asset sign mapping / full dual-leg validation | NOT_ESTABLISHED / NOT PASS |
| COL official separate portfolio asset and liability series located | PASS |
| COL frequency, unit, end-period and disclosure date captured from catalogue | PASS |
| COL exact Q2 values / series IDs / raw export / SHA | NOT_DONE |
| COL national sign and vintage bridge | NOT_ESTABLISHED |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Next exact actions
1. COL: use a genuinely different supported route to retrieve the two already identified SUAMECA series (not the same 502 catalogue URL); capture series identifiers, exact 2026-Q2 values, original response bytes, retrieval timestamp, unit, signs, revision metadata and SHA-256.
2. Compare COL asset and liability legs separately against the existing archived IMF exact-key rows. No IMF re-query, no net-to-leg inference, no IIP-stock substitution.
3. If SUAMECA export remains inaccessible, preserve COL as PARTIAL/BLOCKED and advance to the next unvalidated member in the fixed cohort; do not repeat the same failing URL.
4. CHN remains closed to same-endpoint retries. Resume only if a genuinely supported file-transfer route becomes available.

## 6. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, inferred sign/scale transform, stock-as-flow, net-to-leg back-solving, IMF re-query, cohort rebuild, or aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
