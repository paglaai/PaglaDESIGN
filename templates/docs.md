# DOCS

> *Documentation is a first-class deliverable, not an afterthought.*

---

# Purpose

The docs template composes a documentation page: orientation, progressive
learning, readable code, and a forward path.

It follows the learning path of `../site/SITEMAP.md`: Introduction →
Installation → Quick Start → Concepts → Guides → API → Examples → FAQ.

---

# Question it answers

> How do I use it?

---

# Anatomy

Three-column orientation on wide screens, collapsing with the content:

| Region | Contents |
| --- | --- |
| Sidebar (left) | Table of contents for the section, current page marked |
| Content (center) | Prose, Code Blocks, Tables, Tabs, Breadcrumbs, in-page nav |
| Context (right, optional) | In-page table of contents — appears at `breakpoint.large` |

---

# Composition

## Prose

- Reading column bounded by `font.maxWidth.body` (`65ch`) inside the content
  region
- Headings are honest and sequential; one accurate top-level heading per page
  (`../governance/DOCUMENTATION_STYLE.md`)
- Code is styled distinctly from prose at `font.size.code`

## Code

- Install and quick-start commands use the Code Block component with a copy
  affordance
- Long lines scroll horizontally; blocks never wrap by default
- Where a command produces real output, the Terminal component shows it
  faithfully

## Navigation

- Breadcrumbs anchor the user in the tree (`../site/NAVIGATION.md`)
- The current page is marked in the sidebar and in Breadcrumbs as text, not a
  link
- Related pages are linked at the end of every article — no dead ends

---

# Spacing rhythm

- Sidebar: `space.6` from viewport edge, items `space.2` apart, section groups
  `space.6` apart
- Content: `space.8` between major sections, `space.4` between paragraph and its
  code block
- Right TOC: sticky at `space.6` from the top of the viewport; does not fight
  the reading column

---

# Responsive

- Below `breakpoint.large`: the right TOC collapses into the content top
- Below `breakpoint.medium`: the sidebar becomes a Menu trigger; the content
  region takes the full column
- Breadcrumbs truncate to the two nearest levels on small screens

---

# Behavior

- In-page TOC links scroll natively and mark position with `color.accent.primary`
- Sidebar active state is shown beyond color (`../design-system/ACCESSIBILITY.md`)
- Code copy confirms visibly; nothing else animates
  (`../design-system/UX_PATTERNS.md`)

---

# Relationship to Documents

- Learning path — `../site/SITEMAP.md`, `../site/CONTENT_STRATEGY.md`
- Documentation style — `../governance/DOCUMENTATION_STYLE.md`
- Navigation — `../site/NAVIGATION.md`
- Components — `../components/COMPONENT_LIBRARY.md`
- Tokens — `../design-system/DESIGN_TOKENS.md`
