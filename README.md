# Sunroom Plant Sale

Listing page for 15 houseplants, served from GitHub Pages and linked from Marketplace listings.

A one-page listing site for 15 houseplants, served from GitHub Pages at
https://jordanromines-jpg.github.io/plant-sale/. Each Marketplace, Craigslist or OfferUp listing links to its plant
with `#p<number>`, e.g. `…/plant-sale/#p6`.

## Update the sale

Everything buyers see comes from `plants.js`. Each plant has `name` (what buyers search for), `sci` (scientific
name), `size`, `pot`, `includes`, `light`, `water`, `pets` and `count`; blank fields are left off the page.


- **Price:** change `price` (and `unit: "each"` for per-item prices).
- **Sold or pending:** add `status: "sold"` or `status: "pending"` to the plant.
- **Listing links:** paste the URL into `links.fb`, `links.cl`, `links.ou` or `links.other`. A Facebook link turns into
  a "Message me on Marketplace" button.
- **Pickup area:** `SALE.pickup`. Bump `SALE.updated` when you change anything.

Then rebuild the paste-ready copy with `node tools/make_listings.js` and commit. Pages redeploys in about a minute.

## Files

- `index.html` – the page (no build step, no dependencies).
- `plants.js` – plant data, prices and copy.
- `LISTINGS.md` – title, price and description for every plant, ready to paste.
- `PRICING.md` – how each ID and price was decided.
- `img/` (540px) and `full/` (full resolution) – stills from the walkthrough video, colour-corrected from iPhone HDR.

## Plans

Plans for this repo live in [`plans/`](plans/README.md), kept as a graph with [plangraph](https://github.com/jordanromines-jpg/plugin-plangraph), which `.claude/settings.json` enables for every Claude Code session here. Start one with `/plangraph:plan`; see where things stand with `/plangraph:plan-status` or `plangraph serve`.

## Versioning and releases

The version is in [`VERSION`](VERSION), and the history is in [`CHANGELOG.md`](CHANGELOG.md).

1. Every change adds a line under `## [Unreleased]` in the changelog.
2. To release, run `scripts/release.py patch|minor|major`. Add `--dry-run` to preview first.

The release script bumps `VERSION`, moves the Unreleased notes into a dated section, tags `vX.Y.Z`, pushes, and publishes a GitHub Release with those notes.
- **Build steps:** if `scripts/build-release.sh` exists, it runs after the release commit, and anything it changes is committed before tagging.
- **Attachments:** files listed in `.release-assets` are attached to the GitHub Release.

---
Created from [template-repo](https://github.com/jordanromines-jpg/template-repo).
