# LANDING

> *The landing page walks the visitor from "what is this" to "where do I start" in one calm arc.*

---

# Purpose

The landing template is the home page composition.

It introduces the ecosystem progressively (`../site/SITEMAP.md`) and ends with
one clear next step. It never overwhelms — each section answers one question
before the next begins.

---

# Question it answers

> What is PaglaAI?

---

# Composition

Sections in order, each with its single question:

| # | Section | Question it answers | Building blocks |
| --- | --- | --- | --- |
| 1 | Hero | What is this? | `HERO.md` (marketing variant) |
| 2 | Vision | Why does it exist? | Statement block: overline, `font.size.h2` statement, `font.maxWidth.body` prose |
| 3 | Ecosystem | What is the whole? | List of products or ecosystem map |
| 4 | Products | What can I use today? | Feature Grid (`sections.md`), Cards |
| 5 | Philosophy | How is it built? | three principle Cards in a row |
| 6 | Documentation | Where do I learn? | Card linking into docs, Code Block teaser |
| 7 | Latest updates | Is it alive? | List of recent posts/notes with dates |
| 8 | Community | Where do I go next? | CTA (`sections.md`) |
| 9 | Footer | Where can I find everything? | Footer (`sections.md`) |

---

# Spacing rhythm

- Section gap: `space.16`
- Within a section: headings `space.8` from their content, `space.6` between
  sibling blocks
- Alternate surface rhythm: content sections sit on `color.base.paper`;
  optional raised sections sit on `color.base.surface` — never more than two
  tones in a row
- Full-bleed sections keep inner content inside `layout.maxWidth` with
  `layout.contentPaddingWide`

---

# Content discipline

- One primary heading per section; one idea per heading
- No more than two actions per section; the page ends with exactly one primary
  CTA
- Product Cards link to their product page; they never duplicate the product
  hero content (`../site/CONTENT_STRATEGY.md`)

---

# Responsive

- Feature Grid collapses to one column below `breakpoint.medium`
- The three-philosophy Cards stack below `breakpoint.large`
- Updates List becomes a two-column timeline below `breakpoint.medium`

---

# Behavior

- In-page section links scroll natively; sticky header stays usable
  (`../site/NAVIGATION.md`)
- No section re-animates on scroll; entrances run once
  (`../design-system/UX_PATTERNS.md`)

---

# Relationship to Documents

- Site order — `../site/SITEMAP.md`
- Content — `../site/CONTENT_STRATEGY.md`
- Navigation — `../site/NAVIGATION.md`
- Sections — `sections.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
