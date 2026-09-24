# Squad Decisions

## Active Decisions

### 2026-09-24T07:59:35.999-07:00: Initial team operating model
**By:** Ryan Bouchard, Manager-dude
**Status:** Accepted

**What:** Use Squad as a coordinator/dispatcher for the seven persistent specialists, with Scribe, Ralph, Rai, and Fact Checker as always-on built-ins. Route specialized work instead of doing it inline; use parallel agents when independent downstream work is useful. Keep local `main` as the canonical Squad state location with `stateBackend: local`. Maintain decisions in `.squad/decisions.md`, agent learnings in each `history.md`, and session/orchestration records through Scribe. Keep project work separate from shared skill/resource changes. Validate with the smallest relevant checks and report uncertainty. Never commit or push unless explicitly requested.

**Why:** The project combines product analytics, statistics, modeling, querying, visualization, reporting, repository hygiene, and delivery coordination. Explicit ownership and durable local state reduce ambiguity while preserving user control and reproducibility.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
