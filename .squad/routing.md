# Work Routing

How to decide who handles what.

## Routing Table

| Work Type | Route To | Examples |
|-----------|----------|----------|
| Visualization and dashboard design | Viz-dude | Decision-oriented charts, accessible labels, uncertainty displays, publication-ready figures |
| Quarto reports and presentations | Quarto-dude | Quarto documents, PowerPoint deliverables, templates, branded styling, render validation |
| Experiments and statistical inference | Experiment-dude | Power/MDE, treatment-control comparisons, confidence intervals, multiple testing |
| Predictive and descriptive modeling | Model-dude | Supervised/unsupervised models, preprocessing, validation, leakage checks, interpretation |
| Git and repository operations | Git-Dude | Repository hygiene, branches, worktrees, `.gitignore`, commits/PR preparation when requested |
| Queries and semantic models | Query-dude | DAX, SQL, KQL, schema discovery, measure/filter validation |
| Planning, triage, and coordination | Manager-dude | Scope decomposition, dependencies, risks, status, handoffs, issue triage |
| Shared decisions and session memory | Scribe | Decision merging, histories, session and orchestration logs |
| Work queue monitoring | Ralph | Actionable issue monitoring, blockers, backlog continuity |
| Responsible AI review | Rai | Background safety, privacy, bias, accessibility, and content review |
| Verification and challenge | Fact Checker | Background claim verification, counter-hypotheses, pre-mortems |

## Issue Routing

| Label | Action | Who |
|-------|--------|-----|
| `squad` | Triage: analyze issue, assign `squad:{member}` label | Manager-dude |
| `squad:{name}` | Pick up issue and complete the work | Named member |

### How Issue Assignment Works

1. When a GitHub issue gets the `squad` label, **Manager-dude** triages it — analyzing content, assigning the right `squad:{member}` label, and commenting with triage notes.
2. When a `squad:{member}` label is applied, that member picks up the issue in their next session.
3. Members can reassign by removing their label and adding another member's label.
4. The `squad` label is the "inbox" — untriaged issues waiting for Manager-dude review.

## Rules

1. **Eager by default** — spawn all agents who could usefully start work, including anticipatory downstream work.
2. **Scribe always runs** after substantial work, always as `mode: "background"`. Never blocks.
3. **Quick facts → coordinator answers directly.** Don't spawn an agent for "what port does the server run on?"
4. **When two agents could handle it**, pick the one whose domain is the primary concern.
5. **"Team, ..." → fan-out.** Spawn all relevant agents in parallel as `mode: "background"`.
6. **Anticipate downstream work.** If a feature is being built, spawn the tester to write test cases from requirements simultaneously.
7. **Issue-labeled work** — when a `squad:{member}` label is applied to an issue, route to that member. Manager-dude handles all `squad` (base label) triage.
8. **Repository actions are opt-in** — Git-Dude never commits or pushes unless explicitly requested.
9. **Background reviewers stay background-only** — Rai and Fact Checker review without taking ownership of implementation.
