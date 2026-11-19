#!/usr/bin/env python3
"""Numerical checks of the formulas in
"Van Vleck perturbation theory and the effective Hamiltonian" (VV).

Run from the repository root:
    python checks/check_van_vleck.py

1. Van Vleck through third order, the matrix elements VV Eqs. (6) and (10), for a static
   random matrix whose model space is not degenerate. The eigenvalue error must fall as
   lambda^3 after second order and as lambda^4 after third order.
2. The operator forms VV Eqs. (5) and (8), with one resolvent per model state, against
   those matrix elements; the degenerate forms VV Eqs. (7) and (9) for a degenerate model
   space; and the single-state limit, Rayleigh-Schroedinger third order.
"""

import numpy as np

rng = np.random.default_rng(2026)


def random_hermitian(n, scale=1.0):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return scale * (a + a.conj().T) / 2


def heff_orders(E, V, P):
    """Van Vleck effective Hamiltonian on the model space P, order by order.

    E: diagonal of H0. V: Hermitian perturbation. P: indices of the model space.
    Returns [H^(0), H^(1), H^(2), H^(3)] as matrices on P (VV Eqs. (6) and (10)).
    """
    P = list(P)
    Q = [i for i in range(len(E)) if i not in set(P)]
    Vpp, Vpq, Vqp, Vqq = V[np.ix_(P, P)], V[np.ix_(P, Q)], V[np.ix_(Q, P)], V[np.ix_(Q, Q)]
    Di = 1.0 / (E[P][:, None] - E[Q][None, :])          # Di[a, al] = 1/(E_a - E_al)
    H0 = np.diag(E[P]).astype(complex)
    H2 = 0.5 * (np.einsum("ai,ib,ai->ab", Vpq, Vqp, Di) + np.einsum("ai,ib,bi->ab", Vpq, Vqp, Di))
    T1 = np.einsum("ai,ij,jb,ai,aj->ab", Vpq, Vqq, Vqp, Di, Di)
    T2 = np.einsum("ai,ij,jb,bi,bj->ab", Vpq, Vqq, Vqp, Di, Di)
    U1 = np.einsum("ac,ci,ib,ai,ci->ab", Vpp, Vpq, Vqp, Di, Di)
    U2 = np.einsum("ai,ic,cb,bi,ci->ab", Vpq, Vqp, Vpp, Di, Di)
    H3 = 0.5 * (T1 + T2) - 0.5 * (U1 + U2)
    return [H0, Vpp, H2, H3]


def resolvent(E, Q, x):
    """R(x) = Q/(x - H0) on the full space, with H0 = diag(E)."""
    d = np.zeros(len(E), complex)
    d[Q] = 1.0 / (x - E[Q])
    return np.diag(d)


def heff_operator(E, V, P):
    """VV Eqs. (5) and (8): operator forms with one resolvent R(E_a) per model state."""
    N = len(E)
    P = list(P)
    Q = [i for i in range(N) if i not in set(P)]
    Pr = {a: np.diag(np.eye(N)[a]) for a in P}
    R = {a: resolvent(E, Q, E[a]) for a in P}
    H2 = sum(0.5 * Pr[a] @ V @ (R[a] + R[b]) @ V @ Pr[b] for a in P for b in P)
    H3 = np.zeros((N, N), complex)
    for a in P:
        for b in P:
            first = V @ (R[a] @ V @ R[a] + R[b] @ V @ R[b]) @ V
            second = sum(V @ Pr[c] @ V @ R[c] @ R[a] @ V + V @ R[b] @ R[c] @ V @ Pr[c] @ V for c in P)
            H3 += 0.5 * Pr[a] @ (first - second) @ Pr[b]
    idx = np.ix_(P, P)
    return H2[idx], H3[idx]


def eig_sorted(M):
    return np.sort(np.linalg.eigvalsh(M))


def check_static():
    print("1. Static random matrix, non-degenerate model space")
    E = np.array([0.0, 0.03, 0.07, 1.0, 1.3, 2.0, 2.5, 3.1, 4.0])
    P = [0, 1, 2]
    V = random_hermitian(len(E))
    print("   lambda    err(2nd)   err(3rd)")
    prev = None
    for lam in (0.02, 0.01, 0.005, 0.0025):
        exact = eig_sorted(np.diag(E) + lam * V)[:3]
        H = heff_orders(E, lam * V, P)
        e2 = np.abs(eig_sorted(H[0] + H[1] + H[2]) - exact).max()
        e3 = np.abs(eig_sorted(H[0] + H[1] + H[2] + H[3]) - exact).max()
        line = f"   {lam:6.3f}   {e2:9.2e}  {e3:9.2e}"
        if prev:
            line += f"   ratios {prev[0] / e2:5.1f} (expect 8)  {prev[1] / e3:5.1f} (expect 16)"
        print(line)
        prev = (e2, e3)


def check_operator_forms():
    print("2. Operator forms against matrix elements")
    E = np.array([0.0, 0.03, 0.07, 1.0, 1.3, 2.0, 2.5, 3.1, 4.0])
    P = [0, 1, 2]
    N = len(E)
    Q = [i for i in range(N) if i not in P]
    V = random_hermitian(N, scale=0.1)
    H = heff_orders(E, V, P)
    H2, H3 = heff_operator(E, V, P)
    print(f"   non-degenerate P: Eq. (5) vs Eq. (6) {np.abs(H2 - H[2]).max():.1e},"
          f"  Eq. (8) vs Eq. (10) {np.abs(H3 - H[3]).max():.1e}")
    # degenerate model space, E_a = E0 = 0: Eqs. (7) and (9)
    Ed = E.copy()
    Ed[P] = 0.0
    Hd = heff_orders(Ed, V, P)
    Pm = np.zeros((N, N))
    Pm[P, P] = 1.0
    R = resolvent(Ed, Q, 0.0)
    PVP = Pm @ V @ Pm
    Nq = Pm @ V @ R @ R @ V @ Pm                     # PVR^2VP, the weight outside P
    H2d = (Pm @ V @ R @ V @ Pm)[np.ix_(P, P)]
    H3d = (Pm @ V @ R @ V @ R @ V @ Pm - 0.5 * (PVP @ Nq + Nq @ PVP))[np.ix_(P, P)]
    print(f"   degenerate P:     Eq. (7) vs Eq. (6) {np.abs(H2d - Hd[2]).max():.1e},"
          f"  Eq. (9) vs Eq. (10) {np.abs(H3d - Hd[3]).max():.1e}")
    # a single state: Rayleigh-Schroedinger third order
    a = 0
    o = [i for i in range(N) if i != a]
    d = E[a] - E[o]
    rs3 = (np.einsum("i,ij,j,i,j->", V[a, o], V[np.ix_(o, o)], V[o, a], 1 / d, 1 / d)
           - V[a, a] * np.sum(np.abs(V[a, o]) ** 2 / d ** 2))
    Hs = heff_orders(E, V, [a])
    print(f"   single state:     Eq. (10) vs Rayleigh-Schroedinger third order {abs(Hs[3][0, 0] - rs3):.1e}")


if __name__ == "__main__":
    check_static()
    print()
    check_operator_forms()
