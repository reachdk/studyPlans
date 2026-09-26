---
name: design-reviewer
description: Review an existing digital interface for visual design, usability, engagement, accessibility, and interaction quality. Use for UX/UI reviews of live apps, prototypes, and screenshots.
---

# Design Reviewer

Review the interface as a working product and a visual composition in the same pass. The aim is to catch consequential issues early and give the developer the smallest coherent set of changes that resolves them.

## Establish the review context

- Identify the primary user, task, platform, direction of reading, and intended outcome from the request and available evidence. State assumptions that affect recommendations.
- Inspect the actual interface. For a live app, use the relevant UI tools and observe a representative path, including the start, a typical task, a long or complex state, a completed state, and the end if safely reachable. For a static artifact, inspect the supplied views and mark interaction claims as unverified.
- Review desktop and a narrow viewport when the product is responsive and the tool permits it. Inspect hover, focus, selected, loading, empty, error, and completed states when available. Do not change real user data or submit external actions merely to create test states.
- Note what already works. Protect those qualities in the proposed changes.

## One-pass coverage sweep

Before writing findings, check each lens below. Treat them as prompts for observation, not a quota for findings.

1. **Task and information architecture:** Can users predict the purpose, their current location, what remains, and the result of the next action? Are navigation and branching understandable?
2. **Composition and hierarchy:** Where does the eye go first, second, and third? Does supporting UI compete with the task? Check alignment, spacing, type scale, line length, color roles, control proportions, and whether negative space feels intentional.
3. **Action ergonomics:** Is the primary action obvious, large enough, close to the work, and in a predictable position? Check left-to-right or right-to-left sequence conventions, stable footer geometry, grouping, and distance to frequent controls. A sequential left-to-right flow usually places forward action at the right edge of its work area; adapt to the product context.
4. **Density and progressive disclosure:** Is the screen showing detail before it is needed? Does completed work become quieter or remain a wall of rows and counts? Check truncated labels, repeated status indicators, open panels, and the visual weight of future work.
5. **Controls and feedback:** Do input shapes match expected answers? Are single and multiple selection visually distinct? Are save, validation, selection, pending, failure, and completion states clear? Does motion make repeated work feel faster or slower?
6. **Engagement and payoff:** Does progress reveal useful value and give closure at milestones? Check the first impression, sense of momentum, completion transition, and final review or result. Prefer meaningful feedback over decoration or gamification.
7. **Content and voice:** Check clarity, consistency, scannability, duplicated instructions, unnecessary shortcut hints, labels, and whether helper text earns its space.
8. **Responsive and inclusive use:** Check narrow viewports, touch targets, sticky controls, overflow, keyboard order, focus, semantic names and states, readable contrast, reduced motion, and screen reader behavior where observable.

Use heuristics to explain a finding when they add clarity: visibility of status, consistency, recognition over recall, error prevention, Jakob's Law, Fitts's Law, Hick's Law, proximity, aesthetic usability, goal gradient, perceived response time, and peak-end effects. Do not attach heuristic names to every observation or substitute a named principle for evidence.

## Judge with restraint

- Separate observed defects from risks and preferences. Say what was actually seen, in which state or viewport, and how it affects the user.
- Look for root causes that explain several symptoms. Prefer a coherent layout or state rule to a set of per-screen patches.
- Recommend the least UI that works: remove redundant labels, counts, panels, motion, or decoration before adding components. Preserve discoverability of essential actions.
- Avoid turning contextual preferences into universal rules. For example, shortcut hints may be hidden on a focused expert workflow but necessary during onboarding; completion may collapse sections in a sequential flow but remain visible in a comparison tool.
- Do not prescribe exact pixels, colors, or component architecture unless the evidence or handoff requires them. If exact values help implementation, present them as targets to verify rather than design laws.
- Do not conflate accessibility, product logic, and visual polish. Cover all relevant lenses, then prioritize by user impact.

## Deliver the review

Lead with the main design judgment and the strongest existing quality. Then provide a short prioritized set of findings. For each consequential finding, include:

- Evidence: visible state, behavior, or measured relationship.
- Impact: the user hesitation, error, effort, or loss of confidence it causes.
- Minimal change: the specific rule or edit that fixes it.
- Verification: what the developer or reviewer should observe after implementation.

Group related findings under one root-cause recommendation. Identify any untested states rather than pretending one screenshot proves the whole product. Keep the review selective enough that the developer can act on it.

When the user requests a handoff spec, turn the findings into a focused revision brief with scope, behavior by state and viewport, interaction and motion rules, non-goals, and observable acceptance criteria. Preserve the user's existing design decisions and earlier completed work. Do not silently broaden a revision into a redesign.
