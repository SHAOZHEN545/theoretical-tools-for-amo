---
tags:
  - tutorial
  - perturbation-theory
  - effective-Hamiltonian
---

We start from

$$
H = H_0 + \lambda V,
$$

where the eigenstates and energies of $H_0$ are known and $V$ is the perturbation. The parameter $\lambda$ only keeps track of orders; we set $\lambda = 1$ once the orders are sorted.

We want an effective Hamiltonian that acts only on a few of the states and still knows about all the others. Why we want it, how to choose the few, and why it amounts to a change of basis are the subject of [[Van Vleck 00 - Near and far|near and far]]. Here we construct it.

## Two subspaces

The *model space* $P$ is spanned by eigenstates $|a\rangle,|b\rangle,|c\rangle,\dots$ of $H_0$, with $H_0|a\rangle=E_a|a\rangle$. Some of the $E_a$ may coincide, and nothing below requires them to be equal or different. The *external space* $Q$ holds everything else, with eigenstates $|\alpha\rangle,|\beta\rangle,\dots$ and energies $E_\alpha$. Using the same letters for the projectors,

$$
P=\sum_a P_a,\qquad P_a=|a\rangle\langle a|,\qquad P+Q=1,\qquad [H_0,P]=[H_0,Q]=0 .
$$

The one requirement is that every state of $Q$ be far from every state of $P$:

$$
|\langle a|V|\alpha\rangle| \ll |E_a - E_\alpha|\qquad\text{for all } a\in P,\ \alpha\in Q .
$$

