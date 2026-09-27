# Google Classroom → NotebookLM sources

`classroom_sync.py` downloads teacher-posted attachments from active **Maths, English, Social Science, Physics, Chemistry, Biology, German and IT** classes. It excludes classes named Advanced Maths/Science and Physical Education. Inspect the class list before confirming; use `--course ID` (repeatable) if the school's class names differ or you want an exact selection. This is separate from `notebooklm_batch.py`, which currently expects a fixed NCERT chapter catalogue, **not** these Classroom files.

## One-time Google setup

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/). Enable **Google Classroom API** and **Google Drive API**.
2. Configure the OAuth consent screen (Google Auth Platform). Choose **External** if the school account isn't in your Workspace organization, and add the child's Google account as a **test user**. Set up the requested Classroom read-only and Drive read-only scopes. Google currently grants the student coursework scope as `classroom.student-submissions.me.readonly`; the script still only reads teacher posts/material attachments and does not download submissions. For private use in testing mode, Google may require reauthorization periodically; if the school blocks third-party OAuth apps, ask its administrator to approve the app. Do not try to bypass its controls.
3. Create an **OAuth client ID → Desktop app**, download its JSON file, and save it in this project as `classroom-credentials.json`. This file and the generated `.classroom-token.json` are gitignored. Never share either file.
4. Install dependencies:

```bash
.venv/bin/python -m pip install -r requirements-classroom.txt
```

## Run

```bash
.venv/bin/python classroom_sync.py --list
.venv/bin/python classroom_sync.py
```

The first command opens a browser for Google's sign-in and prints the active classes (`*` means auto-selected). **Sign in as the child whose Classroom classes you want.** The second command prints them again and asks for confirmation before syncing. For exact selection, copy IDs from `--list`:

```bash
.venv/bin/python classroom_sync.py --course 123456789 --course 987654321
```

Files are organized neatly under `downloads/classroom/<subject>/` (e.g. `chemistry/`, `mathematics/`, `physics/`, `biology/`, `english/`, `social-science/`, `information-technology/`, `german/`) and named with their teacher-posted date prefix: `YYYY-MM-DD_<slug-title>.<ext>` (e.g. `2026-06-29_chemistry-review-sheet.pdf`). The file's filesystem modification time (`mtime`) is also set to the post date so macOS Finder / file managers sort them chronologically by default. Google Docs, Slides, Sheets and Drawings are exported as PDFs; other Drive files retain their original extension. A `manifest.json` records file names, originating course/post, external URLs and failures. Re-running downloads only missing or changed files. Other attachments (web links, videos, Forms) are **listed in the manifest but not fetched**; inspect those separately. Student submissions and comments are not fetched even though Google may label the read-only coursework authorization as a student-submissions scope. If an attachment cannot be accessed or exported, the script reports it and exits with an error; check the manifest's `errors` field. Some Google exports have size limits.

Upload the relevant PDFs/files from the class folders into NotebookLM as sources. Avoid adding the manifest (it contains links and post metadata), classmates' personal information, or files you don't want sent to NotebookLM. The current `notebooklm_batch.py` does not yet ingest these folders automatically.

The OAuth token grants read access to Classroom and Drive files visible to this account. Keep it private; to revoke access, remove the app from the Google account's third-party connections, then delete `.classroom-token.json`. `downloads/classroom/` is gitignored, but still contains school material: protect local backups and don't share the folder publicly.
