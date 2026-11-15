# NIC-2025 ↔ NIC-2008 Concordance — Source Line Map and Extraction Boundary

Date: 2026-11-15
Status: OFFICIAL SOURCE TEXT RANGE VERIFIED; STRUCTURED EXTRACTION NOT YET DONE
Purpose: Freeze exact source boundaries for the later 463-row extraction and QA, avoiding repeated discovery.

## Canonical source used in this checkpoint

- Publisher: Government of India, MoSPI / National Statistics Office.
- Official PDF URL: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf
- Browser-opened PDF: 322 pages.
- PDF contents identify the concordance on printed pages 232–238.
- Table heading: “CONCORDANCE BETWEEN 4-DIGIT INDUSTRY CLASSES OF NIC-2025 AND NIC-2008”.
- Source legend: “(p) denotes part, + denotes aggregation of classes”.
- Extracted source line range: 10330–10872 inclusive (table content and page transitions).

## Printed-page to extracted-line map

| Printed page | PDF page marker | Extracted lines | Notes |
|---|---:|---:|---|
| 232 | P256 | 10330–10407 | Table start; heading and legend; first continuation at 0330 |
| 233 | P257 | 10408–10493 | Manufacturing table starts; includes 1512, 1811 |
| 234 | P258 | 10494–10579 | Manufacturing rows incl. 2611/2619, 3101/3102 |
| 235 | P259 | 10580–10671 | Trade rows; includes 4772 split continuation |
| 236 | P260 | 10672–10757 | Services/finance rows |
| 237 | P261 | 10758–10843 | Public/admin, education, arts rows |
| 238 | P262 | 10844–10872 | Final rows through 9900 |

## Mandatory continuation handling

- NIC-2025 key 0330 has its NIC-2008 expression split across lines 10378–10379: 0311(p)+0312(p)+0321(p)+ followed by 0322(p).
- NIC-2025 key 4340 is split across lines 10571–10573.
- NIC-2025 key 4772 is split across lines 10626–10630: first fragment 4772(p)+4789(p)+4791(p)+, followed by a table-header repeat and blank-code continuation 4799(p). Preserve both fragments and join only with table/page sequence evidence.
- Other wrapped expressions must be preserved and joined deterministically; do not treat repeated column headings as data rows.
- The final row 9900 9900 appears at line 10872; the following lines belong to explanatory notes, not the concordance.

## Extraction contract (unchanged)

Every accepted row must preserve:
- nic2025_class_4d as a four-character string;
- nic2008_expression_raw exactly as printed after deterministic line-wrap joining;
- parsed NIC-2008 component codes as four-character strings;
- per-component partial boolean derived only from (p);
- has_partial, has_aggregation;
- printed page, extracted line range, source URL, extraction status.

QA must establish exactly 463 distinct non-empty NIC-2025 class keys, no unexplained duplicate keys, all source rows represented once, all plus-separated components retained, every (p) retained, all codes four digits, and forward/reverse multiplicities independently calculated. The published 463-class taxonomy count is a cross-check, not proof of concordance completeness.

No 2-digit roll-up, no IIP item-group/weight mapping, no index-level conversion, and no production use may be inferred from this class-level table.

## Integrity limitation

- Raw PDF binary download was attempted using the canonical URL during this checkpoint and failed.
- No local PDF binary, byte length, or SHA-256 is available; no raw-file archival is claimed.
- The browser-extracted text is suitable for source inspection and line-boundary planning, but the complete structured 463-row CSV/JSON and parser QA have not yet been generated.
- Existing previously documented examples and PASS safety decisions remain unchanged.

## Progress

- Canonical official PDF browser access: 100% COMPLETE.
- Exact concordance line-range and page map: 100% COMPLETE.
- Continuation-row boundary identification: 100% COMPLETE.
- Raw PDF binary archival / SHA-256: 0% NOT_DONE.
- Full structured extraction: 0% NOT_DONE.
- Parser QA / multiplicity report: 0% NOT_STARTED.
- IIP-specific item-group/weight bridge: UNKNOWN / BLOCKED.

No synthetic rows, fabricated timestamps, paid APIs, spending, external contact, workflow reruns, PR merges, production code changes, or protected V11.3 invariant changes.
