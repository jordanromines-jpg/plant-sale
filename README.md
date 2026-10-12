# template-repo

A GitHub template for new repos, with versioning and releases built in.

| File | Purpose |
|---|---|
| `VERSION` | Current version (SemVer). It starts at `0.0.0`, so the first `release.py minor` makes 0.1.0. |
| `CHANGELOG.md` | Keep a Changelog, with this repo's MAJOR/MINOR/PATCH definitions at the top. Every change gets an `[Unreleased]` entry. |
| `scripts/release.py` | `patch\|minor\|major\|X.Y.Z [--dry-run]`. Bumps VERSION, dates the Unreleased notes, commits, tags, pushes, and publishes a GitHub Release with those notes. Optional extras: `scripts/build-release.sh` and `.release-assets`. |
| `scripts/init.py` | One-time setup after "Use this template": fresh README, CHANGELOG and VERSION, then it deletes itself. |
| `CLAUDE.md` | Tells Claude sessions to follow these conventions. |
| `.gitignore` | Common OS, editor, Python, Node, env and log ignores. |

## Use

```bash
gh repo create tool-my-thing --private --template jordanromines-jpg/template-repo --clone
cd tool-my-thing
scripts/init.py "My Thing" "One-line description"
git add -A && git commit -m "Initialise from template-repo" && git push
```

Next:
1. Edit the MAJOR/MINOR/PATCH definitions at the top of `CHANGELOG.md`.
2. Work, adding an `[Unreleased]` entry with each change.
3. Run `scripts/release.py minor` for v0.1.0.

Plans come built in: `plans/` holds a [plangraph](https://github.com/jordanromines-jpg/plugin-plangraph) graph and its
README, and `.claude/settings.json` enables the plangraph plugin for every Claude Code session in the new repo (each
person is asked to trust the folder first). Start a plan with `/plangraph:plan`.

For Claude skills, use [template-skill](https://github.com/jordanromines-jpg/template-skill). It's this template plus a `SKILL.md` skeleton, trigger tests and `.skill` packaging.

## Naming

Every repo name starts with its type:

| Prefix | For | Example |
|---|---|---|
| `skill-` | A Claude skill (the skill's `name:` equals the repo name) | `skill-imgbb-upload` |
| `plugin-` | A Claude Code plugin (may bundle skills and MCP servers) | `plugin-chart-advisor` |
| `mcp-` | A standalone MCP server | `mcp-…` |
| `tool-` | A script or CLI | `tool-…` |
| `app-` | An application or site | `app-…` |
| `data-` | A dataset or knowledge base | `data-dataviz-library` |
| `template-` | A GitHub template repo | `template-skill` |
| `hub-` | An index of other repos | `hub-claude-skills` |

## Versioning of this template

This repo versions itself with the same tools. Its own history is in `CHANGELOG.md`. `scripts/init.py` replaces that file in new repos, so the template's history never carries over.
