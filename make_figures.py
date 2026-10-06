"""
Figures for EE 513 lecture 1: The imaging pipeline end to end.

Every figure in this deck is generated here so it can be regenerated when the
test image, a parameter, or a library version changes. Writes SVG into Figures/.

Run from this directory:  python make_figures.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
FIGURES = HERE / "Figures"
IMAGES = HERE.parents[1] / "Images"          # the term's standard captures

FIGURES.mkdir(exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.bbox": "tight",
    "font.family": "Helvetica Neue",
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "svg.fonttype": "none",                  # keep text as text in the SVG
})

PSU_GREEN = "#6d8d24"
PSU_FOREST = "#213921"
PSU_BLUE = "#008ac1"
ACCENT = "#cfd82d"


def save(fig, name):
    path = FIGURES / f"{name}.svg"
    fig.savefig(path)
    plt.close(fig)
    print(f"wrote {path.relative_to(HERE)}")


def pipeline_block_diagram():
    """The end-to-end pipeline, with the course's coverage marked."""
    stages = [
        ("Scene", "radiance"),
        ("Lens", "optics, PSF"),
        ("Sensor", "photons to DN"),
        ("ISP", "raw to RGB"),
        ("Encode", "JPEG, video"),
        ("Use", "display or model"),
    ]
    fig, ax = plt.subplots(figsize=(11, 2.6))
    ax.set_axis_off()
    ax.set_xlim(0, len(stages) * 2)
    ax.set_ylim(-1.05, 1.25)

    for i, (name, sub) in enumerate(stages):
        x = i * 2 + 0.1
        face = "#f4f7ec" if i in (1, 2, 3) else "#ffffff"
        edge = PSU_GREEN if i in (1, 2, 3) else "#999999"
        ax.add_patch(FancyBboxPatch(
            (x, -0.32), 1.55, 0.78,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            linewidth=2, edgecolor=edge, facecolor=face))
        ax.text(x + 0.78, 0.26, name, ha="center", va="center",
                fontsize=13, fontweight="bold", color=PSU_FOREST)
        ax.text(x + 0.78, -0.10, sub, ha="center", va="center",
                fontsize=9.5, color="#555555")
        if i < len(stages) - 1:
            ax.add_patch(FancyArrowPatch(
                (x + 1.62, 0.07), (x + 2.03, 0.07),
                arrowstyle="-|>", mutation_scale=14,
                linewidth=1.6, color="#777777"))

    ax.plot([2.1, 7.35], [-0.62, -0.62], color=PSU_GREEN, linewidth=2.5)
    ax.text(4.7, -0.86, "most of EE 513", ha="center", va="center",
            fontsize=11, color=PSU_GREEN, fontweight="bold")
    ax.text(11.0, -0.86, "EE 514 and EE 515", ha="center", va="center",
            fontsize=11, color="#888888")

    save(fig, "L01-Pipeline")


def what_is_lost():
    """One scene value, followed through the pipeline, losing information."""
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    x = np.linspace(0, 1, 1000)
    scene = 0.5 + 0.45 * np.sin(2 * np.pi * 9 * x ** 1.7)

    blurred = np.convolve(scene, np.ones(55) / 55, mode="same")
    rng = np.random.default_rng(0)
    n = 24
    idx = np.linspace(0, 999, n).astype(int)
    sampled = blurred[idx] + rng.normal(0, 0.035, n)
    quantized = np.round(sampled * 15) / 15

    ax.plot(x, scene, color="#bbbbbb", linewidth=1.4, label="Scene radiance")
    ax.plot(x, blurred, color=PSU_BLUE, linewidth=2, label="After the lens (PSF)")
    ax.plot(x[idx], quantized, "o", color=PSU_GREEN, markersize=6,
            label="After the sensor (sampled, noisy, quantized)")
    ax.set_xlabel("Position across the scene")
    ax.set_ylabel("Relative radiance")
    ax.set_ylim(-0.05, 1.15)
    ax.legend(loc="upper right", fontsize=9.5, framealpha=0.95)
    save(fig, "L01-WhatIsLost")


def job_families():
    """Where EE 513 graduates work, by role family."""
    families = [
        "Camera systems\nand ISP",
        "Image quality\nand test",
        "Inspection and\nmetrology",
        "Scientific and\nmedical imaging",
        "Computational\nphotography",
    ]
    employers = [
        "Apple, Qualcomm, Google,\nSamsung, Sony, MediaTek",
        "Apple, Meta, Planet,\nTeledyne",
        "Lam, KLA, Applied Materials,\nASML, Onto",
        "Thermo Fisher, Zeiss,\nOHSU, medical devices",
        "Apple, Google, Adobe",
    ]
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(families))
    for i, (fam, emp) in enumerate(zip(families, employers)):
        y = len(families) - i - 1
        ax.add_patch(FancyBboxPatch(
            (0.05, y + 0.12), 2.9, 0.76,
            boxstyle="round,pad=0.03,rounding_size=0.06",
            linewidth=2, edgecolor=PSU_GREEN, facecolor="#f4f7ec"))
        ax.text(1.5, y + 0.5, fam, ha="center", va="center",
                fontsize=10.5, fontweight="bold", color=PSU_FOREST)
        ax.text(3.25, y + 0.5, emp, ha="left", va="center",
                fontsize=10, color="#444444")
    save(fig, "L01-JobFamilies")


if __name__ == "__main__":
    pipeline_block_diagram()
    what_is_lost()
    job_families()
