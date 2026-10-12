# Conventions for Claude sessions in this repo

- **Changelog:** every change that affects users or the repo gets a line under `## [Unreleased]` in `CHANGELOG.md`, in the same commit. Use the Keep a Changelog headings: Added, Changed, Fixed, Removed, Deprecated, Security.
- **Version:** never edit `VERSION`, tags or releases by hand. Use `scripts/release.py patch|minor|major` and choose the level from the definitions at the top of `CHANGELOG.md`. Release only when the user asks, and run `--dry-run` first.
- **Docs:** keep `README.md` accurate when behaviour changes.
- **Secrets:** they come from environment variables or the keychain, never from files in this repo.
- **Plans:** work beyond what Jordan has approved is written into a plan first and waits for his go. Plans live in
  `plans/` as a [plangraph](https://github.com/jordanromines-jpg/plugin-plangraph) graph (enabled for this repo in
  `.claude/settings.json`): use `/plangraph:plan` to write one, and change plans only with `plangraph` or its MCP
  tools, never by editing `plans/graph/` or a generated block. Approvals and answers are Jordan's own words
  (`plangraph approve|answer --quote`). Run `plangraph check` before committing plan changes, and add a line to
  `plans/CHANGELOG.md` in the same commit.

## How we work with Jordan

From how the web-agent sessions work (`plans/reference/how-we-work.md` there, Jordan, 11 Oct 2026: "I want to be able
to replicate this in the future for a new session").

- **One voice.** One session talks to Jordan. What other sessions or agents find reaches him rewritten, only what
  matters.
- **Keyed tables with a recommendation.** Every status, ask or option list is a table he can answer by key, each row
  with "My rec" (`plangraph asks` prints what waits on him). He answers "yes", "all rec" or by key; his exact words
  are recorded against each key (`plangraph answer D-4,G-2 --quote "<his words>"`, `--rec` for "all rec").
- **Status is a table of pull requests with their keys under them.** Short when asked: what's done, what's left, what
  waits on him, risks. Times in the local clock.
- **Gates are his.** Never answer or default a gate for him; record only his words and evidenced states.
- **New work waits for his go.** Work beyond what he approved is written into the plan first, and found work is
  proposed (`plangraph add … --propose`); adding detail to an idea isn't agreement.
- **Files first.** Before building, say which files a step touches: one editor per file at a time.
- **Mistakes, said plainly.** What went wrong, what it touched, the fix, the rule learned.
- **No agents unless he asks.** Parallel work is sessions he starts, not subagents.
