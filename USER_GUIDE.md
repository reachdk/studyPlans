# User Guide

## What the automation does

For a run containing `N` chapters, the program creates one new NotebookLM notebook with `N + 4` Studio artifacts:

1. `N` chapter presentations, each using only its corresponding chapter source
2. One Flashcard deck using all selected chapters
3. One Mind Map using all selected chapters
4. One assessment question-paper PDF using all selected chapters
5. One assessment answer-key PDF using all selected chapters

The program leaves artifact generation to NotebookLM and waits for every artifact and the assessment chat response to finish.

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

1. Subject
2. Chapter numbers
3. Confirmation of the resolved chapter list

Nothing is uploaded if the confirmation is anything other than `y`.

### Subject input

Subject names are case-insensitive. Supported inputs are:

| Input | Chapter folder |
|---|---|
| `Physics`, `Chemistry`, `Biology`, `Science` | `downloads/class-09/science` |
| `Math`, `Maths`, `Mathematics` | `downloads/class-09/mathematics` |
| `English` | `downloads/class-09/english` |
| `Social Science`, `Social Studies`, `social-science` | `downloads/class-09/social-science` |

Physics, Chemistry, and Biology share the Science textbook folder. The program trusts the selected chapter numbers; it does not decide whether a Science chapter belongs to the requested discipline.

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

The browser workflow is:

1. Create a new NotebookLM notebook.
2. Upload the resolved PDF chapters.
3. Wait until every source finishes processing.
4. Rename the notebook to `CBSE Class 9 <Subject> — Chapters <numbers>`.
5. Select one chapter at a time and ask NotebookLM chat to create its Slide Deck with the Studio tool.
6. Select every chapter and ask chat to create the combined Flashcard deck with the Studio tool.
7. Ask chat to create the combined Mind Map with the Studio tool.
8. Ask chat first for the Question Paper Studio Report, then for its matching Answer Key Studio Report.
9. Wait for the question paper, answer key, and all Studio artifacts to finish.
10. Print the new notebook URL.

NotebookLM generation can take several minutes. Keep both the terminal and automation Chrome window open. The program prints the completed artifact count while waiting. Comet can be used normally during the run.

When everything is complete, the terminal asks you to press Enter before closing the automation browser. Use the printed URL to reopen the notebook later.

## Prompts and generated settings

The study prompts are stored as the `PRESENTATION`, `MIND_MAP`, and `FLASHCARDS` constants in `notebooklm_batch.py`; `assessment_document_prompt` builds the separate Question Paper and Answer Key instructions. Each is prefixed with an explicit instruction from `STUDIO_ACTIONS` telling NotebookLM chat which Studio tool to invoke, followed by `STUDIO_EXECUTE_NOW` to prevent preview or confirmation responses.

The entered subject replaces `{subject}` in the Assessment and Presentation prompts. Other prompt text is submitted unchanged.

Source selection is one chapter for each presentation and all chapters for the combined artifacts. NotebookLM controls any Studio settings not specified by the prompts.

## Validation and expected results

For two selected chapters, the completed Studio panel should contain six artifacts:

- Two Slide Decks showing `1 source` each
- One Flashcard deck showing `2 sources`
- One Mind Map showing `2 sources`
- Two PDF assessment files showing `2 sources` each

NotebookLM chooses the individual artifact titles. The program verifies artifact completion and source counts, not the educational accuracy of generated content. Review all assessments and study materials before distributing them.

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
