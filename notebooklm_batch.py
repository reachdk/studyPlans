#!/usr/bin/env python3
"""Create a Class 9 NotebookLM study notebook from selected local chapters."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).parent
DOWNLOADS = ROOT / "downloads" / "class-09"
PROFILE = ROOT / ".notebooklm-chrome-profile"
NOTEBOOKLM = "https://notebook.google.com/"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CHROME_DATA = Path.home() / "Library/Application Support/Google/Chrome"
CHROME_PROFILE = "Ghar"
STREAMS = {
    "PHY": ("science", "Physics"),
    "CHEM": ("science", "Chemistry"),
    "BIO": ("science", "Biology"),
    "HIST": ("social-science", "History"),
    "GEO": ("social-science", "Geography"),
    "ECO": ("social-science", "Economics"),
    "POL": ("social-science", "Political Science"),
    "MATH": ("mathematics", "Mathematics"),
    "ENG": ("english", "English"),
}
STREAM_ALIASES = {
    **{code.casefold(): code for code in STREAMS},
    "physics": "PHY",
    "chemistry": "CHEM",
    "biology": "BIO",
    "history": "HIST",
    "geography": "GEO",
    "economics": "ECO",
    "political science": "POL",
    "pol science": "POL",
    "math": "MATH",
    "maths": "MATH",
    "mathematics": "MATH",
    "english": "ENG",
}
TITLE_STOPWORDS = {"a", "an", "and", "around", "how", "i", "in", "my", "of", "on", "the", "to", "us"}
PDF_KINDS = {
    "Guide", "Pack", "Test-Master", "Test-QP", "Test-Key",
    "Diag-Master", "Diag-QP", "Diag-Key", "Exam-Master", "Exam-QP", "Exam-Key",
}

PRESENTATION = """Act as an experienced CBSE Class 9 {subject} teacher. Create a chapter-wise study guide for the specified assessment scope.

The students are capable learners, but they need clear explanations and strong conceptual understanding. Keep the material engaging without using unnecessary stories or adding content beyond the supplied sources.

For this chapter, include:

1. What the student should be able to understand or do
2. Prerequisite ideas
3. Concepts explained in a logical teaching sequence
4. Simple examples based on the sources
5. Important definitions, formulas, diagrams, reactions, laws, or conventions
6. Important diagrams and visual aids directly from NCERT book
7. Common misconceptions and how to correct them
8. “Why does this happen?” explanations for difficult concepts
9. Worked examples where appropriate
10. Five checkpoint questions distributed through the chapter
11. A concise end-of-chapter summary
12. Practice questions grouped as:
    - Recall
    - Understanding
    - Application
    - Higher-order thinking

Provide answers after the practice section, not immediately below each question. Clearly label any diagram that the student should reproduce in an examination."""

MIND_MAP = """Create a revision mind map for each specified chapter, followed by one combined cross-chapter map.

Use a clear hierarchy:

Chapter
→ major concept
→ sub-concept
→ definition, rule, formula, example, or consequence

Show meaningful relationships using labels such as:
- causes
- results in
- depends on
- differs from
- example of
- measured by

Include:
- Core concepts
- Important terminology
- Formulas, units, reactions, or laws
- Diagram relationships
- Commonly confused ideas
- Tricky points
- Connections between chapters

Keep each node short enough for rapid revision. Do not turn the mind map into paragraphs. After each map, include five self-test questions that require the student to reconstruct important branches from memory."""

FLASHCARDS = """Create active-recall flashcards for the specified CBSE Class 9 chapters.

Use a mixture of:
- Definition → term
- Term → explanation
- Why/how questions
- Formula and unit recall
- Diagram-label questions
- Compare-and-contrast questions
- Application questions
- Misconception-correction questions
- Cloze deletion cards

Rules:
- Test one idea per card
- Make every question unambiguous
- Keep answers concise but complete
- Avoid yes/no questions
- Do not repeat the same fact in multiple forms unless it is especially difficult
- Include enough context for each card to stand alone
- Tag every card with its chapter, topic, and difficulty
- Cite the supporting source section

Organise the output as a table:

Card number | Chapter | Topic | Difficulty | Front | Back | Source

Finish with an appropriately sized “must know” deck containing the highest-priority cards across all selected chapters. Do not cross 60 Cards in a deck."""

ENGLISH_UNIT_GUIDE = """Create one polished downloadable PDF study pack for this selected CBSE Class 9 English Kaveri unit, using only the selected source. Do not return the guide as chat text.

First identify the prose, drama, poetry, vocabulary, grammar, and writing components actually present. Then create only the applicable pages:

