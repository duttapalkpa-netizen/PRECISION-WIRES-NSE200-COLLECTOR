# NSE–BSE Taxonomy Inventory Extraction Checkpoint
Recorded: 2026-11-17 (Asia/Kolkata)
Status: PARTIAL SOURCE-LEVEL RECONCILIATION; FULL CODE DIFF NOT COMPLETED
Scope: Research-only; no parser/registry/production changes.

## Prior work not repeated
- Authority verification, BSE/NSE hierarchy comparison and version mismatch detection were already recorded as complete in the Chapter 31 screenshot.
- Previously discussed code examples (including Copper, Pharmaceuticals, Dredging and candidate rename/recode examples) are not new discoveries and are not reclassified here.
- No code-level full inventory or issuer mapping is claimed.

## Official source documents opened in this checkpoint
1. NSE Indices Industry Classification Structure, March 2022 (34-page PDF):
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE%20Indices_Industry%20Classification%20Structure-2022-03.pdf
2. NSE Indices Industry Classification Structure, July 2023 (23-page PDF):
   https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf
3. BSE India Industry Classification Structure (16-page PDF):
   https://www.bseindices.com/Downloads/India_Industry_Classification_Structure.pdf
4. BSE India Sector Leaders methodology paper, October 2025:
   https://www.bseindices.com/Downloads/BSE_India_Sector_Leader_Paper_Oct_2025.pdf

## Directly inspected source facts
- NSE March 2022 PDF contains the hierarchical columns MES_Code, Sect_Code, Ind_Code, Basic_Ind_Code and definitions. Examples directly visible include IN010302002 Copper and IN020101002 2/3 Wheelers; the 2022 definition includes bicycles.
- NSE July 2023 PDF uses the same hierarchical code fields. IN020101002 2/3 Wheelers explicitly excludes bicycles and tricycles; IN020201002 Cycles includes bicycles and tricycles.
- July 2023 source shows IN020101004 Auto Dealer and IN020102007 Trading - Auto Components. These exact codes differ from 2022's IN020101003 Trading - Automobiles and IN020102005 Trading - Auto Ancillaries. These are observed code/name changes, but full transition semantics are not inferred.
- BSE classification PDF contains the same code hierarchy and has visible rows including IN010302002 Copper and IN020101004 Auto-Dealer. BSE October 2025 methodology paper states 12 macro-economic indicators, 22 sectors, 59 industries and 197 basic industries.
- The above are sampled/visible source facts only; no full-document inventory was extracted or counted in this checkpoint.

## Newly observed high-value discrepancy
NSE March 2022 IN020101002 definition includes bicycles; July 2023 version excludes bicycles/tricycles, while July 2023 separately lists IN020201002 Cycles. This is a scope change / classification reassignment signal, not evidence that the old code was simply renamed. Preserve both versioned rows and definitions.

## Work status
- Official source discovery and PDF text inspection for the four documents: PASS for this bounded checkpoint.
- Full 2022/2023 NSE code extraction: NOT_DONE.
- Full BSE code extraction and version/date provenance: NOT_DONE.
- Bidirectional exact-code diff: NOT_DONE.
- Definition-level semantic diff: PARTIAL (only observed examples above).
- Historical version archive with raw PDF byte SHA-256: NOT_DONE; PDFs were inspected through the web document reader, but raw bytes were not archived or hashed in this checkpoint.
- Issuer-level mapping: NOT_DONE.
- Parser/registry integration: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next actions (do not repeat source discovery)
1. Obtain machine-readable/raw official PDF bytes or reliable text exports for all three classification PDFs; archive originals and compute SHA-256.
2. Extract all hierarchy rows into versioned records, preserving codes as strings and definitions verbatim.
3. Independently validate counts and uniqueness at each hierarchy level against source totals.
4. Generate exact-code intersection/addition/removal tables and separate name/definition changes.
5. Reconcile BSE against NSE by exact code and version, leaving ambiguous mappings UNKNOWN.
6. Only after full inventory QA, consider issuer-level mapping; no automatic production mapping.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is neither PASS nor FAIL. ₹0 spend; official sources only. No synthetic data, no inferred timestamps, no production change.
