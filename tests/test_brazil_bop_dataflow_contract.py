import tempfile, unittest
from pathlib import Path
from qa.audit_brazil_bop_dataflow_contract import audit

class BrazilBOPDataflowContractTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
  for d in ["brazil_bop","imf_bop_dsd/bop6_dataflow","imf_bop_dsd/dataflow","imf_bop_dsd/bop6_constraint","imf_bop_dsd/constraint"]:
   (self.root/d).mkdir(parents=True,exist_ok=True)
  (self.root/"brazil_bop/response.xml").write_text('''<StructureSpecificData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:test https://sdmxcentral.imf.org/ws/public/sdmxapi/rest/schema/dataflow/IMF/BOP_BPM6/1.0?format=sdmx-2.1"><Header><ID>IREF149528</ID><Prepared>2026-10-26T11:42:36Z</Prepared><Sender id="ZZZ"/><Structure structureID="IMF_BOP_BPM6_1_0" namespace="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD"/></Header><DataSet><Series DATA_DOMAIN="BOP6" REF_AREA="BR" INDICATOR="A"/><Series DATA_DOMAIN="BOP6" REF_AREA="BR" INDICATOR="B"><Obs TIME_PERIOD="2026-01" OBS_VALUE="1"/></Series></DataSet></StructureSpecificData>''')
  (self.root/"brazil_bop/bop6_registration_alignment.json").write_text('''{"registration_snapshot":{"row":{"dataflow":"IMF:BOP6(1.0)","provider":"IMF:BR1","registered_url":"https://www.bcb.gov.br/source.xml"}}}''')
  (self.root/"brazil_bop/response_headers.txt").write_text("Last-Modified: Mon, 26 Oct 2026 11:44:11 GMT\n")
  (self.root/"brazil_bop/transfer_metadata.txt").write_text("http_code=200\nsize_download=1\n")
  (self.root/"brazil_bop/capture_manifest.json").write_text('{"status":"PASS_RAW_XML_PARSE"}')
  for path,df,name in [
   ("imf_bop_dsd/bop6_dataflow/raw.xml","BOP6","Balance of Payments (BPM6) for Collection"),
   ("imf_bop_dsd/dataflow/raw.xml","BOP_BPM6","Balance of Payments -- BPM6")]:
   (self.root/path).write_text(f'<Structure><Dataflow agencyID="IMF" id="{df}" version="1.0"><Name>{name}</Name><Structure><Ref class="DataStructure" id="ECOFIN_DSD" agencyID="IMF" version="1.0"/></Structure></Dataflow></Structure>')
  for path,cid,df,codes in [
   ("imf_bop_dsd/bop6_constraint/raw.xml","BOP6_CONSTRAINT","BOP6",["A","B","C"]),
   ("imf_bop_dsd/constraint/raw.xml","BOP_BP6_CONSTRAINT","BOP_BPM6",["A"])]:
   vals="".join(f"<Value>{x}</Value>" for x in codes)
   (self.root/path).write_text(f'<Structure><ContentConstraint id="{cid}" type="Allowed"><ConstraintAttachment><Dataflow><Ref class="Dataflow" id="{df}" agencyID="IMF" version="1.0"/></Dataflow></ConstraintAttachment><CubeRegion><KeyValue id="INDICATOR">{vals}</KeyValue></CubeRegion></ContentConstraint></Structure>')
 def tearDown(self): self.tmp.cleanup()
 def test_exact_dataflow_mismatch_and_constraint_membership(self):
  r=audit(self.root, verify_hashes=False)
  self.assertEqual(r["bcb_header"]["dataflow"],"IMF:BOP_BPM6(1.0)")
  self.assertEqual(r["provenance"]["registration_snapshot"]["dataflow"],"IMF:BOP6(1.0)")
  self.assertEqual(r["imf_dataflows"]["data_structure_id"],"ECOFIN_DSD")
  self.assertEqual(r["constraints"]["BOP6_CONSTRAINT"]["payload_allowed_count"],2)
  self.assertEqual(r["constraints"]["BOP_BP6_CONSTRAINT"]["payload_allowed_count"],1)
 def test_truncated_payload_fails_closed(self):
  (self.root/"brazil_bop/response.xml").write_text("<StructureSpecificData>")
  with self.assertRaisesRegex(ValueError,"Malformed or truncated XML"): audit(self.root, verify_hashes=False)
 def test_header_identity_change_fails_closed(self):
  p=self.root/"brazil_bop/response.xml"
  p.write_text(p.read_text().replace("BOP_BPM6","BOP6"))
  with self.assertRaisesRegex(ValueError,"no longer identifies"): audit(self.root)
 def test_wrong_constraint_attachment_fails_closed(self):
  p=self.root/"imf_bop_dsd/constraint/raw.xml"
  p.write_text(p.read_text().replace('id="BOP_BPM6"','id="BOP6"'))
  with self.assertRaisesRegex(ValueError,"BOP_BPM6 constraint attachment mismatch"): audit(self.root)
if __name__=="__main__": unittest.main()
