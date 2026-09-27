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
Ingest the provided NCERT chapter and produce 4 files adhering to the Gold Standard:
1. meta.json: id, code, title, sub (category id), theme, lg (learning goal), desc, pdf relative path.
2. guide.md: Comprehensive 200–250 line revision guide using 5 progressive disclosure accordions:
   - Section 1: Teacher's Masterclass Overview & Definitional Foundations
   - Section 2: Core Taxonomy & Multi-Case Boundary Condition Tables (8+ test cases)
   - Section 3: Algorithmic Step-by-Step "How-to-Solve" Protocols & Sign Hygiene
   - Section 4: Deep Theorems, Formula Derivations, and Geometric/Real-World Intuition
   - Section 5: Examiner's Pitfall Matrix & 4-Tiered Solved Practice (Foundational -> HOTS)
   - Embedded Interactive Parameter Explorer Widget
3. flashcards.json: Exactly 18–20 high-yield cards across 5 recall categories:
   - Category 1: Definitions & Constraints (4 cards)
   - Category 2: Degree, Classification & Key Theorems (4 cards)
   - Category 3: Rapid Mental Math & Calculation Drills (4 cards)
   - Category 4: Exam Traps & True/False Nuances (4 cards)
   - Category 5: Geometric Intuition & Visual Connections (2-3 cards)
4. questions.json: 8–10 authentic CBSE questions covering the Section A–E blueprint:
   - 2x MCQs (1m) with 4 options and distractor analysis
   - 1x Assertion-Reasoning (1m) with authentic 4 CBSE standard choices
   - 2x Very Short Answer (2m) with explicit [1m + 1m] marking scheme
   - 2x Short Answer (3m) with explicit [1m + 1m + 1m] marking scheme
   - 1x Long Answer / HOTS (5m) with multi-part synthesis [1m + 2m + 2m]
   - 1x Case-Based Integrated Study (4m) with authentic real-world stem and 3 sub-questions [1m + 1m + 2m] with internal choice
   *Every question MUST have: id, title, type, marks, prompt, options (if MCQ/AR), solution, markingScheme (array of fractional point breakdowns), and examinerTip.*
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
