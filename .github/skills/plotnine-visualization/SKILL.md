# Skill: Plotnine Visualization

---
name: plotnine-visualization
description: Create standardized data visualizations using plotnine with RTI Growth themes and color palettes
domain: visualization
confidence: high
source: devdiv-growth-analytics — rti_growth_theme.py and rti_growth_colors.py used in 40+ projects
---

## Context

All analysis deliverables in this team use a consistent visual identity built on
**plotnine** (Python's grammar of graphics, equivalent to R's ggplot2). This
skill covers the standard themes, color palettes, and chart formatting patterns.

## Prerequisites

```
pip install plotnine>=0.14.5 matplotlib seaborn great-tables pypalettes
```

## 1. RTI Growth color palettes

Standard palettes for consistent branding:

```python
# Primary palettes
Bay_12 = ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087",
          "#f95d6a", "#ff7c43", "#ffa600", "#c9b700", "#88c540",
          "#2db757", "#00a08a"]
Bay_6 = ["#003f5c", "#665191", "#d45087", "#ff7c43", "#c9b700", "#2db757"]

Starfish_6 = ["#0d7680", "#2a8f93", "#54a8a7", "#8abfbd", "#c4d7d5", "#6b3a7a"]

Sunset_12 = ["#003f5c", "#2a4e7a", "#485d8e", "#636ca0", "#7e7caf",
             "#9a8dbe", "#b7a0cb", "#d5b4d7", "#f1c9e2", "#ffa7b7",
             "#ff7c43", "#ffa600"]

# Microsoft brand colors
msft_8 = ["#0078D4", "#50E6FF", "#00BCF2", "#D83B01",
          "#FFB900", "#107C10", "#B4009E", "#5C2D91"]
msft_grayscale = ["#000000", "#404040", "#808080", "#B0B0B0",
                  "#D0D0D0", "#E8E8E8", "#F5F5F5"]
```

### Choosing a palette

| Palette | Best for |
|---------|----------|
| `Bay_6` / `Bay_12` | Default — most charts, sequential data |
| `Starfish_6` | Teal-purple contrast, categorical data |
| `Sunset_12` | Large number of categories |
| `msft_8` | Microsoft-branded presentations |
| `msft_grayscale` | Accessible, print-friendly charts |

## 2. RTI Growth Plotnine Theme

```python
from plotnine import theme, element_text, element_line, element_rect, element_blank

def rti_growth_plotnine_theme():
    """Light theme for reports and deliverables."""
    return theme(
        # Text
        plot_title=element_text(size=14, weight="bold", family="Aptos"),
        axis_title=element_text(size=12, family="Aptos"),
        axis_text=element_text(size=11, family="Aptos"),
        legend_title=element_text(size=11, family="Aptos"),
        legend_text=element_text(size=10, family="Aptos"),
        # Grid
        panel_grid_major=element_line(color="#dadada", size=0.25),
        panel_grid_minor=element_blank(),
        # Background
        panel_background=element_rect(fill="white"),
        plot_background=element_rect(fill="white"),
        # Border
        panel_border=element_rect(color="#dadada", size=0.5),
    )

def rti_growth_plotnine_theme_dark():
    """Dark theme for presentations."""
    return theme(
        plot_title=element_text(size=14, weight="bold", color="white", family="Aptos"),
        axis_title=element_text(size=12, color="white", family="Aptos"),
        axis_text=element_text(size=11, color="#cccccc", family="Aptos"),
        legend_title=element_text(size=11, color="white", family="Aptos"),
        legend_text=element_text(size=10, color="#cccccc", family="Aptos"),
        panel_grid_major=element_line(color="#404040", size=0.25),
        panel_grid_minor=element_blank(),
        panel_background=element_rect(fill="#1e1e1e"),
        plot_background=element_rect(fill="#1e1e1e"),
        panel_border=element_rect(color="#404040", size=0.5),
        legend_background=element_rect(fill="#1e1e1e"),
    )
```

## 3. Common Chart Patterns

### Time series line chart

```python
from plotnine import ggplot, aes, geom_line, labs, scale_x_date

chart = (
    ggplot(df, aes(x="Date", y="Users"))
    + geom_line(color=Bay_6[0], size=1)
    + labs(title="Daily Active Users", x="Date", y="Users")
    + scale_x_date(date_labels="%b %Y")
    + rti_growth_plotnine_theme()
)
```

### Multi-series line chart

```python
chart = (
    ggplot(df, aes(x="Date", y="Users", color="Product"))
    + geom_line(size=1)
    + scale_color_manual(values=Bay_6)
    + labs(title="Users by Product", x="Date", y="Users")
    + rti_growth_plotnine_theme()
)
```

### Bar chart

```python
from plotnine import geom_col, coord_flip

chart = (
    ggplot(df, aes(x="reorder(Category, Value)", y="Value"))
    + geom_col(fill=Bay_6[0])
    + coord_flip()
    + labs(title="Values by Category", x="", y="Value")
    + rti_growth_plotnine_theme()
)
```

## 4. Saving Charts

Use the `save-and-show-viz` skill for saving and displaying charts. It handles saving to `outputs/figures/` and rendering inline in notebooks via the `save_and_show_plotnine()` helper.

See `skills/save-and-show-viz/SKILL.md` for the full pattern, argument order, and file naming conventions.

## Workflow

When an agent creates visualizations:

1. **Import RTI Growth palette and theme** at the top of the notebook
2. **Use plotnine (ggplot)** — not matplotlib directly
3. **Apply `rti_growth_plotnine_theme()`** to every chart
4. **Pick colors from standard palettes** — `Bay_6` as default
5. **Save charts** using the `save-and-show-viz` skill pattern
6. **Include clear labels** — title, axis labels, units

## Pitfalls

- **Don't use `print()` or `.draw(show=True)` to render in VS Code notebooks.** `print(p)` outputs a text repr (no image). `.draw(show=True)` renders twice (double display). Instead, make the plot object the **last expression** in the cell — e.g., assign to `p` and put `p` on the final line. IPython's display system handles rendering.
- **Save BEFORE the bare expression.** `.save()` must be its own line *before* the final `p` line. If `.save()` is after `p`, it never executes — IPython returns after evaluating the expression. Pattern: `p.save(...); p` (on separate lines).
- **Use `verbose=True` during development** — `verbose=False` silently swallows save failures. Switch to `False` only after confirming saves work.
- **`coord_flip()` causes trailing tick dashes** — category-axis tick marks render as visible dashes next to labels. Fix: add `axis_ticks_major_y=element_blank()` to the theme.
- **`coord_flip()` swaps grid line axes** — after flip, `panel_grid_major_y` controls the original x-axis (categories). Blank it for horizontal bar charts.
- **Use `pd.Categorical` for label ordering** — plotnine auto-sorts string labels alphabetically. Use `pd.Categorical(..., categories=[...], ordered=True)` to enforce display order.
- **Don't use matplotlib defaults** — always apply the RTI Growth theme
- **Don't hardcode hex colors** — use palette variables for consistency
- **Use `plotnine` not `seaborn`** for primary charts — seaborn is fine for quick EDA
- **Set `dpi=150+`** when saving — low-res charts look bad in reports
- **Use `.svg` for presentations** — vector scales without pixelation
