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

The rotated Hamiltonian has the same spectrum, and in it our states no longer talk to the rest. We may then simply discard the rest. What survives is $H_{\rm eff}$, which acts on $P$ alone and remembers the excursions through the rotation. What the rotation does to the states, and why discarding the rest is legitimate, is taken up in [[#A change of basis]].

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

## A change of basis

Folding down rests on one idea from elementary quantum mechanics: a unitary transformation is a change of basis. It pays to make this precise, because it tells us how to read everything that follows.

A unitary operator $U$, with $U^\dagger U=1$, carries an orthonormal basis into another orthonormal basis. We can use it in two ways. In the *active* view, $U$ moves every state, $|\psi\rangle\to U|\psi\rangle$, and every operator along with it, $O\to UOU^\dagger$, while the basis stays where it was. In the *passive* view nothing moves. The states and operators stay what they are, and we describe them in a new basis. Both views give the same numbers, and we use the passive one. It keeps the physics fixed: the atom and its Hamiltonian $H=H_0+V$ are what they are, and only our description of them changes.

Van Vleck theory writes the unitary operator as $e^{A}$, with $A^\dagger=-A$. We start from the eigenstates of $H_0$, the *bare* states $|a\rangle$ of $P$ and $|\alpha\rangle$ of $Q$, and define the *dressed* states

$$
|\tilde a\rangle=e^{-A}|a\rangle,\qquad|\tilde\alpha\rangle=e^{-A}|\alpha\rangle .
$$
^eq-dressed-states

They are orthonormal again, because $e^{-A}$ is unitary. Their bras are $\langle\tilde a|=\langle a|\big(e^{-A}\big)^\dagger=\langle a|e^{A}$, so the Hamiltonian has the matrix elements

$$
\langle\tilde a|H|\tilde b\rangle=\langle a|e^{A}He^{-A}|b\rangle
$$
^eq-dressed-matrix-elements

in the dressed basis, and likewise between any other pair of basis states. Nothing here is special to $H$; every operator obeys the same identity.

This settles the question of which basis the rotated Hamiltonian $\tilde H=e^{A}He^{-A}$ belongs to. Written in the old, bare basis, $\tilde H$ has exactly the matrix that the true Hamiltonian $H$ has in the new, dressed basis. We compute with $\tilde H$ in the bare basis, because the bare states are the ones we know. We read the result in the dressed basis, because that is what it describes. (In the active view the roles are exchanged: $e^{A}$ moves the states and the Hamiltonian, and we keep looking in the bare basis. The numbers are the same.)

A state is described by its components, and in the dressed basis these are $\langle\tilde a|\psi\rangle=\langle a|e^{A}|\psi\rangle$, the bare components of $e^{A}|\psi\rangle$. The eigenvalue equation therefore reads the same in either basis. Multiplying $H|\psi\rangle=E|\psi\rangle$ by $e^{A}$ and inserting $1=e^{-A}e^{A}$ after $H$,

$$
e^{A}He^{-A}\,e^{A}|\psi\rangle=E\,e^{A}|\psi\rangle,\qquad\text{that is,}\qquad\tilde H\big(e^{A}|\psi\rangle\big)=E\big(e^{A}|\psi\rangle\big).
$$

$\tilde H$ has the eigenvalues of $H$, and its eigenvectors are the eigenstates of $H$, written in the dressed basis.

Now the point of the construction. We choose $A$ so that $\tilde H$ has no matrix elements between $P$ and $Q$. In the dressed basis this reads

$$
\langle\tilde\alpha|H|\tilde a\rangle=0\qquad\text{for every } a\in P,\ \alpha\in Q .
$$

Acting on a dressed state of $P$, the Hamiltonian therefore produces only dressed states of $P$. The true eigenstates that grow out of the model space lie in the span of the $|\tilde a\rangle$, and we find them by diagonalizing the small matrix $\langle\tilde a|H|\tilde b\rangle$. That matrix is $H_{\rm eff}$.

Notice what has not happened. The dressed states are not eigenstates of $H$. Inside $P$ the Hamiltonian still connects them, and those couplings, however strong, are left for the exact diagonalization of $H_{\rm eff}$. Folding down is a block diagonalization, not a full one.

With two levels, one in $P$ and one in $Q$, each block is a single number, and block diagonal means diagonal. The dressed states are then the exact eigenstates of the $2\times2$ problem of [[#Two levels]]. For a real coupling $v$ they are the bare pair rotated by an angle $\varphi$,

$$
|\tilde1\rangle=\cos\varphi\,|1\rangle+\sin\varphi\,|2\rangle,\qquad|\tilde2\rangle=-\sin\varphi\,|1\rangle+\cos\varphi\,|2\rangle,\qquad\tan2\varphi=\frac{2v}{E_1-E_2} .
$$
^eq-two-level-dressed

The angle is the one that removes the off-diagonal element in the rotated basis, $\langle\tilde2|H|\tilde1\rangle=v\cos2\varphi-\tfrac12(E_1-E_2)\sin2\varphi=0$. When the levels are far apart, $\varphi\approx v/(E_1-E_2)$, and each dressed state is its bare state with an admixture of the other, of the size $\theta$ found above. Here $e^{-A}$ is literally a rotation of the plane spanned by $|1\rangle$ and $|2\rangle$, and the name sticks to every unitary transformation of this kind.

## What the atom does

The change of basis is exact algebra, whatever the history of the system. It also describes what an atom actually does.

Take an atom in its ground level and switch on a static electric field. The field couples the ground level to excited levels of opposite parity, hundreds of terahertz away, and the electrons respond on the time scale of the inverse distance, a few femtoseconds. Any field we switch on in the laboratory takes nanoseconds at the very least. Compared with the distance to $Q$ the switching is slow, so the adiabatic theorem applies. A bare state of $P$ turns continuously into a state in the span of the dressed states of $P$, and practically no amplitude ends up in the dressed states of $Q$. With the field on, the atom lives among the dressed states, and the rotation finds the states it has already settled into. Only a switch faster than femtoseconds would leave the atom in its bare state, which is a dressed state of $P$ with a small admixture of the dressed states of $Q$.

The atom settles only with respect to the far states. The adiabatic argument works because the distance to $Q$ is large compared with the rate at which we change things. Inside $P$ that need not hold. The splittings there range from hertz to gigahertz, and the experiment acts on those very time scales: a spin precesses, a superposition of sublevels evolves, a Ramsey sequence prepares one and reads it out. This slow motion is what we want to describe, and $H_{\rm eff}$ generates it. Folding down separates the two time scales. The fast excursions into $Q$, which the atom follows without our help, are built into the dressed states; the slow dynamics inside $P$ is left to $H_{\rm eff}$.

A laboratory field barely polarizes an atom, because the levels of opposite parity are far away: their coupling is small compared with their distance, so the dressing is a small admixture, and folding them away is safe. In a polar molecule the levels of opposite parity are only about a GHz apart, and 1 kV/cm mixes them completely. They cannot be folded away. They belong in $P$, and the polarization of the molecule is computed exactly, by diagonalizing $H_{\rm eff}$.

## The notes that follow

[[Van Vleck perturbation theory and the effective Hamiltonian]] is the main line. It finds the generator $A$ order by order and derives $H_{\rm eff}$ through third order. It works with operators throughout and assumes nothing about the energies inside $P$, so the matrix elements, and the non-degenerate and degenerate formulas, come out at the end as special cases.

Three notes take up what the main line sets aside. [[Van Vleck perturbation theory - dressed states and rotated operators|Dressed states and rotated operators]] follows the dressed states order by order and explains why every operator other than $H$ must be rotated too. [[Van Vleck perturbation theory - errors|Errors]] estimates what a truncated $H_{\rm eff}$ gets wrong, and ends with the question of when the folding fails, which brings us back to the decision made here. [[Van Vleck perturbation theory - symmetries|Symmetries]] explains why $H_{\rm eff}$ inherits the symmetries of $H$, which often fixes its form before any calculation.
