---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

[[Van Vleck perturbation theory and the effective Hamiltonian]] builds the effective Hamiltonian order by order, and the result is compact: a few products of $V$ and resolvents, squeezed between projectors. The compactness hides several questions that decide whether we can trust the result and how to use it.

The Hamiltonian has been rotated, so what do the states of the model space stand for? What happens to the other operators we want to measure? The second-order denominators are averaged between the two ends of a matrix element; is that exact, or merely convenient? How large is what we dropped? Why does the effective Hamiltonian inherit the symmetries of the full one, and what does that ask of us? And when does the construction fail?

We take these questions one at a time, in the notation of the derivation. $P$ and $Q$ are the model and external spaces, spanned by eigenstates $|a\rangle,|b\rangle,\dots$ and $|\alpha\rangle,|\beta\rangle,\dots$ of $H_0$. $A=A_1+A_2+\cdots$ is the anti-Hermitian generator, $\tilde H=e^{A}He^{-A}$, $H_{\rm eff}=P\tilde HP$, and $R(E)=Q/(E-H_0)$. Equation numbers refer to the derivation, and each one links to it.

## What the model states stand for

The rotation $e^{A}$ is a change of basis, not of physics. $\tilde H$ has exactly the spectrum of $H$, and its eigenvectors are those of $H$, rotated.

To see how they correspond, take an eigenvector of the effective Hamiltonian, $H_{\rm eff}|\varphi\rangle=E|\varphi\rangle$ with $|\varphi\rangle$ in $P$, and rotate it back, $|\psi\rangle=e^{-A}|\varphi\rangle$. Inserting $1=e^{-A}e^{A}$ in front of $H$,

$$
H|\psi\rangle=He^{-A}|\varphi\rangle=e^{-A}\big(e^{A}He^{-A}\big)|\varphi\rangle=e^{-A}\tilde H|\varphi\rangle .
$$

Since $\tilde H$ is block diagonal, it maps $|\varphi\rangle$ into $P$, and there it acts as $H_{\rm eff}$: $\tilde H|\varphi\rangle=P\tilde HP|\varphi\rangle=E|\varphi\rangle$. Hence

$$
H|\psi\rangle=E\,e^{-A}|\varphi\rangle=E|\psi\rangle .
$$

The one input beyond algebra was the block diagonality of $\tilde H$, so this holds to the order at which we stopped the rotation.

Each basis state $|a\rangle$ of $P$ therefore stands for a dressed state

$$
|\tilde a\rangle=e^{-A}|a\rangle ,
$$

and an eigenvector $\sum_ac_a|a\rangle$ of $H_{\rm eff}$ stands for the true eigenstate $\sum_ac_a|\tilde a\rangle$. The coefficients $c_a$ are what we compute inside $P$; the dressing is common to all eigenvectors and is carried by $e^{-A}$. In this basis $H$ has the matrix elements $\langle\tilde a|H|\tilde b\rangle=\langle a|H_{\rm eff}|b\rangle$, which is how [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|the derivation]] explains its averaged denominators.

### The first-order dressing

To first order only $A_1$ acts, and by [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]], $A_1|a\rangle=-R(E_a)V|a\rangle$. So

$$
\begin{aligned}
|\tilde a\rangle&=|a\rangle+R(E_a)V|a\rangle+O(V^2)\\
&=|a\rangle+\sum_{\alpha\in Q}|\alpha\rangle\,\frac{\langle\alpha|V|a\rangle}{E_a-E_\alpha}+O(V^2) .
\end{aligned}
$$

Each model state takes in every external state, with an amplitude equal to its rotation angle, coupling over distance. This is the first-order state of Rayleigh–Schrödinger theory, now attached to every state of $P$ at once.

### The second-order dressing

At second order the dressing reaches back into $P$. With $e^{-A}=1-A+\tfrac12A^2-\cdots$ and $A=A_1+A_2+\cdots$,

$$
|\tilde a\rangle=|a\rangle-A_1|a\rangle-A_2|a\rangle+\tfrac12A_1^2|a\rangle+O(V^3) .
$$

The terms with one generator lie in $Q$, because an off-diagonal operator carries $P$ into $Q$. Two generators carry $|a\rangle$ out and back, and [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]] applied twice gives

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