- One page for each prose or dramatic text: situation, turning points, character motivation, themes, narrative method, brief evidence references, and common weak interpretations
- One page for each poem: speaker, stanza movement, imagery, tone, sound devices, central idea, and evidence-based interpretation
- One page for each grammar topic: rule, contrasting examples, contextual application, and error correction
- One page for each writing task: purpose, audience, structure, tone, word limit, planning steps, marking checklist, and one concise weak-to-improved example

Keep every component to one readable page. Avoid lengthy plot summaries, dictionary-style vocabulary lists, long quotations, and memorised model answers. Do not invent a text, grammar topic, or writing task absent from the selected source."""

ENGLISH_FLASHCARDS = """Create an active-recall Flashcard deck for the selected CBSE Class 9 English Kaveri units.

- Balance vocabulary in context, literary devices in actual textual context, grammar application, and common-error correction
- At least 70% of cards must require interpretation, sentence completion, correction, or application
- Test vocabulary through meaning in context, collocation, or usage rather than isolated synonyms
- Test literary devices through their effect in a brief source-based example rather than definition recall
- Avoid plot-recall cards, duplicates, yes/no questions, and memorised model answers
- Keep every answer concise, complete, and independently understandable"""

MATH_REVISION_GUIDE = """Create one polished downloadable PDF revision guide for the selected CBSE Class 9 Mathematics chapters, using only the selected sources.

Give each chapter one readable main section containing:

- The big idea in plain language
- Essential concepts, definitions, notation, formulas, and conditions
- One central diagram or proof skeleton where genuinely useful
- One annotated worked example explaining the choice of method
- One common mistake and its correction
- Three unanswered self-check questions covering explanation, solving, and unfamiliar application

Finish with one consolidated answer section. Use precise NCERT terminology and mathematical notation. Exclude historical trivia and omit low-value detail rather than crowding the pages."""

MATH_FLASHCARDS = """Create an active-recall flashcard deck for the selected CBSE Class 9 Mathematics chapters.

- Prioritise concepts, notation, method selection, short calculations, reasoning, and misconception correction.
- At least 70% of cards should require explanation, solving, or error diagnosis.
- Test one idea per card with a concise, unambiguous answer.
- Avoid duplicates, yes/no questions, historical trivia, and facts already obvious from a displayed formula."""

MATH_MIND_MAP = """Create a revision Mind Map for the selected CBSE Class 9 Mathematics chapters.

Cover:

- Core concepts and definitions
- Notation and formulas with their conditions
- Method selection
- Important diagram relationships
- Common mistakes and commonly confused ideas

Use labelled relationships such as depends on, results in, differs from, and example of. Keep every node short and exclude names, dates, and historical trivia."""

MATH_ASSESSMENT_BLUEPRINTS = {
    20: (
        (("A", "Multiple-choice", 4, 1), ("B", "Short-answer", 4, 2), ("C", "Competency/long-answer", 2, 4)),
        (11, 5, 4),
    ),
    40: (
        (("A", "Multiple-choice", 8, 1), ("B", "Very-short-answer", 4, 2), ("C", "Short-answer", 4, 3), ("D", "Long-answer", 2, 4), ("E", "Case/competency", 1, 4)),
        (21, 10, 9),
    ),
    80: (
        (("A", "Multiple-choice", 20, 1), ("B", "Very-short-answer", 5, 2), ("C", "Short-answer", 6, 3), ("D", "Long-answer", 4, 5), ("E", "Case-based", 3, 4)),
        (43, 19, 18),
    ),
}


def balanced_flashcard_prompt(prompt: str, chapter_count: int) -> str:
    total = min(60, 10 * chapter_count + 10)
    minimum, extra = divmod(total, chapter_count)
    maximum = minimum + bool(extra)
    allocation = str(minimum) if minimum == maximum else f"{minimum} or {maximum}"
    return f"{prompt}\n\nCreate exactly {total} cards. Balance coverage so every selected chapter receives {allocation} cards."


def balanced_mind_map_prompt(prompt: str, chapter_count: int) -> str:
    single_chapter = "Do not create a redundant cross-chapter map." if chapter_count == 1 else "Add one final branch containing only the most useful cross-chapter connections."
    return f"""{prompt}

