# Skill: Save-and-Show Visualization Pattern

## What

A reusable pattern for saving visualizations to disk AND displaying them inline in Jupyter notebooks. Supports Altair, matplotlib, and plotnine.

## When to Use

Every time a visualization is produced in a notebook in this repository. This is a team directive from Ryan.

## Pattern

### Core Idea

1. Create the chart object (Altair chart, matplotlib figure, or plotnine plot)
2. Call `save_and_show_*(chart, "descriptive_filename")` 
3. The helper saves to `../outputs/figures/{filename}.png` and renders inline

### Import

```python
from shared_utils.viz_utils import save_and_show_altair, save_and_show_mpl, save_and_show_plotnine
```

> Requires `pip install -e .` from the repo root (done automatically by the
> Conda environment setup — see `environment/SETUP.md`).

### Altair

```python
chart = alt.Chart(df).mark_bar().encode(x="category", y="value")
save_and_show_altair(chart, "revenue_by_segment")
```

### matplotlib

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["category"], df["value"])
save_and_show_mpl(fig, "revenue_by_segment")
```

### plotnine

```python
p = ggplot(df, aes("category", "value")) + geom_bar(stat="identity")
save_and_show_plotnine(p, "revenue_by_segment")
```

## File Naming

- Lowercase, underscores: `cu_bridge_last_12_weeks.png`
- Default format: PNG at 150 DPI
- SVG for vector/presentation quality

## Key Files

- Helper implementations: `shared/viz_utils.py`
- PRD reference: `projects/standard_project_template/PRD.md` § 6
- Viz guidelines: `.github/instructions/visualizations.md`

## Post-Render QA

After saving, review the rendered image using the chart-vision-qa skill (`.squad/skills/chart-vision-qa/SKILL.md`) to catch truncated labels, clipped text, and other visual defects.
