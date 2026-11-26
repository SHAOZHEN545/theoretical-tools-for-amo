---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

Most of the time we care about only a handful of states. In a precision measurement on a molecule, for instance, these are the few spin sublevels of one electronic, vibrational and rotational level. Everything else, from excited electronic states to other rotational levels, lies far away.

The far-away states still matter. The perturbations we care about connect our handful of states to them, and these brief virtual excursions shift and split the levels we measure. We would like a Hamiltonian that acts only on the handful of states and still knows about the excursions.

Van Vleck perturbation theory builds one by choosing a better basis in which to write the Hamiltonian. The construction is often called "folding down" the Hilbert space; in condensed-matter physics it is known as the Schrieffer–Wolff transformation. What the better basis is, and why it gives us such a Hamiltonian, is the subject of [[#The Hamiltonian as a matrix]] and [[#A change of basis]]. First we have to decide which states to keep, and that decision rests on one comparison.

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

When $\theta\ll1$, we may expand the square root. Each level is pushed away from the other by $|v|^2/|E_1-E_2|$, a fraction $\theta^2$ of their distance, and each eigenstate takes in the other with an amplitude of size $\theta$. In [[Van Vleck 01 - The effective Hamiltonian#Solving for the generator|the effective Hamiltonian]] this amplitude returns as the angle by which the new basis turns each state of $P$ toward each state of $Q$.

When $\theta$ is of order one, the two states mix completely, and no expansion in $v$ can describe that: the series diverges as soon as $\theta>1/2$. We have to diagonalize the $2\times2$ problem as it stands.

So near and far are not properties of the spectrum alone. They compare an energy difference with a coupling. Two states are far apart, for a given perturbation, when their coupling is small compared with their energy difference. They are degenerate when their energies are equal, and nearly degenerate when the difference is not large compared with the coupling.

The same pair of levels can be both. The $N=0$ and $N=1$ levels of a polar molecule lie about a GHz apart. For the nuclear-spin couplings, at most a few hundred MHz, they are far apart. A static field of 1 kV/cm couples them by about twice their spacing, and for that perturbation they are nearly degenerate.

## What goes into the model space

The strategy follows. We put into a model space $P$ the states we care about, together with every state that is near them, and we treat all couplings among these exactly. Every other state must be far from all states of $P$, and those we fold away perturbatively. Inside $P$ nothing needs to be far.

The familiar theories are special cases. Non-degenerate perturbation theory is the case of a model space with a single state; its requirement that no other level come close is our requirement on everything outside. Degenerate perturbation theory is the case of a model space with one degenerate level. Van Vleck's construction covers both, and everything in between, with one set of formulas.

## The Hamiltonian as a matrix

The Hamiltonian is an operator, a linear map on the Hilbert space, like every other observable, and as an operator it knows nothing about bases. A matrix does. Once we pick an orthonormal basis $B=\{|i\rangle\}$, an operator $O$ is represented by the array of numbers

$$
[O]_B,\qquad\big([O]_B\big)_{ij}=\langle i|O|j\rangle .
$$
^eq-representation

One operator has as many matrices as there are bases, and they look different. Whether a matrix is diagonal, or block diagonal, is a property of the matrix, so the question makes sense only once the basis is named.

The natural basis is the one we know: the eigenstates of $H_0$, which we call the *bare* states. Those in the model space are $|a\rangle,|b\rangle,\dots$, with energies $E_a,E_b,\dots$; those outside are $|\alpha\rangle,|\beta\rangle,\dots$, with energies $E_\alpha,E_\beta,\dots$. The projectors onto the two sets are $P$ and $Q$. Listing the states of $P$ first, the matrix of $H=H_0+V$ in the bare basis falls into four blocks,

$$
[H]_{\rm bare}=\begin{pmatrix}H_{PP}&V_{PQ}\\V_{QP}&H_{QQ}\end{pmatrix} ,
$$

where $H_{PP}$ collects the elements $\langle a|H|b\rangle$, $V_{PQ}$ the elements $\langle a|V|\beta\rangle$, and so on. Only $V$ appears in the off-diagonal blocks, because $H_0$ has no elements between its own eigenstates: $\langle a|H_0|\beta\rangle=E_\beta\langle a|\beta\rangle=0$.

This matrix is not block diagonal, and the reason is the basis. The bare states are eigenstates of $H_0$, not of $H$, and in this basis $V$ ties the states we keep to the rest of the world through the blocks $V_{PQ}$ and $V_{QP}$.

So we look for another basis, one in which these blocks vanish. We do not ask for a diagonal matrix. The couplings inside $P$ may stay, since we will diagonalize that small block exactly at the end. We ask only that the matrix be block diagonal, at least to the order of perturbation theory we work at:

$$
[H]_{\rm new}=\begin{pmatrix}H_{\rm eff}&0\\0&\ast\end{pmatrix} .
$$

This is what folding down means. In the new basis the states that *grow* out of $P$ no longer talk to the rest, and we may discard the block marked $\ast$. What survives is $H_{\rm eff}$, a Hamiltonian for the model space alone, which remembers the far states through the choice of basis.

## A change of basis

Any two orthonormal bases are related by a unitary operator. Van Vleck theory writes it as $e^{-A}$, with $A$ anti-Hermitian, $A^\dagger=-A$, and defines the new basis states

$$
|\tilde a\rangle=e^{-A}|a\rangle,\qquad|\tilde\alpha\rangle=e^{-A}|\alpha\rangle .
$$
^eq-dressed-states

We call them *dressed* states. The Hamiltonian itself is untouched; we have only picked another basis of the same Hilbert space in which to write it.

Each dressed state keeps the label of the bare state it came from, and the labels carry the split into $P$ and $Q$ over to the new basis. The dressed states $|\tilde a\rangle$ span a subspace $\tilde P$, and the $|\tilde\alpha\rangle$ span its complement $\tilde Q$. Their projectors are

$$
\tilde P=\sum_a|\tilde a\rangle\langle\tilde a|=e^{-A}Pe^{A},\qquad\tilde Q=\sum_\alpha|\tilde\alpha\rangle\langle\tilde\alpha|=e^{-A}Qe^{A} .
$$
^eq-dressed-subspaces

The generator $A$ will be built to vanish when $V$ does, so for a weak perturbation $\tilde P$ is $P$ tilted slightly toward $Q$. This is what it means for states to grow out of $P$: as $V$ is turned up from zero, each $|a\rangle$ turns continuously into $|\tilde a\rangle$, and $P$ into $\tilde P$. In this language, folding down asks for the dressed basis in which $H$ does not connect $\tilde P$ to $\tilde Q$,

$$
\tilde PH\tilde Q=0 .
$$

To find it we need the matrix of $H$ in the dressed basis. The bras of the dressed states are $\langle\tilde a|=\langle a|\big(e^{-A}\big)^\dagger=\langle a|e^{A}$, so for any two labels $i,j$, from either part,

$$
\langle\tilde i|H|\tilde j\rangle=\langle i|e^{A}He^{-A}|j\rangle .
$$
^eq-dressed-matrix-elements

This identity is what makes the construction work, and it is worth reading slowly. We do not know the dressed basis yet; finding it is the whole problem. The right-hand side, however, involves only the bare states, which we do know, and the operator

$$
\tilde H=e^{A}He^{-A} .
$$

Read as a statement about matrices, the identity says that the matrix of $H$ in the dressed basis is the matrix of $\tilde H$ in the bare basis, block by block:

$$
[H]_{\rm dressed}=\begin{pmatrix}\langle\tilde a|H|\tilde b\rangle&\langle\tilde a|H|\tilde\beta\rangle\\langle\tilde\alpha|H|\tilde b\rangle&\langle\tilde\alpha|H|\tilde\beta\rangle\end{pmatrix}=\begin{pmatrix}\langle a|\tilde H|b\rangle&\langle a|\tilde H|\beta\rangle\\langle\alpha|\tilde H|b\rangle&\langle\alpha|\tilde H|\beta\rangle\end{pmatrix}=[\tilde H]_{\rm bare} .
$$
^eq-dressed-equals-bare

So $\tilde H$ is not a second Hamiltonian; there is only one, $H$. $\tilde H$ is the table of numbers that $H$ has in the dressed basis, attached to the bare kets and bras so that we have something to calculate with:

$$
\tilde H=\sum_{i,j}|i\rangle\,\langle\tilde i|H|\tilde j\rangle\,\langle j| .
$$

Inserting [[#^eq-dressed-matrix-elements|the identity]] and the completeness of the bare basis, $\sum_i|i\rangle\langle i|=1$, turns the right-hand side back into $e^{A}He^{-A}$. The bare kets serve only as labels: row $i$ of $[\tilde H]_{\rm bare}$ belongs to the dressed state $|\tilde i\rangle$. Following the literature we call $\tilde H$ the *rotated Hamiltonian*.

The same correspondence holds for the blocks as operators. Sandwiching $H$ between the dressed projectors of [[#^eq-dressed-subspaces|the subspaces above]],

$$
\tilde PH\tilde P=e^{-A}Pe^{A}\,H\,e^{-A}Pe^{A}=e^{-A}\big(P\tilde HP\big)e^{A},\qquad\tilde PH\tilde Q=e^{-A}\big(P\tilde HQ\big)e^{A},
$$

and likewise for the other two blocks. Each block of $H$ with respect to $\tilde P$ and $\tilde Q$ is the matching block of $\tilde H$ with respect to $P$ and $Q$, carried over by $e^{-A}$. In particular

$$
\tilde PH\tilde Q=0\qquad\Longleftrightarrow\qquad P\tilde HQ=0 .
$$

The right-hand side is a condition on the known subspaces $P$ and $Q$, and it is the condition we will solve. The $P$ block of $\tilde H$ is the effective Hamiltonian,

$$
H_{\rm eff}=P\tilde HP,\qquad\langle a|H_{\rm eff}|b\rangle=\langle\tilde a|H|\tilde b\rangle .
$$
^eq-heff-definition

$H_{\rm eff}$ is an operator on the bare space $P$, and we diagonalize it there. What do its eigenvectors tell us about $H$? Take one, expanded in bare states,

$$
H_{\rm eff}|\varphi\rangle=E|\varphi\rangle,\qquad|\varphi\rangle=\sum_bc_b|b\rangle .
$$

In components this reads $\sum_b\langle a|H_{\rm eff}|b\rangle\,c_b=E\,c_a$, and by the definition of $H_{\rm eff}$,

$$
\sum_b\langle\tilde a|H|\tilde b\rangle\,c_b=E\,c_a .
$$

Now put the same coefficients on the dressed states, $|\psi\rangle=\sum_bc_b|\tilde b\rangle=e^{-A}|\varphi\rangle$. Its components in the dressed basis are $\langle\tilde a|\psi\rangle=c_a$ and $\langle\tilde\alpha|\psi\rangle=0$. Those of $H|\psi\rangle$ follow from the equation above and from $\tilde PH\tilde Q=0$:

$$
\langle\tilde a|H|\psi\rangle=\sum_b\langle\tilde a|H|\tilde b\rangle\,c_b=E\,c_a,\qquad\langle\tilde\alpha|H|\psi\rangle=\sum_b\langle\tilde\alpha|H|\tilde b\rangle\,c_b=0 .
$$

Every component of $H|\psi\rangle$ is $E$ times the same component of $|\psi\rangle$, so

$$
H|\psi\rangle=E|\psi\rangle .
$$
^eq-heff-eigenstates

The eigenvalues of $H_{\rm eff}$ are eigenvalues of $H$, and an eigenvector $\sum_bc_b|b\rangle$ of $H_{\rm eff}$ gives the eigenstate $\sum_bc_b|\tilde b\rangle$ of $H$: the same coefficients, on the dressed states instead of the bare ones. [[Van Vleck 01 - The effective Hamiltonian|The effective Hamiltonian]] finds $A$ order by order from the condition $P\tilde HQ=0$.

> [!question]- Can the $P$ block pick up eigenvalues that do not belong to it?
> If $H$ is exactly block diagonal in the dressed basis, every eigenvalue of $H_{\rm eff}$ is an exact eigenvalue of $H$, as we have just seen. The real question is which eigenvalues end up in $P$.
>
> Block diagonality alone does not decide that. A large enough change of basis could swap a state of $P$ with one of $Q$ and still leave the matrix block diagonal. Van Vleck theory rules this out by building $A$ as a power series in $V$ that vanishes when $V$ does. At $V=0$ the $P$ block holds exactly the energies $E_a$, and as $V$ grows every eigenvalue moves continuously. For an eigenvalue to pass from one block to the other, a state of $Q$ would have to come close to a state of $P$, which is what the choice of [[#What goes into the model space|the model space]] forbids. The $P$ block therefore holds the eigenvalues of $H$ that grow out of the $E_a$, the same ones an exact diagonalization assigns to the model space.
>
> In practice we stop the series at some order, and the eigenvalues of the truncated $H_{\rm eff}$ differ from those exact eigenvalues by terms of the first order we left out. [[Van Vleck 03 - Errors|Errors]] estimates them. When a state of $Q$ does come close, the series stops converging, and the cure is to move that state into $P$.

With two levels, one in $P$ and one in $Q$, each block is a single number, and block diagonal means diagonal. The dressed states are then the exact eigenstates of the $2\times2$ problem of [[#Two levels]]. For a real coupling $v$ they are the bare pair rotated by an angle $\varphi$,

$$
|\tilde1\rangle=\cos\varphi\,|1\rangle+\sin\varphi\,|2\rangle,\qquad|\tilde2\rangle=-\sin\varphi\,|1\rangle+\cos\varphi\,|2\rangle,\qquad\tan2\varphi=\frac{2v}{E_1-E_2} .
$$
^eq-two-level-dressed

The angle is the one that removes the off-diagonal element in the new basis, $\langle\tilde2|H|\tilde1\rangle=v\cos2\varphi-\tfrac12(E_1-E_2)\sin2\varphi=0$. When the levels are far apart, $\varphi\approx v/(E_1-E_2)$, and each dressed state is its bare state with an admixture of the other, of the size $\theta$ found above. Here $e^{-A}$ is literally a rotation of the plane spanned by $|1\rangle$ and $|2\rangle$, which is where the name of the rotated Hamiltonian comes from.

With more than one state in $P$, block diagonal is no longer diagonal. The dressed states of $P$ are not eigenstates of $H$: inside $P$ the Hamiltonian still connects them, and those couplings, however strong, are left for the exact diagonalization of $H_{\rm eff}$. The example below shows the two steps in the smallest system where they differ.

> [!example]- Three states
> Take two degenerate states in the model space, $|1\rangle$ and $|2\rangle$ at energy $0$, and one far state $|3\rangle$ at $\Delta$, coupled to them by real matrix elements $v_1,v_2\ll\Delta$. This is a far-detuned $\Lambda$ system. In the bare basis, with the $P$ states first,
>
> $$
> [H]_{\rm bare}=\left(\begin{array}{cc|c}0&0&v_1\\0&0&v_2\\\hline v_1&v_2&\Delta\end{array}\right).
> $$
>
> The off-diagonal blocks are of first order. To first order, each dressed state leans toward the other block by its coupling over its distance, by the rule of [[Van Vleck 01 - The effective Hamiltonian#Solving for the generator|the effective Hamiltonian]]:
>
> $$
> |\tilde1\rangle\approx|1\rangle-\frac{v_1}{\Delta}|3\rangle,\qquad|\tilde2\rangle\approx|2\rangle-\frac{v_2}{\Delta}|3\rangle,\qquad|\tilde3\rangle\approx|3\rangle+\frac{v_1|1\rangle+v_2|2\rangle}{\Delta}.
> $$
>
> To get the matrix of $H$ in this basis, let $H$ act on a dressed state. The admixture of $|3\rangle$ cancels:
>
> $$
> H|\tilde1\rangle=H|1\rangle-\frac{v_1}{\Delta}H|3\rangle=v_1|3\rangle-\frac{v_1}{\Delta}\big(v_1|1\rangle+v_2|2\rangle+\Delta|3\rangle\big)=-\frac{v_1}{\Delta}\big(v_1|1\rangle+v_2|2\rangle\big).
> $$
>
> Projecting onto the dressed bras gives $\langle\tilde1|H|\tilde1\rangle=-v_1^2/\Delta$ and $\langle\tilde2|H|\tilde1\rangle=-v_1v_2/\Delta$, while $\langle\tilde3|H|\tilde1\rangle$ is of order $v^3/\Delta^2$. Doing the same for $|\tilde2\rangle$,
>
> $$
> [H]_{\rm dressed}\approx\left(\begin{array}{cc|c}-v_1^2/\Delta&-v_1v_2/\Delta&O(v^3/\Delta^2)\\-v_1v_2/\Delta&-v_2^2/\Delta&O(v^3/\Delta^2)\\\hline O(v^3/\Delta^2)&O(v^3/\Delta^2)&\Delta+O(v^2/\Delta)\end{array}\right).
> $$
>
> The coupling between the blocks has dropped from first order to third. The $P$ block is $H_{\rm eff}$, and it is not diagonal. Diagonalizing it is the second, exact step: the dark state $v_2|1\rangle-v_1|2\rangle$ has the eigenvalue $0$, and the bright state $v_1|1\rangle+v_2|2\rangle$ has $-(v_1^2+v_2^2)/\Delta$, its light shift. The $3\times3$ matrix agrees. The dark state is an exact eigenstate at $0$, and the lower of the other two eigenvalues is $-(v_1^2+v_2^2)/\Delta+O(v^4/\Delta^3)$.

## What the atom does

The change of basis is exact algebra, whatever the history of the system. It also describes what an atom actually does.

Take an atom in its ground level and switch on a static electric field. The field couples the ground level to excited levels of opposite parity, hundreds of terahertz away, and the electrons respond on the time scale of the inverse distance, a few femtoseconds. Any field we switch on in the laboratory takes nanoseconds at the very least. Compared with the distance to $Q$ the switching is slow, so the adiabatic theorem applies. A bare state of $P$ turns continuously into a state in the span of the dressed states of $P$, and practically no amplitude ends up in the dressed states of $Q$. With the field on, the atom lives among the dressed states: the dressed basis is made of the states it has already settled into. Only a switch faster than femtoseconds would leave the atom in its bare state, which is a dressed state of $P$ with a small admixture of the dressed states of $Q$.

The atom settles only with respect to the far states. The adiabatic argument works because the distance to $Q$ is large compared with the rate at which we change things. Inside $P$ that need not hold. The splittings there range from hertz to gigahertz, and the experiment acts on those very time scales: a spin precesses, a superposition of sublevels evolves, a Ramsey sequence prepares one and reads it out. This slow motion is what we want to describe, and $H_{\rm eff}$ generates it. Folding down separates the two time scales. The fast excursions into $Q$, which the atom follows without our help, are built into the dressed states; the slow dynamics inside $P$ is left to $H_{\rm eff}$.

A laboratory field barely polarizes an atom, because the levels of opposite parity are far away: their coupling is small compared with their distance, so the dressing is a small admixture, and folding them away is safe. In a polar molecule the levels of opposite parity are only about a GHz apart, and 1 kV/cm mixes them completely. They cannot be folded away. They belong in $P$, and the polarization of the molecule is computed exactly, by diagonalizing $H_{\rm eff}$.

## The notes that follow

[[Van Vleck 01 - The effective Hamiltonian|The effective Hamiltonian]] is the main line. It finds the generator $A$ order by order from the condition $P\tilde HQ=0$ and derives $H_{\rm eff}$ through third order. It works with operators throughout and assumes nothing about the energies inside $P$, so the matrix elements, and the non-degenerate and degenerate formulas, come out at the end as special cases.

Three notes take up what the main line sets aside. [[Van Vleck 02 - Dressed states and rotated operators|Dressed states and rotated operators]] follows the dressed states order by order and explains why every operator other than $H$ must be rotated too. [[Van Vleck 03 - Errors|Errors]] estimates what a truncated $H_{\rm eff}$ gets wrong, and ends with the question of when the folding fails, which brings us back to the decision made here. [[Van Vleck 04 - Symmetries|Symmetries]] explains why $H_{\rm eff}$ inherits the symmetries of $H$, which often fixes its form before any calculation.
