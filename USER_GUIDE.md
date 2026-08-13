# User Guide

## What the automation does

For a Science or Social Science run containing `N` chapters, the program finishes with `N + 3` Studio artifacts and two local assessment PDFs:

1. `N` chapter presentations, each using only its corresponding chapter source
2. One Flashcard deck using all selected chapters
3. One Mind Map using all selected chapters
4. One assessment master PDF using all selected chapters

The master is downloaded and split locally by copying whole PDF pages. The Question Paper and Answer Key are saved under `output/pdf/`; the master remains in Studio.

For an English run containing `N` selected Kaveri units, the program finishes with `N + 4` Studio artifacts and four local assessment PDFs:

1. `N` Chapter Pack PDFs, each using only its corresponding unit source
2. One balanced Flashcard deck using all selected units
3. One mixed Quiz using all selected units
4. One English Skill Diagnostic master PDF
5. One Cumulative Timed English master PDF

English does not create Slide Decks or a Mind Map.

For Mathematics, every run finishes with five Studio artifacts and four local assessment PDFs regardless of the chapter count:

1. One combined chapter Revision Guide PDF
2. One combined Flashcard deck
3. One combined Mind Map
4. One chapter-wise Diagnostic master PDF
5. One Cumulative Timed master PDF

Mathematics does not create Slide Decks or a separate mixed quiz.

The program leaves artifact generation to NotebookLM and waits for every artifact, the assessment chat response, and all active Studio generation to finish. It then downloads each assessment master, finds the `ANSWER KEY AND MARKING SCHEME` page, copies the two page ranges into local PDFs, and verifies their page counts.

## Before the first run

Open a terminal in this repository and create the isolated Python environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Google Chrome must be installed. The program drives an isolated Chrome instance directly and does not require a separately downloaded Playwright browser.

If the `downloads/class-09` chapter folders are missing or incomplete, populate them with:

```bash
.venv/bin/python download_ncert.py
```

This only downloads missing or invalid chapter PDFs; valid existing files are preserved.

## Starting a run

```bash
.venv/bin/python notebooklm_batch.py
```

The program asks for three decisions before changing NotebookLM:

1. Stream code
2. Chapter numbers
3. Confirmation of the resolved chapter list

For English, Science, Social Science, and Mathematics, duration and marks are not configurable. They scale from the chapter count: 1–2 chapters use 45 minutes/20 marks, 3–5 use 90 minutes/40 marks, and larger scopes use the full 180 minutes/80 marks. English preserves its 25% Reading, 25% Writing and Grammar, and 50% Literature weighting; Mathematics retains its CBSE cognitive-weighting split.

Nothing is uploaded if the confirmation is anything other than `y`.

### Stream input

Enter one stream code. Codes and source folders are:

| Code | Stream | Chapter folder |
|---|---|---|
| `PHY` | Physics | `downloads/class-09/science` |
| `CHEM` | Chemistry | `downloads/class-09/science` |
| `BIO` | Biology | `downloads/class-09/science` |
| `HIST` | History | `downloads/class-09/social-science` |
| `GEO` | Geography | `downloads/class-09/social-science` |
| `ECO` | Economics | `downloads/class-09/social-science` |
| `POL` | Political Science | `downloads/class-09/social-science` |
| `MATH` | Mathematics | `downloads/class-09/mathematics` |
| `ENG` | English | `downloads/class-09/english` |

Codes are case-insensitive; long stream names remain accepted for convenience. Generic `Science`, `Social Science`, and `Social Studies` runs are rejected because every run must belong to one stream. The program trusts the selected chapter numbers; it does not decide whether a chapter belongs to the requested stream.

### Chapter input

Enter individual chapter numbers, comma-separated values, ranges, or a combination:

```text
4
4,6,7
4-7
2,4-6,9
```

Duplicates are removed and chapters are processed in numerical order.

The chapter number is read from the final two digits of the filename prefix. For example:

```text
iesc104--describing-motion-around-us.pdf  → chapter 4
iesc106--how-forces-affect-motion.pdf     → chapter 6
```

