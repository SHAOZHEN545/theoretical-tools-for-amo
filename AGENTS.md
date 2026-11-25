# Markdown math formatting

Use $...$ for inline math and $$...$$ for display math in Markdown files and Markdown code blocks. Do not use backslash-parenthesis or backslash-bracket math delimiters there.

Preserve Obsidian wikilinks, native callouts, and the shared figure syntax. Prefer existing Obsidian and Quartz capabilities over custom rendering code. Keep notes and attachments inside Notes/, one subfolder per topic.

## Scope

This repository is public. It holds generic theoretical tools for atomic and molecular physics, written as self-contained tutorials. Do not copy in anything about unpublished experimental work, and do not link to notes that live only in other repositories: every cross-reference must point to a note inside Notes/, or be replaced by a short self-contained explanation.

Numerical checks of the notes live in checks/ and are linked from the notes by their GitHub URL, because the website only publishes Notes/. Scripts that draw the figures live in figures/ and write SVGs into the Pictures/ folder of their topic; keep their output reproducible (text as paths, a fixed svg.hashsalt, no date).

Notes follow the pedagogical-notes skill in .claude/skills/, including its rule for equation block IDs and block links.

## Website

The website setup (Quartz 5.0.0, GitHub Pages, GitHub Actions) is copied from the sibling repository scattering-theory-for-ultracold, including its small Quartz adaptations; its BUILD_PLAN.md records why each one exists. Keep the two setups in step when either is fixed. The user uploads the repository to GitHub; do not create or push a remote on their behalf unless asked.
