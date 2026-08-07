# MOCKUP — Home

> High-fidelity, token-referenced. Light theme is the default; every surface
> re-resolves under the dark theme via `[data-theme="dark"]`.

---

# Base

- **Background:** `color.base.paper` (`#FFFFFF` light / `#0A0A0B` dark)
- **Text:** `color.base.ink`, hierarchy via `font.weight` and `font.size`
- **Accent:** `color.accent.primary` (`#6B7EFF`) — overline underlines, focus
  rings, the current Timeline dot only. Never a fill (D-004)
- **Surfaces:** `color.base.paper` for content sections, `color.base.surface`
  (`#F5F5F3` / `#17171A`) for the raised bands
- **Borders:** `color.base.border` hairlines (`#E8E8E6` / `#2A2A2E`)

---

# Typography

| Element | Token |
| --- | --- |
| Hero headline | `font.size.display`, `font.weight.light`, `font.tracking.display`, `font.lineHeight.display` |
| Section headings | `font.size.h2`, `font.weight.medium`, `font.tracking.heading` |
| Overline | `font.size.small`, `font.tracking.uppercase`, `color.base.muted` |
| Body | `font.size.body`, `font.maxWidth.body` (65ch), `font.lineHeight.body` |
| Terminal/code | `font.size.code` |

---

# Section surfaces

| Section | Surface | Notes |
| --- | --- | --- |
| Header | paper | sticky, `color.base.border` bottom hairline |
| Hero | paper | centered, `space.16`–`space.24` vertical |
| Vision | paper | prose centered under 65ch |
| Ecosystem | `surface` | full-width band, inner content `layout.maxWidth` |
| Products | paper | Feature Grid, Cards on paper with border |
| Philosophy | paper | 3 Cards, border |
| Documentation | `surface` | Code Block on `color.base.surface`, border |
| Updates | paper | List, dates `color.base.muted` |
| Community | paper | CTA, centered |
| Footer | paper | top hairline, muted links |

---

# Components in use

- **Buttons:** primary = `color.accent.primary` text + border, paper background;
  ghost = transparent. No filled accent (D-004)
- **Terminal:** border hairline, prompt `color.accent.primary`, output ink,
  `radius.md`
- **Feature Cards:** `radius.md`, `space.4` padding, icon at `icon.md`
- **Chips (if used):** `radius.sm`, selected shown with a check + border

---

# Spacing rhythm

- Section gap `space.16`; heading-to-content `space.8`; card-internal `space.4`
- Raised bands get inner padding `space.16`
- All content inside `layout.maxWidth` + `layout.contentPaddingWide`

---

# Dark theme

Same semantics, inverted values: paper ↔ ink, surface `#17171A`, border
`#2A2A2E`, muted `#9AA0AE`. Accent family unchanged. Contrast baseline holds
(`../design-system/ACCESSIBILITY.md`).

---

# Reduced motion

All entrances resolve to `motion.reduced` (`0ms`). No scroll reveals.
