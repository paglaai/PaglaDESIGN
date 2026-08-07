# BLOG

> *The blog documents progress. Transparency, not marketing.*

---

# Purpose

The blog template composes the article index and the article page.

It presents development logs, release notes, design and engineering articles,
and research notes honestly (`../site/CONTENT_STRATEGY.md`).

---

# Questions it answers

- Index: > What is happening?
- Article: > What was learned or shipped?

---

# Composition

## Index

| Section | Building blocks |
| --- | --- |
| Hero | `HERO.md` (article variant) — overline, headline, summary |
| Filter | Chip row — all posts, by type (development log, release notes, research) |
| Post list | List of Cards: title, summary, type, date, read time |
| Paging | Menu or List of numbered links; never infinite auto-load |

## Article

| Section | Building blocks |
| --- | --- |
| Hero | Overline (type + date), headline, summary, author/read time |
| Body | Prose at `font.maxWidth.body`, Code Blocks, Tables, headings |
| In-page nav | Right TOC at `breakpoint.large` (as in `docs.md`) |
| Related | List of two related posts |
| Next step | CTA — "Read the next post" or "See the release" |

---

# Content discipline

- Dates are honest; release notes state versions
- Code in articles is real and copyable
- One primary idea per post; the summary carries it before the body expands
  (`../site/CONTENT_STRATEGY.md`)

---

# Spacing rhythm

- Index Cards: `space.6` between items, `space.4` between title, summary, and
  meta within a Card
- Article body uses the docs prose rhythm: `space.8` between major sections,
  `space.4` between paragraph and code

---

# Responsive

- Filter Chips wrap, never scroll horizontally
- Article body takes the full column below `breakpoint.large`; the TOC collapses
- Cards become a single column below `breakpoint.medium`

---

# Behavior

- Chips filter the visible list and are announced; selection is shown beyond
  color
- Article links scroll natively; nothing re-animates on scroll
  (`../design-system/UX_PATTERNS.md`)

---

# Relationship to Documents

- Content types — `../site/CONTENT_STRATEGY.md`
- Structure — `../site/SITEMAP.md`
- Components — `../components/COMPONENT_LIBRARY.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
