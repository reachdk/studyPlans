# Standard Operating Procedure (SOP): Rapid Subject & Chapter Generation

This guide details how to generate a brand new, authentic, CBSE-standard interactive study dashboard for any subject (e.g. Mathematics, Social Science, English, IT, or Class 10) in **under 1 hour** using the Study Portal Engine.

---

## The 5-Step Generation Pipeline

```
1. SOURCING          2. CONTENT CREATION        3. VALIDATION        4. COMPILATION      5. PACKAGING
(PDFs & Worksheets)  (Markdown & JSON)          (validator.py)       (builder.py)        (packager.py)
        │                     │                        │                   │                   │
        ▼                     ▼                        ▼                   ▼                   ▼
downloads/class-09/  subjects/<subject>/        0% errors,           Self-contained      Lean ~15MB
NCERT chapter PDFs   chapters/ & mock_papers/   80m verified         Single HTML file    Kid Bundle
```

---

## Step 1: Initialize Subject Folder Structure

Create the subject directory:
```bash
mkdir -p subjects/<subject_id>/chapters subjects/<subject_id>/mock_papers
```

Create `subjects/<subject_id>/manifest.json`:
```json
{
  "id": "mathematics",
  "title": "Class 9 Mathematics — Interactive Study Portal",
  "subjectName": "Mathematics",
  "grade": "Class 9",
  "badge": "CLASS 9 MATH",
  "subtitle": "NCERT Ganita Manjari • CBSE Exam Preparation",
  "categories": [
    { "id": "num", "name": "Number Systems", "color": "#0284c7", "light": "#f0f9ff" },
    { "id": "alg", "name": "Algebra", "color": "#7c3aed", "light": "#f5f3ff" },
    { "id": "geom", "name": "Geometry & Mensuration", "color": "#16a34a", "light": "#f0fdf4" }
  ],
  "defaultActiveScope": ["iemh101", "iemh102", "iemh103", "iemh104", "iemh106"],
  "chapters": [
    { "folder": "ch01_coordinates" },
    { "folder": "ch02_linear_polynomials" },
    { "folder": "ch03_world_of_numbers" },
    { "folder": "ch04_algebraic_identities" },
    { "folder": "ch06_perimeter_and_area" }
  ]
}
```

---

## Step 2: Extract Chapter Content (Prompt for AI Agent)

For each chapter, provide the NCERT PDF or text to the LLM/subagent using this prompt:

### System Prompt / Extraction Instruction:
```text
You are an expert CBSE Class 9 curriculum specialist and question paper setter.
Ingest the provided NCERT chapter and produce 4 files:
1. meta.json: id, code, title, sub (category id), theme, lg (learning goal), desc, pdf relative path.
2. guide.md: High-yield revision summary with:
   - Teacher's Overview (> 👨‍🏫 **Teacher's Overview:**)
   - Core concepts, definitions, and theorems
   - Key formulas with clean math notation (x^2, \sqrt{...}, (x, y))
   - Comparison tables (| Property | Concept A | Concept B |)
   - Common Exam Traps (> ⚠️ **Exam Trap:**)
3. flashcards.json: Array of 8-10 cards with id, tag, front (prompt/concept), back (detailed explanation/derivation), note.
4. questions.json: 8-10 authentic CBSE questions categorized by type:
   - MCQs (1m) with options
   - Assertion-Reasoning (1m) with options
   - Short Answer (2m & 3m)
   - Long Answer (5m)
   - Case-Based Studies (4m)
   *Every question MUST have: prompt, marks, answer, markingScheme (step-by-step mark breakdown), and examinerTip.*
```

---

## Step 3: Full-Length CBSE Mock Papers

Create 3 non-overlapping papers in `subjects/<subject_id>/mock_papers/paper_1.json`, `paper_2.json`, `paper_3.json`:
- **Pattern**: Section A (20m MCQs/AR), Section B (10-12m VSA), Section C (18-21m SA), Section D (15-20m LA), Section E (12m Case Studies) = **Total 80 Marks**.
- **Requirement**: Use authentic school question papers (e.g. from `downloads/classroom/`) and CBSE Board past years. Ensure 0% question overlap between papers.

---

## Step 4: Validate and Compile

Run the automated quality validator:
```bash
python portal_engine/validator.py --subject <subject_id>
```
*If any mark counts do not sum to 80, if questions overlap, or if PDF links are broken, the validator will halt with explicit file and line details.*

Compile into the self-contained dashboard:
```bash
python portal_engine/builder.py --subject <subject_id>
```
*Outputs: `study_<subject_id>_dashboard.html` (~500 KB, 100% offline, zero external dependencies).*

---

## Step 5: Export Lean Distribution Bundle for Google Drive

Run:
```bash
python portal_engine/packager.py --subject <subject_id> --output ~/Desktop/<Subject>_Study_Portal
```
*Creates a ~15-25 MB folder containing only the dashboard HTML, referenced NCERT PDFs, and notes. Clean, safe, and ready to share.*
