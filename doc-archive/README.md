# Doc archive

Content that used to be published on `https://hans-blok.github.io/entoli-publish/`
but was removed from the site navigation on 2026-09-06 as part of an
information-architecture cleanup.

This directory is **not** part of the MkDocs `docs_dir` (`doc/`), so nothing
here is built or published. It exists so the underlying material is not lost,
in case any of it is needed again later — either republished as-is or folded
into another page.

- `business-model/` — the full explanatory text of the Business Model and the
  Business Model Canvas, moved here on 2026-09-12. The site still publishes
  both artefacts, but as **visual only**: `doc/business-model/` now contains
  just the two PNGs plus a thin page per visual. These files are the
  authoritative written source and are unchanged; note that their relative
  image links (`business-model-visual.png`, `bmc-visual.png`) resolve against
  `doc/business-model/`, where the images still live.
- `artikelen/` — two standalone articles ("Datamodelleren met Entoli" and
  "Source-regime, Synthesis-regime en Task Mode") and the business-model
  image that used to be embedded on the homepage. Original, non-canonical
  essay content; safe to keep here indefinitely or to re-publish later.
- `codes/classification-register.md` — a **derivative** copy of the
  Classification Register. Its own frontmatter states the authoritative
  source is `foundations/.canonical/general/entoli-concepts.md` in the
  canon repository, not this file. This copy could eventually be deleted
  outright without losing authoritative knowledge, but it is kept here
  rather than deleted outright, out of caution.
- `data-models/` — the former "Datamodellen" section (`index.md` plus
  `ldm-datamodelling.svg`), removed from the site on 2026-09-06 at the
  user's request. Not referenced from anywhere else in the repo.
