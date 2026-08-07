# NAVIGATION

> *Navigation answers three questions at every moment: Where am I? What can I do here? Where can I go next?*

---

# Purpose

NAVIGATION defines how users move through the PaglaAI ecosystem — the site and,
by extension, every product surface that inherits this system.

It is the behavioral counterpart to `SITEMAP.md`.

- `SITEMAP.md` defines the structure.
- `NAVIGATION.md` defines how users move within it.

The goals are predictability and calm: users should never have to learn a new
navigation model when they switch products.

---

# Navigation Model

The site uses a single, stable model with three layers:

```
Primary        — the top-level destinations, always visible
Secondary      — context-specific routes within a section
Utility        — search, theme, and account or product-level actions
```

Each layer has one job. A link belongs to exactly one layer.

---

# Primary Navigation

The primary navigation mirrors `SITEMAP.md` and stays intentionally small:

```
Home · Products · Documentation · BrandKit · Philosophy · Blog · About
```

Rules:

- The primary list changes only when a major ecosystem area is added.
- It is identical on every page — location changes, list does not.
- New products do not extend the list; they live under **Products**.
- One item is the current location and is marked as such (see States).

---

# Secondary Navigation

Secondary navigation exposes the structure of the current section.

Examples:

- **Products** — PaglaMLX, PaglaCPP, PaglaROUTER, PaglaAPI, PaglaGPT, PaglaOS
- **Documentation** — Getting Started, Guides, Tutorials, API Reference,
  Architecture, FAQ

Rules:

- Secondary navigation appears only where the section has depth.
- It reflects the section structure exactly — the map and the territory agree.
- On documentation surfaces it may become a persistent in-page sidebar
  (see In-Page Navigation).

---

# Utility Navigation

Utility actions sit apart from content routes:

- **Search** — the fastest path for returning users (`USER_JOURNEYS.md`)
- **Theme** — light / dark toggle
- **GitHub** — the repository as a destination

Utility actions are few. If a utility competes with a primary link, it is not a
utility.

---

# In-Page Navigation

Long documents use a table of contents that mirrors their headings.

Rules:

- The in-page list is generated from the heading hierarchy, not hand-curated.
- It is one level deep by default; deeper levels only when the document
  requires them.
- The current heading is marked as the reader scrolls (see States).
- Related documents are linked at the end — never a dead end
  (`DOCUMENTATION_STYLE.md`).

---

# Breadcrumbs

Breadcrumbs appear on pages deeper than two levels from the root.

Format follows the structure, never invents it:

```
Home › Documentation › API Reference
```

Rules:

- The last item is the current page and is not a link.
- Breadcrumbs never replace the heading; they confirm location.
- They are optional on pages reachable in one step from primary navigation.

---

# Footer Navigation

The footer mirrors the primary destinations and adds the legal and license set:

```
Products · Documentation · BrandKit · Blog · About · GitHub · Privacy · License
```

The footer is a fallback, not a second navigation model. It never contains
routes the primary navigation hides.

---

# States

Every navigation element communicates its state.

- **Current** — the item naming the page you are on is marked, by type weight
  and position, never by color alone.
- **Hover** — the item responds within `motion.duration.fast`, subtly.
- **Focus** — the item shows the shared focus indicator
  (`../design-system/ACCESSIBILITY.md`).
- **Active** — the press registers immediately.
- **Disabled** — only when the destination genuinely does not exist.

The current-location marker uses typography first, per the color discipline
(`../design-system/COLOR_SYSTEM.md`): weight and placement, reinforced by
`color.state.active`, never color alone.

---

# Mobile and Responsive Behavior

The navigation model is the same at every breakpoint
(`../design-system/DESIGN_TOKENS.md`); the presentation changes.

- **Primary** — collapses to a menu below `breakpoint.medium`. The menu uses
  the Menu component (`../components/COMPONENT_LIBRARY.md`).
- **Secondary** — becomes an accordion or a filter above the content.
- **In-page** — collapses to a heading, expandable on demand.
- **Breadcrumbs** — the deepest level remains visible; ancestors truncate
  without breaking the format.

At every size, the three questions remain answerable:
where am I, what can I do here, where can I go next.

---

# Accessibility

Navigation is held to the baseline (`../design-system/ACCESSIBILITY.md`):

- Landmarks are semantic: `header`, `nav`, `main`, `footer`.
- One primary `nav` landmark; secondary sections use `aria-label`s.
- The current location is announced, not implied.
- Focus order follows visual order; the mobile menu traps focus while open and
  releases it on close.
- The skip link jumps straight to main content.
- Link text describes the destination; it never says "click here".

---

# Search as Navigation

Search is navigation for returning users (`USER_JOURNEYS.md`).

- Search is reachable from every page.
- Results surface the destination and where it lives in the structure.
- A result carries the context that explains it, so the reader can decide
  without guessing.

---

# Relationship to Documents

- Structure — `SITEMAP.md`
- Journeys — `USER_JOURNEYS.md`
- Content and voice — `CONTENT_STRATEGY.md`
- Components used — `../components/COMPONENT_LIBRARY.md`
- Values — `../design-system/DESIGN_TOKENS.md`
- Decision history — `../governance/DECISIONS.md`

---

# Final Principle

> *Good navigation is invisible. Users notice it only when it fails.*
