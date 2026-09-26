# NotebookLM Class 9 Study Builder

Creates a new personal NotebookLM notebook from selected local NCERT chapters.

For Science and Social Science the notebook contains:

- One Slide Deck per chapter
- One combined Flashcard deck
- One combined Mind Map
- One assessment master PDF

With `--split`, NotebookLM creates separate Question Paper and Answer Key PDFs in Studio. The master is deleted only after both exact output names are verified.

For `N` selected English Kaveri units it generates `N + 4` Studio artifacts by default:

- `N` source-specific Chapter Pack PDFs
- One combined Flashcard deck
- One combined Quiz
- Two timed assessment master PDFs in Studio
- With `--split`, two Question Paper PDFs and two matching Answer Key PDFs replace the masters in Studio

For Mathematics it generates five Studio artifacts by default:

- One combined chapter Revision Guide PDF
- One combined Flashcard deck
- One combined Mind Map
- One Diagnostic master PDF and one Cumulative master PDF in Studio
- With `--split`, Question Paper and Answer Key PDFs replace both masters in Studio

The program asks for a stream code and chapter numbers, resolves the matching PDFs under `downloads/class-09`, uploads them through an isolated Google Chrome instance, and asks NotebookLM chat to create the configured artifacts with its Studio tools. Supported stream codes are `PHY`, `CHEM`, `BIO`, `HIST`, `GEO`, `ECO`, `POL`, `MATH`, and `ENG`.

Notebook and artifact titles follow one sortable convention. For example, a Physics run for chapters 4 and 6 creates notebook `G9-PHY-C04_C06`; its combined cards are `G9-PHY-C04_C06-Cards`, while chapter 6 slides are `G9-PHY-C06-Forces-Affect-Motion-Slides`. PDF artifacts retain their `.pdf` extension. English scopes use `U`, such as `G9-ENG-U01_U03`.

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

To split every assessment master into Question Paper and Answer Key PDFs in Studio, use:

```bash
.venv/bin/python notebooklm_batch.py --split
```

Each master is split and verified before the next assessment starts. If generation fails or the titles do not match, the master is preserved and the run stops.

Example input:

```text
Stream code (PHY/CHEM/BIO/HIST/GEO/ECO/POL/MATH/ENG): PHY
Chapters (for example 4,6-7): 4,6

Resolved PHY (Physics) chapters:
  04 — Describing Motion Around Us
  06 — How Forces Affect Motion

Create the NotebookLM notebook? [y/N] y
```

All subject-specific paper sizes scale automatically with the selected chapter scope. Flashcard counts and chapter coverage also scale automatically; Mathematics additionally retains the CBSE cognitive-weighting split. English and Mathematics do not create Slide Decks.

On the first run, confirm NotebookLM opens while signed in to Google Chrome, quit Chrome completely with `Command-Q`, then return to the terminal and press Enter. The program copies that profile into its dedicated automation profile; your normal Chrome data is not modified. Comet remains available for normal browsing while the automation runs.

### Chrome profile on another computer

The Chrome profile display name is configured near the top of `notebooklm_batch.py`:

```python
CHROME_PROFILE = "Ghar"
```

When moving the program to another computer, replace `Ghar` with the profile name shown in Chrome's profile menu. Open NotebookLM in that profile once and confirm it is signed in before running the program. The code resolves the display name to Chrome's internal directory automatically; do not replace it with a directory name such as `Profile 1`.

See [USER_GUIDE.md](USER_GUIDE.md) for supported inputs, the complete workflow, and troubleshooting.

## Google Classroom source sync

For teacher-posted materials in selected classes, see [CLASSROOM_SYNC.md](CLASSROOM_SYNC.md). `classroom_sync.py` uses Google's OAuth sign-in and Classroom/Drive APIs to download attachments into `downloads/classroom/` for use as NotebookLM sources. It does not change the NCERT chapter workflow above.

## Check the installation

```bash
.venv/bin/python notebooklm_batch.py --self-test
```

## Current limitation

Every confirmed run creates a new notebook. Interrupted runs are not resumed automatically; inspect the partially created notebook before starting another run.
