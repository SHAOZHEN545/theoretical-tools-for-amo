#!/usr/bin/env python3
"""Numerical checks of the claims in
"Van Vleck perturbation theory - dressed states and rotated operators" and
"Van Vleck perturbation theory - errors" (VVB),
the companions of "Van Vleck perturbation theory and the effective Hamiltonian" (VV).

Run from the repository root:
    python checks/check_van_vleck_states_errors.py

1. Dressed states. |a~> = e^{-A}|a> keeps the weight 1 - w_a in P, with
   w_a = <a|V R(E_a)^2 V|a>, up to corrections of third order.
2. Projections versus model states. The van Vleck effective Hamiltonian through third order
   approaches, as lambda^4, the operator sum_k E_k |phi_k><phi_k| built from the exact
   eigenvalues and the symmetrically orthonormalized projections P|psi_k>. The operator built
   from the bare projections (Bloch's) differs already at second order.
3. The average versus other choices. Second-order operators built with the average and with
   the exact energy (Loewdin, solved self-consistently) both have eigenvalue errors of order
   lambda^3; adding VV Eq. (8) to the average gives lambda^4. Taking E_a for every element
   <a|.|b> instead of the average moves the real parts of the eigenvalues only at lambda^4,
   but the operator is not Hermitian, and its eigenvalues acquire imaginary parts at lambda^3.
4. What stopping leaves behind. Rotating exactly with A_1 (or A_1 + A_2) and diagonalizing the
   whole P block of the rotated Hamiltonian leaves an error of order lambda^4 (lambda^6): the
   discarded off-diagonal coupling acts at order 2n + 2, later than the truncation of H_eff.
5. A rotated operator. For a parity-odd coupling V = -F d, the bare <g|d|g> vanishes, while
   <g|P[A_1, d]P|g> reproduces the exact induced dipole up to relative corrections of order F^2.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_van_vleck import heff_orders  # noqa: E402

rng = np.random.default_rng(11)

# A model space of three non-degenerate states, well separated from five external ones.
E = np.array([0.0, 0.3, 0.7, 2.0, 2.6, 3.1, 3.9, 4.5])
P = [0, 1, 2]
Q = [i for i in range(len(E)) if i not in P]
LAMBDAS = (0.04, 0.02, 0.01, 0.005)


def random_hermitian(n, scale=1.0):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return scale * (a + a.conj().T) / 2


def block_diagonal(X, P):
    """X_D = PXP + QXQ."""
    inP = np.zeros(len(X), bool)
    inP[list(P)] = True
    return np.where(inP[:, None] == inP[None, :], X, 0)


def generator(E, X, P):
    """Off-diagonal solution of [A, H0] = -X_OD with H0 = diag(E): A_ij = X_ij / (E_i - E_j)."""
    inP = np.zeros(len(E), bool)
    inP[list(P)] = True
    od = inP[:, None] ^ inP[None, :]
    A = np.zeros(X.shape, complex)
    A[od] = X[od] / (E[:, None] - E[None, :])[od]
    return A


def generators(E, V, P):
    """A_1 from VV Eq. (1) and A_2 from VV Eq. (2), for the perturbation V as given."""
    A1 = generator(E, V, P)
    VD = block_diagonal(V, P)
    A2 = generator(E, A1 @ VD - VD @ A1, P)
    return A1, A2


def expm_antihermitian(A):
    """e^A for anti-Hermitian A, through the Hermitian matrix -iA."""
    k, W = np.linalg.eigh(-1j * A)
    return (W * np.exp(1j * k)) @ W.conj().T


def exact_model_states(H, P):
    """Eigenvalues and eigenvectors of the states that grow out of P, sorted by energy."""
    vals, vecs = np.linalg.eigh(H)
    idx = np.argsort((np.abs(vecs[P, :]) ** 2).sum(axis=0))[-len(P):]
    idx = idx[np.argsort(vals[idx])]
    return vals[idx], vecs[:, idx]


def ratio_line(lam, errs, prev, expect):
    line = f"   {lam:6.3f}  " + "  ".join(f"{e:9.2e}" for e in errs)
    if prev is not None:
        line += "   ratios " + "  ".join(f"{p / e:5.1f}" for p, e in zip(prev, errs))
        line += f"  (expect {expect})"
    return line


def check_dressed_states(V):
    print("1. Dressed states: weight left in P, compared with 1 - w_a")
    print("   lambda   max_a |(1 - w_a) - ||P e^{-A}|a>||^2|")
    prev = None
    for lam in LAMBDAS:
        A1, A2 = generators(E, lam * V, P)
        U = expm_antihermitian(-(A1 + A2))                     # e^{-A}
        err = 0.0
        for a in P:
            w = np.sum(np.abs(lam * V[Q, a]) ** 2 / (E[a] - E[Q]) ** 2)
            err = max(err, abs((1 - w) - np.sum(np.abs(U[P, a]) ** 2)))
        print(ratio_line(lam, [err], prev, "8"))
        prev = [err]


def check_projections(V):
    print("2. Van Vleck H_eff (through 3rd order) against operators built from exact eigenstates")
    print("   lambda   sym. orthonormalized   bare projections (Bloch)")
    prev = None
    for lam in LAMBDAS:
        Ek, vecs = exact_model_states(np.diag(E) + lam * V, P)
        p = vecs[P, :]                                         # columns: P|psi_k>
        g, Wg = np.linalg.eigh(p.conj().T @ p)
        phi = p @ (Wg / np.sqrt(g)) @ Wg.conj().T              # Loewdin orthonormalization
        H_sym = (phi * Ek) @ phi.conj().T
        H_bloch = (p * Ek) @ np.linalg.inv(p)
        H = heff_orders(E, lam * V, P)
        Hvv = H[0] + H[1] + H[2] + H[3]
        errs = [np.abs(Hvv - H_sym).max(), np.abs(Hvv - H_bloch).max()]
        print(ratio_line(lam, errs, prev, "16 and 4"))
        prev = errs


def check_choices(V):
    print("3. Second-order denominators: the average, the exact energy, and E_a alone")
    print("   lambda   errors: average   exact E   average+3rd   E_a vs average: Re diff   max Im")
    prev = None
    for lam in LAMBDAS:
        Vl = lam * V
        exact, _ = exact_model_states(np.diag(E) + Vl, P)
        H = heff_orders(E, Vl, P)
        H01 = H[0] + H[1]
        Vpq, Vqp = Vl[np.ix_(P, Q)], Vl[np.ix_(Q, P)]
        Di = 1.0 / (E[P][:, None] - E[Q][None, :])
        H_a = H01 + np.einsum("ai,ib,ai->ab", Vpq, Vqp, Di)    # R(E_a) for every element <a|.|b>
        loew = []
        for k, e in enumerate(np.linalg.eigvalsh(H01 + H[2])):
            for _ in range(100):                               # E = eig_k[PHP + PVR(E)VP]
                e = np.linalg.eigvalsh(H01 + Vpq @ np.diag(1.0 / (e - E[Q])) @ Vqp)[k]
            loew.append(e)
        avg = np.linalg.eigvalsh(H01 + H[2])
        ea = np.linalg.eigvals(H_a)
        ea = ea[np.argsort(ea.real)]
        errs = [np.abs(avg - exact).max(), np.abs(np.array(loew) - exact).max(),
                np.abs(np.linalg.eigvalsh(H01 + H[2] + H[3]) - exact).max(),
                np.abs(ea.real - avg).max(), np.abs(ea.imag).max()]
        print(ratio_line(lam, errs, prev, "8, 8, 16, 16, 8"))
        prev = errs


def check_residual(V):
    print("4. Whole P block after an exact rotation, against the truncated H_eff")
    print("   lambda   H_eff 2nd   P block, A1   H_eff 3rd   P block, A1+A2")
    prev = None
    for lam in LAMBDAS:
        H = np.diag(E) + lam * V
        exact, _ = exact_model_states(H, P)
        A1, A2 = generators(E, lam * V, P)
        Hv = heff_orders(E, lam * V, P)
        errs = []
        for gen, trunc in ((A1, Hv[0] + Hv[1] + Hv[2]), (A1 + A2, Hv[0] + Hv[1] + Hv[2] + Hv[3])):
            U = expm_antihermitian(gen)                        # e^{A}
            block = (U @ H @ U.conj().T)[np.ix_(P, P)]
            errs += [np.abs(np.linalg.eigvalsh(trunc) - exact).max(),
                     np.abs(np.linalg.eigvalsh(block) - exact).max()]
        print(ratio_line(lam, errs, prev, "8, 16, 16, 64"))
        prev = errs


def check_induced_dipole():
    print("5. Induced dipole of a state of definite parity: bare and rotated operator")
    Ed = np.array([0.0, 1.5, 2.0, 2.4, 3.3, 4.0, 1.8, 2.9])
    parity = np.array([1, -1, -1, -1, -1, -1, 1, 1])
    d = random_hermitian(len(Ed))
    d[parity[:, None] == parity[None, :]] = 0.0               # E1 changes parity
    print("   field     exact <d>     bare     rotated    relative error")
    prev = None
    for F in (0.02, 0.01, 0.005):
        Ek, vecs = exact_model_states(np.diag(Ed) - F * d, [0])
        psi = vecs[:, 0]
        exact = np.real(psi.conj() @ d @ psi)
        A1 = generator(Ed, -F * d, [0])
        rotated = np.real((A1 @ d - d @ A1)[0, 0])
        rel = abs(rotated - exact) / abs(exact)
        line = f"   {F:5.3f}   {exact: .6e}   {d[0, 0].real:.1f}   {rotated: .6e}   {rel:.2e}"
        if prev is not None:
            line += f"   ratio {prev / rel:4.1f} (expect 4)"
        print(line)
        prev = rel


if __name__ == "__main__":
    V = random_hermitian(len(E))
    check_dressed_states(V)
    print()
    check_projections(V)
    print()
    check_choices(V)
    print()
    check_residual(V)
    print()
    check_induced_dipole()