Balance coverage across all {chapter_count} selected chapters. Give every chapter one top-level branch with comparable detail and no more than 12 leaf nodes; do not let one chapter dominate. {single_chapter}"""

STUDIO_ACTIONS = {
    "flashcards": "Create Flashcards in Studio using the Studio Flashcards tool.",
    "mind map": "Create a Mind Map in Studio using the Studio Mind Map tool.",
    "pdf": "Create one PDF from the instructions below and save it in Studio.",
    "quiz": "Create a Quiz in Studio using the Studio Quiz tool.",
    "slide deck": "Create a Slide Deck in Studio using the Studio Slide Deck tool.",
}
STUDIO_EXECUTE_NOW = "Do not provide a preview or ask for confirmation. Start immediately."


def english_quiz_prompt(chapter_count: int) -> str:
    questions = min(30, 10 + 5 * chapter_count)
    return f"""Create exactly {questions} questions in one mixed CBSE Class 9 English Quiz covering all {chapter_count} selected Kaveri units.

- Balance coverage across the selected units and across textbook extracts, inference, evidence selection, vocabulary in context, grammar application, error correction, and answer improvement
- Include one short, newly written age-appropriate unseen passage; do not copy the reading passage from a selected literary text
- Make at least 70% of questions application, interpretation, or improvement tasks
- Do not repeat factual or definition recall already suited to Flashcards
- Give concise explanations after answers, including why a tempting incorrect answer fails"""


def english_assessment_prompt(paper: str, chapter_count: int) -> str:
    duration, marks = assessment_scheme(chapter_count)
    reading = marks // 4
    writing_grammar = marks // 4
    literature = marks // 2
    common = f"""Use only the selected sources to create a CBSE Class 9 English Language and Literature assessment, except for one newly written age-appropriate unseen passage.

Duration: {duration} minutes
Maximum marks: {marks}

Use this section weighting:
- Reading Comprehension: {reading} marks
- Writing Skills and Grammar: {writing_grammar} marks
- Language through Literature: {literature} marks

Balance Literature marks across the selected units and restrict grammar, vocabulary, and writing formats to those present in the sources.

Produce exactly two parts.

PART A — QUESTION PAPER

- Include student-information fields, instructions, section headings, and marks
- Number questions sequentially and provide appropriate writing space
- Include no answers, clues, rubrics, or source citations

Start PART B on a new page with the exact heading ANSWER KEY AND MARKING SCHEME.

PART B — ANSWER KEY AND MARKING SCHEME

- Answer exactly the questions in Part A using the same numbering
- Give precise answers for Reading and Grammar
- Give Literature value points while accepting interpretations supported by evidence
- Use an analytic Writing rubric covering content, organisation, format, tone, expression, and accuracy

Before finalizing the output, verify section totals, unit coverage, numbering, and the correspondence between every question and marking point."""
    if paper == "diagnostic":
        requirements = """Use the internal document heading PAPER 1 — ENGLISH SKILL DIAGNOSTIC.

Keep Reading, Writing, Grammar, and Literature results distinguishable, and identify the skill and revision need for each question."""
    elif paper == "cumulative":
        requirements = """Use the internal document heading PAPER 2 — CUMULATIVE TIMED ENGLISH EXAMINATION.

Use examination-style ordering and test inference, evidence-based interpretation, contextual grammar, and independent writing."""
    else:
        raise ValueError(f"unknown English paper: {paper}")
    return f"{common}\n\n{requirements}"


def english_jobs(chapter_count: int) -> tuple[tuple[str, str, str], ...]:
    return (
        ("flashcards", balanced_flashcard_prompt(ENGLISH_FLASHCARDS, chapter_count), "English Flashcards"),
        ("quiz", english_quiz_prompt(chapter_count), "English Quiz"),
        ("pdf", english_assessment_prompt("diagnostic", chapter_count), "English Diagnostic Master PDF"),
        ("pdf", english_assessment_prompt("cumulative", chapter_count), "English Cumulative Master PDF"),
    )


def combined_assessment_prompt(subject: str, chapter_count: int) -> str:
    duration, marks = assessment_scheme(chapter_count)
    return f"""Use only the selected sources to create a periodic assessment for CBSE Class 9 {subject}.

Duration: {duration} minutes
Maximum marks: {marks}

Produce exactly two internally consistent parts. Balance coverage and marks as evenly as practical across all selected chapters. Use recall, understanding, application, competency, and higher-order questions with approximately 30% easy, 50% moderate, and 20% challenging marks.

PART A — QUESTION PAPER

- Include a title, student-information fields, time, maximum marks, instructions, section-wise questions, marks, and adequate working space
- Number questions once and sequentially with no gaps, duplicates, bracketed IDs, or secondary numbering
- Keep answers, clues, marking notes, skill labels, and source citations out of Part A
- Ensure every question is answerable from the selected sources
- Ensure the questions total exactly {marks} marks and are appropriate for {duration} minutes

Start PART B on a new page with the exact heading ANSWER KEY AND MARKING SCHEME.

PART B — ANSWER KEY AND MARKING SCHEME

