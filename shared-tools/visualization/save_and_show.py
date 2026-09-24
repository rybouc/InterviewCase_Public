"""Notebook-friendly helpers for saving and displaying visualizations."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import altair as alt
    from matplotlib.figure import Figure
    from plotnine.ggplot import ggplot

__all__ = [
    "save_and_show_mpl",
    "save_and_show_plotnine",
    "save_and_show_altair",
]

_DEFAULT_OUTPUT_DIR = Path("../outputs/figures")
_MPL_FORMATS = {"png", "svg"}
_PLOTNINE_FORMATS = {"png", "svg"}
_ALTAIR_FORMATS = {"png", "svg", "html"}


def _build_output_path(
    filename: str,
    output_dir: str | Path | None,
    fmt: str,
) -> Path:
    """Return the output path for a rendered visualization."""
    resolved_dir = Path(output_dir) if output_dir is not None else _DEFAULT_OUTPUT_DIR
    resolved_dir.mkdir(parents=True, exist_ok=True)

    suffix = fmt.lstrip(".")
    if not suffix:
        raise ValueError("fmt must be a non-empty file extension")

    file_path = Path(filename)
    target_name = file_path.with_suffix(f".{suffix}").name
    return resolved_dir / target_name


def _validate_format(fmt: str, supported_formats: set[str]) -> None:
    """Raise a ValueError when a format is unsupported."""
    if fmt not in supported_formats:
        formatted_choices = ", ".join(
            f"'{choice}'" for choice in sorted(supported_formats)
        )
        raise ValueError(
            f"Unsupported format '{fmt}'. Choose from {formatted_choices}."
        )


def _display_saved_image(image_path: Path, fmt: str) -> None:
    """Display a saved visualization inline when IPython is available."""
    try:
        from IPython.display import HTML, SVG, Image, display
    except ImportError:
        return

    if fmt == "png":
        display(Image(filename=str(image_path)))
    elif fmt == "svg":
        display(SVG(filename=str(image_path)))
    elif fmt == "html":
        display(HTML(filename=str(image_path)))
    else:
        raise ValueError(f"Unsupported display format '{fmt}'.")


def save_and_show_mpl(
    fig: "Figure",
    filename: str,
    output_dir: str | Path | None = None,
    dpi: int = 150,
    fmt: str = "png",
) -> Path:
    """Save a matplotlib figure, display it inline, and close it.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.
    filename : str
        Output filename, with or without an extension.
    output_dir : str | Path | None, optional
        Directory for saved figures. Defaults to ``Path("../outputs/figures")``.
    dpi : int, optional
        Raster DPI passed to ``Figure.savefig``.
    fmt : {"png", "svg"}, optional
        File format/extension to save.

    Returns
    -------
    pathlib.Path
        Path to the saved image file.
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ImportError(
            "matplotlib is required to save and close matplotlib figures."
        ) from exc

    _validate_format(fmt, _MPL_FORMATS)
    output_path = _build_output_path(filename=filename, output_dir=output_dir, fmt=fmt)
    fig.savefig(output_path, dpi=dpi, format=fmt, bbox_inches="tight")
    try:
        _display_saved_image(output_path, fmt)
    finally:
        plt.close(fig)
    return output_path


def save_and_show_plotnine(
    plot: "ggplot",
    filename: str,
    output_dir: str | Path | None = None,
    dpi: int = 150,
    width: float = 10,
    height: float = 6,
    fmt: str = "png",
) -> Path:
    """Save a plotnine plot and display the saved image inline.

    Parameters
    ----------
    plot : plotnine.ggplot
        Plotnine plot object to save.
    filename : str
        Output filename, with or without an extension.
    output_dir : str | Path | None, optional
        Directory for saved figures. Defaults to ``Path("../outputs/figures")``.
    dpi : int, optional
        Raster DPI passed to plotnine.
    width : float, optional
        Output width in inches.
    height : float, optional
        Output height in inches.
    fmt : {"png", "svg"}, optional
        File format/extension to save.

    Returns
    -------
    pathlib.Path
        Path to the saved image file.
    """
    _validate_format(fmt, _PLOTNINE_FORMATS)
    output_path = _build_output_path(filename=filename, output_dir=output_dir, fmt=fmt)
    plot.save(
        filename=str(output_path),
        format=fmt,
        dpi=dpi,
        width=width,
        height=height,
        units="in",
        verbose=False,
    )
    _display_saved_image(output_path, fmt)
    return output_path


def save_and_show_altair(
    chart: "alt.TopLevelMixin",
    filename: str,
    output_dir: str | Path | None = None,
    scale_factor: float = 2.0,
    fmt: str = "png",
) -> Path:
    """Save an Altair chart, display the saved image inline, and return its path.

    Parameters
    ----------
    chart : altair.TopLevelMixin
        Altair chart to save.
    filename : str
        Output filename, with or without an extension.
    output_dir : str | Path | None, optional
        Directory for saved figures. Defaults to ``Path("../outputs/figures")``.
    scale_factor : float, optional
        Export scale factor used for crisp PNG output. Ignored for SVG/HTML.
    fmt : {"png", "svg", "html"}, optional
        File format/extension to save.

    Returns
    -------
    pathlib.Path
        Path to the saved image file.
    """
    _validate_format(fmt, _ALTAIR_FORMATS)
    output_path = _build_output_path(filename=filename, output_dir=output_dir, fmt=fmt)
    if fmt == "png":
        chart.save(str(output_path), format=fmt, scale_factor=scale_factor)
    else:
        chart.save(str(output_path), format=fmt)
    _display_saved_image(output_path, fmt)
    return output_path
