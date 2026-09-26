import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
            self.assertEqual(len(manifest["files"]), 1)


if __name__ == "__main__":
    unittest.main()
