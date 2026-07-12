# NotebookLM Artifact Verification - 12 July 2026

## Verification scope

- Notebook: `c1408142-ec97-4ce4-a23e-e7fda721f5b7`
- Canonical source: `iesc104.pdf`
- Approved chapter pack: `class-9-science-chapter-4-describing-motion-around-us.md`
- Chapter: NCERT Class 9 Science, Chapter 4, *Describing Motion Around Us*
- Generated artifacts inspected: 6
- Enabled artifacts absent from the notebook: 2

## Source result

**PASS**

The notebook contains and selects only the approved chapter pack. No web
research or unrelated source is present. Verification was performed against
both the chapter pack and the official 24-page NCERT chapter PDF in `output/`.

## Overall result

**FAIL: 0 of 8 enabled artifacts pass the verification gate.**

Six artifacts were generated but each has at least one qualifying failure.
The enabled diagram pack and diagnostic paper were not generated.

## Artifact results

### 1. Audio overview - Why Doubling Speed Quadruples Stopping Distance

**FAIL**

Exact contract failure:

- Duration is `22:54`; the artifact contract requires `12-15 minutes`.

Minimal regeneration instruction:

> Regenerate the audio as a 12-15 minute explanation in the chapter's original sequence, covering the Core Concept Checklist without filler.

### 2. Presentation - The Kinematic Blueprint

**FAIL**

Exact incorrect item:

- The braking-distance slide says braking distance increases "exponentially"
  with speed. Under the chapter's stated constant braking acceleration,
  `v^2 = u^2 + 2as` gives braking distance proportional to the square of the
  initial speed; doubling speed makes it four times as large. This is
  quadratic, not exponential.

The deck does meet its `15-20` slide count with 16 slides.

Minimal regeneration instruction:

> Regenerate only the braking-distance slide: replace "exponentially" with the source-supported quadratic relationship `s proportional to u^2` under the same constant braking acceleration, and retain the doubling-speed/four-times-distance example.

### 3. Standard assessment paper

**FAIL**

Exact missing or incorrect items:

- The general instructions define upward as positive and downward as negative,
  but the Section C vertical-motion answer uses downward displacement
  `s = +0.6 m` and downward acceleration `a = +9.8 m s^-2` without declaring a
  new convention. With the paper's convention, both values must be negative.
- The Assessment Blueprint requires one graph-plotting task. The paper includes
  graph interpretation and area/slope calculations, but no task requiring the
  student to plot a graph with labelled axes, units and a scale.

The paper does total 40 marks and its reported numerical result for the
vertical-motion time remains `0.35 s`; the defect is the contradictory sign
working.

Minimal regeneration instruction:

> Keep the paper at 40 marks, correct the Section C vertical-motion working to `s = -0.6 m` and `a = -9.8 m s^-2` under the stated convention, and replace or rebalance one existing graph item with a graph-plotting task requiring labelled axes, units and scale.

### 4. Quiz - Motion Quiz

**FAIL**

Exact ambiguous item:

- Question 10 states only that `v < u`, then treats acceleration as negative
  **and opposite to the direction of motion**. `v < u` proves negative
  acceleration for a positive time interval, but it does not establish that
  acceleration opposes motion unless the velocity direction is also specified.
  For negative `u` and `v`, negative acceleration can be in the same direction
  as motion.

The quiz contains exactly 25 complete questions.

Minimal regeneration instruction:

> Keep the other 24 questions unchanged and revise Question 10 to state that the object moves in the chosen positive direction with positive `u` and `v`, where `v < u`; retain the answer that acceleration is negative and opposite to velocity.

### 5. Flashcards - Motion Flashcards

**FAIL**

Exact missing core concepts:

- Linear motion and its consistent positive/negative direction convention.
- Acceleration can result from a change in speed, direction or both.
- Plotting motion data with labelled axes, units and suitable scales.
- Motion in a plane as two-dimensional motion.
- For one complete revolution: distance `2 pi R`, zero displacement and zero
  average velocity. Only average speed is included.
- Stopping distance depends on reaction time and road conditions, not only
  initial speed and braking acceleration.

The artifact does meet the contract for exactly 30 unique, complete
front-and-back pairs.

Minimal regeneration instruction:

> Keep exactly 30 cards, replacing lower-priority recall cards as needed so the six missing Core Concept Checklist items above are each covered once; keep every front and back non-empty.

### 6. Mind map - Motion Mindmap

**FAIL**

Exact missing or incorrect items:

- The complete-revolution branch includes `2 pi R`, zero displacement and
  `2 pi R/T`, but omits zero average velocity.
- It does not state the core relationship that acceleration can result from a
  change in velocity magnitude, direction or both.
- The position-time branch says slope represents the "magnitude of velocity";
  preserve the chapter terminology that slope represents velocity (average
  velocity over a selected interval).

The artifact meets the four-level structure contract and uses the chapter
title as root with the four major sections as first-level branches.

Minimal regeneration instruction:

> Keep the current four-level map, add zero average velocity to the one-revolution branch, add magnitude/direction/both under acceleration, and change the position-time slope label to velocity (average velocity over an interval).

### 7. Diagram pack

**FAIL - NOT GENERATED**

Exact missing item:

- No diagram pack appears in the notebook, although `diagram_pack` is enabled
  in `config.yaml`.

Minimal regeneration instruction:

> Generate the enabled diagram pack from Required Visuals D01-D18, covering each visual exactly once with stable ID, purpose, labels, preferred visual type, placement and accuracy constraints.

### 8. Diagnostic assessment paper

**FAIL - NOT GENERATED**

Exact missing item:

- No diagnostic paper appears in the notebook, although `paper_diagnostic` is
  enabled in `config.yaml`.

Minimal regeneration instruction:

> Generate the enabled 40-mark diagnostic paper from the Assessment Blueprint and Common Misconceptions, covering every high-priority misconception and assessment domain with a verified answer key and marks totalling exactly 40.
