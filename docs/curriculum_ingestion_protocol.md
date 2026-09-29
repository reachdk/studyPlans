# Curriculum Ingestion Protocol & Ground-Truth Verification Standard

## Purpose & Scope
This protocol establishes an enforceable engineering standard for authoring, updating, or reviewing educational content, curriculum dossiers, and study portals (English, Mathematics, Science, Social Science, Information Technology, German, and future subjects).

It directly addresses and permanently prevents the failure mode of **parametric hallucination** and **shallow title verification**, ensuring that every fact, narrative arc, character dossier, poem stanza, and examination question in our portals is directly grounded in verified primary source documents.

---

## The 4 Golden Rules of Curriculum Ingestion

### Rule 1: The "Extraction-First" Mandate (Zero-Guess Rule)
- **Never author content from memory or chapter titles alone.**
- Before writing data structures, summaries, character dossiers, or questions, the agent must execute an extraction script or tool to extract the raw text from the primary source document (PDF, PPT, or official syllabus document) into an intermediate, auditable text buffer or markdown dossier.
- If a chapter or unit has not been extracted and read, it must **never** be synthesized.

### Rule 2: Named-Entity & Textual Citation Gate
For every literary piece, historical event, or scientific phenomenon, the agent must explicitly verify and cite:
1. **Primary Author / Poet / Source**: Full verified name and context.
2. **Key Named Characters / Entities**: Primary protagonists and secondary characters as they appear in the source text (no generalized or substitute names).
3. **Exact Opening & Closing Citations**: Direct quotes from the source document.
4. **Source Page Numbers**: Specific page references matching the source PDF.

### Rule 3: Automated Content Integrity Testing
Every subject must have an automated test suite (e.g. `tests/test_<subject>_curriculum_integrity.py`) that:
- Asserts that all core named entities, themes, and quotations in the data module appear in the extracted source text.
- Scans for and forbids known hallucinated or placeholder tokens.
- Fails the build immediately if discrepancies or ungrounded entities are detected.

### Rule 4: Traceable Provenance
All datasets (`portal_engine/*_data.py` or `subjects/*/*.json`) must document the exact source files from which they were compiled, including filename, page count, and MD5 / SHA-256 or git revision, ensuring complete auditability.
