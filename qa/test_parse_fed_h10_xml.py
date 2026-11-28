import csv
import io
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from pipeline.parse_fed_h10_xml import parse_archive, sha256

MSG = "http://www.SDMX.org/resources/SDMXML/schemas/v1_0/message"
STRUCT = "http://www.SDMX.org/resources/SDMXML/schemas/v1_0/structure"
FRB = "http://www.federalreserve.gov/structure/compact/common"
H10 = "http://www.federalreserve.gov/structure/compact/H10_H10"


def make_fixture(tmp: Path):
    specs = [
        ("JRXWTFB_N.B", "BRD", "Index:_1997_Jan_100", "NA", "100.0", "A"),
        ("JRXWTFN_N.B", "AFE", "Index:_1997_Jan_100", "NA", "101.0", "A"),
        ("JRXWTFO_N.B", "EME", "Index:_1997_Jan_100", "NA", "-9999", "ND"),
        ("RXI_N.B.IN", "INR", "Currency", "INR", "83.5", "A"),
    ]
    series = []
    for code, fx, unit, currency, value, status in specs:
        series.append(
            f'<kf:Series SERIES_NAME="{code}" FREQ="9" UNIT="{unit}" UNIT_MULT="1" FX="{fx}" CURRENCY="{currency}">'
            f'<frb:Obs TIME_PERIOD="2006-01-02" OBS_VALUE="{value}" OBS_STATUS="{status}"/></kf:Series>'
        )
    data = (
        f'<message:MessageGroup xmlns:message="{MSG}" xmlns:frb="{FRB}" xmlns:kf="{H10}">'
        f'<message:Header><message:Prepared>2026-11-09T18:25:06</message:Prepared></message:Header>'
        f'<frb:DataSet id="H10">{"".join(series)}</frb:DataSet></message:MessageGroup>'
    ).encode()
    struct = (
        f'<message:Structure xmlns:message="{MSG}" xmlns:structure="{STRUCT}"><message:CodeLists>'
        '<structure:CodeList id="CL_FREQ"><structure:Code value="9"><structure:Description>Business day</structure:Description>'
        '</structure:Code></structure:CodeList></message:CodeLists></message:Structure>'
    ).encode()
    raw = io.BytesIO()
    with ZipFile(raw, "w") as z:
        z.writestr("H10_data.xml", data)
        z.writestr("H10_struct.xml", struct)
        z.writestr("H10_H10.xsd", '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>')
        z.writestr("frb_common.xsd", '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>')
    archive_bytes = raw.getvalue()
    archive_path = tmp / "raw.zip"
    archive_path.write_bytes(archive_bytes)
    manifest_path = tmp / "raw.manifest.json"
    manifest_path.write_text(json.dumps({
        "sha256": sha256(archive_bytes),
        "source_class": "OFFICIAL_GOVERNMENT",
        "source": "Board of Governors of the Federal Reserve System",
        "source_url": "https://www.federalreserve.gov/test",
        "retrieved_at_utc": "2026-11-12T00:00:00Z",
    }))
    return archive_path, manifest_path


class TestFedH10XmlParser(unittest.TestCase):
    def test_extracts_panel_and_preserves_nd_status(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            archive, raw_manifest = make_fixture(tmp)
            manifest = parse_archive(archive, raw_manifest, tmp / "out")
            self.assertEqual(manifest["calendar"]["rows"], 1)
            self.assertEqual(manifest["selected_series"]["RXI_N.B.IN"]["observations"], 1)
            with (tmp / "out" / "fed_h10_daily_fx_panel.csv").open(newline="") as f:
                row = next(csv.DictReader(f))
            self.assertEqual(row["usd_inr"], "83.5")
            self.assertEqual(row["emerging_usd_index"], "")
            self.assertEqual(row["emerging_usd_index_status"], "ND")
            self.assertEqual(manifest["xsd_validation"]["status"], "UNKNOWN_NOT_RUN")

    def test_rejects_archive_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            archive, raw_manifest = make_fixture(tmp)
            m = json.loads(raw_manifest.read_text())
            m["sha256"] = "0" * 64
            raw_manifest.write_text(json.dumps(m))
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                parse_archive(archive, raw_manifest, tmp / "out")

    def test_rejects_missing_inr_calendar_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            archive, raw_manifest = make_fixture(tmp)
            with ZipFile(archive) as z:
                entries = {n: z.read(n) for n in z.namelist()}
            entries["H10_data.xml"] = entries["H10_data.xml"].replace(
                b'TIME_PERIOD="2006-01-02" OBS_VALUE="83.5"',
                b'TIME_PERIOD="2006-01-03" OBS_VALUE="83.5"',
            )
            buf = io.BytesIO()
            with ZipFile(buf, "w") as z:
                for n, b in entries.items():
                    z.writestr(n, b)
            archive.write_bytes(buf.getvalue())
            m = json.loads(raw_manifest.read_text())
            m["sha256"] = sha256(archive.read_bytes())
            raw_manifest.write_text(json.dumps(m))
            with self.assertRaisesRegex(ValueError, "does not cover"):
                parse_archive(archive, raw_manifest, tmp / "out")


if __name__ == "__main__":
    unittest.main()
