#!/usr/bin/env python3
"""Merge isolated NSE raw shard artifacts without rewriting source CSV bytes."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


FILE_RE = re.compile(r"^sec_bhavdata_full_(\\d{8})\\.csv$")


def discover_shards(root: Path):
    candidates = []
    for sessions in root.rglob("sessions.txt"):
        folder = sessions.parent
        files = list(folder.glob("sec_bhavdata_full_*.csv"))
        if files:
            candidates.append((folder, sessions, files))
    # A root-level sessions.txt is a valid single-shard input too.
    return sorted(candidates, key=lambda item: item[0].as_posix())


def merge(root: Path, output: Path, expected: int) -> int:
    shards = discover_shards(root)
    blockers = []
    if not shards:
        blockers.append(f"No shard artifacts with sessions.txt and raw CSVs found under {root}")
    collected = {}
    listed_all = []
    for folder, sessions_path, files in shards:
        listed = [line.strip() for line in sessions_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if len(listed) != len(set(listed)):
            blockers.append(f"{sessions_path}: duplicate session entries")
        csv_by_date = {}
        for source in files:
            match = FILE_RE.fullmatch(source.name)
            if not match:
                blockers.append(f"{source}: unexpected raw filename")
                continue
            try:
                day = datetime.strptime(match.group(1), "%d%m%Y").date().isoformat()
            except ValueError:
                blockers.append(f"{source}: invalid filename date")
                continue
            if day in csv_by_date:
                blockers.append(f"{folder}: multiple raw files for {day}")
            csv_by_date[day] = source
        for day in listed:
            try:
                datetime.strptime(day, "%Y-%m-%d")
            except ValueError:
                blockers.append(f"{sessions_path}: invalid ISO date {day!r}")
                continue
            if day not in csv_by_date:
                blockers.append(f"{sessions_path}: listed date {day} has no matching raw CSV")
                continue
            if day in collected:
                blockers.append(f"duplicate session across shards: {day}")
                continue
            collected[day] = csv_by_date[day]
            listed_all.append(day)
        for day in sorted(set(csv_by_date) - set(listed)):
            blockers.append(f"{folder}: raw CSV {day} is absent from sessions.txt")

    if len(collected) != expected:
        blockers.append(f"expected exactly {expected} unique sessions, found {len(collected)}")
    if blockers:
        print("\\n".join(f"BLOCKER: {item}" for item in blockers), file=sys.stderr)
        return 1

    output.mkdir(parents=True, exist_ok=True)
    for day, source in sorted(collected.items()):
        target = output / source.name
        if target.exists():
            print(f"BLOCKER: refusing to overwrite {target}", file=sys.stderr)
            return 1
        shutil.copyfile(source, target)
        if target.stat().st_size != source.stat().st_size:
            print(f"BLOCKER: copied byte-size mismatch for {source.name}", file=sys.stderr)
            return 1
    (output / "sessions.txt").write_text("\\n".join(sorted(collected)) + "\\n", encoding="utf-8")
    print(f"MERGED_SHARDS={len(shards)}")
    print(f"UNIQUE_SESSIONS={len(collected)}")
    print(f"FIRST_SESSION={min(collected)}")
    print(f"LAST_SESSION={max(collected)}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=Path("data/raw"))
    parser.add_argument("--expected-sessions", type=int, default=200)
    args = parser.parse_args()
    if args.expected_sessions < 1:
        parser.error("--expected-sessions must be >= 1")
    result = merge(args.input_root, args.output_root, args.expected_sessions)
    if result:
        return result
    audit = subprocess.run(
        [sys.executable, "scripts/research/build_raw_archive_manifest.py",
         "--expected-sessions", str(args.expected_sessions)],
        check=False,
    )
    return audit.returncode


if __name__ == "__main__":
    raise SystemExit(main())
