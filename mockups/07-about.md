# MOCKUP — About

> High-fidelity, token-referenced. Who is behind the ecosystem, honestly.

---

# Base

- Paper background, ink text. Generous vertical whitespace throughout — it is
  the design (`../design-system/DESIGN_TOKENS.md`, spacing doctrine).

---

# Typography

| Element | Token |
| --- | --- |
| Page title | `font.size.h1`, `font.weight.medium` |
| Section headings | `font.size.h2`, `font.weight.medium` |
| Value card titles | `font.size.h4`, `font.weight.semibold` |
| Prose | `font.size.body`, 65ch, `font.lineHeight.body` |
| Timeline dates | `font.size.small`, `color.base.muted` |

---

# Region treatment

## Hero

- Left-aligned; overline `font.tracking.uppercase`, muted

## Mission

- Single prose block, left-aligned under 65ch; `space.8` paragraph rhythm

## The Architect

- Prose + a List; keep it authentic
  (`../site/CONTENT_STRATEGY.md`)

## Values

- 3 Cards, `radius.md`, hairline, `space.6` apart at `breakpoint.large`;
  stack below `breakpoint.medium`
- Value names at `h4`; one line each

## Timeline

- Date rail `color.base.muted`; content rail milestone + one line
- Hairline rail; only the current moment dot is `color.accent.primary`
- `space.8` between rows

## Contact

- List: email · GitHub · community, muted labels
- Or a single CTA Button if one channel is primary

---

# Components in use

- **Card:** plain
- **Timeline:** informational; `../templates/sections.md`
- **List:** contact channels

---

# Spacing rhythm

- Section gap `space.16`
- Mission and Architect `space.8` internal
- Values `space.6` between Cards; Timeline rows `space.8`
- Contact `space.4` between rows

---

# Dark theme

Standard inversion; timeline rail `#2A2A2E`; current dot accent unchanged.

---

# Reduced motion

No reveals; timeline static.
