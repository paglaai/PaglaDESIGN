# SECTIONS

> *Sections are the repeatable mid-level compositions every template shares.*

---

# Purpose

SECTIONS documents the reusable section-level compositions: Feature Grid, CTA,
Timeline, and Footer.

They are not components (they have no single role or state set) and not
templates (they are not full pages). They are the shared mid-level building
blocks used across `landing.md`, `product.md`, `blog.md`, and `case-study.md`.

---

# Feature Grid

A grid of Cards that each carry one capability or fact.

- **Structure:** overline (optional), heading, grid of Cards — each Card has an
  optional icon, a name, and a one-line description
- **Columns:** 2 at `breakpoint.small`+, 3 at `breakpoint.large`+, 1 below
  `breakpoint.small`
- **Spacing:** `space.6` between Cards; `space.4` within a Card between icon,
  name, and line
- **Behavior:** Cards are plain unless the grid links out; interactive Cards
  are keyboard-focusable with one action each
- **Icon discipline:** icons come from `../design-system/ICONS.md` at `icon.md`;
  they carry meaning, never decoration

---

# CTA

A single-idea closing block that ends a page or a major section.

- **Structure:** one `font.size.h2` statement, one sentence of context, one
  primary Button; a secondary ghost link only when genuinely useful
- **Spacing:** `space.16` above and below; centered, content inside
  `font.maxWidth.body`
- **Surface:** paper or surface, matching the section it closes — never a new
  bright color
- **Behavior:** exactly one primary action
  (`../site/CONTENT_STRATEGY.md`); the whole block is not a button, only the
  Button is

---

# Timeline

A chronological sequence for roadmaps and history.

- **Structure:** a date rail and a content rail; each row is a date, a heading,
  and one line
- **Spacing:** `space.8` between rows; date rail `space.6` from content
- **Behavior:** purely informational, never interactive; no auto-play, no
  scroll-jacking (`../design-system/MOTION.md`)
- **Markers:** the rail uses a token hairline and `color.accent.primary` dots
  for the current moment only — meaning, not decoration (D-004)

---

# Footer

The closing navigation composition.

- **Structure:** product links, documentation links, GitHub/BrandKit/Blog/About,
  legal links (Privacy, License), and the wordmark
- **Columns:** 4 at `breakpoint.large`+, collapsing to stacked groups below
  `breakpoint.medium`
- **Spacing:** `space.16` above; `space.4` between link groups; `space.2`
  between links
- **Behavior:** links are standard, descriptive anchors
  (`../design-system/ACCESSIBILITY.md`); the footer repeats primary destinations
  but never hides them from the header

---

# Relationship to Documents

- Templates that use these — `landing.md`, `product.md`, `blog.md`,
  `case-study.md`
- Components — `../components/COMPONENT_LIBRARY.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
- Navigation — `../site/NAVIGATION.md`
