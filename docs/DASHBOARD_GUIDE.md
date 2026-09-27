# Class 9 Science Study Portal — Guide & Setup

A serverless, single-folder interactive study portal designed for Class 9 CBSE Science. When copied into your child's Google Drive, it runs independently, tracks their individual progress, and provides active recall tools with zero server setup.

---

## What's in the Folder

```
studyPlans/
├── study_dashboard.html         # Main interactive study portal (open this file)
├── DASHBOARD_GUIDE.md           # This guide
├── generate_dashboard_data.py   # Offline & dataset verification script
├── notes/science/               # Full CBSE Class 9 revision guides (13 chapters)
│   ├── foundations/             # Ch 1: Entering Secondary Science
│   ├── biology/                 # Ch 2, 3, 11, 12, 13
│   ├── chemistry/               # Ch 5, 8, 9
│   └── physics/                 # Ch 4, 6, 7, 10
└── downloads/class-09/          # Local NCERT official chapter PDFs
    └── science/exploration/     # iesc101 to iesc113
```

---

## 1. Two-Tier Hierarchical Flow

### Tier 1: Main Dashboard (Science Hub)
* **Subject Tabs**: Filter across **All Science (13 Chapters)**, **Physics (4)**, **Chemistry (3)**, **Biology (5)**, and **Foundations (1)**.
* **Progress Snapshot**:
  * Shows overall completion across the curriculum.
  * Every chapter tile displays a live progress bar reflecting:
    * Notes marked as completed
    * Practice questions attempted and self-evaluated
    * Flashcards mastered
* **Direct Tile Action**: Click **`🚀 Open Chapter Study Room →`** on any tile to immediately enter that chapter's workspace.

### Tier 2: Dedicated Chapter Study Room
Clicking any chapter tile opens its dedicated workspace with four specialized sub-tabs:
1. **📖 Interactive Revision Guide**:
   * Fully embedded inside the page with clean typography and collapsible concept accordions.
   * **Live Interactive Formula Calculators**:
     * *Ch 4 Motion*: Kinematic solver for $v = u + at$ and $s = ut + \frac{1}{2}at^2$.
     * *Ch 5 Mixtures*: Solution concentration solver ($\% \text{ w/w}$).
     * *Ch 6 Force*: Newton's Second Law solver ($F = ma$).
   * **Visual Difference Tables**: Formatted comparison grids (Solution vs Colloid vs Suspension, Xylem vs Phloem, Striated vs Smooth muscle, etc.).
   * **"Why Does This Happen?"**: Deep-dive real-world reasoning and CBSE topper exam tips.
2. **✍️ Practice Questions & Attempt Reveal**:
   * Questions displayed with marks and difficulty badges.
   * **Attempt Checkpoint**: Model answers are folded away behind an active confirmation button (`✍️ I have attempted this — Reveal Solution`).
   * Once confirmed, the step-by-step model solution, CBSE marking scheme, and tip are revealed.
   * **Self-Evaluation**: Mark `🌟 Nailed it! (+1)` or `🔁 Need review` to record progress.
3. **🔄 3D Flashcards**:
   * Realistic 3D card flips with `Spacebar` or tap.
   * Controls for Next, Prev, Shuffle, and `🌟 Mastered`.
4. **📄 NCERT Chapter PDF**:
   * One-click direct link to open the official NCERT textbook PDF stored in the local folder.

---

## 2. Using with Two Kids in Google Drive

Because the folder uses **100% relative paths** and is completely self-contained:

1. **Copy the entire folder** into **Child 1's Google Drive** (e.g. `My Drive > Aarav > Science_Study_Portal`).
2. **Copy the entire folder** into **Child 2's Google Drive** (e.g. `My Drive > Diya > Science_Study_Portal`).
3. Each child opens their own copy of `study_dashboard.html`:
   * They can click on the name pill in the top header (`👤 Student's Hub ✏️`) to personalize their name (e.g., *"Aarav's Study Hub"*).
   * All progress, card mastery, and question completions will save independently for each child.
4. **Zero Cross-Talk**: Neither child's scores or progress will ever interfere with the other.

---

## 3. Resetting & Undoing Progress (Multi-Level)

If you are testing the dashboard or accidentally mark an item as complete, you can undo or reset at any granularity:

1. **Question Level (Instant Undo)**:
   * **Reset Question**: Click `↺ Reset Question` on any question card header to re-lock the solution behind the friction checkpoint and mark it back to `⚪ Not Attempted`.
   * **Self-Evaluation Toggle**: Click `🔁 Undo / Need Review` inside the revealed solution bar to remove the solved point.
2. **Flashcard Level (Undo Mastery)**:
   * Click `🌟 Mastered (Click to Undo)` to toggle a card back to unmastered state.
3. **Chapter Level**:
   * Inside any Chapter Study Room, click `↺ Reset Chapter` in the top action bar to clear all questions, flashcards, and reading marks for that chapter.
4. **Subject Level (Physics / Chemistry / Biology)**:
   * Click `🔄 Reset` in the top header or `🔄 Reset Progress...` next to the progress bar.
   * Select **Reset Physics**, **Reset Chemistry**, or **Reset Biology** to reset only that subject's 3 chapters.
5. **Overall Level**:
   * Select **⚠️ Reset Everything** in the Reset modal to reset all 9 chapters back to a fresh 0% state.

---

## 4. Keyboard Shortcuts (Inside Flashcards)

* `Spacebar`: Flip card
* `Right Arrow (→)`: Next card
* `Left Arrow (←)`: Previous card

---

## 5. Verification Check

To verify that the portal remains self-contained, valid, and 100% offline-ready:

```bash
.venv/bin/python generate_dashboard_data.py --verify
```

