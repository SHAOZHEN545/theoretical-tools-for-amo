---
name: pedagogical-notes
description: Writing conventions for pedagogical notes in this vault — textbook-style physics exposition. Use whenever the user asks for pedagogical notes, or when writing or rewriting a note in Notes/.
---

# Pedagogical Notes

When I ask for **pedagogical notes**, follow these writing conventions:

Write in English, with the clarity and natural flow of a well-written physics textbook rather than a technical report.

Develop ideas through motivated, step-by-step reasoning. Let mathematics carry the derivation, using concise prose to motivate each step and explain its physical meaning.

Keep the prose concise but conversational, using the inclusive "we" rather than "I". Break paragraphs naturally as the reasoning progresses. Aim for a visually comfortable rhythm of short paragraphs interspersed with well-placed display equations, avoiding dense prose and excessive inline math.

Use natural, reader-oriented section titles. Avoid unnecessary headings, executive summaries, boldfaced takeaways, and grand-sounding statements.

Be rigorous without being stiff. Let interesting questions, physical intuition, and occasional humor arise naturally, never artificially.

Prioritize the reader's understanding over comprehensive coverage. Do not generate additional sections or notes beyond what I request.

## Equation numbers and references

Number only the equations that the text refers to again: the key results, and the steps a later derivation builds on. Leave the others unnumbered.

When a reference points to an equation the reader cannot see from where they are reading, because it is more than a screen away or in another note, make the reference a block link. Hovering over the link then shows the equation, in Obsidian's reading view and on the published Quartz site. Put a block ID on the line directly after the closing `$$`:

```markdown
$$
[A_1,H_0]=-V_{OD} .
\tag{1}
$$
^eq-a1-condition
```

Link to it with `[[#^eq-a1-condition|Eq. (1)]]` inside the note, and with `[[Note title#^eq-a1-condition|Eq. (1)]]` from another note. An equation a few lines above needs no link; "Eq. (1)" or "the equation above" is enough there. Derivations in folded callouts follow the same rule, because a callout is often read on its own, long after the equations it uses.

Block IDs contain only lowercase letters, digits and hyphens. Start equation IDs with `eq-` and let them describe the content rather than the number, so that renumbering never breaks a link. A callout or paragraph that will be cited can carry an ID in the same way; for a callout, put the ID on its own line after the callout, separated from it by a blank line. Link a heading (`[[Note title#Section]]`) when the reference is to an argument, and a block ID when it is to a single equation.

## Derivations and callouts

Use Obsidian's foldable callouts selectively for supplementary derivations or questions that would interrupt the main narrative. Keep them focused and concise, letting equations do most of the work. Expand only the steps needed to resolve the specific question, without repeating the main text or introducing tangential material.

If an explanation is essential to following the argument, develop it naturally in the main text rather than hiding it in a callout. When the material becomes too substantial for a single coherent note, consider splitting it into separate, linked notes.

Choose Obsidian's built-in callout types according to their purpose. For example:

- `[!question]-` for genuine conceptual questions or subtle points a reader might wonder about.
- `[!example]-` for supplementary worked examples or calculations.
- `[!note]-` for additional derivations, background explanations, or related physical insights.
- `[!attention]` for brief caveats, important assumptions, or potential pitfalls.

These are suggestions, not rigid categories. Choose whichever presentation feels most natural for the content, without forcing every explanation into a question or every derivation into an example. Use foldable callouts for longer supplementary discussions, while brief notices may remain open.

Preserve Obsidian's existing styling. Do not modify CSS snippets or Obsidian settings unless explicitly requested.

Treat task-specific editorial decisions as local to that task, not as permanent additions to these writing conventions.