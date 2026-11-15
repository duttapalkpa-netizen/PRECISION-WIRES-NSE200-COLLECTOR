#!/usr/bin/env python3
"""Fail-closed parser for MoSPI NIC-2025/NIC-2008 concordance text.

Input must be a UTF-8 text dump retaining source line/page markers:
L10330@P256: <line text>. This module does not fetch or OCR the PDF.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

MARKER = re.compile(r"^L(?P<line>\d+)@P(?P<pdfpage>\d+)(?:-(?P<pdfpage_end>\d+))?:\s?(?P<text>.*)$")
ROW = re.compile(r"^(?P<key>\d{4})\s+(?P<expr>\d{4}(?:\s*\(p\))?(?:\s*\+\s*\d{4}(?:\s*\(p\))?)*(?:\s*\+)?)\s*$", re.I)
CONT = re.compile(r"^\d{4}(?:\s*\(p\))?(?:\s*\+\s*\d{4}(?:\s*\(p\))?)*(?:\s*\+)?\s*$", re.I)
HEADER = re.compile(r"^(?:NIC\s*2025\s*Code|NIC\s*2008\s*Code)$", re.I)
SOURCE_URL = "https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf"

@dataclass
class Row:
    nic2025_class_4d: str
    nic2008_expression_raw: str
    source_fragments: list[str] = field(default_factory=list)
    source_lines: list[int] = field(default_factory=list)
    pdf_pages: list[int] = field(default_factory=list)

    def normalized_expression(self) -> str:
        return re.sub(r"\s+", "", self.nic2008_expression_raw).lower()

    def components(self) -> list[dict]:
        tokens = self.normalized_expression().split("+")
        out = []
        for token in tokens:
            m = re.fullmatch(r"(\d{4})(\(p\))?", token)
            if not m:
                raise ValueError(f"Malformed or incomplete component {token!r} for key {self.nic2025_class_4d}")
            out.append({"code": m.group(1), "partial": bool(m.group(2))})
        return out

    def as_record(self) -> dict:
        comps = self.components()
        if not self.source_lines or not self.pdf_pages:
            raise ValueError(f"Missing source provenance for key {self.nic2025_class_4d}")
        return {
            "nic2025_class_4d": self.nic2025_class_4d,
            "nic2008_expression_raw": self.nic2008_expression_raw,
            "nic2008_components": comps,
            "has_partial": any(x["partial"] for x in comps),
            "has_aggregation": len(comps) > 1,
            "source_printed_pages": sorted({p - 24 for p in self.pdf_pages}),
            "source_line_start": min(self.source_lines),
            "source_line_end": max(self.source_lines),
            "source_pdf_url": SOURCE_URL,
            "extraction_status": "PARSED_FROM_SOURCE_TEXT_NOT_YET_FULL_TABLE_ACCEPTED",
            "source_fragments": self.source_fragments,
        }


def parse_source_lines(lines: Iterable[str]) -> list[Row]:
    rows: list[Row] = []
    current: Row | None = None
    in_table = False
    for raw in lines:
        raw = raw.rstrip("\n")
        mm = MARKER.match(raw)
        if mm:
            line_no, pdf_page, text = int(mm.group("line")), int(mm.group("pdfpage")), mm.group("text").strip()
            pdf_page_end = int(mm.group("pdfpage_end")) if mm.group("pdfpage_end") else pdf_page
        else:
            line_no, pdf_page, text, pdf_page_end = None, None, raw.strip(), None
        if "CONCORDANCE BETWEEN 4-DIGIT INDUSTRY CLASSES" in text:
            in_table = True
            continue
        if not in_table:
            continue
        if text.startswith("EXPLANATORY NOTES") or text.startswith("SECTION ") or text.startswith("DIVISION ") or text.startswith("Group "):
            break
        if not text or HEADER.fullmatch(text):
            continue
        # Strip the printed page number appended at a PDF page boundary.
        text = re.sub(r"\s+\d{3}$", "", text)
        # pdftotext -layout preserves the source's two side-by-side
        # concordance columns. A physical line can therefore contain two
        # independent (NIC-2025 key, NIC-2008 expression) pairs separated by
        # wide whitespace. Split only on 2+ spaces; never split inside a
        # compact expression or silently discard an unmatched column.
        columns = [part.strip() for part in re.split(r"\\s{2,}", text) if part.strip()]
        if len(columns) >= 3:
            if len(columns) % 2:
                raise ValueError(f"Unpaired side-by-side concordance column at line {line_no}: {text!r}")
            for offset in range(0, len(columns), 2):
                pair = f"{columns[offset]} {columns[offset + 1]}"
                m = ROW.fullmatch(pair)
                if not m:
                    raise ValueError(f"Unparsed side-by-side concordance pair at line {line_no}: {pair!r}")
                key, expr = m.group("key"), m.group("expr").strip()
                row = Row(key, expr, [pair], [line_no] if line_no else [], [pdf_page] if pdf_page else [])
                rows.append(row)
                current = row
            continue
        m = ROW.fullmatch(text)
        if m:
            key, expr = m.group("key"), m.group("expr").strip()
            # Attribute a row to the page where its source text begins.
            current = Row(key, expr, [text], [line_no] if line_no else [], [pdf_page] if pdf_page else [])
            rows.append(current)
            continue
        # A blank-key continuation is valid only if the preceding expression ends in '+'.
        if current and current.nic2008_expression_raw.rstrip().endswith("+") and CONT.fullmatch(text):
            current.nic2008_expression_raw += text
            current.source_fragments.append(text)
            if line_no: current.source_lines.append(line_no)
            if pdf_page: current.pdf_pages.append(pdf_page)
            continue
        # A standalone printed page number is metadata only when it agrees with
        # the PDF-page-to-printed-page offset documented for this source (P256 -> 232).
        # Any other numeric token, including 1-3 digit values, is an unresolved
        # table token and must fail closed rather than silently disappearing.
        if re.fullmatch(r"\d{1,3}", text) and pdf_page is not None and text == str(pdf_page - 24):
            continue
        if re.match(r"^\d", text):
            raise ValueError(f"Unparsed numeric source line {line_no}: {text!r}")
    if not rows:
        raise ValueError("No concordance rows found; source text must include table heading and line markers")
    for row in rows:
        row.components()
    return rows


def audit(rows: list[Row], expected_count: int = 463, source_line_min: int = 1, source_line_max: int | None = None) -> dict:
    keys = [r.nic2025_class_4d for r in rows]
    duplicates = sorted(k for k, n in Counter(keys).items() if n > 1)
    forward = {r.nic2025_class_4d: [c["code"] for c in r.components()] for r in rows}
    reverse = defaultdict(list)
    for new, old_codes in forward.items():
        for old in old_codes:
            reverse[old].append(new)
    malformed_keys = sorted(k for k in keys if not re.fullmatch(r"\d{4}", k))
    count_ok = len(rows) == expected_count
    unique_ok = len(set(keys)) == len(keys)
    provenance_complete = all(r.source_lines and r.pdf_pages for r in rows)
    ordered_rows = all(rows[i].source_lines and rows[i + 1].source_lines and max(rows[i].source_lines) < min(rows[i + 1].source_lines) for i in range(len(rows) - 1))
    observed_min = min((min(r.source_lines) for r in rows if r.source_lines), default=-1)
    observed_max = max((max(r.source_lines) for r in rows if r.source_lines), default=-1)
    source_bounds_ok = bool(rows) and observed_min >= source_line_min and (source_line_max is None or observed_max <= source_line_max)
    terminal_key_ok = bool(keys) and keys[-1] == "9900"
    acceptance_ok = count_ok and unique_ok and not malformed_keys and provenance_complete and ordered_rows and source_bounds_ok and terminal_key_ok
    return {
        "row_count": len(rows), "expected_row_count": expected_count,
        "row_count_pass": count_ok, "unique_key_count": len(set(keys)),
        "duplicate_keys": duplicates, "unique_keys_pass": unique_ok,
        "malformed_keys": malformed_keys,
        "provenance_complete": provenance_complete,
        "source_line_order_pass": ordered_rows,
        "source_bounds_pass": source_bounds_ok,
        "terminal_key_9900_pass": terminal_key_ok,
        "forward_mapping_count": len(forward),
        "reverse_mapping_component_count": len(reverse),
        "reverse_multiplicity": {k: len(v) for k, v in sorted(reverse.items())},
        "acceptance": "PASS" if acceptance_ok else "UNKNOWN_BLOCKED",
        "limitations": [
            "Count and uniqueness alone do not prove source completeness.",
            "IIP item-group/weight bridge is outside this parser and remains UNKNOWN until separately evidenced."
        ]
    }


def write_outputs(rows: list[Row], out_prefix: Path, expected_count: int = 463, source_line_min: int = 1, source_line_max: int | None = None) -> dict:
    records = [r.as_record() for r in rows]
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    json_path = out_prefix.with_suffix(".json")
    csv_path = out_prefix.with_suffix(".csv")
    audit_path = out_prefix.with_name(out_prefix.name + "_audit.json")
    json_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["nic2025_class_4d", "nic2008_expression_raw", "nic2008_components", "has_partial", "has_aggregation", "source_printed_pages", "source_line_start", "source_line_end", "source_pdf_url", "extraction_status"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for rec in records:
            writer.writerow({**rec, "nic2008_components": json.dumps(rec["nic2008_components"]), "source_printed_pages": json.dumps(rec["source_printed_pages"])})
    report = audit(rows, expected_count, source_line_min, source_line_max)
    audit_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"json": str(json_path), "csv": str(csv_path), "audit": str(audit_path), **report}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_text", type=Path, help="UTF-8 text dump with L<number>@P<page>: prefixes")
    ap.add_argument("--out-prefix", type=Path, default=Path("nic2025_concordance"))
    ap.add_argument("--expected-count", type=int, default=463)
    ap.add_argument("--source-line-min", type=int, default=1)
    ap.add_argument("--source-line-max", type=int, default=None)
    args = ap.parse_args()
    rows = parse_source_lines(args.source_text.read_text(encoding="utf-8").splitlines())
    result = write_outputs(rows, args.out_prefix, args.expected_count, args.source_line_min, args.source_line_max)
    print(json.dumps(result, indent=2))
    return 0 if result["acceptance"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
