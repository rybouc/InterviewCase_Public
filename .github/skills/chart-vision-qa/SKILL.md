# Skill: Chart Vision QA

| Field | Value |
|-------|-------|
| **Name** | chart-vision-qa |
| **Description** | Vision-based review of saved chart images to catch visual defects before delivery |
| **Domain** | Visualization Quality Assurance |
| **Confidence** | Low |
| **Source** | Team practice — codified from manual review patterns |

---

## Context

Charts from this repository are presented to **leadership and executive stakeholders**. A truncated axis label or clipped title doesn't just look sloppy — it erodes trust in the underlying analysis. Code review catches logic errors but cannot catch visual defects: overlapping text, squished aspect ratios, unreadable font sizes, or legends covering data points. Those defects only appear in the rendered image.

This skill defines a systematic, vision-based QA pass that any chart-producing agent can run after rendering. It turns "looks fine to me" into a repeatable checklist.

---

## When to Use

- **After any `save_and_show_*` call** produces a chart to `outputs/figures/`.
- **Before including any chart** in a Quarto report (`.qmd`) or slide deck.
- **During chart review** when another agent asks the visualization specialist to review their charts.

---

## How It Works

1. **View the saved PNG** — Use the `view` tool on the rendered image file (e.g., `outputs/figures/revenue_by_segment.png`).
2. **Run through the checklist** below, category by category. Note any defects.
3. **If defects found** → fix the chart code, re-render, and re-check.
4. **If clean** → move on. No annotation needed for passing charts.

---

## Review Checklist

### Category 1: Rendering & Layout
*Is anything broken?*

- [ ] **Truncated labels** — Axis labels, tick labels, or legend text cut off at figure edge
- [ ] **Clipped titles/subtitles** — Title or subtitle text runs past the figure boundary
- [ ] **Overlapping text** — Annotations, axis labels, or data labels stacked on top of each other
- [ ] **Legend overflow** — Legend extends beyond the plot area or covers data points
- [ ] **Aspect ratio distortion** — Chart appears squished or stretched unnaturally
- [ ] **White space imbalance** — Excessive empty space or elements too cramped
- [ ] **Figure size mismatch** — Figure too small for the content it contains, or unnecessarily large

### Category 2: Readability
*Can a VP glance and understand?*

- [ ] **Font size adequacy** — Minimum ~10pt rendered for reports; 18–24pt for slide decks
- [ ] **Color contrast** — Low contrast between series or between data and background
- [ ] **Too many series/categories** — More than 5–7 distinct visual elements competing for attention
- [ ] **Overplotting** — Dense scatter plots where points obscure the underlying pattern
- [ ] **Grid/background noise** — Heavy gridlines or dark backgrounds that distract from data
- [ ] **Legend vs. direct labeling** — Could direct labels replace the legend? (Direct labels are faster to parse — Tufte)

### Category 3: Communication & Accuracy
*Does the chart tell the truth?*

- [ ] **Insight-driven title** — Title states the takeaway, not just the metric name
- [ ] **Non-zero baseline** — Bar chart y-axis not starting at 0 (misleading magnitude)
- [ ] **Inconsistent scales** — Side-by-side charts using different axis ranges without callout
- [ ] **Missing units** — Numbers shown without CU, %, USD, count, or other unit labels
- [ ] **Unformatted large numbers** — Raw values like 1200000 instead of "1.2M"
- [ ] **Color accessibility** — Red-green encoding without shape or pattern backup for colorblind viewers
- [ ] **Temporal axis clarity** — Ambiguous date labels (e.g., "03" — March? Third day? Third week?)

### Category 4: Presentation Context
*Will this survive a slide deck?*

- [ ] **Slide-ready dimensions** — 16:9 aspect ratio; `fig-width: 10`, `fig-height: 5–5.5` per quarto-pptx skill
- [ ] **PNG resolution** — ≥150 DPI for projection on large screens
- [ ] **Standalone interpretability** — Chart makes sense without verbal narration or surrounding text
- [ ] **Consistent visual identity** — Colors, fonts, and styling match other charts in the project

---

## Common Fixes

| Defect | Typical Fix |
|--------|-------------|
| Truncated x-axis labels | Rotate labels 45°, increase `fig_width`, or abbreviate text |
| Clipped title | `plt.tight_layout()` or increase top margin (`plt.subplots_adjust(top=0.88)`) |
| Overlapping annotations | Use `adjustText` library, reduce annotation count, or increase figure size |
| Legend covering data | `bbox_to_anchor` outside plot area, or switch to direct labels |
| Text too small | Increase `base_size` in plotnine, `font_scale` in seaborn, or `fontsize` in matplotlib |
| Non-zero baseline | `scale_y_continuous(limits=(0, None))` in plotnine; `ax.set_ylim(bottom=0)` in matplotlib |
| Raw large numbers | `label_number(scale_cut=cut_short_scale())` in plotnine; custom `FuncFormatter` in matplotlib |
| Low contrast between series | Switch to `cubehelix` or `viridis`-family palette |

---

## Model Requirements

Vision-based chart review requires a model that can interpret images:

- **Supported:** Sonnet 4.5+, Sonnet 4, Opus
- **Not supported:** Haiku — skip vision QA if spawned on Haiku (it cannot process images)
- **Recommendation:** For critical executive-facing charts, Opus provides the highest visual acuity

If running on Haiku, note that vision QA was skipped and flag the chart for manual review.

---

## Cross-References

- `.github/instructions/visualizations.md` — Design standards and chart defaults
- `.squad/skills/save-and-show-viz/SKILL.md` — Save-and-show pattern (render step before QA)
- `.squad/skills/quarto-pptx/SKILL.md` — Slide dimensions and PowerPoint rendering constraints