- Answer exactly the questions in Part A using the same question numbers and wording
- Give stepwise marking, acceptable alternatives, required concepts or keywords, and marks awarded at each step
- Do not introduce, omit, reorder, or rewrite questions

Before finalizing the output, silently verify chapter coverage, calculations, units, numbering, and mark totals. Do not print this verification ledger in Part A."""


def assessment_scheme(chapter_count: int) -> tuple[int, int]:
    if chapter_count < 1:
        raise ValueError("an assessment requires at least one chapter")
    if chapter_count <= 2:
        return 45, 20
    if chapter_count <= 5:
        return 90, 40
    return 180, 80


def mathematics_assessment_prompt(paper: str, chapter_count: int) -> str:
    duration, marks = assessment_scheme(chapter_count)
    sections, cognitive_marks = MATH_ASSESSMENT_BLUEPRINTS[marks]
    section_plan = "\n".join(
        f"- Section {name}: {count} {kind} questions × {each} mark{'s' if each != 1 else ''} = {count * each} marks"
        for name, kind, count, each in sections
    )
    remembering, applying, higher_order = cognitive_marks
    question_count = sum(count for _, _, count, _ in sections)
    common = f"""Use only the selected sources to create a CBSE Class 9 Mathematics assessment.

Duration: {duration} minutes
Maximum marks: {marks}

Use exactly this structure:
{section_plan}

Across the paper allocate {remembering} marks to Remembering and Understanding, {applying} marks to Applying, and {higher_order} marks to higher-order reasoning. Balance the selected chapters and challenge students through method selection, application, and error analysis rather than difficult arithmetic or historical trivia.

Produce exactly two parts.

PART A — QUESTION PAPER

- Number the {question_count} questions sequentially as Q1 through Q{question_count}
- Show marks clearly and provide suitable working space
- Use proper mathematical notation and labelled diagrams where needed
- Include no answers, clues, or marking notes

Start PART B on a new page with the exact heading ANSWER KEY AND MARKING SCHEME.

PART B — ANSWER KEY AND MARKING SCHEME

- Answer exactly the questions in Part A using the same numbering
- Give verified working and mark allocation
- Accept alternative valid methods and award reasoning marks where appropriate

Before finalizing the output, verify the question count, section totals, cognitive totals, calculations, and correspondence between the paper and marking scheme."""
    if paper == "diagnostic":
        requirements = """Use the internal document heading QUESTION PAPER 1 — CHAPTER-WISE DIAGNOSTIC.

Cover every selected chapter, isolate misconceptions where practical, and identify the chapter, skill, and revision need for each answer."""
    elif paper == "cumulative":
        requirements = """Use the internal document heading QUESTION PAPER 2 — CUMULATIVE TIMED EXAMINATION.

