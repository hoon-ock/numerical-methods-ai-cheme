"""One matplotlib style for the whole book.

Every notebook starts with::

    from cheme_numerics import use_course_style
    use_course_style()

so figures are visually consistent from chapter 1 to the last appendix. Do not
set rcParams or hard-code hex colors inside a chapter; change them here instead.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt

#: Categorical color cycle. Colorblind-safe (Okabe-Ito), ordered so the first
#: three are distinguishable in grayscale for printed handouts.
COLORS: list[str] = [
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#009E73",  # green
    "#CC79A7",  # purple
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#F0E442",  # yellow
    "#000000",  # black
]


def use_course_style(dpi: int = 110, figsize: tuple[float, float] = (6.0, 4.0)) -> None:
    """Apply the course-wide matplotlib style.

    Parameters
    ----------
    dpi
        Display resolution. The default suits the web book; raise to ~200 when
        exporting figures for print or slides.
    figsize
        Default figure size in inches. Chosen to sit comfortably in the book's
        content column without horizontal scrolling.
    """
    mpl.rcParams.update(
        {
            "figure.figsize": figsize,
            "figure.dpi": dpi,
            "savefig.dpi": dpi,
            "savefig.bbox": "tight",
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "axes.titleweight": "semibold",
            "axes.grid": True,
            "axes.axisbelow": True,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.prop_cycle": mpl.cycler(color=COLORS),
            "grid.alpha": 0.3,
            "grid.linewidth": 0.6,
            "legend.frameon": False,
            "lines.linewidth": 2.0,
            "lines.markersize": 5,
            "xtick.direction": "out",
            "ytick.direction": "out",
        }
    )


def annotate_convergence(ax: plt.Axes, order: int, x: float, y: float) -> None:
    """Draw a reference slope triangle of a given order on a log-log error plot.

    Used in the error-analysis chapters to show observed vs. theoretical order of
    convergence without eyeballing the slope.
    """
    dx = 0.6
    ax.plot([x, x * 10**dx], [y, y], color="0.4", lw=1)
    ax.plot([x * 10**dx, x * 10**dx], [y, y * 10 ** (-order * dx)], color="0.4", lw=1)
    ax.text(
        x * 10 ** (dx / 2),
        y * 1.15,
        "1",
        ha="center",
        va="bottom",
        fontsize=9,
        color="0.4",
    )
    ax.text(
        x * 10 ** (dx * 1.05),
        y * 10 ** (-order * dx / 2),
        f"{order}",
        ha="left",
        va="center",
        fontsize=9,
        color="0.4",
    )
