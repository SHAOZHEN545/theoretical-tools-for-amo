---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

A truncated effective Hamiltonian is an approximation, and before we trust a number computed from it we want to know how good it is. If we could carry the rotation to all orders, nothing would be lost. When the series converges, the eigenvalues of $H_{\rm eff}$ are exact eigenvalues of $H$: those of the states that grow out of $P$. Every error comes from stopping the series, or from approximations made on top of stopping. This note sorts them out, and ends with the case in which the series does not converge at all.

The notation is that of [[Van Vleck perturbation theory and the effective Hamiltonian|the derivation]]. $P$ and $Q$ are spanned by eigenstates $|a\rangle,|b\rangle,\dots$ and $|\alpha\rangle,|\beta\rangle,\dots$ of $H_0$, $A=A_1+A_2+\cdots$ is the anti-Hermitian generator, $\tilde H=e^{A}He^{-A}$, $H_{\rm eff}=P\tilde HP$, and $R(E)=Q/(E-H_0)$. Equation numbers refer to the derivation and link to it.

## The small parameter

Everything is controlled by the rotation angles of [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-a1|Eq. (4)]], $\langle\alpha|V|a\rangle/(E_a-E_\alpha)$. Each order of $H_{\rm eff}$ has one more factor of $V$ and one more resolvent than the last, that is, one more angle. A convenient single number is the probability of leaving the model space, $w_a$, the sum of the squared angles ([[Van Vleck perturbation theory - dressed states and rotated operators#The second-order dressing|dressed states]]).

For a light shift the angle has a simple meaning. In a two-level picture, with a coupling $v$ (half the Rabi frequency) and a detuning $\Delta$, the shift is $U=-|v|^2/\Delta$ and the angle is $v/\Delta$ in size, so

$$
w=\frac{|v|^2}{\Delta^2}=\frac{|U|}{|\Delta|} .
$$

The probability of being in the excited state is the light shift over the detuning: $10^{-8}$ for a trap 1 MHz deep and a detuning of 100 THz. Its square root, $10^{-4}$, is the rotation angle itself: the amplitude of the excited state in the dressed ground state.

## Stopping

Stopping after order $n$ drops $H^{(n+1)}$ and everything beyond, so the error is the size of the first dropped term, smaller than the last kept term by about one angle. The two-level picture above shows it. Its exact lower eigenvalue is

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

## How exact the average is

At second order, [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h2|Eq. (5)]] measures the distance of each intermediate state once from $E_a$ and once from $E_b$, and takes the average. Within the van Vleck construction this is not an approximation: the rotation produces exactly the average. The real question is how the average compares with the exact answer, and an exact folding settles it.

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
^eq-exact-folding

Nothing has been approximated; this is Löwdin's partitioning, known in nuclear physics as Feshbach's projection. Exactness has a price. The operator in brackets depends on the eigenvalue $E$ we are looking for, and its eigenvectors are the projections $P|\psi\rangle$, which are neither normalized nor orthogonal ([[Van Vleck perturbation theory - dressed states and rotated operators#^projections|dressed states]]).

Expanding the inverse in powers of $QVQ$, with $QHQ=QH_0Q+QVQ$,

$$
PVQ\,\frac{1}{E-QHQ}\,QVP=PV\,R(E)\,VP+PV\,R(E)\,V\,R(E)\,VP+\cdots .
$$

In the exact theory, then, every intermediate state is measured from the true energy $E$, and the coupling inside $Q$ enters through the higher terms.

Perturbation theory cannot use $E$, which is what it is trying to find, and has to measure from unperturbed energies instead. That is the real approximation. Its relative cost is $(E-E_a)/(E_a-E_\alpha)$, where $E-E_a$ is set by the shifts inside $P$ and, for off-diagonal elements, by its spread. In the eigenvalues it first shows up at third order.

Which unperturbed energy we use matters much less. For an element between $a$ and $b$ we could take $E_a$, $E_b$, their average, or anything in between. Every such choice differs from the average by an anti-Hermitian matrix, proportional to $\langle a|V[R(E_a)-R(E_b)]V|b\rangle$. At first order, an anti-Hermitian change can move the eigenvalues of a Hermitian matrix only by imaginary amounts, so their real parts change only at fourth order. In the numerical example of [`check_van_vleck_states_errors.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck_states_errors.py), measuring every element from the energy of one end shifts the real parts of the eigenvalues as $\lambda^4$. It also gives them imaginary parts of order $\lambda^3$, as large as the second-order error itself.

So the average is singled out not by accuracy but by structure. Measuring every element from the energy of its ket gives a non-Hermitian operator, with complex eigenvalues once truncated: to second order, Bloch's effective Hamiltonian, whose eigenvectors are the projections $P|\psi\rangle$. Löwdin's operator is Hermitian but depends on $E$. The unitary rotation gives an operator that is Hermitian and independent of $E$, with orthonormal eigenvectors, and at second order that requires the average.

The difference between true and unperturbed energies does not go away; it moves to third order. For a degenerate model space the exact formula reproduces the third order of van Vleck theory in a few lines (callout below). The excursion with two steps outside comes from the $QVQ$ term of the expansion. The term $-\tfrac12\{PVP,PVR^2VP\}$ of [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h3-degenerate|Eq. (9)]] is the shift of $E$ away from $E_0$, inserted into $R(E)$. Its symmetric form is what remains once the projections are normalized.

> [!note]- Eq. (9) from the exact folding
> Let the model space be degenerate at $E_0$, write $R=R(E_0)$ and $N=PVR^2VP$, and keep terms to third order. Since $R(E)=R-(E-E_0)R^2+\cdots$, the [[#^eq-exact-folding|exact equation]] becomes
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
> To third order, $(1+N)^{-1/2}h(1+N)^{-1/2}=h-\tfrac12\{N,PVP\}$, because $N$ is of second order and $h$ starts at first. Adding $E_0$ gives [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h2-degenerate|Eq. (7)]] plus [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h3-degenerate|Eq. (9)]]. The rescaling by $(1+N)^{1/2}$ is the symmetric orthonormalization of the projections: to this order $M^2=1-N$, with $M$ from [[Van Vleck perturbation theory - dressed states and rotated operators#^projections|dressed states]].

## Approximations on top

Three further errors come from approximations we often make on top of stopping.

The denominators are measured from unperturbed energies, while the system sits at its perturbed energy, as we have just seen. The higher orders correct for this, as the second term of [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h3-degenerate|Eq. (9)]] does at third order. The relative cost is the shift inside $P$ over the distance to $Q$. This is the fine print behind "inside $P$ nothing is required" in [[Van Vleck perturbation theory and the effective Hamiltonian#Two subspaces|the derivation]]. The couplings inside $P$ may be as strong as they like compared with the spacings inside $P$, but not compared with the distance to $Q$. If $PVP$ were comparable with that distance, we would first move it into $H_0$, diagonalize $H_0+PVP$ inside $P$, and fold with its eigenstates and energies. That route is often the natural one anyway.

The degenerate forms, [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h2-degenerate|Eq. (7)]] and [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h3-degenerate|Eq. (9)]], use one energy $E_0$ for the whole model space. Applied to a model space that is only nearly degenerate, they cost a relative error of its spread over the distance to $Q$: $10^{-14}$ for Zeeman sublevels and $10^{-4}$ for the Stark manifold of a polar molecule, as estimated in [[Van Vleck perturbation theory and the effective Hamiltonian#Second order|the derivation]].

Finally, an error that is not in $H_{\rm eff}$ at all. An operator other than $H$, evaluated without rotation as the bare $POP$, is wrong at first order in the angles if it has an off-diagonal part, and at relative order $w$ if it is block diagonal ([[Van Vleck perturbation theory - dressed states and rotated operators#Other operators must be rotated too|dressed states]]). Of all the errors here, this is the largest and the easiest to make.

To judge a second-order effective Hamiltonian, then, we estimate the angles of the strongest couplings out of $P$. We ask whether symmetry allows the third order, which leaves a relative error of about one angle, or forbids it, which leaves about its square. If we used the degenerate form, we add the spread of $P$ over the distance to $Q$. And we make sure that every other operator we evaluate in $P$ has been rotated.

## When the folding fails

Everything rests on small rotation angles. If a state of $Q$ comes close to a state of $P$, compared with their coupling, its angle is no longer small. [[Van Vleck perturbation theory and the effective Hamiltonian#^eq-h2-elements|Eq. (6)]] then blows up as $E_\alpha\to E_a$, the higher orders are worse, and the series stops converging: for two levels, as soon as the coupling exceeds half their distance ([[Van Vleck perturbation theory - near and far#Two levels|near and far]]). In quantum chemistry such a state is called an intruder.

Pushing the perturbation theory to higher orders does not help. Instead we move the offending state into $P$, where its coupling is treated exactly when we diagonalize $H_{\rm eff}$.

Light tuned toward a resonance is the standard example. Count the photons of the light field along with the state of the atom. The model state $|a\rangle$ with $n$ photons has the energy $E_a+n\omega$, and an excited state $|\beta\rangle$ with one photon absorbed has $E_\beta+(n-1)\omega$. As $\omega$ approaches $E_\beta-E_a$, that state approaches the model space, and its contribution to the light shift, $|v_{\beta a}|^2/(E_a+\omega-E_\beta)$, diverges; here $v_{\beta a}$ is the coupling that absorbs the photon. Moved into $P$, it gives a $2\times2$ effective Hamiltonian whose eigenstates are the dressed states of atom and light, split by the Rabi frequency: the Autler–Townes doublet. The far-detuned light shift is the perturbative limit of that splitting.

This is the one real decision in any application, the decision of [[Van Vleck perturbation theory - near and far#What goes into the model space|near and far]]. States that are far from the model space compared with their coupling go into $Q$ and are folded away. States that are near go into $P$ and are diagonalized together with the states we care about. The readout light of [[Van Vleck perturbation theory - dressed states and rotated operators#What this means for a measurement|dressed states]] is the same decision in the laboratory: for resonant light, the excited state is near.
