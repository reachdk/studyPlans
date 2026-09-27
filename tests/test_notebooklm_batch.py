import json
import sys
import unittest
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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
                prompt = app.studio_prompt(kind, "Instructions", "G9-PHY-C04-Cards")
                self.assertTrue(prompt.startswith(action))
                self.assertIn('Title the Studio artifact exactly "G9-PHY-C04-Cards"', prompt)
                self.assertIn(app.STUDIO_EXECUTE_NOW, prompt)
                self.assertTrue(prompt.endswith("\n\nInstructions"))
        pdf_prompt = app.studio_prompt("pdf", "Instructions", "G9-MATH-C01-Guide.pdf")
        self.assertIn("Create one PDF from the instructions below and save it in Studio.", pdf_prompt)
        self.assertNotIn("Studio tool", pdf_prompt)

    def test_stream_codes_resolve_to_folder_and_display_name(self):
        self.assertEqual(app.stream_details("PHY"), ("PHY", "science", "Physics"))
        self.assertEqual(app.stream_details("pol"), ("POL", "social-science", "Political Science"))
        self.assertEqual(app.stream_details("Maths"), ("MATH", "mathematics", "Mathematics"))
        with self.assertRaisesRegex(ValueError, "unknown stream"):
            app.stream_details("Science")

    def test_notebook_and_artifact_names_enumerate_the_scope(self):
        path = Path("iesc106--how-forces-affect-motion.pdf")
        self.assertEqual(app.notebook_title("PHY", [4, 5, 6]), "G9-PHY-C04_C05_C06")
        self.assertEqual(app.notebook_title("ENG", [1, 3]), "G9-ENG-U01_U03")
        self.assertEqual(
            app.artifact_title("PHY", [6], "Slides", path),
            "G9-PHY-C06-Forces-Affect-Motion-Slides",
        )
        self.assertEqual(app.artifact_title("MATH", [1, 3], "Diag-QP"), "G9-MATH-C01_C03-Diag-QP.pdf")

    def test_english_uses_chapter_packs_flashcards_quiz_and_two_masters(self):
        jobs = app.english_jobs(2)
        self.assertEqual([kind for kind, _, _ in jobs], ["flashcards", "quiz", "pdf", "pdf"])
        self.assertNotIn("slide deck", [kind for kind, _, _ in jobs])
        self.assertNotIn("mind map", [kind for kind, _, _ in jobs])
        self.assertIn("One page for each prose or dramatic text", app.ENGLISH_UNIT_GUIDE)
        self.assertIn("One page for each poem", app.ENGLISH_UNIT_GUIDE)
        self.assertIn("One page for each grammar topic", app.ENGLISH_UNIT_GUIDE)
        self.assertIn("One page for each writing task", app.ENGLISH_UNIT_GUIDE)

    def test_english_flashcards_and_quiz_scale_with_chapters(self):
        jobs = app.english_jobs(3)
        self.assertIn("Create exactly 40 cards", jobs[0][1])
        self.assertIn("every selected chapter receives 13 or 14 cards", jobs[0][1])
        self.assertIn("exactly 25 questions", jobs[1][1])
        self.assertIn("newly written age-appropriate unseen passage", jobs[1][1])

    def test_english_papers_preserve_cbse_section_weighting(self):
        expected = {1: (5, 5, 10), 3: (10, 10, 20), 6: (20, 20, 40)}
        for chapters, marks in expected.items():
            with self.subTest(chapters=chapters):
                prompt = app.english_assessment_prompt("diagnostic", chapters)
                self.assertIn(f"Reading Comprehension: {marks[0]} marks", prompt)
                self.assertIn(f"Writing Skills and Grammar: {marks[1]} marks", prompt)
                self.assertIn(f"Language through Literature: {marks[2]} marks", prompt)
                self.assertIn("Literature value points while accepting interpretations", prompt)
                self.assertIn("analytic Writing rubric", prompt)
                self.assertIn("PAPER 1 — ENGLISH SKILL DIAGNOSTIC", prompt)
                self.assertLess(len(prompt.split()), 300)

    def test_science_and_social_assessments_use_one_balanced_master(self):
        for subject in ("Science", "Social Science"):
            with self.subTest(subject=subject):
                prompt = app.combined_assessment_prompt(subject, 2)
                self.assertIn("exactly two internally consistent parts", prompt)
                self.assertIn("Balance coverage and marks", prompt)
                self.assertIn("Duration: 45 minutes", prompt)
                self.assertIn("Maximum marks: 20", prompt)
                self.assertIn("PART A — QUESTION PAPER", prompt)
                self.assertIn("PART B — ANSWER KEY AND MARKING SCHEME", prompt)

    def test_mathematics_has_five_jobs_and_no_slide_deck(self):
        jobs = app.mathematics_jobs(2)
        self.assertEqual(len(jobs), 5)
        self.assertEqual(
            [kind for kind, _, _ in jobs],
            ["pdf", "flashcards", "mind map", "pdf", "pdf"],
        )
        self.assertNotIn("slide deck", [kind for kind, _, _ in jobs])

    def test_mathematics_scales_assessment_without_extra_input(self):
        self.assertEqual(app.assessment_scheme(1), (45, 20))
        self.assertEqual(app.assessment_scheme(3), (90, 40))
        self.assertEqual(app.assessment_scheme(6), (180, 80))

    def test_mathematics_blueprints_balance_sections_and_cognitive_marks(self):
        for marks, (sections, cognitive_marks) in app.MATH_ASSESSMENT_BLUEPRINTS.items():
            with self.subTest(marks=marks):
                self.assertEqual(sum(count * each for _, _, count, each in sections), marks)
                self.assertEqual(sum(cognitive_marks), marks)

    def test_mathematics_pdfs_keep_each_paper_and_key_together(self):
        jobs = app.mathematics_jobs(2)
        for _, prompt, _ in jobs[3:]:
            self.assertIn("Duration: 45 minutes", prompt)
            self.assertIn("Maximum marks: 20", prompt)
            self.assertIn("Section A: 4 Multiple-choice questions × 1 mark = 4 marks", prompt)
            self.assertIn("allocate 11 marks to Remembering and Understanding", prompt)
            self.assertIn("Q1 through Q10", prompt)
            self.assertIn("PART A — QUESTION PAPER", prompt)
            self.assertIn("PART B — ANSWER KEY AND MARKING SCHEME", prompt)
            self.assertIn("same numbering", prompt)
            self.assertLess(len(prompt.split()), 300)

    def test_mathematics_study_prompts_limit_history_and_ambiguous_labels(self):
        jobs = app.mathematics_jobs(2)
        self.assertIn("Exclude historical trivia", jobs[0][1])
        self.assertIn("Create exactly 30 cards", jobs[1][1])
        self.assertIn("every selected chapter receives 15 cards", jobs[1][1])
        self.assertNotIn("semicircle", jobs[2][1])
        self.assertIn("exclude names, dates, and historical trivia", jobs[2][1])
        self.assertIn("no more than 12 leaf nodes", jobs[2][1])

    def test_balanced_flashcard_size_scales_and_caps_at_sixty(self):
        self.assertIn("exactly 20 cards", app.balanced_flashcard_prompt("Cards", 1))
        self.assertIn("exactly 50 cards", app.balanced_flashcard_prompt("Cards", 4))
        prompt = app.balanced_flashcard_prompt("Cards", 7)
        self.assertIn("exactly 60 cards", prompt)
        self.assertIn("8 or 9 cards", prompt)

    def test_assessment_master_uses_the_working_note_prompt(self):
        prompt = app.assessment_master_prompt(
            "Assessment instructions", "G9-MATH-C06-Diag-Master.pdf"
        )
        self.assertTrue(prompt.startswith("Generate a comprehensive Assessment PDF Document"))
        self.assertIn('Title the document exactly "G9-MATH-C06-Diag-Master"', prompt)
        self.assertNotIn("Create one PDF", prompt)
        self.assertNotIn(app.STUDIO_EXECUTE_NOW, prompt)

    def test_studio_split_names_one_master_pair(self):
        prompt, outputs = app.studio_split_prompt("G9-MATH-C01_C02-Diag-Master.pdf")
        self.assertEqual(outputs, {
            "G9-MATH-C01_C02-Diag-QP.pdf",
            "G9-MATH-C01_C02-Diag-Key.pdf",
        })
        self.assertIn("create these two PDF files and save them in Studio", prompt)

    def test_split_verifies_outputs_before_deleting_master(self):
        master = "G9-MATH-C01_C02-Diag-Master.pdf"
        expected = {
            "G9-MATH-C01_C02-Diag-QP.pdf",
            "G9-MATH-C01_C02-Diag-Key.pdf",
        }
        with (
            mock.patch.object(
                app,
                "artifact_title_counts",
                side_effect=[Counter({master: 1}), Counter({master: 1, **{title: 1 for title in expected}})],
            ),
            mock.patch.object(app, "send_chat_instruction"),
            mock.patch.object(app, "wait_for_artifacts", return_value={master} | expected),
            mock.patch.object(app, "delete_artifact") as delete,
        ):
            self.assertEqual(app.split_assessment(mock.Mock(), master, {master}), expected)
        delete.assert_called_once_with(mock.ANY, master)

    def test_failed_split_keeps_master(self):
        master = "G9-MATH-C01_C02-Diag-Master.pdf"
        with (
            mock.patch.object(
                app,
                "artifact_title_counts",
                side_effect=[Counter({master: 1}), Counter({master: 1, "Random": 1})],
            ),
            mock.patch.object(app, "send_chat_instruction"),
            mock.patch.object(app, "wait_for_artifacts", return_value={master, "Random"}),
            mock.patch.object(app, "delete_artifact") as delete,
        ):
            with self.assertRaisesRegex(RuntimeError, "Studio created"):
                app.split_assessment(mock.Mock(), master, {master})
        delete.assert_not_called()

    def test_master_deletion_confirms_dialog_and_survives_reload(self):
        page = mock.Mock()
        card = mock.Mock()
        menu_item = mock.Mock()
        dialog = mock.Mock()
        dialog.count.return_value = 1
        dialog.is_visible.return_value = True
        page.get_by_role.side_effect = [menu_item, dialog]
        with (
            mock.patch.object(app, "artifact_card", return_value=card),
            mock.patch.object(
                app,
                "artifact_title_counts",
                side_effect=[Counter(), Counter()],
            ),
        ):
            app.delete_artifact(page, "Master.pdf")

        card.get_by_role.assert_called_once_with("button", name="More", exact=True)
        menu_item.click.assert_called_once_with()
        page.evaluate.assert_called_once()
        page.reload.assert_called_once_with(wait_until="domcontentloaded")

    def test_named_artifact_wait_rejects_random_titles(self):
        with (
            mock.patch.object(app, "wait_for_artifacts", return_value={"Random title"}),
            mock.patch.object(app, "artifact_title_counts", return_value=Counter({"Random title": 1})),
        ):
            with self.assertRaisesRegex(RuntimeError, "instead of"):
                app.wait_for_named_artifacts(mock.Mock(), {"G9-PHY-C04-Cards"})

    def test_master_verification_rejects_duplicate_titles(self):
        title = "G9-MATH-C03_C04-Diag-Master.pdf"
        with (
            mock.patch.object(app, "send_chat_instruction"),
            mock.patch.object(app, "wait_for_artifacts", return_value={title}),
            mock.patch.object(
                app,
                "artifact_title_counts",
                side_effect=[Counter(), Counter({title: 9})],
            ),
        ):
            with self.assertRaisesRegex(RuntimeError, "expected one new master"):
                app.create_assessment_master(mock.Mock(), "prompt", title, set())

    def test_chat_instruction_is_submitted_once_after_query_is_editable(self):
        page = mock.Mock()
        query = mock.Mock()
        query.is_editable.return_value = True
        responding = mock.Mock()
        page.get_by_role.side_effect = [responding, query, mock.Mock()]
        page.locator.return_value.count.return_value = 0

        app.send_chat_instruction(page, "prompt", "PDF")

        self.assertEqual(query.is_editable.call_count, 2)
        query.fill.assert_called_once_with("prompt")
        responding.wait_for.assert_has_calls([
            mock.call(state="hidden", timeout=mock.ANY),
            mock.call(state="visible", timeout=mock.ANY),
            mock.call(state="hidden", timeout=mock.ANY),
        ])

    def test_chat_instruction_fails_fast_on_notebooklm_refusal(self):
        page = mock.Mock()
        query = mock.Mock()
        query.is_editable.return_value = True
        responding = mock.Mock()
        page.get_by_role.side_effect = [responding, query, mock.Mock()]
        messages = page.locator.return_value
        messages.count.side_effect = [0, 1]
        messages.nth.return_value.inner_text.return_value = "Gemini Notebook can’t answer this question."

        with self.assertRaisesRegex(RuntimeError, "refused"):
            app.send_chat_instruction(page, "prompt", "Assessment")

    def test_artifact_wait_requires_studio_to_have_no_generating_cards(self):
        page = mock.Mock()
        completed = mock.Mock()
        completed.count.side_effect = [1, 1]
        responding = mock.Mock()
        responding.count.return_value = 0
        generating = mock.Mock()
        generating.count.side_effect = [1, 0]
        page.get_by_role.side_effect = [completed, responding, generating]

        with mock.patch.object(app, "completed_artifact_titles", return_value={"artifact"}):
            self.assertEqual(app.wait_for_artifacts(page, 1), {"artifact"})

        page.wait_for_timeout.assert_called_once_with(10_000)


if __name__ == "__main__":
    unittest.main()
