---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

Most of the time we care about only a handful of states. In a precision measurement on a molecule, for instance, these are the few spin sublevels of one electronic, vibrational and rotational level. Everything else, from excited electronic states to other rotational levels, lies far away.

The far-away states still matter. The perturbations we care about connect our handful of states to them, and these brief virtual excursions shift and split the levels we measure. We would like a Hamiltonian that acts only on the handful of states and still knows about the excursions.

Van Vleck perturbation theory builds one. Call the span of our handful of states $P$ and the span of everything else $Q$. Both are spanned by eigenstates of the unperturbed Hamiltonian $H_0$, so only the perturbation $V$ connects them. Written in blocks, $P$ first, the theory finds a unitary transformation $e^{A}$ that removes the connection:

$$
H=\begin{pmatrix}H_{PP}&V_{PQ}\\V_{QP}&H_{QQ}\end{pmatrix}
\quad\longrightarrow\quad
e^{A}He^{-A}=\begin{pmatrix}H_{\rm eff}&0\\0&\tilde H_{QQ}\end{pmatrix} .
$$

The rotated Hamiltonian has the same spectrum, and in it our states no longer talk to the rest. We may then simply discard the rest. What survives is $H_{\rm eff}$, which acts on $P$ alone and remembers the excursions through the rotation.

The procedure is often called "folding down" the Hilbert space. In condensed-matter physics the same construction is known as the Schrieffer–Wolff transformation.

Whether it works depends on one comparison, and the same comparison tells us which states belong in $P$.

## Two levels

Every perturbative statement rests on this comparison. Take two eigenstates of $H_0$ with energies $E_1$ and $E_2$, and let the perturbation couple them with a matrix element $v$. The exact energies are

$$
E_\pm=\frac{E_1+E_2}{2}\pm\sqrt{\Big(\frac{E_1-E_2}{2}\Big)^2+|v|^2}=\frac{E_1+E_2}{2}\pm\frac{|E_1-E_2|}{2}\sqrt{1+4\theta^2},
$$

where

$$
\theta=\frac{|v|}{|E_1-E_2|}
$$

is the coupling over the distance. This one ratio decides how the two levels behave.

When $\theta\ll1$, we may expand the square root. Each level is pushed away from the other by $|v|^2/|E_1-E_2|$, a fraction $\theta^2$ of their distance, and each eigenstate takes in the other with an amplitude of size $\theta$. In [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|the derivation]] this amplitude returns as the angle by which the rotation turns each state of $P$ toward each state of $Q$.

When $\theta$ is of order one, the two states mix completely, and no expansion in $v$ can describe that: the series diverges as soon as $\theta>1/2$. We have to diagonalize the $2\times2$ problem as it stands.

So near and far are not properties of the spectrum alone. They compare an energy difference with a coupling. Two states are far apart, for a given perturbation, when their coupling is small compared with their energy difference. They are degenerate when their energies are equal, and nearly degenerate when the difference is not large compared with the coupling.

The same pair of levels can be both. The $N=0$ and $N=1$ levels of a polar molecule lie about a GHz apart. For the nuclear-spin couplings, at most a few hundred MHz, they are far apart. A static field of 1 kV/cm couples them by about twice their spacing, and for that perturbation they are nearly degenerate.
## What goes into the model space

The strategy follows. We put into a model space $P$ the states we care about, together with every state that is near them, and we treat all couplings among these exactly. Every other state must be far from all states of $P$, and those we fold away perturbatively. Inside $P$ nothing needs to be far.

The familiar theories are special cases. Non-degenerate perturbation theory is the case of a model space with a single state; its requirement that no other level come close is our requirement on everything outside. Degenerate perturbation theory is the case of a model space with one degenerate level. Van Vleck's construction covers both, and everything in between, with one set of formulas.

[[Van Vleck perturbation theory and the effective Hamiltonian]] derives that set of formulas through third order. It works with operators throughout and assumes nothing about the energies inside $P$, so the matrix elements, and the non-degenerate and degenerate formulas, come out at the end as special cases.

[[Van Vleck perturbation theory - dressed states, errors and symmetries]] takes up the questions the formulas leave open: what the states of the model space stand for, what becomes of other operators, how exact the energy denominators are, where the errors come from, and why symmetries survive. Its last question, when the folding fails, brings us back to the decision made here.
