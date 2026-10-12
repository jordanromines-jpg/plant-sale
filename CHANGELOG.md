# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning](https://semver.org/).

- **MAJOR:** a new sale (a different set of plants) or a change to the page's URL or plant links (`#p<number>`).
- **MINOR:** plants added or removed, or a new page feature.
- **PATCH:** prices, sold/pending status, listing links, copy and photo fixes.

Add an entry under [Unreleased] with every change, then cut releases with `scripts/release.py patch|minor|major`. Each release is tagged `vX.Y.Z` and published as a GitHub Release, with its section here as the notes.

## [Unreleased]

### Added
- Project scaffold from [template-repo](https://github.com/jordanromines-jpg/template-repo).
- Listing page for 15 plants with photos from the walkthrough video, final prices, care notes and per-plant links (`#p<number>`).
- `plants.js` as the single place to edit prices, status and listing links.
- `LISTINGS.md` paste-ready listings and `tools/make_listings.js` to rebuild them.
- `PRICING.md` with the ID and price reasoning.
