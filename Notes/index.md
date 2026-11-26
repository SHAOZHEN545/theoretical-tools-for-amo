---
title: Theoretical Tools for Atomic and Molecular Physics
description: Notes on the theoretical methods that come up again and again in atomic, molecular and optical physics experiments.
---

These notes collect theoretical tools that atomic and molecular physics keeps returning to. Each topic is developed from the start, in the form an experimentalist can use: operators first, matrix elements and familiar special cases at the end, and quick numbers along the way.

## A guide to the notes

### Van Vleck perturbation theory

Atoms and molecules have a hierarchy of energy scales: electronic, vibrational, rotational, fine and hyperfine. An experiment usually cares about a handful of states at one level of that hierarchy, while everything else lies far away. Van Vleck perturbation theory "folds down" the Hilbert space onto those few states and gives an effective Hamiltonian that still remembers the rest.

- [[Van Vleck 00 - Near and far|Near and far]] — The context. Why we fold the Hilbert space down, when two states count as near or far, why folding down is a change of basis, and what an atom does when a field is switched on.
- [[Van Vleck 01 - The effective Hamiltonian|The effective Hamiltonian]] — **The main line**. The unitary rotation that decouples the model space, and the effective Hamiltonian through third order, with the non-degenerate and degenerate formulas as special cases.
- [[Van Vleck 02 - Dressed states and rotated operators|Dressed states and rotated operators]] — What the basis states of the model space stand for, order by order, and why every operator other than the Hamiltonian must be rotated too.
- [[Van Vleck 03 - Errors|Errors]] — How good a truncated effective Hamiltonian is: the small parameter, the cost of stopping, how exact the averaged denominators are, and when the folding fails.
- [[Van Vleck 04 - Symmetries|Symmetries]] — Why the effective Hamiltonian inherits the symmetries of the full one, and what that asks of the model space.

## Browsing the notes

Use the note explorer or search to find a topic. Hover over a shortened explorer entry to see its full title, or over an internal link in the text to preview the linked note. The right sidebar contains the page outline and backlinks. The sidebar buttons let you hide either panel while reading.

> [!info] Derivations and remarks
> Click a folded callout to expand a derivation, an example or a remark. The main text reads on without them.
