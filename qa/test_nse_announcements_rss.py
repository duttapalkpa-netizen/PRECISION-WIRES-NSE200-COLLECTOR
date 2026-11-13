import importlib.util
import unittest

spec = importlib.util.spec_from_file_location("nse_rss", "collector/nse_announcements_rss.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class RSSParserTests(unittest.TestCase):
    def test_preserves_original_pubdate_and_guid(self):
        raw = b'''<?xml version="1.0"?><rss version="2.0"><channel><item><title>Example</title><link>https://example.invalid/a</link><guid isPermaLink="false">id-1</guid><pubDate>Fri, 13 Nov 2026 12:00:00 +0530</pubDate><description>Issuer text</description></item></channel></rss>'''
        items = mod.parse_rss(raw)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["guid"], "id-1")
        self.assertEqual(items[0]["guid_is_permalink"], "false")
        self.assertEqual(items[0]["pubDate_original"], "Fri, 13 Nov 2026 12:00:00 +0530")
        self.assertEqual(items[0]["description_original"], "Issuer text")

    def test_missing_guid_is_retained(self):
        items = mod.parse_rss(b"<rss><channel><item><title>No ID</title></item></channel></rss>")
        self.assertEqual(len(items), 1)
        self.assertIsNone(items[0]["guid"])

    def test_rejects_dtd_and_entities(self):
        raw = b'<!DOCTYPE rss [<!ENTITY x "bad">]><rss><channel/></rss>'
        with self.assertRaisesRegex(ValueError, "DTD_OR_ENTITY"):
            mod.parse_rss(raw)

    def test_rejects_wrong_root(self):
        with self.assertRaisesRegex(ValueError, "UNEXPECTED_XML_ROOT"):
            mod.parse_rss(b"<html/>")

if __name__ == "__main__":
    unittest.main()
