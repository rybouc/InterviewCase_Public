# Squad Team

> Product analytics interview case using fictitious Azure App Service customer acquisition and retention data.

## Coordinator

| Name | Role | Notes |
|------|------|-------|
| Squad | Coordinator | Routes work, enforces handoffs and reviewer gates. |

## Members

| Name | Role | Charter | Status |
|------|------|---------|--------|
| Viz-dude | Visualization Specialist | `.squad/agents/viz-dude/charter.md` | ✅ Active |
| Quarto-dude | Quarto Reporting Specialist | `.squad/agents/quarto-dude/charter.md` | ✅ Active |
| Experiment-dude | Experimentation & Statistics Specialist | `.squad/agents/experiment-dude/charter.md` | ✅ Active |
| Model-dude | Modeling Specialist | `.squad/agents/model-dude/charter.md` | ✅ Active |
| Git-Dude | Git & Repository Specialist | `.squad/agents/git-dude/charter.md` | ✅ Active |
| Query-dude | Query Specialist | `.squad/agents/query-dude/charter.md` | ✅ Active |
| Manager-dude | Project Management Specialist | `.squad/agents/manager-dude/charter.md` | ✅ Active |
| Scribe | Session Logger, Memory Manager & Decision Merger | `.squad/agents/scribe/charter.md` | 📋 Background |
| Ralph | Work Monitor | `.squad/agents/ralph/charter.md` | 🔄 Monitor |
| Rai | RAI Reviewer | `.squad/agents/rai/charter.md` | 🛡️ Background |
| Fact Checker | Verification & Devil's Advocate | `.squad/agents/fact-checker/charter.md` | 🔍 Background |

## Coding Agent

<!-- copilot-auto-assign: false -->

| Name | Role | Charter | Status |
|------|------|---------|--------|
| @copilot | Coding Agent | — | 🤖 Coding Agent |

### Capabilities

**🟢 Good fit — auto-route when enabled:**
- Bug fixes with clear reproduction steps
- Test coverage (adding missing tests, fixing flaky tests)
- Lint/format fixes and code style cleanup
- Dependency updates and version bumps
- Small isolated features with clear specs
- Boilerplate/scaffolding generation
- Documentation fixes and README updates

**🟡 Needs review — route to @copilot but flag for squad member PR review:**
- Medium features with clear specs and acceptance criteria
- Refactoring with existing test coverage
- API endpoint additions following established patterns
- Migration scripts with well-defined schemas

**🔴 Not suitable — route to squad member instead:**
- Architecture decisions and system design
- Multi-system integration requiring coordination
- Ambiguous requirements needing clarification
- Security-critical changes (auth, encryption, access control)
- Performance-critical paths requiring benchmarking
- Changes requiring cross-team discussion

## Project Context

- **Requester:** Ryan Bouchard
- **Project:** InterviewCase_Public
- **Stack:** Fictitious CSV-style product data, notebooks/analytics, visualizations, Quarto reports, and presentation deliverables
- **Description:** Analyze Azure App Service customer acquisition and retention to produce decision-ready findings and growth opportunities.
- **Created:** 2026-09-24T07:59:35.999-07:00
