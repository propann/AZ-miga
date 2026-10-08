#!/usr/bin/env python3
"""Read-only ROM inventory by documented exact CRC32 + byte count."""
import argparse
import json
from pathlib import Path
import zlib

BASE = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((BASE / "data/kickstart-manifest.json").read_text(encoding="utf8"))["entries"]

def file_crc(path):
    result = 0
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            result = zlib.crc32(block, result)
    return f"{result:08x}"

def check(directory):
    expected = {row["crc32"]: row for row in MANIFEST}
    found = {}
    for p in sorted(directory.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in {".rom",".bin",".a500",".a600",".a1200",".a4000",".cd32"}:
            continue
        try:
            crc = file_crc(p)
        except OSError as ex:
            print("ERROR",p,ex)
            continue
        row = expected.get(crc)
        if row:
            found[crc] = p
            print(f"FOUND {row['filename']:20} {p}")
        else:
            print(f"UNKNOWN CRC={crc} {p}")
    for row in MANIFEST:
        if row["crc32"] not in found:
            print(f"MISSING {'REQUIRED' if row['whdload_required'] else 'OPTIONAL'} {row['filename']} [{row['crc32']}]")
    return found

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("directory",type=Path)
    args=a.parse_args()
    if not args.directory.is_dir(): a.error("Directory does not exist")
    check(args.directory)