up to terms of third order. So $w_a$ is the probability of finding the system outside the model space. It is the natural measure of how strongly the folding disturbs a state, and it sets the size of the errors in [[#Where the errors are]].

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

This is the BCH series of [[Van Vleck perturbation theory and the effective Hamiltonian#Rotating the Hamiltonian|the derivation]], with one difference: the generator is no longer ours to choose. $H$ has fixed it, and every other operator has to follow. The Hamiltonian is the one operator for which this is automatic, because $H_{\rm eff}$ is $H$ rotated.

Rayleigh–Schrödinger theory never seems to need this step, but it takes the step silently. There the corrected states are written out, $|\psi\rangle=|a\rangle+R(E_a)V|a\rangle+\cdots$, and $\langle\psi|O|\psi\rangle$ is evaluated with them, so the admixture of $Q$ sits in the states. Van Vleck theory keeps the states of $P$ simple, so the admixture has to sit in the operator instead. The equation above is one identity read in two ways.

### How large the correction is

The block rule of [[Van Vleck perturbation theory and the effective Hamiltonian#Rotating the Hamiltonian|the derivation]] answers at once: each commutator with $A$ flips the block type of $O$. Every operator is the sum of a block-diagonal and an off-diagonal part, and the two parts behave differently.

An off-diagonal operator connects $P$ only to $Q$, so $POP=0$. The first correction, $P[A_1,O]P$, is then the leading term. With [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]],

$$
\langle a|O_{\rm eff}|b\rangle=\langle a|V\,R(E_a)\,O|b\rangle+\langle a|O\,R(E_b)\,V|b\rangle+\cdots .
$$

The bare operator misses the effect entirely.

For a block-diagonal operator, $[A_1,O]$ and $[A_2,O]$ are off-diagonal and vanish between two $P$'s. The first correction comes at second order, and [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]] used twice gives

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

The readout light is a new perturbation, and for it the excited state is not far: the light is resonant. That state cannot be folded away, and the readout needs a model space of its own that contains it ([[#When the folding fails]]). The effective Hamiltonian of the trap light has nothing to say about the readout itself.

What connects the two stages is the map between dressed and bare states. Suppose the trap light is turned off before the readout, slowly compared with the inverse of its detuning; every laboratory ramp is slow on the scale of femtoseconds. Then the adiabatic theorem carries each dressed state continuously into the bare state with the same label. The populations and coherences computed in $P$ reach the readout unchanged, and nothing has to be rotated.

If the readout happens with the trap light still on, the readout light addresses dressed states, and its operators should be rotated. A projector onto a spin sublevel is block diagonal, so its correction is of relative size $w$, roughly the light shift over the detuning ([[#The small parameter]]): $10^{-8}$ for a megahertz trap and a detuning of a hundred terahertz. That changes the contrast, not the phase. Only a sudden switch would leave a trace. The bare state would then be the dressed state plus a small amplitude, coupling over distance, in the states that grow out of $Q$. For a periodic drive, Floquet theory gives the same picture, with the rotation becoming a periodic micromotion of the state at the drive frequency.

## How exact the average is

At second order, [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|Eq. (5)]] measures the distance of each intermediate state once from $E_a$ and once from $E_b$, and takes the average. Within the van Vleck construction this is not an approximation: the rotation produces exactly the average. The real question is how the average compares with the exact answer, and an exact folding settles it.

Split the eigenvalue equation $H|\psi\rangle=E|\psi\rangle$ into its two blocks. Since $H_0$ is block diagonal, $PHQ=PVQ$, and

$$
\begin{aligned}
PHP\,P|\psi\rangle+PVQ\,Q|\psi\rangle&=E\,P|\psi\rangle,\\
QVP\,P|\psi\rangle+QHQ\,Q|\psi\rangle&=E\,Q|\psi\rangle .
\end{aligned}
$$

The second line gives $Q|\psi\rangle=(E-QHQ)^{-1}QVP|\psi\rangle$, with the inverse taken on $Q$. Inserted into the first,

$$
\Big[PHP+PVQ\,\frac{1}{E-QHQ}\,QVP\Big]P|\psi\rangle=E\,P|\psi\rangle .
$$

Nothing has been approximated; this is Löwdin's partitioning, known in nuclear physics as Feshbach's projection. Exactness has a price. The operator in brackets depends on the eigenvalue $E$ we are looking for, and its eigenvectors are the projections $P|\psi\rangle$, which are neither normalized nor orthogonal ([[#What the model states stand for]]).

Expanding the inverse in powers of $QVQ$, with $QHQ=QH_0Q+QVQ$,

$$
PVQ\,\frac{1}{E-QHQ}\,QVP=PV\,R(E)\,VP+PV\,R(E)\,V\,R(E)\,VP+\cdots .
$$

In the exact theory, then, every intermediate state is measured from the true energy $E$, and the coupling inside $Q$ enters through the higher terms.

Perturbation theory cannot use $E$, which is what it is trying to find, and has to measure from unperturbed energies instead. That is the real approximation. Its relative cost is $(E-E_a)/(E_a-E_\alpha)$, where $E-E_a$ is set by the shifts inside $P$ and, for off-diagonal elements, by its spread. In the eigenvalues it first shows up at third order.

Which unperturbed energy we use matters much less. For an element between $a$ and $b$ we could take $E_a$, $E_b$, their average, or anything in between. Every such choice differs from the average by an anti-Hermitian matrix, proportional to $\langle a|V[R(E_a)-R(E_b)]V|b\rangle$. At first order, an anti-Hermitian change can move the eigenvalues of a Hermitian matrix only by imaginary amounts, so their real parts change only at fourth order. In the numerical example of [`check_van_vleck_states_errors.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck_states_errors.py), measuring every element from the energy of one end shifts the real parts of the eigenvalues as $\lambda^4$. It also gives them imaginary parts of order $\lambda^3$, as large as the second-order error itself.

So the average is singled out not by accuracy but by structure. Measuring every element from the energy of its ket gives a non-Hermitian operator, with complex eigenvalues once truncated: to second order, Bloch's effective Hamiltonian, whose eigenvectors are the projections $P|\psi\rangle$. Löwdin's operator is Hermitian but depends on $E$. The unitary rotation gives an operator that is Hermitian and independent of $E$, with orthonormal eigenvectors, and at second order that requires the average.

The difference between true and unperturbed energies does not go away; it moves to third order. For a degenerate model space the exact formula reproduces the third order of van Vleck theory in a few lines (callout below). The excursion with two steps outside comes from the $QVQ$ term of the expansion. The term $-\tfrac12\{PVP,PVR^2VP\}$ of [[Van Vleck perturbation theory and the effective Hamiltonian#Third order|Eq. (9)]] is the shift of $E$ away from $E_0$, inserted into $R(E)$. Its symmetric form is what remains once the projections are normalized.

> [!note]- Eq. (9) from the exact folding
> Let the model space be degenerate at $E_0$, write $R=R(E_0)$ and $N=PVR^2VP$, and keep terms to third order. Since $R(E)=R-(E-E_0)R^2+\cdots$, the exact equation becomes
>
> $$
> \big[E_0+PVP+PVRVP+PVRVRVP-(E-E_0)\,N\big]P|\psi\rangle=E\,P|\psi\rangle .
> $$
>
> Move the term with $E-E_0$ to the right, and let $h=PVP+PVRVP+PVRVRVP$:
>
> $$
> h\,P|\psi\rangle=(E-E_0)(1+N)\,P|\psi\rangle .
> $$
>
> This is a generalized eigenvalue problem, because $P|\psi\rangle$ is not normalized. With $|\varphi\rangle=(1+N)^{1/2}P|\psi\rangle$ it becomes an ordinary one,
>
> $$
> (1+N)^{-1/2}\,h\,(1+N)^{-1/2}|\varphi\rangle=(E-E_0)|\varphi\rangle .
> $$
>
> To third order, $(1+N)^{-1/2}h(1+N)^{-1/2}=h-\tfrac12\{N,PVP\}$, because $N$ is of second order and $h$ starts at first. Adding $E_0$ gives [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|Eq. (7)]] plus [[Van Vleck perturbation theory and the effective Hamiltonian#Third order|Eq. (9)]]. The rescaling by $(1+N)^{1/2}$ is the symmetric orthonormalization of the projections: to this order $M^2=1-N$, with $M$ from [[#What the model states stand for]].

## Where the errors are

If we could carry the rotation to all orders, nothing would be lost. When the series converges, the eigenvalues of $H_{\rm eff}$ are exact eigenvalues of $H$: those of the states that grow out of $P$. Every error comes from stopping, or from approximations made on top of stopping. It pays to know which is which, and how large each one is.

### The small parameter

Everything is controlled by the rotation angles of [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]], $\langle\alpha|V|a\rangle/(E_a-E_\alpha)$. Each order of $H_{\rm eff}$ has one more factor of $V$ and one more resolvent than the last, that is, one more angle. A convenient single number is the probability of leaving the model space, $w_a$, the sum of the squared angles ([[#The second-order dressing]]).

For a light shift the angle has a simple meaning. In a two-level picture, with a coupling $v$ (half the Rabi frequency) and a detuning $\Delta$, the shift is $U=-|v|^2/\Delta$ and the angle is $v/\Delta$ in size, so

$$
w=\frac{|v|^2}{\Delta^2}=\frac{|U|}{|\Delta|} .
$$

The probability of being in the excited state is the light shift over the detuning: $10^{-8}$ for a trap 1 MHz deep and a detuning of 100 THz. Its square root, $10^{-4}$, is the rotation angle itself: the amplitude of the excited state in the dressed ground state.

### Stopping

Stopping after order $n$ drops $H^{(n+1)}$ and everything beyond, so the error is the size of the first dropped term, smaller than the last kept term by about one angle. The two-level example shows it. Its exact lower eigenvalue is

$$
\begin{aligned}
\frac{\Delta-\sqrt{\Delta^2+4|v|^2}}{2}&=-\frac{|v|^2}{\Delta}+\frac{|v|^4}{\Delta^3}-\frac{2|v|^6}{\Delta^5}+\cdots\\
&=U+\frac{U^2}{\Delta}+\frac{2U^3}{\Delta^2}+\cdots ,
\end{aligned}
$$

so after second order the error is $U^2/\Delta=w\,|U|$. For a random model space that is not degenerate, [`check_van_vleck.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck.py) finds the same pattern: the eigenvalue error falls as $\lambda^3$ after second order and as $\lambda^4$ after third.

In the two-level example the third order vanished, and the error jumped from third order to fourth. This happens whenever parity forbids the odd orders. If the model space has definite parity and $V$ is odd, as for a static electric field or the electric field of light, every product of an odd number of $V$'s vanishes between two states of $P$. Then $H^{(3)}=0$, and a second-order effective Hamiltonian is good to relative order $w$ rather than to one angle. For trap light the fourth-order term is the hyperpolarizability, of size $U^2/\Delta$: about 10 mHz for the trap above. Optical lattice clocks have to account for it.

Stopping also leaves a coupling behind in the off-diagonal block. The generators $A_1,\dots,A_n$ fix $H_{\rm eff}$ through order $n+1$, because $A_{n+1}$ enters order $n+1$ of $\tilde H$ only through $[A_{n+1},H_0]$, which is off-diagonal. With these generators, however, the rotated Hamiltonian still couples $P$ to $Q$ at order $n+1$, and discarding $Q$ throws that coupling away.

This costs less than it seems. A coupling between $P$ and $Q$ shifts the energies in $P$ only at second order in itself, through one more excursion. The leftover coupling of order $n+1$ therefore shifts the energies at order $2n+2$, never earlier than the first dropped term of $H_{\rm eff}$, at order $n+2$. [`check_van_vleck_states_errors.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck_states_errors.py) shows it directly. After an exact rotation with $A_1$, the whole $P$ block of $\tilde H$ has eigenvalue errors of order $\lambda^4$, while $H_{\rm eff}$ cut at second order has errors of order $\lambda^3$. With $A_1+A_2$ the two become $\lambda^6$ and $\lambda^4$. Truncating the series, not discarding $Q$, is what limits the accuracy.

### Approximations on top

Three further errors come from approximations we often make on top of stopping.

The denominators are measured from unperturbed energies, while the system sits at its perturbed energy ([[#How exact the average is]]). The higher orders correct for this, as the second term of [[Van Vleck perturbation theory and the effective Hamiltonian#Third order|Eq. (9)]] does at third order. The relative cost is the shift inside $P$ over the distance to $Q$. This is the fine print behind "inside $P$ nothing is required" in [[Van Vleck perturbation theory and the effective Hamiltonian#Two subspaces|the derivation]]. The couplings inside $P$ may be as strong as they like compared with the spacings inside $P$, but not compared with the distance to $Q$. If $PVP$ were comparable with that distance, we would first move it into $H_0$, diagonalize $H_0+PVP$ inside $P$, and fold with its eigenstates and energies. That route is often the natural one anyway.

The degenerate forms, [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|Eq. (7)]] and [[Van Vleck perturbation theory and the effective Hamiltonian#Third order|Eq. (9)]], use one energy $E_0$ for the whole model space. Applied to a model space that is only nearly degenerate, they cost a relative error of its spread over the distance to $Q$: $10^{-14}$ for Zeeman sublevels and $10^{-4}$ for the Stark manifold of a polar molecule, as estimated in [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|the derivation]].

Finally, an error that is not in $H_{\rm eff}$ at all. An operator other than $H$, evaluated without rotation as the bare $POP$, is wrong at first order in the angles if it has an off-diagonal part, and at relative order $w$ if it is block diagonal ([[#Other operators must be rotated too]]). Of all the errors here, this is the largest and the easiest to make.

To judge a second-order effective Hamiltonian, then, we estimate the angles of the strongest couplings out of $P$. We ask whether symmetry allows the third order, which leaves a relative error of about one angle, or forbids it, which leaves about its square. If we used the degenerate form, we add the spread of $P$ over the distance to $Q$. And we make sure that every other operator we evaluate in $P$ has been rotated.

## Symmetries survive the folding

Suppose a symmetry, unitary $U$ or antiunitary $\Theta$ such as time reversal, commutes with $H_0$, with $V$ and with $P$. It is natural to expect $H_{\rm eff}$ to inherit it, and it does:

$$
UH_{\rm eff}U^{-1}=H_{\rm eff} .
$$

At second order we can read this off [[Van Vleck perturbation theory and the effective Hamiltonian#Solving for the generator|Eq. (4)]]. Group the model states by energy, and let $\Pi_E$ project onto the states of $P$ with energy $E$. The equation then reads

$$
A_1=\sum_E\Big(\Pi_E\,V\,R(E)-R(E)\,V\,\Pi_E\Big),
$$

a sum over the distinct energies in $P$. A symmetry of $H_0$ maps each energy level onto itself, so it commutes with every $\Pi_E$ and with every $R(E)=Q/(E-H_0)$. If it also commutes with $V$, it commutes with $A_1$, and then with $H^{(2)}=\tfrac12P[A_1,V_{OD}]P$. No factor of $i$ appears anywhere, and $E$ is a real number, so the argument holds for an antiunitary $\Theta$ as well.

The grouping by energy matters. A symmetry may mix the states of a degenerate level, so it need not commute with the individual $P_a=|a\rangle\langle a|$; it does commute with their sum over the level. The higher generators are built in the same way, from $V$, the $\Pi_E$, the resolvents and the lower generators, so the argument repeats at every order. A tidier proof, valid at all orders at once, rests on the uniqueness of the generator.

> [!note]- Proof for unitary and antiunitary symmetries
> *Uniqueness.* Suppose $A_1$ and $A_1'$ are both off-diagonal and both satisfy [[Van Vleck perturbation theory and the effective Hamiltonian#Rotating the Hamiltonian|Eq. (1)]]. Their difference is off-diagonal and commutes with $H_0$, so each of its elements obeys $\langle a|A_1-A_1'|\alpha\rangle(E_\alpha-E_a)=0$. Since $E_a\neq E_\alpha$, $A_1'=A_1$.
>
> *Unitary $U$.* $UA_1U^{-1}$ is off-diagonal, because $U$ commutes with $P$, and it satisfies the same equation:
>
> $$
> [UA_1U^{-1},H_0]=U[A_1,H_0]U^{-1}=-UV_{OD}U^{-1}=-V_{OD} .
> $$
>
> By uniqueness, $UA_1U^{-1}=A_1$. At order $n$, $A_n$ is fixed by an equation of the same form, $[A_n,H_0]=-(\cdots)_{OD}$, whose right-hand side is built from $H_0$, $V$, $P$ and the lower generators. By induction every $A_n$ commutes with $U$, and so do $e^{A}$, $\tilde H$ and $H_{\rm eff}$.
>
> *Antiunitary $\Theta$.* The equations for the $A_n$ contain no explicit factor of $i$; their coefficients are the real numbers of the BCH series. So the same argument gives $\Theta A_n\Theta^{-1}=A_n$ at every order, and $\Theta$ commutes with $e^{A}$ and $H_{\rm eff}$. This is one reason to work with the anti-Hermitian $A$ rather than the Hermitian $S=-iA$: since $\Theta\,i\,\Theta^{-1}=-i$, $S$ would change sign.

### Covariance

In practice the symmetry is usually broken, by the very fields we apply. A rotation does not leave $-\mathbf d\cdot\mathbf E$ alone; it turns it into $-\mathbf d\cdot\mathbf E'$, with the rotated field. The same argument still applies when the symmetry relates two Hamiltonians,

$$
UH(F)U^{-1}=H(F'),
$$

where $F$ stands for the external parameters, such as fields and polarizations, and $F'$ for their transformed values. Provided the model space is carried along, $UP(F)U^{-1}=P(F')$, the generator for $H(F)$ is mapped onto the generator for $H(F')$, and

$$
H_{\rm eff}(F')=UH_{\rm eff}(F)U^{-1} .
$$

This covariant form is the one we use. It says that $H_{\rm eff}$ must be assembled from operators acting inside $P$ and from the external parameters, in combinations that transform correctly. Before anything is computed, that fixes which terms can appear; perturbation theory is needed only for their coefficients. For an atom of angular momentum $\mathbf F$ in a magnetic field $\mathbf B$, for example, the only candidates are scalars built from $\mathbf F$ and $\mathbf B$, such as $\mathbf F\cdot\mathbf B$, $B^2$ and $(\mathbf F\cdot\mathbf B)^2$. Perturbation theory then supplies the $g$-factor and the coefficients of the quadratic Zeeman effect.

An interaction that breaks a symmetry can be handled in the same way: we treat its strength as one more parameter, with its own sign under the symmetry. The interaction of an electric dipole moment with an electric field, $-d\,\mathbf F\cdot\mathbf E/F$, is the standard example. $\mathbf F$ is even under parity and odd under time reversal, $\mathbf E$ the other way round, so $\mathbf F\cdot\mathbf E$ is odd under both. If we let $d$ change sign under $P$ and under $T$, the interaction becomes invariant, and $d$ enters the symmetry analysis next to $\mathbf E$ and $\mathbf B$.

### What the theorem needs

The proof uses two closure properties, and each can fail in practice.

The model space must be closed under the symmetry. If $P$ is a truncation that breaks a multiplet, for example a few $M$ sublevels of a rotational level, rotations carry states out of $P$, and $H_{\rm eff}$ need not be covariant. It can then contain terms that single out a direction in space that nothing physical singles out. We keep whole multiplets in $P$. When $P$ depends on the fields, as for the polarized states of a molecule in a static field, it must be defined covariantly, so that rotating the field rotates $P$ with it.

The same holds for the sums over intermediate states. A calculation that keeps only a few states of $Q$, as every practical sum over states does, respects the symmetry only if it keeps whole multiplets there too: all the $M$ sublevels of every excited level it includes.

## When the folding fails

Everything rests on small rotation angles. If a state of $Q$ comes close to a state of $P$, compared with their coupling, its angle is no longer small. [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|Eq. (6)]] then blows up as $E_\alpha\to E_a$, the higher orders are worse, and the series stops converging: for two levels, as soon as the coupling exceeds half their distance ([[Van Vleck perturbation theory and the effective Hamiltonian#Near and far|near and far]]). In quantum chemistry such a state is called an intruder.

Pushing the perturbation theory to higher orders does not help. Instead we move the offending state into $P$, where its coupling is treated exactly when we diagonalize $H_{\rm eff}$.

Light tuned toward a resonance is the standard example. Count the photons of the light field along with the state of the atom. The model state $|a\rangle$ with $n$ photons has the energy $E_a+n\omega$, and an excited state $|\beta\rangle$ with one photon absorbed has $E_\beta+(n-1)\omega$. As $\omega$ approaches $E_\beta-E_a$, that state approaches the model space, and its contribution to the light shift, $|v_{\beta a}|^2/(E_a+\omega-E_\beta)$, diverges; here $v_{\beta a}$ is the coupling that absorbs the photon. Moved into $P$, it gives a $2\times2$ effective Hamiltonian whose eigenstates are the dressed states of atom and light, split by the Rabi frequency: the Autler–Townes doublet. The far-detuned light shift is the perturbative limit of that splitting.

This is the one real decision in any application, the decision of [[Van Vleck perturbation theory and the effective Hamiltonian#Near and far|near and far]]. States that are far from the model space compared with their coupling go into $Q$ and are folded away. States that are near go into $P$ and are diagonalized together with the states we care about. The readout light of [[#What this means for a measurement]] is the same decision in the laboratory: for resonant light, the excited state is near.
