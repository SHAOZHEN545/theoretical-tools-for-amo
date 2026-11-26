---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

Long before we compute any coefficient, we usually know which operators an effective Hamiltonian may contain. That knowledge rests on one property of the folding: the effective Hamiltonian inherits the symmetries of the full one. This note shows why, how the statement is used when the applied fields break the symmetry, and what it asks of the model space.

The notation is that of [[Van Vleck 01 - The effective Hamiltonian|the derivation]]. $P$ and $Q$ are spanned by eigenstates $|a\rangle,|b\rangle,\dots$ and $|\alpha\rangle,|\beta\rangle,\dots$ of $H_0$, $A=A_1+A_2+\cdots$ is the anti-Hermitian generator, $\tilde H=e^{A}He^{-A}$, $H_{\rm eff}=P\tilde HP$, and $R(E)=Q/(E-H_0)$. Equation numbers refer to the derivation and link to it.

## Symmetries survive the folding

Suppose a symmetry, unitary $U$ or antiunitary $\Theta$ such as time reversal, commutes with $H_0$, with $V$ and with $P$. It is natural to expect $H_{\rm eff}$ to inherit it, and it does:

$$
UH_{\rm eff}U^{-1}=H_{\rm eff} .
$$

At second order we can read this off [[Van Vleck 01 - The effective Hamiltonian#^eq-a1|Eq. (4)]]. Group the model states by energy, and let $\Pi_E$ project onto the states of $P$ with energy $E$. The equation then reads

$$
A_1=\sum_E\Big(\Pi_E\,V\,R(E)-R(E)\,V\,\Pi_E\Big),
$$

a sum over the distinct energies in $P$. A symmetry of $H_0$ maps each energy level onto itself, so it commutes with every $\Pi_E$ and with every $R(E)=Q/(E-H_0)$. If it also commutes with $V$, it commutes with $A_1$, and then with $H^{(2)}=\tfrac12P[A_1,V_{OD}]P$. No factor of $i$ appears anywhere, and $E$ is a real number, so the argument holds for an antiunitary $\Theta$ as well.

The grouping by energy matters. A symmetry may mix the states of a degenerate level, so it need not commute with the individual $P_a=|a\rangle\langle a|$; it does commute with their sum over the level. The higher generators are built in the same way, from $V$, the $\Pi_E$, the resolvents and the lower generators, so the argument repeats at every order. A tidier proof, valid at all orders at once, rests on the uniqueness of the generator.

> [!note]- Proof for unitary and antiunitary symmetries
> *Uniqueness.* Suppose $A_1$ and $A_1'$ are both off-diagonal and both satisfy [[Van Vleck 01 - The effective Hamiltonian#^eq-a1-condition|Eq. (1)]]. Their difference is off-diagonal and commutes with $H_0$, so each of its elements obeys $\langle a|A_1-A_1'|\alpha\rangle(E_\alpha-E_a)=0$. Since $E_a\neq E_\alpha$, $A_1'=A_1$.
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

## Covariance

In practice the symmetry is usually broken, by the very fields we apply. A rotation does not leave $-\mathbf d\cdot\mathbf E$ alone; it turns it into $-\mathbf d\cdot\mathbf E'$, with the rotated field. The same argument still applies when the symmetry relates two Hamiltonians,

$$
UH(F)U^{-1}=H(F'),
$$

where $F$ stands for the external parameters, such as fields and polarizations, and $F'$ for their transformed values. Provided the model space is carried along, $UP(F)U^{-1}=P(F')$, the generator for $H(F)$ is mapped onto the generator for $H(F')$, and

$$
H_{\rm eff}(F')=UH_{\rm eff}(F)U^{-1} .
$$
^eq-covariance

This covariant form is the one we use. It says that $H_{\rm eff}$ must be assembled from operators acting inside $P$ and from the external parameters, in combinations that transform correctly. Before anything is computed, that fixes which terms can appear; perturbation theory is needed only for their coefficients. For an atom of angular momentum $\mathbf F$ in a magnetic field $\mathbf B$, for example, the only candidates are scalars built from $\mathbf F$ and $\mathbf B$, such as $\mathbf F\cdot\mathbf B$, $B^2$ and $(\mathbf F\cdot\mathbf B)^2$. Perturbation theory then supplies the $g$-factor and the coefficients of the quadratic Zeeman effect.

An interaction that breaks a symmetry can be handled in the same way: we treat its strength as one more parameter, with its own sign under the symmetry. The interaction of an electric dipole moment with an electric field, $-d\,\mathbf F\cdot\mathbf E/F$, is the standard example. $\mathbf F$ is even under parity and odd under time reversal, $\mathbf E$ the other way round, so $\mathbf F\cdot\mathbf E$ is odd under both. If we let $d$ change sign under $P$ and under $T$, the interaction becomes invariant, and $d$ enters the symmetry analysis next to $\mathbf E$ and $\mathbf B$.

## What the theorem needs

The proof uses two closure properties, and each can fail in practice.

The model space must be closed under the symmetry. If $P$ is a truncation that breaks a multiplet, for example a few $M$ sublevels of a rotational level, rotations carry states out of $P$, and $H_{\rm eff}$ need not be covariant. It can then contain terms that single out a direction in space that nothing physical singles out. We keep whole multiplets in $P$. When $P$ depends on the fields, as for the polarized states of a molecule in a static field, it must be defined covariantly, so that rotating the field rotates $P$ with it.

The same holds for the sums over intermediate states. A calculation that keeps only a few states of $Q$, as every practical sum over states does, respects the symmetry only if it keeps whole multiplets there too: all the $M$ sublevels of every excited level it includes.
