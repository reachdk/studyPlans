# Work Plan for 12 July 2026

## Objective

Complete the lesson-plan overview for NCERT Class 9 Science, Chapter 4, *Describing Motion Around Us*, using a controlled manual NotebookLM workflow followed by diagram selection in Codex.

## 1. Recreate the NotebookLM artifacts manually

- Start again manually in NotebookLM.
- Use only this approved chapter pack:
  - `output/class-9-science-chapter-4-describing-motion-around-us.md`
- Do not select the official PDF, unrelated notebook sources, web sources, or NotebookLM research results during artifact generation.
- Generate each artifact exclusively from the approved chapter pack.
- Verify that no *Structure of the Atom* content or other unsupported research appears.

## 2. Update the artifact prompt for diagrams

Update the generation prompt so NotebookLM also returns a structured **diagram pack**.

The diagram pack should contain one entry for every place where a diagram would materially help the artifact or lesson plan. Each entry should include:

- a stable diagram ID;
- the related chapter section or concept;
- the diagram's instructional purpose;
- the exact scientific content and labels required;
- the preferred diagram type, such as number line, motion sequence, graph, apparatus, comparison or annotated illustration;
- the artifact or lesson-plan location where it should appear;
- whether it must reproduce an NCERT figure concept or may be a newly designed explanatory diagram;
- any accuracy constraints or common misconception the diagram must avoid.

NotebookLM should describe the required diagrams, not invent unsupported scientific content.

## 3. Bring the diagram pack back to Codex

- Add the generated diagram pack to this workspace.
- Review every diagram entry against the approved chapter pack.
- Decide the most appropriate visual treatment for each entry.
- Reuse an NCERT figure only where necessary and appropriate.
- Otherwise create a clear, student-friendly explanatory diagram that preserves NCERT terminology and meaning.
- Check labels, directions, signs, axes, units, scales, equations and scientific relationships.
- Map every approved diagram to its exact position in the lesson plan or artifact.

## 4. Complete the chapter lesson-plan overview

Combine the approved content artifacts and diagram mapping into the final lesson-plan overview.

Completion criteria:

- only the approved chapter pack was used in NotebookLM;
- every core Chapter 4 concept is covered;
- no atomic-structure or unsupported research content remains;
- the diagram pack is complete and verified;
- every diagram has an approved visual approach and lesson-plan location;
- the final overview follows the NCERT instructional sequence;
- terminology, equations, graphs, activities and assessments remain accurate.

## Starting point

Use the previous verification report to avoid repeating the source-contamination issues:

- `output/notebooklm-artifact-verification.md`
