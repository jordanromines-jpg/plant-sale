# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [Semantic Versioning](https://semver.org/).

- **MAJOR:** a new sale (a different set of plants) or a change to the page's URL or plant links (`#p<number>`).
- **MINOR:** plants added or removed, or a new page feature.
- **PATCH:** prices, sold/pending status, listing links, copy and photo fixes.

Add an entry under [Unreleased] with every change, then cut releases with `scripts/release.py patch|minor|major`. Each release is tagged `vX.Y.Z` and published as a GitHub Release, with its section here as the notes.

## [Unreleased]

### Changed
- The snail pot (no. 8) and planter box (no. 13) are listed as included.

### Removed
- Estimated pot sizes, which were wrong for most plants; pot sizes now appear only where Jordan gave them.

### Changed
- No. 1 is a Philodendron 'Burle Marx' (Jordan's ID), repriced to $70; no. 3 lists two Florida Beauties at $90 each.
- Every plant now shows the name buyers search for, the scientific name, size, pot, what's included, light, water and pet safety, on the page and in `LISTINGS.md`.
- Repriced the large specimens using sizes measured from the video (hand, can, gallon jug for scale): billietiae $125, giant elephant ear $150, Monstera $125, Mojito $110 and others; total ask $972.
- Added full-plant photos for the billietiae, giant elephant ear, Monstera and Scindapsus 'Dark Form'.
- Repriced all 15 plants for their real sizes (6 to 8 inch pots; the elephant ear is almost 5 ft in a 10 to 12 inch pot): total ask $769.
- No. 10 identified as a highly variegated White Wizard-type Philodendron (cataphylls rule out Monstera); no. 3 copy now notes its variegation; no. 2 renamed Giant elephant ear and featured first.

### Added
- Project scaffold from [template-repo](https://github.com/jordanromines-jpg/template-repo).
- Listing page for 15 plants with photos from the walkthrough video, final prices, care notes and per-plant links (`#p<number>`).
- `plants.js` as the single place to edit prices, status and listing links.
- `LISTINGS.md` paste-ready listings and `tools/make_listings.js` to rebuild them.
- `PRICING.md` with the ID and price reasoning.