Mix the selected chapters and test method selection, multi-step reasoning, mathematical communication, and unfamiliar application."""
    else:
        raise ValueError(f"unknown Mathematics paper: {paper}")
    return f"{common}\n\n{requirements}"


def mathematics_jobs(chapter_count: int) -> tuple[tuple[str, str, str], ...]:
    return (
        ("pdf", MATH_REVISION_GUIDE, "Mathematics Revision Guide PDF"),
        ("flashcards", balanced_flashcard_prompt(MATH_FLASHCARDS, chapter_count), "Flashcards"),
        ("mind map", balanced_mind_map_prompt(MATH_MIND_MAP, chapter_count), "Mind Map"),
        ("pdf", mathematics_assessment_prompt("diagnostic", chapter_count), "Diagnostic Paper and Marking Scheme PDF"),
        ("pdf", mathematics_assessment_prompt("cumulative", chapter_count), "Cumulative Paper and Marking Scheme PDF"),
    )


def parse_chapters(value: str) -> list[int]:
    chapters: set[int] = set()
    for part in value.replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            start, end = map(int, part.split("-", 1))
            if start > end:
                raise ValueError(f"invalid chapter range: {part}")
            chapters.update(range(start, end + 1))
        else:
            chapters.add(int(part))
    if not chapters or min(chapters) < 1:
        raise ValueError("provide one or more positive chapter numbers")
    return sorted(chapters)


def stream_details(value: str) -> tuple[str, str, str]:
    code = STREAM_ALIASES.get(value.strip().casefold())
    if not code:
        choices = "/".join(STREAMS)
        raise ValueError(f"unknown stream {value!r}; use one of: {choices}")
    folder, display_name = STREAMS[code]
    return code, folder, display_name


def chapter_number(path: Path) -> int | None:
    match = re.match(r"^[a-z]+1(\d{2})--.+\.pdf$", path.name, re.IGNORECASE)
    return int(match.group(1)) if match else None


def resolve_chapters(stream: str, numbers: list[int]) -> list[Path]:
    _, folder, _ = stream_details(stream)

    files = list((DOWNLOADS / folder).rglob("*.pdf"))
    matches = {number: [path for path in files if chapter_number(path) == number] for number in numbers}
    missing = [number for number, paths in matches.items() if not paths]
    ambiguous = {number: paths for number, paths in matches.items() if len(paths) > 1}
    if missing:
        raise ValueError(f"chapters not found for {stream}: {', '.join(map(str, missing))}")
    if ambiguous:
        details = "; ".join(f"{number}: {', '.join(path.name for path in paths)}" for number, paths in ambiguous.items())
        raise ValueError(f"ambiguous chapters: {details}")
    return [matches[number][0] for number in numbers]


def title_from_path(path: Path) -> str:
    return path.stem.split("--", 1)[1].replace("-", " ").title()


def scope_token(stream_code: str, numbers: list[int]) -> str:
    prefix = "U" if stream_code == "ENG" else "C"
    return "_".join(f"{prefix}{number:02d}" for number in numbers)


def short_title(path: Path) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title_from_path(path))
    meaningful = [word for word in words if word.casefold() not in TITLE_STOPWORDS]
    return "-".join((meaningful or words)[:3])


def artifact_title(stream_code: str, numbers: list[int], kind: str, path: Path | None = None) -> str:
    parts = ["G9", stream_code, scope_token(stream_code, numbers)]
    if path:
        parts.append(short_title(path))
    title = "-".join((*parts, kind))
    return f"{title}.pdf" if kind in PDF_KINDS else title


def notebook_title(stream_code: str, numbers: list[int]) -> str:
    return f"G9-{stream_code}-{scope_token(stream_code, numbers)}"


def studio_prompt(kind: str, prompt: str, title: str) -> str:
    return f'{STUDIO_ACTIONS[kind]} Title the Studio artifact exactly "{title}". {STUDIO_EXECUTE_NOW}\n\n{prompt}'


def select_sources(page, selected: list[str], all_filenames: list[str]) -> None:
    wanted = set(selected)
    for filename in all_filenames:
        checkbox = page.get_by_role("checkbox", name=filename, exact=True)
        expected = filename in wanted
        if checkbox.is_checked() != expected:
            checkbox.locator("xpath=ancestor::label").click()
            for _ in range(10):
                if checkbox.is_checked() == expected:
                    break
                page.wait_for_timeout(100)
            else:
                raise RuntimeError(f"could not {'select' if expected else 'deselect'} source {filename}")


def completed_artifact_titles(page) -> set[str]:
    completed = page.get_by_role("button", name=re.compile(r".+\d+ sources? ·"))
    return {
        completed.nth(index)
        .locator("xpath=ancestor::artifact-library-item")
        .locator(".artifact-title")
        .inner_text()
        .strip()
        for index in range(completed.count())
    }


def artifact_title_counts(page) -> Counter[str]:
    return Counter(title.strip() for title in page.locator(".artifact-title").all_inner_texts())


def artifact_card(page, title: str):
    titles = page.locator(".artifact-title")
    matches = [index for index in range(titles.count()) if titles.nth(index).inner_text().strip() == title]
    if len(matches) != 1:
        raise RuntimeError(f"expected one completed Studio artifact named {title!r}, found {len(matches)}")
    return titles.nth(matches[0]).locator("xpath=ancestor::artifact-library-item")


def assessment_output_titles(master_title: str) -> tuple[str, str]:
    if not master_title.endswith("-Master.pdf"):
        raise ValueError(f"assessment master title must end with '-Master.pdf': {master_title!r}")
    stem = master_title.removesuffix("-Master.pdf")
    return f"{stem}-QP.pdf", f"{stem}-Key.pdf"


def assessment_master_prompt(prompt: str, title: str) -> str:
    if not title.endswith("-Master.pdf"):
        raise ValueError(f"assessment master title must end with '-Master.pdf': {title!r}")
    return (
        "Generate a comprehensive Assessment PDF Document and save the PDF in Studio. "
        f'Title the document exactly "{title.removesuffix(".pdf")}".\n\n{prompt}'
    )


def studio_split_prompt(master: str) -> tuple[str, set[str]]:
    question_paper, answer_key = assessment_output_titles(master)
    prompt = f"""Using the completed Assessment Document "{master}" in Studio, create these two PDF files and save them in Studio:

- "{question_paper}" containing only PART A — QUESTION PAPER
- "{answer_key}" containing only PART B — ANSWER KEY AND MARKING SCHEME

