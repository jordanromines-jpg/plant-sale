# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning](https://semver.org/).

These versions cover the template itself.
- **MAJOR:** a breaking change to `release.py` or `init.py` usage, or to the file conventions repos rely on.
- **MINOR:** a new scaffold file or script capability.
- **PATCH:** fixes and wording.

Releases are cut with `scripts/release.py`.

## [Unreleased]

## [1.4.0] - 2026-10-11

### Added
- "How we work with Jordan" in `CLAUDE.md` (every session loads it) and `plans/README.md`: one voice, keyed tables
  with a recommendation answered by key or "all rec", status as pull requests with their keys, gates are his, new work
  waits for his go, files first, mistakes said plainly, no agents unless he asks (Jordan, 11 Oct 2026).
- `plans/README.md` has a roadmap block (Now / Next / Later / Done, from plangraph 0.3). Install plangraph 0.3
  or later first: older versions don't know the view.

## [1.3.0] - 2026-10-11

### Added
- Planning built in: `plans/` with a README (how plans are written and moved, with a generated index),
  `CHANGELOG.md`, `plangraph.json` (required sections, line limit), and empty `graph/` and `archive/` folders, for the
  [plangraph](https://github.com/jordanromines-jpg/plugin-plangraph) plugin.
- `.claude/settings.json` declares the plangraph marketplace (`plugin-dist` branch) and enables the plugin, so every
  repo made from this template has it in Claude Code.
- `CLAUDE.md`: the planning rules. The generated README gets a Plans section; `init.py` starts the new repo with an
  empty graph and a fresh plans changelog.

## [1.2.1] - 2026-10-10

### Changed
- `release.py` also looks for the build hook at `tools/build-release.sh`, for repos that keep their tooling in `tools/` (for example plugin-chart-advisor).

## [1.2.0] - 2026-10-10

### Added
- README → Naming: the type-prefix convention for repo names.

### Changed
- The repo is renamed `repo-template` → `template-repo`. Links and examples use the new names (`tool-my-thing`). GitHub redirects the old URLs.

## [1.1.0] - 2026-10-10

### Added
- `release.py --trailer TEXT` (repeatable) adds commit trailers, such as `Co-Authored-By`, to the release and build commits.

## [1.0.0] - 2026-10-10

### Added
- `scripts/release.py`: SemVer bump; it moves `[Unreleased]` into a dated section, updates compare links, commits, tags, pushes, and publishes a GitHub Release with the section as notes.
  - Optional `scripts/build-release.sh` hook; its output is committed before tagging.
  - Optional `.release-assets` attachments.
  - Before starting it checks: on the default branch, clean tree, in sync with origin, Unreleased not empty, tag free.
  - `--dry-run` previews without changing anything.
- `scripts/init.py`: one-time setup of a new repo, writing a fresh README, CHANGELOG and VERSION 0.0.0, then deleting itself.
- `CLAUDE.md` with changelog, release and secrets conventions for Claude sessions.
- `.gitignore`, and a README that documents the template.

[Unreleased]: https://github.com/jordanromines-jpg/template-repo/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/jordanromines-jpg/template-repo/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/jordanromines-jpg/template-repo/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/jordanromines-jpg/template-repo/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/jordanromines-jpg/template-repo/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jordanromines-jpg/template-repo/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jordanromines-jpg/template-repo/releases/tag/v1.0.0
