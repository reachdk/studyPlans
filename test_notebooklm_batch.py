import unittest
from unittest import mock
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import json

import notebooklm_batch as app
from pypdf.generic import DecodedStreamObject


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
                self.assertIn("one internally consistent PDF with exactly two parts", prompt)
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

    def test_answer_key_boundary_requires_one_heading_after_the_question_paper(self):
        pages = [
            mock.Mock(extract_text=mock.Mock(return_value="QUESTION PAPER\nQ1")),
            mock.Mock(extract_text=mock.Mock(return_value="PART B — ANSWER KEY AND MARKING SCHEME\nQ1")),
            mock.Mock(extract_text=mock.Mock(return_value="continued answers")),
        ]
        self.assertEqual(app.answer_key_start(mock.Mock(pages=pages)), 1)
        pages.append(mock.Mock(extract_text=mock.Mock(return_value="ANSWER KEY AND MARKING SCHEME")))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            app.answer_key_start(mock.Mock(pages=pages))

    def test_assessment_pdf_is_split_by_copying_whole_pages(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            master = root / "Master.pdf"
            questions = root / "QP.pdf"
            answers = root / "Key.pdf"
            writer = app.PdfWriter()
            for _ in range(3):
                writer.add_blank_page(width=612, height=792)
            with master.open("wb") as output:
                writer.write(output)

            with mock.patch.object(app, "answer_key_start", return_value=2):
                app.split_assessment_pdf(master, questions, answers)

            self.assertEqual(len(app.PdfReader(questions).pages), 2)
            self.assertEqual(len(app.PdfReader(answers).pages), 1)

    def test_assessment_output_names_are_local_not_studio_artifacts(self):
        with TemporaryDirectory() as directory, mock.patch.object(app, "PDF_OUTPUT", Path(directory)):
            questions, answers = app.assessment_output_paths("G9-MATH-C01_C02-Diag-Master.pdf")
            self.assertEqual(questions.name, "G9-MATH-C01_C02-Diag-QP.pdf")
            self.assertEqual(answers.name, "G9-MATH-C01_C02-Diag-Key.pdf")

    def test_experimental_split_names_both_outputs_for_both_masters(self):
        prompt, outputs = app.studio_split_prompt([
            "G9-MATH-C01_C02-Diag-Master.pdf",
            "G9-MATH-C01_C02-Exam-Master.pdf",
        ])
        self.assertEqual(outputs, {
            "G9-MATH-C01_C02-Diag-QP.pdf",
            "G9-MATH-C01_C02-Diag-Key.pdf",
            "G9-MATH-C01_C02-Exam-QP.pdf",
            "G9-MATH-C01_C02-Exam-Key.pdf",
        })
        self.assertIn("Copy the existing pages verbatim", prompt)

    def test_pdf_signature_includes_page_drawing_commands(self):
        with TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in ("one.pdf", "two.pdf")]
            for path, drawing in zip(paths, (b"0 0 m 1 1 l S", b"0 1 m 1 0 l S")):
                writer = app.PdfWriter()
                writer.add_blank_page(width=612, height=792)
                page = writer.pages[-1]
                stream = DecodedStreamObject()
                stream.set_data(drawing)
                stream.indirect_reference = writer._add_object(stream)
                page.replace_contents(stream)
                with path.open("wb") as output:
                    writer.write(output)

            self.assertNotEqual(app.pdf_signature(paths[0]), app.pdf_signature(paths[1]))

    def test_failed_studio_split_keeps_the_local_fallback(self):
        masters = [
            "G9-MATH-C01_C02-Diag-Master.pdf",
            "G9-MATH-C01_C02-Exam-Master.pdf",
        ]
        local_outputs = {
            Path("G9-MATH-C01_C02-Diag-QP.pdf"),
            Path("G9-MATH-C01_C02-Diag-Key.pdf"),
            Path("G9-MATH-C01_C02-Exam-QP.pdf"),
            Path("G9-MATH-C01_C02-Exam-Key.pdf"),
        }
        with (
            mock.patch.object(app, "artifact_title_counts", return_value=Counter(masters)),
            mock.patch.object(app, "send_chat_instruction", side_effect=TimeoutError("no split")),
        ):
            self.assertFalse(app.try_studio_split_assessments(mock.Mock(), masters, local_outputs))

    def test_completed_master_is_downloaded_from_its_studio_menu(self):
        page = mock.Mock()
        card = mock.Mock()
        download = mock.Mock()
        download.save_as.side_effect = lambda path: Path(path).write_bytes(b"%PDF-1.7\n")
        download_info = mock.MagicMock()
        download_info.__enter__.return_value.value = download
        page.expect_download.return_value = download_info
        menu_item = page.get_by_role.return_value

        with TemporaryDirectory() as directory, mock.patch.object(app, "artifact_card", return_value=card):
            destination = Path(directory) / "Master.pdf"
            app.download_artifact(page, "Master.pdf", destination)

        card.get_by_role.assert_called_once_with("button", name="More", exact=True)
        menu_item.click.assert_called_once_with()
        download.save_as.assert_called_once()

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

        app.send_chat_instruction(page, "prompt", "PDF")

        query.is_editable.assert_called_once()
        query.fill.assert_called_once_with("prompt")
        responding.wait_for.assert_has_calls([
            mock.call(state="hidden", timeout=1_800_000),
            mock.call(state="visible", timeout=30_000),
            mock.call(state="hidden", timeout=1_800_000),
        ])

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
