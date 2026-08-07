# MOCKUP — Product (PaglaMLX)

> High-fidelity, token-referenced. First instantiation: PaglaMLX.

---

# Base

- Same base as `01-home.md`: paper background, ink text, accent for meaning only.
- Raised bands alternate paper / `color.base.surface`.

---

# Typography

| Element | Token |
| --- | --- |
| Product headline | `font.size.display`, `font.weight.light`, `font.tracking.display` |
| Section headings | `font.size.h2`, `font.weight.medium` |
| Feature names | `font.weight.semibold` at `font.size.body` |
| Feature lines | `font.size.body`, `color.base.muted` |
| Meta/labels | `font.size.small`, `color.base.muted` |

---

# Section surfaces

| Section | Surface | Notes |
| --- | --- | --- |
| Breadcrumbs | paper | links muted, current `color.base.ink` text |
| Hero | paper | two-column grid at `breakpoint.large` |
| Overview | paper | prose, left-aligned, 65ch |
| Problem | `surface` | pains List, muted markers |
| Solution | paper | prose + Feature Grid (2 col) |
| Key Features | paper | Feature Grid (3 col) |
| Architecture | paper | layer List, border hairline separators |
| Documentation | `surface` | Code Block (install) + Card |
| Downloads | paper | List with per-row Button (ghost) |
| Roadmap | paper | Timeline, current dot `color.accent.primary` |
| FAQ | paper | Tabs, underline variant |
| Next step | paper | centered CTA |
| Footer | paper | top hairline |

---

# Components in use

- **Terminal (hero):** border hairline, `radius.md`, prompt `color.accent.primary`,
  real install + run output at `font.size.code`
- **Code Block:** copy affordance, confirmation in `color.accent.success`
- **Tabs (FAQ):** underline variant; active tab underline
  `color.accent.primary`; panel prose 65ch
- **Timeline:** date rail `color.base.muted`, hairline rail, current marker dot
  `color.accent.primary`

---

# Spacing rhythm

- Section gap `space.16`; hero content `space.16`–`space.24`
- Feature Grid: `space.6` between Cards, `space.4` internal
- FAQ Tabs `space.6` above panel, panel prose `space.4` paragraphs

---

# Dark theme

Value inversion per `DESIGN_TOKENS.md` dark table. Terminal and Code Blocks
invert too — border `#2A2A2E`, surface `#17171A`, ink `#F5F5F3`.

---

# Reduced motion

Tabs switch instantly or at `motion.duration.fast`; reduced-motion users get
instant switch with announced state.
