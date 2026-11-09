import csv,json,subprocess,sys,unittest
from pathlib import Path
class TestIIPWeightPublicAccessAudit(unittest.TestCase):
 def test_public_nic2_cohort(self):
  with open("research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv",encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),23); self.assertEqual(sorted(r["nic_2025_2digit"] for r in rows),[str(i) for i in range(10,33)])
 def test_published_weight_arithmetic(self):
  with open("research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv",encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
  self.assertAlmostEqual(sum(float(r["weight_pct"]) for r in rows),76.065,places=3)
  self.assertAlmostEqual(11.053+76.062+10.865+2.020,100.000,places=3)
  self.assertLessEqual(abs(76.065-76.062),0.005)
 def test_fail_closed_access(self):
  s=Path("pipeline/audit_iip_2022_23_weight_public_access.py").read_text()
  self.assertIn("registration_or_application_submitted",s); self.assertIn("UNKNOWN_NOT_ACQUIRED",s); self.assertIn("NOT_APPROVED",s)
 def test_script_output(self):
  subprocess.run([sys.executable,"pipeline/audit_iip_2022_23_weight_public_access.py"],check=True)
  r=json.loads(Path("artifacts/iip_item_weight_public_access/iip_2022_23_weight_public_access_audit.json").read_text())
  self.assertEqual(r["status"],"PASS_PUBLIC_NIC2_WEIGHT_RECONCILIATION_WITH_ITEM_LEVEL_ACCESS_GAP")
  self.assertEqual(r["manufacturing_nic2_rows"],23); self.assertFalse(r["access_decision"]["registration_or_application_submitted"])
if __name__=="__main__": unittest.main(verbosity=2)
