import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import json

import notebooklm_batch as app


class Checkbox:
    def __init__(self):
        self.checked = False

    def is_checked(self):
        return self.checked

    def locator(self, selector):
        assert selector == "xpath=ancestor::label"
        return self

    def click(self):
        self.checked = not self.checked


class Page:
    def __init__(self, filenames):
        self.boxes = {filename: Checkbox() for filename in filenames}

    def get_by_role(self, role, name, exact=False):
        assert role == "checkbox" and exact
        return self.boxes[name]

    def wait_for_timeout(self, milliseconds):
        pass


class NotebookLMBatchTests(unittest.TestCase):
    def test_chrome_profile_is_selected_by_display_name(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Local State").write_text(json.dumps({
                "profile": {
                    "last_used": "Default",
                    "info_cache": {"Default": {"name": "Moon"}, "Profile 2": {"name": "Ghar"}},
                }
            }))
            self.assertEqual(app.profile_name(root, "Ghar"), "Profile 2")

    def test_select_sources_selects_only_requested_chapter(self):
        filenames = ["chapter-6.pdf", "chapter-7.pdf"]
        page = Page(filenames)
        app.select_sources(page, ["chapter-6.pdf"], filenames)
        self.assertTrue(page.boxes["chapter-6.pdf"].checked)
        self.assertFalse(page.boxes["chapter-7.pdf"].checked)

    def test_select_sources_can_restore_all_chapters(self):
        filenames = ["chapter-6.pdf", "chapter-7.pdf"]
        page = Page(filenames)
        app.select_sources(page, filenames, filenames)
        self.assertTrue(all(box.checked for box in page.boxes.values()))

    def test_every_studio_prompt_starts_with_an_explicit_tool_request(self):
        for kind, action in app.STUDIO_ACTIONS.items():
            with self.subTest(kind=kind):
                prompt = app.studio_prompt(kind, "Instructions")
                self.assertTrue(prompt.startswith(action))
                self.assertIn(app.STUDIO_EXECUTE_NOW, prompt)
                self.assertTrue(prompt.endswith("\n\nInstructions"))

    def test_assessment_is_split_into_two_single_report_prompts(self):
        question = app.assessment_document_prompt("Social Science", "question paper")
        answer = app.assessment_document_prompt("Social Science", "answer key")
        self.assertIn("only the final, print-ready QUESTION PAPER", question)
        self.assertNotIn("ANSWER KEY AND MARKING SCHEME", question)
        self.assertIn("only the final, print-ready ANSWER KEY AND MARKING SCHEME", answer)
        self.assertIn("requested immediately before this message", answer)


if __name__ == "__main__":
    unittest.main()