The program stops before opening Chrome when a chapter is missing. If multiple books under one subject contain the same chapter number, it reports the ambiguity instead of guessing.

## First Google sign-in

The automation uses a dedicated Chrome profile stored at:

```text
.notebooklm-chrome-profile/
```

On the first run:

1. NotebookLM opens in the Chrome profile named `Ghar`.
2. Sign in manually if needed and confirm that NotebookLM opens in the correct account.
3. Quit Chrome completely with `Command-Q`; closing only the window is insufficient.
4. Return to the terminal and press Enter. The program copies the `Ghar` Chrome profile into `.notebooklm-chrome-profile` and reopens it for automation. Your normal Chrome profile is not modified.

The program never asks for or reads the password. It copies the local Chrome profile, including its authenticated session, into `.notebooklm-chrome-profile`, so later runs should not require another sign-in.

Do not commit, copy, or share `.notebooklm-chrome-profile`; it contains browser session data and is excluded by `.gitignore`.

When using another computer or Chrome profile, change the `CHROME_PROFILE` constant near the top of `notebooklm_batch.py` from `Ghar` to the display name shown in Chrome's profile menu. Use the visible profile name, not an internal directory such as `Default` or `Profile 1`.

## What happens after confirmation

For Science and Social Science, the browser workflow is:

1. Create a new NotebookLM notebook.
2. Upload the resolved PDF chapters.
3. Wait until every source finishes processing.
4. Rename the notebook to `G9-<STREAM>-<SCOPE>`, such as `G9-PHY-C04_C06`.
5. Select one chapter at a time and ask NotebookLM chat to create its Slide Deck with the Studio tool.
6. Select every chapter and ask chat to create the combined Flashcard deck with the Studio tool.
7. Ask chat to create the combined Mind Map with the Studio tool.
8. Create one combined assessment master and wait for it to finish.
9. Download the master and split it locally into verified Question Paper and Answer Key PDFs.
10. Print the new notebook URL.

For English, steps 5–9 are replaced by:

1. Select each chosen Kaveri unit separately and create its Chapter Pack PDF.
2. Select all chosen units and create the balanced Flashcard deck and mixed Quiz.
3. Create the English Skill Diagnostic and Cumulative Timed Examination as two master PDFs.
4. Download both masters and split them locally into four verified PDFs.
5. Keep the `N + 4` generated artifacts in Studio.

For Mathematics, steps 5–9 are replaced by:

1. Select all chosen chapters.
2. Create the combined Revision Guide PDF.
3. Create the combined Flashcard deck and Mind Map.
4. Create Diagnostic Paper 1 and its marking scheme together in one master PDF.
5. Create Cumulative Paper 2 and its marking scheme together in one master PDF.
6. Download both masters and split them locally into four verified PDFs.
7. Keep all five generated artifacts in Studio.

Both Mathematics papers use fixed, arithmetically verified section blueprints and the CBSE cognitive-weighting split. Questions use one sequential numbering series, and each marking scheme is created with its paper in a canonical master before the lossless local page split.

NotebookLM generation can take several minutes. Keep both the terminal and automation Chrome window open. The program prints the completed artifact count while waiting. Comet can be used normally during the run.

When everything is complete, the terminal asks you to press Enter before closing the automation browser. Use the printed URL to reopen the notebook later.

## Prompts and generated settings

The shared study prompts are stored as the `PRESENTATION`, `MIND_MAP`, and `FLASHCARDS` constants in `notebooklm_batch.py`; `combined_assessment_prompt` builds Science and Social Science masters. English uses `ENGLISH_UNIT_GUIDE`, `ENGLISH_FLASHCARDS`, `english_quiz_prompt`, `english_assessment_prompt`, and `english_jobs`. Mathematics uses `MATH_REVISION_GUIDE`, `MATH_MIND_MAP`, `mathematics_assessment_prompt`, and `mathematics_jobs`.

For Science and Social Science streams, the resolved stream name replaces `{subject}` in the shared prompts. English and Mathematics use their dedicated prompts.