Inside $P$ nothing is required. Its states may be degenerate or not, and $V$ may couple them strongly, because in the end we diagonalize the effective Hamiltonian exactly. (The one proviso, that these couplings must not push the model states toward $Q$, is taken up in [[Van Vleck 03 - Errors#Approximations on top|errors]].)

It helps to split every operator $X$ into its block-diagonal and off-diagonal parts,

$$
X_D = PXP + QXQ,\qquad X_{OD} = PXQ + QXP .
$$

$H_0$ is block diagonal. $V$ generally has both parts, and $V_{OD}$ is the troublemaker: it is what ties our states to the rest of the world.

## The rotated Hamiltonian

Folding down means finding a basis of dressed states, $|\tilde i\rangle=e^{-A}|i\rangle$ with $A^\dagger=-A$, in which $H$ is block diagonal. As [[Van Vleck 00 - Near and far#A change of basis|near and far]] shows, the matrix of $H$ in that basis is the matrix of the rotated Hamiltonian

$$
\tilde H = e^{A} H e^{-A}
$$

in the bare basis, [[Van Vleck 00 - Near and far#^eq-dressed-equals-bare|block by block]]. So we look for an $A$ such that $\tilde H$ has no off-diagonal block, $P\tilde HQ=0$, **at least up to the order we need**. (Many texts write $A=iS$ with a Hermitian $S$.) The $P$ block is then the effective Hamiltonian, $H_{\rm eff}=P\tilde HP$, and its eigenvalues are eigenvalues of $H$ to that order.

> [!figure|center]
> ![[Van Vleck block diagonalization.svg|center|680]]
> Folding is a block diagonalization. Left, $H$ in the bare basis; right, $\tilde H$ in the bare basis, which is $H$ in the dressed basis. The change of basis removes the blocks $PVQ$ and $QVP$ that tie the model space to the far states. A generator built through order $n$ in $V$ leaves a coupling of order $n+1$, which we drop together with the $Q$ block. What remains is $H_{\rm eff}=P\tilde HP$, and nothing inside $P$ had to be small.

The Baker–Campbell–Hausdorff formula expands $\tilde H$ in nested commutators,

$$
\tilde H = H + [A, H] + \frac{1}{2!}[A,[A,H]] + \frac{1}{3!}[A,[A,[A,H]]] + \cdots
$$
^eq-bch

> [!note]- The BCH series
> Let $f(t) = e^{tA} H e^{-tA}$. Differentiating,
>
> $$
> f'(t) = e^{tA}\,[A,H]\,e^{-tA},\qquad f''(t) = e^{tA}\,[A,[A,H]]\,e^{-tA},
> $$
>
> and so on, each derivative adding one more commutator with $A$. The Taylor series of $f$ at $t=1$ is the BCH series quoted above.

We still have freedom in choosing $A$. The natural choice, and the one van Vleck made, is to let $A$ act only between the two subspaces, $PAP=QAQ=0$. Such an $A$ rotates $P$ into $Q$ and does nothing else. A block-diagonal part of $A$ would only reshuffle states within $P$ and within $Q$, which changes $H_{\rm eff}$ by a unitary transformation inside $P$ and leaves its eigenvalues alone.

With this choice one rule does most of the work below: a commutator with $A$ flips the block type. If $X$ is block diagonal, $[A,X]$ is off-diagonal; if $X$ is off-diagonal, $[A,X]$ is block diagonal. So $[A,H_0]$ is off-diagonal, and $[A,[A,X]]$ has the same block type as $X$.

> [!note]- Why a commutator with $A$ flips the block type
> Write an operator as a $2\times2$ array of blocks, with rows and columns labeled by $P$ and $Q$, and abbreviate $PXQ$ as $X_{PQ}$ and so on. A block-diagonal operator $X$ and an off-diagonal operator $Y$ are
>
> $$
> X=\begin{pmatrix}X_{PP}&0\\0&X_{QQ}\end{pmatrix},\qquad Y=\begin{pmatrix}0&Y_{PQ}\\Y_{QP}&0\end{pmatrix}.
> $$
>
> Multiplying such arrays,
>
> $$
> XX'=\begin{pmatrix}X_{PP}X'_{PP}&0\\0&X_{QQ}X'_{QQ}\end{pmatrix},\qquad
> YY'=\begin{pmatrix}Y_{PQ}Y'_{QP}&0\\0&Y_{QP}Y'_{PQ}\end{pmatrix},
> $$
>
> $$
> XY=\begin{pmatrix}0&X_{PP}Y_{PQ}\\X_{QQ}Y_{QP}&0\end{pmatrix},\qquad
> YX=\begin{pmatrix}0&Y_{PQ}X_{QQ}\\Y_{QP}X_{PP}&0\end{pmatrix}.
> $$
>
> Products behave like products of even and odd functions: two factors of the same kind give a block-diagonal operator, two of different kinds an off-diagonal one. A commutator is a difference of two such products, so it follows the same rule. With $A$ off-diagonal, $[A,X]$ is off-diagonal and $[A,Y]$ is block diagonal.

If $V$ vanishes, no rotation is needed, so $A$ starts at first order, $A=\lambda A_1+\lambda^2A_2+\cdots$. Substituting into the BCH series and collecting powers of $\lambda$,

$$
\begin{aligned}
\tilde H^{(1)} &= V + [A_1, H_0],\\
\tilde H^{(2)} &= [A_2, H_0] + [A_1, V] + \tfrac12[A_1,[A_1,H_0]] ,
\end{aligned}
$$

and so on. At each order we choose the new generator to cancel whatever is off-diagonal.

> [!note]- Collecting powers of $\lambda$
> Insert $H=H_0+\lambda V$ and $A=\lambda A_1+\lambda^2A_2+\cdots$ into the BCH series and keep everything through $\lambda^2$. The single commutator gives
>
> $$
> [A,H]=\lambda\,[A_1,H_0]+\lambda^2\big([A_2,H_0]+[A_1,V]\big)+O(\lambda^3) .
> $$
>
> The double commutator starts at second order, because each factor of $A$ brings at least one $\lambda$,
>
> $$
> \tfrac12[A,[A,H]]=\tfrac12\lambda^2\,[A_1,[A_1,H_0]]+O(\lambda^3),
> $$
>
> and the triple commutator starts at third. Adding $H$ itself and sorting by powers of $\lambda$,
>
> $$
> \tilde H=H_0+\lambda\big(V+[A_1,H_0]\big)+\lambda^2\Big([A_2,H_0]+[A_1,V]+\tfrac12[A_1,[A_1,H_0]]\Big)+O(\lambda^3) .
> $$
>
> The brackets are $\tilde H^{(1)}$ and $\tilde H^{(2)}$. Order $n$ collects terms with at most $n$ nested commutators, and the generator $A_n$ appears in it only through $[A_n,H_0]$.

At first order, $[A_1,H_0]$ is off-diagonal, so it can cancel $V_{OD}$ and nothing else:

$$
[A_1, H_0] = -V_{OD} .
\tag{1}
$$
^eq-a1-condition

Then $\tilde H^{(1)} = V - V_{OD} = V_D$.

At second order we use Eq. (1) in the double commutator, which becomes $\tfrac12[A_1,-V_{OD}]$, and we split $[A_1,V]=[A_1,V_D]+[A_1,V_{OD}]$. By the block rule,

$$
\tilde H^{(2)} = \underbrace{[A_2, H_0] + [A_1, V_D]}_{\text{off-diagonal}} + \underbrace{\tfrac12[A_1, V_{OD}]}_{\text{block diagonal}} .
$$

The off-diagonal part is removed by choosing

$$
[A_2, H_0] = -[A_1, V_D] ,
\tag{2}
$$
^eq-a2-condition

and the block-diagonal part, $\tfrac12[A_1,V_{OD}]$, is what survives. The third order works the same way; its block-diagonal part turns out to be $\tfrac12[A_2,V_{OD}]$ (callout below).

The effective Hamiltonian is the $P$ block of the rotated Hamiltonian, $H_{\rm eff}=P\tilde HP$. Order by order,

$$
\begin{aligned}
H^{(0)}&=PH_0P, & H^{(1)}&=PVP,\\
H^{(2)}&=\tfrac12P[A_1,V_{OD}]P, & H^{(3)}&=\tfrac12P[A_2,V_{OD}]P .
\end{aligned}
\tag{3}
$$
^eq-heff-orders

> [!note]- The third order of the rotation
> Collect the terms of order $\lambda^3$ in the BCH series:
>
> $$
> \tilde H^{(3)}=[A_3,H_0]+[A_2,V]+\tfrac12\Big([A_1,[A_2,H_0]]+[A_2,[A_1,H_0]]+[A_1,[A_1,V]]\Big)+\tfrac16[A_1,[A_1,[A_1,H_0]]] .
> $$
>
> Use Eqs. [[#^eq-a1-condition|(1)]] and [[#^eq-a2-condition|(2)]] to remove every commutator with $H_0$ except the first:
>
> $$
> \tilde H^{(3)}=[A_3,H_0]+[A_2,V]-\tfrac12[A_1,[A_1,V_D]]-\tfrac12[A_2,V_{OD}]+\tfrac12[A_1,[A_1,V]]-\tfrac16[A_1,[A_1,V_{OD}]] .
> $$
>
> Split $V=V_D+V_{OD}$ in the second and fifth terms. The two terms with $[A_1,[A_1,V_D]]$ cancel, and
>
> $$
> \tilde H^{(3)}=[A_3,H_0]+[A_2,V_D]+\tfrac12[A_2,V_{OD}]+\tfrac13[A_1,[A_1,V_{OD}]] .
> $$
>
> By the block rule, $[A_3,H_0]$ and $[A_2,V_D]$ are off-diagonal. So is $[A_1,[A_1,V_{OD}]]$, since two commutators with $A_1$ restore the block type of $V_{OD}$. Only $\tfrac12[A_2,V_{OD}]$ is block diagonal. The off-diagonal rest fixes $A_3$, which we would need only at fourth order.

Nothing so far refers to a basis, and nothing assumes anything about the energies inside $P$. Each order of $H_{\rm eff}$ is a commutator of a generator with $V_{OD}$, squeezed between two $P$'s. The energies enter only when we solve Eqs. [[#^eq-a1-condition|(1)]] and [[#^eq-a2-condition|(2)]] for the generators.

## Solving for the generator

[[#^eq-a1-condition|Eq. (1)]] is a linear equation for $A_1$, and we now solve it. Because $A_1$ is off-diagonal, it consists of two blocks, $QA_1P$ and $PA_1Q$, and anti-Hermiticity ties them together: $PA_1Q=-(QA_1P)^\dagger$. So it is enough to find $QA_1P$. Multiplying Eq. (1) by $Q$ from the left and by $P$ from the right, and using that $H_0$ commutes with both projectors, we get

$$
QA_1P\,H_0-H_0\,QA_1P=-QVP .
$$

Multiply from the right by $P_a$. Since $H_0P_a=E_aP_a$, the first term becomes $E_a\,QA_1P_a$, and

$$
(E_a-H_0)\,QA_1P_a=-QVP_a .
$$

On $Q$ the operator $E_a-H_0$ can be inverted, as long as no state of $Q$ has the energy $E_a$. The inverse is the resolvent restricted to $Q$,

$$
R(E)=\frac{Q}{E-H_0}=\sum_{\alpha\in Q}\frac{|\alpha\rangle\langle\alpha|}{E-E_\alpha} ,
$$

so $QA_1P_a=-R(E_a)VP_a$. Taking the adjoint gives $P_aA_1Q=P_aVR(E_a)$, and altogether

$$
A_1=QA_1P+PA_1Q=\sum_{a}\Big(P_aV\,R(E_a)-R(E_a)\,VP_a\Big) .
\tag{4}
$$
^eq-a1

This is the one step in which the energies of the model space enter, and **each model state brings its own**. The rotation turns $|a\rangle$ toward each state $\alpha$ of $Q$ by an angle equal to their coupling over their distance, $\langle\alpha|V|a\rangle/(E_a-E_\alpha)$.

> [!example]- What Eq. (4) does to the states
> Acting on a model state, only the second term of Eq. (4) survives, because $R(E_b)|a\rangle=0$:
>
> $$
> A_1|a\rangle=-R(E_a)V|a\rangle=-\sum_{\alpha\in Q}|\alpha\rangle\,\frac{\langle\alpha|V|a\rangle}{E_a-E_\alpha} .
> $$
>
> Acting on an external state, only the first survives:
>
> $$
> A_1|\alpha\rangle=\sum_{b\in P} P_bV R(E_b)|\alpha\rangle=\sum_{b\in P} P_bV\frac{Q}{E_b-H_0}|\alpha\rangle=\sum_{b\in P}|b\rangle\,\frac{\langle b|V|\alpha\rangle}{E_b-E_\alpha} .
> $$
>
> To see what this means, keep a single model state $|a\rangle$ and a single external state $|\alpha\rangle$, with a real coupling $v=\langle a|V|\alpha\rangle$, and let $\theta=v/(E_a-E_\alpha)$. In the basis $(|a\rangle,|\alpha\rangle)$,
>
> $$
> A_1=\begin{pmatrix}0&\theta\\-\theta&0\end{pmatrix},\qquad e^{-A_1}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix} .
> $$
>
> So $e^{-A_1}$ is a rotation by the angle $\theta$ in the plane of $|a\rangle$ and $|\alpha\rangle$. It carries $|a\rangle$ into the dressed state of [[Van Vleck 00 - Near and far#A change of basis|near and far]],
>
> $$
> |\tilde a\rangle=e^{-A_1}|a\rangle=\cos\theta\,|a\rangle+\sin\theta\,|\alpha\rangle\approx|a\rangle+\theta\,|\alpha\rangle .
> $$
>
> How good is this? For these two states the full Hamiltonian $H=H_0+V$ is the $2\times2$ matrix
>
> $$
> H=\begin{pmatrix}E_a&v\\v&E_\alpha\end{pmatrix} ,
> $$
>
> and its exact eigenvector that grows out of $|a\rangle$ is $\cos\varphi\,|a\rangle+\sin\varphi\,|\alpha\rangle$, with $\tan2\varphi=2v/(E_a-E_\alpha)=2\theta$ ([[Van Vleck 00 - Near and far#^eq-two-level-dressed|near and far]]). For small $\theta$, $\varphi=\tfrac12\arctan2\theta=\theta-\tfrac43\theta^3+\cdots$. The first-order rotation gives the exact eigenvector, up to terms of third order in the angle.
>
> With many states, Eq. (4) is a sum of such small rotations, one in the plane of every pair $(a,\alpha)$, each by its own angle, coupling over distance. The angle is measured from the energy of its own model state, which is why every $P_a$ in Eq. (4) comes with its own $R(E_a)$. For all angles to be small, every external state must be far from every model state, which is the requirement of [[#Two subspaces]]. What the dressed states look like then, and at higher orders, is the subject of [[Van Vleck 02 - Dressed states and rotated operators|dressed states and rotated operators]].

When the model space is degenerate, $E_a=E_0$ for every $a$, the sum in Eq. (4) collapses to an operator that needs no basis at all:

$$
A_1=PVR-RVP,\qquad R\equiv R(E_0) .
$$

Eq. (4) also shows where the theory breaks down. $R(E_a)$ blows up when a state of $Q$ approaches $E_a$, which is the requirement of [[#Two subspaces]] seen from the inside ([[Van Vleck 03 - Errors#When the folding fails|when the folding fails]]).

## Second order

Inserting [[#^eq-a1|Eq. (4)]] into $H^{(2)}=\tfrac12P[A_1,V_{OD}]P=\tfrac12\big(PA_1Q\,VP-PV\,QA_1P\big)$ gives

$$
H^{(2)}=\frac12\sum_{a,b}P_a\,V\Big[R(E_a)+R(E_b)\Big]V\,P_b .
\tag{5}
$$
^eq-h2

> [!note]- The substitution behind Eq. (5)
> The generator only crosses between the subspaces, so $PA_1=PA_1Q$ and $A_1P=QA_1P$, while $V_{OD}$ between $P$ and $Q$ is simply $V$. That is how the commutator became the two products above. Now write $P=\sum_aP_a$ on the left and $P=\sum_bP_b$ on the right, so that every term carries its two end states:
>
> $$
> H^{(2)}=\frac12\sum_{a,b}\Big(P_aA_1Q\,VP_b-P_aV\,QA_1P_b\Big) .
> $$
>
> [[#^eq-a1|Eq. (4)]] supplies both blocks of the generator. Its first term has a model state on the left and $Q$ on the right, inside the resolvent; its second term has them the other way round. So
>
> $$
> P_aA_1Q=P_aV\,R(E_a),\qquad QA_1P_b=-R(E_b)\,VP_b .
> $$
>
> Substituting both,
>
> $$
> H^{(2)}=\frac12\sum_{a,b}\Big(P_aV\,R(E_a)\,VP_b+P_aV\,R(E_b)\,VP_b\Big) ,
> $$
>
> which is Eq. (5).

Eq. (5) shows something that a degenerate model space would hide. Between $\langle a|$ and $|b\rangle$ the excursion into $Q$ is described by two resolvents, $R(E_a)$ and $R(E_b)$. The distance of each intermediate state is measured once from the energy of the bra's state and once from that of the ket's state, and the two are averaged. In a degenerate model space $E_a=E_b$ and the distinction disappears; in general the two denominators differ.

The commutator shows where the two energies come from. $P[A_1,V_{OD}]P$ has two terms, one with the generator to the left of $V$ and one with it to the right. By [[#^eq-a1|Eq. (4)]], the first brings the rotation of the bra's state, with $E_a$, and the second the rotation of the ket's state, with $E_b$. The $\tfrac12$ from the BCH series gives each of them half the weight.

To get matrix elements, we sandwich Eq. (5) between $\langle a|$ and $|b\rangle$ and insert $Q=\sum_\alpha|\alpha\rangle\langle\alpha|$. Together with the first two orders,

$$
\begin{aligned}
\langle a|H_{\rm eff}|b\rangle={}&E_a\delta_{ab}+\langle a|V|b\rangle\\
&+\frac12\sum_{\alpha\in Q}\langle a|V|\alpha\rangle\langle\alpha|V|b\rangle\left(\frac{1}{E_a-E_\alpha}+\frac{1}{E_b-E_\alpha}\right)+O(V^3) .
\end{aligned}
\tag{6}
$$
^eq-h2-elements

The second-order term has a simple reading. The system leaves $P$ through $V$, spends a while in an intermediate state $\alpha$ that it cannot really afford, and returns to $P$ through $V$ again. The denominators measure how far off the energy shell the excursion is, seen from either end.

Three special cases are worth having at hand.

When the model space is degenerate, $E_a=E_0$ for every $a$, the two resolvents in [[#^eq-h2|Eq. (5)]] are the same, and the sums over $a$ and $b$ rebuild $P$ on both sides:

$$
H_{\rm eff}=E_0P+PVP+PV\,R\,VP+O(V^3),\qquad R=\frac{Q}{E_0-H_0} .
\tag{7}
$$
^eq-h2-degenerate

No basis is needed at any point, since with one energy in the model space [[#^eq-a1|Eq. (4)]] is already basis free. $R$ is the propagator of the virtual excursion.

When the model space is only nearly degenerate, with a spread small compared with every distance to $Q$, we may still use Eq. (7) with any $E_0$ inside the spread, at a relative error of the spread over the distance. For Zeeman sublevels a few hertz apart, folded against electronic states hundreds of THz away, that is $10^{-14}$. For the Stark-mixed rotational levels of a polar molecule, tens of GHz against the same hundreds of THz, it is $10^{-4}$.

When the model space holds a single state, $P=|a\rangle\langle a|$, [[#^eq-h2-elements|Eq. (6)]] is a number,

$$
E_a+\langle a|V|a\rangle+\sum_{\alpha\neq a}\frac{|\langle a|V|\alpha\rangle|^2}{E_a-E_\alpha} ,
$$

the second-order energy of non-degenerate (Rayleigh–Schrödinger) perturbation theory.

> [!example]- A two-level check
> Take one state in each subspace, $P=\{|1\rangle\}$ and $Q=\{|2\rangle\}$, with
>
> $$
> H_0=\begin{pmatrix}0&0\\0&\Delta\end{pmatrix},\qquad V=\begin{pmatrix}0&v\\v^*&0\end{pmatrix},
> $$
>
> and $\Delta>0$, so that $|1\rangle$ is the lower level. With $E_1=0$, $E_2=\Delta$ and $\langle1|V|1\rangle=0$, the single-state formula above gives
>
> $$
> H_{\rm eff}=0+0+\frac{|v|^2}{0-\Delta}=-\frac{|v|^2}{\Delta} .
> $$
>
> The exact eigenvalues of $H_0+V$ are $\tfrac12\big(\Delta\pm\sqrt{\Delta^2+4|v|^2}\big)$, and the lower one grows out of $|1\rangle$. Write the square root as $\Delta\sqrt{1+x}$ with $x=4|v|^2/\Delta^2$, and expand $\sqrt{1+x}=1+\tfrac12x-\tfrac18x^2+\cdots$:
>
> $$
> \frac{\Delta-\sqrt{\Delta^2+4|v|^2}}{2}=\frac{\Delta}{2}\Big(1-\sqrt{1+x}\Big)=-\frac{|v|^2}{\Delta}+\frac{|v|^4}{\Delta^3}-\cdots .
> $$
>
> The second-order formula reproduces the first term. The first correction is smaller by $|v|^2/\Delta^2$, the square of the angle, coupling over distance. There is no third-order term in between, because $V$ has no diagonal elements here; [[Van Vleck 03 - Errors#Stopping|errors]] explains when this happens in general.

Textbook degenerate perturbation theory is organized differently from Eq. (7). It first diagonalizes $V$ inside the degenerate level and then applies the non-degenerate formulas to the new states. That works when $PVP$ lifts the degeneracy. When it does not, as for the light shifts of an atomic ground level, where $PVP=0$ and the splitting first appears in $PVRVP$, the recipe needs care. Eq. (7) simply hands us the operator to diagonalize, first and second order together.

## Third order

The third order follows the same pattern, with one step more: $H^{(3)}=\tfrac12P[A_2,V_{OD}]P$ needs the second generator. [[#^eq-a2-condition|Eq. (2)]] fixes $A_2$ in the same way as [[#^eq-a1-condition|Eq. (1)]] fixed $A_1$, with $[A_1,V_D]$ in place of $V$. Taking its $QP$ block and multiplying by $P_a$ from the right, exactly as before,

$$
QA_2P_a=-R(E_a)\,Q[A_1,V_D]P_a .
$$

So we need the $QP$ block of the commutator $[A_1,V_D]=A_1V_D-V_DA_1$. Between $Q$ and $P_a$, each of the two products has a single route, because $A_1$ only crosses between the subspaces and $V_D$ never does:

$$
Q[A_1,V_D]P_a=QA_1P\cdot PVP_a-QVQ\cdot QA_1P_a .
$$

Both factors of $A_1$ come from [[#^eq-a1|Eq. (4)]]: $QA_1P=-\sum_cR(E_c)\,VP_c$ and $QA_1P_a=-R(E_a)\,VP_a$. Substituting them, and using that the resolvent already contains $Q$,

$$
\begin{aligned}
Q[A_1,V_D]P_a&=-\sum_cR(E_c)\,VP_c\,VP_a+QVQ\,R(E_a)\,VP_a\\
&=QV\,R(E_a)\,VP_a-\sum_{c}R(E_c)\,VP_cVP_a .
\end{aligned}
$$

The two terms are the two orders in which the first rotation and $V_D$ can act. In the first, the rotation takes $|a\rangle$ out into $Q$, and $V$ then moves the system within $Q$. In the second, $V$ first acts inside $P$, taking $|a\rangle$ to $|c\rangle$, and the rotation then takes $|c\rangle$ out, with its own energy $E_c$. Altogether,

$$
QA_2P_a=-R(E_a)\,V\,R(E_a)\,VP_a+\sum_cR(E_a)R(E_c)\,VP_cVP_a .
$$

Inserting this into $H^{(3)}=\tfrac12\big(PA_2Q\,VP-PV\,QA_2P\big)$, with $PA_2Q=-(QA_2P)^\dagger$, gives

$$
\begin{aligned}
H^{(3)}=\frac12\sum_{a,b}P_a\Big\{&V\Big[R(E_a)\,V\,R(E_a)+R(E_b)\,V\,R(E_b)\Big]V\\
&-\sum_c\Big[VP_cV\,R(E_c)R(E_a)\,V+V\,R(E_b)R(E_c)\,VP_cV\Big]\Big\}P_b .
\end{aligned}
\tag{8}
$$
^eq-h3

> [!note]- The substitution behind Eq. (8)
> As at second order, write $P=\sum_aP_a$ on the left and $P=\sum_bP_b$ on the right:
>
> $$
> H^{(3)}=\frac12\sum_{a,b}\Big(P_aA_2Q\,VP_b-P_aV\,QA_2P_b\Big) .
> $$
>
> The block $QA_2P_b$ is the result just found, with $a$ renamed $b$:
>
> $$
> QA_2P_b=-R(E_b)\,V\,R(E_b)\,VP_b+\sum_cR(E_b)R(E_c)\,VP_cVP_b .
> $$
>
> The other block follows from anti-Hermiticity, $P_aA_2Q=-(QA_2P_a)^\dagger$. The operators $V$, $P_c$ and $R(E)$ are Hermitian, so the adjoint simply reverses the order of each product:
>
> $$
> P_aA_2Q=P_aV\,R(E_a)\,V\,R(E_a)-\sum_cP_aVP_cV\,R(E_c)R(E_a) .
> $$
>
> Now attach the remaining $V$ to each block:
>
> $$
> \begin{aligned}
> P_aA_2Q\,VP_b&=P_a\Big[V\,R(E_a)\,V\,R(E_a)\,V-\sum_cVP_cV\,R(E_c)R(E_a)\,V\Big]P_b ,\\
> -P_aV\,QA_2P_b&=P_a\Big[V\,R(E_b)\,V\,R(E_b)\,V-\sum_cV\,R(E_b)R(E_c)\,VP_cV\Big]P_b .
> \end{aligned}
> $$
>
> Half their sum, summed over $a$ and $b$, is Eq. (8). For a degenerate model space every resolvent is $R$. The first bracket of Eq. (8) becomes $2RVR$, the sum over $c$ turns $VP_cV$ into $VPV$, and the sums over $a$ and $b$ rebuild $P$ on both sides, which gives Eq. (9) below.

For a degenerate model space every resolvent is $R$, and Eq. (8) becomes

$$
H^{(3)}=PVRVRVP-\tfrac12\Big(PVP\cdot PVR^2VP+PVR^2VP\cdot PVP\Big) .
\tag{9}
$$
^eq-h3-degenerate

Its matrix elements, in the general case of Eq. (8), are

$$
\begin{aligned}
\langle a|H^{(3)}|b\rangle={}&\frac12\sum_{\alpha,\beta\in Q}V_{a\alpha}V_{\alpha\beta}V_{\beta b}\left[\frac{1}{(E_a-E_\alpha)(E_a-E_\beta)}+\frac{1}{(E_b-E_\alpha)(E_b-E_\beta)}\right]\\
&-\frac12\sum_{c\in P}\sum_{\alpha\in Q}\left[\frac{V_{ac}V_{c\alpha}V_{\alpha b}}{(E_a-E_\alpha)(E_c-E_\alpha)}+\frac{V_{a\alpha}V_{\alpha c}V_{cb}}{(E_b-E_\alpha)(E_c-E_\alpha)}\right],
\end{aligned}
\tag{10}
$$
^eq-h3-elements

with $V_{a\alpha}\equiv\langle a|V|\alpha\rangle$ and so on. This is the form given by R. Winkler, *Spin–Orbit Coupling Effects in Two-Dimensional Electron and Hole Systems* (Springer, 2003), Appendix B. [`check_van_vleck.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck.py) checks Eqs. (5) to (10) against one another and against exact diagonalization.

The two kinds of terms have simple readings, easiest to see in Eq. (9).

The first is an excursion with two steps outside: the system leaves $P$, hops from one intermediate state to another through $QVQ$, and returns.

The second needs $V$ to act inside $P$. The operator

$$
PVR^2VP=\sum_{\alpha\in Q}\frac{PV|\alpha\rangle\langle\alpha|VP}{(E_0-E_\alpha)^2}
$$

is the norm of the first-order admixture, so its expectation value in a model state is the probability of finding the system outside $P$ ([[Van Vleck 02 - Dressed states and rotated operators#The second-order dressing|dressed states]]). The term $-\tfrac12\{PVP,PVR^2VP\}$ says that the couplings inside $P$ act only while the system is actually in $P$. Equivalently, it corrects the distances: $PVP$ moves the true energy away from $E_0$, and every excursion is really measured from there.

For a single state both readings are visible at once. With $a=b=c$, Eq. (10) is

$$
\sum_{\alpha,\beta\neq a}\frac{V_{a\alpha}V_{\alpha\beta}V_{\beta a}}{(E_a-E_\alpha)(E_a-E_\beta)}-V_{aa}\sum_{\alpha\neq a}\frac{|V_{a\alpha}|^2}{(E_a-E_\alpha)^2},
$$

the third-order energy of Rayleigh–Schrödinger theory. Its last term is the first-order shift $V_{aa}$ times the energy derivative of the second-order term. When $PVP=0$, as for a level of definite parity and a perturbation that is odd under parity, the second kind of term vanishes altogether.

## What the formulas leave open

The main line ends here, with $H_{\rm eff}$ through third order, as operators and as matrix elements. Several questions were set aside on the way, and each has a note of its own.

The basis states of $P$ stand for dressed states. What these look like order by order, how they explain the averaged denominators of [[#^eq-h2|Eq. (5)]], and why every other operator we measure must be rotated with the same generator, is taken up in [[Van Vleck 02 - Dressed states and rotated operators|dressed states and rotated operators]].

We stopped the series at some order and measured every distance from unperturbed energies. How large the resulting errors are, how the averaged denominators compare with an exact folding of the eigenvalue equation, and when the construction fails altogether, is the subject of [[Van Vleck 03 - Errors|errors]].

Finally, $H_{\rm eff}$ inherits the symmetries of $H$, which often fixes its form before any coefficient is computed. [[Van Vleck 04 - Symmetries|Symmetries]] explains why, and what this asks of the model space.
