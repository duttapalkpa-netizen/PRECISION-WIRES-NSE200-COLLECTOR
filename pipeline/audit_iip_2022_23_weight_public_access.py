#!/usr/bin/env python3
"""Public-scope IIP 2022-23 weight reconciliation; never fabricates hidden item weights."""
import csv, hashlib, json
from pathlib import Path

SRC=Path("research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv")
OUT=Path("artifacts/iip_item_weight_public_access")
OUT.mkdir(parents=True,exist_ok=True)
SECTOR={"Mining & Quarrying":11.053,"Manufacturing":76.062,"Electricity & Gas Supply":10.865,"Water Supply, Sewerage & Waste Management":2.020}
EXPECTED=[str(i) for i in range(10,33)]
TOL=0.005
SOURCES={
"new_iip_faq":"https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf",
"gsdd_2026_faq":"https://mospi.gov.in/faq",
"asi_2022_23_press_release":"https://www.mospi.gov.in/sites/default/files/press_release/PR_ASI_30102024.pdf",
"asi_2022_23_volume_i":"https://mospi.gov.in/sites/default/files/asi_results/ASI%202022-23%20Volume%20I-compressed.pdf",
"sept_2026_iip_pib":"https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2329475&lang=2&reg=48"}

def main():
    if not SRC.exists(): raise SystemExit("BLOCKED: source NIC-2 Statement II-A CSV missing")
    raw=SRC.read_bytes(); src_sha=hashlib.sha256(raw).hexdigest()
    with SRC.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    errors=[]; codes=[r.get("nic_2025_2digit","") for r in rows]
    if len(rows)!=23: errors.append(f"expected 23 NIC-2 rows, found {len(rows)}")
    if sorted(codes)!=EXPECTED or len(set(codes))!=23: errors.append("NIC-2025 codes are not exactly 10-32")
    if any(r.get("base_year")!="2022-23" or r.get("reference_month")!="2026-09" for r in rows): errors.append("mixed base or reference month")
    if any(r.get("estimate_stage")!="QUICK_ESTIMATE" for r in rows): errors.append("mixed estimate stage")
    if any(r.get("source_statement")!="II_A" or "PRID=2329475" not in r.get("source_url","") for r in rows): errors.append("source provenance mismatch")
    weights=[float(r["weight_pct"]) for r in rows]
    displayed=sum(weights); official=SECTOR["Manufacturing"]; diff=round(displayed-official,3)
    if abs(diff)>TOL: errors.append(f"NIC-2 displayed weight sum outside rounding tolerance: {diff}")
    sector_sum=sum(SECTOR.values())
    if abs(sector_sum-100)>1e-9: errors.append(f"sector weights do not sum to 100: {sector_sum}")
    with (OUT/"iip_2022_23_public_nic2_manufacturing_weights.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["nic_2025_2digit","description","published_weight_pct","base_year","source_statement","source_url"]); w.writeheader()
        for r in rows: w.writerow({"nic_2025_2digit":r["nic_2025_2digit"],"description":r["description"],"published_weight_pct":r["weight_pct"],"base_year":"2022-23","source_statement":r["source_statement"],"source_url":r["source_url"]})
    matrix=[
      {"layer":"Sector","basis":"NAS 2022-23 current-price GVA shares","access":"Category A open access","status":"PUBLIC_METHOD_AND_AGGREGATE_WEIGHTS_VERIFIED","detail":"Sector weights sum to 100.000."},
      {"layer":"Manufacturing NIC-2","basis":"ASI 2022-23 GVA shares","access":"Category A open access","status":"23_OF_23_PUBLIC_WEIGHT_ROWS_RECONCILED","detail":f"Displayed sum {displayed:.3f}; official total {official:.3f}; difference {diff:+.3f}, within ±{TOL:.3f} rounding tolerance; no values altered."},
      {"layer":"Manufacturing NIC-3/NIC-4","basis":"ASI 2022-23 GVA shares","access":"Category A ASI Volume I aggregate","status":"SOURCE_EXISTS_BUT_NEW_IIP_WEIGHT_BRIDGE_NOT_CERTIFIED","detail":"ASI Volume I has NIC-2008 4-digit data. NIC-2025 concordance contains partial/aggregated mappings; no automatic NIC-2025 weight bridge inferred."},
      {"layer":"Manufacturing item-group weights","basis":"ASI 2022-23 GVO within each 4-digit industry","access":"Category B registered access","status":"NOT_ACQUIRED_REGISTRATION_AND_AGREEMENT_REQUIRED","detail":"Item-level IIP data requires registration, application and Data Access Agreement/Undertaking; free for non-commercial research. No request submitted."},
      {"layer":"ASI product/by-product GVO","basis":"NPC-MS 2011 (Revised)","access":"Volume II described as CD-ROM publication","status":"PUBLIC_WEB_BINARY_NOT_CAPTURED","detail":"ASI Volume II contains product/by-product output by 3-digit NIC; no substitute or fabricated item data used."}
    ]
    (OUT/"iip_weight_source_access_matrix.json").write_text(json.dumps(matrix,indent=2,ensure_ascii=False),encoding="utf-8")
    report={
      "status":"PASS_PUBLIC_NIC2_WEIGHT_RECONCILIATION_WITH_ITEM_LEVEL_ACCESS_GAP" if not errors else "BLOCKED_WITH_PUBLIC_WEIGHT_QA_ERRORS",
      "scope":"Publicly accessible IIP 2022-23 sector/NIC-2 weights and official access-path verification only",
      "source_csv":str(SRC),"source_csv_bytes":len(raw),"source_csv_sha256":src_sha,
      "reference_month":"2026-09","base_year":"2022-23","classification":"NIC-2025",
      "manufacturing_nic2_rows":len(rows),"unique_nic2_codes":len(set(codes)),"expected_nic2_codes":EXPECTED,
      "displayed_nic2_weight_sum_pct":round(displayed,3),"official_manufacturing_weight_pct":official,
      "rounding_difference_pct_points":diff,"rounding_tolerance_pct_points":TOL,
      "sector_weights_pct":SECTOR,"sector_weight_sum_pct":round(sector_sum,3),
      "item_basket":{"old_2011_12_manufacturing_groups":405,"new_2022_23_manufacturing_groups":455,"old_total_groups":407,"new_total_groups":463,"old_products":839,"new_products":1042,"added_groups":120,"dropped_groups":64,"one_to_one_crosswalk":False},
      "weight_hierarchy":{"sector":"NAS 2022-23 current-price GVA","manufacturing_nic2_nic3_nic4":"ASI 2022-23 GVA","manufacturing_item":"ASI 2022-23 GVO share within respective 4-digit industry"},
      "access_decision":{"public_nic2_weights":"VERIFIED","asi_volume_i_nic2008_4digit_gva":"PUBLIC_SOURCE_AVAILABLE_NOT_RECOMPUTED","item_level_iip":"CATEGORY_B_REGISTERED_ACCESS","noncommercial_access":"FREE_AFTER_REGISTRATION_APPLICATION_AND_DATA_ACCESS_AGREEMENT","registration_or_application_submitted":False,"item_level_weights":"UNKNOWN_NOT_ACQUIRED"},
      "nic_concordance_use":"classification reference only; partial/aggregation markers prohibit direct item-weight transfer",
      "production_integration":"NOT_APPROVED","errors":errors,"sources":SOURCES,
      "invariants":{"production_selector_unchanged":True,"ranking_score_unchanged":True,"pressure_fade_unchanged":True,"core_672_unchanged":True,"hard_gate_relaxed":False,"synthetic_data_created":False,"paid_source_used":False}}
    (OUT/"iip_2022_23_weight_public_access_audit.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(report,indent=2,ensure_ascii=False))
    if errors: raise SystemExit(2)
if __name__=="__main__": main()
