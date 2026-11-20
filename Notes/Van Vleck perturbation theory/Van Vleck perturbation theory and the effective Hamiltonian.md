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

We want an effective Hamiltonian that acts only on a few of the states and still knows about all the others. Why we want it, and how to choose the few, is the subject of [[Van Vleck perturbation theory - near and far|near and far]].

## Two subspaces

The *model space* $P$ is spanned by eigenstates $|a\rangle,|b\rangle,|c\rangle,\dots$ of $H_0$, with $H_0|a\rangle=E_a|a\rangle$. Some of the $E_a$ may coincide, and nothing below requires them to be equal or different. The *external space* $Q$ holds everything else, with eigenstates $|\alpha\rangle,|\beta\rangle,\dots$ and energies $E_\alpha$. Using the same letters for the projectors,

$$
P=\sum_a P_a,\qquad P_a=|a\rangle\langle a|,\qquad P+Q=1,\qquad [H_0,P]=[H_0,Q]=0 .
$$

The one requirement is that every state of $Q$ be far from every state of $P$:

$$
|\langle a|V|\alpha\rangle| \ll |E_a - E_\alpha|\qquad\text{for all } a\in P,\ \alpha\in Q .
$$

Inside $P$ nothing is required. Its states may be degenerate or not, and $V$ may couple them strongly, because in the end we diagonalize the effective Hamiltonian exactly. (The one proviso, that these couplings must not push the model states toward $Q$, is taken up in [[Van Vleck perturbation theory - dressed states, errors and symmetries#Where the errors are|the companion note]].)

It helps to split every operator $X$ into its block-diagonal and off-diagonal parts,

$$
X_D = PXP + QXQ,\qquad X_{OD} = PXQ + QXP .
$$

$H_0$ is block diagonal. $V$ generally has both parts, and $V_{OD}$ is the troublemaker: it is what ties our states to the rest of the world.

## Rotating the Hamiltonian

We look for a unitary transformation $e^{A}$, with $A$ anti-Hermitian, $A^\dagger=-A$, such that

$$
\tilde H = e^{A} H e^{-A}
$$

has no off-diagonal block, at least up to the order we need. (Many texts write $A=iS$ with a Hermitian $S$.) Once that is true, $P\tilde H P$ is a Hamiltonian on $P$ alone. Its eigenvalues are eigenvalues of $H$ to that order, because a unitary transformation does not change the spectrum.

The Baker–Campbell–Hausdorff formula expands $\tilde H$ in nested commutators,

$$
\tilde H = H + [A, H] + \frac{1}{2!}[A,[A,H]] + \frac{1}{3!}[A,[A,[A,H]]] + \cdots
$$

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

At first order, $[A_1,H_0]$ is off-diagonal, so it can cancel $V_{OD}$ and nothing else:

$$
[A_1, H_0] = -V_{OD} .
\tag{1}
$$

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

and the block-diagonal part, $\tfrac12[A_1,V_{OD}]$, is what survives. The third order works the same way; its block-diagonal part turns out to be $\tfrac12[A_2,V_{OD}]$ (callout below).

The effective Hamiltonian is the $P$ block of the rotated Hamiltonian, $H_{\rm eff}=P\tilde HP$. Order by order,

$$
\begin{aligned}
H^{(0)}&=PH_0P, & H^{(1)}&=PVP,\\
H^{(2)}&=\tfrac12P[A_1,V_{OD}]P, & H^{(3)}&=\tfrac12P[A_2,V_{OD}]P .
\end{aligned}
\tag{3}
$$

> [!note]- The third order of the rotation
> Collect the terms of order $\lambda^3$ in the BCH series:
>
> $$
> \tilde H^{(3)}=[A_3,H_0]+[A_2,V]+\tfrac12\Big([A_1,[A_2,H_0]]+[A_2,[A_1,H_0]]+[A_1,[A_1,V]]\Big)+\tfrac16[A_1,[A_1,[A_1,H_0]]] .
> $$
>
> Use Eqs. (1) and (2) to remove every commutator with $H_0$ except the first:
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

Nothing so far refers to a basis, and nothing assumes anything about the energies inside $P$. Each order of $H_{\rm eff}$ is a commutator of a generator with $V_{OD}$, squeezed between two $P$'s. The energies enter only when we solve Eqs. (1) and (2) for the generators.

## Solving for the generator

Eq. (1) is a linear equation for $A_1$, and we now solve it. Because $A_1$ is off-diagonal, it consists of two blocks, $QA_1P$ and $PA_1Q$, and anti-Hermiticity ties them together: $PA_1Q=-(QA_1P)^\dagger$. So it is enough to find $QA_1P$. Multiplying Eq. (1) by $Q$ from the left and by $P$ from the right, and using that $H_0$ commutes with both projectors, we get

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
A_1=\sum_{a}\Big(P_aV\,R(E_a)-R(E_a)\,VP_a\Big) .
\tag{4}
$$

This is the one step in which the energies of the model space enter, and each model state brings its own. The rotation turns $|a\rangle$ toward each state $\alpha$ of $Q$ by an angle equal to their coupling over their distance, $\langle\alpha|V|a\rangle/(E_a-E_\alpha)$.

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
> A_1|\alpha\rangle=\sum_{b\in P}|b\rangle\,\frac{\langle b|V|\alpha\rangle}{E_b-E_\alpha} .
> $$
>
> To see what this means, keep a single model state $|a\rangle$ and a single external state $|\alpha\rangle$, with a real coupling $v=\langle a|V|\alpha\rangle$, and let $\theta=v/(E_a-E_\alpha)$. In the basis $(|a\rangle,|\alpha\rangle)$,
>
> $$
> A_1=\begin{pmatrix}0&\theta\\-\theta&0\end{pmatrix},\qquad e^{-A_1}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix} .
> $$
>
> So $e^{-A_1}$ is a rotation by the angle $\theta$ in the plane of $|a\rangle$ and $|\alpha\rangle$. It carries $|a\rangle$ into $\cos\theta\,|a\rangle+\sin\theta\,|\alpha\rangle\approx|a\rangle+\theta\,|\alpha\rangle$. The exact eigenvector of the $2\times2$ problem is rotated by an angle $\phi$ with $\tan2\phi=2\theta$, which agrees with $\theta$ to first order.
>
> With many states, Eq. (4) is a sum of such small rotations, one in the plane of every pair $(a,\alpha)$, each by its own angle, coupling over distance. The angle is measured from the energy of its own model state, which is why every $P_a$ in Eq. (4) comes with its own $R(E_a)$. For all angles to be small, every external state must be far from every model state, which is the requirement of [[#Two subspaces]].

When the model space is degenerate, $E_a=E_0$ for every $a$, the sum in Eq. (4) collapses to an operator that needs no basis at all:

$$
A_1=PVR-RVP,\qquad R\equiv R(E_0) .
$$

Eq. (4) also shows where the theory breaks down. $R(E_a)$ blows up when a state of $Q$ approaches $E_a$, which is the requirement of [[#Two subspaces]] seen from the inside ([[Van Vleck perturbation theory - dressed states, errors and symmetries#When the folding fails|when the folding fails]]).

## Second order

Inserting Eq. (4) into $H^{(2)}=\tfrac12P[A_1,V_{OD}]P=\tfrac12\big(PA_1Q\,VP-PV\,QA_1P\big)$ gives

$$
H^{(2)}=\frac12\sum_{a,b}P_a\,V\Big[R(E_a)+R(E_b)\Big]V\,P_b .
\tag{5}
$$

Eq. (5) shows something that a degenerate model space would hide. Between $\langle a|$ and $|b\rangle$ the excursion into $Q$ is described by two resolvents, $R(E_a)$ and $R(E_b)$. The distance of each intermediate state is measured once from the energy of the bra's state and once from that of the ket's state, and the two are averaged. In a degenerate model space $E_a=E_b$ and the distinction disappears; in general the two denominators differ.

The commutator shows where the two energies come from. $P[A_1,V_{OD}]P$ has two terms, one with the generator to the left of $V$ and one with it to the right. By Eq. (4), the first brings the rotation of the bra's state, with $E_a$, and the second the rotation of the ket's state, with $E_b$. The $\tfrac12$ from the BCH series gives each of them half the weight.

The same thing looks more natural in terms of states. The rotation $e^{A}$ is a change of basis, and the basis state $|a\rangle$ of $P$ stands for the dressed state $|\tilde a\rangle=e^{-A}|a\rangle$. Since $e^{A}$ is unitary, $\langle a|e^{A}=\langle\tilde a|$, and

$$
\langle a|H_{\rm eff}|b\rangle=\langle a|e^{A}He^{-A}|b\rangle=\langle\tilde a|H|\tilde b\rangle .
$$

The effective Hamiltonian is the true Hamiltonian written in the basis of dressed states. To first order, by Eq. (4), $|\tilde a\rangle=|a\rangle+R(E_a)V|a\rangle$: every model state is dressed with the external states, with denominators measured from its own energy. A matrix element has a dressed state at each end, so it carries both energies, and it carries them symmetrically. The callout below checks that the two dressings combine into exactly the average of Eq. (5).

The dressed states are not eigenstates of $H$. They form the basis in which $H$ no longer connects $P$ to $Q$, while inside $P$ it still has matrix elements between them, and diagonalizing $H_{\rm eff}$ takes care of those. Nor is Hermiticity something we have to impose. Both ends of every matrix element are dressed in the same way, so $\langle\tilde a|H|\tilde b\rangle^*=\langle\tilde b|H|\tilde a\rangle$ automatically. What the dressed states look like beyond first order is taken up in [[Van Vleck perturbation theory - dressed states, errors and symmetries#What the model states stand for|the companion note]].

> [!note]- The average from the dressed states
> To second order, $e^{-A}|b\rangle=|b\rangle-A_1|b\rangle-A_2|b\rangle+\tfrac12A_1^2|b\rangle$. Write $R_b\equiv R(E_b)$. By Eq. (4), $-A_1|b\rangle=R_bV|b\rangle$ lies in $Q$, while
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
> the average of Eq. (5). The first two terms alone, the coupling of a bare end to a dressed one, would count the excursion twice. The energy carried by the admixtures removes half of it.

Is the average the exact answer, or one convenient choice among several? Compared with an exact folding, every reasonable choice gives the same eigenvalues at second order, and the true energies enter only at third. The average is the choice that keeps $H_{\rm eff}$ Hermitian and independent of the energy we are looking for ([[Van Vleck perturbation theory - dressed states, errors and symmetries#How exact the average is|how exact the average is]]).

To get matrix elements, we sandwich Eq. (5) between $\langle a|$ and $|b\rangle$ and insert $Q=\sum_\alpha|\alpha\rangle\langle\alpha|$. Together with the first two orders,

$$
\begin{aligned}
\langle a|H_{\rm eff}|b\rangle={}&E_a\delta_{ab}+\langle a|V|b\rangle\\
&+\frac12\sum_{\alpha\in Q}\langle a|V|\alpha\rangle\langle\alpha|V|b\rangle\left(\frac{1}{E_a-E_\alpha}+\frac{1}{E_b-E_\alpha}\right)+O(V^3) .
\end{aligned}
\tag{6}
$$

The second-order term has a simple reading. The system leaves $P$ through $V$, spends a while in an intermediate state $\alpha$ that it cannot really afford, and returns to $P$ through $V$ again. The denominators measure how far off the energy shell the excursion is, seen from either end.

Three special cases are worth having at hand.

When the model space is degenerate, $E_a=E_0$ for every $a$, the two resolvents in Eq. (5) are the same, and the sums over $a$ and $b$ rebuild $P$ on both sides:

$$
H_{\rm eff}=E_0P+PVP+PV\,R\,VP+O(V^3),\qquad R=\frac{Q}{E_0-H_0} .
\tag{7}
$$

No basis is needed at any point, since with one energy in the model space Eq. (4) is already basis free. $R$ is the propagator of the virtual excursion.

When the model space is only nearly degenerate, with a spread small compared with every distance to $Q$, we may still use Eq. (7) with any $E_0$ inside the spread, at a relative error of the spread over the distance. For Zeeman sublevels a few hertz apart, folded against electronic states hundreds of THz away, that is $10^{-14}$. For the Stark-mixed rotational levels of a polar molecule, tens of GHz against the same hundreds of THz, it is $10^{-4}$.

When the model space holds a single state, $P=|a\rangle\langle a|$, Eq. (6) is a number,

$$
E_a+\langle a|V|a\rangle+\sum_{\alpha\neq a}\frac{|\langle a|V|\alpha\rangle|^2}{E_a-E_\alpha} ,
$$

the second-order energy of non-degenerate (Rayleigh–Schrödinger) perturbation theory.

Textbook degenerate perturbation theory is organized differently from Eq. (7). It first diagonalizes $V$ inside the degenerate level and then applies the non-degenerate formulas to the new states. That works when $PVP$ lifts the degeneracy. When it does not, as for the light shifts of an atomic ground level, where $PVP=0$ and the splitting first appears in $PVRVP$, the recipe needs care. Eq. (7) simply hands us the operator to diagonalize, first and second order together.

A two-level system makes a quick check. Take $P=\{|1\rangle\}$ and $Q=\{|2\rangle\}$ with $H_0=\mathrm{diag}(0,\Delta)$ and a coupling $v$ between them. Eq. (6) gives $-|v|^2/\Delta$. The exact lower eigenvalue is $\tfrac12\big(\Delta-\sqrt{\Delta^2+4|v|^2}\big)=-|v|^2/\Delta+|v|^4/\Delta^3-\cdots$, so the two agree at second order, and the first correction is smaller by $|v/\Delta|^2$.

## Third order

The third order follows the same pattern, with one step more: $H^{(3)}=\tfrac12P[A_2,V_{OD}]P$ needs the second generator. Eq. (2) fixes $A_2$ in the same way as Eq. (1) fixed $A_1$, with $[A_1,V_D]$ in place of $V$. Taking its $QP$ block and multiplying by $P_a$ from the right, exactly as before,

$$
QA_2P_a=-R(E_a)\,Q[A_1,V_D]P_a .
$$

So we need the $QP$ block of the commutator $[A_1,V_D]=A_1V_D-V_DA_1$. Between $Q$ and $P_a$, each of the two products has a single route, because $A_1$ only crosses between the subspaces and $V_D$ never does:

$$
Q[A_1,V_D]P_a=QA_1P\cdot PVP_a-QVQ\cdot QA_1P_a .
$$

With $QA_1P_c=-R(E_c)VP_c$ from Eq. (4) for both factors of $A_1$,

$$
Q[A_1,V_D]P_a=QV\,R(E_a)\,VP_a-\sum_{c}R(E_c)\,VP_cVP_a .
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

For a degenerate model space every resolvent is $R$, and Eq. (8) becomes

$$
H^{(3)}=PVRVRVP-\tfrac12\Big(PVP\cdot PVR^2VP+PVR^2VP\cdot PVP\Big) .
\tag{9}
$$

Its matrix elements, in the general case of Eq. (8), are

$$
\begin{aligned}
\langle a|H^{(3)}|b\rangle={}&\frac12\sum_{\alpha,\beta\in Q}V_{a\alpha}V_{\alpha\beta}V_{\beta b}\left[\frac{1}{(E_a-E_\alpha)(E_a-E_\beta)}+\frac{1}{(E_b-E_\alpha)(E_b-E_\beta)}\right]\\
&-\frac12\sum_{c\in P}\sum_{\alpha\in Q}\left[\frac{V_{ac}V_{c\alpha}V_{\alpha b}}{(E_a-E_\alpha)(E_c-E_\alpha)}+\frac{V_{a\alpha}V_{\alpha c}V_{cb}}{(E_b-E_\alpha)(E_c-E_\alpha)}\right],
\end{aligned}
\tag{10}
$$

with $V_{a\alpha}\equiv\langle a|V|\alpha\rangle$ and so on. This is the form given by R. Winkler, *Spin–Orbit Coupling Effects in Two-Dimensional Electron and Hole Systems* (Springer, 2003), Appendix B. [`check_van_vleck.py`](https://github.com/SHAOZHEN545/theoretical-tools-for-amo/blob/main/checks/check_van_vleck.py) checks Eqs. (5) to (10) against one another and against exact diagonalization.

The two kinds of terms have simple readings, easiest to see in Eq. (9).

The first is an excursion with two steps outside: the system leaves $P$, hops from one intermediate state to another through $QVQ$, and returns.

The second needs $V$ to act inside $P$. The operator

$$
PVR^2VP=\sum_{\alpha\in Q}\frac{PV|\alpha\rangle\langle\alpha|VP}{(E_0-E_\alpha)^2}
$$

is the norm of the first-order admixture, so its expectation value in a model state is the probability of finding the system outside $P$. The term $-\tfrac12\{PVP,PVR^2VP\}$ says that the couplings inside $P$ act only while the system is actually in $P$. Equivalently, it corrects the distances: $PVP$ moves the true energy away from $E_0$, and every excursion is really measured from there. The exact folding produces both kinds of terms, as [[Van Vleck perturbation theory - dressed states, errors and symmetries#How exact the average is|the companion note]] shows.

For a single state both readings are visible at once. With $a=b=c$, Eq. (10) is

$$
\sum_{\alpha,\beta\neq a}\frac{V_{a\alpha}V_{\alpha\beta}V_{\beta a}}{(E_a-E_\alpha)(E_a-E_\beta)}-V_{aa}\sum_{\alpha\neq a}\frac{|V_{a\alpha}|^2}{(E_a-E_\alpha)^2},
$$

the third-order energy of Rayleigh–Schrödinger theory. Its last term is the first-order shift $V_{aa}$ times the energy derivative of the second-order term. When $PVP=0$, as for a level of definite parity and a perturbation that is odd under parity, the second kind of term vanishes altogether.

This completes the main line. The questions the formulas leave open, from the meaning of the model states to the size of the errors, continue in [[Van Vleck perturbation theory - dressed states, errors and symmetries]].
