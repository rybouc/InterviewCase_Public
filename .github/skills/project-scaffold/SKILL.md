# Skill: Project Scaffold

---
name: project-scaffold
description: Standard project structure, README template, and notebook setup for new data science projects
domain: project-management
confidence: high
source: devdiv-growth-analytics — best practices from 100+ projects (sections 2.1-2.3)
---

## Context

Every analysis project in this team follows a standard structure. This makes
projects navigable, reviewable, and maintainable. This skill defines the
template for new projects and the README-driven development approach.

## 1. Standard Project Structure

```
projects/{YYYYMMDD}_{alias}_{project-name}/
├── README.md                    # Business problem, approach, deliverables
├── notebooks/                   # Jupyter notebooks for analysis
│   ├── 01-data-exploration.ipynb
│   └── 02-analysis.ipynb
├── queries/                     # query files
├── data/                        # Local data cache 
├── outputs/                     # All generated artifacts
│   ├── figures/                 # Charts, plots, visualizations
│   ├── reports/                 # Reports, decks, summaries
│   ├── data/                    # Processed/derived datasets
│   └── cache/                   # Cached query results (see dcp-query-caching skill)
├── pyproject.toml               # Python dependencies
└── .gitignore                   # Only if you need exceptions to repo-level rules
```

### Project Naming Convention

Project folders follow the format `{YYYYMMDD}_{alias}_{project-name}`:

- **YYYYMMDD** — date the project was created (for chronological sorting)
- **alias** — the creator's alias (for ownership at a glance)
- **project-name** — short descriptive name in PascalCase or kebab-case

Example: `20260428_alortoll_OpsAgentRetention`

This makes it easy to see when a project was started, who owns it, and what it's about — all from the folder name.

**Shared helpers live in `shared-tools/` at the repo root — import them, don't copy them into projects.**

### Artifact Organization

Generated artifacts should be organized as follows:
- **Charts/plots** → `outputs/figures/`
- **Reports/decks/summaries** → `outputs/reports/`
- **Processed datasets** → `outputs/data/`
- **Cached query results** → `outputs/cache/` (see `dcp-query-caching` skill for the full pattern)

## 2. README Template

Every project **must** have a README.md created **before coding begins**:

```markdown
# {Project Name}

**Lead Data Scientist:** {name}

## Business Problem

{What question are we answering? Why does it matter?}

## Deliverables

{What outputs will be produced? (Report, dashboard, dataset, presentation)}

## Decisions Enabled

{How will the results be used? What decisions depend on this analysis?}

## People and Teams Involved

| Role | Person/Team |
|------|-------------|
| Analyst | {name} |
| Stakeholder | {name/team} |
| Data Owner | {team} |

## Data Sources

| Source | Table/Database | Description |
|--------|---------------|-------------|
| {Kusto cluster} | {database.table} | {what this data contains} |

## Analysis Approach

{Methodology — retention analysis, DiD, segmentation, etc.}

## Key Findings

{Filled in after analysis is complete}

## Status

- [ ] Problem defined
- [ ] Data sources identified
- [ ] Analysis complete
- [ ] Results reviewed
- [ ] Deliverable shared
```

## 3. Notebook Setup Pattern

The first cell of every notebook should set up the environment:

```python
# Cell 1: Configuration
USE_CACHE = True  # Set False to force re-query; see dcp-query-caching skill
START_DATE = "2024-01-01"
END_DATE = "2024-06-30"

# Cell 2: Imports and paths
import sys
from pathlib import Path
import polars as pl
from plotnine import *

# Repo root is 3 levels up from notebooks/
repo_root = Path.cwd().parent.parent.parent
sys.path.insert(0, str(repo_root))

# Cell 3: Data access

```

### Why 3 levels up?

```
repo_root/
└── projects/
    └── {project}/
        └── notebooks/    ← cwd is here
            └── analysis.ipynb
```

`Path.cwd().parent` = `notebooks/`, `.parent` = `{project}/`, `.parent` = `projects/`, `.parent` = `repo_root/`

That's 4 levels. But if cwd is the notebook's directory: 3 levels → `repo_root`.

The `shared_tools` package is installed at the repo root, so imports reference it directly.

## 4. pyproject.toml Template

```toml
[project]
name = "{project-name}"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "polars>=1.22.0",
    "plotnine>=0.14.5",
    "pins>=0.8.7",
    "pyarrow>=19.0.1",
    "loguru",
    "jinja2",
]
```

`pyproject.toml` is the standard Python dependency format (PEP 621). It works with any installer — `pip install .`, `uv pip install .`, or `pip install .` inside a conda environment. No `environment.yml` or `requirements.txt` needed.

## 5. .gitignore — Exceptions to Repo-Level Rules

**The repo-level `.gitignore` already handles global data file exclusions** (`*.csv`, `*.parquet`, `*.pkl`, `data/`, cache files, etc.). 

Most projects do **not** need a per-project `.gitignore`. However, create one **only if your project needs an exception** to the repo-level rules — for example, to commit a small reference file:

```gitignore
# Example: Allow a specific reference CSV while excluding others
!data/reference_mapping.csv
```

### How .gitignore Hierarchy Works

- **Repo-level `.gitignore`** blocks patterns globally (e.g., `*.csv` blocks all CSVs)
- **Project-level `.gitignore`** can override repo-level rules using `!` patterns
- Rules combine: later rules can whitelist exceptions to earlier blocks
- A file matching both a block and an exception is **allowed** (exception wins)

**If you have no exceptions to the repo-level rules, don't add a per-project `.gitignore`.**

## Workflow

When an agent starts a new project:

1. **Create the project directory** under `projects/{YYYYMMDD}_{alias}_{project-name}/` using today's date and the user's alias
2. **Write the README first** — fill in Business Problem, Deliverables, Decisions Enabled. If project details are not provided upfront, request this information from the user before proceeding — the README must contain a full description of the project, its deliverables, and components.
3. **Create subdirectories**: `notebooks/`, `queries/`, `data/`, `outputs/figures/`, `outputs/reports/`, `outputs/data/`, `outputs/cache/`
4. **Add `pyproject.toml`** with standard dependencies
5. **Add per-project `.gitignore` only if needed** — the repo-level `.gitignore` already excludes data files, caches, and OS junk. Only add a `.gitignore` if you need to create an exception (e.g., `!data/small_reference.csv` to allow a specific file)
6. **Set up the first notebook** with the standard configuration cell pattern
7. **Reference existing skills** — `plotnine-visualization` for charts

## Pitfalls

- **Don't skip the README** — write it before coding, update it after analysis
- **Don't commit data files** — the repo-level `.gitignore` automatically excludes `*.csv`, `*.parquet`, `*.pkl`, `data/`, and other cache patterns. No per-project `.gitignore` needed for this.
- **Don't hardcode paths** — use `Path.cwd().parent` chains or `repo_root` variable
- **Number notebooks** (`01-`, `02-`) to indicate execution order
- **Don't duplicate shared helpers** — import from `shared-tools/` at the repo root, don't copy them into your project
