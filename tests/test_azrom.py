import sys
from pathlib import Path
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import azrom

class ScannerTests(unittest.TestCase):
    def test_file_hashing_and_kind(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "my_disk.adf"
            p.write_bytes(b"sample-only")
            rows = list(azrom.scan(Path(td)))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["kind"], "floppy")
            self.assertEqual(rows[0]["size"], 11)
            self.assertIsNone(rows[0]["identified_as"])

    def test_ignore_unrelated_and_no_writes(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "notes.txt"
            p.write_text("hello")
            self.assertEqual(list(azrom.scan(Path(td))), [])
            self.assertEqual(p.read_text(), "hello")

if __name__ == "__main__":
    unittest.main()
