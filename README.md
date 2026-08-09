# NotebookLM Class 9 Study Builder

Creates a new personal NotebookLM notebook from selected local NCERT chapters and generates:

- One Slide Deck per chapter
- One combined Flashcard deck
- One combined Mind Map
- One assessment question-paper PDF
- One assessment answer-key PDF

The program asks for a subject and chapter numbers, resolves the matching PDFs under `downloads/class-09`, uploads them through an isolated Google Chrome instance, and asks NotebookLM chat to create the configured artifacts with its Studio tools.

## Setup

Requirements:

- Python 3.10 or newer
- Google Chrome
- A personal Google account with NotebookLM access

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Download the current local chapter catalogue if it is not already present:

```bash
.venv/bin/python download_ncert.py
```

## Run

```bash
.venv/bin/python notebooklm_batch.py
```

Example input:

```text
Subject: Physics
Chapters (for example 4,6-7): 4,6

Resolved chapters:
  04 — Describing Motion Around Us
  06 — How Forces Affect Motion

Create the NotebookLM notebook? [y/N] y
```

On the first run, confirm NotebookLM opens while signed in to Google Chrome, quit Chrome completely with `Command-Q`, then return to the terminal and press Enter. The program copies that profile into its dedicated automation profile; your normal Chrome data is not modified. Comet remains available for normal browsing while the automation runs.

### Chrome profile on another computer

The Chrome profile display name is configured near the top of `notebooklm_batch.py`:

```python
CHROME_PROFILE = "Ghar"
```

When moving the program to another computer, replace `Ghar` with the profile name shown in Chrome's profile menu. Open NotebookLM in that profile once and confirm it is signed in before running the program. The code resolves the display name to Chrome's internal directory automatically; do not replace it with a directory name such as `Profile 1`.

See [USER_GUIDE.md](USER_GUIDE.md) for supported inputs, the complete workflow, and troubleshooting.

## Check the installation

```bash
.venv/bin/python notebooklm_batch.py --self-test
```

## Current limitation

Every confirmed run creates a new notebook. Interrupted runs are not resumed automatically; inspect the partially created notebook before starting another run.
