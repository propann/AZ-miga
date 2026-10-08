#!/usr/bin/env python3
"""AZ-miga read-only local media scanner. Python standard library only."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import zlib

KINDS = {
    ".rom": "kickstart", ".bin": "firmware", ".adf": "floppy",
    ".adz": "floppy-compressed", ".hdf": "hard-disk", ".hdz": "hard-disk-compressed",
    ".iso": "cd-image", ".cue": "cd-cue", ".lha": "archive", ".lzh": "archive",
    ".ipf": "floppy-preservation", ".rp9": "amiga-package",
}
# Public identification checksum metadata (no ROM content).
KNOWN = {
    "891e9a547772fe0c6c19b610baf8bc4ea7fcb785": ("Kickstart 1.3 r34.005", "A500", "kick34005.A500"),
    "e21545723fe8374e91342617604f1b3d703094f1": ("Kickstart 3.1 r40.068", "A1200", "kick40068.A1200"),
    "02843c4253bbd29aba535b0aa3bd9a85034ecde4": ("Kickstart 2.05 r37.350", "A600", "kick37350.A600"),
    "f0b4e9e29e12218c2d5bd7020e4e785297d91fd7": ("Kickstart 3.0 r39.106", "A4000", "kick39106.A4000"),
}
CHUNK = 1024 * 1024

def inspect(path):
    h1, h256, crc, size = hashlib.sha1(), hashlib.sha256(), 0, 0
    with path.open("rb") as inp:
        for chunk in iter(lambda: inp.read(CHUNK), b""):
            h1.update(chunk)
            h256.update(chunk)
            crc = zlib.crc32(chunk, crc)
            size += len(chunk)
    sha1 = h1.hexdigest()
    known = KNOWN.get(sha1)
    return {
        "path": str(path.resolve()), "name": path.name, "size": size,
        "kind": KINDS.get(path.suffix.lower(), "unknown"),
        "sha1": sha1, "sha256": h256.hexdigest(), "crc32": f"{crc:08x}",
        "identified_as": known[0] if known else None,
        "model": known[1] if known else None,
        "suggested_name": known[2] if known else None,
        "confidence": "sha1-exact" if known else "unidentified",
    }

def scan(folder):
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in KINDS:
            try:
                yield inspect(path)
            except (OSError, PermissionError) as exc:
                yield {"path": str(path), "error": str(exc)}

def save_db(records, target):
    with sqlite3.connect(target) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS media (
        path TEXT PRIMARY KEY, name TEXT, size INTEGER, kind TEXT, sha1 TEXT,
        sha256 TEXT, crc32 TEXT, identified_as TEXT, model TEXT,
        suggested_name TEXT, confidence TEXT, last_scan TEXT DEFAULT CURRENT_TIMESTAMP)""")
        for row in records:
            if "error" in row:
                continue
            con.execute("""INSERT OR REPLACE INTO media
            (path,name,size,kind,sha1,sha256,crc32,identified_as,model,suggested_name,confidence)
            VALUES (:path,:name,:size,:kind,:sha1,:sha256,:crc32,:identified_as,:model,:suggested_name,:confidence)""", row)

def main():
    parser = argparse.ArgumentParser(description="AZ-miga local media scanner (never uploads files)")
    parser.add_argument("directory", type=Path, help="Directory containing your own media")
    parser.add_argument("--json", type=Path, help="Write scan result JSON")
    parser.add_argument("--db", type=Path, help="Update local SQLite catalogue")
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error("Directory does not exist")
    rows = list(scan(args.directory))
    for row in rows:
        if "error" in row:
            print("ERROR", row["path"], row["error"])
        else:
            print(f'{row["kind"]:20} {row["size"]:>10} {row["identified_as"] or "unknown":25} {row["path"]}')
    if args.json:
        args.json.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.db:
        save_db(rows, args.db)
    print(f"Scanned {len(rows)} file(s); exact identifications: {sum(bool(x.get('identified_as')) for x in rows)}")

if __name__ == "__main__":
    main()
