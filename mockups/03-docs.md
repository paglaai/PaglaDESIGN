# MOCKUP — Docs

> High-fidelity, token-referenced. One documentation page.

---

# Base

- Paper background; ink text; reading column at `font.maxWidth.body`.
- Three regions at `breakpoint.large`: sidebar (paper), content (paper), right
  TOC (paper, sticky).

---

# Typography

| Element | Token |
| --- | --- |
| Page title | `font.size.h1`, `font.weight.medium` |
| Section headings | `font.size.h2` / `h3`, `font.weight.medium` |
| Prose | `font.size.body`, `font.lineHeight.body` |
| Code | `font.size.code` |
| Sidebar links | `font.size.small`; current = `color.base.ink`, `font.weight.medium` |
| Breadcrumbs | `font.size.small`, muted except current |

---

# Region treatment

## Sidebar

- Hairline right border (`color.base.border`)
- Section labels: `font.tracking.uppercase`, `font.size.caption`, muted
- Items `space.2` apart; groups `space.6` apart; active item has
  `color.accent.primary` left rail + `font.weight.medium`

## Content

- `space.8` between sections; paragraphs `space.4`
- Code Blocks: `color.base.surface` background, hairline border,
  `radius.md`, copy Button ghost
- Terminal: as Code Block with prompt styling
- Breadcrumbs above `h1`

## Context TOC

- Sticky at `space.6`; links muted; current = `color.accent.primary` text,
  no fill
- Collapses into content top below `breakpoint.large`

---

# Components in use

- **Breadcrumbs:** ordered list, separators `color.base.border`, current page
  text (not link)
- **Code Block:** header row (filename/language, `font.size.caption`, muted),
  copy affordance with success confirmation
- **Table (if used):** header `font.weight.semibold`, `color.base.border`
  hairlines, hover row `color.state.hover`

---

# Spacing rhythm

- Sidebar: `space.6` from edge, groups `space.6`
- Content: sections `space.8`, paragraph-to-code `space.4`, code blocks
  `space.6` apart
- Related links at end: `space.6` above, list items `space.2` apart

---

# Dark theme

Standard inversion. Code Blocks `#17171A` surface on `#0A0A0B` paper; hairlines
`#2A2A2E`.

---

# Reduced motion

In-page TOC scrolls natively; active marker updates instantly.
