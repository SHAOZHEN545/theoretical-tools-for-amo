---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

[[Van Vleck 01 - The effective Hamiltonian|The effective Hamiltonian]] rotates the Hamiltonian, $\tilde H=e^{A}He^{-A}$, and keeps its $P$ block. As [[Van Vleck 00 - Near and far#A change of basis|near and far]] explains, the rotation is a change of basis: written in the bare basis, $\tilde H$ is the true Hamiltonian $H$ written in a basis of dressed states. The main line never needed those states. Here we look at them, and at what they mean for every operator other than $H$.

The notation is that of the derivation. $P$ and $Q$ are spanned by eigenstates $|a\rangle,|b\rangle,\dots$ and $|\alpha\rangle,|\beta\rangle,\dots$ of $H_0$, $A=A_1+A_2+\cdots$ is the anti-Hermitian generator, $H_{\rm eff}=P\tilde HP$, and $R(E)=Q/(E-H_0)$. Equation numbers refer to the derivation and link to it.

## What the model states stand for

Each bare state $|a\rangle$ of the model space labels a dressed state, defined in [[Van Vleck 00 - Near and far#A change of basis|near and far]],

$$
|\tilde a\rangle=e^{-A}|a\rangle ,
$$

and the matrix elements of the effective Hamiltonian are those of the true Hamiltonian between dressed states,

$$
\langle a|H_{\rm eff}|b\rangle=\langle a|e^{A}He^{-A}|b\rangle=\langle\tilde a|H|\tilde b\rangle .
$$
^eq-heff-dressed

As [[Van Vleck 00 - Near and far#^eq-heff-eigenstates|near and far]] shows, an eigenvector $\sum_ac_a|a\rangle$ of $H_{\rm eff}$, with eigenvalue $E$, gives the eigenstate $\sum_ac_a|\tilde a\rangle=e^{-A}\sum_ac_a|a\rangle$ of $H$ with the same eigenvalue. The coefficients $c_a$ are what we compute inside $P$; the dressing is common to all eigenvectors and is carried by $e^{-A}$. The argument uses only the block diagonality, so it holds to the order at which we stop the series for $A$.

The dressed states themselves are not eigenstates of $H$. They form the basis in which $H$ no longer connects $P$ to $Q$, while inside $P$ it still has matrix elements between them, and diagonalizing $H_{\rm eff}$ takes care of those. Only when $P$ holds a single state is its dressed state an eigenstate, as for the two levels of [[Van Vleck 00 - Near and far#^eq-two-level-dressed|near and far]].

### The first-order dressing

To first order only $A_1$ acts, and by [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]], $A_1|a\rangle=-R(E_a)V|a\rangle$. So

$$
\begin{aligned}
|\tilde a\rangle&=|a\rangle+R(E_a)V|a\rangle+O(V^2)\\
&=|a\rangle+\sum_{\alpha\in Q}|\alpha\rangle\,\frac{\langle\alpha|V|a\rangle}{E_a-E_\alpha}+O(V^2) .
\end{aligned}
$$
^eq-dressing-first-order

Each model state takes in every external state, with an amplitude equal to its rotation angle, coupling over distance. This is the first-order state of Rayleigh–Schrödinger theory, now attached to every state of $P$ at once.

### The second-order dressing

At second order the dressing reaches back into $P$. With $e^{-A}=1-A+\tfrac12A^2-\cdots$ and $A=A_1+A_2+\cdots$,

$$
|\tilde a\rangle=|a\rangle-A_1|a\rangle-A_2|a\rangle+\tfrac12A_1^2|a\rangle+O(V^3) .
$$
^eq-dressing-second-order

The terms with one generator lie in $Q$, because an off-diagonal operator carries $P$ into $Q$. Two generators carry $|a\rangle$ out and back, and [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]] applied twice gives

$$
\tfrac12A_1^2|a\rangle=-\frac12\sum_{b\in P}|b\rangle\,\langle b|V\,R(E_b)R(E_a)\,V|a\rangle .
$$

Its component along $|a\rangle$ itself is $-\tfrac12w_a$, where

$$
w_a=\langle a|V\,R(E_a)^2\,V|a\rangle=\sum_{\alpha\in Q}\frac{|\langle\alpha|V|a\rangle|^2}{(E_a-E_\alpha)^2}
$$

is the squared norm of the first-order admixture. The two pieces balance. The dressed state keeps unit norm, and the weight it gains in $Q$ is taken from its weight in $P$:

$$
\big\|Q|\tilde a\rangle\big\|^2=w_a,\qquad\big\|P|\tilde a\rangle\big\|^2=1-w_a ,
$$

up to terms of third order. So $w_a$ is the probability of finding the system outside the model space. It is the natural measure of how strongly the folding disturbs a state, and it sets the size of the errors in [[Van Vleck 03 - Errors#The small parameter|errors]].

The components along the other model states, $-\tfrac12\langle b|VR(E_b)R(E_a)V|a\rangle$, have the same origin. The admixtures of $|a\rangle$ and $|b\rangle$ overlap in $Q$, by $\langle a|VR(E_a)R(E_b)V|b\rangle$, and the two dressed states remain orthogonal only because their parts in $P$ lean away from each other by half that overlap each.

> [!question]- Are the eigenvectors of $H_{\rm eff}$ the projections of the true eigenstates?
> Not quite. If $|\psi\rangle=e^{-A}|\varphi\rangle$ is a true eigenstate, its projection onto the model space is
>
> $$
> P|\psi\rangle=M|\varphi\rangle,\qquad M\equiv Pe^{-A}P=P\cosh A\,P .
> $$
>
> Only even powers of the off-diagonal $A$ survive between two $P$'s, and since $A^2=-A^\dagger A$, $M$ is Hermitian. To second order, $M=P-\tfrac12\sum_{a,b}P_aVR(E_a)R(E_b)VP_b$. The projections are therefore shorter than the van Vleck eigenvectors, and the projections of different eigenstates are not orthogonal: their overlaps are $\langle\varphi_k|M^2|\varphi_l\rangle$.
>
> Because $M$ is Hermitian, the van Vleck eigenvectors follow from the projections by removing their overlap symmetrically,
>
> $$
> |\varphi_k\rangle=\sum_lP|\psi_l\rangle\,\big[G^{-1/2}\big]_{lk},\qquad G_{kl}=\langle\psi_k|P|\psi_l\rangle ,
> $$
>
> to all orders. This is Löwdin's symmetric orthonormalization. [`check_van_vleck_states_errors.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck_states_errors.py) confirms it numerically. The operator $\sum_kE_k|\varphi_k\rangle\langle\varphi_k|$ built in this way from exact eigenstates agrees with $H_{\rm eff}$ through third order up to terms of fourth order. The operator built from the bare projections, Bloch's effective Hamiltonian, is not Hermitian and differs already at second order. The distinction matters only when we ask for the weight of a particular model state in a true eigenstate, which is a second-order question.

^projections

## The averaged denominators, seen from the states

[[Van Vleck 01 - The effective Hamiltonian#^eq-h2|Eq. (5)]] measures the distance of each intermediate state once from the energy of the bra's state and once from that of the ket's state, and takes the average. The derivation traced the two energies to the two terms of a commutator. The dressed states give a more natural picture.

By [[#^eq-heff-dressed|the identity above]], a matrix element of $H_{\rm eff}$ is a matrix element of $H$ with a dressed state at each end. By the first-order dressing, each end is dressed with denominators measured from its own energy. So the element carries both energies, and it carries them symmetrically. The callout below checks that the two dressings combine into exactly the average.

Hermiticity comes out the same way, without being imposed. Both ends of every matrix element are dressed in the same way, so $\langle\tilde a|H|\tilde b\rangle^*=\langle\tilde b|H|\tilde a\rangle$ automatically.

> [!note]- The average from the dressed states
> Take the [[#^eq-dressing-second-order|second-order dressing]] of $|\tilde b\rangle$ and write $R_b\equiv R(E_b)$. By [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]], $-A_1|b\rangle=R_bV|b\rangle$ lies in $Q$, while
>
> $$
> \tfrac12A_1^2|b\rangle=-\frac12\sum_{c\in P}|c\rangle\langle c|VR_cR_bV|b\rangle
> $$
>
> lies in $P$ and keeps $|\tilde b\rangle$ normalized. The term $-A_2|b\rangle$ lies in $Q$ and is already of second order, so it reaches $\langle\tilde a|H|\tilde b\rangle$ only at third order.
>
> Now collect the second-order part of $\langle\tilde a|H|\tilde b\rangle$, with $H=H_0+V$.
> - $V$ between a bare end and a dressed end gives $\langle a|VR_bV|b\rangle+\langle a|VR_aV|b\rangle$.
> - $H_0$ between the two admixtures gives $\langle a|VR_aH_0R_bV|b\rangle$.
> - $H_0$ between a bare end and the $P$ part of the other end gives $-\tfrac12(E_a+E_b)\langle a|VR_aR_bV|b\rangle$.
>
> Everything else vanishes at this order, because $\langle a|H_0R=E_a\langle a|R=0$. For one intermediate state $\alpha$, with $d_a=E_a-E_\alpha$ and $d_b=E_b-E_\alpha$, the four terms combine into
>
> $$
> \begin{aligned}
> \frac1{d_b}+\frac1{d_a}+\frac{E_\alpha}{d_ad_b}-\frac{E_a+E_b}{2d_ad_b}&=\frac{d_a+d_b}{2d_ad_b}\\
> &=\frac12\Big(\frac1{d_a}+\frac1{d_b}\Big),
> \end{aligned}
> $$
>
> the average of [[Van Vleck 01 - The effective Hamiltonian#^eq-h2|Eq. (5)]]. The first two terms alone, the coupling of a bare end to a dressed one, would count the excursion twice. The energy carried by the admixtures removes half of it.

## Other operators must be rotated too

Any question we ask of a true eigenstate must be asked of $|\psi\rangle=e^{-A}|\varphi\rangle$, not of $|\varphi\rangle$. For an operator $O$,

$$
\langle\psi_k|O|\psi_l\rangle=\langle\varphi_k|e^{A}Oe^{-A}|\varphi_l\rangle ,
$$

so inside the model space $O$ is represented not by $POP$ but by

$$
\begin{aligned}
O_{\rm eff}=Pe^{A}Oe^{-A}P&=POP+P[A_1,O]P\\
&\quad+P[A_2,O]P+\tfrac12P[A_1,[A_1,O]]P+\cdots .
\end{aligned}
$$
^eq-o-eff

This is the [[Van Vleck 01 - The effective Hamiltonian#^eq-bch|BCH series]] of the derivation, with one difference: the generator is no longer ours to choose. $H$ has fixed it, and every other operator has to follow. The Hamiltonian is the one operator for which this is automatic, because $H_{\rm eff}$ is $H$ rotated.

Rayleigh–Schrödinger theory never seems to need this step, but it takes the step silently. There the corrected states are written out, $|\psi\rangle=|a\rangle+R(E_a)V|a\rangle+\cdots$, and $\langle\psi|O|\psi\rangle$ is evaluated with them, so the admixture of $Q$ sits in the states. Van Vleck theory keeps the states of $P$ simple, so the admixture has to sit in the operator instead. The equation above is one identity read in two ways.

### How large the correction is

The block rule of [[Van Vleck 01 - The effective Hamiltonian#The rotated Hamiltonian|the derivation]] answers at once: each commutator with $A$ flips the block type of $O$. Every operator is the sum of a block-diagonal and an off-diagonal part, and the two parts behave differently.

An off-diagonal operator connects $P$ only to $Q$, so $POP=0$. The first correction, $P[A_1,O]P$, is then the leading term. With [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]],

$$
\langle a|O_{\rm eff}|b\rangle=\langle a|V\,R(E_a)\,O|b\rangle+\langle a|O\,R(E_b)\,V|b\rangle+\cdots .
$$

The bare operator misses the effect entirely.

For a block-diagonal operator, $[A_1,O]$ and $[A_2,O]$ are off-diagonal and vanish between two $P$'s. The first correction comes at second order, and [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]] used twice gives

$$
\tfrac12P[A_1,[A_1,O]]P=\sum_{a,b}P_aV\,R(E_a)\,O\,R(E_b)\,VP_b-\tfrac12\{N,POP\},
$$

with $N=\sum_{a,b}P_aV\,R(E_a)R(E_b)\,VP_b$, the operator whose diagonal elements are the $w_a$. The first term is $O$ measured in the admixtures, and the second removes the weight that the admixtures took from $P$. For such operators the bare $POP$ is right to first order, and the correction is of relative size $w_a$.

> [!example]- The induced dipole moment of an atom
> Take an atom in a level $|g\rangle$ of definite parity, in a static field along $z$, so that $V=-d_z\mathcal E$. Parity forbids a permanent dipole, $\langle g|d_z|g\rangle=0$, so the bare operator says that the atom has no dipole moment at all. The rotated operator, from the formula above with $O=d_z$, gives
>
> $$
> \langle g|(d_z)_{\rm eff}|g\rangle=-2\mathcal E\,\langle g|d_z\,R(E_g)\,d_z|g\rangle=2\mathcal E\sum_{\beta}\frac{|\langle\beta|d_z|g\rangle|^2}{E_\beta-E_g} ,
> $$
>
> the induced dipole: the static polarizability times the field. The effective Hamiltonian gives the energy $E^{(2)}=-\mathcal E^2\sum_\beta|\langle\beta|d_z|g\rangle|^2/(E_\beta-E_g)$, and $-\partial E^{(2)}/\partial\mathcal E$ is the same induced dipole, as the Hellmann–Feynman theorem requires. For a random model of this kind, [`check_van_vleck_states_errors.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck_states_errors.py) finds that the rotated operator reproduces the exact $\langle\psi|d_z|\psi\rangle$ up to relative corrections of order $\mathcal E^2$. The induced dipole is first order in the field, and $POP$ misses all of it.

### What this means for a measurement

Must we then rotate everything that touches the atoms during an experiment? Take an EDM measurement on $^{171}$Yb in an optical trap. The trap light dresses the ground level $^1S_0$: each nuclear-spin sublevel takes in a little $^1P_1$ and $^3P_1$. The effective Hamiltonian describes the spin precession in this dressed manifold. At the end the spin state is read out optically, with resonant light that drives the atoms to an excited state and so couples them to other electronic states again.

Three things should be kept apart.

The precession phase is the difference of two eigenvalues of $H_{\rm eff}$, accumulated over time. Eigenvalues do not depend on the basis, and nothing has to be rotated for them. This is the quantity an EDM measurement is after.

The readout light is a new perturbation, and for it the excited state is not far: the light is resonant. That state cannot be folded away, and the readout needs a model space of its own that contains it ([[Van Vleck 03 - Errors#When the folding fails|when the folding fails]]). The effective Hamiltonian of the trap light has nothing to say about the readout itself.

What connects the two stages is the map between dressed and bare states. Suppose the trap light is turned off before the readout, slowly compared with the inverse of its detuning; every laboratory ramp is slow on the scale of femtoseconds. Then the adiabatic theorem carries each dressed state continuously into the bare state with the same label, the reverse of what happens when a field is switched on ([[Van Vleck 00 - Near and far#What the atom does|near and far]]). The populations and coherences computed in $P$ reach the readout unchanged, and nothing has to be rotated.

If the readout happens with the trap light still on, the readout light addresses dressed states, and its operators should be rotated. A projector onto a spin sublevel is block diagonal, so its correction is of relative size $w$, roughly the light shift over the detuning ([[Van Vleck 03 - Errors#The small parameter|errors]]): $10^{-8}$ for a megahertz trap and a detuning of a hundred terahertz. That changes the contrast, not the phase. Only a sudden switch would leave a trace. The bare state would then be the dressed state plus a small amplitude, coupling over distance, in the states that grow out of $Q$. For a periodic drive, Floquet theory gives the same picture, with the rotation becoming a periodic micromotion of the state at the drive frequency.
