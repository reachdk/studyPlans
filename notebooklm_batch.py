#!/usr/bin/env python3
"""Create a Class 9 NotebookLM study notebook from selected local chapters."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).parent
DOWNLOADS = ROOT / "downloads" / "class-09"
PROFILE = ROOT / ".notebooklm-chrome-profile"
NOTEBOOKLM = "https://notebook.google.com/"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CHROME_DATA = Path.home() / "Library/Application Support/Google/Chrome"
CHROME_PROFILE = "Ghar"

SUBJECT_FOLDERS = {
    "biology": "science",
    "chemistry": "science",
    "english": "english",
    "math": "mathematics",
    "mathematics": "mathematics",
    "maths": "mathematics",
    "physics": "science",
    "science": "science",
    "social science": "social-science",
    "social-science": "social-science",
    "social studies": "social-science",
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

STUDIO_ACTIONS = {
    "answer key": "Create a Report in Studio using the Studio Reports tool. The report must be the Answer Key and Marking Scheme described below.",
    "flashcards": "Create Flashcards in Studio using the Studio Flashcards tool.",
    "mind map": "Create a Mind Map in Studio using the Studio Mind Map tool.",
    "question paper": "Create a Report in Studio using the Studio Reports tool. The report must be the Question Paper described below.",
    "slide deck": "Create a Slide Deck in Studio using the Studio Slide Deck tool.",
}
STUDIO_EXECUTE_NOW = "Do not provide a preview or ask for confirmation. Invoke the Studio tool immediately."


def assessment_document_prompt(subject: str, document: str) -> str:
    common = f"""Create a periodic assessment for CBSE Class 9 {subject}, using only the uploaded syllabus and textbook sources.

Learning levels: recall, understanding, application, and higher-order thinking. Difficulty distribution: approximately 30% easy, 50% moderate, and 20% challenging."""
    if document == "question paper":
        requirements = """Create only the final, print-ready QUESTION PAPER.

- Title and student-information fields
- Time, maximum marks, and clear instructions
- Section-wise questions and marks
- Unambiguous numbering
- Adequate working space where appropriate
- No answers, clues, marking notes, or source citations

Ensure every question is answerable from the supplied sources. Avoid duplicate questions and accidental clues. Check calculations, units, numbering, and mark totals before finalising."""
    elif document == "answer key":
        requirements = """Create only the final, print-ready ANSWER KEY AND MARKING SCHEME corresponding exactly to the Question Paper requested immediately before this message.

- Correct answer for every question
- Stepwise marking for numerical or descriptive answers
- Acceptable alternative answers
- Required keywords or concepts
- Marks awarded at each step
- Total marks verified against the question paper

