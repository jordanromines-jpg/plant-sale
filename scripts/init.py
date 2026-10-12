#!/usr/bin/env python3
"""One-time setup for a repo created from this template. Run it right after "Use this template":

  scripts/init.py "Project name" ["One-line description"]

It writes a fresh README.md, CHANGELOG.md (starting at [Unreleased]) and VERSION 0.0.0, so the
template's own history doesn't carry over, then deletes itself. The first
`scripts/release.py minor` makes v0.1.0.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = "template-repo"
TEMPLATE_LINK = f"[{TEMPLATE}](https://github.com/jordanromines-jpg/{TEMPLATE})"

README = "# {name}\n\nOne sentence: what this is and who it's for.\n\n## Quick start\n\n```bash\n# the fewest commands that get someone from clone to working\n```\n\n## How it works\n\nA short description of the moving parts, and where each lives.\n\n## Development\n\n```bash\n# set up, run, test\n```\n\n## Plans\n\nPlans for this repo live in [`plans/`](plans/README.md), kept as a graph with [plangraph](https://github.com/jordanromines-jpg/plugin-plangraph), which `.claude/settings.json` enables for every Claude Code session here. Start one with `/plangraph:plan`; see where things stand with `/plangraph:plan-status` or `plangraph serve`.\n\n## Versioning and releases\n\nThe version is in [`VERSION`](VERSION), and the history is in [`CHANGELOG.md`](CHANGELOG.md).\n\n1. Every change adds a line under `## [Unreleased]` in the changelog.\n2. To release, run `scripts/release.py patch|minor|major`. Add `--dry-run` to preview first.\n\nThe release script bumps `VERSION`, moves the Unreleased notes into a dated section, tags `vX.Y.Z`, pushes, and publishes a GitHub Release with those notes.\n- **Build steps:** if `scripts/build-release.sh` exists, it runs after the release commit, and anything it changes is committed before tagging.\n- **Attachments:** files listed in `.release-assets` are attached to the GitHub Release.\n\n---\nCreated from {template_link}.\n"

CHANGELOG = '# Changelog\n\nFormat: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning](https://semver.org/).\n\n<!-- Replace these definitions with what MAJOR, MINOR and PATCH mean for this repo, then delete this comment. -->\n- **MAJOR:** a breaking change for users of this repo (removed or renamed commands, flags, files, fields or APIs).\n- **MINOR:** new functionality that is backwards compatible.\n- **PATCH:** bug fixes and docs, with no change in behaviour.\n\nAdd an entry under [Unreleased] with every change, then cut releases with `scripts/release.py patch|minor|major`. Each release is tagged `vX.Y.Z` and published as a GitHub Release, with its section here as the notes.\n\n## [Unreleased]\n\n### Added\n- Project scaffold from {template_link}.\n'


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    name = sys.argv[1]
    readme = README.format(name=name, template_link=TEMPLATE_LINK)
    if len(sys.argv) > 2:
        readme = readme.replace("One sentence: what this is and who it's for.", sys.argv[2])
    (ROOT / "README.md").write_text(readme)
    (ROOT / "CHANGELOG.md").write_text(CHANGELOG.format(template_link=TEMPLATE_LINK))
    (ROOT / "VERSION").write_text("0.0.0\n")
    for extra in EXTRA_RESET:
        extra(ROOT, name)
    Path(__file__).unlink()
    print(f"Initialised {name!r}. Review the files, commit, and fill in the MAJOR/MINOR/PATCH definitions in CHANGELOG.md.")
    subprocess.run(["git", "status", "--short"], cwd=ROOT)


def reset_plans(root: Path, name: str) -> None:
    """A new repo starts with no plans: an empty graph and a fresh plans changelog."""
    graph = root / "plans" / "graph"
    for f in graph.glob("*/*.json"):
        f.unlink()
    (root / "plans" / "CHANGELOG.md").write_text(
        "# Plans changelog\n\nOne line per change to any plan, newest first, in the same commit as the change.\n"
    )


EXTRA_RESET = [reset_plans]

if __name__ == "__main__":
    main()
