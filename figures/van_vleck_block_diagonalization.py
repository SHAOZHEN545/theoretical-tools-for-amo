#!/usr/bin/env python3
"""Folding as a block diagonalization, for the note
"Van Vleck perturbation theory and the effective Hamiltonian".

Left: H = H0 + lambda V in blocks, with the couplings PVQ and QVP to the far states.
Right: the rotated Hamiltonian e^A H e^-A. A generator built through order n leaves an
off-diagonal coupling with n + 1 factors of V; the P block is H_eff.

Writes Notes/Van Vleck perturbation theory/Pictures/Van Vleck block diagonalization.svg.
The output is reproducible: text is stored as paths, with a fixed hash salt and no date.

Usage (any working directory):
    python figures/van_vleck_block_diagonalization.py
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Notes", "Van Vleck perturbation theory", "Pictures",
                   "Van Vleck block diagonalization.svg")

# Colors of the group-meeting slide this figure was redrawn from.
INK = "#1E2A38"          # frames, arrow, captions under the matrices
TEAL_DARK = "#1D6F66"    # P labels, "decoupled" label
TEAL = "#2A9D8F"         # H_eff block
TEAL_LIGHT = "#BFE3DE"   # PHP block
MAROON = "#8E2C48"       # couplings to the far states
PINK = "#F7CDD3"         # PVQ and QVP blocks
SLATE = "#5F6B78"        # Q labels and Q blocks
GRAY_LIGHT = "#DCE1E7"   # QHQ block
WHITE = "#FFFFFF"

# Geometry, in data units. Each matrix is a square of side SIDE; the P block is the
# smaller upper-left square of side PW, because P holds only a few states.
SIDE, PW = 30.0, 11.5
Y0 = 8.0                        # bottom edge of both matrices
LEFT_X0, RIGHT_X0 = 11.0, 62.0   # left edges of the two matrices


def block_matrix(ax, x0, fills, labels, colors, sizes):
    """Draw a 2x2 block matrix with its lower-left corner at (x0, Y0).

    fills, labels, colors and sizes are dicts keyed by "PP", "PQ", "QP", "QQ".
    """
    xs = {"P": (x0, PW), "Q": (x0 + PW, SIDE - PW)}            # column: left edge, width
    ys = {"P": (Y0 + SIDE - PW, PW), "Q": (Y0, SIDE - PW)}     # row: bottom edge, height
    for key in ("PP", "PQ", "QP", "QQ"):
        row, col = key[0], key[1]
        (x, w), (y, h) = xs[col], ys[row]
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fills[key], edgecolor=INK, lw=0.8))
        ax.text(x + w / 2, y + h / 2, labels[key], color=colors[key], fontsize=sizes[key],
                ha="center", va="center")
    ax.add_patch(Rectangle((x0, Y0), SIDE, SIDE, fill=False, edgecolor=INK, lw=1.8))
    # row labels, P above Q
    ax.text(x0 - 2.4, ys["P"][0] + PW / 2, r"$P$", color=TEAL_DARK, fontsize=17,
            ha="center", va="center")
    ax.text(x0 - 2.4, Y0 + (SIDE - PW) / 2, r"$Q$", color=SLATE, fontsize=17,
            ha="center", va="center")


def main():
    plt.rcParams.update({
        "svg.hashsalt": "van-vleck-block-diagonalization",
        "svg.fonttype": "path",
        "mathtext.fontset": "cm",
        "font.family": "DejaVu Sans",
    })
    fig = plt.figure(figsize=(9.0, 4.14))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 46.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 100, 46.0, facecolor=WHITE, edgecolor="none"))

    # --- the Hamiltonian before the rotation
    block_matrix(
        ax, LEFT_X0,
        fills={"PP": TEAL_LIGHT, "PQ": PINK, "QP": PINK, "QQ": GRAY_LIGHT},
        labels={"PP": r"$PHP$", "PQ": r"$PVQ$", "QP": r"$QVP$", "QQ": r"$QHQ$"},
        colors={"PP": TEAL_DARK, "PQ": MAROON, "QP": MAROON, "QQ": SLATE},
        sizes={"PP": 16, "PQ": 18, "QP": 18, "QQ": 18},
    )
    ax.text(LEFT_X0 + SIDE / 2, Y0 + SIDE + 2.6, "couplings to the far states",
            color=MAROON, fontsize=13, ha="center", va="bottom")
    ax.text(LEFT_X0 + SIDE / 2, Y0 - 2.6, r"$H=H_0+\lambda V$", color=INK, fontsize=19,
            ha="center", va="top")

    # --- the rotation
    xa, xb, ya = LEFT_X0 + SIDE + 4.0, RIGHT_X0 - 7.0, Y0 + SIDE / 2
    ax.add_patch(FancyArrowPatch((xa, ya), (xb, ya), arrowstyle="-|>", mutation_scale=18,
                                 color=INK, lw=1.6))
    ax.text((xa + xb) / 2, ya + 1.6, r"$e^{A}$", color=INK, fontsize=19,
            ha="center", va="bottom")

    # --- the Hamiltonian after the rotation
    block_matrix(
        ax, RIGHT_X0,
        fills={"PP": TEAL, "PQ": WHITE, "QP": WHITE, "QQ": GRAY_LIGHT},
        labels={"PP": r"$H_{\rm eff}$", "PQ": r"$O(V^{\,n+1})$", "QP": r"$O(V^{\,n+1})$",
                "QQ": r"$Q\tilde HQ$"},
        colors={"PP": WHITE, "PQ": INK, "QP": INK, "QQ": SLATE},
        sizes={"PP": 18, "PQ": 13, "QP": 13, "QQ": 18},
    )
    ax.text(RIGHT_X0 + SIDE / 2, Y0 + SIDE + 2.6, r"decoupled: keep the $P$ block",
            color=TEAL_DARK, fontsize=13, ha="center", va="bottom")
    ax.text(RIGHT_X0 + SIDE / 2, Y0 - 2.6, r"$\tilde H=e^{A}He^{-A}$", color=INK,
            fontsize=19, ha="center", va="top")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, format="svg", metadata={"Date": None})
    print("wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
