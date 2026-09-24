# Visualization Instructions

These instructions apply whenever creating charts, tables, or visual summaries.
The primary goal of visualizations in this repository is **clear communication of insights**, often for leadership and executive audiences.

---

## Core Visualization Principles
- Favor **simplicity over completeness**.
- Remove visual clutter (excess gridlines, borders, legends, annotations).
- Charts should be interpretable without verbal explanation.
- Every chart should have a clear takeaway.

---

## Preferred Chart Types
- Prefer **horizontal bar charts** over vertical bar charts.
- Use line charts for trends over time.
- Avoid pie charts unless the number of categories is very small and comparison is trivial.
- Use tables only when precise values matter more than patterns.

---

## Preferred Libraries
Use the library best suited to the task, with a preference for **grammar-of-graphics** approaches:

### Python
- `plotnine`
- `altair`

### R
- `ggplot2`

If another library is clearly better for a specific chart (e.g., interaction, performance, layout), use it.

---

## Chart Design Defaults
- Use **muted or neutral color palettes** by default.
- Use color intentionally to highlight a key comparison or takeaway.
- Avoid unnecessary legends when direct labeling is possible.
- Titles should state the insight, not just the metric.

Good:
> "Revenue growth driven primarily by existing customers"

Less helpful:
> "Revenue by customer segment"

---

## Axes & Labels
- Axis labels should be concise and human-readable.
- Use consistent units and scales across related charts.
- Avoid unnecessary precision (e.g., too many decimal places).
- Start axes at zero for bar charts unless there is a compelling reason not to.
- For large numbers above 10000, us "10K" in the axis label instead of 10000.

---

## Formatting & Layout
- Prefer clean backgrounds.
- Minimize gridlines; keep only what aids interpretation.
- Avoid excessive annotation—use it only to emphasize key points.
- Charts should be presentation-ready without additional editing.

---

## Defaults to Assume
Unless otherwise specified:
- Horizontal bars > vertical bars
- Fewer colors > more colors
- Simpler chart > denser chart
- Interpretability > visual novelty
