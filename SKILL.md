# studyPlans

Create source-grounded study artifacts from one approved NCERT chapter pack.

## Manual workflow

1. In NotebookLM, select only the approved chapter pack. Do not enable web
   research or unrelated notebook sources.
2. Run `python3 run.py artifacts` and use its output as the completion
   checklist. Generate each listed artifact once, one artifact at a time.
   Render its complete prompt with `python3 run.py prompt <artifact>`.
3. Paste presentation, mind-map, flashcard and quiz prompts into the
   matching Studio customisation dialog, not NotebookLM Chat. Native Studio
   artifacts are generated asynchronously and do not return in Chat; this is
   expected and is not a failed contract.
4. Paste diagram-pack, assessment-paper and `audio` prompts into NotebookLM Chat
   so they return inspectable Markdown directly; the `audio` prompt returns the
   script to synthesize after verification. Paste each prompt as one unchanged
   block; do not reorder, prepend or append rules.
5. Render the matching gate with `python3 run.py verify <artifact>` and verify
   each artifact immediately. Repair only the exact failed items and preserve
   all passing content.
6. Do not call the run complete until every enabled artifact has a passing
   verification result.

## Native-format boundary

NotebookLM controls native slide count dynamically. Treat 15-20 slides as a
directional target only; never relax source accuracy, concept coverage, required
visuals, labels, equations or relationships to meet it.

Do not ask NotebookLM Chat to create or return a native slide deck. Submit the
rendered presentation prompt through Studio's `Customize Slide Deck` dialog and
verify the completed Studio artifact after asynchronous generation.

Do not use NotebookLM's native Audio Overview for a gated artifact. Deep Dive
adds unsupported explanations, while Brief can omit required concepts. Generate
the audio script in Chat, verify that text, then have Codex synthesize speech
from the passing script without changing its words. Treat recording duration as
directional only.

NotebookLM should specify required diagrams from the chapter pack. Codex should
render the final diagrams from the verified diagram pack so labels and geometry
can be checked deterministically.

## Repair loop

For a failed artifact, paste the verifier's minimal regeneration instruction
into the same notebook and request a revision of that artifact only. Run the
same verification gate again. Never regenerate an artifact that already passes.
For a native quiz, use Studio's question editor to replace only a failed item.