Check all answers, calculations, units, numbering, and mark totals before finalising. Do not reproduce the question paper as a second document."""
    else:
        raise ValueError(f"unknown assessment document: {document}")
    return f"{common}\n\n{requirements}"


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


def chapter_number(path: Path) -> int | None:
    match = re.match(r"^[a-z]+1(\d{2})--.+\.pdf$", path.name, re.IGNORECASE)
    return int(match.group(1)) if match else None


def resolve_chapters(subject: str, numbers: list[int]) -> list[Path]:
    folder = SUBJECT_FOLDERS.get(subject.casefold())
    if not folder:
        choices = ", ".join(sorted(SUBJECT_FOLDERS))
        raise ValueError(f"unknown subject {subject!r}; choose from: {choices}")

    files = list((DOWNLOADS / folder).rglob("*.pdf"))
    matches = {number: [path for path in files if chapter_number(path) == number] for number in numbers}
    missing = [number for number, paths in matches.items() if not paths]
    ambiguous = {number: paths for number, paths in matches.items() if len(paths) > 1}
    if missing:
        raise ValueError(f"chapters not found for {subject}: {', '.join(map(str, missing))}")
    if ambiguous:
        details = "; ".join(f"{number}: {', '.join(path.name for path in paths)}" for number, paths in ambiguous.items())
        raise ValueError(f"ambiguous chapters: {details}")
    return [matches[number][0] for number in numbers]


def title_from_path(path: Path) -> str:
    return path.stem.split("--", 1)[1].replace("-", " ").title()


def studio_prompt(kind: str, prompt: str) -> str:
    return f"{STUDIO_ACTIONS[kind]} {STUDIO_EXECUTE_NOW}\n\n{prompt}"


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


def artifact_job_count(page) -> int:
    generating = page.get_by_role("button", name=re.compile(r"Generating .+ based on \d+ sources?"))
    completed = page.get_by_role("button", name=re.compile(r".+\d+ sources? ·"))
    return generating.count() + completed.count()


def send_chat_instruction(page, prompt: str, expected_jobs: int, label: str) -> None:
    print(f"Requesting {label}...")
    query = page.get_by_role("textbox", name="Query box")
    query.fill(prompt)
    page.get_by_role("button", name="Submit").last.click()
    responding = page.get_by_role("button", name="Stop generating")
    responding.wait_for(state="visible", timeout=30_000)
    responding.wait_for(state="hidden", timeout=300_000)

    deadline = time.monotonic() + 180
    while time.monotonic() < deadline:
        if artifact_job_count(page) >= expected_jobs:
            print(f"{label} Studio job confirmed ({expected_jobs} total)")
            return
        page.wait_for_timeout(2_000)
    raise TimeoutError(f"chat completed but only {artifact_job_count(page)} of {expected_jobs} Studio jobs appeared")


def wait_for_artifacts(page, expected: int, timeout_minutes: int = 30) -> None:
    completed = page.get_by_role("button", name=re.compile(r".+\d+ sources? ·"))
    responding = page.get_by_role("button", name="Stop generating")
    deadline = time.monotonic() + timeout_minutes * 60
    while time.monotonic() < deadline:
        count = completed.count()
        print(f"Studio artifacts complete: {count}/{expected}", end="\r", flush=True)
        if count >= expected and not responding.count():
            print()
            return
        page.wait_for_timeout(10_000)
    raise TimeoutError(f"only {completed.count()} of {expected} Studio artifacts completed")


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


def run_browser(subject: str, paths: list[Path]) -> str:
    from playwright.sync_api import sync_playwright

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
        notebook_title = f"CBSE Class 9 {subject.title()} — Chapters {', '.join(map(str, numbers))}"
        title_box = page.get_by_role("textbox").first
        title_box.fill(notebook_title)
        title_box.press("Enter")

        presentation_prompt = PRESENTATION.format(subject=subject.title())
        expected_jobs = 0
        for path in paths:
            select_sources(page, [path.name], filenames)
            expected_jobs += 1
            send_chat_instruction(page, studio_prompt("slide deck", presentation_prompt), expected_jobs, path.name)

        select_sources(page, filenames, filenames)
        expected_jobs += 1
        send_chat_instruction(page, studio_prompt("flashcards", FLASHCARDS), expected_jobs, "Flashcards")
        expected_jobs += 1
        send_chat_instruction(page, studio_prompt("mind map", MIND_MAP), expected_jobs, "Mind Map")
        expected_jobs += 1
        send_chat_instruction(
            page,
            studio_prompt("question paper", assessment_document_prompt(subject.title(), "question paper")),
            expected_jobs,
            "Question Paper PDF",
        )
        expected_jobs += 1
        send_chat_instruction(
            page,
            studio_prompt("answer key", assessment_document_prompt(subject.title(), "answer key")),
            expected_jobs,
            "Answer Key PDF",
        )

        expected = len(paths) + 4
        wait_for_artifacts(page, expected)
        url = page.url
        print(f"Notebook ready: {url}")
        input("Press Enter to close the automation browser: ")
        context.close()
        return url


def self_test() -> None:
    assert parse_chapters("4, 6-7") == [4, 6, 7]
    paths = resolve_chapters("physics", [4, 6])
    assert [chapter_number(path) for path in paths] == [4, 6]
    assert title_from_path(paths[0]) == "Describing Motion Around Us"
    print("self-test passed")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0

    subject = input("Subject: ").strip()
    try:
        numbers = parse_chapters(input("Chapters (for example 4,6-7): "))
        paths = resolve_chapters(subject, numbers)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print("\nResolved chapters:")
    for number, path in zip(numbers, paths):
        print(f"  {number:02d} — {title_from_path(path)}")
    if input("\nCreate the NotebookLM notebook? [y/N] ").strip().casefold() != "y":
        print("Cancelled")
        return 0

    run_browser(subject, paths)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