Source selection is one chapter for each presentation or English Chapter Pack and all chapters for the combined artifacts. NotebookLM controls any Studio settings not specified by the prompts.

For English, Science, Social Science, and Mathematics, Flashcards scale to 20/30/40/50/60 cards for one through five-or-more chapters and are balanced across the selected chapters. Science, Social Science, and Mathematics Mind Maps use comparable chapter branches capped at 12 leaf nodes each. English Quizzes scale from 15 questions for one unit to a maximum of 30.

## Validation and expected results

For two selected Science or Social Science chapters, the completed Studio panel should contain five artifacts:

- Two Slide Decks showing `1 source` each
- One Flashcard deck showing `2 sources`
- One Mind Map showing `2 sources`
- One assessment master PDF showing `2 sources`
- Two local split PDFs under `output/pdf/`

For two selected English units, the completed Studio panel should contain six artifacts:

- Two Chapter Pack PDFs showing `1 source` each
- One Flashcard deck and one Quiz showing `2 sources` each
- Two assessment master PDFs showing `2 sources` each
- Four local split PDFs under `output/pdf/`
- No Slide Deck or Mind Map

For any Mathematics chapter selection, the completed Studio panel should contain five artifacts. Every artifact should show the full selected source count; there should be no Slide Deck or plain-text Mathematics Report. Four split assessment PDFs are saved under `output/pdf/`.

### Naming convention

Notebook names use `G9-<STREAM>-<SCOPE>`. Artifact names append a short type; per-chapter artifacts also include a short title:

```text
G9-PHY-C04_C05_C06
G9-PHY-C04_C05_C06-Cards
G9-PHY-C06-Forces-Affect-Motion-Slides
G9-MATH-C01_C03-Diag-QP.pdf
G9-ENG-U01-Taught-Grandmother-Read-Pack.pdf
```

Scopes always enumerate chapters or units (`C04_C05_C06`, never `C04-06`). Local assessment suffixes are `Test-QP`/`Test-Key` for Science and Social Science streams and `Diag-QP`/`Diag-Key` plus `Exam-QP`/`Exam-Key` for Mathematics and English. Corresponding `*-Master` PDFs remain in Studio.

The program sets and verifies the notebook title, then requests and verifies exact artifact titles. It verifies artifact completion and source counts, not the educational accuracy of generated content. Review all assessments and study materials before distributing them.

## Troubleshooting

### `No module named 'playwright'`

Run the program through the repository's virtual environment:

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python notebooklm_batch.py
```

### Google sign-in does not complete

Finish sign-in in Chrome, quit it with `Command-Q`, and only then press Enter in the terminal. If the wrong account is active, switch to the correct Chrome profile, open NotebookLM, quit Chrome, and run again.

### `chapters not found`

Verify the subject and chapter numbers, then check that the corresponding PDFs exist below `downloads/class-09`. Run `download_ncert.py` to restore the supported catalogue.

### `ambiguous chapters`

More than one PDF under the subject folder has the same encoded chapter number. Remove or relocate the unintended duplicate. The program deliberately does not choose between them.

### Artifact generation times out

The current wait limit is 30 minutes. Open the notebook in NotebookLM and inspect Studio; NotebookLM may still finish jobs after the automation stops. Account quotas or a NotebookLM generation error can also prevent completion.

Do not immediately rerun without inspecting the notebook: every confirmed run creates another notebook.

### `expected the answer-key heading on exactly one PDF page`

The generated master did not contain one unambiguous `ANSWER KEY AND MARKING SCHEME` boundary. The master remains in Studio and existing local PDFs are left untouched. Inspect the master before deciding whether to regenerate it or split it manually.

### The browser or terminal was closed during a run

Open NotebookLM manually and inspect the newly created notebook. Already submitted jobs may continue in the background. Automatic resume is not implemented yet.

## Installation check

Run the local input and catalogue check without opening Chrome:

```bash
.venv/bin/python notebooklm_batch.py --self-test
```

Expected output:

```text
self-test passed
```