Preserve the existing content, mathematical notation, diagrams, numbering, marks, and layout."""
    return prompt, {question_paper, answer_key}


def delete_artifact(page, title: str) -> None:
    card = artifact_card(page, title)
    card.get_by_role("button", name="More", exact=True).click()
    page.get_by_role("menuitem", name="Delete", exact=True).click()

    dialog = page.get_by_role("dialog")
    for _ in range(30):
        if dialog.count() and dialog.is_visible():
            page.evaluate("""() => [...document.querySelectorAll('[role="dialog"] button')]
                .find(button => button.textContent.trim() === 'Delete')?.click()""")
            break
        if artifact_title_counts(page)[title] == 0:
            break
        page.wait_for_timeout(100)

    for _ in range(300):
        if artifact_title_counts(page)[title] == 0:
            break
        page.wait_for_timeout(100)
    else:
        raise TimeoutError(f"{title}: Studio artifact was not deleted")

    page.reload(wait_until="domcontentloaded")
    page.locator("artifact-library-item").first.wait_for(timeout=30_000)
    if artifact_title_counts(page)[title]:
        raise RuntimeError(f"{title}: Studio artifact reappeared after reload")


def split_assessment(page, master: str, artifacts: set[str]) -> set[str]:
    prompt, expected = studio_split_prompt(master)
    before = artifact_title_counts(page)
    if before[master] != 1:
        raise RuntimeError(f"expected one master named {master!r}, found {before[master]}")
    existing = sorted(expected & before.keys())
    if existing:
        raise RuntimeError(f"Studio split outputs already exist: {existing}")

    send_chat_instruction(page, prompt, f"Split {master}")
    completed = wait_for_artifacts(page, sum(before.values()) + len(expected))
    created = artifact_title_counts(page) - before
    if created != Counter(expected):
        raise RuntimeError(f"{master}: Studio created {dict(created)} instead of {sorted(expected)}")

    delete_artifact(page, master)
    return (completed - {master}) | expected


def send_chat_instruction(page, prompt: str, label: str) -> None:
    print(f"Requesting {label}...")
    deadline = time.monotonic() + 1_800
    responding = page.get_by_role("button", name="Stop generating")
    responding.wait_for(state="hidden", timeout=max(1, int((deadline - time.monotonic()) * 1_000)))
    query = page.get_by_role("textbox", name="Query box")
    while not query.is_editable():
        if time.monotonic() >= deadline:
            raise TimeoutError(f"{label}: query box did not become editable")
        page.wait_for_timeout(1_000)
    messages = page.locator(".chat-message-pair")
    message_count = messages.count()
    query.fill(prompt)
    page.get_by_role("button", name="Submit").last.click()
    responding.wait_for(state="visible", timeout=min(30_000, max(1, int((deadline - time.monotonic()) * 1_000))))
    responding.wait_for(state="hidden", timeout=max(1, int((deadline - time.monotonic()) * 1_000)))
    while not query.is_editable():
        if time.monotonic() >= deadline:
            raise TimeoutError(f"{label}: query box did not become editable after generation")
        page.wait_for_timeout(1_000)
    replies = "\n".join(messages.nth(index).inner_text() for index in range(message_count, messages.count()))
    if "Gemini Notebook can’t answer this question." in replies or "Gemini Notebook can't answer this question." in replies:
        raise RuntimeError(f"{label}: NotebookLM refused the request")
    print(f"{label} request accepted")


def wait_for_artifacts(page, expected: int, timeout_minutes: int = 30) -> set[str]:
    completed = page.get_by_role("button", name=re.compile(r".+\d+ sources? ·"))
    responding = page.get_by_role("button", name="Stop generating")
    generating = page.get_by_role("button", name=re.compile(r"Generating .+ based on \d+ sources?"))
    deadline = time.monotonic() + timeout_minutes * 60
    while time.monotonic() < deadline:
        count = completed.count()
        active = generating.count()
        print(f"Studio artifacts complete: {count}/{expected}; generating: {active}", end="\r", flush=True)
        if count >= expected and not responding.count() and not active:
            print()
            return completed_artifact_titles(page)
        page.wait_for_timeout(10_000)
    raise TimeoutError(f"only {completed.count()} of {expected} Studio artifacts completed")


def wait_for_named_artifacts(page, expected: set[str]) -> set[str]:
    completed = wait_for_artifacts(page, len(expected))
    counts = artifact_title_counts(page)
    if counts != Counter(expected):
        raise RuntimeError(f"Studio created {dict(counts)} instead of one each of {sorted(expected)}")
    return completed


def create_assessment_master(
    page, prompt: str, title: str, artifacts: set[str]
) -> set[str]:
    before = artifact_title_counts(page)
    if before[title]:
        raise RuntimeError(f"refusing to recreate existing master {title!r}")
    send_chat_instruction(page, assessment_master_prompt(prompt, title), title)
    completed = wait_for_artifacts(page, len(artifacts) + 1)
    created = artifact_title_counts(page) - before
    if created != Counter({title: 1}):
        raise RuntimeError(f"{title}: expected one new master, found {dict(created)}")
    return completed


def profile_name(root: Path, display_name: str | None = None) -> str:
    profiles = json.loads((root / "Local State").read_text())["profile"]
    if display_name is None:
        return profiles.get("last_used", "Default")
    matches = [directory for directory, details in profiles["info_cache"].items() if details["name"] == display_name]
    if len(matches) != 1:
        raise RuntimeError(f"expected one Chrome profile named {display_name!r}, found {len(matches)}")
    return matches[0]


def import_chrome_profile(name: str) -> str:
    for _ in range(20):
        if subprocess.run(["pgrep", "-x", "Google Chrome"], capture_output=True).returncode != 0:
            break
        time.sleep(0.5)
    else:
        raise RuntimeError("Google Chrome is still running; quit it completely with Command-Q and try again")
    source = CHROME_DATA / name
    if not source.is_dir():
        raise RuntimeError(f"Chrome profile was not found: {source}")
    importing = PROFILE.with_name(f"{PROFILE.name}.importing")
    shutil.rmtree(importing, ignore_errors=True)
    importing.mkdir()
    shutil.copy2(CHROME_DATA / "Local State", importing / "Local State")
    shutil.copytree(
        source,
        importing / name,
        ignore=shutil.ignore_patterns("Cache", "Code Cache", "Extensions", "GPUCache", "Service Worker"),
    )
    (importing / ".import-complete").touch()
    shutil.rmtree(PROFILE, ignore_errors=True)
    importing.replace(PROFILE)
    return name


def refresh_chrome_profile() -> str:
    if not CHROME.exists():
        raise RuntimeError(f"Google Chrome was not found at {CHROME}")
    name = profile_name(CHROME_DATA, CHROME_PROFILE)
    subprocess.Popen(
        [str(CHROME), f"--profile-directory={name}", NOTEBOOKLM],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    input(f"Confirm NotebookLM opens in the Chrome profile {CHROME_PROFILE!r}, quit Chrome with Command-Q, then press Enter: ")
    return import_chrome_profile(name)


def launch_context(playwright, profile_name: str):
    return playwright.chromium.launch_persistent_context(
        PROFILE,
        executable_path=str(CHROME),
        headless=False,
        no_viewport=True,
        args=[f"--profile-directory={profile_name}"],
        ignore_default_args=["--password-store=basic", "--use-mock-keychain"],
    )


def run_browser(stream: str, paths: list[Path], try_studio_split: bool = False) -> str:
    stream_code, _, display_name = stream_details(stream)
    is_mathematics = stream_code == "MATH"
    from playwright.sync_api import expect, sync_playwright

    name = profile_name(PROFILE, CHROME_PROFILE) if (PROFILE / ".import-complete").exists() else refresh_chrome_profile()
    with sync_playwright() as playwright:
        context = launch_context(playwright, name)
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(NOTEBOOKLM)
        if "accounts.google.com" in page.url:
            context.close()
            context = launch_context(playwright, refresh_chrome_profile())
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(NOTEBOOKLM)
        if "notebook.google.com" not in page.url:
            raise RuntimeError("NotebookLM sign-in was not completed")

        page.get_by_role("button", name="Create new notebook").click()
        page.wait_for_url(re.compile(r".*/notebook/.*"))
        page.get_by_role("button", name="add a source", exact=True).click()
        with page.expect_file_chooser() as chooser:
            page.get_by_role("button", name="Upload files").click()
        chooser.value.set_files([str(path.resolve()) for path in paths])

        filenames = [path.name for path in paths]
        for filename in filenames:
            page.get_by_role("checkbox", name=filename, exact=True).wait_for(timeout=180_000)

        numbers = [chapter_number(path) for path in paths]
        title = notebook_title(stream_code, numbers)
        title_box = page.get_by_role("textbox").first
        title_box.fill(title)
        title_box.press("Enter")
        expect(title_box).to_have_value(title, timeout=30_000)

        expected_titles: set[str] = set()
        if is_mathematics:
            select_sources(page, filenames, filenames)
            jobs = mathematics_jobs(len(paths))
            for (kind, prompt, _), artifact_kind in zip(jobs[:3], ("Guide", "Cards", "Map")):
                artifact = artifact_title(stream_code, numbers, artifact_kind)
                expected_titles.add(artifact)
                send_chat_instruction(page, studio_prompt(kind, prompt, artifact), artifact)
            artifacts = wait_for_named_artifacts(page, expected_titles)
            masters = [
                artifact_title(stream_code, numbers, "Diag-Master"),
                artifact_title(stream_code, numbers, "Exam-Master"),
            ]
            for (_, prompt, _), master in zip(jobs[3:], masters):
                artifacts = create_assessment_master(page, prompt, master, artifacts)
                if try_studio_split:
                    artifacts = split_assessment(page, master, artifacts)
        elif stream_code == "ENG":
            for path in paths:
                select_sources(page, [path.name], filenames)
                artifact = artifact_title(stream_code, [chapter_number(path)], "Pack", path)
                expected_titles.add(artifact)
                send_chat_instruction(
                    page,
                    studio_prompt("pdf", ENGLISH_UNIT_GUIDE, artifact),
                    artifact,
                )

            select_sources(page, filenames, filenames)
            jobs = english_jobs(len(paths))
            for (kind, prompt, _), artifact_kind in zip(jobs[:2], ("Cards", "Quiz")):
                artifact = artifact_title(stream_code, numbers, artifact_kind)
                expected_titles.add(artifact)
                send_chat_instruction(page, studio_prompt(kind, prompt, artifact), artifact)
            artifacts = wait_for_named_artifacts(page, expected_titles)
            masters = [
                artifact_title(stream_code, numbers, "Diag-Master"),
                artifact_title(stream_code, numbers, "Exam-Master"),
            ]
            for (_, prompt, _), master in zip(jobs[2:], masters):
                artifacts = create_assessment_master(page, prompt, master, artifacts)
                if try_studio_split:
                    artifacts = split_assessment(page, master, artifacts)
        else:
            presentation_prompt = PRESENTATION.format(subject=display_name)
            for path in paths:
                select_sources(page, [path.name], filenames)
                artifact = artifact_title(stream_code, [chapter_number(path)], "Slides", path)
                expected_titles.add(artifact)
                send_chat_instruction(
                    page, studio_prompt("slide deck", presentation_prompt, artifact), artifact
                )

            select_sources(page, filenames, filenames)
            cards = artifact_title(stream_code, numbers, "Cards")
            expected_titles.add(cards)
            send_chat_instruction(
                page,
                studio_prompt("flashcards", balanced_flashcard_prompt(FLASHCARDS, len(paths)), cards),
                cards,
            )
            mind_map = artifact_title(stream_code, numbers, "Map")
            expected_titles.add(mind_map)
            send_chat_instruction(
                page,
                studio_prompt("mind map", balanced_mind_map_prompt(MIND_MAP, len(paths)), mind_map),
                mind_map,
            )
            artifacts = wait_for_named_artifacts(page, expected_titles)
            master = artifact_title(stream_code, numbers, "Test-Master")
            artifacts = create_assessment_master(
                page,
                combined_assessment_prompt(display_name, len(paths)),
                master,
                artifacts,
            )
            if try_studio_split:
                artifacts = split_assessment(page, master, artifacts)

        url = page.url
        print(f"Notebook ready: {url}")
        input("Press Enter to close the automation browser: ")
        context.close()
        return url


def self_test() -> None:
    assert parse_chapters("4, 6-7") == [4, 6, 7]
    paths = resolve_chapters("PHY", [4, 6])
    assert [chapter_number(path) for path in paths] == [4, 6]
    assert title_from_path(paths[0]) == "Describing Motion Around Us"
    assert notebook_title("PHY", [4, 6]) == "G9-PHY-C04_C06"
    print("self-test passed")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if sys.argv[1:] not in ([], ["--split"]):
        print("Usage: notebooklm_batch.py [--self-test|--split]", file=sys.stderr)
        return 2
    try_studio_split = sys.argv[1:] == ["--split"]

    stream = input("Stream code (PHY/CHEM/BIO/HIST/GEO/ECO/POL/MATH/ENG): ").strip()
    try:
        numbers = parse_chapters(input("Chapters (for example 4,6-7): "))
        stream_code, _, display_name = stream_details(stream)
        paths = resolve_chapters(stream_code, numbers)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(f"\nResolved {stream_code} ({display_name}) chapters:")
    for number, path in zip(numbers, paths):
        print(f"  {number:02d} — {title_from_path(path)}")

    if input("\nCreate the NotebookLM notebook? [y/N] ").strip().casefold() != "y":
        print("Cancelled")
        return 0

    run_browser(stream_code, paths, try_studio_split)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
