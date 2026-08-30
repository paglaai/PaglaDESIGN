# WIREFRAME — Footer (OpenAI-scale)

> Structural only. Visual tokens are decided by the mockup.

---

# Question it answers

> Where do I go next when the page ends?

---

# Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ FOOTER  surface: paper, border-top: hairline `color.base.border`              │
│                                                                              │
│   GRID — 5 cols @ ≥64rem, 2 cols @ ≥48rem, 1 col @ <40rem                    │
│   gap: `space.8`  ·  padding-block: `space.16` top / `space.8` bottom         │
│                                                                              │
│   COL 1 — Research                                                           │
│     subhead: Research                                                        │
│       Research Index · Research Overview · Color & Tokens                    │
│     subhead: Latest Advancements                                             │
│       PaglaDESIGN v1.7 · v1.6 · v1.0                                          │
│     subhead: Safety                                                          │
│       Accessibility · Motion Safety · Security & Privacy · Trust             │
│                                                                              │
│   COL 2 — Products                                                           │
│     subhead: Products                                                        │
│       PaglaCHAT ↗ · PaglaMLX ↗ · PaglaROUTER ↗ · PaglaDESIGN ↗ · PaglaCPP   │
│       Release Notes                                                          │
│     subhead: API Platform                                                    │
│       Overview · API Reference ↗ · BrandKit · Docs ↗                         │
│                                                                              │
│   COL 3 — Developers / Business                                              │
│     subhead: Developers                                                      │
│       Docs ↗ · API Reference · Design Tokens ↗ · Resources ↗ · Forum ↗       │
│     subhead: Business                                                        │
│       Overview · Solutions · Resources · Customer Stories · Contact Sales    │
│                                                                              │
│   COL 4 — Company                                                            │
│     subhead: Company                                                         │
│       About Us · Our Charter · Careers · News                                │
│     subhead: Support                                                         │
│       Help Center ↗                                                          │
│                                                                              │
│   COL 5 — More                                                               │
│     subhead: More                                                            │
│       Stories · Academy · GitHub · Sitemap · Podcast · RSS                   │
│     subhead: Terms & Policies                                                │
│       Terms of Use · Privacy Policy · Other Policies                         │
│                                                                              │
│   ───────────────── hairline `color.base.border` ─────────────────           │
│                                                                              │
│   BOTTOM BAR — flex wrap, justify-between, align-center, gap `space.4`        │
│     LEFT: [social icons 16px, 5 items]  X · LinkedIn · YouTube · GitHub ·    │
│           Discord · each 44×44 target, `interactive.minTarget`, hover        │
│           `color.base-ink` + `color.state.hover` border                      │
│     CENTER: PaglaAI © 2015–2026  Manage Cookies (link)                        │
│     RIGHT: [locale pill]  `English  United States`  `color.base.surface` bg, │
│            `color.base.border`, `radius.pill`, `space.2`/`space.4` pad        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

# Region table

| Region | Composition | Purpose |
| --- | --- | --- |
| Grid | `footer-grid` 5→2→1 responsive | expose every destination without scrolling |
| Subhead | `footer-col__subhead` uppercase, `font.tracking.uppercase`, `color.base.muted` | section label, not a link |
| List | `footer-col__list` + `footer-col__link` | secondary navigation, `font.size.small`, `color.base.muted` → `ink` on hover+underline |
| Bottom bar | `footer-bottom` + `footer-social` + `footer-locale` | utility, social proof, locale |

---

# Responsive notes

- Grid collapses 5 → 2 → 1; gap holds at `space.8`
- Social icons stay 44×44 minimum target; locale pill wraps below on <48rem
- No new breakpoints; uses existing `breakpoint.medium` (48rem) and large (64rem)
- Reduced motion: no animation

---

# Accessibility

- Column subheads are `<p>` with `font.tracking.uppercase` — not headings to avoid outline inflation; real `<h2>` would be "Footer navigation" landmark
- Social links have `aria-label` ("GitHub", "X", etc.) + `aria-hidden` on icons
- Locale pill has `role="status"` + `aria-label="Language and region"`
- External links use `↗` visual only; `aria-label` adds context where needed
