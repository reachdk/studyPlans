import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import classroom_sync as cs


class ClassroomSyncTests(unittest.TestCase):
    def test_subject_filter(self):
        for name in ("Maths", "English", "Social Science", "Physics", "Chemistry",
                     "Biology", "Bio", "CHEM G9B", "German", "IT", "Information Technology"):
            self.assertTrue(cs.selected({"name": name}), name)
        for name in ("Advanced Maths", "Advanced Science", "Physical Education", "Art", "CHEM-G9A"):
            self.assertFalse(cs.selected({"name": name}), name)
        for name in ("CHEM G9B", "Physics Grade IX", "G-9 Bio", "Mathematics - 9A & 9B", "Physics Grade IX"):
            self.assertTrue(cs.selected({"name": name}), name)

    def test_pagination(self):
        calls = []
        def request(**kwargs):
            calls.append(kwargs["pageToken"])
            class R:
                def execute(self):
                    return {"courses": [calls[-1]], "nextPageToken": "next"} if len(calls) == 1 else {"courses": [calls[-1]]}
            return R()
        self.assertEqual(list(cs.pages(request, "courses")), [None, "next"])

    def test_materials_only(self):
        class Resource:
            def __init__(self, data):
                self.data = data
            def list(self, **kwargs):
                return self
            def execute(self):
                return {self.data[0]: self.data[1]}
        class Courses:
            def courseWorkMaterials(self):
                return Resource(("courseWorkMaterial", [{"id": "post", "title": "Unit 1", "materials": [
                    {"driveFile": {"driveFile": {"id": "abc", "title": "Notes"}}},
                    {"link": {"url": "https://example.org", "title": "Reading"}}]}]))
            def courseWork(self):
                return Resource(("courseWork", []))
            def announcements(self):
                return Resource(("announcements", []))
        class Classroom:
            def courses(self):
                return Courses()
        rows = list(cs.attachment_rows(Classroom(), [{"id": "123", "name": "Maths"}]))
        self.assertEqual([r["type"] for r in rows], ["drive", "link"])
        self.assertEqual(rows[0]["file_id"], "abc")

    def test_incremental(self):
        class Get:
            def execute(self):
                return {"name": "Study.pdf", "mimeType": "application/pdf", "modifiedTime": "v1", "size": "12"}
        class Files:
            def get(self, **kwargs):
                return Get()
        class Drive:
            def files(self):
                return Files()
        with tempfile.TemporaryDirectory() as temp, patch.object(cs, "download") as download:
            def create_file(drive, file_id, target, export_mime):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b"%PDF-test")
            download.side_effect = create_file
            rows = [{"type": "drive", "file_id": "abc", "folder": "maths--123"}]
            self.assertTrue(cs.sync(Drive(), rows, Path(temp)))
            self.assertTrue(cs.sync(Drive(), rows, Path(temp)))
            self.assertEqual(download.call_count, 1)
            manifest = json.loads((Path(temp) / "manifest.json").read_text())
    def test_clean_subject(self):
        self.assertEqual(cs.clean_subject("CHEM G9B (2026-27)"), "chemistry")
        self.assertEqual(cs.clean_subject("English Grade 9 (2026-2027)"), "english")
        self.assertEqual(cs.clean_subject("G 9B -IT(402)/26-27"), "information-technology")
        self.assertEqual(cs.clean_subject("G-9 Bio"), "biology")
        self.assertEqual(cs.clean_subject("German  Grade IX"), "german")
        self.assertEqual(cs.clean_subject("Mathematics - 9A & 9B -(2026-2027)"), "mathematics")
        self.assertEqual(cs.clean_subject("Physics Grade IX (2026-27)"), "physics")
        self.assertEqual(cs.clean_subject("Social Science 9A & 9B (2026-27)"), "social-science")

    def test_date_prefixed_naming_and_collision(self):
        class Get:
            def __init__(self, name):
                self.name = name
            def execute(self):
                return {"name": self.name, "mimeType": "application/pdf", "modifiedTime": "v1", "size": "100"}
        class Files:
            def get(self, fileId, **kwargs):
                return Get("Chapter Notes.pdf")
        class Drive:
            def files(self):
                return Files()

        with tempfile.TemporaryDirectory() as temp, patch.object(cs, "download") as download:
            def create_file(drive, file_id, target, export_mime):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b"%PDF-test")
            download.side_effect = create_file

            rows = [
                {"type": "drive", "file_id": "file1_abc123", "course": "Physics Grade IX",
                 "post_created": "2026-08-15T10:00:00.000Z", "folder": "physics"},
                {"type": "drive", "file_id": "file2_xyz789", "course": "Physics Grade IX",
                 "post_created": "2026-08-15T10:00:00.000Z", "folder": "physics"}
            ]
            self.assertTrue(cs.sync(Drive(), rows, Path(temp)))
            manifest = json.loads((Path(temp) / "manifest.json").read_text())
            path1 = manifest["files"]["file1_abc123"]["path"]
            path2 = manifest["files"]["file2_xyz789"]["path"]
            self.assertEqual(path1, "physics/2026-08-15_chapter-notes.pdf")
            self.assertEqual(path2, "physics/2026-08-15_chapter-notes_file2_.pdf")
            self.assertTrue((Path(temp) / path1).is_file())
            self.assertTrue((Path(temp) / path2).is_file())


if __name__ == "__main__":
    unittest.main()
